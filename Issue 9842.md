# Issue 9842: modular/overconvergent/weightspace.py uses Maxima because of symbolic variables

archive/issues_009842.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @loefflerd\n\nThis is in the top-level docstring of the file:\n\n\n```\nsage: L = Qp(17).extension(x^2 - 17, names='a'); L.rename('L')\nsage: \nExiting Sage (CPU time 0m0.94s, Wall time 0m25.72s).\nExiting spawned Maxima process.\n```\n\n\nPatch on its way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9843\n\n",
    "created_at": "2010-08-31T22:09:56Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "modular/overconvergent/weightspace.py uses Maxima because of symbolic variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9842",
    "user": "https://github.com/aghitza"
}
```
Assignee: @craigcitro

CC:  @loefflerd

This is in the top-level docstring of the file:


```
sage: L = Qp(17).extension(x^2 - 17, names='a'); L.rename('L')
sage: 
Exiting Sage (CPU time 0m0.94s, Wall time 0m25.72s).
Exiting spawned Maxima process.
```


Patch on its way.

Issue created by migration from https://trac.sagemath.org/ticket/9843





---

archive/issue_comments_096978.json:
```json
{
    "body": "OK, I have a patch but I'm getting a trac error when trying to attach it (no space left on device).",
    "created_at": "2010-08-31T22:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96978",
    "user": "https://github.com/aghitza"
}
```

OK, I have a patch but I'm getting a trac error when trying to attach it (no space left on device).



---

archive/issue_comments_096979.json:
```json
{
    "body": "Test post.",
    "created_at": "2010-08-31T23:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96979",
    "user": "https://github.com/mwhansen"
}
```

Test post.



---

archive/issue_comments_096980.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-09-01T02:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96980",
    "user": "https://github.com/aghitza"
}
```

Changing priority from major to minor.



---

archive/issue_comments_096981.json:
```json
{
    "body": "Attachment [trac_9843.patch](tarball://root/attachments/some-uuid/ticket9843/trac_9843.patch) by @aghitza created at 2010-09-01 02:43:28",
    "created_at": "2010-09-01T02:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96981",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_9843.patch](tarball://root/attachments/some-uuid/ticket9843/trac_9843.patch) by @aghitza created at 2010-09-01 02:43:28



---

archive/issue_comments_096982.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-01T02:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96982",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096983.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2010-09-22T09:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96983",
    "user": "https://github.com/loefflerd"
}
```

Looks fine to me.



---

archive/issue_comments_096984.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T09:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96984",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-96985",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009970.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T09:11:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9842#event-9970"
}
```
