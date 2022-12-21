# Issue 4581: Permutation constructor fails with PermutationGroupElement

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2008-11-22 01:45:10

Assignee: mhansen

CC:  rlm sage-combinat

Since PermutationGroupElement accepts Permutations:

```
sage: PermutationGroupElement(Permutation([2,1,3]))
(1,2)
```

it would be good if the other direction worked as well:

```
sage: g = PermutationGroupElement([2,1,3])
sage: g
(1,2)
sage: Permutation(g)
...
ValueError: l must be a list
```

The following works:

```
sage: Permutation(g.list())
[2, 1, 3]
```



---

Comment by mhansen created at 2008-12-02 08:51:03

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-12-02 15:55:52

rlm, 

I know you are busy, but can you give this a review? :)

Cheers,

Michael


---

Comment by saliola created at 2008-12-02 16:18:29

The patch applies successfully and doctests pass here.


---

Comment by mabshoff created at 2008-12-04 13:35:02

Resolution: fixed


---

Comment by mabshoff created at 2008-12-04 13:35:02

Merged in Sage 3.2.2.alpha0
