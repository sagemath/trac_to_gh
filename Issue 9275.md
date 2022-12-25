# Issue 9275: 2 Bugs related to Simple Sage Server API

archive/issues_009275.json:
```json
{
    "body": "Assignee: jason, was\n\nThis is from a user:\n\n\n```\n\nHi.\n\nI was recently trying to use the Simple Sage Server API as described here:\nhttp://www.sagemath.org/doc/reference/sagenb/simple/twist.html\nI am using the opensuse-64bit build of Sage-4.4.\n\nWell it didn't work (always got an error when I tried to compute\nsomething), so I started to follow the error.\n\nOn my way I found to Bugs:\n\nFile sage.server.notebook.worksheet, Line 3497, in def preparse(self, s)\nreplace:   s = preparse_file(s, magic=False, do_time=True,\nignore_prompts=False)\nwith   :   s = preparse_file(s)\n(The arguments magic and do_time do not exist in preparse_file)\n\nFile sage.server.notebook.worksheet, Line 2871, in def\nstart_next_comp(self) before:    input +=\n'sage.server.notebook.interact.SAGE_CELL_ID=%s\\n'%(C.id())\ninsert:    input += 'import sage.server.notebook.interact\\n'\n(You need to import the module before using it)\n\nWhen I applied those two patches the tutorial worked out for me.\n\ngreetings,\nDavid Poetzsch-Heffter\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9275\n\n",
    "created_at": "2010-06-19T18:16:11Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "2 Bugs related to Simple Sage Server API",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9275",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

This is from a user:


```

Hi.

I was recently trying to use the Simple Sage Server API as described here:
http://www.sagemath.org/doc/reference/sagenb/simple/twist.html
I am using the opensuse-64bit build of Sage-4.4.

Well it didn't work (always got an error when I tried to compute
something), so I started to follow the error.

On my way I found to Bugs:

File sage.server.notebook.worksheet, Line 3497, in def preparse(self, s)
replace:   s = preparse_file(s, magic=False, do_time=True,
ignore_prompts=False)
with   :   s = preparse_file(s)
(The arguments magic and do_time do not exist in preparse_file)

File sage.server.notebook.worksheet, Line 2871, in def
start_next_comp(self) before:    input +=
'sage.server.notebook.interact.SAGE_CELL_ID=%s\n'%(C.id())
insert:    input += 'import sage.server.notebook.interact\n'
(You need to import the module before using it)

When I applied those two patches the tutorial worked out for me.

greetings,
David Poetzsch-Heffter
```


Issue created by migration from https://trac.sagemath.org/ticket/9275





---

archive/issue_comments_087229.json:
```json
{
    "body": "The bugfixes mentioned above as a patch file",
    "created_at": "2010-06-24T10:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9275#issuecomment-87229",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

The bugfixes mentioned above as a patch file



---

archive/issue_comments_087230.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-14T17:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9275#issuecomment-87230",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087231.json:
```json
{
    "body": "Attachment [14208.patch](tarball://root/attachments/some-uuid/ticket9275/14208.patch) by @kcrisman created at 2013-06-14 17:11:40\n\nThe simple server does not currently work at all; however, the [Sage cell server](https://github.com/sagemath/sagecell) should fit most of those needs.",
    "created_at": "2013-06-14T17:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9275#issuecomment-87231",
    "user": "https://github.com/kcrisman"
}
```

Attachment [14208.patch](tarball://root/attachments/some-uuid/ticket9275/14208.patch) by @kcrisman created at 2013-06-14 17:11:40

The simple server does not currently work at all; however, the [Sage cell server](https://github.com/sagemath/sagecell) should fit most of those needs.



---

archive/issue_comments_087232.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-14T17:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9275#issuecomment-87232",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087233.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2013-06-14T18:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9275#issuecomment-87233",
    "user": "https://github.com/kcrisman"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_087234.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2014-09-17T02:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9275#issuecomment-87234",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_087235.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-09-18T18:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9275#issuecomment-87235",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_009437.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-09-18T18:01:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9275",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9275#event-9437"
}
```
