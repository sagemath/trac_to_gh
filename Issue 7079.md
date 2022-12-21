# Issue 7079: parallel doctest broken in Sage 4.1.2.alpha4 if HOME/.sage/tmp doesn't exist

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-30 07:07:28

Assignee: tbd

CC:  fwclarke jason timdumol ddrake

With a freshly compiled Sage 4.1.2.alpha4, or take the sage.math binary for Sage 4.1.2.alpha4, follow these steps and watch the carnage:

 1. Delete the directory HOME/.sage, yes that directory and everything under it. Or you could just make sure that HOME/.sage/tmp doesn't exist. Yes, it's "tmp", not "temp".
 1. Go to SAGE_ROOT.
 1. Open SAGE_ROOT/makefile and give the variable NUM_THREADS a positive integer such as 2, or say anything positive integer from 2 to 10 on sage.math.
 1. From SAGE_ROOT, do "make ptestlong" and watch Sage give a bunch of file not found errors:
 {{{
sage -t -long devel/sage/doc/en/tutorial/distributed.rst
         [0.1Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 587, in test_file
    open(f,"w").write(s)
IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//tmp/.doctest_tour_algebra.py'
Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 587, in test_file
    open(f,"w").write(s)
IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//tmp/.doctest_tour_help.py'
Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 587, in test_file
    open(f,"w").write(s)
IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//tmp/.doctest_programming.py'
Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 587, in test_file
    open(f,"w").write(s)
IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//tmp/.doctest_tour_polynomial.py'
Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 587, in test_file
    open(f,"w").write(s)
IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//tmp/.doctest_tour_groups.py'
Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 587, in test_file
    open(f,"w").write(s)
IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//tmp/.doctest_tour_plotting.py'
Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 587, in test_file
    open(f,"w").write(s)
IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//tmp/.doctest_introduction.py'
 s]
 }}}


---

Comment by fwclarke created at 2009-09-30 08:27:47

I think the attached patch might solve the problem.  [I'm off to work now, so I've no time to test whether this is so.]


---

Attachment


---

Comment by mvngu created at 2009-09-30 09:36:09

With the patch `trac_7079.patch`, I followed the steps as listed above and got the following errors:

```
init.sage does not exist ... creating
Global iterations: 1
File iterations: 1
No long cached timings exist; will create upon successful finish.
Doctesting 2096 files doing 10 jobs in parallel
Traceback (most recent call last):
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 754, in <module>
    test_file(argv[1], library_code = library_code)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/bin/sage-doctest", line 608, in test_file
    os.makedirs(VALGRIND)
  File "/scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 17] File exists: '/home/mvngu/.sage//valgrind/'

<SNIP>

The following tests failed:

        sage -t -long devel/sage/doc/common/builder.py # File not found
----------------------------------------------------------------------
Total time for all tests: 666.1 seconds
```



---

Comment by fwclarke created at 2009-09-30 17:39:17

Replying to [comment:5 mvngu]:

This seems very strange.  Lines 606-608 of SAGE_ROOT/local/bin are 

```
        VALGRIND = '%s/valgrind/'%DOT_SAGE
        if not os.path.exists(VALGRIND):
          os.makedirs(VALGRIND)
```

which, apart from the non-standard indent, seem perfectly ok.  In particular, line 608 can never be executed if the directory VALGRIND exists.  And yet this is what seems to be happening for you.

I've tried following your steps (with NUM_THREADS=2), and it's running smoothly, though with

```
sage -t -long devel/sage/sage/calculus/calculus.py
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```

and a couple more like this.  I'll investigate these cases and any others that arise.


---

Comment by fwclarke created at 2009-10-01 08:30:20

Replying to [comment:6 fwclarke]:

>{{{
> A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
> }}}
> and a couple more like this.  I'll investigate these cases and any others that arise.


The "mysterious" errors (of which there were 14) seem to be cases where Sage 4.1.2.alpha4 crashes 
(on my Mac OS X 10.6.1).  E.g.,

```
sage -t -verbose "devel/sage/sage/functions/hyperbolic.py"  
...
Trying:
    arccosh._evalf_(Integer(2), Integer(53))###line 13:_sage_    >>> arccosh._evalf_(2, 53)
Expecting:
    1.31695789692482
ok
...
Trying:
    bool(diff(csch(x), x) == diff(Integer(1)/sinh(x), x))###line 185:_sage_    >>> bool(diff(csch(x), x) == diff(1/sinh(x), x))
Expecting:
    True
         [16.9 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -verbose "devel/sage/sage/functions/hyperbolic.py"
Total time for all tests: 16.9 seconds
```


While

```
----------------------------------------------------------------------
----------------------------------------------------------------------
...
sage: diff(csch(x), x) == diff(Integer(1)/sinh(x), x)
-coth(x)*csch(x) == -cosh(x)/sinh(x)^2
sage: bool(diff(csch(x), x) == diff(Integer(1)/sinh(x), x))
/Users/mafwc/sage-4.1.2.alpha4/local/bin/sage-sage: line 200:   
378 Abort trap  sage-ipython "$`@`" -i
```

compared with

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: fwc
sage: bool(diff(csch(x), x) == diff(1/sinh(x), x))
True
```



---

Comment by jhpalmieri created at 2009-10-03 22:38:47

I think the patch is a good idea.  It basically works for me on Mac OS X 10.5 and on sage.math.  Maybe it should get a positive review and then we should work on the "mysterious" errors. On sage.math, if I don't apply the patch, delete my .sage directory, and do parallel doctesting, it's a complete disaster.  Once I apply the patch, if I delete my .sage directory, and while in SAGE_ROOT I do `sage -tp 2 devel/sage/sage/algebras`, then I get 

```
init.sage does not exist ... creating
touch: cannot touch `/home/palmieri/.sage//init.sage': No such file or directory
Global iterations: 1
File iterations: 1
No cached timings exist; will create upon successful finish.
Doctesting 21 files doing 2 jobs in parallel
sage -t  devel/sage/sage/algebras/free_algebra_quotient.py
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```

and then all of the other doctests pass.  This is not related, I think, to the problems on Mac OS X 10.6: if I do it again (but with an existing .sage directory), all tests pass.  Maybe the issue is that one thread is running a doctest while another is still busy creating .sage and all of its subdirectories, and so the doctest crashes?  Or two threads are both trying to create .sage at the same time, and this leads to problems?  This might also explain mvngu's problems with .sage/valgrind.  Should we run one test and then switch to parallel testing, or should we run the script (whatever it is) that creates .sage, and then go on to parallel testing?

So I don't know if this should get a positive review and the mysterious crashes should be in a separate ticket, since that would solve most of the problem, or if this should be marked "needs work" and the whole thing fixed at once...


---

Comment by was created at 2009-10-03 23:58:22

> So I don't know if this should get a positive review and the mysterious crashes 
> should be in a separate ticket,

That's what I think.  So I've switched to to that, applied it, and opened a new ticket: #7103


---

Comment by was created at 2009-10-03 23:59:10

merged into 4.2.1.rc0.


---

Comment by was created at 2009-10-03 23:59:10

Resolution: fixed
