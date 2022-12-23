# Issue 724: graph6 parsing does not throw an error when the string is the wrong size.

Issue created by migration from https://trac.sagemath.org/ticket/724

Original creator: jason

Original creation time: 2007-09-21 00:40:12

Assignee: was

Keywords: graph6, graph

Making a graph from a graph6 string should check to make sure the string is the right size and throw an error if the string is too long or too short.  I believe now it just silently hands back a graph that is not correct.

This is bad, especially when your string has an escaped character and you didn't realize it :).


---

Comment by rlm created at 2007-10-24 07:50:00

Changing status from new to assigned.


---

Comment by rlm created at 2007-10-24 07:50:00

Changing assignee from was to rlm.


---

Attachment


---

Comment by rlm created at 2007-10-25 18:54:28

This patches cleanly onto 2.8.9.


---

Comment by cwitty created at 2007-10-26 06:38:22

Please add doctests to show the new exceptions.  (Every bug fix should have a doctest.)

Thanks!


---

Attachment


---

Comment by cwitty created at 2007-10-27 04:53:30

Resolution: fixed
