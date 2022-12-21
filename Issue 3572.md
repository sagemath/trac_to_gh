# Issue 3572: optimize sage startup time by not importing any modules that import linbox by default.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 21:28:10

Assignee: cwitty




---

Attachment


---

Comment by was created at 2008-07-06 22:46:01

on osx, BEFORE:

```
teragon-2:matrix was$ sage -startuptime |grep linbox
            sage.libs.linbox.linbox: 0.270 (matrix_modn_dense)
0.270 sage.libs.linbox.linbox (matrix_modn_dense)
```


AFTER

```
teragon-2:matrix was$ sage -startuptime |grep linbox
teragon-2:matrix was$ 
```


Of course now,


```
sage: time a = matrix(ZZ,2)
CPU times: user 0.34 s, sys: 0.01 s, total: 0.35 s
Wall time: 0.36 s
sage: time a = matrix(ZZ,3)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```


but that makes a lot of sense.  Only make people pay if they use the goods.

William


---

Comment by mabshoff created at 2008-07-07 04:21:53

With this patch applied against 3.0.4.alpha2 I get one doctest failure:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ ./sage -t -long devel/sage/sage/misc/session.pyx
sage -t -long devel/sage/sage/misc/session.pyx              
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/session.py", line 212:
    sage: save_session('session', verbose=True)
Expected:
    Not saving ...
Got:
    Saving doctest
    Saving a
    Not saving example_2: example_2 is a function
    Not saving example_3: example_3 is a function
    Not saving example_0: example_0 is a function
    Not saving example_1: example_1 is a function
    Not saving example_4: example_4 is a function
    Not saving example_5: example_5 is a function
    Saving __file__
    Not saving f: f is a function
    Saving __doc__
    Saving __builtins__
    Saving __name__
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_session.py
	 [2.0 s]
exit code: 1024
```


Cheers,

Michael


---

Comment by jhpalmieri created at 2009-05-10 23:21:22

The patch doesn't apply cleanly any more, as you might expect.  I only got one doctest failure, from the following issue (not the one mabshoff reported, perhaps because that doctest in the patch didn't apply): 

```
sage: os.system('sage -startuptime | grep linbox')
           sage.libs.linbox.linbox: 0.006 (sage.matrix.matrix_modn_dense)
0
```

So there's another import which needs to be removed...
