# Issue 2910: bug in Integer(string)

Issue created by migration from https://trac.sagemath.org/ticket/2910

Original creator: was

Original creation time: 2008-04-13 19:11:36

Assignee: robertwb

CC:  timothyclemans

This behavior is inconsistent and could lead to horrible bugs:

```
sage: int('070')
70
sage: Integer('070')
56
```


Because Sage uses Python instead of inventing its own language, there
are issues like this.   The only options to fix this problem
are (a) make int('070') return 56 or (b) make Integer('070') return 70.
Irregardless of what Sage *should* do, (a) is not an option since it
requires changing the Python interpreter, and an axiom of Sage development
is that we will never do that.  So (b) it is.   To resolve this trac tick
one must thus do (b).




---

Comment by robertwb created at 2008-05-01 05:24:44

Ugh. This means


```
sage: Integer('070') == Integer(070)
False
```


So be it I guess...


---

Comment by boothby created at 2009-01-23 10:05:56

A PEP deals with this:

http://mail.python.org/pipermail/python-3000/2007-March/006444.html


```
During the present discussion, it was almost universally agreed that::

    eval('010') == 8

should no longer be true, because that is confusing to new users.
```


Additional thoughts?


---

Comment by boothby created at 2009-01-23 10:10:34

Resolution: wontfix


---

Comment by boothby created at 2009-01-23 10:10:34

William said "hobgoblin something something consistency foolish something.  close it as wontfix".


---

Comment by robertwb created at 2009-01-23 10:16:29

+1 to wontfix for me
