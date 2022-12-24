# Issue 2459: Fix GSL_DISABLE_DEPRECAED macro in setup.py

archive/issues_002459.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrancois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that:\n\n```\nIn sage-2.10.3.rc3 in the top setup.py at line 430 we have:\ndefine_macros = [('GSL_DISABLE_DEPRECAED','1')]\nFor those who can't spot it, it miss a 'T'. \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2459\n\n",
    "created_at": "2008-03-10T14:58:39Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Fix GSL_DISABLE_DEPRECAED macro in setup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2459",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Francois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that:

```
In sage-2.10.3.rc3 in the top setup.py at line 430 we have:
define_macros = [('GSL_DISABLE_DEPRECAED','1')]
For those who can't spot it, it miss a 'T'. 
```



Issue created by migration from https://trac.sagemath.org/ticket/2459





---

archive/issue_comments_016650.json:
```json
{
    "body": "Changing component from Cygwin to build.",
    "created_at": "2008-03-10T14:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16650",
    "user": "mabshoff"
}
```

Changing component from Cygwin to build.



---

archive/issue_comments_016651.json:
```json
{
    "body": "Attachment [2459.hg](tarball://root/attachments/some-uuid/ticket2459/2459.hg) by @dfdeshom created at 2008-03-14 05:42:31",
    "created_at": "2008-03-14T05:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16651",
    "user": "@dfdeshom"
}
```

Attachment [2459.hg](tarball://root/attachments/some-uuid/ticket2459/2459.hg) by @dfdeshom created at 2008-03-14 05:42:31



---

archive/issue_comments_016652.json:
```json
{
    "body": "I've attached a patch that fixes this typo. `real_double_vector` (the module to be built in line 430) built fine and passed all doctests.",
    "created_at": "2008-03-14T05:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16652",
    "user": "@dfdeshom"
}
```

I've attached a patch that fixes this typo. `real_double_vector` (the module to be built in line 430) built fine and passed all doctests.



---

archive/issue_comments_016653.json:
```json
{
    "body": "Patch looks good to me and does the right thing.",
    "created_at": "2008-03-15T07:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16653",
    "user": "mabshoff"
}
```

Patch looks good to me and does the right thing.



---

archive/issue_comments_016654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T08:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16654",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016655.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-15T08:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16655",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
