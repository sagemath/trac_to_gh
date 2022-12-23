# Issue 2853: A correction to the weight of crystal elements for type A and a speedup for all types

Issue created by migration from https://trac.sagemath.org/ticket/2853

Original creator: bump

Original creation time: 2008-04-08 05:55:37

Assignee: mhansen

CC:  sage-combinat

For Cartan Types 'A' a problem with the weight function of crystals was described here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en

The method of correcting this problem was to hard-code the weight in the crystals of letters, 
and to have the crystals of tensors get the weight of a tensor element by summing the weights 
of its constituents. This alters the weight for Type A (correcting the defect) and returns the
same weight as the old algorithm for other Cartan types.

When the patch was implemented it was found to be 2-3 times faster than the old algorithm.


---

Comment by bump created at 2008-04-08 05:58:21

patch correcting problem with weights for crystal graphs of type A and speeding up all Cartan types.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-04-08 09:32:29

Hi Dan,

I've updated a patch to move the tests for .weight() to the docstring for the definition of weight.  There is an issue with ['G',2] though:


Before the patch:

```
sage: C = CrystalOfLetters(['G',2])
sage: hwvs = C.highest_weight_vectors()
sage: wlr = C.weight_lattice_realization()
sage: v = hwvs[0]; v
1
sage: v.weight()
(1, 0, -1)
sage: wlr.weyl_dimension(v.weight())
7
```


After the patch:

```
sage: C = CrystalOfLetters(['G',2])
sage: wlr = C.weight_lattice_realization()
sage: hwvs = C.highest_weight_vectors()
sage: hwvs
[1]
sage: v = hwvs[0]; v
1
sage: v.weight()
(-1, 0, 1)
sage: wlr.weyl_dimension(v.weight())
0
```



---

Comment by bump created at 2008-04-08 16:41:13

I was unable to confirm the problem with G2. I applied the patch in the modified form
that you posted, and sage: wlr.weyl_dimension(v.weight()) returns 7 for me.

Dan


---

Comment by mabshoff created at 2008-04-08 17:06:31

Replying to [comment:3 bump]:
> I was unable to confirm the problem with G2. I applied the patch in the modified form
> that you posted, and sage: wlr.weyl_dimension(v.weight()) returns 7 for me.
> 
> Dan

Hi Dan,

I can confirm that with 3.0.alpha2 and your patch applied wlr.weyl_dimension(v.weight()) returns 0. With what build did you try? Are there any other patches you have in your tree?

Cheers,

Michael


---

Comment by bump created at 2008-04-08 19:49:11

> Hi Dan,
> 
> I can confirm that with 3.0.alpha2 and your patch applied wlr.weyl_dimension(v.weight()) returns 0. With what build did you try? Are there any other patches you have in your tree?
> 
> Cheers,
> 
> Michael

I did this with 3.0-alph0 and no other patches. I can install 3.0.alpha2 and debug the patch.

Dan


---

Attachment

It turns out that I had forgotten the G2 patch that went in on Saturday.

I corrected the patch and added it as 2853.1.patch. I believe it is now
correct.

Dan


---

Comment by mhansen created at 2008-04-08 23:22:51

Looks good to me.  Apply just 2853.1.patch.


---

Comment by mabshoff created at 2008-04-09 00:11:46

Resolution: fixed


---

Comment by mabshoff created at 2008-04-09 00:11:46

Merged in Sage 3.0.alpha3.
