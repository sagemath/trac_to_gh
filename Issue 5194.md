# Issue 5194: add option to turn off automatic updates for an interact

archive/issues_005194.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  jason\n\nWhenever the user of an interact tabs from one input_box to another, the function is called, which sets off all the computations associated with the interact. Even when the computations are not very time-consuming, it can be a hassle if, for example, the user wishes to change several input boxes at once, before getting an update.\n\nThis enhancement, discussed [here](http://groups.google.com/group/sage-devel/browse_thread/thread/9ff935e0d6a729b3/554c6c448e6a75e5?lnk=gst&q=interact+update#554c6c448e6a75e5) on sage-devel, would allow an interact to turn off automatic update, adding a user interface element that will prompt the interact to re-run.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5194\n\n",
    "created_at": "2009-02-06T03:38:45Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "add option to turn off automatic updates for an interact",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5194",
    "user": "john_perry"
}
```
Assignee: boothby

CC:  jason

Whenever the user of an interact tabs from one input_box to another, the function is called, which sets off all the computations associated with the interact. Even when the computations are not very time-consuming, it can be a hassle if, for example, the user wishes to change several input boxes at once, before getting an update.

This enhancement, discussed [here](http://groups.google.com/group/sage-devel/browse_thread/thread/9ff935e0d6a729b3/554c6c448e6a75e5?lnk=gst&q=interact+update#554c6c448e6a75e5) on sage-devel, would allow an interact to turn off automatic update, adding a user interface element that will prompt the interact to re-run.

Issue created by migration from https://trac.sagemath.org/ticket/5194





---

archive/issue_comments_039811.json:
```json
{
    "body": "Attachment [update_interact.patch](tarball://root/attachments/some-uuid/ticket5194/update_interact.patch) by john_perry created at 2009-02-06 03:39:33\n\na patch that adds a checkbox to control automatic updating",
    "created_at": "2009-02-06T03:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39811",
    "user": "john_perry"
}
```

Attachment [update_interact.patch](tarball://root/attachments/some-uuid/ticket5194/update_interact.patch) by john_perry created at 2009-02-06 03:39:33

a patch that adds a checkbox to control automatic updating



---

archive/issue_comments_039812.json:
```json
{
    "body": "The patch I've attached is **not** the one described in the final version of the discussion. Mike Hansen recommended that we provide a button that, when pressed, updates the interact, and when not pressed, does not.\n\nI don't know how to create a button (Sage doesn't have them yet), but I do know how to create a checkbox. After looking at the code tonight, I also suspect that it will take a more serious rewrite of interact to make that version work. The submitted patch can serve as a stopgap.",
    "created_at": "2009-02-06T03:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39812",
    "user": "john_perry"
}
```

The patch I've attached is **not** the one described in the final version of the discussion. Mike Hansen recommended that we provide a button that, when pressed, updates the interact, and when not pressed, does not.

I don't know how to create a button (Sage doesn't have them yet), but I do know how to create a checkbox. After looking at the code tonight, I also suspect that it will take a more serious rewrite of interact to make that version work. The submitted patch can serve as a stopgap.



---

archive/issue_comments_039813.json:
```json
{
    "body": "This stopgap patch: \n* still causes a roundtrip to the server\n* //deletes// the output when unchecked, and you can't see the output again until you check it.  This could be considered a good thing.\n\nHowever, it's still a nice stopgap approach.  The documentation is missing, though.  Positive review when the documentation to the interact function mentions this parameter and tells what it does.",
    "created_at": "2009-02-06T20:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39813",
    "user": "jason"
}
```

This stopgap patch: 
* still causes a roundtrip to the server
* //deletes// the output when unchecked, and you can't see the output again until you check it.  This could be considered a good thing.

However, it's still a nice stopgap approach.  The documentation is missing, though.  Positive review when the documentation to the interact function mentions this parameter and tells what it does.



---

archive/issue_comments_039814.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39814",
    "user": "mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_039815.json:
```json
{
    "body": "Attachment [trac_5194.patch](tarball://root/attachments/some-uuid/ticket5194/trac_5194.patch) by mhansen created at 2009-02-07 05:35:29",
    "created_at": "2009-02-07T05:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39815",
    "user": "mhansen"
}
```

Attachment [trac_5194.patch](tarball://root/attachments/some-uuid/ticket5194/trac_5194.patch) by mhansen created at 2009-02-07 05:35:29



---

archive/issue_comments_039816.json:
```json
{
    "body": "I've posted a patch which implements what was discussed on sage-devel.  A lot of it is mostly general infrastructure stuff such as separating the updating of values from the running of the interact function.\n\nCurrently, when the values are changed, the output is deleted.  One could get around this, but the implementation is a bit messy since the update button would have to go through all of the controls and update the values in the Sage process for each of them.",
    "created_at": "2009-02-07T05:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39816",
    "user": "mhansen"
}
```

I've posted a patch which implements what was discussed on sage-devel.  A lot of it is mostly general infrastructure stuff such as separating the updating of values from the running of the interact function.

Currently, when the values are changed, the output is deleted.  One could get around this, but the implementation is a bit messy since the update button would have to go through all of the controls and update the values in the Sage process for each of them.



---

archive/issue_comments_039817.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2009-02-07T05:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39817",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_039818.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-07T05:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39818",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039819.json:
```json
{
    "body": "The second patch does exactly what I would have liked. It is unfortunate that the output is deleted, but the current situation is much better than the previous one. In addition, it adds some infrastructure for a button object to interact, although anything beyond the Update button is non-trivial to get working.\n\nThe only caution I would issue is that when I ran `sage -t` I initially encountered the following failure:\n\n**********************************************************************\nFile \"/home/software/sage-3.2.1/devel/sage-main/sage/server/notebook/interact.py\", line 677:\n    sage: sage.server.notebook.interact.InputBox('theta', 1).render()\nExpected:\n    '<input type=\\'text\\' value=\"1\" size=80 onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"theta\\\\\", ..., sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64(this.value)+\"\\\\\"), globals());sage.server.notebook.interact.recompute(0)\")\\'></input>'\nGot:\n    '<input type=\\'text\\' value=\\'1\\' size=80 onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"theta\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64(this.value)+\"\\\\\"), globals());sage.server.notebook.interact.recompute(0)\")\\'></input>'\n**********************************************************************\n\nThis appears to be due to a difference in code that your patch did not update: once I changed the relevant line to return `value=\"%r\"` and `value=\"%s\"` instead of `value='%r'` and `value='%s'` this worked. Maybe I was missing some intermediate patch?",
    "created_at": "2009-02-08T17:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39819",
    "user": "john_perry"
}
```

The second patch does exactly what I would have liked. It is unfortunate that the output is deleted, but the current situation is much better than the previous one. In addition, it adds some infrastructure for a button object to interact, although anything beyond the Update button is non-trivial to get working.

The only caution I would issue is that when I ran `sage -t` I initially encountered the following failure:

**********************************************************************
File "/home/software/sage-3.2.1/devel/sage-main/sage/server/notebook/interact.py", line 677:
    sage: sage.server.notebook.interact.InputBox('theta', 1).render()
Expected:
    '<input type=\'text\' value="1" size=80 onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", ..., sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals());sage.server.notebook.interact.recompute(0)")\'></input>'
Got:
    '<input type=\'text\' value=\'1\' size=80 onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals());sage.server.notebook.interact.recompute(0)")\'></input>'
**********************************************************************

This appears to be due to a difference in code that your patch did not update: once I changed the relevant line to return `value="%r"` and `value="%s"` instead of `value='%r'` and `value='%s'` this worked. Maybe I was missing some intermediate patch?



---

archive/issue_comments_039820.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2009-02-08T17:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39820",
    "user": "john_perry"
}
```

Resolution: worksforme



---

archive/issue_comments_039821.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2009-02-08T18:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39821",
    "user": "mabshoff"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_039822.json:
```json
{
    "body": "John,\n\n* do not close tickets, the release manager does that once the patch has been merged.\n* do not give an unconditional positive review to ticket that have doctest failures\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T18:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39822",
    "user": "mabshoff"
}
```

John,

* do not close tickets, the release manager does that once the patch has been merged.
* do not give an unconditional positive review to ticket that have doctest failures

Cheers,

Michael



---

archive/issue_comments_039823.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-08T18:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39823",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_039824.json:
```json
{
    "body": "Ok, according to the doctesting this is the problem:\n\n```\n    '<input type=\\'text\\' value=\"1\" size=80 \n    '<input type=\\'text\\' value=\\'1\\' size=80 \n```\n\ni.e. a change in escaping. This looks fine to me, but I will apply the patches and see if the doctest issue is still even there.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T11:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39824",
    "user": "mabshoff"
}
```

Ok, according to the doctesting this is the problem:

```
    '<input type=\'text\' value="1" size=80 
    '<input type=\'text\' value=\'1\' size=80 
```

i.e. a change in escaping. This looks fine to me, but I will apply the patches and see if the doctest issue is still even there.

Cheers,

Michael



---

archive/issue_comments_039825.json:
```json
{
    "body": "With my merge tree and mhansen's patch only:\n\n```\nAll tests passed!\nTimings have been updated.\nTotal time for all tests: 266.2 seconds\n```\n\nSo back to positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T11:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39825",
    "user": "mabshoff"
}
```

With my merge tree and mhansen's patch only:

```
All tests passed!
Timings have been updated.
Total time for all tests: 266.2 seconds
```

So back to positive review.

Cheers,

Michael



---

archive/issue_comments_039826.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-09T11:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39826",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039827.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T11:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5194#issuecomment-39827",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael
