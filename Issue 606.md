# Issue 606: add notebook support for loading of spyx and pyx files

archive/issues_000606.json:
```json
{
    "body": "Assignee: @mwhansen\n\nFrom the notebook,\n\n```\n%sh\ncat > hello.pyx << EOF\ndef hello(name):\n    \"\"\"\n    Print hello with the given name.\n    \"\"\"\n    print(\"Hello %s\"%name)\nEOF\n```\n\n```\nload \"hello.pyx\"\nLoading of file\n\"/opt/sage-2.8.3.rc3/sage_notebook/worksheets/admin/0/cells/0/hello.pyx\"\nhas type not implemented.\n```\n\nThere is a function that currently just checks to see if the filename extension is .py or .sage before it tries to load the file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/606\n\n",
    "closed_at": "2007-09-07T02:38:16Z",
    "created_at": "2007-09-07T00:02:17Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "add notebook support for loading of spyx and pyx files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/606",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

From the notebook,

```
%sh
cat > hello.pyx << EOF
def hello(name):
    """
    Print hello with the given name.
    """
    print("Hello %s"%name)
EOF
```

```
load "hello.pyx"
Loading of file
"/opt/sage-2.8.3.rc3/sage_notebook/worksheets/admin/0/cells/0/hello.pyx"
has type not implemented.
```

There is a function that currently just checks to see if the filename extension is .py or .sage before it tries to load the file.

Issue created by migration from https://trac.sagemath.org/ticket/606





---

archive/issue_comments_003102.json:
```json
{
    "body": "Attachment [606.patch](tarball://root/attachments/some-uuid/ticket606/606.patch) by @mwhansen created at 2007-09-07 00:32:49",
    "created_at": "2007-09-07T00:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3102",
    "user": "https://github.com/mwhansen"
}
```

Attachment [606.patch](tarball://root/attachments/some-uuid/ticket606/606.patch) by @mwhansen created at 2007-09-07 00:32:49



---

archive/issue_comments_003103.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2007-09-07T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3103",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_003104.json:
```json
{
    "body": "Patch added and tested.",
    "created_at": "2007-09-07T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3104",
    "user": "https://github.com/mwhansen"
}
```

Patch added and tested.



---

archive/issue_comments_003105.json:
```json
{
    "body": "This patch is completely bogus.",
    "created_at": "2007-09-07T01:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3105",
    "user": "https://github.com/williamstein"
}
```

This patch is completely bogus.



---

archive/issue_comments_003106.json:
```json
{
    "body": "This is a good spyx file to test:\n\n```\nwas@ubuntu:~$ more a.spyx\ndef foo(int n):\n    return n*n\n```",
    "created_at": "2007-09-07T01:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3106",
    "user": "https://github.com/williamstein"
}
```

This is a good spyx file to test:

```
was@ubuntu:~$ more a.spyx
def foo(int n):
    return n*n
```



---

archive/issue_comments_003107.json:
```json
{
    "body": "Attachment [606-2.patch](tarball://root/attachments/some-uuid/ticket606/606-2.patch) by @williamstein created at 2007-09-07 02:38:08\n\nchanged version that i like",
    "created_at": "2007-09-07T02:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3107",
    "user": "https://github.com/williamstein"
}
```

Attachment [606-2.patch](tarball://root/attachments/some-uuid/ticket606/606-2.patch) by @williamstein created at 2007-09-07 02:38:08

changed version that i like



---

archive/issue_comments_003108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T02:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3108",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_003109.json:
```json
{
    "body": "Attachment [6199.patch](tarball://root/attachments/some-uuid/ticket606/6199.patch) by @williamstein created at 2007-09-07 02:38:16",
    "created_at": "2007-09-07T02:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3109",
    "user": "https://github.com/williamstein"
}
```

Attachment [6199.patch](tarball://root/attachments/some-uuid/ticket606/6199.patch) by @williamstein created at 2007-09-07 02:38:16



---

archive/issue_events_001613.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T02:38:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/606#event-1613"
}
```



---

archive/issue_events_001614.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T02:38:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/606#event-1614"
}
```
