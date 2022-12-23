# Issue 5727: Improve doctest coverage for sage/modular

Issue created by migration from https://trac.sagemath.org/ticket/5727

Original creator: davidloeffler

Original creation time: 2009-04-09 18:05:44

Assignee: craigcitro

Keywords: doctests

The attached patch adds doctests for 28 previously undoctested functions in the sage/modular directory, and fixes 2 small bugs uncovered in the process: one in pickling of arithmetic subgroups defined by permutations, and one in dirichlet characters (galois_orbits() returned meaningless garbage when the base ring wasn't an integral domain). 

This brings the doctest coverage to 100% for everything *except* the three big subdirectories modform/, modsym/ and hecke/. I will get to work on these next.


---

Comment by davidloeffler created at 2009-04-09 18:06:10

patch against 3.4.1.rc1


---

Attachment

Let's change the status so the right reports pick up this ticket :)

Cheers,

Michael


---

Comment by was created at 2009-04-10 00:51:02

REVIEW:
  * Put backquotes aroudn start_weight in the modform_generators docstring: 
    ` - start_weight -- an integer (default: 2) `
  * A doctest fails on 32-bit OS X: 

```
sage -t --long devel/sage/sage/modular/arithgroup/arithgroup_perm.py
**********************************************************************
File "/Users/wstein/build/sage-3.4.1.rc1/devel/sage-main/sage/modular/arithgroup/arithgroup_perm.py", line 202:
    sage: cmp(G, 1)
Expected:
    -1
Got:
    1
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_9
***Test Failed*** 1 failures.
```

I recommend changing the doctest to:

```
   sage: cmp(G,1) in [-1,1]
```

since it depends on the OS.


These are trivial changes, so I've posted a tiny patch that adds them and given this a positive review.


---

Attachment

apply this after applying the above patch


---

Comment by mabshoff created at 2009-04-10 01:53:35

Resolution: fixed


---

Comment by mabshoff created at 2009-04-10 01:53:35

Merged both patches in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-04-10 19:31:01

Resolution changed from fixed to 


---

Comment by davidloeffler created at 2009-04-10 19:31:01

Here's some more -- mostly in sage/modular/hecke/hecke_operator.py and sage/modular/hecke/module.py. This patch also adds Brandt modules into the reference manual.


---

Comment by davidloeffler created at 2009-04-10 19:31:01

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-04-10 19:39:59

Resolution: fixed


---

Comment by mabshoff created at 2009-04-10 19:39:59

Please do not reopen tickets with merged patches. Instead open a new ticket for the new patch. I have deleted the new patch.

Cheers,

Michael
