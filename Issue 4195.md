# Issue 4195: [with patch, needs review] implicit plotting for multivariate polynomial ideals

archive/issues_004195.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @wdjoyner\n\nKeywords: plotting, ideal, polynomial\n\nThis now works without having surf installed:\n\n```\nsage: R.<x,y> = PolynomialRing(QQ,2)\nsage: I = R.ideal([y^3 - x^2])\nsage: I.plot()\nsage: I = R.ideal([y^2 - x^2 - 1])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4195\n\n",
    "created_at": "2008-09-25T12:09:01Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] implicit plotting for multivariate polynomial ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4195",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

CC:  @wdjoyner

Keywords: plotting, ideal, polynomial

This now works without having surf installed:

```
sage: R.<x,y> = PolynomialRing(QQ,2)
sage: I = R.ideal([y^3 - x^2])
sage: I.plot()
sage: I = R.ideal([y^2 - x^2 - 1])
```


Issue created by migration from https://trac.sagemath.org/ticket/4195





---

archive/issue_comments_030388.json:
```json
{
    "body": "Attachment [mpolynomial_ideal_plot.patch](tarball://root/attachments/some-uuid/ticket4195/mpolynomial_ideal_plot.patch) by @malb created at 2008-09-25 12:09:51\n\nI'm CCing wdj as he wrote the original plotting code.",
    "created_at": "2008-09-25T12:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4195#issuecomment-30388",
    "user": "https://github.com/malb"
}
```

Attachment [mpolynomial_ideal_plot.patch](tarball://root/attachments/some-uuid/ticket4195/mpolynomial_ideal_plot.patch) by @malb created at 2008-09-25 12:09:51

I'm CCing wdj as he wrote the original plotting code.



---

archive/issue_comments_030389.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-25T19:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4195#issuecomment-30389",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_030390.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-26T05:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4195#issuecomment-30390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030391.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T05:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4195#issuecomment-30391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
