# Issue 958: bug in "make install"

archive/issues_000958.json:
```json
{
    "body": "Assignee: @williamstein\n\nReported by Paul Zimmerman:\n\n```\n\n- in case one redefines DESTDIR in make install, one gets strange paths:\n $ make install -n DESTDIR=/usr/local/sage-2.8.7\n ...\n cp /usr/local/sage-2.8.7/usr/local/sage/sage /usr/local/sage-2.8.7/usr/bin/\n (I would expect at least 'usr' to disappear.)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/958\n\n",
    "created_at": "2007-10-21T12:40:04Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "bug in \"make install\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/958",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Reported by Paul Zimmerman:

```

- in case one redefines DESTDIR in make install, one gets strange paths:
 $ make install -n DESTDIR=/usr/local/sage-2.8.7
 ...
 cp /usr/local/sage-2.8.7/usr/local/sage/sage /usr/local/sage-2.8.7/usr/bin/
 (I would expect at least 'usr' to disappear.)
```


Issue created by migration from https://trac.sagemath.org/ticket/958





---

archive/issue_comments_005840.json:
```json
{
    "body": "Attachment [958.patch](tarball://root/attachments/some-uuid/ticket958/958.patch) by cwitty created at 2007-10-27 18:43:39\n\n2.8.10 will have the above patch.  Then, \n\nmake install DESTDIR=/usr/local/sage-2.8.7\n\nwill copy the entire sage directory to $(DESTDIR)/sage, and put a copy of the sage startup script in $(DESTDIR)/bin .",
    "created_at": "2007-10-27T18:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/958#issuecomment-5840",
    "user": "cwitty"
}
```

Attachment [958.patch](tarball://root/attachments/some-uuid/ticket958/958.patch) by cwitty created at 2007-10-27 18:43:39

2.8.10 will have the above patch.  Then, 

make install DESTDIR=/usr/local/sage-2.8.7

will copy the entire sage directory to $(DESTDIR)/sage, and put a copy of the sage startup script in $(DESTDIR)/bin .



---

archive/issue_comments_005841.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T18:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/958#issuecomment-5841",
    "user": "cwitty"
}
```

Resolution: fixed
