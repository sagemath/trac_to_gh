# Issue 7774: notebook: after performing "evaluate all" behauviour of  creating new cells changes.

archive/issues_007774.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage 4.3, 32-bit Athlon XP, OS: Debian \"lenny\", this issue appears in a local notebook as well as on www.sagenb.org using firefox 3.0.6 and epiphany\n\nWhen working in the notebook, usually after evaluating the last cell, the result is printed out and the cursor is placed in a newly created empty cell.\n\nThis behaviour changes if \"evaluate all\" is performed on the worksheet:\n\nCreate a new worksheet, type \"1+1\" into the first cell and evaluate it, then go to the menu \"action\" and perform \"evaluate all\", then go to the last empty cell again, type something like \"1+2\" and evaluate the cell (by pressing Shift-Return), the result is printed out, but instead of creating a new empty cell and placing the cursor there, no new cell will be created, the cursor is placed in the beginning of the last evaluated cell.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7774\n\n",
    "created_at": "2009-12-27T16:10:19Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook: after performing \"evaluate all\" behauviour of  creating new cells changes.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7774",
    "user": "ggrafendorfer"
}
```
Assignee: @williamstein

sage 4.3, 32-bit Athlon XP, OS: Debian "lenny", this issue appears in a local notebook as well as on www.sagenb.org using firefox 3.0.6 and epiphany

When working in the notebook, usually after evaluating the last cell, the result is printed out and the cursor is placed in a newly created empty cell.

This behaviour changes if "evaluate all" is performed on the worksheet:

Create a new worksheet, type "1+1" into the first cell and evaluate it, then go to the menu "action" and perform "evaluate all", then go to the last empty cell again, type something like "1+2" and evaluate the cell (by pressing Shift-Return), the result is printed out, but instead of creating a new empty cell and placing the cursor there, no new cell will be created, the cursor is placed in the beginning of the last evaluated cell.


Issue created by migration from https://trac.sagemath.org/ticket/7774





---

archive/issue_comments_067030.json:
```json
{
    "body": "I confirm this bug (K-meleon and WVista, server is 32-bit Debian lenny).\nHowever, when I \"save and quit\" the notebook a return back, the missing new cell is at the and.",
    "created_at": "2009-12-27T17:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-67030",
    "user": "@robert-marik"
}
```

I confirm this bug (K-meleon and WVista, server is 32-bit Debian lenny).
However, when I "save and quit" the notebook a return back, the missing new cell is at the and.



---

archive/issue_comments_067031.json:
```json
{
    "body": "This should be fixed by #7666 + #6855.",
    "created_at": "2010-01-02T00:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-67031",
    "user": "@qed777"
}
```

This should be fixed by #7666 + #6855.



---

archive/issue_comments_067032.json:
```json
{
    "body": "If someone sees this again, let's open a new ticket with more updated info; I cannot replicate this.",
    "created_at": "2014-12-10T20:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-67032",
    "user": "@kcrisman"
}
```

If someone sees this again, let's open a new ticket with more updated info; I cannot replicate this.



---

archive/issue_comments_067033.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-10T20:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-67033",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067034.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-10T20:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-67034",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067035.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2014-12-11T18:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-67035",
    "user": "@vbraun"
}
```

Resolution: worksforme
