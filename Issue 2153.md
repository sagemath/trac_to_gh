# Issue 2153: Defined Hom parent of group homomorphisms.

archive/issues_002153.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @tscrim\n\nDefined parent of a group homomorphism such that the following example\nworks (and similar for permutation groups):\n\nsage: G.<x,y> = AbelianGroup(2,[2,3]); G \nMultiplicative Abelian Group isomorphic to C2 x C3\nsage: H.<a,b,c> = AbelianGroup(3,[2,3,4]); H\nMultiplicative Abelian Group isomorphic to C2 x C3 x C4\nsage: phi = AbelianGroupMorphism(G,H,[x,y],[a,b])\nsage: phi\n\nAbelianGroup morphism:\n  From: Multiplicative Abelian Group isomorphic to C2 x C3\n  To:   Multiplicative Abelian Group isomorphic to C2 x C3 x C4\nsage: phi.parent()\nSet of Morphisms from Multiplicative Abelian Group isomorphic to C2 x C3 to Multiplicative Abelian Group isomorphic to C2 x C3 x C4 in Category of groups\nsage: Hom(G,H) == phi.parent()\nTrue\n\nIssue created by migration from https://trac.sagemath.org/ticket/2153\n\n",
    "created_at": "2008-02-13T22:42:50Z",
    "labels": [
        "group theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "Defined Hom parent of group homomorphisms.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2153",
    "user": "kohel"
}
```
Assignee: joyner

CC:  @tscrim

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

Issue created by migration from https://trac.sagemath.org/ticket/2153





---

archive/issue_comments_014129.json:
```json
{
    "body": "Attachment [group_homs.hg](tarball://root/attachments/some-uuid/ticket2153/group_homs.hg) by @mwhansen created at 2008-02-14 07:19:14",
    "created_at": "2008-02-14T07:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14129",
    "user": "@mwhansen"
}
```

Attachment [group_homs.hg](tarball://root/attachments/some-uuid/ticket2153/group_homs.hg) by @mwhansen created at 2008-02-14 07:19:14



---

archive/issue_comments_014130.json:
```json
{
    "body": "Apply aa5061b07eef.  Documentation and tests are fantastic!\n\n45b75671c677 and 25e03ebc5b0d appear to be the same.  Whether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.\n\n02e052cfe50a should be applied, although I don't like leaving commented code around.",
    "created_at": "2008-02-15T04:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14130",
    "user": "@ncalexan"
}
```

Apply aa5061b07eef.  Documentation and tests are fantastic!

45b75671c677 and 25e03ebc5b0d appear to be the same.  Whether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.

02e052cfe50a should be applied, although I don't like leaving commented code around.



---

archive/issue_comments_014131.json:
```json
{
    "body": "BTW, why isn't the motivating example a doctest in the attached patch?",
    "created_at": "2008-02-15T04:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14131",
    "user": "@ncalexan"
}
```

BTW, why isn't the motivating example a doctest in the attached patch?



---

archive/issue_comments_014132.json:
```json
{
    "body": "#1840 is aa5061b07eef.\n\n#1893 is 45b75671c677 and 25e03ebc5b0d.\n\nSo the only new patch is 02e052cfe50a.",
    "created_at": "2008-02-15T04:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14132",
    "user": "@ncalexan"
}
```

#1840 is aa5061b07eef.

#1893 is 45b75671c677 and 25e03ebc5b0d.

So the only new patch is 02e052cfe50a.



---

archive/issue_comments_014133.json:
```json
{
    "body": "There are various points raised in the previous comments which should be addressed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-12T01:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14133",
    "user": "mabshoff"
}
```

There are various points raised in the previous comments which should be addressed.

Cheers,

Michael



---

archive/issue_comments_014134.json:
```json
{
    "body": "Attachment [9271.patch](tarball://root/attachments/some-uuid/ticket2153/9271.patch) by @wdjoyner created at 2008-04-06 00:56:35\n\ntried to create patch based on sage-3.0.alphaa0 from code D Kohel sent",
    "created_at": "2008-04-06T00:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14134",
    "user": "@wdjoyner"
}
```

Attachment [9271.patch](tarball://root/attachments/some-uuid/ticket2153/9271.patch) by @wdjoyner created at 2008-04-06 00:56:35

tried to create patch based on sage-3.0.alphaa0 from code D Kohel sent



---

archive/issue_comments_014135.json:
```json
{
    "body": "Maybe others could apply the bundle but I could not. I asked David Kohel for his code, which he emailed me. I tried to create a patch from that. It seems to pass sage -t (I cannot get sage -testall to work without locking up on this machine).  Since I get\n\n\n```\nsage: G.<x,y> = AbelianGroup(2,[2,3]); G\nMultiplicative Abelian Group isomorphic to C2 x C3\nsage: H.<a,b,c> = AbelianGroup(3,[2,3,4]); H\nMultiplicative Abelian Group isomorphic to C2 x C3 x C4\nsage: phi = AbelianGroupMorphism(G,H,[x,y],[a,b])\nsage: phi\n<sage.groups.abelian_gps.abelian_group_morphism.AbelianGroupMorphism instance at 0x364cef0>\nsage: phi.parent()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/mnt/drive_hda1/sagefiles/sage-3.0.alpha0/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: AbelianGroupMorphism instance has no attribute 'parent'\n```\n\nI apparently made a mistake somewhere....",
    "created_at": "2008-04-06T01:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14135",
    "user": "@wdjoyner"
}
```

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

archive/issue_comments_014136.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2015-04-13T16:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14136",
    "user": "@mezzarobba"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_014137.json:
```json
{
    "body": "The example in the description now works. In there still something to be done here?",
    "created_at": "2015-04-13T16:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14137",
    "user": "@mezzarobba"
}
```

The example in the description now works. In there still something to be done here?



---

archive/issue_comments_014138.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2018-01-17T13:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14138",
    "user": "@fchapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_014139.json:
```json
{
    "body": "I have added the example as a doctest. \n\nI also took the opportunity to make small improvements in the same file.\n----\nNew commits:",
    "created_at": "2018-01-17T13:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14139",
    "user": "@fchapoton"
}
```

I have added the example as a doctest. 

I also took the opportunity to make small improvements in the same file.
----
New commits:



---

archive/issue_comments_014140.json:
```json
{
    "body": "green bot",
    "created_at": "2018-01-17T14:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14140",
    "user": "@fchapoton"
}
```

green bot



---

archive/issue_comments_014141.json:
```json
{
    "body": "Did you consider using libgap instead of moving strings around?\nGuess one could leave it for a different ticket.",
    "created_at": "2018-01-19T17:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14141",
    "user": "@simonbrandhorst"
}
```

Did you consider using libgap instead of moving strings around?
Guess one could leave it for a different ticket.



---

archive/issue_comments_014142.json:
```json
{
    "body": "It would be certainly much better with libgap, but I am not able to do that, so better keep it for another ticket and for somebody else, yes.",
    "created_at": "2018-01-19T19:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14142",
    "user": "@fchapoton"
}
```

It would be certainly much better with libgap, but I am not able to do that, so better keep it for another ticket and for somebody else, yes.



---

archive/issue_comments_014143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-01-21T19:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14143",
    "user": "@simonbrandhorst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014144.json:
```json
{
    "body": "The class is still a mess but it is certainly better with the cleanup than without.\n\nPositive review.",
    "created_at": "2018-01-21T19:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14144",
    "user": "@simonbrandhorst"
}
```

The class is still a mess but it is certainly better with the cleanup than without.

Positive review.



---

archive/issue_comments_014145.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-01-27T16:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14145",
    "user": "@vbraun"
}
```

Resolution: fixed
