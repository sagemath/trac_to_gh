# Issue 1923: Make an obvious checkbox or menu to switch on pretty printing in the notebook

archive/issues_001923.json:
```json
{
    "body": "Assignee: was\n\nWe ought to have a very obvious, easy-to-use switch to switch on or off pretty printing in the notebook.  This request is related to the updated work done in #1922 .\n\nSomething like a checkbox up by the menus would be great.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1923\n\n",
    "created_at": "2008-01-25T08:15:33Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "title": "Make an obvious checkbox or menu to switch on pretty printing in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1923",
    "user": "jason"
}
```
Assignee: was

We ought to have a very obvious, easy-to-use switch to switch on or off pretty printing in the notebook.  This request is related to the updated work done in #1922 .

Something like a checkbox up by the menus would be great.

Issue created by migration from https://trac.sagemath.org/ticket/1923





---

archive/issue_comments_012192.json:
```json
{
    "body": "Changing assignee from was to boothby.",
    "created_at": "2008-01-25T17:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12192",
    "user": "jason"
}
```

Changing assignee from was to boothby.



---

archive/issue_comments_012193.json:
```json
{
    "body": "Changing component from algebraic geometry to notebook.",
    "created_at": "2008-01-25T17:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12193",
    "user": "jason"
}
```

Changing component from algebraic geometry to notebook.



---

archive/issue_comments_012194.json:
```json
{
    "body": "Apply this after the patch in #1922 (or change the executed command to \"lprint()\" in the sage.eval() )",
    "created_at": "2008-01-25T19:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12194",
    "user": "jason"
}
```

Apply this after the patch in #1922 (or change the executed command to "lprint()" in the sage.eval() )



---

archive/issue_comments_012195.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-25T19:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12195",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_012196.json:
```json
{
    "body": "I'm OK, with this temporarily, except I would like \"[ ] Format output\" replaced by \"[ ] Typeset output\".  Format output is too vague. \n\nI think the checkbox doesn't look like anything else in the interface.  But it is OK until something better is suggested.\n\nAnother issue is that typing pretty_print_default(True) doesn't change the state\nof the checkbox.  This is something that will get reported as a bug, but again\nI do not think it's a show stopper.  So I think this patch should be applied with the\nphrase \"Format output\" replaced by \"Typeset output\".  \n\nWilliam",
    "created_at": "2008-01-27T17:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12196",
    "user": "was"
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

archive/issue_comments_012197.json:
```json
{
    "body": "Attachment\n\nApply this instead of pretty-print-checkbox.patch",
    "created_at": "2008-01-28T15:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12197",
    "user": "jason"
}
```

Attachment

Apply this instead of pretty-print-checkbox.patch



---

archive/issue_comments_012198.json:
```json
{
    "body": "I've updated the patch to change Format output to Typeset output.\n\nDynamically updating the checkbox will require some way for the embedded sage session to communicate directly with the notebook or will require some command to be run after every evaluation (which seems bad).  This is linked to the much bigger issue (and momentum) of having interactive widgets in the notebook and I don't think the fix will be trivial.\n\nI'm not sure if the state of the checkbox is actually saved with the notebook or how that works.  I'll be working on that soon.  Do I need for the setting to appear when the \"text\" version of the worksheet is shown?\n\nI think this (updated) patch ought to go in as a start on full functionality (meaning saving the state and restoring the state when the worksheet is saved, putting the value in the text form of the worksheet, etc.).",
    "created_at": "2008-01-28T15:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12198",
    "user": "jason"
}
```

I've updated the patch to change Format output to Typeset output.

Dynamically updating the checkbox will require some way for the embedded sage session to communicate directly with the notebook or will require some command to be run after every evaluation (which seems bad).  This is linked to the much bigger issue (and momentum) of having interactive widgets in the notebook and I don't think the fix will be trivial.

I'm not sure if the state of the checkbox is actually saved with the notebook or how that works.  I'll be working on that soon.  Do I need for the setting to appear when the "text" version of the worksheet is shown?

I think this (updated) patch ought to go in as a start on full functionality (meaning saving the state and restoring the state when the worksheet is saved, putting the value in the text form of the worksheet, etc.).



---

archive/issue_comments_012199.json:
```json
{
    "body": "I think this should go into Sage as is.   More should be done at some point, but isn't needed now.  Already this is very useful (and I do use it now in fact!)",
    "created_at": "2008-01-29T12:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12199",
    "user": "was"
}
```

I think this should go into Sage as is.   More should be done at some point, but isn't needed now.  Already this is very useful (and I do use it now in fact!)



---

archive/issue_comments_012200.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-29T12:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12200",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012201.json:
```json
{
    "body": "Merged prettyprint-checkbox-updated.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-29T12:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1923#issuecomment-12201",
    "user": "mabshoff"
}
```

Merged prettyprint-checkbox-updated.patch in Sage 2.10.1.rc3
