# Issue 2238: [with trivial patch, needs review] doctest failure in sage 2.10.2.alpha1: const.tex

Issue created by migration from https://trac.sagemath.org/ticket/2238

Original creator: AlexGhitza

Original creation time: 2008-02-20 23:00:49

Assignee: tba

Hi,

Computing the points on elliptic curves over finite fields goes through finding the structure of the corresponding abelian group, and the code picks random generators for this.  Therefore the particular generators displayed, and the order in which the set of points is listed, vary from run to run.

This sometimes causes doctest failures on the examples in const.tex; I added comments containing the word "random" so that this doesn't happen.

Alex



---

Attachment


---

Comment by was created at 2008-02-20 23:12:17

1. The right solution is to always *SORT* the output if possible (which it is), so there is nothing random involved.

2. And 2, my red flag went off when I saw list. Check out this bug!

```
sage: E = EllipticCurve(GF(5),[0, -1, 1, -10, -20]) 
sage: w = E.points(); w
[(0 : 1 : 0), (0 : 0 : 1), (1 : 4 : 1), (1 : 0 : 1), (0 : 4 : 1)]
sage: w[0] = 15
sage: E.points()
[15, (0 : 0 : 1), (1 : 4 : 1), (1 : 0 : 1), (0 : 4 : 1)]
```


I'll post a patch to fix both issues.


---

Comment by was created at 2008-02-21 00:21:29

this and doc-2238.patch should replace the above patch (apply this to sage repo; and doc to doc repo)


---

Attachment


---

Attachment


---

Comment by was created at 2008-02-21 00:21:56

Changing priority from major to blocker.


---

Attachment

replace sage-2238.patch


---

Comment by AlexGhitza created at 2008-02-21 02:57:05

Looks great; unfortunately it breaks another doctest (trivial to fix, so I've done it and put in a new patch replacing sage-2238.patch).  The doc-2238.patch looks fine.


---

Comment by mabshoff created at 2008-02-21 03:05:09

Resolution: fixed


---

Comment by mabshoff created at 2008-02-21 03:05:09

Merged sage-2238.patch and sage-2238-new.patch in Sage 2.10.2.alpah2


---

Comment by cremona created at 2008-03-02 17:11:01

Thanks to Alex and William for fixing these things which were caused by me:  as a relative novice to Python I am not aware as I should be of the critical differences between lists and tuples!  And the need to sort things to be canonical.

I'm not sure what the correct milestone is for this, certainly not 2.10.2, and it's not in 2.10.3.rc0 either, but not for lack of positive reviews.


---

Comment by mabshoff created at 2008-03-02 17:25:14

Replying to [comment:6 cremona]:
> Thanks to Alex and William for fixing these things which were caused by me:  as a relative novice to Python I am not aware as I should be of the critical differences between lists and tuples!  And the need to sort things to be canonical.
> 
> I'm not sure what the correct milestone is for this, certainly not 2.10.2, and it's not in 2.10.3.rc0 either, but not for lack of positive reviews.
> 

I check my 2.10.3.rc1 and:

 * sage-2238-new.patch is "changeset: 8647:97976cb27ad3" in the sage repo (this is in the 2.10.2 release time frame)
 * doc-2238.patch is "changeset: 429:3a30bbba6c29" in the doc repo (this is in the 2.10.2 release time frame)

So, I am sure both patches have been applied. 

Cheers,

Michael
