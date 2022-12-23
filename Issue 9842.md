# Issue 9842: modular/overconvergent/weightspace.py uses Maxima because of symbolic variables

archive/issues_009842.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  davidloeffler\n\nThis is in the top-level docstring of the file:\n\n\n```\nsage: L = Qp(17).extension(x^2 - 17, names='a'); L.rename('L')\nsage: \nExiting Sage (CPU time 0m0.94s, Wall time 0m25.72s).\nExiting spawned Maxima process.\n```\n\n\nPatch on its way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9843\n\n",
    "created_at": "2010-08-31T22:09:56Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "modular/overconvergent/weightspace.py uses Maxima because of symbolic variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9842",
    "user": "AlexGhitza"
}
```
Assignee: craigcitro

CC:  davidloeffler

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

archive/issue_comments_097137.json:
```json
{
    "body": "OK, I have a patch but I'm getting a trac error when trying to attach it (no space left on device).",
    "created_at": "2010-08-31T22:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97137",
    "user": "AlexGhitza"
}
```

OK, I have a patch but I'm getting a trac error when trying to attach it (no space left on device).



---

archive/issue_comments_097138.json:
```json
{
    "body": "Test post.",
    "created_at": "2010-08-31T23:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97138",
    "user": "mhansen"
}
```

Test post.



---

archive/issue_comments_097139.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-09-01T02:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97139",
    "user": "AlexGhitza"
}
```

Changing priority from major to minor.



---

archive/issue_comments_097140.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-01T02:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97140",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_097141.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-01T02:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97141",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097142.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2010-09-22T09:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97142",
    "user": "davidloeffler"
}
```

Looks fine to me.



---

archive/issue_comments_097143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T09:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97143",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097144.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9842#issuecomment-97144",
    "user": "mpatel"
}
```

Resolution: fixed
