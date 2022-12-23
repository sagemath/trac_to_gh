# Issue 196: sage signal handler -- ctrl-c interrupt, etc.

archive/issues_000196.json:
```json
{
    "body": "Assignee: was\n\nSomewhat bizarrely, the SAGE _sig_on/_sig_off signal handling code\nappears to be completely not doing anything at all.  Weird!  This is a\nmajor bug that must be fixed before SAGE-2.0. \n\nIssue created by migration from https://trac.sagemath.org/ticket/196\n\n",
    "created_at": "2007-01-19T09:54:09Z",
    "labels": [
        "user interface",
        "blocker",
        "bug"
    ],
    "title": "sage signal handler -- ctrl-c interrupt, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/196",
    "user": "was"
}
```
Assignee: was

Somewhat bizarrely, the SAGE _sig_on/_sig_off signal handling code
appears to be completely not doing anything at all.  Weird!  This is a
major bug that must be fixed before SAGE-2.0. 

Issue created by migration from https://trac.sagemath.org/ticket/196





---

archive/issue_comments_000891.json:
```json
{
    "body": "Changing assignee from was to malb.",
    "created_at": "2007-01-20T00:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/196#issuecomment-891",
    "user": "malb"
}
```

Changing assignee from was to malb.



---

archive/issue_comments_000892.json:
```json
{
    "body": "I believe to have fixed this bug in\n\ncsage: rev6\nsage_source: rev2493",
    "created_at": "2007-01-20T00:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/196#issuecomment-892",
    "user": "malb"
}
```

I believe to have fixed this bug in

csage: rev6
sage_source: rev2493



---

archive/issue_comments_000893.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-21T21:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/196#issuecomment-893",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000894.json:
```json
{
    "body": "Martin Albrecht fixed this -- it will be in SAGE-1.8.",
    "created_at": "2007-01-21T21:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/196#issuecomment-894",
    "user": "was"
}
```

Martin Albrecht fixed this -- it will be in SAGE-1.8.
