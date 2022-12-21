# Issue 3748: bug in integers modulo n

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-07-30 15:29:00

Assignee: somebody

this was reported to me by Emmanuel Thome with Sage 3.0.3:

```
sage: R=Integers(17^5)
sage: R
Ring of integers modulo 1419857
sage: R(17)^5
1419857
sage: R(17)^5==0
False
sage: R(R(17)^5)
0
```

Clearly R(17)^5 is not in canonical form, which is what we would expect... However:

```
sage: R(17)*R(17)*R(17)*R(17)*R(17)
0
```



---

Comment by mabshoff created at 2008-07-30 15:34:38

Resolution: duplicate


---

Comment by mabshoff created at 2008-07-30 15:34:38

Hi Paul,

David Harvey reported the same problem from sage-devel and already put up a patch that has been positively reviewed patch at #3747. So I am closing this as a duplicate.

Cheers,

Michael
