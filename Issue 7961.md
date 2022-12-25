# Issue 7961: Make recognition of runpath/develpath in editmodule more robust

archive/issues_007961.json:
```json
{
    "body": "Assignee: @nbruin\n\nCurrently, the code that recognizes a source file is part of the sage library and hence is run from a different location than where the edit copy lives, is broken due to the python2.5 -> python2.6 upgrade. Attached fixes this problem and makes matching more robust so that it won't break the next time. To illustrate the problem, currently we have\n\n```\nsage: sage.misc.edit_module.file_and_line(edit)\n('/usr/local/sage/4.3/local/lib/python2.6/site-packages/sage/misc/edit_module.py', 194)\n```\n\nwhich obviously is NOT the file to edit. It should be `.../sage/devel/...` instead. Attached patch fixes this.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7961\n\n",
    "created_at": "2010-01-17T02:41:47Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Make recognition of runpath/develpath in editmodule more robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7961",
    "user": "https://github.com/nbruin"
}
```
Assignee: @nbruin

Currently, the code that recognizes a source file is part of the sage library and hence is run from a different location than where the edit copy lives, is broken due to the python2.5 -> python2.6 upgrade. Attached fixes this problem and makes matching more robust so that it won't break the next time. To illustrate the problem, currently we have

```
sage: sage.misc.edit_module.file_and_line(edit)
('/usr/local/sage/4.3/local/lib/python2.6/site-packages/sage/misc/edit_module.py', 194)
```

which obviously is NOT the file to edit. It should be `.../sage/devel/...` instead. Attached patch fixes this.


Issue created by migration from https://trac.sagemath.org/ticket/7961





---

archive/issue_comments_069350.json:
```json
{
    "body": "Attachment [edit_module.patch](tarball://root/attachments/some-uuid/ticket7961/edit_module.patch) by @nbruin created at 2010-01-17 02:46:14\n\nmaking misc.edit_module pathname mangling more robust",
    "created_at": "2010-01-17T02:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7961#issuecomment-69350",
    "user": "https://github.com/nbruin"
}
```

Attachment [edit_module.patch](tarball://root/attachments/some-uuid/ticket7961/edit_module.patch) by @nbruin created at 2010-01-17 02:46:14

making misc.edit_module pathname mangling more robust



---

archive/issue_comments_069351.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T02:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7961#issuecomment-69351",
    "user": "https://github.com/nbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069352.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-17T10:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7961#issuecomment-69352",
    "user": "https://github.com/TimDumol"
}
```

LGTM.



---

archive/issue_comments_069353.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T10:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7961#issuecomment-69353",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069354.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7961#issuecomment-69354",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
