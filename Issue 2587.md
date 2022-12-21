# Issue 2587: [with 2-line patch, needs review] subgroup of a permutation group is so slow it's silly

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-03-18 17:07:41

Assignee: joyner

The setup:

```
sage: C = QuadraticResidueCode(7, GF(2))
sage: G = C.permutation_automorphism_group()
sage: G.order()
168
```

Before:

```
sage: time SG = G.subgroup(list(G.gens()[:3]))
CPU times: user 0.86 s, sys: 0.34 s, total: 1.20 s
Wall time: 1.24
```

After:

```
sage: time SG = G.subgroup(list(G.gens()[:3]))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
```



---

Attachment

This looks good and works for me.


---

Comment by mabshoff created at 2008-03-19 00:29:55

Merged in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-19 00:29:55

Resolution: fixed
