# Issue 6953: follow-up to #6950: fix warning when building reference manual

Issue created by migration from https://trac.sagemath.org/ticket/6953

Original creator: mvngu

Original creation time: 2009-09-17 23:35:08

Assignee: tba

CC:  ylchapuy malb

This is a follow-up to ticket #6950. I got the following warning when building the reference manual with the patch at #6950:

```
WARNING: inline latex u'f(x)g(x) = 0 \x0corall x.\n\n': latex exited with error:
```



---

Comment by malb created at 2009-09-18 08:49:44

Patch looks good except there seems to be a 'fullstop' (aka 'period') missing at the end.


---

Attachment

depends on #6950


---

Comment by mvngu created at 2009-09-18 09:06:33

Replying to [comment:2 malb]:
> Patch looks good except there seems to be a 'fullstop' (aka 'period') missing at the end. 
Fixed. See the new patch.


---

Comment by malb created at 2009-09-18 09:22:35

:) I only pointed it out because I know you care about these kind of things.


---

Comment by mvngu created at 2009-09-18 13:05:30

Resolution: fixed


---

Comment by mvngu created at 2009-09-18 13:05:30

Merged patches in this order:

 1. the patch at #6950
 1. `trac_6953-typo-fixes.patch`
