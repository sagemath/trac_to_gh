# Issue 414: Attaching .pyx doesn't work anymore (only .spyx)

archive/issues_000414.json:
```json
{
    "body": "Assignee: @williamstein\n\nApparently, the list of allowed file formats to attach got shorter recently:\n\n\n```\n<type 'exceptions.ImportError'>: Attaching of '/home/malb/foobar.pyx'\nnot implemented (load .py, .spyx, and .sage files)\n```\n\n\nbut `attach 'foobar.spyx'` works.\n\nIssue created by migration from https://trac.sagemath.org/ticket/414\n\n",
    "created_at": "2007-08-09T13:36:35Z",
    "labels": [
        "component: user interface",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "Attaching .pyx doesn't work anymore (only .spyx)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/414",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Apparently, the list of allowed file formats to attach got shorter recently:


```
<type 'exceptions.ImportError'>: Attaching of '/home/malb/foobar.pyx'
not implemented (load .py, .spyx, and .sage files)
```


but `attach 'foobar.spyx'` works.

Issue created by migration from https://trac.sagemath.org/ticket/414





---

archive/issue_comments_002032.json:
```json
{
    "body": "I never remember allowing attaching of .pyx.  ????",
    "created_at": "2007-08-31T21:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/414#issuecomment-2032",
    "user": "https://github.com/williamstein"
}
```

I never remember allowing attaching of .pyx.  ????



---

archive/issue_comments_002033.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2007-09-14T02:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/414#issuecomment-2033",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_002034.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2007-09-14T09:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/414#issuecomment-2034",
    "user": "https://github.com/malb"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_002035.json:
```json
{
    "body": "Why is this wontfix? AFAIK there is no preparsing involved in the spyx anyway. Is reopening the right way of dealing with this question? Let's try.",
    "created_at": "2007-09-14T09:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/414#issuecomment-2035",
    "user": "https://github.com/malb"
}
```

Why is this wontfix? AFAIK there is no preparsing involved in the spyx anyway. Is reopening the right way of dealing with this question? Let's try.



---

archive/issue_comments_002036.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-14T09:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/414#issuecomment-2036",
    "user": "https://github.com/malb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-14T22:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/414#issuecomment-2037",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_002038.json:
```json
{
    "body": "Attachment [pyx.patch](tarball://root/attachments/some-uuid/ticket414/pyx.patch) by @williamstein created at 2007-09-14 22:07:40\n\nFixed for sage-2.8.4.3.  Now both .spyx and .pyx files are accepted.",
    "created_at": "2007-09-14T22:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/414#issuecomment-2038",
    "user": "https://github.com/williamstein"
}
```

Attachment [pyx.patch](tarball://root/attachments/some-uuid/ticket414/pyx.patch) by @williamstein created at 2007-09-14 22:07:40

Fixed for sage-2.8.4.3.  Now both .spyx and .pyx files are accepted.
