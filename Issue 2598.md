# Issue 2598: [with patch, needs review] allow ZZ element to be constructed from GF(2) list

Issue created by migration from https://trac.sagemath.org/ticket/2598

Original creator: malb

Original creation time: 2008-03-19 16:04:10

Assignee: somebody

This works for some time now:


```
sage: ZZ([1,0], 2)
1
```


and after the patch this also works:


```
sage: ZZ([GF(2)(1),GF(2)(0)], 2)
1
```


It is -- at least for my applications -- common to get a list of bits, do some bitstuff with them and combine them again to an integer.

}}}


---

Attachment


---

Comment by jbmohler created at 2008-03-20 12:45:23

The patch does what it claims and adds an appropriate doc-test.  There is a small (maybe 7-8%) speed-hit, but I think it is worth it for the improved functionality.

I say it should be applied.


---

Comment by mabshoff created at 2008-03-21 02:30:19

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 02:30:19

Merged in Sage 2.11.alpha1
