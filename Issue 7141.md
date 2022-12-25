# Issue 7141: `math_parse` parses $'s in <script> tags

archive/issues_007141.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: sagenb notebook jQuery\n\n`sagenb.notebook.jsmath.math_parse` (and the source, `sage.misc.html.math_parse`) parse $'s in <script> tags, which breaks jQuery code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7141\n\n",
    "created_at": "2009-10-06T15:02:03Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "`math_parse` parses $'s in <script> tags",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7141",
    "user": "https://github.com/TimDumol"
}
```
Assignee: boothby

Keywords: sagenb notebook jQuery

`sagenb.notebook.jsmath.math_parse` (and the source, `sage.misc.html.math_parse`) parse $'s in <script> tags, which breaks jQuery code.

Issue created by migration from https://trac.sagemath.org/ticket/7141





---

archive/issue_comments_059068.json:
```json
{
    "body": "Attachment [trac_7141-sagenb-math_parse.patch](tarball://root/attachments/some-uuid/ticket7141/trac_7141-sagenb-math_parse.patch) by @TimDumol created at 2009-10-06 15:37:55\n\nFixes math_parse in sagenb.notebook.jsmath to skip <script> tags. Apply to sagenb repo.",
    "created_at": "2009-10-06T15:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7141#issuecomment-59068",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7141-sagenb-math_parse.patch](tarball://root/attachments/some-uuid/ticket7141/trac_7141-sagenb-math_parse.patch) by @TimDumol created at 2009-10-06 15:37:55

Fixes math_parse in sagenb.notebook.jsmath to skip <script> tags. Apply to sagenb repo.



---

archive/issue_comments_059069.json:
```json
{
    "body": "Very nice!\n\nAnd I've applied it and pushed it to the official sagenb branch.",
    "created_at": "2009-10-07T04:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7141#issuecomment-59069",
    "user": "https://github.com/williamstein"
}
```

Very nice!

And I've applied it and pushed it to the official sagenb branch.



---

archive/issue_comments_059070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-07T04:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7141#issuecomment-59070",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_007361.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-10-07T04:48:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7141#event-7361"
}
```
