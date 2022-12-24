# Issue 3561: make it so sage does *not* import numpy by default on startup.

archive/issues_003561.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3561\n\n",
    "created_at": "2008-07-06T08:46:08Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "make it so sage does *not* import numpy by default on startup.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3561",
    "user": "was"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/3561





---

archive/issue_comments_025168.json:
```json
{
    "body": "The attached patch gets rid of a bunch of numpy imports.  However, according to \n\n```\n  sage -timeup\n```\n\n(see #3559) there is still some mysterious numpy import that gets triggered in real_double_vector.pyx.  I'm very confused by that since there is no python \"import numpy\" anywhere there.  Fixing that can be another ticket for later.",
    "created_at": "2008-07-06T09:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3561#issuecomment-25168",
    "user": "was"
}
```

The attached patch gets rid of a bunch of numpy imports.  However, according to 

```
  sage -timeup
```

(see #3559) there is still some mysterious numpy import that gets triggered in real_double_vector.pyx.  I'm very confused by that since there is no python "import numpy" anywhere there.  Fixing that can be another ticket for later.



---

archive/issue_comments_025169.json:
```json
{
    "body": "Attachment [sage-3561.patch](tarball://root/attachments/some-uuid/ticket3561/sage-3561.patch) by mabshoff created at 2008-07-06 09:25:53\n\nPatch looks good to me. Positive review.",
    "created_at": "2008-07-06T09:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3561#issuecomment-25169",
    "user": "mabshoff"
}
```

Attachment [sage-3561.patch](tarball://root/attachments/some-uuid/ticket3561/sage-3561.patch) by mabshoff created at 2008-07-06 09:25:53

Patch looks good to me. Positive review.



---

archive/issue_comments_025170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T09:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3561#issuecomment-25170",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025171.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T09:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3561#issuecomment-25171",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
