# Issue 2089: major finite field printing (?) bug

Issue created by migration from https://trac.sagemath.org/ticket/2089

Original creator: was

Original creation time: 2008-02-07 22:12:40

Assignee: somebody

In sage-2.10.1

```
sage: sage: F.<u> = GF(2^20)
sage: sage: F.gens()
(a,)
sage: u^3
u^3
sage: u
a
```



---

Comment by was created at 2008-02-07 22:13:11

Changing assignee from somebody to malb.


---

Comment by AlexGhitza created at 2008-02-17 23:04:49


```
sage: GF(2**15, 'u').gens()
(u,)
sage: GF(3**15, 'u').gens()
(u,)
sage: GF(2**16, 'u').gens()
(a,)
```


Conclusion: this only happens for GF(2**n) when n>=16, so FiniteField_ntl_gf2e is at fault here.  I've stared at it for a while now and I have no idea what's wrong.


---

Comment by malb created at 2008-02-18 15:16:41

fix


---

Attachment

The attached patch fixes the issue for me.


---

Comment by malb created at 2008-02-18 15:17:16

Changing status from new to assigned.


---

Comment by was created at 2008-02-19 02:38:52

Perfect.


---

Comment by mabshoff created at 2008-02-19 15:00:23

Resolution: fixed


---

Comment by mabshoff created at 2008-02-19 15:00:23

Merged in Sage 2.10.2.alpha1
