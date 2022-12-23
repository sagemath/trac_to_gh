# Issue 501: more memory leaks in basic arithmetic

Issue created by migration from https://trac.sagemath.org/ticket/501

Original creator: was

Original creation time: 2007-08-28 19:53:02

Assignee: somebody

These are all from Ifti:


The original code at

http://www.sagemath.org:9002/sage_trac/ticket/274


```
sage: get_memory_usage()
'276M'
sage: K = GF(10007^2, 'a')
sage: X = PolynomialRing(K, 'x').gen()
sage: for i in range(1000):
   s = K.random_element(); t = K.random_element()
   poly = s + t*X
....:
sage: get_memory_usage()
'281M'
```


now only leaks about 0.1MB, but extending the for loop range from 10**3
to 10**5 leaks about 6.3MB!

Also the following code


```
def Supercomp():
   p=ZZ(10**5).next_prime()
   szfilename = "timings100k.txt"
   mem_szfilename = "memory100k.txt"
   while true:
       t = cputime()
       M = get_memory_usage()
       X = SupersingularModule(p)
       X.hecke_matrix(2)
       f = open(szfilename, 'a')
       f.write(str([p, cputime(t)]) + ", ")
       f.close()
       g = open(mem_szfilename, 'a')
       g.write(str([p, get_memory_usage()-M]) + ", ")
       g.close()
       X.save('X' + str(p))
       p = ZZ(p).next_prime()

Supercomp()
```


had consumed 20% of memory on sage.math after a day of computation and I
had to kill it.

### PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
24320 burhanud  39  19 12.2g  11g  15m R  100 18.9   1453:36 sage-ipython
### I'll have to spend some time to pin down where the leaks are.

Regards,
Ifti



---

Comment by was created at 2007-08-29 01:01:16

Some of this is caused by __repr__ in ntl.pyx.  Demo code:


```
ntl.set_modulus(ntl.ZZ(20)) 
f = ntl.ZZ_pX(range(10000))
t = get_memory_usage()
for i in range(100):
    s = str(f)
print get_memory_usage(t)
///
big bad number
```


The fix is to change the repr methods to look like this:


```
    def __repr__(self):
        cdef char* s = ZZ_pX_repr(self.x)
        t = str(s)
        free(s)
        return t
```


*except* that we must use C++'s delete rather than malloc's free here.


---

Comment by mabshoff created at 2007-08-29 11:28:01

The biggest problem is in the ntl wrapper:

```
==22784== 791,674 bytes in 65,421 blocks are definitely lost in loss record 2,472 of 2,481
==22784==    at 0x4A05CB9: operator new[](unsigned long) (vg_replace_malloc.c:199)
==22784==    by 0x9280247: ZZ_pX_repr (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libcsage.so.0.0.0)
==22784==    by 0x176D6D57: __pyx_f_3ntl_9ntl_ZZ_pX___repr__ (ntl.c:6216)
==22784==    by 0x443C61: _PyObject_Str (object.c:406)
==22784==    by 0x443D0A: PyObject_Str (object.c:426)
==22784==    by 0x44EA8F: string_new (stringobject.c:3892)
==22784==    by 0x45A272: type_call (typeobject.c:422)
==22784==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==22784==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==22784==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==22784==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==22784==    by 0x4CFF37: function_call (funcobject.c:517)
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 11:18:01

Changing assignee from somebody to mabshoff.


---

Comment by mabshoff created at 2007-08-30 11:18:01

Changing component from basic arithmetic to memleak.


---

Comment by mabshoff created at 2007-08-30 16:36:24

Hello,

I looked at the first bit of code with 2.8.3rc3:

```
sage: get_memory_usage()
577.2734375
sage: K = GF(10007^2, 'a')
sage: X = PolynomialRing(K, 'x').gen()
sage: for i in range(10**5):
....:        s = K.random_element(); t = K.random_element()
....:    poly = s + t*X
....:
sage: get_memory_usage()
581.1953125
sage: for i in range(10**5):
   s = K.random_element(); t = K.random_element()
   poly = s + t*X
....:
sage: get_memory_usage()
581.63671875
sage: for i in range(10**5):
   s = K.random_element(); t = K.random_element()
   poly = s + t*X
....:
sage: get_memory_usage()
581.63671875
sage: for i in range(10**5):
   s = K.random_element(); t = K.random_element()
   poly = s + t*X
....:
sage: get_memory_usage()
581.63671875
```

Notice that the RAM consumption grows by 6 MB after the first round and then a little bit after the second. After that the RAM consumption stays consistent. The reason for the initial growth is python internal, so there is little we can do short term. I am planning to look into this in the long term, but there are still "low hanging fruits" memleak-wise in sage to fix.

I am about to revisit the second computation. Stay tuned.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 20:13:10

And the other half passes Valgrind, too:

```
sage: def Supercomp():
....:        p=ZZ(10**5).next_prime()
....:    for i in range(4):
....:          print(i)
....:      print get_memory_usage()
....:      t = cputime()
....:      X = SupersingularModule(p)
....:      X.hecke_matrix(2)
....:      p = ZZ(p).next_prime()
....:      print get_memory_usage()
....:
sage: Supercomp(); quit
0
741.2421875
764.8984375
1
764.8984375
768.6484375
2
768.6484375
768.6484375
3
768.6484375
768.6328125
```

I removed the whole writing to file bit. If that causes leaks we can open another ticket for that.

I am closing the ticket for 2.8.3

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 20:13:10

Resolution: fixed
