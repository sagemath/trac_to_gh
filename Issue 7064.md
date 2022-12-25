# Issue 7064: fix warnings when building reference manual in Sage 4.1.2.alpha4

archive/issues_007064.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @malb polybori\n\nOn a fresh compiled Sage 4.1.2.alpha4, building the HTML version of the reference manual resulted in the following warnings:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/numerical/knapsack.py:docstring of sage.numerical.knapsack.knapsack:69: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.MonomialFactory:1: (WARNING/2) Inline literal start-string without end-string.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.PolynomialFactory:1: (WARNING/2) Inline literal start-string without end-string.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.VariableFactory:1: (WARNING/2) Inline literal start-string without end-string.\n```\n\nThis should be fixed before releasing the upcoming rc0. I have made this ticket a blocker for 4.1.2. The HTML version of the reference manual should build without any warnings.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7064\n\n",
    "created_at": "2009-09-29T06:30:40Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "fix warnings when building reference manual in Sage 4.1.2.alpha4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7064",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

CC:  @malb polybori

On a fresh compiled Sage 4.1.2.alpha4, building the HTML version of the reference manual resulted in the following warnings:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/numerical/knapsack.py:docstring of sage.numerical.knapsack.knapsack:69: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.MonomialFactory:1: (WARNING/2) Inline literal start-string without end-string.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.PolynomialFactory:1: (WARNING/2) Inline literal start-string without end-string.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.VariableFactory:1: (WARNING/2) Inline literal start-string without end-string.
```

This should be fixed before releasing the upcoming rc0. I have made this ticket a blocker for 4.1.2. The HTML version of the reference manual should build without any warnings.

Issue created by migration from https://trac.sagemath.org/ticket/7064





---

archive/issue_comments_058323.json:
```json
{
    "body": "based on Sage 4.1.2.alpha4",
    "created_at": "2009-09-29T09:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7064#issuecomment-58323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.1.2.alpha4



---

archive/issue_comments_058324.json:
```json
{
    "body": "Attachment [trac_7064-fix-warnings.patch](tarball://root/attachments/some-uuid/ticket7064/trac_7064-fix-warnings.patch) by mvngu created at 2009-09-29 09:15:32",
    "created_at": "2009-09-29T09:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7064#issuecomment-58324",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7064-fix-warnings.patch](tarball://root/attachments/some-uuid/ticket7064/trac_7064-fix-warnings.patch) by mvngu created at 2009-09-29 09:15:32



---

archive/issue_events_007284.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-30T03:55:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7064",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7064#event-7284"
}
```



---

archive/issue_comments_058325.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-30T03:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7064#issuecomment-58325",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
