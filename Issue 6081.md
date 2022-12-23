# Issue 6081: [with patch, needs review] make abelian categories abelian

Issue created by migration from https://trac.sagemath.org/ticket/6081

Original creator: jhpalmieri

Original creation time: 2009-05-19 03:53:34

Assignee: tbd

As reported [on sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/ea99b379e5b1b8ab): 

```
sage: RingModules(ZZ).is_abelian() 
False 
sage: AbelianGroups().is_abelian()
False
```

The attached patch should fix this.


---

Attachment


---

Comment by AlexGhitza created at 2009-05-30 08:22:30

This applies cleanly to 4.0.rc2 and passes doctests.  It looks good to me, but someone with a better overview should decide whether to merge it or just wait for the new category code to be merged.


---

Comment by mhansen created at 2009-06-04 18:29:43

Merged in 4.0.1.rc1.


---

Comment by mhansen created at 2009-06-04 18:29:43

Resolution: fixed


---

Comment by nthiery created at 2009-06-09 22:28:27

LARGE GRUMBLE.

Was it really that urgent to integrate this in????? 

I said I was going to handle it.

Now I again need to rebase the category code + work around the compatibility in the sage-combinat patches.


---

Comment by mhansen created at 2009-06-09 22:41:19

There wasn't any comment on the ticket saying that it shouldn't be merged.  It had a positive review and fixed a bug that someone actually encountered.  I guess I'm just so used to rebasing things that I don't think anything of it.  Sorry about that.


---

Comment by nthiery created at 2009-06-09 23:07:39

Alex had asked explicitly whether this should wait for the category code to be merged.

Oh well.

Btw: other than that, I truly appreciated the hard work you did put into making this release happen!
