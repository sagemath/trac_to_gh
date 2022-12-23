# Issue 3894: [with patch, needs review] in tutorial, live version, triple dots are not visible

archive/issues_003894.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: tutorial\n\nIn examples like this in the tutorial:\n\n```\nsage: def is_even(n):\n...       return n%2 == 0\n```\n\nthe three dots are not actually visible in the 'live' version of the documentation.  So change the documentation to try to reflect this.  (It would be better to have text printed conditionally, depending on whether it was for the live version, the static version, or the dvi/pdf version, but I don't know how to do that.)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3894\n\n",
    "created_at": "2008-08-19T03:25:20Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] in tutorial, live version, triple dots are not visible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3894",
    "user": "jhpalmieri"
}
```
Assignee: tba

Keywords: tutorial

In examples like this in the tutorial:

```
sage: def is_even(n):
...       return n%2 == 0
```

the three dots are not actually visible in the 'live' version of the documentation.  So change the documentation to try to reflect this.  (It would be better to have text printed conditionally, depending on whether it was for the live version, the static version, or the dvi/pdf version, but I don't know how to do that.)



Issue created by migration from https://trac.sagemath.org/ticket/3894





---

archive/issue_comments_027840.json:
```json
{
    "body": "Attachment\n\nLooks good.  I've made this change in the ReST version of the tutorial too.",
    "created_at": "2008-09-16T02:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3894#issuecomment-27840",
    "user": "mhansen"
}
```

Attachment

Looks good.  I've made this change in the ReST version of the tutorial too.



---

archive/issue_comments_027841.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-16T03:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3894#issuecomment-27841",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027842.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc5",
    "created_at": "2008-09-16T03:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3894#issuecomment-27842",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc5
