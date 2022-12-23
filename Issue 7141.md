# Issue 7141: `math_parse` parses $'s in <script> tags

archive/issues_007141.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: sagenb notebook jQuery\n\n`sagenb.notebook.jsmath.math_parse` (and the source, `sage.misc.html.math_parse`) parse $'s in <script> tags, which breaks jQuery code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7141\n\n",
    "created_at": "2009-10-06T15:02:03Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "`math_parse` parses $'s in <script> tags",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7141",
    "user": "timdumol"
}
```
Assignee: boothby

Keywords: sagenb notebook jQuery

`sagenb.notebook.jsmath.math_parse` (and the source, `sage.misc.html.math_parse`) parse $'s in <script> tags, which breaks jQuery code.

Issue created by migration from https://trac.sagemath.org/ticket/7141





---

archive/issue_comments_059180.json:
```json
{
    "body": "Attachment\n\nFixes math_parse in sagenb.notebook.jsmath to skip <script> tags. Apply to sagenb repo.",
    "created_at": "2009-10-06T15:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7141#issuecomment-59180",
    "user": "timdumol"
}
```

Attachment

Fixes math_parse in sagenb.notebook.jsmath to skip <script> tags. Apply to sagenb repo.



---

archive/issue_comments_059181.json:
```json
{
    "body": "Very nice!\n\nAnd I've applied it and pushed it to the official sagenb branch.",
    "created_at": "2009-10-07T04:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7141#issuecomment-59181",
    "user": "was"
}
```

Very nice!

And I've applied it and pushed it to the official sagenb branch.



---

archive/issue_comments_059182.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-07T04:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7141#issuecomment-59182",
    "user": "was"
}
```

Resolution: fixed
