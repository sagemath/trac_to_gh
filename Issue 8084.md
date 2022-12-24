# Issue 8084: fix "show" in the notebook for strings

archive/issues_008084.json:
```json
{
    "body": "Assignee: tbd\n\nFrom [this thread in sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f7961d6de8646b26?tvc=2):\n\n```\nwhen doing in notebook \nsage: show('x^2') \nor \nsage: show(type(factor)) \nI get error Unknown control sequence '\\texttt' \n```\n\nThere are other problems, too; for example, from the command line (not the notebook), \n\n```\nsage: view(type(factor))\nsage: view(identity_matrix)\n```\n\nproduce odd-looking output -- see the attached pngs.  (The old versions are before the patch, the new ones afterwards.  If you wanted output like the old version of `view(identity_matrix)`, it's probably better to do `browse_sage_doc(identity_matrix)` instead.)\n\nThe attached patch should fix these problems.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8084\n\n",
    "created_at": "2010-01-26T21:28:05Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "fix \"show\" in the notebook for strings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8084",
    "user": "jhpalmieri"
}
```
Assignee: tbd

From [this thread in sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f7961d6de8646b26?tvc=2):

```
when doing in notebook 
sage: show('x^2') 
or 
sage: show(type(factor)) 
I get error Unknown control sequence '\texttt' 
```

There are other problems, too; for example, from the command line (not the notebook), 

```
sage: view(type(factor))
sage: view(identity_matrix)
```

produce odd-looking output -- see the attached pngs.  (The old versions are before the patch, the new ones afterwards.  If you wanted output like the old version of `view(identity_matrix)`, it's probably better to do `browse_sage_doc(identity_matrix)` instead.)

The attached patch should fix these problems.

Issue created by migration from https://trac.sagemath.org/ticket/8084





---

archive/issue_comments_070842.json:
```json
{
    "body": "Attachment [factor_old.png](tarball://root/attachments/some-uuid/ticket8084/factor_old.png) by jhpalmieri created at 2010-01-26 21:28:49\n\noutput of view(type(factor)) before the patch",
    "created_at": "2010-01-26T21:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70842",
    "user": "jhpalmieri"
}
```

Attachment [factor_old.png](tarball://root/attachments/some-uuid/ticket8084/factor_old.png) by jhpalmieri created at 2010-01-26 21:28:49

output of view(type(factor)) before the patch



---

archive/issue_comments_070843.json:
```json
{
    "body": "output of view(type(factor)) after the patch",
    "created_at": "2010-01-26T21:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70843",
    "user": "jhpalmieri"
}
```

output of view(type(factor)) after the patch



---

archive/issue_comments_070844.json:
```json
{
    "body": "Attachment [factor_new.png](tarball://root/attachments/some-uuid/ticket8084/factor_new.png) by jhpalmieri created at 2010-01-28 21:15:57",
    "created_at": "2010-01-28T21:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70844",
    "user": "jhpalmieri"
}
```

Attachment [factor_new.png](tarball://root/attachments/some-uuid/ticket8084/factor_new.png) by jhpalmieri created at 2010-01-28 21:15:57



---

archive/issue_comments_070845.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T21:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70845",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070846.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T22:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70846",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070847.json:
```json
{
    "body": "Changing keywords from \"\" to \"latex, jsmath\".",
    "created_at": "2010-01-28T22:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70847",
    "user": "robert.marik"
}
```

Changing keywords from "" to "latex, jsmath".



---

archive/issue_comments_070848.json:
```json
{
    "body": "Works for me and fixes the problem in Sage 4.3.1. Tests passed. Thanks for the patch.",
    "created_at": "2010-01-28T22:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70848",
    "user": "robert.marik"
}
```

Works for me and fixes the problem in Sage 4.3.1. Tests passed. Thanks for the patch.



---

archive/issue_comments_070849.json:
```json
{
    "body": "Merged [trac_8084-show.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8084/trac_8084-show.patch).",
    "created_at": "2010-01-30T23:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70849",
    "user": "mvngu"
}
```

Merged [trac_8084-show.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8084/trac_8084-show.patch).



---

archive/issue_comments_070850.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70850",
    "user": "mvngu"
}
```

Resolution: fixed
