# Issue 8890: map_support modifies the zero element of a free module!

archive/issues_008890.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  sage-combinat\n\n\n```\nsage: B = CombinatorialFreeModule(ZZ, ['a','b'])\nsage: B.an_element().map_support(lambda i: i)\n2*B['a'] + 2*B['b']\nsage: B.zero()\n2*B['a'] + 2*B['b']\n```\n\n\nLooking at the code exposes the problem:\n\n```\n        res = self.parent()(0)\n        z_elt = {}\n        for m,c in self.monomial_coefficients().iteritems():\n            z_elt[f(m)] = c\n        res._monomial_coefficients = z_elt\n        return res\n```\n\n\nWe should not change the dictionary of zero!\n\nIssue created by migration from https://trac.sagemath.org/ticket/8890\n\n",
    "created_at": "2010-05-05T16:12:51Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "map_support modifies the zero element of a free module!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8890",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @aghitza

CC:  sage-combinat


```
sage: B = CombinatorialFreeModule(ZZ, ['a','b'])
sage: B.an_element().map_support(lambda i: i)
2*B['a'] + 2*B['b']
sage: B.zero()
2*B['a'] + 2*B['b']
```


Looking at the code exposes the problem:

```
        res = self.parent()(0)
        z_elt = {}
        for m,c in self.monomial_coefficients().iteritems():
            z_elt[f(m)] = c
        res._monomial_coefficients = z_elt
        return res
```


We should not change the dictionary of zero!

Issue created by migration from https://trac.sagemath.org/ticket/8890





---

archive/issue_comments_081600.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-05T17:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81600",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081601.json:
```json
{
    "body": "Changing keywords from \"\" to \"free modules\".",
    "created_at": "2010-05-05T17:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81601",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "free modules".



---

archive/issue_comments_081602.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-01T20:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81602",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081603.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-01T23:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81603",
    "user": "https://github.com/jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081604.json:
```json
{
    "body": "Looks good to me.  Thanks Nicolas!  Positive review.",
    "created_at": "2010-06-01T23:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81604",
    "user": "https://github.com/jbandlow"
}
```

Looks good to me.  Thanks Nicolas!  Positive review.



---

archive/issue_comments_081605.json:
```json
{
    "body": "Oops, I forgot to mention that this depends on #8881.",
    "created_at": "2010-06-02T01:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81605",
    "user": "https://github.com/jbandlow"
}
```

Oops, I forgot to mention that this depends on #8881.



---

archive/issue_comments_081606.json:
```json
{
    "body": "Attachment [trac_8890-free_module-cleanup-nt.patch](tarball://root/attachments/some-uuid/ticket8890/trac_8890-free_module-cleanup-nt.patch) by @nthiery created at 2010-06-02 08:30:54",
    "created_at": "2010-06-02T08:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81606",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8890-free_module-cleanup-nt.patch](tarball://root/attachments/some-uuid/ticket8890/trac_8890-free_module-cleanup-nt.patch) by @nthiery created at 2010-06-02 08:30:54



---

archive/issue_comments_081607.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8890#issuecomment-81607",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_009047.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-06-06T01:11:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8890",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8890#event-9047"
}
```
