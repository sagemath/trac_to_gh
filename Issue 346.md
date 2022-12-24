# Issue 346: Notebook input cell focus

archive/issues_000346.json:
```json
{
    "body": "Assignee: boothby\n\nIn Firefox 1.5 (which is still what ships standard with, say Redhat), the following happens:\nIf I select text by dragging in a cell that currently does not have input focus, then the cell that did have focus loses it, but the cell in which I select the text does not gain focus.\n\nThe result is that the usual reflex for deleting the selection (press backspace) doesn't get sent to the cell but to the browser window, where it means the back button!\n\nIf I first put the cell in focus and then select the text, things work as expected, so there is a work-around. However, it does involve unlearning a reflex that works almost everywhere else. The penalty, getting sent to the previously visited page, is also a rather shocking experience.\n\nI understand that this behaviour might be out of the control of sage, but it would be nice if you could work around it.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/346\n\n",
    "created_at": "2007-04-03T21:04:31Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook input cell focus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/346",
    "user": "nbruin"
}
```
Assignee: boothby

In Firefox 1.5 (which is still what ships standard with, say Redhat), the following happens:
If I select text by dragging in a cell that currently does not have input focus, then the cell that did have focus loses it, but the cell in which I select the text does not gain focus.

The result is that the usual reflex for deleting the selection (press backspace) doesn't get sent to the cell but to the browser window, where it means the back button!

If I first put the cell in focus and then select the text, things work as expected, so there is a work-around. However, it does involve unlearning a reflex that works almost everywhere else. The penalty, getting sent to the previously visited page, is also a rather shocking experience.

I understand that this behaviour might be out of the control of sage, but it would be nice if you could work around it.




Issue created by migration from https://trac.sagemath.org/ticket/346





---

archive/issue_comments_001683.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2007-04-05T00:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/346#issuecomment-1683",
    "user": "nbruin"
}
```

Changing priority from minor to major.



---

archive/issue_comments_001684.json:
```json
{
    "body": "Upgraded to major. I'm running into this problem all the time and since other programs reinforce the behaviour, the habit does not go away. I think it's enough for me to abandon using the notebook.",
    "created_at": "2007-04-05T00:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/346#issuecomment-1684",
    "user": "nbruin"
}
```

Upgraded to major. I'm running into this problem all the time and since other programs reinforce the behaviour, the habit does not go away. I think it's enough for me to abandon using the notebook.



---

archive/issue_comments_001685.json:
```json
{
    "body": "This isn't a bug but a feature request.",
    "created_at": "2007-08-19T02:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/346#issuecomment-1685",
    "user": "was"
}
```

This isn't a bug but a feature request.



---

archive/issue_comments_001686.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-19T02:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/346#issuecomment-1686",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_001687.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-17T04:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/346#issuecomment-1687",
    "user": "boothby"
}
```

Resolution: invalid



---

archive/issue_comments_001688.json:
```json
{
    "body": "This hasn't been an issue since we removed syntax hilighting.",
    "created_at": "2008-03-17T04:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/346#issuecomment-1688",
    "user": "boothby"
}
```

This hasn't been an issue since we removed syntax hilighting.
