# Issue 5943: Sage 3.4.2.a0: prime_pi(2^50) segfaults

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-29 22:45:19

Assignee: was

CC:  boothby mjo

This is *bad*.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-29 22:48:16

Hmm, the back trace looks pretty bad:

```
mabshoff`@`sage:~$ sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/usr/local/sage/local/bin/sage-ipython
GNU gdb 6.8-debian
Copyright (C) 2008 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...
[Thread debugging using libthread_db enabled]
Python 2.5.2 (r252:60911, Mar 11 2009, 22:18:38) 
[GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu3)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
[New Thread 0x7fe3285456e0 (LWP 11010)]
sage: prime_pi(2^50)
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fe3285456e0 (LWP 11010)]
0x00007fe32776bf4e in ?? () from /lib/libc.so.6
(gdb) bt
#0  0x00007fe32776bf4e in ?? () from /lib/libc.so.6
#1  0x00fc73d0eb623c9b in ?? ()
Cannot access memory at address 0xff0ff3d0eb624364
(gdb) 
```



---

Comment by AlexGhitza created at 2009-05-02 11:15:04

I can't get this to segfault.  I tried on sage.math and on my laptop (macbook running 32-bit archlinux).  The problem is that the two machines get different answers after a while (I hope the table is clear -- the last column is a function that's "known" to be a good approximation to prime_pi):


```
x     prime_pi(x) on sage.math     prime_pi(x) on my laptop     Li(x)-Li(sqrt(x))/2
2^46   2280998753949                2280998753949               2.28099863535e+12
2^47   4461632979717                4454203917918               4.46163280359e+12
2^48   8731188863470                8612800813048               8.73118897751e+12
2^49  17094432576778               15793194017311               1.70944327138e+13
2^50  33483379603407               21969300962685               3.34833795774e+13
```


So it seems that the problem starts somewhere between `2^46` and `2^47`, and that the sage.math output is most likely correct.


---

Comment by mabshoff created at 2009-05-03 00:29:40

We might want to either implement this ourselves or just put reasonable limit on this:

```
sage" len(prime_range(2^35))
/home/mabshoff/.sage/temp/sage.math.washington.edu/10069/_home_mabshoff__sage_init_sage_0.py in <module>()

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/IPython/iplib.pyc in ipmagic(self, arg_s)
    951         else:
    952             magic_args = self.var_expand(magic_args,1)
--> 953             return fn(magic_args)
    954 
    955     def ipalias(self,arg_s):

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/IPython/Magic.pyc in magic_time(self, parameter_s)
   1905         if mode=='eval':
   1906             st = clk()
-> 1907             out = eval(code,glob)
   1908             end = clk()
   1909         else:

/home/mabshoff/.sage/temp/sage.math.washington.edu/10069/_home_mabshoff__sage_init_sage_0.py in <module>()

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3772)()

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3458)()

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.primes_up_to_n (sage/libs/pari/gen.c:40660)()

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44402)()

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.allocatemem (sage/libs/pari/gen.c:40001)()

/scratch/mabshoff/sage-3.4.2.final/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.init_stack (sage/libs/pari/gen.c:43371)()

MemoryError: Unable to allocate 131072000000 bytes memory for PARI.
```



---

Comment by was created at 2009-06-15 23:28:37

Changing priority from blocker to critical.


---

Comment by wuthrich created at 2009-12-03 14:49:34

I get now (in sage 4.2.1)


```
len(prime_range(2^50))

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_4.py", line 5, in <module>
    len(prime_range(_sage_const_2 **_sage_const_50 ))
  File "", line 1, in <module>
    
  File "fast_arith.pyx", line 56, in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3822)
  File "fast_arith.pyx", line 100, in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3508)
  File "gen.pyx", line 8663, in sage.libs.pari.gen.PariInstance.primes_up_to_n (sage/libs/pari/gen.c:41327)
OverflowError: long int too large to convert to int
```


which is the same problem as #7017.


---

Comment by kini created at 2011-10-15 09:07:45

In Sage 4.7.2.alpha3, I get the following:


```
sage: len(prime_range(2^50))
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/keshav/<ipython console> in <module>()

/home/keshav/sage/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:4082)()

/home/keshav/sage/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3717)()

/home/keshav/sage/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:47679)()

PariError: not enough memory (28)
```


Is there something wrong with this, or should this ticket be closed?


---

Comment by mjo created at 2011-12-12 02:14:55

Patch doctesting the correct behaviour


---

Attachment

I think the current behavior is desirable given the alternatives.
The slower algorithm falls on its face just as hard if you choose an upper bound that will cause out-of-memory, so there's no sense in falling back to that after we catch the exception.


---

Comment by mjo created at 2011-12-12 02:18:51

Changing status from new to needs_review.


---

Comment by kini created at 2011-12-12 02:29:33

Changing status from needs_review to positive_review.


---

Comment by kini created at 2011-12-12 02:29:33

Sounds good to me.


---

Comment by jdemeyer created at 2011-12-17 09:12:40

Resolution: fixed


---

Comment by jdemeyer created at 2011-12-21 09:18:30

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-12-21 09:18:30

On hawk (OpenSolaris 06.2009-32):

```
sage -t -long  -force_lib devel/sage/sage/rings/fast_arith.pyx
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/devel/sage-main/sage/rings/fast_arith.pyx", line 122:
    sage: prime_range(sys.maxint)
Expected:
    Traceback (most recent call last):
    ...
    PariError: not enough memory (28)
Got:
    Traceback (most recent call last):
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[16]>", line 1, in <module>
        prime_range(sys.maxint)###line 122:
    sage: prime_range(sys.maxint)
      File "fast_arith.pyx", line 56, in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:4149)
        cpdef prime_range(start, stop=None, algorithm="pari_primes", bint py_ints=False):
      File "fast_arith.pyx", line 161, in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3929)
        res.append(z)
    MemoryError
**********************************************************************
```



---

Comment by jdemeyer created at 2011-12-21 09:18:30

Resolution changed from fixed to 


---

Comment by kini created at 2011-12-21 09:30:23

Hmm. For comparison, on x86_64, within a doctest:


```
Expected:
    Traceback (most recent call last):
    ...
    PariError: not enough memory (28)
    xyzzy
Got:
    Traceback (most recent call last):
      File "/opt/sage-4.8.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/opt/sage-4.8.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/opt/sage-4.8.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[16]>", line 1, in <module>
        prime_range(sys.maxint)###line 122:_sage_    >>> prime_range(sys.maxint)
      File "fast_arith.pyx", line 56, in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:4149)
      File "fast_arith.pyx", line 150, in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3795)
      File "gen.pyx", line 10262, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:49373)
    PariError: not enough memory (28)
```


What's `sys.maxint` on hawk? I don't have an account there. On my machine:


```
sage: sys.maxint
9223372036854775807
```


Maybe the doctest should test a specific number to avoid vagaries of various platforms? Or maybe we should dig around in the code to find out why there are two different code paths that run out of memory in this operation with two different error messages.


---

Comment by mjo created at 2011-12-21 16:35:55

Sorry, the sys.maxint was (apparently not so) carefully chosen to prevent an overflow error on 32-bit systems (see #11741 and #7017). My reasoning was that it should also be large enough to cause the not-enough-memory error on any 32-bit system, but I've been outsmarted.

It looks like Pari actually created a list of `(2^32 - 1)` primes? I think I still have an OpenSolaris VM somewhere I can test on.


---

Comment by jdemeyer created at 2011-12-22 12:40:33

Replying to [comment:12 kini]:
> What's `sys.maxint` on hawk? I don't have an account there.

```
sage: sys.maxint
2147483647
sage: 2**31 -1
2147483647
```



---

Comment by mjo created at 2011-12-22 15:36:10

On 32-bit machines with PAE and a lot of memory, `sys.maxint` is smaller than the number of primes that Pari can compute (and `sys.maxint` is the biggest one we can ask for without triggering the OverflowError). Trying to append those primes to a python list requires more memory than Pari does, so it's possible to get a MemoryError there.

I think that trying to test for the not-enough-memory condition here on x32 is probably doomed. The patch for #11741 has the right idea: on 64-bit machines, we know that we can't compute close to `sys.maxint` primes regardless of how much memory is in the machine. On 32-bit machines, just sidestep the issue and cause a predictable failure.

The actual bug is still fixed: you get python errors instead of segfaults now. That leaves only the question of whether #11741 is a sufficient doctest.


---

Comment by vbraun created at 2012-04-19 16:39:55

Changing status from new to needs_review.


---

Comment by vbraun created at 2012-04-19 16:39:55

Michael wrote on sage-devel: So if someone else agrees that the doctest in #11741 is sufficient, we can close #5943. (I don't have access to my trac account right now)


---

Comment by vbraun created at 2012-04-19 16:41:37

Changing status from needs_review to positive_review.


---

Comment by leif created at 2012-04-19 16:56:35

Or did you mean the doctest from #11741 is _not_ sufficient?


---

Comment by vbraun created at 2012-04-19 17:00:47

#11741 is sufficient, as I wrote in the ticket description.


---

Comment by jdemeyer created at 2012-04-22 19:53:54

Resolution: worksforme
