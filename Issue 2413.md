# Issue 2413: Correction in "How to use the Sage Notebook"

archive/issues_002413.json:
```json
{
    "body": "Assignee: tba\n\nIn SAGE Notebook Help:\n\nThe variable DATA contains the directory with data files that you upload into the worksheet. For example, to open a file in that directory, do \"open(DIR+'filename')\".\n\n\nshould be:\n\nThe variable DATA contains the directory with data files that you upload into the worksheet. For example, to open a file in that directory, do \"open(DATA+'filename')\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/2413\n\n",
    "created_at": "2008-03-06T23:33:19Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Correction in \"How to use the Sage Notebook\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2413",
    "user": "https://trac.sagemath.org/admin/accounts/users/hfvillafuerte"
}
```
Assignee: tba

In SAGE Notebook Help:

The variable DATA contains the directory with data files that you upload into the worksheet. For example, to open a file in that directory, do "open(DIR+'filename')".


should be:

The variable DATA contains the directory with data files that you upload into the worksheet. For example, to open a file in that directory, do "open(DATA+'filename')".

Issue created by migration from https://trac.sagemath.org/ticket/2413





---

archive/issue_comments_016247.json:
```json
{
    "body": "I believe this refers to documentation which is generated from server/notebook/tutorial.py, and which shows up on the introductory page when you click help from the notebook.  If so, this is already fixed as of 3.1.2.rc2.",
    "created_at": "2008-09-14T05:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2413#issuecomment-16247",
    "user": "https://github.com/jicama"
}
```

I believe this refers to documentation which is generated from server/notebook/tutorial.py, and which shows up on the introductory page when you click help from the notebook.  If so, this is already fixed as of 3.1.2.rc2.



---

archive/issue_events_002589.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-14T05:34:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2413",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2413#event-2589"
}
```



---

archive/issue_comments_016248.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T05:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2413#issuecomment-16248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016249.json:
```json
{
    "body": "This was fixed in Sage 3.0.1 via #3095. Thanks for tracking this down.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T05:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2413#issuecomment-16249",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This was fixed in Sage 3.0.1 via #3095. Thanks for tracking this down.

Cheers,

Michael
