# Issue 5314: [with patch, needs review] The empty permutations exists !

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-02-19 19:33:12

Assignee: hivert

CC:  sage-combinat

Keywords: permutations, empty

Right now sage consider that there is no empty permutations.

```
sage: [] in Permutations()
False
```

There seems to be an agreement about the fact that the empty permutations exists ! Indeed there exists an empty set, and there exits exactly one function from the empty set to itself which is clearly bijective.

The patch solve this defect:

```
sage: import sage_emacs as emacs
sage: [] in Permutations()
True
sage: Permutations(0).list()
[[]]
sage: Permutations(0).count()
1
```


Author: Florent Hivert



---

Comment by hivert created at 2009-02-19 19:34:02

Patch proposal


---

Comment by mhansen created at 2009-02-19 19:37:56

Changing assignee from hivert to mhansen.


---

Comment by mhansen created at 2009-02-19 19:37:56

Changing status from new to assigned.


---

Attachment

Looks good and passes tests for me.


---

Comment by mabshoff created at 2009-02-20 07:24:22

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:24:22

Resolution: fixed
