# Issue 7798: Recomputing graphs after changing range of axes

archive/issues_007798.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: axes, range\n\nThe purpose of the ticket is be able to recompute plots such that the following problem can be solved\n\n```\n\n# to increase the range of axis does not extend the plots\n# we need to recompute the plot to do that\nvar('x')\np = plot(x**,x)\np.set_axes_range(-10,10,-10,10)\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7798\n\n",
    "created_at": "2009-12-31T00:56:07Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "Recomputing graphs after changing range of axes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7798",
    "user": "https://trac.sagemath.org/admin/accounts/users/slosoi"
}
```
Assignee: @williamstein

Keywords: axes, range

The purpose of the ticket is be able to recompute plots such that the following problem can be solved

```

# to increase the range of axis does not extend the plots
# we need to recompute the plot to do that
var('x')
p = plot(x**,x)
p.set_axes_range(-10,10,-10,10)

```

Issue created by migration from https://trac.sagemath.org/ticket/7798





---

archive/issue_comments_067357.json:
```json
{
    "body": "Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket7798/plot.patch) by slosoi created at 2009-12-31 01:11:28\n\nNot working attempt: trying to get some text initially to the plot",
    "created_at": "2009-12-31T01:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67357",
    "user": "https://trac.sagemath.org/admin/accounts/users/slosoi"
}
```

Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket7798/plot.patch) by slosoi created at 2009-12-31 01:11:28

Not working attempt: trying to get some text initially to the plot



---

archive/issue_comments_067358.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-12-31T01:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67358",
    "user": "https://trac.sagemath.org/admin/accounts/users/slosoi"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_067359.json:
```json
{
    "body": "To recompute line first to get coordinates right",
    "created_at": "2009-12-31T23:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67359",
    "user": "https://trac.sagemath.org/admin/accounts/users/slosoi"
}
```

To recompute line first to get coordinates right



---

archive/issue_comments_067360.json:
```json
{
    "body": "Attachment [recomputing_line.patch](tarball://root/attachments/some-uuid/ticket7798/recomputing_line.patch) by slosoi created at 2009-12-31 23:36:57\n\nI get the error in running the patch. There is somewhere a bug which prevents the loading of the module.",
    "created_at": "2009-12-31T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67360",
    "user": "https://trac.sagemath.org/admin/accounts/users/slosoi"
}
```

Attachment [recomputing_line.patch](tarball://root/attachments/some-uuid/ticket7798/recomputing_line.patch) by slosoi created at 2009-12-31 23:36:57

I get the error in running the patch. There is somewhere a bug which prevents the loading of the module.



---

archive/issue_comments_067361.json:
```json
{
    "body": "Attachment [error_for_recomputing_line](tarball://root/attachments/some-uuid/ticket7798/error_for_recomputing_line) by slosoi created at 2009-12-31 23:42:10",
    "created_at": "2009-12-31T23:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67361",
    "user": "https://trac.sagemath.org/admin/accounts/users/slosoi"
}
```

Attachment [error_for_recomputing_line](tarball://root/attachments/some-uuid/ticket7798/error_for_recomputing_line) by slosoi created at 2009-12-31 23:42:10



---

archive/issue_comments_067362.json:
```json
{
    "body": "Changing keywords from \"plot, label\" to \"axes, range\".",
    "created_at": "2010-01-02T04:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67362",
    "user": "https://trac.sagemath.org/admin/accounts/users/slosoi"
}
```

Changing keywords from "plot, label" to "axes, range".



---

archive/issue_comments_067363.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7798#issuecomment-67363",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.
