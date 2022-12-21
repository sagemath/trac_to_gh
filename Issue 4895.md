# Issue 4895: bug in pattern avoiding permutations

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2008-12-31 01:54:19

Assignee: mhansen

CC:  jbandlow sage-combinat

Keywords: pattern avoiding permutations

The following behavior is clearly bad:

```
sage: [p for p in Permutations(4,avoiding=[2,3,1]) if p.has_pattern([2,3,1])]               
[[2, 3, 1, 4], [4, 2, 3, 1]]
```


Similar behavior occurs when avoiding [1,3,2], [2,1,3], and [3,1,2].


---

Attachment

The problem was a simple typo in an initial condition (combined with a bunch of doctests that tested for incorrect behavior).  Warning: I've been travelling and not had an opportunity to upgrade sage recently, so this patch is based off 3.2.1.  I don't expect this to be a problem, but if the patch does not apply, let me know and I will fix it as soon as possible.


---

Comment by jbandlow created at 2009-01-15 07:55:44

Changing assignee from mhansen to jbandlow.


---

Comment by mhansen created at 2009-01-24 03:02:16

Nice work Jason.


---

Comment by mabshoff created at 2009-01-25 02:20:55

Resolution: fixed


---

Comment by mabshoff created at 2009-01-25 02:20:55

Merged in Sage 3.3.alpha2.

Cheers,

Michael
