# Issue 5701: Remove Guava from standard Sage

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-06 21:57:46

Assignee: rlm

CC:  wdj

We currently ship Guava per default in the GAP.spkg. But Guava is limited in functionality, i.e. compared to Magma see http://wiki.sagemath.org/magma#CodingTheory for a list by wdj, and tends to crash at exit, too.  

The following doctests fail when guava is removed from the GAP spkg. 

```
	sage -t -long "devel/sage/sage/combinat/combinat.py"
	sage -t -long "devel/sage/sage/combinat/designs/block_design.py"
	sage -t -long "devel/sage/sage/coding/linear_code.py"
	sage -t -long "devel/sage/sage/coding/code_bounds.py"
	sage -t -long "devel/sage/sage/coding/code_constructions.py"
	sage -t -long "devel/sage/sage/coding/guava.py"
```


Cheers,

Michael


---

Attachment

based on 4.0.a0


---

Attachment

I have run tests and checked the code here, and everything seems fine, with the following caveat: I did not run tests on a fresh install, i.e. I ran tests on a system with Guava still installed.

I will give this a positive review, pending the tests passing on a system with the right GAP spkg and workspace setup, and  wdj will follow up on #6094.


---

Attachment

to be applied after the other 2 patches (all three can be based on 4.0.rc0)


---

Comment by wdj created at 2009-05-26 02:08:56

I just added a third patch. If you remove guava from gap*/pkg, reset the GAP workspace, and then apply these three patches then all tests pass on a 64bit ubuntu 9.04 machine.


---

Comment by rlm created at 2009-05-26 06:36:55

Since you are adding an input to `wtdist_gap`, you also need to add a description to the INPUT section.


---

Attachment

to be applied after the others.


---

Comment by wdj created at 2009-06-05 11:55:59

Adds 2 line description to linear_code.py docstring following referees suggestion.


---

Comment by ncalexan created at 2009-06-12 07:34:37

Resolution: fixed
