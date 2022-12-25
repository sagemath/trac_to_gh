# Issue 8982: Fix jacobian for ode_solver example.

archive/issues_008982.json:
```json
{
    "body": "Assignee: @burcin\n\nThe jacobian used for the Van der Pol oscillator in the gsl/ode.pyx file has wrong dimensions 3x2. The example runs fine as the last line is ignored. The attached patch corrects that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8982\n\n",
    "created_at": "2010-05-17T11:33:57Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Fix jacobian for ode_solver example.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8982",
    "user": "https://trac.sagemath.org/admin/accounts/users/lfousse"
}
```
Assignee: @burcin

The jacobian used for the Van der Pol oscillator in the gsl/ode.pyx file has wrong dimensions 3x2. The example runs fine as the last line is ignored. The attached patch corrects that.

Issue created by migration from https://trac.sagemath.org/ticket/8982





---

archive/issue_comments_082727.json:
```json
{
    "body": "Attachment [ode_example.patch](tarball://root/attachments/some-uuid/ticket8982/ode_example.patch) by @burcin created at 2010-05-22 11:54:55\n\nYou should mark the ticket as `needs_review` when you submit a patch. This will put it on the relevant trac reports http://trac.sagemath.org/sage_trac/report/30 and http://trac.sagemath.org/sage_trac/report/10.",
    "created_at": "2010-05-22T11:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82727",
    "user": "https://github.com/burcin"
}
```

Attachment [ode_example.patch](tarball://root/attachments/some-uuid/ticket8982/ode_example.patch) by @burcin created at 2010-05-22 11:54:55

You should mark the ticket as `needs_review` when you submit a patch. This will put it on the relevant trac reports http://trac.sagemath.org/sage_trac/report/30 and http://trac.sagemath.org/sage_trac/report/10.



---

archive/issue_comments_082728.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-22T11:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82728",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082729.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-22T11:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82729",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082730.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-22T11:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82730",
    "user": "https://github.com/burcin"
}
```

Looks good to me.



---

archive/issue_comments_082731.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82731",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
