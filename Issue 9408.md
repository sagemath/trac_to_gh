# Issue 9408: relativize in number fields is broken

archive/issues_009408.json:
```json
{
    "body": "Assignee: davidloeffler\n\nKeywords: relativize\n\nDoes not work due to (maybe) denominators\n\n\n```\nsage: K.<a> = NumberField(x^4-4*x^3+12*x^2-16*x+8)\nsage: L.<u,v> = K.relativize(3*a**3 - 9*a**2 + 24*a -16)\nsage:#This seems OK\nsage: L2.<u2,v2> = K.relativize((3/4)*a**3 - (9/4)*a**2 + 6*a -4)\n```\n\nPariError:  (8)\n\nSimpler example\n\n\n```\nsage: L.<a,b> = QQ[i].relativize(1) #Ok\nsage: L.<a,b> = QQ[i].relativize(1/2) #PariError\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9408\n\n",
    "created_at": "2010-07-02T16:04:23Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "relativize in number fields is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9408",
    "user": "lftabera"
}
```
Assignee: davidloeffler

Keywords: relativize

Does not work due to (maybe) denominators


```
sage: K.<a> = NumberField(x^4-4*x^3+12*x^2-16*x+8)
sage: L.<u,v> = K.relativize(3*a**3 - 9*a**2 + 24*a -16)
sage:#This seems OK
sage: L2.<u2,v2> = K.relativize((3/4)*a**3 - (9/4)*a**2 + 6*a -4)
```

PariError:  (8)

Simpler example


```
sage: L.<a,b> = QQ[i].relativize(1) #Ok
sage: L.<a,b> = QQ[i].relativize(1/2) #PariError
```


Issue created by migration from https://trac.sagemath.org/ticket/9408





---

archive/issue_comments_089665.json:
```json
{
    "body": "This ticket should be closed as duplicate of #252",
    "created_at": "2010-07-06T10:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89665",
    "user": "lftabera"
}
```

This ticket should be closed as duplicate of #252



---

archive/issue_comments_089666.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-07-06T10:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89666",
    "user": "lftabera"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_089667.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-06-07T08:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89667",
    "user": "lftabera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_089668.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-15T12:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89668",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089669.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-11-15T09:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89669",
    "user": "jdemeyer"
}
```

Resolution: duplicate
