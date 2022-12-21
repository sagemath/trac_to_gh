# Issue 243: two permutation group bugs: __contains__ hangs.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-04 22:51:48

Assignee: somebody

From David Kohel

```
sage: G = SymmetricGroup(16)
sage: g = G.random() # note random_element doesn't exist which seems to be the SAGE preference
sage: parent(g) is G
True
sage: parent(g) == G
True
sage: g in G # hangs despite the above...not sure where it goes wrong
```



---

Comment by was created at 2007-02-05 07:23:09

Resolution: fixed


---

Comment by was created at 2007-02-05 07:23:09

David Kohel fixed this.
