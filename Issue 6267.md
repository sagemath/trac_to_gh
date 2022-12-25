# Issue 6267: Same typesetting for two different variables:

archive/issues_006267.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mvngu\n\nKeywords: latex, variables\n\nSage (4.0.1) typesets two different variables as same latex string\n\n\n```\nvar('xi, xi_')\nlatex(xi)\n\\xi\nlatex(xi_)\n\\xi\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6267\n\n",
    "created_at": "2009-06-12T15:19:15Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Same typesetting for two different variables:",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6267",
    "user": "https://github.com/golam-m-hossain"
}
```
Assignee: cwitty

CC:  mvngu

Keywords: latex, variables

Sage (4.0.1) typesets two different variables as same latex string


```
var('xi, xi_')
latex(xi)
\xi
latex(xi_)
\xi
```


Issue created by migration from https://trac.sagemath.org/ticket/6267





---

archive/issue_comments_049963.json:
```json
{
    "body": "Is this a bug?  I thought it was a design decision.",
    "created_at": "2009-06-12T18:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6267#issuecomment-49963",
    "user": "https://github.com/jasongrout"
}
```

Is this a bug?  I thought it was a design decision.



---

archive/issue_comments_049964.json:
```json
{
    "body": "Note the following choice Sage makes (by design):\n\n\n```\nsage: latex(var('x0'))\nx_{0}\nsage: latex(var('x_0'))\nx_{0}\n```\n",
    "created_at": "2009-06-12T18:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6267#issuecomment-49964",
    "user": "https://github.com/jasongrout"
}
```

Note the following choice Sage makes (by design):


```
sage: latex(var('x0'))
x_{0}
sage: latex(var('x_0'))
x_{0}
```




---

archive/issue_comments_049965.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2009-06-12T22:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6267#issuecomment-49965",
    "user": "https://github.com/golam-m-hossain"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_049966.json:
```json
{
    "body": "I agree. Sage does typeset two different objects as same latex string\nby design. Sorry for the false alarm.",
    "created_at": "2009-06-12T22:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6267#issuecomment-49966",
    "user": "https://github.com/golam-m-hossain"
}
```

I agree. Sage does typeset two different objects as same latex string
by design. Sorry for the false alarm.



---

archive/issue_comments_049967.json:
```json
{
    "body": "Should we close this?",
    "created_at": "2010-02-02T05:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6267#issuecomment-49967",
    "user": "https://github.com/qed777"
}
```

Should we close this?



---

archive/issue_comments_049968.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-02-02T05:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6267#issuecomment-49968",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: invalid
