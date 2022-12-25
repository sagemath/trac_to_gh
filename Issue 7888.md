# Issue 7888: Do not pass comment lines to Macaulay2

archive/issues_007888.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently passing \"pure comments\" to Macaulay2 locks the interface since Macaulay2 does not print a new input prompts. Evaluating whitespace lines locks it as well and while there is some stripping code in Expect, it does not work if whitespace lines appear in the middle of a block.\n\nThe attached patch replaces all such lines with empty ones before passing to Macaulay2. This may break string constants occupying several lines, however, as far as I understand, they have no chance of working without substantial modification of Expect.eval, which currently executes code line by line. (In particular, they hang up now.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7888\n\n",
    "created_at": "2010-01-10T01:53:39Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Do not pass comment lines to Macaulay2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7888",
    "user": "https://github.com/novoselt"
}
```
Assignee: @williamstein

Currently passing "pure comments" to Macaulay2 locks the interface since Macaulay2 does not print a new input prompts. Evaluating whitespace lines locks it as well and while there is some stripping code in Expect, it does not work if whitespace lines appear in the middle of a block.

The attached patch replaces all such lines with empty ones before passing to Macaulay2. This may break string constants occupying several lines, however, as far as I understand, they have no chance of working without substantial modification of Expect.eval, which currently executes code line by line. (In particular, they hang up now.)

Issue created by migration from https://trac.sagemath.org/ticket/7888





---

archive/issue_comments_068468.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-10T01:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7888#issuecomment-68468",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068469.json:
```json
{
    "body": "Attachment [do_not_pass_comment_lines_to_Macaulay2.patch](tarball://root/attachments/some-uuid/ticket7888/do_not_pass_comment_lines_to_Macaulay2.patch) by @novoselt created at 2010-01-10 01:54:38",
    "created_at": "2010-01-10T01:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7888#issuecomment-68469",
    "user": "https://github.com/novoselt"
}
```

Attachment [do_not_pass_comment_lines_to_Macaulay2.patch](tarball://root/attachments/some-uuid/ticket7888/do_not_pass_comment_lines_to_Macaulay2.patch) by @novoselt created at 2010-01-10 01:54:38



---

archive/issue_comments_068470.json:
```json
{
    "body": "Ticket #7897 fixes this in a better way.",
    "created_at": "2010-01-11T20:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7888#issuecomment-68470",
    "user": "https://github.com/novoselt"
}
```

Ticket #7897 fixes this in a better way.



---

archive/issue_comments_068471.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-11T20:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7888#issuecomment-68471",
    "user": "https://github.com/novoselt"
}
```

Resolution: duplicate



---

archive/issue_events_008103.json:
```json
{
    "actor": "https://github.com/novoselt",
    "created_at": "2010-01-11T20:59:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7888",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7888#event-8103"
}
```
