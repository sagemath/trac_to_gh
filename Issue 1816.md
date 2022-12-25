# Issue 1816: rename MPolynomialRing.repr_long method to __str__

archive/issues_001816.json:
```json
{
    "body": "Assignee: @malb\n\nJust as symbolic variables behave (and what is the Python-way IIRC):\n\n```\nsage: f = x/var('y')\nsage: f\nx/y\nsage: str(f)\n'                                       x\\r\\n                                       -\\r\\n                                       y'\nsage: print str(f)\n                                       x\n                                       -\n                                       y\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1816\n\n",
    "created_at": "2008-01-17T23:38:32Z",
    "labels": [
        "component: commutative algebra",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "rename MPolynomialRing.repr_long method to __str__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1816",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Just as symbolic variables behave (and what is the Python-way IIRC):

```
sage: f = x/var('y')
sage: f
x/y
sage: str(f)
'                                       x\r\n                                       -\r\n                                       y'
sage: print str(f)
                                       x
                                       -
                                       y
```


Issue created by migration from https://trac.sagemath.org/ticket/1816





---

archive/issue_comments_011446.json:
```json
{
    "body": "Attachment [trac_1816.patch](tarball://root/attachments/some-uuid/ticket1816/trac_1816.patch) by @malb created at 2008-01-18 17:11:10",
    "created_at": "2008-01-18T17:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1816#issuecomment-11446",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1816.patch](tarball://root/attachments/some-uuid/ticket1816/trac_1816.patch) by @malb created at 2008-01-18 17:11:10



---

archive/issue_comments_011447.json:
```json
{
    "body": "The patch is fine, and does what it says, but it makes it look like printing a polynomial ring will give this verbose output:\n\n```\nsage: P.<x,y,z> = PolynomialRing(QQ,order=TermOrder('degrevlex',1)+TermOrder('lex',2)) \nsage: print P\nMultivariate Polynomial Ring\nBase Ring : Rational Field \nSize : 3 Variables \nBlock  0 : Ordering : degrevlex \n```\n\nThat's *not* okay -- way too much by default!",
    "created_at": "2008-01-20T07:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1816#issuecomment-11447",
    "user": "https://github.com/ncalexan"
}
```

The patch is fine, and does what it says, but it makes it look like printing a polynomial ring will give this verbose output:

```
sage: P.<x,y,z> = PolynomialRing(QQ,order=TermOrder('degrevlex',1)+TermOrder('lex',2)) 
sage: print P
Multivariate Polynomial Ring
Base Ring : Rational Field 
Size : 3 Variables 
Block  0 : Ordering : degrevlex 
```

That's *not* okay -- way too much by default!



---

archive/issue_comments_011448.json:
```json
{
    "body": "Because I disagree with Nick's verdict, I forwarded this to [sage-devel]:\n\n  http://groups.google.com/group/sage-devel/browse_thread/thread/612b3ec4a61310fa\n\nI figure, that this is more a design choice than a correctness issue and thus it should be discussed on [sage-devel] rather than here. I hope that's okay with you, Nick.",
    "created_at": "2008-01-20T16:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1816#issuecomment-11448",
    "user": "https://github.com/malb"
}
```

Because I disagree with Nick's verdict, I forwarded this to [sage-devel]:

  http://groups.google.com/group/sage-devel/browse_thread/thread/612b3ec4a61310fa

I figure, that this is more a design choice than a correctness issue and thus it should be discussed on [sage-devel] rather than here. I hope that's okay with you, Nick.



---

archive/issue_comments_011449.json:
```json
{
    "body": "My impression is: The verdict on [sage-devel] was overall negative, so I propose to close this ticket as `wontfix`.",
    "created_at": "2008-02-27T00:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1816#issuecomment-11449",
    "user": "https://github.com/malb"
}
```

My impression is: The verdict on [sage-devel] was overall negative, so I propose to close this ticket as `wontfix`.



---

archive/issue_events_001973.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-04-01T12:06:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1816",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1816#event-1973"
}
```



---

archive/issue_comments_011450.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-04-01T12:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1816#issuecomment-11450",
    "user": "https://github.com/malb"
}
```

Resolution: wontfix
