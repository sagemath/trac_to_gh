# Issue 1342: very serious bug in number field residue_field

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-30 09:16:28

Assignee: was

Notice that the parent of a changes below when you do a*a!!


```
sage: K.<z> = CyclotomicField(7)
sage: P = K.factor_integer(17)[0][0]
sage: ff = K.residue_field(P)
sage: a = ff(z)
sage: parent(a)
Residue field of Fractional ideal (17)
sage: parent(a*a)
Finite Field in z of size 17^6
```


This doesn't happen if 17 is replaced by something much smaller.
The problem is an optimization in finite field pari element, which
has two separate parent attributes. BAD.  



---

Attachment


---

Comment by roed created at 2007-12-02 04:01:33

Looks good to me. -- David Roe


---

Comment by mabshoff created at 2007-12-02 04:53:53

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 04:53:53

Merged in 2.8.15.alpha2.
