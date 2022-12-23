# Issue 9512: Sage Source Editor

Issue created by migration from https://trac.sagemath.org/ticket/9512

Original creator: acleone

Original creation time: 2010-07-15 20:07:12

Assignee: jason, was

CC:  boothby acleone cwitty chapoton

Add an "Edit this page" link at the bottom of source files (/src/...) where one can edit the file.

Only `user_type(username) == 'admin'` can edit the files.


---

Attachment


---

Comment by boothby created at 2010-07-15 20:08:49

Changing status from new to needs_review.


---

Comment by acleone created at 2010-07-15 20:10:22

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-23 06:59:33

I'm added the commit string

```
#9512: Sage source editor.  Tom Boothby
```

for the patch I'm merging into SageNB 0.8.2 (#9572).


---

Comment by mpatel created at 2010-07-23 07:18:42

Resolution: fixed


---

Comment by mpatel created at 2010-07-25 07:28:25

[comment:ticket:9572:6 C. Witty's comment] at #9572:
> Actually, I found a bug: the "source editor" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).

> Given the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.

I also see this behavior.  I'm reopening this ticket, changing its status to "needs work," and removing it, for now, from #9572's SageNB 0.8.2.


---

Comment by mpatel created at 2010-07-25 07:28:25

Resolution changed from fixed to 


---

Comment by mpatel created at 2010-07-25 07:28:25

Changing status from closed to new.


---

Comment by mpatel created at 2010-07-25 07:28:35

Changing status from new to needs_work.


---

Comment by mpatel created at 2010-07-25 07:28:52

Changing priority from trivial to minor.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2020-09-11 10:41:57

Resolution: invalid
