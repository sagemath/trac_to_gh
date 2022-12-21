# Issue 2582: [with patch, needs review] fix bug in PermutationGroupElement

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-03-18 07:29:53

Assignee: robertwb


```
sage: PermutationGroupElement([1,2,4,3,5])
---------------------------------------------------------------------------
<type 'exceptions.AssertionError'>        Traceback (most recent call last)

/Users/rlmill/sage-2.10.4/<ipython console> in <module>()

/Users/rlmill/sage-2.10.4/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()

<type 'exceptions.AssertionError'>: 
```



---

Attachment


---

Comment by mabshoff created at 2008-03-18 10:17:45

Merged in Sage 2.11.alpha0.


---

Comment by mabshoff created at 2008-03-18 10:17:45

Resolution: fixed


---

Comment by mabshoff created at 2008-03-18 10:19:13

For the record: You posted a GNU patch and not a mercurial patch, so I ended up with credit in the hg log :). I need to start looking at patches before I merge so that this doesn't happen again. Note: you can export mercurial patches from mercurial ques.

Cheers,

Michael
