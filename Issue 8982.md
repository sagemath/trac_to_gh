# Issue 8982: Fix jacobian for ode_solver example.

archive/issues_008982.json:
```json
{
    "body": "Assignee: burcin\n\nThe jacobian used for the Van der Pol oscillator in the gsl/ode.pyx file has wrong dimensions 3x2. The example runs fine as the last line is ignored. The attached patch corrects that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8982\n\n",
    "created_at": "2010-05-17T11:33:57Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "title": "Fix jacobian for ode_solver example.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8982",
    "user": "lfousse"
}
```
Assignee: burcin

The jacobian used for the Van der Pol oscillator in the gsl/ode.pyx file has wrong dimensions 3x2. The example runs fine as the last line is ignored. The attached patch corrects that.

Issue created by migration from https://trac.sagemath.org/ticket/8982





---

archive/issue_comments_082863.json:
```json
{
    "body": "Attachment\n\nYou should mark the ticket as `needs_review` when you submit a patch. This will put it on the relevant trac reports http://trac.sagemath.org/sage_trac/report/30 and http://trac.sagemath.org/sage_trac/report/10.",
    "created_at": "2010-05-22T11:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82863",
    "user": "burcin"
}
```

Attachment

You should mark the ticket as `needs_review` when you submit a patch. This will put it on the relevant trac reports http://trac.sagemath.org/sage_trac/report/30 and http://trac.sagemath.org/sage_trac/report/10.



---

archive/issue_comments_082864.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-22T11:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82864",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082865.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-22T11:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82865",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082866.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-22T11:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82866",
    "user": "burcin"
}
```

Looks good to me.



---

archive/issue_comments_082867.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8982#issuecomment-82867",
    "user": "mhansen"
}
```

Resolution: fixed
