# Issue 2153: Defined Hom parent of group homomorphisms.

archive/issues_002153.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @tscrim\n\nDefined parent of a group homomorphism such that the following example\nworks (and similar for permutation groups):\n\nsage: G.<x,y> = AbelianGroup(2,[2,3]); G \nMultiplicative Abelian Group isomorphic to C2 x C3\nsage: H.<a,b,c> = AbelianGroup(3,[2,3,4]); H\nMultiplicative Abelian Group isomorphic to C2 x C3 x C4\nsage: phi = AbelianGroupMorphism(G,H,[x,y],[a,b])\nsage: phi\n\nAbelianGroup morphism:\n  From: Multiplicative Abelian Group isomorphic to C2 x C3\n  To:   Multiplicative Abelian Group isomorphic to C2 x C3 x C4\nsage: phi.parent()\nSet of Morphisms from Multiplicative Abelian Group isomorphic to C2 x C3 to Multiplicative Abelian Group isomorphic to C2 x C3 x C4 in Category of groups\nsage: Hom(G,H) == phi.parent()\nTrue\n\nIssue created by migration from https://trac.sagemath.org/ticket/2153\n\n",
    "created_at": "2008-02-13T22:42:50Z",
    "labels": [
        "component: group theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "Defined Hom parent of group homomorphisms.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2153",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
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

archive/issue_comments_014098.json:
```json
{
    "body": "Attachment [group_homs.hg](tarball://root/attachments/some-uuid/ticket2153/group_homs.hg) by @mwhansen created at 2008-02-14 07:19:14",
    "created_at": "2008-02-14T07:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14098",
    "user": "https://github.com/mwhansen"
}
```

Attachment [group_homs.hg](tarball://root/attachments/some-uuid/ticket2153/group_homs.hg) by @mwhansen created at 2008-02-14 07:19:14



---

archive/issue_comments_014099.json:
```json
{
    "body": "Apply aa5061b07eef.  Documentation and tests are fantastic!\n\n45b75671c677 and 25e03ebc5b0d appear to be the same.  Whether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.\n\n02e052cfe50a should be applied, although I don't like leaving commented code around.",
    "created_at": "2008-02-15T04:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14099",
    "user": "https://github.com/ncalexan"
}
```

Apply aa5061b07eef.  Documentation and tests are fantastic!

45b75671c677 and 25e03ebc5b0d appear to be the same.  Whether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.

02e052cfe50a should be applied, although I don't like leaving commented code around.



---

archive/issue_comments_014100.json:
```json
{
    "body": "BTW, why isn't the motivating example a doctest in the attached patch?",
    "created_at": "2008-02-15T04:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14100",
    "user": "https://github.com/ncalexan"
}
```

BTW, why isn't the motivating example a doctest in the attached patch?



---

archive/issue_comments_014101.json:
```json
{
    "body": "#1840 is aa5061b07eef.\n\n#1893 is 45b75671c677 and 25e03ebc5b0d.\n\nSo the only new patch is 02e052cfe50a.",
    "created_at": "2008-02-15T04:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14101",
    "user": "https://github.com/ncalexan"
}
```

#1840 is aa5061b07eef.

#1893 is 45b75671c677 and 25e03ebc5b0d.

So the only new patch is 02e052cfe50a.



---

archive/issue_comments_014102.json:
```json
{
    "body": "There are various points raised in the previous comments which should be addressed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-12T01:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are various points raised in the previous comments which should be addressed.

Cheers,

Michael



---

archive/issue_events_005148.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:03:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5148"
}
```



---

archive/issue_comments_014103.json:
```json
{
    "body": "Attachment [9271.patch](tarball://root/attachments/some-uuid/ticket2153/9271.patch) by @wdjoyner created at 2008-04-06 00:56:35\n\ntried to create patch based on sage-3.0.alphaa0 from code D Kohel sent",
    "created_at": "2008-04-06T00:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14103",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [9271.patch](tarball://root/attachments/some-uuid/ticket2153/9271.patch) by @wdjoyner created at 2008-04-06 00:56:35

tried to create patch based on sage-3.0.alphaa0 from code D Kohel sent



---

archive/issue_comments_014104.json:
```json
{
    "body": "Maybe others could apply the bundle but I could not. I asked David Kohel for his code, which he emailed me. I tried to create a patch from that. It seems to pass sage -t (I cannot get sage -testall to work without locking up on this machine).  Since I get\n\n\n```\nsage: G.<x,y> = AbelianGroup(2,[2,3]); G\nMultiplicative Abelian Group isomorphic to C2 x C3\nsage: H.<a,b,c> = AbelianGroup(3,[2,3,4]); H\nMultiplicative Abelian Group isomorphic to C2 x C3 x C4\nsage: phi = AbelianGroupMorphism(G,H,[x,y],[a,b])\nsage: phi\n<sage.groups.abelian_gps.abelian_group_morphism.AbelianGroupMorphism instance at 0x364cef0>\nsage: phi.parent()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/mnt/drive_hda1/sagefiles/sage-3.0.alpha0/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: AbelianGroupMorphism instance has no attribute 'parent'\n```\n\nI apparently made a mistake somewhere....",
    "created_at": "2008-04-06T01:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14104",
    "user": "https://github.com/wdjoyner"
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

archive/issue_events_005149.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5149"
}
```



---

archive/issue_events_005150.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5150"
}
```



---

archive/issue_events_005151.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5151"
}
```



---

archive/issue_events_005152.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5152"
}
```



---

archive/issue_events_005153.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5153"
}
```



---

archive/issue_events_005154.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5154"
}
```



---

archive/issue_events_005155.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5155"
}
```



---

archive/issue_events_005156.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5156"
}
```



---

archive/issue_comments_014105.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2015-04-13T16:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14105",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_014106.json:
```json
{
    "body": "The example in the description now works. In there still something to be done here?",
    "created_at": "2015-04-13T16:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14106",
    "user": "https://github.com/mezzarobba"
}
```

The example in the description now works. In there still something to be done here?



---

archive/issue_comments_014107.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2018-01-17T13:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14107",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_014108.json:
```json
{
    "body": "I have added the example as a doctest. \n\nI also took the opportunity to make small improvements in the same file.\n----\nNew commits:",
    "created_at": "2018-01-17T13:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14108",
    "user": "https://github.com/fchapoton"
}
```

I have added the example as a doctest. 

I also took the opportunity to make small improvements in the same file.
----
New commits:



---

archive/issue_events_005157.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-01-17T13:35:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5157"
}
```



---

archive/issue_events_005158.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-01-17T13:35:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "milestone": "sage-8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5158"
}
```



---

archive/issue_comments_014109.json:
```json
{
    "body": "green bot",
    "created_at": "2018-01-17T14:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14109",
    "user": "https://github.com/fchapoton"
}
```

green bot



---

archive/issue_comments_014110.json:
```json
{
    "body": "Did you consider using libgap instead of moving strings around?\nGuess one could leave it for a different ticket.",
    "created_at": "2018-01-19T17:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14110",
    "user": "https://github.com/simonbrandhorst"
}
```

Did you consider using libgap instead of moving strings around?
Guess one could leave it for a different ticket.



---

archive/issue_comments_014111.json:
```json
{
    "body": "It would be certainly much better with libgap, but I am not able to do that, so better keep it for another ticket and for somebody else, yes.",
    "created_at": "2018-01-19T19:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14111",
    "user": "https://github.com/fchapoton"
}
```

It would be certainly much better with libgap, but I am not able to do that, so better keep it for another ticket and for somebody else, yes.



---

archive/issue_comments_014112.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-01-21T19:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14112",
    "user": "https://github.com/simonbrandhorst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014113.json:
```json
{
    "body": "The class is still a mess but it is certainly better with the cleanup than without.\n\nPositive review.",
    "created_at": "2018-01-21T19:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14113",
    "user": "https://github.com/simonbrandhorst"
}
```

The class is still a mess but it is certainly better with the cleanup than without.

Positive review.



---

archive/issue_comments_014114.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-01-27T16:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2153#issuecomment-14114",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_005159.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2018-01-27T16:00:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2153",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2153#event-5159"
}
```
