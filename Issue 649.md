# Issue 649: [with patch, positive review] create a special symbolic matrix data type

archive/issues_000649.json:
```json
{
    "body": "Assignee: @mwhansen\n\nIt should have:\n* simplify_* methods\n* underlying data should be a pointer to a maxima matrix object, so that matrix operations are very fast.\n\n\nThis should also resolve a bug reported by Kate Minola on 20070914 with doctesting \n\n     sage -t devel/sage-main/sage/plot/plot3d/transform.pyx\n\nIssue created by migration from https://trac.sagemath.org/ticket/649\n\n",
    "closed_at": "2007-12-22T18:37:41Z",
    "created_at": "2007-09-13T18:44:26Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "[with patch, positive review] create a special symbolic matrix data type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/649",
    "user": "https://github.com/robertwb"
}
```
Assignee: @mwhansen

It should have:
* simplify_* methods
* underlying data should be a pointer to a maxima matrix object, so that matrix operations are very fast.


This should also resolve a bug reported by Kate Minola on 20070914 with doctesting 

     sage -t devel/sage-main/sage/plot/plot3d/transform.pyx

Issue created by migration from https://trac.sagemath.org/ticket/649





---

archive/issue_comments_003357.json:
```json
{
    "body": "Changing component from coding theory to calculus.",
    "created_at": "2007-09-13T18:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3357",
    "user": "https://github.com/robertwb"
}
```

Changing component from coding theory to calculus.



---

archive/issue_events_001729.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-13T19:42:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/649#event-1729"
}
```



---

archive/issue_events_001730.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-14T17:31:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/649#event-1730"
}
```



---

archive/issue_events_001731.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-14T17:31:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/649#event-1731"
}
```



---

archive/issue_comments_003358.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-10-19T18:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3358",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_003359.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-10-19T18:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3359",
    "user": "https://github.com/mwhansen"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_003360.json:
```json
{
    "body": "Attachment [649-symbolic-matrices.hg](tarball://root/attachments/some-uuid/ticket649/649-symbolic-matrices.hg) by @robertwb created at 2007-12-20 10:47:34\n\nI've posted a preliminary bundle. Something's up with the eigenvalues command however.",
    "created_at": "2007-12-20T10:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3360",
    "user": "https://github.com/robertwb"
}
```

Attachment [649-symbolic-matrices.hg](tarball://root/attachments/some-uuid/ticket649/649-symbolic-matrices.hg) by @robertwb created at 2007-12-20 10:47:34

I've posted a preliminary bundle. Something's up with the eigenvalues command however.



---

archive/issue_events_001732.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2007-12-20T10:47:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/649#event-1732"
}
```



---

archive/issue_events_001733.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2007-12-20T10:47:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/649#event-1733"
}
```



---

archive/issue_comments_003361.json:
```json
{
    "body": "Attachment [649.patch](tarball://root/attachments/some-uuid/ticket649/649.patch) by @mwhansen created at 2007-12-22 18:18:00",
    "created_at": "2007-12-22T18:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3361",
    "user": "https://github.com/mwhansen"
}
```

Attachment [649.patch](tarball://root/attachments/some-uuid/ticket649/649.patch) by @mwhansen created at 2007-12-22 18:18:00



---

archive/issue_comments_003362.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T18:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3362",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003363.json:
```json
{
    "body": "Patch attached (which unintentionally includes the changes from Robert's bundle).",
    "created_at": "2007-12-22T18:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3363",
    "user": "https://github.com/mwhansen"
}
```

Patch attached (which unintentionally includes the changes from Robert's bundle).



---

archive/issue_comments_003364.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T18:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3364",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_003365.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T18:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/649#issuecomment-3365",
    "user": "https://github.com/rlmill"
}
```

merged in 2.9.1 rc0



---

archive/issue_events_001734.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-22T18:37:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/649",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/649#event-1734"
}
```
