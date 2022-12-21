# Issue 2377: [with patch, needs review] Bugfix for the new __copy__ method of SingularElement

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-03-03 17:09:01

Assignee: was

CC:  malb

Keywords: copy SingularElement

This is related with #2300. The patch of #2300 was already merged in sage-2.10.3.rc0, so malb suggested to make a new ticket for the following bugfix.

In sage-2.10.3.rc0, the following example would produce a traceback when copying the quotient ring Q. With the patch, it works.

```
sage: R=singular.ring(0,'(x,y)','dp')
sage: L=R.ringlist()
sage: L[4]=singular.ideal('x**2-5')
sage: Q=L.ring()
sage: otherR=singular.ring(5,'(x)','dp')
sage: cpQ=copy(Q)
sage: cpQ.set_ring()
sage: cpQ

//   characteristic : 0
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
// quotient ring from ideal
_[1]=x^2-5
```


The bug consists in the following: In `__copy__`, ringlist is called. In the case of quotient rings or non-commutative rings, ringlist contains polynomial data. Hence, it is invalid if the current ring (here: otherR) does not fit.

Solution: With the patch, `__copy__` applied to a ring or quotient ring Q first makes Q active, then produces a copy of Q, returns to the previously active ring, and provides the copy of Q.


---

Attachment

Bugfix for the new copy method for SingularElement?; should apply to sage-2.10.3.rc0


---

Comment by mabshoff created at 2008-03-03 17:34:43

To quote malb from #2300:

```
The code looks good, I don't know a better Singular solution. I'm happy to give 
the bugfix a 'positive review' once it is attached to a new ticket
```


So: positive review from malb.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 17:55:40

Merged in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-03 17:55:40

Resolution: fixed
