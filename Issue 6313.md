# Issue 6313: optional doctest failure -- caused by maxima --> pynac switch ?

archive/issues_006313.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/symbolic/expression.pyx\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx\", line 482:\n    sage: magma(f)                         # optional - magma\nExpected:\n    sin(cos(x^2) + log(x))\nGot:\n    sin(log(x) + cos(x^2))\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx\", line 2803:\n    sage: maple.eval('subs(x^2 + y^2 = t, cos(x) + sin(y) + x^2 + y^2 + t)')          # optional requires maple\nExpected:\n    'cos(x)+sin(y)+x^2+y^2+t'\nGot:\n    'read \"/scratch/wstein/sage//temp/sage.math.washington.edu/560//interface//'\n**********************************************************************\n2 items had failures:\n   1 of   7 in __main__.example_14\n   1 of  18 in __main__.example_67\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_expression.py\n\t [26.8 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6313\n\n",
    "created_at": "2009-06-16T14:42:04Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- caused by maxima --> pynac switch ?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6313",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx", line 482:
    sage: magma(f)                         # optional - magma
Expected:
    sin(cos(x^2) + log(x))
Got:
    sin(log(x) + cos(x^2))
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx", line 2803:
    sage: maple.eval('subs(x^2 + y^2 = t, cos(x) + sin(y) + x^2 + y^2 + t)')          # optional requires maple
Expected:
    'cos(x)+sin(y)+x^2+y^2+t'
Got:
    'read "/scratch/wstein/sage//temp/sage.math.washington.edu/560//interface//'
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_14
   1 of  18 in __main__.example_67
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_expression.py
	 [26.8 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6313





---

archive/issue_comments_050299.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2022-08-06T19:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6313#issuecomment-50299",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050300.json:
```json
{
    "body": "outdated, should close",
    "created_at": "2022-08-06T19:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6313#issuecomment-50300",
    "user": "https://github.com/mkoeppe"
}
```

outdated, should close



---

archive/issue_comments_050301.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-08-09T05:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6313#issuecomment-50301",
    "user": "https://github.com/DaveWitteMorris"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050302.json:
```json
{
    "body": "I agree.",
    "created_at": "2022-08-09T05:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6313#issuecomment-50302",
    "user": "https://github.com/DaveWitteMorris"
}
```

I agree.



---

archive/issue_comments_050303.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-09-01T02:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6313#issuecomment-50303",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
