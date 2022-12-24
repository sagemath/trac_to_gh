# Issue 7207: from __future__ import <anything> results in a Syntax Error

archive/issues_007207.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777 @williamstein\n\n`from __future__ import *` statements must be the first statements in a file. However, the old Sage Notebook inserts synchronization code before the file, and the new SageNB inserts prompt changing code first. Both of the aforementioned changes break the code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7207\n\n",
    "created_at": "2009-10-14T11:42:07Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "from __future__ import <anything> results in a Syntax Error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7207",
    "user": "@TimDumol"
}
```
Assignee: boothby

CC:  @qed777 @williamstein

`from __future__ import *` statements must be the first statements in a file. However, the old Sage Notebook inserts synchronization code before the file, and the new SageNB inserts prompt changing code first. Both of the aforementioned changes break the code.

Issue created by migration from https://trac.sagemath.org/ticket/7207





---

archive/issue_comments_059799.json:
```json
{
    "body": "Fixed formatting to relocate future imports to the top of the file.",
    "created_at": "2009-10-16T11:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59799",
    "user": "@TimDumol"
}
```

Fixed formatting to relocate future imports to the top of the file.



---

archive/issue_comments_059800.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-16T11:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59800",
    "user": "@TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059801.json:
```json
{
    "body": "Attachment [trac_7207-sagenb-future-import.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.patch) by @TimDumol created at 2009-10-16 11:03:17",
    "created_at": "2009-10-16T11:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59801",
    "user": "@TimDumol"
}
```

Attachment [trac_7207-sagenb-future-import.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.patch) by @TimDumol created at 2009-10-16 11:03:17



---

archive/issue_comments_059802.json:
```json
{
    "body": "Would anyone mind reviewing this? It just moves the `displayhook_hack` to another file, and adds some tests and a tad of refactoring.",
    "created_at": "2009-12-05T09:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59802",
    "user": "@TimDumol"
}
```

Would anyone mind reviewing this? It just moves the `displayhook_hack` to another file, and adds some tests and a tad of refactoring.



---

archive/issue_comments_059803.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T20:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59803",
    "user": "@williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059804.json:
```json
{
    "body": "Needs work, since this has a subtle bug, which I bet you can easily fix.  See below.\n\nUsing regular expressions is unfortunately not rock solid.  For example, this input \"mysteriously\" gives a SyntaxError:\n\n```\nprint \"\"\"\nfrom __future__ import division\"\"\"\n```\n\noutputs:\n\n```\nSyntax Error:\n    from __future__ import division\"\"\"\n```\n\nwhereas the similar\n\n```\nprint \"\"\"\nfrom __xfuture__ import division\"\"\"\n```\n\nworks fine.  \n\nI think the right fix is to require that the even in the notebook the `from __future__ import ...` lines appear at the very top.  This would make it possible to use the same method you already used.",
    "created_at": "2009-12-08T20:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59804",
    "user": "@williamstein"
}
```

Needs work, since this has a subtle bug, which I bet you can easily fix.  See below.

Using regular expressions is unfortunately not rock solid.  For example, this input "mysteriously" gives a SyntaxError:

```
print """
from __future__ import division"""
```

outputs:

```
Syntax Error:
    from __future__ import division"""
```

whereas the similar

```
print """
from __xfuture__ import division"""
```

works fine.  

I think the right fix is to require that the even in the notebook the `from __future__ import ...` lines appear at the very top.  This would make it possible to use the same method you already used.



---

archive/issue_comments_059805.json:
```json
{
    "body": "Uses stdlib's `ast` to parse the file instead of regexp's.",
    "created_at": "2009-12-10T16:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59805",
    "user": "@TimDumol"
}
```

Uses stdlib's `ast` to parse the file instead of regexp's.



---

archive/issue_comments_059806.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-10T16:14:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59806",
    "user": "@TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059807.json:
```json
{
    "body": "Attachment [trac_7207-sagenb-future-import.2.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.2.patch) by @TimDumol created at 2009-12-10 16:14:30\n\nThis version of the patch uses `ast` (from stdlib). It should prevent errors such as what you described.",
    "created_at": "2009-12-10T16:14:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59807",
    "user": "@TimDumol"
}
```

Attachment [trac_7207-sagenb-future-import.2.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.2.patch) by @TimDumol created at 2009-12-10 16:14:30

This version of the patch uses `ast` (from stdlib). It should prevent errors such as what you described.



---

archive/issue_comments_059808.json:
```json
{
    "body": "Attachment [trac_7207-sagenb-future-import.2.2.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.2.2.patch) by @TimDumol created at 2009-12-16 12:37:59\n\nRebased on #7650 and its dependencies.",
    "created_at": "2009-12-16T12:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59808",
    "user": "@TimDumol"
}
```

Attachment [trac_7207-sagenb-future-import.2.2.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.2.2.patch) by @TimDumol created at 2009-12-16 12:37:59

Rebased on #7650 and its dependencies.



---

archive/issue_comments_059809.json:
```json
{
    "body": "Attachment [trac_7207-sagenb-future-import.2.3.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.2.3.patch) by @TimDumol created at 2009-12-16 13:01:11\n\nMissed an import on the rebase.",
    "created_at": "2009-12-16T13:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59809",
    "user": "@TimDumol"
}
```

Attachment [trac_7207-sagenb-future-import.2.3.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.2.3.patch) by @TimDumol created at 2009-12-16 13:01:11

Missed an import on the rebase.



---

archive/issue_comments_059810.json:
```json
{
    "body": "Attachment [trac_7207-sagenb-future-import.3.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.3.patch) by acleone created at 2010-01-20 07:17:58\n\nRebased to ~0.60",
    "created_at": "2010-01-20T07:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59810",
    "user": "acleone"
}
```

Attachment [trac_7207-sagenb-future-import.3.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.3.patch) by acleone created at 2010-01-20 07:17:58

Rebased to ~0.60



---

archive/issue_comments_059811.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T07:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59811",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059812.json:
```json
{
    "body": "Rebased to a bit after 0.60 (see trac_7207-sagenb-future-import.3.patch). Other than that LGTM.",
    "created_at": "2010-01-20T07:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59812",
    "user": "acleone"
}
```

Rebased to a bit after 0.60 (see trac_7207-sagenb-future-import.3.patch). Other than that LGTM.



---

archive/issue_comments_059813.json:
```json
{
    "body": "V4 is rebased for this queue:\n\n```\nsagenb-0.6\ntrac_7249-jinja2_v9.5.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_7969-escaped-backslash.patch\ntrac_4217-html-system-formatting.3.patch\ntrac_3083-print-documentation.5.patch\ntrac_6182-double-quotes-ws.2.patch\ntrac_5263-publish-url.patch\ntrac_7631-republish-name.patch\ntrac_6353-cookies-diff-ports.patch\ntrac_7207-sagenb-future-import.3.patch\n```\n",
    "created_at": "2010-01-25T00:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59813",
    "user": "@qed777"
}
```

V4 is rebased for this queue:

```
sagenb-0.6
trac_7249-jinja2_v9.5.patch
trac_7962-link-worksheets-zip-file.patch
trac_7969-escaped-backslash.patch
trac_4217-html-system-formatting.3.patch
trac_3083-print-documentation.5.patch
trac_6182-double-quotes-ws.2.patch
trac_5263-publish-url.patch
trac_7631-republish-name.patch
trac_6353-cookies-diff-ports.patch
trac_7207-sagenb-future-import.3.patch
```




---

archive/issue_comments_059814.json:
```json
{
    "body": "Rebased for SageNB 0.6 + queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T00:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59814",
    "user": "@qed777"
}
```

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.



---

archive/issue_comments_059815.json:
```json
{
    "body": "Attachment [trac_7207-sagenb-future-import.4.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.4.patch) by @qed777 created at 2010-01-25 00:52:54",
    "created_at": "2010-01-25T00:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59815",
    "user": "@qed777"
}
```

Attachment [trac_7207-sagenb-future-import.4.patch](tarball://root/attachments/some-uuid/ticket7207/trac_7207-sagenb-future-import.4.patch) by @qed777 created at 2010-01-25 00:52:54



---

archive/issue_comments_059816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7207#issuecomment-59816",
    "user": "@qed777"
}
```

Resolution: fixed
