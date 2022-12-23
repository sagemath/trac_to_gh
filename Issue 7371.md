# Issue 7371: rename quotient_group() to quotient() in groups/perm_gps/permgroup.py

Issue created by migration from https://trac.sagemath.org/ticket/7371

Original creator: AlexGhitza

Original creation time: 2009-11-01 22:29:41

Assignee: joyner

There is a generic group method called `quotient`, which is meant to return the quotient group by a normal subgroup, and is meant to be overridden by inheriting classes.  However, the corresponding method for permutation groups is called `quotient_group` instead:


```
sage: S = SymmetricGroup(6)
sage: N = S.normal_subgroups()[1]
sage: S.quotient(N)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/674/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-stable/local/lib/python2.6/site-packages/sage/groups/group.so in sage.groups.group.Group.quotient (sage/groups/group.c:1719)()

NotImplementedError: 
sage: S.quotient_group(N)
Permutation Group with generators [(), (1,2)]
```


The attached patch renames the permutation group method to `quotient` and deprecates `quotient_group`.



---

Attachment


---

Comment by AlexGhitza created at 2009-11-01 23:13:44

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-17 12:10:28

Looks good to me.


---

Comment by mhansen created at 2009-11-17 12:10:28

Resolution: fixed
