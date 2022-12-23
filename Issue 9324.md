# Issue 9324: bug in Tate's algorithm over number fields

archive/issues_009324.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  robertwb rlm\n\n\n```\nsage: K.<a> = NumberField(x^2-x+6)\nsage: K.disc()\n-23\nsage: E = EllipticCurve([0,0,0,-53160*a-43995,-5067640*a+19402006])\nsage: E.conductor()\n[boom!]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9324\n\n",
    "created_at": "2010-06-24T05:39:36Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "title": "bug in Tate's algorithm over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9324",
    "user": "cremona"
}
```
Assignee: cremona

CC:  robertwb rlm


```
sage: K.<a> = NumberField(x^2-x+6)
sage: K.disc()
-23
sage: E = EllipticCurve([0,0,0,-53160*a-43995,-5067640*a+19402006])
sage: E.conductor()
[boom!]
```



Issue created by migration from https://trac.sagemath.org/ticket/9324





---

archive/issue_comments_087933.json:
```json
{
    "body": "Applies to 4.4.4.alpha1",
    "created_at": "2010-06-24T06:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9324#issuecomment-87933",
    "user": "cremona"
}
```

Applies to 4.4.4.alpha1



---

archive/issue_comments_087934.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-24T06:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9324#issuecomment-87934",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_087935.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-24T06:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9324#issuecomment-87935",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087936.json:
```json
{
    "body": "Works as advertised.",
    "created_at": "2010-06-24T17:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9324#issuecomment-87936",
    "user": "rlm"
}
```

Works as advertised.



---

archive/issue_comments_087937.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T17:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9324#issuecomment-87937",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087938.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9324#issuecomment-87938",
    "user": "mpatel"
}
```

Resolution: fixed
