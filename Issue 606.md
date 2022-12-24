# Issue 606: add notebook support for loading of spyx and pyx files

archive/issues_000606.json:
```json
{
    "body": "Assignee: boothby\n\nFrom the notebook,\n\n\n```\n%sh\ncat > hello.pyx << EOF\ndef hello(name):\n    \"\"\"\n    Print hello with the given name.\n    \"\"\"\n    print(\"Hello %s\"%name)\nEOF\n```\n\n\n```\nload \"hello.pyx\"\nLoading of file\n\"/opt/sage-2.8.3.rc3/sage_notebook/worksheets/admin/0/cells/0/hello.pyx\"\nhas type not implemented.\n```\n\n\nThere is a function that currently just checks to see if the filename extension is .py or .sage before it tries to load the file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/606\n\n",
    "created_at": "2007-09-07T00:02:17Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "add notebook support for loading of spyx and pyx files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/606",
    "user": "@mwhansen"
}
```
Assignee: boothby

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

archive/issue_comments_003114.json:
```json
{
    "body": "Attachment [606.patch](tarball://root/attachments/some-uuid/ticket606/606.patch) by @mwhansen created at 2007-09-07 00:32:49",
    "created_at": "2007-09-07T00:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3114",
    "user": "@mwhansen"
}
```

Attachment [606.patch](tarball://root/attachments/some-uuid/ticket606/606.patch) by @mwhansen created at 2007-09-07 00:32:49



---

archive/issue_comments_003115.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2007-09-07T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3115",
    "user": "@mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_003116.json:
```json
{
    "body": "Patch added and tested.",
    "created_at": "2007-09-07T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3116",
    "user": "@mwhansen"
}
```

Patch added and tested.



---

archive/issue_comments_003117.json:
```json
{
    "body": "This patch is completely bogus.",
    "created_at": "2007-09-07T01:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3117",
    "user": "@williamstein"
}
```

This patch is completely bogus.



---

archive/issue_comments_003118.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2007-09-07T01:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3118",
    "user": "@williamstein"
}
```

Changing priority from minor to major.



---

archive/issue_comments_003119.json:
```json
{
    "body": "This is a good spyx file to test:\n\n\n```\nwas@ubuntu:~$ more a.spyx\ndef foo(int n):\n    return n*n\n```\n",
    "created_at": "2007-09-07T01:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3119",
    "user": "@williamstein"
}
```

This is a good spyx file to test:


```
was@ubuntu:~$ more a.spyx
def foo(int n):
    return n*n
```




---

archive/issue_comments_003120.json:
```json
{
    "body": "Attachment [606-2.patch](tarball://root/attachments/some-uuid/ticket606/606-2.patch) by @williamstein created at 2007-09-07 02:38:08\n\nchanged version that i like",
    "created_at": "2007-09-07T02:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3120",
    "user": "@williamstein"
}
```

Attachment [606-2.patch](tarball://root/attachments/some-uuid/ticket606/606-2.patch) by @williamstein created at 2007-09-07 02:38:08

changed version that i like



---

archive/issue_comments_003121.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T02:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3121",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_003122.json:
```json
{
    "body": "Attachment [6199.patch](tarball://root/attachments/some-uuid/ticket606/6199.patch) by @williamstein created at 2007-09-07 02:38:16",
    "created_at": "2007-09-07T02:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/606#issuecomment-3122",
    "user": "@williamstein"
}
```

Attachment [6199.patch](tarball://root/attachments/some-uuid/ticket606/6199.patch) by @williamstein created at 2007-09-07 02:38:16
