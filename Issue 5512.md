# Issue 5512: CombinatorialSpeciesStructures with different labels are equal

archive/issues_005512.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: species\n\n\n```\nsage: T = species.BinaryTreeSpecies()\nsage: t = T.structures([1,2,3])[0]; t\n1*(2*3)\nsage: t[0], t[1][0]\n1, 2\nsage: t[0] == t[1][0]\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5512\n\n",
    "created_at": "2009-03-13T17:31:47Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.3",
    "title": "CombinatorialSpeciesStructures with different labels are equal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5512",
    "user": "https://github.com/saliola"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: species


```
sage: T = species.BinaryTreeSpecies()
sage: t = T.structures([1,2,3])[0]; t
1*(2*3)
sage: t[0], t[1][0]
1, 2
sage: t[0] == t[1][0]
True
```


Issue created by migration from https://trac.sagemath.org/ticket/5512





---

archive/issue_comments_042727.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-24T23:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42727",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042728.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-08T11:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42728",
    "user": "https://trac.sagemath.org/admin/accounts/users/elnorreip"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042729.json:
```json
{
    "body": "Added reviewers.",
    "created_at": "2011-02-08T13:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42729",
    "user": "https://trac.sagemath.org/admin/accounts/users/elnorreip"
}
```

Added reviewers.



---

archive/issue_comments_042730.json:
```json
{
    "body": "Moving to sage-feature as long as #10227 does not have a positive_review.",
    "created_at": "2011-03-11T22:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42730",
    "user": "https://github.com/jdemeyer"
}
```

Moving to sage-feature as long as #10227 does not have a positive_review.



---

archive/issue_comments_042731.json:
```json
{
    "body": "Hi Jeroen,\n\nThanks for pointing that #10227 is still awaiting for review. \n\nOne question concerning sage-wait: if someone (eg: me this week end if I find the time) review #10227, am I supposed to change the milestone of this one ? \n\nFlorent",
    "created_at": "2011-06-10T18:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42731",
    "user": "https://github.com/hivert"
}
```

Hi Jeroen,

Thanks for pointing that #10227 is still awaiting for review. 

One question concerning sage-wait: if someone (eg: me this week end if I find the time) review #10227, am I supposed to change the milestone of this one ? 

Florent



---

archive/issue_comments_042732.json:
```json
{
    "body": "Replying to [comment:9 hivert]:\n> Hi Jeroen,\n> \n> Thanks for pointing that #10227 is still awaiting for review. \n> \n> One question concerning sage-wait: if someone (eg: me this week end if I find the time) review #10227, am I supposed to change the milestone of this one ? \n\nI would say: yes, you can do that, at least if you are sufficient familiar with *this* ticket to be sure that there is no further obstruction.",
    "created_at": "2011-06-14T17:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42732",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:9 hivert]:
> Hi Jeroen,
> 
> Thanks for pointing that #10227 is still awaiting for review. 
> 
> One question concerning sage-wait: if someone (eg: me this week end if I find the time) review #10227, am I supposed to change the milestone of this one ? 

I would say: yes, you can do that, at least if you are sufficient familiar with *this* ticket to be sure that there is no further obstruction.



---

archive/issue_comments_042733.json:
```json
{
    "body": "Checking the patch, there is no hard dependency on #10227.",
    "created_at": "2012-07-31T22:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42733",
    "user": "https://github.com/mwhansen"
}
```

Checking the patch, there is no hard dependency on #10227.



---

archive/issue_comments_042734.json:
```json
{
    "body": "Apply trac_5512-species_equality.patch",
    "created_at": "2012-07-31T22:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42734",
    "user": "https://github.com/mwhansen"
}
```

Apply trac_5512-species_equality.patch



---

archive/issue_comments_042735.json:
```json
{
    "body": "Attachment [trac_5512-species_equality.patch](tarball://root/attachments/some-uuid/ticket5512/trac_5512-species_equality.patch) by @jdemeyer created at 2012-08-03 10:28:33",
    "created_at": "2012-08-03T10:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42735",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_5512-species_equality.patch](tarball://root/attachments/some-uuid/ticket5512/trac_5512-species_equality.patch) by @jdemeyer created at 2012-08-03 10:28:33



---

archive/issue_comments_042736.json:
```json
{
    "body": "Rebased to sage-5.3.beta0.",
    "created_at": "2012-08-03T10:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42736",
    "user": "https://github.com/jdemeyer"
}
```

Rebased to sage-5.3.beta0.



---

archive/issue_events_005763.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-08-12T18:58:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5512#event-5763"
}
```



---

archive/issue_comments_042737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-08-12T18:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5512#issuecomment-42737",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
