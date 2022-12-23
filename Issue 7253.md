# Issue 7253: inefficient polynomial powering for positive characteristic

archive/issues_007253.json:
```json
{
    "body": "Assignee: tbd\n\nOne can take advantage of the fact that (a+b)<sup>p</sup> = a<sup>p</sup> + b<sup>p</sup> to quickly expand f<sup>n</sup> = f<sup>qp</sup> * f<sup>r</sup> (where r<p, so one can literally write out the resulting monomials). \n\nSee http://groups.google.com/group/sage-support/browse_thread/thread/38c3d619a7684a90\n\nIssue created by migration from https://trac.sagemath.org/ticket/7253\n\n",
    "created_at": "2009-10-20T06:07:13Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "inefficient polynomial powering for positive characteristic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7253",
    "user": "robertwb"
}
```
Assignee: tbd

One can take advantage of the fact that (a+b)<sup>p</sup> = a<sup>p</sup> + b<sup>p</sup> to quickly expand f<sup>n</sup> = f<sup>qp</sup> * f<sup>r</sup> (where r<p, so one can literally write out the resulting monomials). 

See http://groups.google.com/group/sage-support/browse_thread/thread/38c3d619a7684a90

Issue created by migration from https://trac.sagemath.org/ticket/7253





---

archive/issue_comments_060249.json:
```json
{
    "body": "This behavior still appears to be present in 2016. Since the underlying representation of multivariate polynomials over a finite field appears to be in Singular, I've raised the issue upstream: \n\nhttp://www.singular.uni-kl.de/forum/viewtopic.php?f=10&t=2523\n\nFor univariate polynomials over a finite field, the underlying representation is in FLINT, and there this seems to be handled correctly (although I haven't looked at the source or asked a developer to confirm):\n\n```\nsage: F = GF(7)\nsage: P.<x> = PolynomialRing(F)\nsage: u = (x^3 + 1)^3\nsage: time v = u^(7^7); # a large power!\nCPU times: user 1.17 s, sys: 44 ms, total: 1.21 s\nWall time: 1.21 s\nsage: time v = u^1000000; # even larger! \nCPU times: user 1.58 s, sys: 36 ms, total: 1.62 s\nWall time: 1.62 s\n```\n",
    "created_at": "2016-04-05T17:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7253#issuecomment-60249",
    "user": "kedlaya"
}
```

This behavior still appears to be present in 2016. Since the underlying representation of multivariate polynomials over a finite field appears to be in Singular, I've raised the issue upstream: 

http://www.singular.uni-kl.de/forum/viewtopic.php?f=10&t=2523

For univariate polynomials over a finite field, the underlying representation is in FLINT, and there this seems to be handled correctly (although I haven't looked at the source or asked a developer to confirm):

```
sage: F = GF(7)
sage: P.<x> = PolynomialRing(F)
sage: u = (x^3 + 1)^3
sage: time v = u^(7^7); # a large power!
CPU times: user 1.17 s, sys: 44 ms, total: 1.21 s
Wall time: 1.21 s
sage: time v = u^1000000; # even larger! 
CPU times: user 1.58 s, sys: 36 ms, total: 1.62 s
Wall time: 1.62 s
```




---

archive/issue_comments_060250.json:
```json
{
    "body": "This has been resolved upstream (see previous Singular link), so I propose to close this ticket.",
    "created_at": "2017-09-23T06:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7253#issuecomment-60250",
    "user": "kedlaya"
}
```

This has been resolved upstream (see previous Singular link), so I propose to close this ticket.



---

archive/issue_comments_060251.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-10-23T12:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7253#issuecomment-60251",
    "user": "kedlaya"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060252.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-10-25T16:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7253#issuecomment-60252",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060253.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-12-12T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7253#issuecomment-60253",
    "user": "embray"
}
```

Resolution: wontfix
