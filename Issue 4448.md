# Issue 4448: easy-to-fix (?) bug in interact with matrices

archive/issues_004448.json:
```json
{
    "body": "Assignee: @itolkov\n\nTry this interact in the notebook:\n\n```\n@interact\ndef f(n=matrix([[pi^2]])):\n    print n\n```\n\n\nNotice that the matrix input appears empty.  What is happening, I think, is that\nstr(...) is being called on each entry instead of repr(...) which causes uses of ASCII art.   It seems this is a problem only for matrices.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4448\n\n",
    "created_at": "2008-11-05T20:06:02Z",
    "labels": [
        "component: interact",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "easy-to-fix (?) bug in interact with matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4448",
    "user": "https://github.com/williamstein"
}
```
Assignee: @itolkov

Try this interact in the notebook:

```
@interact
def f(n=matrix([[pi^2]])):
    print n
```


Notice that the matrix input appears empty.  What is happening, I think, is that
str(...) is being called on each entry instead of repr(...) which causes uses of ASCII art.   It seems this is a problem only for matrices.

Issue created by migration from https://trac.sagemath.org/ticket/4448





---

archive/issue_comments_032736.json:
```json
{
    "body": "Attachment [trac-4448-interact-grid.patch](tarball://root/attachments/some-uuid/ticket4448/trac-4448-interact-grid.patch) by @jasongrout created at 2008-11-05 20:38:10\n\nIndeed, that was the problem.",
    "created_at": "2008-11-05T20:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4448#issuecomment-32736",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-4448-interact-grid.patch](tarball://root/attachments/some-uuid/ticket4448/trac-4448-interact-grid.patch) by @jasongrout created at 2008-11-05 20:38:10

Indeed, that was the problem.



---

archive/issue_comments_032737.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-08T05:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4448#issuecomment-32737",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_comments_032738.json:
```json
{
    "body": "Merged in Sage 3.2.rc0",
    "created_at": "2008-11-08T07:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4448#issuecomment-32738",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc0



---

archive/issue_comments_032739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-08T07:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4448#issuecomment-32739",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
