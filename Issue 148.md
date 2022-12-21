# Issue 148: links in HTML version don't work

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2006-10-23 16:26:43

Assignee: was

links in a notebook saved to html point to localhost -- they should just be relative anyway.


---

Comment by boothby created at 2006-10-23 16:27:01

Changing component from algebraic geometry to notebook.


---

Comment by boothby created at 2006-10-23 16:27:01

Changing assignee from was to boothby.


---

Comment by boothby created at 2006-10-23 16:27:01

Changing priority from major to trivial.


---

Comment by was created at 2007-01-19 11:32:45

this simply isn't true.  I tried this both with print mode and
directly from a worksheet with this in edit mode followed by
io cells.  

```

<a href="/trac92">trac92</a>


```



In each case the link does not go to localhost.  It's absolute. 
Anyway, I do not understand this bug report at all.


---

Comment by was created at 2007-01-22 01:43:54

Resolution: fixed


---

Comment by was created at 2007-01-22 01:43:54

Not a problem anymore...
