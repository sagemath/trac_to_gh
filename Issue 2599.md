# Issue 2599: Permutation -> PermutationGroupElement fails for the identity

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-03-19 18:46:00

Assignee: mhansen

CC:  sage-combinat


```
sage: Permutation([1,2,3]).to_permutation_group_element()
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/<ipython console> in <module>()

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/combinat/permutation.py in to_permutation_group_element(self)
    438         """
    439 
--> 440         return PermutationGroupElement(self.to_cycles(singletons=False))
    441 
    442     def signature(p):

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.gap_format()

<type 'exceptions.IndexError'>: list index out of range
```



---

Attachment


---

Comment by mhansen created at 2008-03-19 19:03:02

Changing status from new to assigned.


---

Comment by malb created at 2008-03-21 02:17:47

The patch does what it advertises and doctests that behavior. All good, I say apply. One could replace the '()' by () though to gain a little speed.


---

Comment by mabshoff created at 2008-03-21 02:25:11

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-21 02:25:11

Resolution: fixed
