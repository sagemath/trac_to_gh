# Issue 4410: [with patch, needs review] Map.__pow__ should return identity for power 0

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-10-31 09:05:10

Assignee: burcin

CC:  robertwb

`sage.categories.map.Map.__pow__` calls `generic_power`, which messes up power 0. There is this todo note there:


```
        # todo -- what about the case n=0 -- need to specify the identity map somehow.
```


Attached patch returns the identity map for power 0.


---

Comment by burcin created at 2008-10-31 09:06:10

make Map.__pow__ return identity for power 0


---

Attachment

This is the suggested fix discussed by RobertWB and Burcin in IRC last night. The code looks correct and passes doctests, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 15:36:46

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 15:36:46

Resolution: fixed
