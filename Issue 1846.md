# Issue 1846: maxima looses minus signs in symbolic expression

archive/issues_001846.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider\n\n```\nlog(a*e^(-a*x-b)).simplify_exp()\n```\n\n\nThis gets expanded correctly, however\n\n\n```\nlog(a*e^(-a*x-b)/(1+exp(-a*x-b))^2 ).simplify_exp()\n```\n\nappears to lose the minus signs on ax and b.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1846\n\n",
    "created_at": "2008-01-19T09:43:52Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "maxima looses minus signs in symbolic expression",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1846",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: @williamstein

Consider

```
log(a*e^(-a*x-b)).simplify_exp()
```


This gets expanded correctly, however


```
log(a*e^(-a*x-b)/(1+exp(-a*x-b))^2 ).simplify_exp()
```

appears to lose the minus signs on ax and b.




Issue created by migration from https://trac.sagemath.org/ticket/1846





---

archive/issue_comments_011658.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-01-19T14:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1846#issuecomment-11658",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_011659.json:
```json
{
    "body": "Actually Sage is right and you are wrong, because of the identity `log(e^(-a*x - b) + 1) == log(e^(a*x + b) + 1) - a*x - b` which one can derive from Taylor expansions of `log(x+1)` and `log(x^(-1) + 1)`.  See below. \n\n\n\n```\nh = log(exp(-a*x-b) + 1)\n```\n\n\n\n```\nh == h.simplify_exp()\n///\nlog(e^(-a*x - b) + 1) == log(e^(a*x + b) + 1) - a*x - b\n```\n\n\n\n```\nlog(x+1).taylor(x,0,5)\n///\nx - x^2/2 + x^3/3 - x^4/4 + x^5/5\n```\n\n\n\n```\nlog(x^(-1)+1).taylor(x,0,5)\n///\n-log(x) + x - x^2/2 + x^3/3 - x^4/4 + x^5/5\n```\n",
    "created_at": "2008-01-19T14:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1846#issuecomment-11659",
    "user": "https://github.com/williamstein"
}
```

Actually Sage is right and you are wrong, because of the identity `log(e^(-a*x - b) + 1) == log(e^(a*x + b) + 1) - a*x - b` which one can derive from Taylor expansions of `log(x+1)` and `log(x^(-1) + 1)`.  See below. 



```
h = log(exp(-a*x-b) + 1)
```



```
h == h.simplify_exp()
///
log(e^(-a*x - b) + 1) == log(e^(a*x + b) + 1) - a*x - b
```



```
log(x+1).taylor(x,0,5)
///
x - x^2/2 + x^3/3 - x^4/4 + x^5/5
```



```
log(x^(-1)+1).taylor(x,0,5)
///
-log(x) + x - x^2/2 + x^3/3 - x^4/4 + x^5/5
```

