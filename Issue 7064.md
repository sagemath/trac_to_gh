# Issue 7064: fix warnings when building reference manual in Sage 4.1.2.alpha4

archive/issues_007064.json:
```json
{
    "body": "Assignee: tba\n\nCC:  malb polybori\n\nOn a fresh compiled Sage 4.1.2.alpha4, building the HTML version of the reference manual resulted in the following warnings:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/numerical/knapsack.py:docstring of sage.numerical.knapsack.knapsack:69: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.MonomialFactory:1: (WARNING/2) Inline literal start-string without end-string.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.PolynomialFactory:1: (WARNING/2) Inline literal start-string without end-string.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.VariableFactory:1: (WARNING/2) Inline literal start-string without end-string.\n```\n\nThis should be fixed before releasing the upcoming rc0. I have made this ticket a blocker for 4.1.2. The HTML version of the reference manual should build without any warnings.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7064\n\n",
    "created_at": "2009-09-29T06:30:40Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "title": "fix warnings when building reference manual in Sage 4.1.2.alpha4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7064",
    "user": "mvngu"
}
```
Assignee: tba

CC:  malb polybori

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

archive/issue_comments_058433.json:
```json
{
    "body": "based on Sage 4.1.2.alpha4",
    "created_at": "2009-09-29T09:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7064#issuecomment-58433",
    "user": "mvngu"
}
```

based on Sage 4.1.2.alpha4



---

archive/issue_comments_058434.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-29T09:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7064#issuecomment-58434",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_058435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-30T03:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7064#issuecomment-58435",
    "user": "mvngu"
}
```

Resolution: fixed
