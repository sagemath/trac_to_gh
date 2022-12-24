# Issue 5191: coercion issue of tanh(2) into QQbar

archive/issues_005191.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  zimmerma\n\nThis is a followup to #5023: Paul Zimmermann reports:\n\n```\nsage: a=tanh(2)\nsage: a._algebraic_(QQbar)\n...\nTypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational\n```\n\n\nCarl: If this is invalid just close the ticker as invalid.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5191\n\n",
    "created_at": "2009-02-06T00:20:10Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "coercion issue of tanh(2) into QQbar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5191",
    "user": "mabshoff"
}
```
Assignee: cwitty

CC:  zimmerma

This is a followup to #5023: Paul Zimmermann reports:

```
sage: a=tanh(2)
sage: a._algebraic_(QQbar)
...
TypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational
```


Carl: If this is invalid just close the ticker as invalid.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5191





---

archive/issue_comments_039802.json:
```json
{
    "body": "QQbar(sinh(2)) fails with the above error message; I believe that sinh(2) is not algebraic, so the conversion must fail, although I suppose the error message could be nicer.\n\nHowever, QQbar(sinh(log(2))) correctly returns 3/4, so the code does work.  Therefore, I'm marking this invalid.",
    "created_at": "2009-02-06T03:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5191#issuecomment-39802",
    "user": "cwitty"
}
```

QQbar(sinh(2)) fails with the above error message; I believe that sinh(2) is not algebraic, so the conversion must fail, although I suppose the error message could be nicer.

However, QQbar(sinh(log(2))) correctly returns 3/4, so the code does work.  Therefore, I'm marking this invalid.



---

archive/issue_comments_039803.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-02-06T03:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5191#issuecomment-39803",
    "user": "cwitty"
}
```

Resolution: invalid
