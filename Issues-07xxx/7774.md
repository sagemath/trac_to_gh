# Issue 7774: notebook: after performing "evaluate all" behauviour of  creating new cells changes.

archive/issues_007774.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage 4.3, 32-bit Athlon XP, OS: Debian \"lenny\", this issue appears in a local notebook as well as on www.sagenb.org using firefox 3.0.6 and epiphany\n\nWhen working in the notebook, usually after evaluating the last cell, the result is printed out and the cursor is placed in a newly created empty cell.\n\nThis behaviour changes if \"evaluate all\" is performed on the worksheet:\n\nCreate a new worksheet, type \"1+1\" into the first cell and evaluate it, then go to the menu \"action\" and perform \"evaluate all\", then go to the last empty cell again, type something like \"1+2\" and evaluate the cell (by pressing Shift-Return), the result is printed out, but instead of creating a new empty cell and placing the cursor there, no new cell will be created, the cursor is placed in the beginning of the last evaluated cell.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7774\n\n",
    "closed_at": "2014-12-11T18:35:00Z",
    "created_at": "2009-12-27T16:10:19Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook: after performing \"evaluate all\" behauviour of  creating new cells changes.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7774",
    "user": "https://trac.sagemath.org/admin/accounts/users/ggrafendorfer"
}
```
Assignee: @williamstein

sage 4.3, 32-bit Athlon XP, OS: Debian "lenny", this issue appears in a local notebook as well as on www.sagenb.org using firefox 3.0.6 and epiphany

When working in the notebook, usually after evaluating the last cell, the result is printed out and the cursor is placed in a newly created empty cell.

This behaviour changes if "evaluate all" is performed on the worksheet:

Create a new worksheet, type "1+1" into the first cell and evaluate it, then go to the menu "action" and perform "evaluate all", then go to the last empty cell again, type something like "1+2" and evaluate the cell (by pressing Shift-Return), the result is printed out, but instead of creating a new empty cell and placing the cursor there, no new cell will be created, the cursor is placed in the beginning of the last evaluated cell.


Issue created by migration from https://trac.sagemath.org/ticket/7774





---

archive/issue_comments_066913.json:
```json
{
    "body": "I confirm this bug (K-meleon and WVista, server is 32-bit Debian lenny).\nHowever, when I \"save and quit\" the notebook a return back, the missing new cell is at the and.",
    "created_at": "2009-12-27T17:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-66913",
    "user": "https://github.com/robert-marik"
}
```

I confirm this bug (K-meleon and WVista, server is 32-bit Debian lenny).
However, when I "save and quit" the notebook a return back, the missing new cell is at the and.



---

archive/issue_comments_066914.json:
```json
{
    "body": "This should be fixed by #7666 + #6855.",
    "created_at": "2010-01-02T00:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-66914",
    "user": "https://github.com/qed777"
}
```

This should be fixed by #7666 + #6855.



---

archive/issue_comments_066915.json:
```json
{
    "body": "If someone sees this again, let's open a new ticket with more updated info; I cannot replicate this.",
    "created_at": "2014-12-10T20:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-66915",
    "user": "https://github.com/kcrisman"
}
```

If someone sees this again, let's open a new ticket with more updated info; I cannot replicate this.



---

archive/issue_comments_066916.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-10T20:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-66916",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_events_018600.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-12-10T20:29:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7774#event-18600"
}
```



---

archive/issue_comments_066917.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-10T20:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-66917",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018601.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-12-11T18:35:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7774#event-18601"
}
```



---

archive/issue_comments_066918.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2014-12-11T18:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7774#issuecomment-66918",
    "user": "https://github.com/vbraun"
}
```

Resolution: worksforme
