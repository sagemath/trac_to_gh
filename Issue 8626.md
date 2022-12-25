# Issue 8626: qqbar quadratic elements

archive/issues_008626.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  cwitty\n\nIt would be nice if roots of quadratics printed using the quadratic formula in QQbar, i.e., \n\n\n```\nsage: QQbar(sqrt(2))\nsqrt(2)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8626\n\n",
    "created_at": "2010-03-29T19:24:06Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "qqbar quadratic elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8626",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @aghitza

CC:  cwitty

It would be nice if roots of quadratics printed using the quadratic formula in QQbar, i.e., 


```
sage: QQbar(sqrt(2))
sqrt(2)
```


Issue created by migration from https://trac.sagemath.org/ticket/8626





---

archive/issue_comments_078077.json:
```json
{
    "body": "This patch almost certainly needs work, but does give some nice results:\n\n\n```\nsage: QQbar(sqrt(5))  \nsqrt(20)/2\nsage: QQbar(sqrt(2))  \nsqrt(8)/2\n```\n\n\nThings are not simplified because I don't want to do any extra work in the printing.",
    "created_at": "2010-03-29T19:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78077",
    "user": "https://github.com/jasongrout"
}
```

This patch almost certainly needs work, but does give some nice results:


```
sage: QQbar(sqrt(5))  
sqrt(20)/2
sage: QQbar(sqrt(2))  
sqrt(8)/2
```


Things are not simplified because I don't want to do any extra work in the printing.



---

archive/issue_comments_078078.json:
```json
{
    "body": "Another example with this patch:\n\n\n```\nsage: m=matrix(2,2,[0,1,1,1]);m\n[0 1]\n[1 1]\nsage: m.eigenvalues()          \n[(--1-sqrt(5))/2, (--1+sqrt(5))/2]\n\n```\n",
    "created_at": "2010-03-29T19:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78078",
    "user": "https://github.com/jasongrout"
}
```

Another example with this patch:


```
sage: m=matrix(2,2,[0,1,1,1]);m
[0 1]
[1 1]
sage: m.eigenvalues()          
[(--1-sqrt(5))/2, (--1+sqrt(5))/2]

```




---

archive/issue_comments_078079.json:
```json
{
    "body": "That last patch corrects the double negative, so I get:\n\n\n```\nsage: m=matrix(2,2,[0,1,1,1]);m\n[0 1]\n[1 1]\nsage: m.eigenvalues()  \n[(1-sqrt(5))/2, (1+sqrt(5))/2]\n\n```\n",
    "created_at": "2010-03-29T19:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78079",
    "user": "https://github.com/jasongrout"
}
```

That last patch corrects the double negative, so I get:


```
sage: m=matrix(2,2,[0,1,1,1]);m
[0 1]
[1 1]
sage: m.eigenvalues()  
[(1-sqrt(5))/2, (1+sqrt(5))/2]

```




---

archive/issue_comments_078080.json:
```json
{
    "body": "Attachment [trac-8626-qqbar-sqrt-printing.patch](tarball://root/attachments/some-uuid/ticket8626/trac-8626-qqbar-sqrt-printing.patch) by @jasongrout created at 2010-04-21 02:47:08",
    "created_at": "2010-04-21T02:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78080",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8626-qqbar-sqrt-printing.patch](tarball://root/attachments/some-uuid/ticket8626/trac-8626-qqbar-sqrt-printing.patch) by @jasongrout created at 2010-04-21 02:47:08



---

archive/issue_comments_078081.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-04-21T02:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78081",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_078082.json:
```json
{
    "body": "Attachment [trac-8626-qqbar-symbolics.patch](tarball://root/attachments/some-uuid/ticket8626/trac-8626-qqbar-symbolics.patch) by @jasongrout created at 2010-04-21 02:48:55\n\nI've attached a work-in-progress patch that allows qqbar elements to be converted to symbolics elements in a smart way, i.e., square roots become symbolic square roots, etc.",
    "created_at": "2010-04-21T02:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78082",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8626-qqbar-symbolics.patch](tarball://root/attachments/some-uuid/ticket8626/trac-8626-qqbar-symbolics.patch) by @jasongrout created at 2010-04-21 02:48:55

I've attached a work-in-progress patch that allows qqbar elements to be converted to symbolics elements in a smart way, i.e., square roots become symbolic square roots, etc.



---

archive/issue_comments_078083.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-21T02:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78083",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_078084.json:
```json
{
    "body": "Here is another problem that could probably be solved if qqbar elements could be converted to symbolics.  The application for this example was trying to plot a line from the eigenvector of a matrix:\n\n\n```\nsage: A=matrix(QQ,2,2,[2,5,1,2])\nsage: EV=A.right_eigenvectors()\nsage: EV\n[(-0.2360679774997897?, [(1, -0.4472135954999580?)], 1), (4.236067977499789?, [(1, 0.4472135954999580?)], 1)]\nsage: evec=EV[0][1][0]\nsage: var('t')\nt\nsage: evec.n()*t # works fine\n(t, -0.447213595499958*t)\nsage: t*evec\nTraceback (most recent call last):\n...\nNotImplementedError: symbol\n\n```\n",
    "created_at": "2010-09-22T03:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78084",
    "user": "https://github.com/jasongrout"
}
```

Here is another problem that could probably be solved if qqbar elements could be converted to symbolics.  The application for this example was trying to plot a line from the eigenvector of a matrix:


```
sage: A=matrix(QQ,2,2,[2,5,1,2])
sage: EV=A.right_eigenvectors()
sage: EV
[(-0.2360679774997897?, [(1, -0.4472135954999580?)], 1), (4.236067977499789?, [(1, 0.4472135954999580?)], 1)]
sage: evec=EV[0][1][0]
sage: var('t')
t
sage: evec.n()*t # works fine
(t, -0.447213595499958*t)
sage: t*evec
Traceback (most recent call last):
...
NotImplementedError: symbol

```




---

archive/issue_comments_078085.json:
```json
{
    "body": "Changing component from algebra to coercion.",
    "created_at": "2010-09-22T03:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78085",
    "user": "https://github.com/jasongrout"
}
```

Changing component from algebra to coercion.



---

archive/issue_comments_078086.json:
```json
{
    "body": "Related: #14239",
    "created_at": "2013-12-28T17:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78086",
    "user": "https://github.com/mezzarobba"
}
```

Related: #14239



---

archive/issue_comments_078087.json:
```json
{
    "body": "Duplicate of #14239",
    "created_at": "2014-12-13T22:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78087",
    "user": "https://github.com/jdemeyer"
}
```

Duplicate of #14239



---

archive/issue_comments_078088.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-12-13T22:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78088",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_078089.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-12-18T07:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8626#issuecomment-78089",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_008795.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-12-18T07:39:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8626",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8626#event-8795"
}
```
