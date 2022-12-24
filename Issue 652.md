# Issue 652: .sage files destroy existing .py files

archive/issues_000652.json:
```json
{
    "body": "Assignee: was\n\nIf files a.sage and a.py exist in a directory, then \n\nsage: load a.sage\n\ndestroys the file a.py and replaces it with an automatically generated file.  Either users should be warned of this \"feature\" or something else should be done.\n\nIssue created by migration from https://trac.sagemath.org/ticket/652\n\n",
    "created_at": "2007-09-14T04:24:51Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": ".sage files destroy existing .py files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/652",
    "user": "jvoight"
}
```
Assignee: was

If files a.sage and a.py exist in a directory, then 

sage: load a.sage

destroys the file a.py and replaces it with an automatically generated file.  Either users should be warned of this "feature" or something else should be done.

Issue created by migration from https://trac.sagemath.org/ticket/652





---

archive/issue_comments_003390.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2007-12-26T02:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3390",
    "user": "mabshoff"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_003391.json:
```json
{
    "body": "Is there any reason to put the .py files in the same directory? It would probably be less confusing to just put them in temp. If one wants to see them, one can use sage -preparse. \n\nI'm having trouble finding where exactly these files are getting written/used.",
    "created_at": "2008-01-04T21:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3391",
    "user": "robertwb"
}
```

Is there any reason to put the .py files in the same directory? It would probably be less confusing to just put them in temp. If one wants to see them, one can use sage -preparse. 

I'm having trouble finding where exactly these files are getting written/used.



---

archive/issue_comments_003392.json:
```json
{
    "body": "Patch preparses .sage files to temporary .py files in a temp directory.",
    "created_at": "2008-01-19T21:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3392",
    "user": "ncalexan"
}
```

Patch preparses .sage files to temporary .py files in a temp directory.



---

archive/issue_comments_003393.json:
```json
{
    "body": "Attachment [ncalexan-652.patch](tarball://root/attachments/some-uuid/ticket652/ncalexan-652.patch) by ncalexan created at 2008-01-23 02:23:51\n\nDO NOT APPLY, THIS HAS TROUBLE WITH DIRECTORIES",
    "created_at": "2008-01-23T02:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3393",
    "user": "ncalexan"
}
```

Attachment [ncalexan-652.patch](tarball://root/attachments/some-uuid/ticket652/ncalexan-652.patch) by ncalexan created at 2008-01-23 02:23:51

DO NOT APPLY, THIS HAS TROUBLE WITH DIRECTORIES



---

archive/issue_comments_003394.json:
```json
{
    "body": "Attachment [ncalexan-652-updated.patch](tarball://root/attachments/some-uuid/ticket652/ncalexan-652-updated.patch) by ncalexan created at 2008-01-23 02:53:16",
    "created_at": "2008-01-23T02:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3394",
    "user": "ncalexan"
}
```

Attachment [ncalexan-652-updated.patch](tarball://root/attachments/some-uuid/ticket652/ncalexan-652-updated.patch) by ncalexan created at 2008-01-23 02:53:16



---

archive/issue_comments_003395.json:
```json
{
    "body": "Updated patch should work -- the issue was that 'load /abs/dir/tofile.sage' was borked.  Hopefully this works better.",
    "created_at": "2008-01-23T02:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3395",
    "user": "ncalexan"
}
```

Updated patch should work -- the issue was that 'load /abs/dir/tofile.sage' was borked.  Hopefully this works better.



---

archive/issue_comments_003396.json:
```json
{
    "body": "I reproduced the problem with the previous code, and the patch does fix the problem; and the code looks good.",
    "created_at": "2008-01-27T01:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3396",
    "user": "cwitty"
}
```

I reproduced the problem with the previous code, and the patch does fix the problem; and the code looks good.



---

archive/issue_comments_003397.json:
```json
{
    "body": "Merged ncalexan-652-updated.patch in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T01:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3397",
    "user": "mabshoff"
}
```

Merged ncalexan-652-updated.patch in Sage 2.10.1.rc1



---

archive/issue_comments_003398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T01:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/652#issuecomment-3398",
    "user": "mabshoff"
}
```

Resolution: fixed
