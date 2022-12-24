# Issue 2605: Notebook tab-backspace-(shift enter) gives bug

archive/issues_002605.json:
```json
{
    "body": "Assignee: boothby\n\nIn an empty cell, type\n  tab, backspace, and shift-enter\nand it gives a strange bug: Missing output for cell ...  \n\nReported by Andrew Guertin, an undergraduate in my Math 252 class.\n\nJV\n\nIssue created by migration from https://trac.sagemath.org/ticket/2605\n\n",
    "created_at": "2008-03-19T20:39:28Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Notebook tab-backspace-(shift enter) gives bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2605",
    "user": "@jvoight"
}
```
Assignee: boothby

In an empty cell, type
  tab, backspace, and shift-enter
and it gives a strange bug: Missing output for cell ...  

Reported by Andrew Guertin, an undergraduate in my Math 252 class.

JV

Issue created by migration from https://trac.sagemath.org/ticket/2605





---

archive/issue_comments_017811.json:
```json
{
    "body": "I cannot replicate this.  If I do the above the cell is deleted and loses focus, which is exactly the desired behavior. \n\nSO -- took keep this from being marked invalid, please list the exact operating system, browser, sage version, etc., and that *you* can replicate the problem (not just your student).",
    "created_at": "2008-03-19T20:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2605#issuecomment-17811",
    "user": "@williamstein"
}
```

I cannot replicate this.  If I do the above the cell is deleted and loses focus, which is exactly the desired behavior. 

SO -- took keep this from being marked invalid, please list the exact operating system, browser, sage version, etc., and that *you* can replicate the problem (not just your student).



---

archive/issue_comments_017812.json:
```json
{
    "body": "I also replicated the bug.  I'm running Sage version 2.10.3 (on a separate Linux machine); the notebook is running under Windows XP with Firefox version:\n\nMozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11\n\nJV",
    "created_at": "2008-03-19T20:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2605#issuecomment-17812",
    "user": "@jvoight"
}
```

I also replicated the bug.  I'm running Sage version 2.10.3 (on a separate Linux machine); the notebook is running under Windows XP with Firefox version:

Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11

JV



---

archive/issue_comments_017813.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-10T21:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2605#issuecomment-17813",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_017814.json:
```json
{
    "body": "I cannot replicate this on any system.  I believe it is no longer a bug.",
    "created_at": "2008-05-10T21:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2605#issuecomment-17814",
    "user": "@williamstein"
}
```

I cannot replicate this on any system.  I believe it is no longer a bug.
