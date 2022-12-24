# Issue 2306: Tab completion in the command-line mode

archive/issues_002306.json:
```json
{
    "body": "Assignee: was\n\nWhen I use tab-complete in the command-line interface when typing an object name, the cursor moves to one space after the end of the name. This is unwanted behaviour, because this means that one cannot then type \".\" and tab-complete again to get the list of functions associated to the object.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2306\n\n",
    "created_at": "2008-02-25T23:33:46Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Tab completion in the command-line mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2306",
    "user": "ljpk"
}
```
Assignee: was

When I use tab-complete in the command-line interface when typing an object name, the cursor moves to one space after the end of the name. This is unwanted behaviour, because this means that one cannot then type "." and tab-complete again to get the list of functions associated to the object.

Issue created by migration from https://trac.sagemath.org/ticket/2306





---

archive/issue_comments_015346.json:
```json
{
    "body": "tab completion works correctly for me (Ubuntu 7.10, 32-bit), i.e., no space after pressing tab.",
    "created_at": "2008-02-25T23:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15346",
    "user": "jason"
}
```

tab completion works correctly for me (Ubuntu 7.10, 32-bit), i.e., no space after pressing tab.



---

archive/issue_comments_015347.json:
```json
{
    "body": "OK, so I should clarify that this is for the Windows-via-VMware version 2.10.1 (as just downloaded this evening).",
    "created_at": "2008-02-25T23:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15347",
    "user": "ljpk"
}
```

OK, so I should clarify that this is for the Windows-via-VMware version 2.10.1 (as just downloaded this evening).



---

archive/issue_comments_015348.json:
```json
{
    "body": "Are you typing directly into the vmware machine, or did you ssh into it via putty or something?",
    "created_at": "2008-02-26T00:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15348",
    "user": "was"
}
```

Are you typing directly into the vmware machine, or did you ssh into it via putty or something?



---

archive/issue_comments_015349.json:
```json
{
    "body": "It works fine for me on the vmware image (run from OS X) directly typing into vmware.",
    "created_at": "2008-02-26T00:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15349",
    "user": "was"
}
```

It works fine for me on the vmware image (run from OS X) directly typing into vmware.



---

archive/issue_comments_015350.json:
```json
{
    "body": "This is directly typing in to the vmware machine.",
    "created_at": "2008-02-26T09:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15350",
    "user": "ljpk"
}
```

This is directly typing in to the vmware machine.



---

archive/issue_comments_015351.json:
```json
{
    "body": "In 2.9.3, tab completion did not put a space after the command (Ubuntu 7.10, 32-bit).\n\nHowever I am seeing this problem in 2.10.2, which, as the original poster mentioned, is annoying and slightly frustrating.",
    "created_at": "2008-03-08T20:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15351",
    "user": "jason"
}
```

In 2.9.3, tab completion did not put a space after the command (Ubuntu 7.10, 32-bit).

However I am seeing this problem in 2.10.2, which, as the original poster mentioned, is annoying and slightly frustrating.



---

archive/issue_comments_015352.json:
```json
{
    "body": "Is this still an issue?",
    "created_at": "2008-07-14T10:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15352",
    "user": "gfurnish"
}
```

Is this still an issue?



---

archive/issue_comments_015353.json:
```json
{
    "body": "Yes.  I am seeing this on a home-compiled Sage 3.0.4 on Ubuntu 8.04.",
    "created_at": "2008-07-14T14:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15353",
    "user": "jason"
}
```

Yes.  I am seeing this on a home-compiled Sage 3.0.4 on Ubuntu 8.04.



---

archive/issue_comments_015354.json:
```json
{
    "body": "For background and how to make a solution, see:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/b96905d2a648ad7b/e8586abd04da4cc5?lnk=gst&q=tab+completion+space#e8586abd04da4cc5",
    "created_at": "2008-07-14T14:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15354",
    "user": "jason"
}
```

For background and how to make a solution, see:

http://groups.google.com/group/sage-support/browse_thread/thread/b96905d2a648ad7b/e8586abd04da4cc5?lnk=gst&q=tab+completion+space#e8586abd04da4cc5



---

archive/issue_comments_015355.json:
```json
{
    "body": "#2469 is another ticket for this issue.",
    "created_at": "2008-08-21T23:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15355",
    "user": "jason"
}
```

#2469 is another ticket for this issue.



---

archive/issue_comments_015356.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-28T00:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15356",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_015357.json:
```json
{
    "body": "Closed as a dupe of #2469 since that ticket has the better explanation.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-28T00:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2306#issuecomment-15357",
    "user": "mabshoff"
}
```

Closed as a dupe of #2469 since that ticket has the better explanation.

Cheers,

Michael
