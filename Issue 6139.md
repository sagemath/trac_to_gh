# Issue 6139: [with patch, needs review] Fix S-Box calling when m != n

archive/issues_006139.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  mvngu\n\nKeywords: crypto, mq, sbox\n\nThis should work:\n\n```\nsage: S = mq.SBox(3, 0, 1, 3, 1, 0, 2, 2)\nsage: S(0)\n3\nsage: S([0,0,0])\n[1, 1]\n```\n\nreported by Sajan.S on [sage-support] (27.5.09)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6139\n\n",
    "created_at": "2009-05-27T12:20:18Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] Fix S-Box calling when m != n",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6139",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  mvngu

Keywords: crypto, mq, sbox

This should work:

```
sage: S = mq.SBox(3, 0, 1, 3, 1, 0, 2, 2)
sage: S(0)
3
sage: S([0,0,0])
[1, 1]
```

reported by Sajan.S on [sage-support] (27.5.09)

Issue created by migration from https://trac.sagemath.org/ticket/6139





---

archive/issue_comments_048927.json:
```json
{
    "body": "Attachment [sbox_call_and_rest.patch](tarball://root/attachments/some-uuid/ticket6139/sbox_call_and_rest.patch) by @malb created at 2009-06-02 13:55:11\n\nHi Minh, can I ask you to review this?",
    "created_at": "2009-06-02T13:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6139#issuecomment-48927",
    "user": "https://github.com/malb"
}
```

Attachment [sbox_call_and_rest.patch](tarball://root/attachments/some-uuid/ticket6139/sbox_call_and_rest.patch) by @malb created at 2009-06-02 13:55:11

Hi Minh, can I ask you to review this?



---

archive/issue_comments_048928.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nPatch applies OK against sage-4.0.1.alpha0, all tests pass even with `-long` option. Most of the patch deals with Sphinxifying the module `sage/crypto/mq/sbox.py`. But the main issue is to fix the bug reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/91ec1975d7bfc565/d6113194a8a6cc3f) thread. And the patch does exactly as claimed. Positive review. I've attached a reviewer patch that fixes some trivial formatting typos.",
    "created_at": "2009-06-03T21:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6139#issuecomment-48928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



Patch applies OK against sage-4.0.1.alpha0, all tests pass even with `-long` option. Most of the patch deals with Sphinxifying the module `sage/crypto/mq/sbox.py`. But the main issue is to fix the bug reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/91ec1975d7bfc565/d6113194a8a6cc3f) thread. And the patch does exactly as claimed. Positive review. I've attached a reviewer patch that fixes some trivial formatting typos.



---

archive/issue_comments_048929.json:
```json
{
    "body": "Attachment [trac_6139-reviewer.patch](tarball://root/attachments/some-uuid/ticket6139/trac_6139-reviewer.patch) by mvngu created at 2009-06-03 21:17:42",
    "created_at": "2009-06-03T21:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6139#issuecomment-48929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6139-reviewer.patch](tarball://root/attachments/some-uuid/ticket6139/trac_6139-reviewer.patch) by mvngu created at 2009-06-03 21:17:42



---

archive/issue_comments_048930.json:
```json
{
    "body": "The referee patch is fine too.",
    "created_at": "2009-06-03T22:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6139#issuecomment-48930",
    "user": "https://github.com/malb"
}
```

The referee patch is fine too.



---

archive/issue_comments_048931.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6139#issuecomment-48931",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048932.json:
```json
{
    "body": "Merged both patches in 4.0.1.rc1.",
    "created_at": "2009-06-04T18:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6139#issuecomment-48932",
    "user": "https://github.com/mwhansen"
}
```

Merged both patches in 4.0.1.rc1.



---

archive/issue_events_014456.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T18:22:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6139",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6139#event-14456"
}
```
