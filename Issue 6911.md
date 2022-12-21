# Issue 6911: Faster basis of a Hecke algebra

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-09-10 05:48:10

Assignee: craigcitro

Followup to #6768, uses algorithm at http://wiki.sagemath.org/days17/projects/presagedays/discussion


---

Comment by robertwb created at 2009-09-10 05:48:57

Also discriminants.


---

Attachment


---

Comment by was created at 2009-09-17 07:47:02

REFEREE REPORT:

1. Awesome trace of product trick!

2. I think the following range must start at 1 -- otherwise this is potentially (in theory) a major bug:

```
span = [self.hecke_operator(n) for n in range(2, bound+1) if not self.is_anemic() or gcd(n, level) == 1] 
```


3. "eisenstein" should be capitalized below:

```
 	1182	        Returns whether self is cuspidal, i.e. has no eisenstein part.
```


4. The patch doesn't seem to apply cleanly to 4.1.2.alpha1:

```
Hunk #4 FAILED at 214
1 out of 6 hunks FAILED -- saving rejects to file sage/modular/hecke/algebra.py.rej
abort: patch failed to apply
```



---

Attachment


---

Attachment


---

Comment by was created at 2009-09-19 11:43:08

Apply these:

```
trac_6911-referee-replace_other_patch-apply_only_this.patch
trac_6911-referee_followup_that_fixes_some_bugs.patch 
```



---

Comment by mvngu created at 2009-09-19 20:40:25

Resolution: fixed


---

Comment by mvngu created at 2009-09-19 20:40:25

Merged patches in this order:

 1. `trac_6911-referee-replace_other_patch-apply_only_this.patch`
 1. `trac_6911-referee_followup_that_fixes_some_bugs.patch`
