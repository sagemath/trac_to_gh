# Issue 7845: Failed browse_sage_doc doctest

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-05 02:55:05

Assignee: mvngu

CC:  jhpalmieri

In Sage 4.3.1.alpha0:

```python
sage -t  "devel/sage/sage/misc/sagedoc.py"
**********************************************************************
File "/home/jaap/downloads/sage-4.3/devel/sage/sage/misc/sagedoc.py", line 897:
     sage: browse_sage_doc(identity_matrix, 'html', False)[:59]
Expected:
     '<div class="docstring">\n    \n  <p><strong>File:</strong> /v'
Got:
     '<div class="docstring">\n    \n  <p><strong>File:</strong> /h'
********************************************************************** 
```



First reported by [Jaap Spies](http://groups.google.com/group/sage-devel/msg/960b6f10c9024d0f).


---

Comment by mpatel created at 2010-01-05 02:57:48

Tweak `browse_sage_doc` doctests.  sage repo.


---

Attachment

Feel free to tweak further!


---

Comment by mpatel created at 2010-01-05 02:58:26

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-01-05 04:31:53

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-01-05 04:31:53

Looks good to me.


---

Comment by rlm created at 2010-01-13 04:14:50

Resolution: fixed
