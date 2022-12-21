# Issue 2153: Defined Hom parent of group homomorphisms.

Issue created by migration from Trac.

Original creator: kohel

Original creation time: 2008-02-13 22:42:50

Assignee: joyner

CC:  tscrim

Defined parent of a group homomorphism such that the following example
works (and similar for permutation groups):

sage: G.<x,y> = AbelianGroup(2,[2,3]); G 
Multiplicative Abelian Group isomorphic to C2 x C3
sage: H.<a,b,c> = AbelianGroup(3,[2,3,4]); H
Multiplicative Abelian Group isomorphic to C2 x C3 x C4
sage: phi = AbelianGroupMorphism(G,H,[x,y],[a,b])
sage: phi

AbelianGroup morphism:
  From: Multiplicative Abelian Group isomorphic to C2 x C3
  To:   Multiplicative Abelian Group isomorphic to C2 x C3 x C4
sage: phi.parent()
Set of Morphisms from Multiplicative Abelian Group isomorphic to C2 x C3 to Multiplicative Abelian Group isomorphic to C2 x C3 x C4 in Category of groups
sage: Hom(G,H) == phi.parent()
True


---

Attachment


---

Comment by ncalexan created at 2008-02-15 04:29:35

Apply aa5061b07eef.  Documentation and tests are fantastic!

45b75671c677 and 25e03ebc5b0d appear to be the same.  Whether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.

02e052cfe50a should be applied, although I don't like leaving commented code around.


---

Comment by ncalexan created at 2008-02-15 04:31:45

BTW, why isn't the motivating example a doctest in the attached patch?


---

Comment by ncalexan created at 2008-02-15 04:47:29

#1840 is aa5061b07eef.

#1893 is 45b75671c677 and 25e03ebc5b0d.

So the only new patch is 02e052cfe50a.


---

Comment by mabshoff created at 2008-03-12 01:08:04

There are various points raised in the previous comments which should be addressed.

Cheers,

Michael


---

Attachment

tried to create patch based on sage-3.0.alphaa0 from code D Kohel sent


---

Comment by wdj created at 2008-04-06 01:01:51

Maybe others could apply the bundle but I could not. I asked David Kohel for his code, which he emailed me. I tried to create a patch from that. It seems to pass sage -t (I cannot get sage -testall to work without locking up on this machine).  Since I get


```
sage: G.<x,y> = AbelianGroup(2,[2,3]); G
Multiplicative Abelian Group isomorphic to C2 x C3
sage: H.<a,b,c> = AbelianGroup(3,[2,3,4]); H
Multiplicative Abelian Group isomorphic to C2 x C3 x C4
sage: phi = AbelianGroupMorphism(G,H,[x,y],[a,b])
sage: phi
<sage.groups.abelian_gps.abelian_group_morphism.AbelianGroupMorphism instance at 0x364cef0>
sage: phi.parent()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/mnt/drive_hda1/sagefiles/sage-3.0.alpha0/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: AbelianGroupMorphism instance has no attribute 'parent'
```

I apparently made a mistake somewhere....


---

Comment by mmezzarobba created at 2015-04-13 16:21:38

Changing status from needs_work to needs_info.


---

Comment by mmezzarobba created at 2015-04-13 16:21:38

The example in the description now works. In there still something to be done here?


---

Comment by chapoton created at 2018-01-17 13:35:30

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2018-01-17 13:35:30

I have added the example as a doctest. 

I also took the opportunity to make small improvements in the same file.
----
New commits:


---

Comment by chapoton created at 2018-01-17 14:39:47

green bot


---

Comment by sbrandhorst created at 2018-01-19 17:18:20

Did you consider using libgap instead of moving strings around?
Guess one could leave it for a different ticket.


---

Comment by chapoton created at 2018-01-19 19:11:54

It would be certainly much better with libgap, but I am not able to do that, so better keep it for another ticket and for somebody else, yes.


---

Comment by sbrandhorst created at 2018-01-21 19:36:13

Changing status from needs_review to positive_review.


---

Comment by sbrandhorst created at 2018-01-21 19:36:13

The class is still a mess but it is certainly better with the cleanup than without.

Positive review.


---

Comment by vbraun created at 2018-01-27 16:00:08

Resolution: fixed
