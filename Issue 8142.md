# Issue 8142: Unexpected notebook behavior when readline init file is non empty

archive/issues_008142.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: notebook readline .inputrc\n\nTo reproduce the problem\n\n===============\n\n1. Create the file ~/.inputrc with the following content:\n\n\n\n$if Python\n\n# Pair insertion\n\n\"\\(\": \"\\C-q()\\C-b\"\n\n$endif\n\n\n\nThis will automaticaly insert a closing brace after the cursor when an opening brace is inserted when the application name is Python.\n\n\n2. Start Sage\n\n\n3. In command line, everything seems ok; closing braces get inserted automaticaly.\n\n\n4. In notebook, closing braces aren't inserted automaticaly AND computations never end!\n\n\nPossible workarounds\n\n=============\n\nFrom Bash documentation (Command Line Editing>Readline Init File>Conditional Init Constructs), \"Each program using the Readline library sets the APPLICATION NAME\". The \"$if\" constructs in the .inputrc file uses this variable for application-specific settings.\n\n\nSage should set that variable to its own value. Better it should change its value when the notebook is started/stopped.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8142\n\n",
    "closed_at": "2021-12-03T18:41:01Z",
    "created_at": "2010-02-01T08:01:43Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Unexpected notebook behavior when readline init file is non empty",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8142",
    "user": "https://github.com/orontee"
}
```
Assignee: @williamstein

Keywords: notebook readline .inputrc

To reproduce the problem

===============

1. Create the file ~/.inputrc with the following content:



$if Python

# Pair insertion

"\(": "\C-q()\C-b"

$endif



This will automaticaly insert a closing brace after the cursor when an opening brace is inserted when the application name is Python.


2. Start Sage


3. In command line, everything seems ok; closing braces get inserted automaticaly.


4. In notebook, closing braces aren't inserted automaticaly AND computations never end!


Possible workarounds

=============

From Bash documentation (Command Line Editing>Readline Init File>Conditional Init Constructs), "Each program using the Readline library sets the APPLICATION NAME". The "$if" constructs in the .inputrc file uses this variable for application-specific settings.


Sage should set that variable to its own value. Better it should change its value when the notebook is started/stopped.

Issue created by migration from https://trac.sagemath.org/ticket/8142





---

archive/issue_events_019486.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19486"
}
```



---

archive/issue_events_019487.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19487"
}
```



---

archive/issue_events_019488.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19488"
}
```



---

archive/issue_events_019489.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19489"
}
```



---

archive/issue_events_019490.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19490"
}
```



---

archive/issue_events_019491.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19491"
}
```



---

archive/issue_events_019492.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19492"
}
```



---

archive/issue_events_019493.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-02T01:04:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19493"
}
```



---

archive/issue_events_019494.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-02T01:04:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19494"
}
```



---

archive/issue_comments_071468.json:
```json
{
    "body": "outdated, should close",
    "created_at": "2021-12-02T01:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8142#issuecomment-71468",
    "user": "https://github.com/mkoeppe"
}
```

outdated, should close



---

archive/issue_comments_071469.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-12-02T01:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8142#issuecomment-71469",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-12-02T23:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8142#issuecomment-71470",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019495.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-03T18:41:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8142#event-19495"
}
```



---

archive/issue_comments_071471.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-12-03T18:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8142#issuecomment-71471",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
