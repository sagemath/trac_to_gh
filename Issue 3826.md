# Issue 3826: Empty string in interact prints \x00

archive/issues_003826.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @saliola\n\nKeywords: interact empty string\n\nIn the notebook of sage 3.0.6: \n\nWrite\n\n\n```\n@interact\ndef f(a=input_box(default='aaa',type=str,label='Your name :')):\n    print a\n    print [1,2,3,a]\n```\n\n\nThen, delete 'aaa' from the box. Press enter and the list prints like this :\n\n\n```\n[1, 2, 3, '\\x00']\n```\n\n\nwhile should be :\n\n\n```\n[1, 2, 3, '']\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3826\n\n",
    "created_at": "2008-08-12T23:23:21Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Empty string in interact prints \\x00",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3826",
    "user": "@seblabbe"
}
```
Assignee: boothby

CC:  @saliola

Keywords: interact empty string

In the notebook of sage 3.0.6: 

Write


```
@interact
def f(a=input_box(default='aaa',type=str,label='Your name :')):
    print a
    print [1,2,3,a]
```


Then, delete 'aaa' from the box. Press enter and the list prints like this :


```
[1, 2, 3, '\x00']
```


while should be :


```
[1, 2, 3, '']
```



Issue created by migration from https://trac.sagemath.org/ticket/3826





---

archive/issue_comments_027216.json:
```json
{
    "body": "Changing assignee from boothby to @itolkov.",
    "created_at": "2008-08-13T00:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27216",
    "user": "mabshoff"
}
```

Changing assignee from boothby to @itolkov.



---

archive/issue_comments_027217.json:
```json
{
    "body": "Changing component from notebook to interact.",
    "created_at": "2008-08-13T00:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27217",
    "user": "mabshoff"
}
```

Changing component from notebook to interact.



---

archive/issue_comments_027218.json:
```json
{
    "body": "Reassigning the component to \"interact\" since I just created it.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T00:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27218",
    "user": "mabshoff"
}
```

Reassigning the component to "interact" since I just created it.

Cheers,

Michael



---

archive/issue_comments_027219.json:
```json
{
    "body": "Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3826/sage.patch) by @itolkov created at 2008-08-13 21:19:06\n\n\n```\njavascript: encode64(\"\")\n```\n\nAA==\n\n\n```\nsage.server.notebook.interact.standard_b64decode(\"AA==\")\n```\n\n'\\x00'\n\nMy patch adds a check in the interact() function. However, encode64() and decode64() seem to be buggy. In particular, they are not inverses. For example,\n\n```\njavascript: encode64(decode64(\"\"))\n```\n\nAAAA",
    "created_at": "2008-08-13T21:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27219",
    "user": "@itolkov"
}
```

Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3826/sage.patch) by @itolkov created at 2008-08-13 21:19:06


```
javascript: encode64("")
```

AA==


```
sage.server.notebook.interact.standard_b64decode("AA==")
```

'\x00'

My patch adds a check in the interact() function. However, encode64() and decode64() seem to be buggy. In particular, they are not inverses. For example,

```
javascript: encode64(decode64(""))
```

AAAA



---

archive/issue_comments_027220.json:
```json
{
    "body": "Attachment [trac3826-javascript-base64.patch](tarball://root/attachments/some-uuid/ticket3826/trac3826-javascript-base64.patch) by cwitty created at 2008-08-23 18:22:13",
    "created_at": "2008-08-23T18:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27220",
    "user": "cwitty"
}
```

Attachment [trac3826-javascript-base64.patch](tarball://root/attachments/some-uuid/ticket3826/trac3826-javascript-base64.patch) by cwitty created at 2008-08-23 18:22:13



---

archive/issue_comments_027221.json:
```json
{
    "body": "Rather than working around the bug, it seems better to just fix the bug.  My patch changes encode64 and decode64 to match the Python behavior (which I believe to be the correct behavior), where the empty string encodes/decodes to the empty string.",
    "created_at": "2008-08-23T18:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27221",
    "user": "cwitty"
}
```

Rather than working around the bug, it seems better to just fix the bug.  My patch changes encode64 and decode64 to match the Python behavior (which I believe to be the correct behavior), where the empty string encodes/decodes to the empty string.



---

archive/issue_comments_027222.json:
```json
{
    "body": "Seems to be working in the example above, as well as in my example.\n\n+1",
    "created_at": "2008-08-27T01:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27222",
    "user": "@itolkov"
}
```

Seems to be working in the example above, as well as in my example.

+1



---

archive/issue_comments_027223.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T01:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27223",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_027224.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T01:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27224",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027225.json:
```json
{
    "body": "PS: I merged *only* Carl's patch, i.e. trac3826-javascript-base64.patch",
    "created_at": "2008-08-27T01:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3826#issuecomment-27225",
    "user": "mabshoff"
}
```

PS: I merged *only* Carl's patch, i.e. trac3826-javascript-base64.patch
