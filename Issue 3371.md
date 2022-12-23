# Issue 3371: bug in uniformiSer for p-adic rings

archive/issues_003371.json:
```json
{
    "body": "Assignee: malb\n\n\nUniformi Z er\n\n\n```\nsage : A = Zp(7,10)\nsage : B.<t> = A.ext(x^2+7)\nsage : B.uniformizer()\nt + O(t^21)\n```\n\n\nversus Uniformi S er\n\n\n```\nsage : B.uniformiser()\n6*t^2 + t^4 + O(t^22)\n```\n\n\nwhich is NOT a uniformiser.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3371\n\n",
    "created_at": "2008-06-05T14:01:32Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "bug in uniformiSer for p-adic rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3371",
    "user": "wuthrich"
}
```
Assignee: malb


Uniformi Z er


```
sage : A = Zp(7,10)
sage : B.<t> = A.ext(x^2+7)
sage : B.uniformizer()
t + O(t^21)
```


versus Uniformi S er


```
sage : B.uniformiser()
6*t^2 + t^4 + O(t^22)
```


which is NOT a uniformiser.


Issue created by migration from https://trac.sagemath.org/ticket/3371





---

archive/issue_comments_023584.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-05T17:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23584",
    "user": "fwclarke"
}
```

Attachment



---

archive/issue_comments_023585.json:
```json
{
    "body": "The attached patch solves the problem [and also eliminates a stray tab].",
    "created_at": "2008-06-05T17:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23585",
    "user": "fwclarke"
}
```

The attached patch solves the problem [and also eliminates a stray tab].



---

archive/issue_comments_023586.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23586",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_023587.json:
```json
{
    "body": "extra touch-ups",
    "created_at": "2008-06-18T08:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23587",
    "user": "craigcitro"
}
```

extra touch-ups



---

archive/issue_comments_023588.json:
```json
{
    "body": "Attachment\n\nI approve of the changes in this ticket.",
    "created_at": "2008-06-18T09:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23588",
    "user": "roed"
}
```

Attachment

I approve of the changes in this ticket.



---

archive/issue_comments_023589.json:
```json
{
    "body": "Attachment\n\nadd a doctest",
    "created_at": "2008-06-18T09:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23589",
    "user": "craigcitro"
}
```

Attachment

add a doctest



---

archive/issue_comments_023590.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T07:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23590",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023591.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T07:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23591",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.0.4.alpha0
