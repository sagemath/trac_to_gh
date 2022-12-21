# Issue 5471: loads(dumps()) does not seem to work as wanted for Symbolic Variables

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2009-03-10 20:12:58

Assignee: tbd

Consider the following Sage session (Sage 3.4.rc1):

```
sage: var('a b c')
(a, b, c)
sage: first = a + b + c
sage: first._operands[0]._operands[0]
a
sage: first._operands[0]._operands[0] is a
True
sage: second = loads(dumps(first))
sage: second._operands[0]._operands[0]
a
sage: second._operands[0]._operands[0] is a
False
```

The last result is unexpected, and may lead to considerable confusion. The topic was raised by "Maurizio" in the thread http://groups.google.com/group/sage-devel/browse_thread/thread/9767e3a8d538438d/9ab45b4fa1ce2e36#9ab45b4fa1ce2e36


---

Comment by GeorgSWeber created at 2009-03-10 20:19:01

Resolution: duplicate


---

Comment by GeorgSWeber created at 2009-03-10 20:19:01

ups, duplicate to #5466, sorry for the fuzz
