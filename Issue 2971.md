# Issue 2971: One method of creating a Laurent poly ring doesn't give access to the variables

archive/issues_002971.json:
```json
{
    "body": "Assignee: mhansen\n\nOne method of creating a Laurent poly ring doesn't give access to the variables.\n\n```\nsage: R = LaurentPolynomialRing(QQ,'x',3) ; R\nMultivariate Laurent Polynomial Ring in x0, x1, x2 over Rational Field\nsage: x0\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/home/bump/sage/<ipython console> in <module>()\n\n<type 'exceptions.NameError'>: name 'x0' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2971\n\n",
    "created_at": "2008-04-20T05:26:13Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "One method of creating a Laurent poly ring doesn't give access to the variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2971",
    "user": "bump"
}
```
Assignee: mhansen

One method of creating a Laurent poly ring doesn't give access to the variables.

```
sage: R = LaurentPolynomialRing(QQ,'x',3) ; R
Multivariate Laurent Polynomial Ring in x0, x1, x2 over Rational Field
sage: x0
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/home/bump/sage/<ipython console> in <module>()

<type 'exceptions.NameError'>: name 'x0' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/2971





---

archive/issue_comments_020475.json:
```json
{
    "body": "Hi Dan,\n\nThat is by design, and the other polynomial rings work that way as well.\n\n\n```\nsage: R = PolynomialRing(QQ,'x',3)\nsage: x0\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/opt/sage-3.0.alpha6/devel/sage-839/<ipython console> in <module>()\n\n<type 'exceptions.NameError'>: name 'x0' is not defined\n```\n\n\nYou can use the .inject_variables() method to get access to the variables.\n\n\n```\nsage: R.inject_variables()\nDefining x0, x1, x2\nsage: x0\nx0\n```\n",
    "created_at": "2008-04-20T05:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2971#issuecomment-20475",
    "user": "mhansen"
}
```

Hi Dan,

That is by design, and the other polynomial rings work that way as well.


```
sage: R = PolynomialRing(QQ,'x',3)
sage: x0
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/opt/sage-3.0.alpha6/devel/sage-839/<ipython console> in <module>()

<type 'exceptions.NameError'>: name 'x0' is not defined
```


You can use the .inject_variables() method to get access to the variables.


```
sage: R.inject_variables()
Defining x0, x1, x2
sage: x0
x0
```




---

archive/issue_comments_020476.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-04-20T05:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2971#issuecomment-20476",
    "user": "mhansen"
}
```

Resolution: invalid
