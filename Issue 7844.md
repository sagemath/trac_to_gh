# Issue 7844: notebook.address AttributeError

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-05 02:24:47

Assignee: AlexGhitza

CC:  was ddrake

On publishing a new worksheet:

```python
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py", line 1316, in render
            addr += notebook.address
        exceptions.AttributeError: 'Notebook' object has no attribute 'address'
```


I think this is a follow-up to #7639.


---

Comment by mpatel created at 2010-01-05 02:28:47

`notebook.address` --> `notebook.interface`.  sagenb repo.


---

Attachment

Have I found them all?


---

Comment by mpatel created at 2010-01-05 02:29:29

Changing component from algebra to notebook.


---

Comment by mpatel created at 2010-01-05 02:29:29

Changing status from new to needs_review.


---

Comment by was created at 2010-01-05 04:00:23

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-05 04:00:36

Resolution: fixed


---

Comment by was created at 2010-01-05 04:00:36

merged into sagenb-0.5.
