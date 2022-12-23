# Issue 7835: Preparsing on server does not account for unicode text

Issue created by migration from https://trac.sagemath.org/ticket/7835

Original creator: timdumol

Original creation time: 2010-01-03 19:15:54

Assignee: was

CC:  was mpatel ddrake

#7483 moves preparsing to the server but does not account for unicode text, i.e., does not have a `# -*- coding: utf-8 -*-` header.

This patch depends on #7514 and everything it depends on.


---

Comment by timdumol created at 2010-01-03 19:17:05

This should do the trick.


---

Comment by timdumol created at 2010-01-03 19:17:05

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-03 19:24:38

Adds '# -*- coding: utf-8 -*-' to the preparsing code.


---

Attachment

This looks good to me.  Is there a simple example that breaks the existing code?


---

Comment by timdumol created at 2010-01-06 20:31:43

You mean without this patch? Just use any non-ASCII character and attempt to evalaute it.


```
print 'é'
```



---

Comment by mpatel created at 2010-01-06 20:45:36

Just to check: I should apply #7249, too.  Otherwise, even with this patch, `print 'é'` raises

```python
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py", line 1205, in render
            max_out=HISTORY_MAX_OUTPUT)
        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 17: ordinal not in range(128)
```

at least for me.


---

Comment by mpatel created at 2010-01-06 20:46:11

Now reviewing #7249...


---

Comment by mpatel created at 2010-01-06 23:20:53

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-01-07 01:26:51

Add short-term workaround for History/Log.  Replaces previous.


---

Comment by mpatel created at 2010-01-07 01:31:28

Changing status from needs_work to needs_review.


---

Attachment

V2 wraps the [comment:4 problem above] in a `try-except` block, for now, i.e., until #7249 takes hold.  My review is positive, but someone should review my change.


---

Comment by mpatel created at 2010-01-18 06:09:50

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-18 06:13:46

I'm assuming my change is OK, given its [comment:9:ticket:7908 position], but feel free to revert the status.


---

Comment by timdumol created at 2010-01-19 03:31:30

Resolution: fixed
