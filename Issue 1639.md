# Issue 1639: missing documentation P.completion()

archive/issues_001639.json:
```json
{
    "body": "Assignee: tba\n\nHow works completion?\n\n\n\n```\nP.<x> = PolynomialRing(QQ); P.completion?\n```\n\n\n\ntells me\n\n\n```\nFile:        /opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\nType:        <type 'instancemethod'>\nDefinition:  P.completion(p, prec, extras)\nDocstring: \nx.__init__(...) initializes x; see x.__class__.__doc__ for signature\n```\n\n\n\nwhat's the p and examples are missing...\n\nIssue created by migration from https://trac.sagemath.org/ticket/1639\n\n",
    "created_at": "2007-12-30T13:35:00Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "title": "missing documentation P.completion()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1639",
    "user": "schilly"
}
```
Assignee: tba

How works completion?



```
P.<x> = PolynomialRing(QQ); P.completion?
```



tells me


```
File:        /opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py
Type:        <type 'instancemethod'>
Definition:  P.completion(p, prec, extras)
Docstring: 
x.__init__(...) initializes x; see x.__class__.__doc__ for signature
```



what's the p and examples are missing...

Issue created by migration from https://trac.sagemath.org/ticket/1639





---

archive/issue_comments_010418.json:
```json
{
    "body": "Changing assignee from tba to failure.",
    "created_at": "2008-02-03T17:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1639#issuecomment-10418",
    "user": "AlexGhitza"
}
```

Changing assignee from tba to failure.



---

archive/issue_comments_010419.json:
```json
{
    "body": "Changing component from documentation to doctest.",
    "created_at": "2008-02-03T17:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1639#issuecomment-10419",
    "user": "AlexGhitza"
}
```

Changing component from documentation to doctest.



---

archive/issue_comments_010420.json:
```json
{
    "body": "Attachment\n\nadds docstring and examples",
    "created_at": "2008-02-17T22:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1639#issuecomment-10420",
    "user": "cremona"
}
```

Attachment

adds docstring and examples



---

archive/issue_comments_010421.json:
```json
{
    "body": "The attached patch adds docstring and tests.\n\nThis ticket should perhaps be kept open in another form so that someone could implement the completion function for irreducuble polynomials other than just x.  I am happy to be the owner of that.",
    "created_at": "2008-02-17T22:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1639#issuecomment-10421",
    "user": "cremona"
}
```

The attached patch adds docstring and tests.

This ticket should perhaps be kept open in another form so that someone could implement the completion function for irreducuble polynomials other than just x.  I am happy to be the owner of that.



---

archive/issue_comments_010422.json:
```json
{
    "body": "Applies to 2.10.3.alpha0 and passes tests for me.",
    "created_at": "2008-02-27T23:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1639#issuecomment-10422",
    "user": "mhansen"
}
```

Applies to 2.10.3.alpha0 and passes tests for me.



---

archive/issue_comments_010423.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T06:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1639#issuecomment-10423",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010424.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T06:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1639#issuecomment-10424",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0
