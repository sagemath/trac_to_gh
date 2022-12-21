# Issue 4100: comparison with None extraordinarily slow

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-11 06:04:35

Assignee: somebody

This is because the coercion model is invoked, and with types it actually tries to cast one direction or the other, raising errors. 


---

Comment by robertwb created at 2008-09-11 06:08:10

Before


```
sage: timeit("1 == None")
625 loops, best of 3: 625 µs per loop
```


After


```
sage: timeit("1 == None")
625 loops, best of 3: 530 ns per loop
```


This is at least close to 


```
sage: timeit("1 is None")
625 loops, best of 3: 330 ns per loop
```


but people who don't know about the `is` operator shouldn't be hit that bad...


---

Attachment


---

Comment by cremona created at 2008-09-18 20:52:21

Review:  patch applies ok to 3.1.2 and all tests in sage/structure pass.  ok!


---

Comment by mabshoff created at 2008-09-19 02:57:29

This patch causes a doctest failure in gen.pyx:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0$ ./sage -t -long devel/sage/sage/libs/pari/gen.pyx
sage -t -long devel/sage/sage/libs/pari/gen.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/gen.py", line 689:
    sage: pari(2.5) > None
Expected:
    False
Got:
    True
**********************************************************************
1 items had failures:
   1 of  16 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/.doctest_gen.py
         [56.1 s]
```



---

Comment by robertwb created at 2008-09-19 07:27:47

I think the doctest should change, I believe the purpose is to show that things don't go boom when you compare with None, not that an ordering is enforced.


---

Comment by cremona created at 2008-09-19 07:59:53

I agree with Robert.  Let's change that doctest (or even remove it, since I don't think it serves any useful purpose!)


---

Comment by mabshoff created at 2008-09-19 15:56:11

I fixed the doctest as indicated. If you want to change something or add a comment please post a patch. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-19 15:57:28

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 15:57:28

Merged in SAge 3.1.3.alpha0
