# Issue 1923: [with patch, positive review] Make an obvious checkbox or menu to switch on pretty printing in the notebook

archive/issues_001923.json:
```json
{
    "body": "Assignee: boothby\n\nWe ought to have a very obvious, easy-to-use switch to switch on or off pretty printing in the notebook.  This request is related to the updated work done in #1922 .\n\nSomething like a checkbox up by the menus would be great.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1923\n\n",
    "closed_at": "2008-01-29T12:38:20Z",
    "created_at": "2008-01-25T08:15:33Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, positive review] Make an obvious checkbox or menu to switch on pretty printing in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1923",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

We ought to have a very obvious, easy-to-use switch to switch on or off pretty printing in the notebook.  This request is related to the updated work done in #1922 .

Something like a checkbox up by the menus would be great.

Issue created by migration from https://trac.sagemath.org/ticket/1923





---

archive/issue_events_004628.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-25T17:49:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "milestone": "sage-2.10.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1923#event-4628"
}
```



---

archive/issue_comments_012162.json:
```json
{
    "body": "Changing assignee from @williamstein to boothby.",
    "created_at": "2008-01-25T17:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12162",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to boothby.



---

archive/issue_comments_012163.json:
```json
{
    "body": "Changing component from algebraic geometry to notebook.",
    "created_at": "2008-01-25T17:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12163",
    "user": "https://github.com/jasongrout"
}
```

Changing component from algebraic geometry to notebook.



---

archive/issue_comments_012164.json:
```json
{
    "body": "Apply this after the patch in #1922 (or change the executed command to \"lprint()\" in the sage.eval() )",
    "created_at": "2008-01-25T19:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12164",
    "user": "https://github.com/jasongrout"
}
```

Apply this after the patch in #1922 (or change the executed command to "lprint()" in the sage.eval() )



---

archive/issue_comments_012165.json:
```json
{
    "body": "Attachment [prettyprint-checkbox.patch](tarball://root/attachments/some-uuid/ticket1923/prettyprint-checkbox.patch) by @jasongrout created at 2008-01-25 19:34:38",
    "created_at": "2008-01-25T19:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12165",
    "user": "https://github.com/jasongrout"
}
```

Attachment [prettyprint-checkbox.patch](tarball://root/attachments/some-uuid/ticket1923/prettyprint-checkbox.patch) by @jasongrout created at 2008-01-25 19:34:38



---

archive/issue_comments_012166.json:
```json
{
    "body": "I'm OK, with this temporarily, except I would like \"[ ] Format output\" replaced by \"[ ] Typeset output\".  Format output is too vague. \n\nI think the checkbox doesn't look like anything else in the interface.  But it is OK until something better is suggested.\n\nAnother issue is that typing pretty_print_default(True) doesn't change the state\nof the checkbox.  This is something that will get reported as a bug, but again\nI do not think it's a show stopper.  So I think this patch should be applied with the\nphrase \"Format output\" replaced by \"Typeset output\".  \n\nWilliam",
    "created_at": "2008-01-27T17:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12166",
    "user": "https://github.com/williamstein"
}
```

I'm OK, with this temporarily, except I would like "[ ] Format output" replaced by "[ ] Typeset output".  Format output is too vague. 

I think the checkbox doesn't look like anything else in the interface.  But it is OK until something better is suggested.

Another issue is that typing pretty_print_default(True) doesn't change the state
of the checkbox.  This is something that will get reported as a bug, but again
I do not think it's a show stopper.  So I think this patch should be applied with the
phrase "Format output" replaced by "Typeset output".  

William



---

archive/issue_comments_012167.json:
```json
{
    "body": "Attachment [prettyprint-checkbox-updated.patch](tarball://root/attachments/some-uuid/ticket1923/prettyprint-checkbox-updated.patch) by @jasongrout created at 2008-01-28 15:22:07\n\nApply this instead of pretty-print-checkbox.patch",
    "created_at": "2008-01-28T15:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12167",
    "user": "https://github.com/jasongrout"
}
```

Attachment [prettyprint-checkbox-updated.patch](tarball://root/attachments/some-uuid/ticket1923/prettyprint-checkbox-updated.patch) by @jasongrout created at 2008-01-28 15:22:07

Apply this instead of pretty-print-checkbox.patch



---

archive/issue_comments_012168.json:
```json
{
    "body": "I've updated the patch to change Format output to Typeset output.\n\nDynamically updating the checkbox will require some way for the embedded sage session to communicate directly with the notebook or will require some command to be run after every evaluation (which seems bad).  This is linked to the much bigger issue (and momentum) of having interactive widgets in the notebook and I don't think the fix will be trivial.\n\nI'm not sure if the state of the checkbox is actually saved with the notebook or how that works.  I'll be working on that soon.  Do I need for the setting to appear when the \"text\" version of the worksheet is shown?\n\nI think this (updated) patch ought to go in as a start on full functionality (meaning saving the state and restoring the state when the worksheet is saved, putting the value in the text form of the worksheet, etc.).",
    "created_at": "2008-01-28T15:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12168",
    "user": "https://github.com/jasongrout"
}
```

I've updated the patch to change Format output to Typeset output.

Dynamically updating the checkbox will require some way for the embedded sage session to communicate directly with the notebook or will require some command to be run after every evaluation (which seems bad).  This is linked to the much bigger issue (and momentum) of having interactive widgets in the notebook and I don't think the fix will be trivial.

I'm not sure if the state of the checkbox is actually saved with the notebook or how that works.  I'll be working on that soon.  Do I need for the setting to appear when the "text" version of the worksheet is shown?

I think this (updated) patch ought to go in as a start on full functionality (meaning saving the state and restoring the state when the worksheet is saved, putting the value in the text form of the worksheet, etc.).



---

archive/issue_comments_012169.json:
```json
{
    "body": "I think this should go into Sage as is.   More should be done at some point, but isn't needed now.  Already this is very useful (and I do use it now in fact!)",
    "created_at": "2008-01-29T12:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12169",
    "user": "https://github.com/williamstein"
}
```

I think this should go into Sage as is.   More should be done at some point, but isn't needed now.  Already this is very useful (and I do use it now in fact!)



---

archive/issue_comments_012170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-29T12:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12170",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012171.json:
```json
{
    "body": "Merged prettyprint-checkbox-updated.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-29T12:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12171",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged prettyprint-checkbox-updated.patch in Sage 2.10.1.rc3



---

archive/issue_events_004629.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-29T12:38:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1923#event-4629"
}
```
