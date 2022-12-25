# Issue 7152: Segmentation fault with monomials()

archive/issues_007152.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mraum@mpim-bonn.mpg.de @malb @wjp\n\nKeywords: monomials, singular\n\nUsing implicite coercion and then calling monomials might cause a segmentation fault. This is a side effect.\n\n```\nK.<rho> = NumberField(x**2 + 1)\nR.<x,y> = QQ[]\np = rho*x\nq = x\np.monomials()\n ...\nq.monomials()\n ...\np.monomials()\n Segmentation Fault\n```\n\nGoing back to line 5 you can avoid this by\n\n```\np.parent()(p).monomials()\n ...\nq.parent()(q).monomials()\n ...\np.parent()(p).monomials()\n ...\n```\nThis might be used as a workaround.\n\nIf no implicite coercion is involved, everything works fine, i.e. use\n\n```\nR.<x,y> = K[]\n```\n\nThis is most probably related to #6160.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7152\n\n",
    "closed_at": "2010-01-18T23:06:13Z",
    "created_at": "2009-10-08T08:11:11Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Segmentation fault with monomials()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7152",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```
Assignee: tbd

CC:  mraum@mpim-bonn.mpg.de @malb @wjp

Keywords: monomials, singular

Using implicite coercion and then calling monomials might cause a segmentation fault. This is a side effect.

```
K.<rho> = NumberField(x**2 + 1)
R.<x,y> = QQ[]
p = rho*x
q = x
p.monomials()
 ...
q.monomials()
 ...
p.monomials()
 Segmentation Fault
```

Going back to line 5 you can avoid this by

```
p.parent()(p).monomials()
 ...
q.parent()(q).monomials()
 ...
p.parent()(p).monomials()
 ...
```
This might be used as a workaround.

If no implicite coercion is involved, everything works fine, i.e. use

```
R.<x,y> = K[]
```

This is most probably related to #6160.

Issue created by migration from https://trac.sagemath.org/ticket/7152





---

archive/issue_comments_059142.json:
```json
{
    "body": "Changing keywords from \"monomials, multivariate polynomial ring, coercion\" to \"monomials, singular\".",
    "created_at": "2010-01-17T02:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7152#issuecomment-59142",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "monomials, multivariate polynomial ring, coercion" to "monomials, singular".



---

archive/issue_comments_059143.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T02:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7152#issuecomment-59143",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059144.json:
```json
{
    "body": "This segfaults because the `monomials()` method doesn't set the current ring. attachment:trac_7152-monomials_cring.patch contains the fix.",
    "created_at": "2010-01-17T02:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7152#issuecomment-59144",
    "user": "https://github.com/burcin"
}
```

This segfaults because the `monomials()` method doesn't set the current ring. attachment:trac_7152-monomials_cring.patch contains the fix.



---

archive/issue_comments_059145.json:
```json
{
    "body": "Attachment [trac_7152-monomials_cring.patch](tarball://root/attachments/some-uuid/ticket7152/trac_7152-monomials_cring.patch) by @burcin created at 2010-01-17 02:36:37\n\nset current ring for singular in monomials() method",
    "created_at": "2010-01-17T02:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7152#issuecomment-59145",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7152-monomials_cring.patch](tarball://root/attachments/some-uuid/ticket7152/trac_7152-monomials_cring.patch) by @burcin created at 2010-01-17 02:36:37

set current ring for singular in monomials() method



---

archive/issue_comments_059146.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T17:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7152#issuecomment-59146",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059147.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-01-17T17:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7152#issuecomment-59147",
    "user": "https://github.com/wjp"
}
```

Looks good.



---

archive/issue_comments_059148.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T23:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7152#issuecomment-59148",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_016909.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-18T23:06:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7152",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7152#event-16909"
}
```
