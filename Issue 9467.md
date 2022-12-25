# Issue 9467: p-adic l-series associated to modular Jacobians

archive/issues_009467.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is a first attempt at merging the code William and I wrote during Sage Days 22 to compute p-adic L-series associated to modular Jacobians.\n\nBelow is an example of a p-adic L-series associated to the rank 2 Jacobian of a curve (level N = 188) in \n\"Empirical evidence for the Birch and Swinnerton-Dyer conjectures for modular Jacobians of genus 2 curves\" (Flynn, Leprevost, Schaefer, Stein, Stoll, Wetherell).\n\nI realize the naming isn't quite right (this is the L-series of a\ncurve whose Jacobian is a certain quotient of J_0(N) ...), but here's the main function:\n\n```\n\nsage: J = J0(188)\nsage: L = J.padic_lseries(7)\nsage: f = L.series(5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9467\n\n",
    "created_at": "2010-07-09T20:15:29Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "p-adic l-series associated to modular Jacobians",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9467",
    "user": "https://github.com/jbalakrishnan"
}
```
Assignee: @williamstein

This is a first attempt at merging the code William and I wrote during Sage Days 22 to compute p-adic L-series associated to modular Jacobians.

Below is an example of a p-adic L-series associated to the rank 2 Jacobian of a curve (level N = 188) in 
"Empirical evidence for the Birch and Swinnerton-Dyer conjectures for modular Jacobians of genus 2 curves" (Flynn, Leprevost, Schaefer, Stein, Stoll, Wetherell).

I realize the naming isn't quite right (this is the L-series of a
curve whose Jacobian is a certain quotient of J_0(N) ...), but here's the main function:

```

sage: J = J0(188)
sage: L = J.padic_lseries(7)
sage: f = L.series(5)
```


Issue created by migration from https://trac.sagemath.org/ticket/9467





---

archive/issue_comments_090657.json:
```json
{
    "body": "Attachment [14329.patch](tarball://root/attachments/some-uuid/ticket9467/14329.patch) by @jbalakrishnan created at 2010-07-09 20:16:59",
    "created_at": "2010-07-09T20:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90657",
    "user": "https://github.com/jbalakrishnan"
}
```

Attachment [14329.patch](tarball://root/attachments/some-uuid/ticket9467/14329.patch) by @jbalakrishnan created at 2010-07-09 20:16:59



---

archive/issue_comments_090658.json:
```json
{
    "body": "Attachment [14330.patch](tarball://root/attachments/some-uuid/ticket9467/14330.patch) by @jbalakrishnan created at 2010-07-09 20:22:29",
    "created_at": "2010-07-09T20:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90658",
    "user": "https://github.com/jbalakrishnan"
}
```

Attachment [14330.patch](tarball://root/attachments/some-uuid/ticket9467/14330.patch) by @jbalakrishnan created at 2010-07-09 20:22:29



---

archive/issue_comments_090659.json:
```json
{
    "body": "New commits:",
    "created_at": "2018-08-19T16:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90659",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_090660.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-08-19T16:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90660",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090661.json:
```json
{
    "body": "Changing keywords from \"\" to \"lseries\".",
    "created_at": "2018-08-20T07:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90661",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "lseries".



---

archive/issue_comments_090662.json:
```json
{
    "body": "Changing keywords from \"lseries\" to \"L-series\".",
    "created_at": "2018-08-20T07:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90662",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "lseries" to "L-series".



---

archive/issue_comments_090663.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-11-28T09:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90663",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090664.json:
```json
{
    "body": "Changing keywords from \"L-series\" to \"lseries\".",
    "created_at": "2019-03-09T07:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9467#issuecomment-90664",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "L-series" to "lseries".
