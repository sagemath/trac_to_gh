# Issue 4326: Root systems improvements

archive/issues_004326.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nDoc:\n- Use $F_4$ instead of F4 \n\nDynkinDiagram:\n- allow for slicing notation for column/row extraction: c[i,:]\n\nAmbientSpace:\n- fundamental coweights by appropriate scaling of the fundamental weights\n- embedding coweight lattice\n\nWeightLatticeRealization\n- scalar product with coweight lattice in finite dimension\n\nGeneric:\n- (signed) reduced word for a chamber/alcove\n\nClassical case:\n- reverse map to coroot space and coroot lattice by scalar product with the fundamental weights\n- => associated coroot\n- s_\\alpha on the (co)root and (co)weight lattice for any root \\alpha\n\nAffine case:\n- analogues whenever well defined \n- reduced words for translations elements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4326\n\n",
    "created_at": "2008-10-20T08:17:24Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Root systems improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4326",
    "user": "@nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Doc:
- Use $F_4$ instead of F4 

DynkinDiagram:
- allow for slicing notation for column/row extraction: c[i,:]

AmbientSpace:
- fundamental coweights by appropriate scaling of the fundamental weights
- embedding coweight lattice

WeightLatticeRealization
- scalar product with coweight lattice in finite dimension

Generic:
- (signed) reduced word for a chamber/alcove

Classical case:
- reverse map to coroot space and coroot lattice by scalar product with the fundamental weights
- => associated coroot
- s_\alpha on the (co)root and (co)weight lattice for any root \alpha

Affine case:
- analogues whenever well defined 
- reduced words for translations elements.

Issue created by migration from https://trac.sagemath.org/ticket/4326





---

archive/issue_comments_031695.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31695",
    "user": "@nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031696.json:
```json
{
    "body": "Attachment [root_systems-4326-nt.patch](tarball://root/attachments/some-uuid/ticket4326/root_systems-4326-nt.patch) by @nthiery created at 2009-06-11 05:48:44",
    "created_at": "2009-06-11T05:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31696",
    "user": "@nthiery"
}
```

Attachment [root_systems-4326-nt.patch](tarball://root/attachments/some-uuid/ticket4326/root_systems-4326-nt.patch) by @nthiery created at 2009-06-11 05:48:44



---

archive/issue_comments_031697.json:
```json
{
    "body": "Changing keywords from \"\" to \"root systems\".",
    "created_at": "2009-06-11T05:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31697",
    "user": "@nthiery"
}
```

Changing keywords from "" to "root systems".



---

archive/issue_comments_031698.json:
```json
{
    "body": "Normally I would have waited for the category patches to be merged\nbefore reviewing this patch. However I recieved an email from Tom Boothby\nurging me to do the review now, so here it is.\n\nThis review is based on the version of the patches in the\ncombinat queue. This is because it depends on patches that\nhave not been merged yet.\n\nAfter qpushing the combinat queue up to this patch but\nnot beyond, all tests pass. This is with Sage 4.1 and\nthe last changeset is this one:\n\n\n```\nchangeset:   1520:188022ff52b9\ntag:         tip\nuser:        Nicolas M. Thiery <nthiery@users.sf.net>\ndate:        Tue Jul 21 01:13:42 2009 +0200\nsummary:     Update\n```\n\n\nThe patch adds quite a bit of new functionality for working\nwith Coxeter groups and affine Weyl groups. The following\nnew files are added. There are new categories added for\nCoxeterGroups and WeylGroups. There is an extensive\nChangeLog in the comments at the beginning of the patch.\n\nSince the patch is over 11,000 lines of code, there could\nvery well be bugs in it. However it probably does not\nintroduce significant new bugs in the portion of the\ncode that deals with classical root systems, since I\nused it extensively during the spring of 2009 in\nconnection with #5794. Every classical Cartan type\nand many reducible types have been created and worked\nwith. What problems I found then were fixed. Moreover\nthe portion of the code that deals with affine root\nsystems was similarly very tested by Anne Schilling\nin connection with affine crystals.\n\nTherefore the most uncertainty in my is with the new\nfunctionality for Coxeter groups. I will mention one\n\"wish\" in this direction, which is that in addition\nto implementing the Bruhat covers, the Bruhat order\nbe properly implemented. This could be done efficiently\nusing Proposition 1.1 in Stembridge, A Short\nDerivation of the M\u00f6bius Function for the Bruhat\nOrder, Journal of Algebraic Combinatorics 25,\n(2007).\n\nThis wish is not a reason to hold up merging the\npatch. Rather the patch should be merged as soon as\npossible and such changes can be made later.",
    "created_at": "2009-07-21T23:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31698",
    "user": "@dwbump"
}
```

Normally I would have waited for the category patches to be merged
before reviewing this patch. However I recieved an email from Tom Boothby
urging me to do the review now, so here it is.

This review is based on the version of the patches in the
combinat queue. This is because it depends on patches that
have not been merged yet.

After qpushing the combinat queue up to this patch but
not beyond, all tests pass. This is with Sage 4.1 and
the last changeset is this one:


```
changeset:   1520:188022ff52b9
tag:         tip
user:        Nicolas M. Thiery <nthiery@users.sf.net>
date:        Tue Jul 21 01:13:42 2009 +0200
summary:     Update
```


The patch adds quite a bit of new functionality for working
with Coxeter groups and affine Weyl groups. The following
new files are added. There are new categories added for
CoxeterGroups and WeylGroups. There is an extensive
ChangeLog in the comments at the beginning of the patch.

Since the patch is over 11,000 lines of code, there could
very well be bugs in it. However it probably does not
introduce significant new bugs in the portion of the
code that deals with classical root systems, since I
used it extensively during the spring of 2009 in
connection with #5794. Every classical Cartan type
and many reducible types have been created and worked
with. What problems I found then were fixed. Moreover
the portion of the code that deals with affine root
systems was similarly very tested by Anne Schilling
in connection with affine crystals.

Therefore the most uncertainty in my is with the new
functionality for Coxeter groups. I will mention one
"wish" in this direction, which is that in addition
to implementing the Bruhat covers, the Bruhat order
be properly implemented. This could be done efficiently
using Proposition 1.1 in Stembridge, A Short
Derivation of the Möbius Function for the Bruhat
Order, Journal of Algebraic Combinatorics 25,
(2007).

This wish is not a reason to hold up merging the
patch. Rather the patch should be merged as soon as
possible and such changes can be made later.



---

archive/issue_comments_031699.json:
```json
{
    "body": "Let me get this straight. Tickets #6136, #6253, #6250, and #5891 must first be merged before merging this ticket?",
    "created_at": "2009-07-23T08:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31699",
    "user": "mvngu"
}
```

Let me get this straight. Tickets #6136, #6253, #6250, and #5891 must first be merged before merging this ticket?



---

archive/issue_comments_031700.json:
```json
{
    "body": "Replying to [comment:8 mvngu]:\n> Let me get this straight. Tickets #6136, #6253, #6250, and #5891 must first be merged before merging this ticket?\n\nIndeed. Should we use a specific subject for patches that have a positive review, but have dependencies on not yet merged tickets?\nSomething like:\n\n[with patch, positive review, depends on #6136, #6253, #6250, #5891] ...",
    "created_at": "2009-07-23T08:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31700",
    "user": "@nthiery"
}
```

Replying to [comment:8 mvngu]:
> Let me get this straight. Tickets #6136, #6253, #6250, and #5891 must first be merged before merging this ticket?

Indeed. Should we use a specific subject for patches that have a positive review, but have dependencies on not yet merged tickets?
Something like:

[with patch, positive review, depends on #6136, #6253, #6250, #5891] ...



---

archive/issue_comments_031701.json:
```json
{
    "body": "Replying to [comment:9 nthiery]:\n> Indeed. Should we use a specific subject for patches that have a positive review, but have dependencies on not yet merged tickets?\n> Something like:\n> \n> [with patch, positive review, depends on #6136, #6253, #6250, #5891] ...\nNo, not really. I just want to double check since the patch is rather huge and I was concerned about it getting bit rotten. Anyway, people who uses the merge script would not be able to easily tell whether a positive-reviewed ticket has other dependencies.",
    "created_at": "2009-07-23T09:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31701",
    "user": "mvngu"
}
```

Replying to [comment:9 nthiery]:
> Indeed. Should we use a specific subject for patches that have a positive review, but have dependencies on not yet merged tickets?
> Something like:
> 
> [with patch, positive review, depends on #6136, #6253, #6250, #5891] ...
No, not really. I just want to double check since the patch is rather huge and I was concerned about it getting bit rotten. Anyway, people who uses the merge script would not be able to easily tell whether a positive-reviewed ticket has other dependencies.



---

archive/issue_comments_031702.json:
```json
{
    "body": "Latest version of the patch from the Sage-Combinat patch server (no change since Dan's review)",
    "created_at": "2009-11-06T14:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31702",
    "user": "@nthiery"
}
```

Latest version of the patch from the Sage-Combinat patch server (no change since Dan's review)



---

archive/issue_comments_031703.json:
```json
{
    "body": "Attachment [trac_4326-root_systems-nt.patch](tarball://root/attachments/some-uuid/ticket4326/trac_4326-root_systems-nt.patch) by @nthiery created at 2009-11-10 14:50:18",
    "created_at": "2009-11-10T14:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31703",
    "user": "@nthiery"
}
```

Attachment [trac_4326-root_systems-nt.patch](tarball://root/attachments/some-uuid/ticket4326/trac_4326-root_systems-nt.patch) by @nthiery created at 2009-11-10 14:50:18



---

archive/issue_comments_031704.json:
```json
{
    "body": "Fix ClassicalWeylSubgroup and remove unneeded long time, as spotted by Mike",
    "created_at": "2009-11-18T13:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31704",
    "user": "@nthiery"
}
```

Fix ClassicalWeylSubgroup and remove unneeded long time, as spotted by Mike



---

archive/issue_comments_031705.json:
```json
{
    "body": "Attachment [trac_4326-root_systems-fix-nt.patch](tarball://root/attachments/some-uuid/ticket4326/trac_4326-root_systems-fix-nt.patch) by @nthiery created at 2009-11-18 13:27:39",
    "created_at": "2009-11-18T13:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31705",
    "user": "@nthiery"
}
```

Attachment [trac_4326-root_systems-fix-nt.patch](tarball://root/attachments/some-uuid/ticket4326/trac_4326-root_systems-fix-nt.patch) by @nthiery created at 2009-11-18 13:27:39



---

archive/issue_comments_031706.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-18T13:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31706",
    "user": "@nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_031707.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-18T13:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31707",
    "user": "@nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_031708.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-18T13:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31708",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031709.json:
```json
{
    "body": "The new patch looks okay to me.",
    "created_at": "2009-11-18T13:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31709",
    "user": "@mwhansen"
}
```

The new patch looks okay to me.



---

archive/issue_comments_031710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4326#issuecomment-31710",
    "user": "@mwhansen"
}
```

Resolution: fixed
