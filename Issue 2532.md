# Issue 2532: [with-patch] padic bugfix

Issue created by migration from https://trac.sagemath.org/ticket/2532

Original creator: roed

Original creation time: 2008-03-15 19:05:56

Assignee: roed

Fixes a number of bugs in p-adic extensions.

1. changes many object creation functions to pass on exceptions if necessary.
2. fixes a bug in precision_absolute for capped relative extension elements that causes it to return the wrong answer if the element is not normalized.
3. Fixes object creation functions so that they do not fail when asked to create an element of precision zero.


---

Attachment


---

Comment by mhansen created at 2008-03-15 22:35:43

The patch applies, builds, and passes all tests.  However, a follow-up patch should be added which adds doctests to show that the bugs are indeed fixed.


---

Comment by mabshoff created at 2008-03-17 00:35:53

Doctests also pass for me when applying the patch to 2.10.4.final. After talking to roed about the missing doctest in IRC yesterday I tend to want to merge this and hope that doctests are forthcomings since these fixes have been tested and reviewed by several people "back east."

Cheers,

Michael


---

Comment by dmharvey created at 2008-03-17 00:52:57

I agree. Given the current doctest coverage and code complexity of the p-adics code, I think we should just merge this and wait for the real doctesting work to catch up.


---

Comment by mabshoff created at 2008-03-17 01:05:11

I agree with dmharvey. #610 covers the need to increase doctest coverage. Maybe somebody else besides roed can help out here?

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-17 01:09:25

Merged in Sage 2.10.4.final - note that the patch is a GNU patch. I did commit it in roed's name.


---

Comment by mabshoff created at 2008-03-17 01:09:25

Resolution: fixed
