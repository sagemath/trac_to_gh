# Issue 8084: fix "show" in the notebook for strings

archive/issues_008084.json:
```json
{
    "body": "Assignee: tbd\n\nFrom [this thread in sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f7961d6de8646b26?tvc=2):\n\n```\nwhen doing in notebook \nsage: show('x^2') \nor \nsage: show(type(factor)) \nI get error Unknown control sequence '\\texttt' \n```\n\nThere are other problems, too; for example, from the command line (not the notebook), \n\n```\nsage: view(type(factor))\nsage: view(identity_matrix)\n```\n\nproduce odd-looking output -- see the attached pngs.  (The old versions are before the patch, the new ones afterwards.  If you wanted output like the old version of `view(identity_matrix)`, it's probably better to do `browse_sage_doc(identity_matrix)` instead.)\n\nThe attached patch should fix these problems.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8084\n\n",
    "created_at": "2010-01-26T21:28:05Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "fix \"show\" in the notebook for strings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8084",
    "user": "https://github.com/jhpalmieri"
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

archive/issue_comments_070721.json:
```json
{
    "body": "Attachment [factor_old.png](tarball://root/attachments/some-uuid/ticket8084/factor_old.png) by @jhpalmieri created at 2010-01-26 21:28:49\n\noutput of view(type(factor)) before the patch",
    "created_at": "2010-01-26T21:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70721",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [factor_old.png](tarball://root/attachments/some-uuid/ticket8084/factor_old.png) by @jhpalmieri created at 2010-01-26 21:28:49

output of view(type(factor)) before the patch



---

archive/issue_comments_070722.json:
```json
{
    "body": "output of view(type(factor)) after the patch",
    "created_at": "2010-01-26T21:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70722",
    "user": "https://github.com/jhpalmieri"
}
```

output of view(type(factor)) after the patch



---

archive/issue_comments_070723.json:
```json
{
    "body": "Attachment [factor_new.png](tarball://root/attachments/some-uuid/ticket8084/factor_new.png) by @jhpalmieri created at 2010-01-28 21:15:57",
    "created_at": "2010-01-28T21:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70723",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [factor_new.png](tarball://root/attachments/some-uuid/ticket8084/factor_new.png) by @jhpalmieri created at 2010-01-28 21:15:57



---

archive/issue_comments_070724.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T21:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70724",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070725.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T22:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70725",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070726.json:
```json
{
    "body": "Changing keywords from \"\" to \"latex, jsmath\".",
    "created_at": "2010-01-28T22:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70726",
    "user": "https://github.com/robert-marik"
}
```

Changing keywords from "" to "latex, jsmath".



---

archive/issue_comments_070727.json:
```json
{
    "body": "Works for me and fixes the problem in Sage 4.3.1. Tests passed. Thanks for the patch.",
    "created_at": "2010-01-28T22:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70727",
    "user": "https://github.com/robert-marik"
}
```

Works for me and fixes the problem in Sage 4.3.1. Tests passed. Thanks for the patch.



---

archive/issue_events_019352.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-30T23:47:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8084#event-19352"
}
```



---

archive/issue_comments_070728.json:
```json
{
    "body": "Merged [trac_8084-show.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8084/trac_8084-show.patch).",
    "created_at": "2010-01-30T23:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8084-show.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8084/trac_8084-show.patch).



---

archive/issue_comments_070729.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8084#issuecomment-70729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
