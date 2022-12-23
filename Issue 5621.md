# Issue 5621: doctests for calculus.py

Issue created by migration from https://trac.sagemath.org/ticket/5621

Original creator: mvngu

Original creation time: 2009-03-28 03:55:27

Assignee: tba

Keywords: doctest, calculus.py

The objective here is to add more doctests to the file `sage/calculus/calculus.py`, especially documentation for methods/functions that are exposed to readers via the reference manual.


---

Comment by mvngu created at 2009-03-28 04:09:15

The patch `trac_5621-doctests-calculus.patch` adds doctests to 6 functions/methods in `sage/calculus/calculus.py`, raising the coverage of that module by 1% to 52%. Interestingly, with the command

```
sage -coverage
```

Sage doesn't pick up doctests for functions/methods where there's a blank line between the docstring and the function/method. For example, as it now stands with Sage 3.4, the function `desolve_system_strings()` in the module `sage/calculus/desolvers.py` has doctests but Sage doesn't pick that up. Doing a doctest coverage on Sage 3.4 shows that the coverage for `sage/calculus/desolvers.py` is at 75%. But after removing the blank line between the function signature and its docstring, running the doctest coverage again shows that `sage/calculus/desolvers.py` has 87% coverage.


---

Comment by was created at 2009-04-12 06:24:01

This patch causes a few tiny doctest failures.  Can you fix them and post another patch:

```
sage -t  devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py", line 4921:
    sage: var("x,y,z");
Expected nothing
Got:
    (x, y, z)
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py", line 4968:
    sage: var("x,y,z");
Expected nothing
Got:
    (x, y, z)
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/calculus/calculus.py", line 5537:
    sage: var("a,b");
Expected nothing
Got:
    (a, b)
**********************************************************************
3 items had failures:
   1 of   6 in __main__.example_119
   1 of  12 in __main__.example_121
   1 of   5 in __main__.example_138
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_calculus.py
         [48.7 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/calculus/calculus.py # 3 doctests failed
```



---

Attachment

based on sage-3.4.1.rc3


---

Comment by mvngu created at 2009-04-17 03:34:48

Replying to [comment:2 was]:
> This patch causes a few tiny doctest failures.  Can you fix them and post another patch:


Your wish is my command :-)  Please see the new patch, rebased against sage-3.4.1.rc3.


---

Comment by jhpalmieri created at 2009-05-10 22:52:34

Looks good, all tests pass on sage.math.  There is a trivial typo, corrected in the referee's patch.


---

Attachment

Given the pynac transformation I don't think it is a good idea to merge this now. calculus.py will be more or less gone before the end of the week anyway :).

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 18:49:21

I talked to Mike Hansen yesterday: The new doctests are going in via new symbolics - no point in creating merge issues when calculus is being more or less completely wiped out :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 01:28:49

This has been merged via #5930 into the new symbolics.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 01:28:49

Resolution: fixed
