# Issue 6406: fixing p_primary_bound on Tate-Shafarevich groups not to allow the reducible case

archive/issues_006406.json:
```json
{
    "body": "Assignee: was\n\nCC:  rlm\n\nKeywords: elliptic curves, tate shafarevich group,\n\nCurrently the p_primary_bound pretends to give back a proven result when the p-torsion is reducible. That is wrong.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6406\n\n",
    "created_at": "2009-06-25T14:37:36Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "fixing p_primary_bound on Tate-Shafarevich groups not to allow the reducible case",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6406",
    "user": "wuthrich"
}
```
Assignee: was

CC:  rlm

Keywords: elliptic curves, tate shafarevich group,

Currently the p_primary_bound pretends to give back a proven result when the p-torsion is reducible. That is wrong.

Issue created by migration from https://trac.sagemath.org/ticket/6406





---

archive/issue_comments_051443.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-25T14:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6406#issuecomment-51443",
    "user": "wuthrich"
}
```

Attachment



---

archive/issue_comments_051444.json:
```json
{
    "body": ".... and there was a bug. It actually never tested for surjectivity, since {{not E.is_surjective(p)}} is always False.",
    "created_at": "2009-06-25T14:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6406#issuecomment-51444",
    "user": "wuthrich"
}
```

.... and there was a bug. It actually never tested for surjectivity, since {{not E.is_surjective(p)}} is always False.



---

archive/issue_comments_051445.json:
```json
{
    "body": "Looks good, applies fine to 4.1.alpha2 and tests pass (I tested all schemes/elliptic_curves).\n\nIs it possible to add a doctest illustrating the suggestion to \"try an_padic instead\"?  That would be useful for the reference manual.  Of course, an_padic has its own tests but it would look good to include one right after one of the new tests which shows the message.",
    "created_at": "2009-06-28T15:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6406#issuecomment-51445",
    "user": "cremona"
}
```

Looks good, applies fine to 4.1.alpha2 and tests pass (I tested all schemes/elliptic_curves).

Is it possible to add a doctest illustrating the suggestion to "try an_padic instead"?  That would be useful for the reference manual.  Of course, an_padic has its own tests but it would look good to include one right after one of the new tests which shows the message.



---

archive/issue_comments_051446.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-29T21:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6406#issuecomment-51446",
    "user": "rlm"
}
```

Resolution: fixed
