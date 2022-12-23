# Issue 7384: SageNB -- Fix Sphinxify doctests

Issue created by migration from https://trac.sagemath.org/ticket/7384

Original creator: timdumol

Original creation time: 2009-11-03 20:46:18

Assignee: boothby

CC:  mpatel

`sphinxify.py`'s doctests currently fail. Fix this.


---

Comment by timdumol created at 2009-11-03 20:47:44

Changing status from new to needs_review.


---

Attachment

Fixed the doctests


---

Comment by mpatel created at 2009-11-04 05:13:18

I got two test failures:

```
sage -t  "4.2/devel/sage-main/sage/sphinxify.py"            
**********************************************************************
File "/home/apps/sage-4.2/devel/sage-main/sage/sphinxify.py", line 51:
    sage: sphinxify('A test')
Expected:
    '\n<div class="docstring">\n    \n  <p>A test</p>\n\n\n</div>'
Got:
    '<div class="docstring">\n    \n  <p>A test</p>\n\n\n</div>'
**********************************************************************
File "/home/apps/sage-4.2/devel/sage-main/sage/sphinxify.py", line 53:
    sage: sphinxify('**Testing**\n`monospace`')
Expected:
    '\n<div class="docstring"...<strong>Testing</strong>\n<span class="math"...</p>\n\n\n</div>'
Got:
    '<div class="docstring">\n    \n  <p><strong>Testing</strong>\n<span class="math">monospace</span></p>\n\n\n</div>'
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_2
***Test Failed*** 2 failures.
```

But it could be my setup.  If not, please see version 2 of the patch.


---

Attachment

Update doctest outputs.  Apply only this patch.


---

Comment by mpatel created at 2009-11-04 05:14:53

To the extent it counts, my review is positive.


---

Comment by was created at 2009-11-12 02:08:29

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-12 02:10:41

Resolution: fixed


---

Comment by was created at 2009-11-12 02:10:41

merged into sagenb-0.4.3
