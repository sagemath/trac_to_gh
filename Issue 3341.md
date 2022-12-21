# Issue 3341: fix minor issue with creating skew partitions by dividng partitions

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-05-31 06:56:01

Assignee: mhansen

CC:  sage-combinat


```
sage: Partition([2,1])/Partition([1])
/home/was/s/local/lib/python2.5/site-packages/sage/combinat/partition.py in __div__(self, p)
    325             
    326         """
--> 327         if not self.dominates(Partition_class(p)):
    328             raise ValueError, "the partition must dominate p"
    329 

/home/was/s/local/lib/python2.5/site-packages/sage/combinat/combinat.py in __init__(self, l)
    546         """
    547         if not isinstance(l, list):
--> 548             raise ValueError, 'l must be a list'
    549         self._list = l
    550         self._hash = None

ValueError: l must be a list
```





---

Attachment


---

Comment by mhansen created at 2008-05-31 06:59:54

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-06-15 22:01:10

Changing keywords from "" to "editor_mhansen".


---

Comment by malb created at 2008-06-19 20:44:24

good work.


---

Comment by mabshoff created at 2008-06-23 07:37:25

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 07:37:25

Merged in Sage 3.0.4.alpha0
