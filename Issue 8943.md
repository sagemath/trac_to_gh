# Issue 8943: RuntimeError with series

archive/issues_008943.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: series, taylor\n\nThe function *series* can not give the power series expansion of f(x)=(1+arctan(x))**(1/x) , while *taylor* succeeds. Note that the function f can be continuously extended at 0.\n\n\n```\nsage: taylor((1+arctan(x))**(1/x), x, 0, 3)\n1/16*x^3*e + 1/8*x^2*e - 1/2*x*e + e\nsage: ((1+arctan(x))**(1/x)).series(x==0, 3)\nRuntimeError: power::eval(): division by zero\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8943\n\n",
    "created_at": "2010-05-10T09:42:29Z",
    "labels": [
        "component: calculus",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "RuntimeError with series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8943",
    "user": "https://trac.sagemath.org/admin/accounts/users/casamayou"
}
```
Assignee: @burcin

Keywords: series, taylor

The function *series* can not give the power series expansion of f(x)=(1+arctan(x))**(1/x) , while *taylor* succeeds. Note that the function f can be continuously extended at 0.


```
sage: taylor((1+arctan(x))**(1/x), x, 0, 3)
1/16*x^3*e + 1/8*x^2*e - 1/2*x*e + e
sage: ((1+arctan(x))**(1/x)).series(x==0, 3)
RuntimeError: power::eval(): division by zero
```


Issue created by migration from https://trac.sagemath.org/ticket/8943





---

archive/issue_comments_082209.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2011-03-16T16:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82209",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from trivial to minor.



---

archive/issue_comments_082210.json:
```json
{
    "body": "Looks like this is in Ginac/Pynac.  But maybe it makes sense *not* to have an answer here?  After all, the technical definition would imply that f doesn't have a Taylor series there, if it doesn't even exist.  Probably Maxima is more lenient about such things.",
    "created_at": "2011-03-16T16:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82210",
    "user": "https://github.com/kcrisman"
}
```

Looks like this is in Ginac/Pynac.  But maybe it makes sense *not* to have an answer here?  After all, the technical definition would imply that f doesn't have a Taylor series there, if it doesn't even exist.  Probably Maxima is more lenient about such things.



---

archive/issue_comments_082211.json:
```json
{
    "body": "Attachment [trac_8943-series.patch](tarball://root/attachments/some-uuid/ticket8943/trac_8943-series.patch) by @burcin created at 2011-05-08 19:51:29\n\nThis was fixed upstream in ginac. The changes will be in the next pynac release. Patch with doctest is attached.",
    "created_at": "2011-05-08T19:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82211",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8943-series.patch](tarball://root/attachments/some-uuid/ticket8943/trac_8943-series.patch) by @burcin created at 2011-05-08 19:51:29

This was fixed upstream in ginac. The changes will be in the next pynac release. Patch with doctest is attached.



---

archive/issue_comments_082212.json:
```json
{
    "body": "New pynac package with the fix is at #11317.",
    "created_at": "2011-05-09T15:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82212",
    "user": "https://github.com/burcin"
}
```

New pynac package with the fix is at #11317.



---

archive/issue_comments_082213.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-09T15:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82213",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082214.json:
```json
{
    "body": "This is nice, and the other examples given by the author also did not work before but now do:\n\n```\nsage: (cos(x)^(sin(x)/x)).series(x==0,9)\n1 + (-1/2)*x^2 + 1/8*x^4 + (-1/30)*x^6 + 631/120960*x^8 + Order(x^9)\nsage: ((1+x)^(1/x)).series(x==0,9)\n(e) + (-1/2*e)*x + (11/24*e)*x^2 + (-7/16*e)*x^3 + (2447/5760*e)*x^4 + (-959/2304*e)*x^5 + (238043/580608*e)*x^6 + (-67223/165888*e)*x^7 + (559440199/1393459200*e)*x^8 + Order(x^9)\n```\n\n\nAlso, the new series does correctly approximate the original function near x=0 :)",
    "created_at": "2011-05-09T19:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82214",
    "user": "https://github.com/kcrisman"
}
```

This is nice, and the other examples given by the author also did not work before but now do:

```
sage: (cos(x)^(sin(x)/x)).series(x==0,9)
1 + (-1/2)*x^2 + 1/8*x^4 + (-1/30)*x^6 + 631/120960*x^8 + Order(x^9)
sage: ((1+x)^(1/x)).series(x==0,9)
(e) + (-1/2*e)*x + (11/24*e)*x^2 + (-7/16*e)*x^3 + (2447/5760*e)*x^4 + (-959/2304*e)*x^5 + (238043/580608*e)*x^6 + (-67223/165888*e)*x^7 + (559440199/1393459200*e)*x^8 + Order(x^9)
```


Also, the new series does correctly approximate the original function near x=0 :)



---

archive/issue_comments_082215.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-09T19:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82215",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082216.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-27T12:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8943#issuecomment-82216",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009097.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-05-27T12:01:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8943",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8943#event-9097"
}
```
