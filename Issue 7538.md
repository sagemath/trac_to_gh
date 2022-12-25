# Issue 7538: equality of posets is broken !

archive/issues_007538.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat nborie\n\nKeywords: posets\n\nIt answer always true if two posets have the same size:\n\n```\nsage: p1 = Posets(2)[0]; p2 = Posets(2)[1]\nsage: p1.cover_relations()\n[]\nsage: p2.cover_relations()\n[[0, 1]]\nsage: p1 == p2\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7538\n\n",
    "created_at": "2009-11-26T21:34:36Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "equality of posets is broken !",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7538",
    "user": "https://github.com/hivert"
}
```
Assignee: @mwhansen

CC:  sage-combinat nborie

Keywords: posets

It answer always true if two posets have the same size:

```
sage: p1 = Posets(2)[0]; p2 = Posets(2)[1]
sage: p1.cover_relations()
[]
sage: p2.cover_relations()
[[0, 1]]
sage: p1 == p2
True
```


Issue created by migration from https://trac.sagemath.org/ticket/7538





---

archive/issue_comments_063818.json:
```json
{
    "body": "Attachment [trac_7538_poset_equal_fix-fh.patch](tarball://root/attachments/some-uuid/ticket7538/trac_7538_poset_equal_fix-fh.patch) by @hivert created at 2009-11-26 21:51:21",
    "created_at": "2009-11-26T21:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63818",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7538_poset_equal_fix-fh.patch](tarball://root/attachments/some-uuid/ticket7538/trac_7538_poset_equal_fix-fh.patch) by @hivert created at 2009-11-26 21:51:21



---

archive/issue_comments_063819.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-11-26T21:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63819",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_063820.json:
```json
{
    "body": "The fix posted here solve the problem of equality but raise a much more subtle one\n\n```\nsage: p1, p2 = Posets(2).list()\nsage: p2 < p1\nTrue\nsage: [[p1.__cmp__(p2) for p1 in Posets(2)] for p2 in Posets(2)]\n[[0, 1], [1, 0]]\nsage: [[p2.__cmp__(p1) for p1 in Posets(2)] for p2 in Posets(2)]\n[[0, 1], [-1, 0]]\nsage: p2 < p1\nFalse\n```\n\n\nI forward the discussion to sage-combinat-devel.",
    "created_at": "2009-11-26T21:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63820",
    "user": "https://github.com/hivert"
}
```

The fix posted here solve the problem of equality but raise a much more subtle one

```
sage: p1, p2 = Posets(2).list()
sage: p2 < p1
True
sage: [[p1.__cmp__(p2) for p1 in Posets(2)] for p2 in Posets(2)]
[[0, 1], [1, 0]]
sage: [[p2.__cmp__(p1) for p1 in Posets(2)] for p2 in Posets(2)]
[[0, 1], [-1, 0]]
sage: p2 < p1
False
```


I forward the discussion to sage-combinat-devel.



---

archive/issue_comments_063821.json:
```json
{
    "body": "Changing assignee from @mwhansen to @hivert.",
    "created_at": "2009-11-28T14:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63821",
    "user": "https://github.com/hivert"
}
```

Changing assignee from @mwhansen to @hivert.



---

archive/issue_comments_063822.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-23T22:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63822",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063823.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-24T13:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63823",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063824.json:
```json
{
    "body": "Hello Nicolas. Since you are implementing `__eq__`, it is a good idea to also implement `__ne__`. (It is does not work the way you might think it should.)",
    "created_at": "2010-02-24T13:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63824",
    "user": "https://github.com/saliola"
}
```

Hello Nicolas. Since you are implementing `__eq__`, it is a good idea to also implement `__ne__`. (It is does not work the way you might think it should.)



---

archive/issue_comments_063825.json:
```json
{
    "body": "Mouhahaha Franco!!! You don't want me to sleep during these Sage Days 20 but I will win the commiting contest! Good review!",
    "created_at": "2010-02-24T21:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63825",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Mouhahaha Franco!!! You don't want me to sleep during these Sage Days 20 but I will win the commiting contest! Good review!



---

archive/issue_comments_063826.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-24T21:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63826",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063827.json:
```json
{
    "body": "Attachment [trac_7538_poset_equal_fix-nb.patch](tarball://root/attachments/some-uuid/ticket7538/trac_7538_poset_equal_fix-nb.patch) by @novoselt created at 2010-04-15 23:51:25\n\nLooks good to me, passes all doctests.\n\nOnly the second patch should be applied.",
    "created_at": "2010-04-15T23:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63827",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_7538_poset_equal_fix-nb.patch](tarball://root/attachments/some-uuid/ticket7538/trac_7538_poset_equal_fix-nb.patch) by @novoselt created at 2010-04-15 23:51:25

Looks good to me, passes all doctests.

Only the second patch should be applied.



---

archive/issue_comments_063828.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-15T23:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63828",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063829.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T17:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63829",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_007768.json:
```json
{
    "actor": "@jhpalmieri",
    "created_at": "2010-04-16T17:28:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7538#event-7768"
}
```



---

archive/issue_comments_063830.json:
```json
{
    "body": "Merged \"trac_7538_poset_equal_fix-nb.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-16T17:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7538#issuecomment-63830",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_7538_poset_equal_fix-nb.patch" into 4.4.alpha0.
