# Issue 7848: Fix misleading stuff about HTML cells on sagenb

archive/issues_007848.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @TimDumol\n\nFrom sage-support:\n\n```\nThe directive given in the help doesn't work: \nShift click between cells to create a new HTML cell. Double click on \nexisting HTML to edit it. \nUse $...$ and $$...$$ to include typeset math in the HTML block. \n```\n\nThere is no mention of the horizontal blue line.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7848\n\n",
    "created_at": "2010-01-05T04:12:35Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Fix misleading stuff about HTML cells on sagenb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7848",
    "user": "@kcrisman"
}
```
Assignee: @williamstein

CC:  @TimDumol

From sage-support:

```
The directive given in the help doesn't work: 
Shift click between cells to create a new HTML cell. Double click on 
existing HTML to edit it. 
Use $...$ and $$...$$ to include typeset math in the HTML block. 
```

There is no mention of the horizontal blue line.

Issue created by migration from https://trac.sagemath.org/ticket/7848





---

archive/issue_comments_067978.json:
```json
{
    "body": "Should we move the contents of `tutorial.py` to an HTML file?",
    "created_at": "2010-01-05T05:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67978",
    "user": "@qed777"
}
```

Should we move the contents of `tutorial.py` to an HTML file?



---

archive/issue_comments_067979.json:
```json
{
    "body": "I believe that some of it can be put into the documentation, under \"The Notebook Interface\", which is a bit lacking.",
    "created_at": "2010-01-05T12:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67979",
    "user": "@TimDumol"
}
```

I believe that some of it can be put into the documentation, under "The Notebook Interface", which is a bit lacking.



---

archive/issue_comments_067980.json:
```json
{
    "body": "Attachment [trac_7848-misleading_HTML_cells.patch](tarball://root/attachments/some-uuid/ticket7848/trac_7848-misleading_HTML_cells.patch) by acleone created at 2010-01-19 07:21:56\n\nChanges the tutorial help verbage regarding text (HTML) cells.  Also replaces all the <b> tags in the tutorial with <strong>",
    "created_at": "2010-01-19T07:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67980",
    "user": "acleone"
}
```

Attachment [trac_7848-misleading_HTML_cells.patch](tarball://root/attachments/some-uuid/ticket7848/trac_7848-misleading_HTML_cells.patch) by acleone created at 2010-01-19 07:21:56

Changes the tutorial help verbage regarding text (HTML) cells.  Also replaces all the <b> tags in the tutorial with <strong>



---

archive/issue_comments_067981.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T07:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67981",
    "user": "acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067982.json:
```json
{
    "body": "trac_7848-misleading_HTML_cells.patch: changes verbage to:\n\n```\nInsert New Text Cell\n\nMove the mouse between cells until a blue bar appears.\n<strong>Shift-click</strong> on the blue bar to create a new text cell.\nDouble click on existing text to edit it.\nUse $...$ and $$...$$ to include typeset math in the text block.\n```\n",
    "created_at": "2010-01-19T07:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67982",
    "user": "acleone"
}
```

trac_7848-misleading_HTML_cells.patch: changes verbage to:

```
Insert New Text Cell

Move the mouse between cells until a blue bar appears.
<strong>Shift-click</strong> on the blue bar to create a new text cell.
Double click on existing text to edit it.
Use $...$ and $$...$$ to include typeset math in the text block.
```




---

archive/issue_comments_067983.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T08:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67983",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067984.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-19T08:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67984",
    "user": "@TimDumol"
}
```

LGTM.



---

archive/issue_comments_067985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7848#issuecomment-67985",
    "user": "@qed777"
}
```

Resolution: fixed
