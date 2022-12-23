# Issue 5033: matrix lift function bad in two ways

Issue created by migration from https://trac.sagemath.org/ticket/5033

Original creator: was

Original creation time: 2009-01-20 06:03:40

Assignee: was

There are two problem here:

```
sage: B = matrix(QQ, 2, [1..4])
sage: B.lift()
...
AttributeError: 'RationalField' object has no attribute 'cover_ring'
sage: B.lift?
            EXAMPLES:
...
}}}          

1. lift should first check if there is a cover_ring attribute.  If not, I think lift should just return self.

2. The lift function is undocumented.  It just has examples but no description of what it is supposed to do.


---

Attachment

this is against sage-3.3.alpha0


---

Comment by ddrake created at 2009-01-20 06:48:45

The patch fixes both issues mentioned in the ticket and the code is nice. Positive review.


---

Comment by mabshoff created at 2009-01-23 09:07:05

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 09:07:05

Merged in Sage 3.3.alpha1
