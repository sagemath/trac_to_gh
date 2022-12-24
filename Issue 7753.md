# Issue 7753: Coxeter groups: more Bruhat and weak order features

archive/issues_007753.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: Bruhat order, Weak order\n\nNew methods:\n- bruhat_le (code inspired from code by Daniel Bump)\n- weak_le\n- bruhat_poset (finite Coxeter groups)\n- weak_poset   (finite Coxeter groups)\n\nImproved doctests for related methods\n\nIssue created by migration from https://trac.sagemath.org/ticket/7753\n\n",
    "created_at": "2009-12-23T22:55:34Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Coxeter groups: more Bruhat and weak order features",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7753",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: Bruhat order, Weak order

New methods:
- bruhat_le (code inspired from code by Daniel Bump)
- weak_le
- bruhat_poset (finite Coxeter groups)
- weak_poset   (finite Coxeter groups)

Improved doctests for related methods

Issue created by migration from https://trac.sagemath.org/ticket/7753





---

archive/issue_comments_066770.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-23T23:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66770",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066771.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-02T22:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66771",
    "user": "bump"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066772.json:
```json
{
    "body": "This patch implements the bruhat_order as a cached method and is badly needed.\n\nWith Sage 4.3, this raises an exception at the test in coxeter_groups.py, line 1010.\n\nThe definition of Q could be rewritten:\n\n\n```\nW = WeylGroup(\"B3\")\nsage: fcn = lambda x,y : x.bruhat_le(y)\nsage: Q=Poset((W.list(),fcn))\n```\n\n\nMaybe the `?!?` should be removed from the `# long time` directive\na couple of lines later since it is unclear what it means.",
    "created_at": "2010-01-02T22:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66772",
    "user": "bump"
}
```

This patch implements the bruhat_order as a cached method and is badly needed.

With Sage 4.3, this raises an exception at the test in coxeter_groups.py, line 1010.

The definition of Q could be rewritten:


```
W = WeylGroup("B3")
sage: fcn = lambda x,y : x.bruhat_le(y)
sage: Q=Poset((W.list(),fcn))
```


Maybe the `?!?` should be removed from the `# long time` directive
a couple of lines later since it is unclear what it means.



---

archive/issue_comments_066773.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-04T15:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66773",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066774.json:
```json
{
    "body": "Replying to [comment:2 bump]:\n> This patch implements the bruhat_order as a cached method and is badly needed.\n> \n> With Sage 4.3, this raises an exception at the test in coxeter_groups.py, line 1010.\n\nOops, I forgot that this depended on another patch; now #7842.  As you mention, this dependency is trivial though, so we can also work around it if #7842 is not merged instantly.\n\n> Maybe the `?!?` should be removed from the `# long time` directive\n> a couple of lines later since it is unclear what it means.\n\nFixed, and updated the # long time around that line. I was just surprised by how much time this was taking. We need more Weyl group optimizations!",
    "created_at": "2010-01-04T15:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66774",
    "user": "nthiery"
}
```

Replying to [comment:2 bump]:
> This patch implements the bruhat_order as a cached method and is badly needed.
> 
> With Sage 4.3, this raises an exception at the test in coxeter_groups.py, line 1010.

Oops, I forgot that this depended on another patch; now #7842.  As you mention, this dependency is trivial though, so we can also work around it if #7842 is not merged instantly.

> Maybe the `?!?` should be removed from the `# long time` directive
> a couple of lines later since it is unclear what it means.

Fixed, and updated the # long time around that line. I was just surprised by how much time this was taking. We need more Weyl group optimizations!



---

archive/issue_comments_066775.json:
```json
{
    "body": "Updated timings w.r.t. #7754 which is already in Sage",
    "created_at": "2010-01-04T18:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66775",
    "user": "nthiery"
}
```

Updated timings w.r.t. #7754 which is already in Sage



---

archive/issue_comments_066776.json:
```json
{
    "body": "Attachment [trac_7753_root_systems-bruhat_order-nt.patch](tarball://root/attachments/some-uuid/ticket7753/trac_7753_root_systems-bruhat_order-nt.patch) by bump created at 2010-01-07 14:18:37\n\nBy now this code is tested a lot, at least for finite Weyl groups, and\nthe previous reviewer comments were addressed. I am changing the\nstatus to positive review.",
    "created_at": "2010-01-07T14:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66776",
    "user": "bump"
}
```

Attachment [trac_7753_root_systems-bruhat_order-nt.patch](tarball://root/attachments/some-uuid/ticket7753/trac_7753_root_systems-bruhat_order-nt.patch) by bump created at 2010-01-07 14:18:37

By now this code is tested a lot, at least for finite Weyl groups, and
the previous reviewer comments were addressed. I am changing the
status to positive review.



---

archive/issue_comments_066777.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T14:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66777",
    "user": "bump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066778.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T09:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7753#issuecomment-66778",
    "user": "rlm"
}
```

Resolution: fixed
