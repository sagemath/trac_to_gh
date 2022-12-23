# Issue 983: abs seems to be missing a proper latex method

Issue created by migration from https://trac.sagemath.org/ticket/983

Original creator: mabshoff

Original creation time: 2007-10-24 17:39:29

Assignee: somebody

Hello,

```
 The problem seems to be the abs() command. Take any function like
 f(x)=2*abs(x) with a changing sign. Entering now latex(f) shows me as
 the result:
 x \ {\mapsto}\ {2 \cdot \abs \left( x \right)}
```

reported by marko in sage-support.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-24 17:41:32

Resolution: duplicate


---

Comment by mabshoff created at 2007-10-24 17:41:32

mhansen was faster - see #982, so close this as a dupe.
