# Issue 6262: notebook takes 5-10 minutes to quit

archive/issues_006262.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was\n\nEven with no worksheets active, with sage-4.0.1 the server takes a long time to quit after pressing ctrl-C.  This did not use to be the case, and is extremely annoying.  It consistently happens to me on an OS 10.5 intel mac.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/6262\n\n",
    "created_at": "2009-06-11T19:34:49Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook takes 5-10 minutes to quit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6262",
    "user": "mhampton"
}
```
Assignee: boothby

CC:  was

Even with no worksheets active, with sage-4.0.1 the server takes a long time to quit after pressing ctrl-C.  This did not use to be the case, and is extremely annoying.  It consistently happens to me on an OS 10.5 intel mac.  

Issue created by migration from https://trac.sagemath.org/ticket/6262





---

archive/issue_comments_049998.json:
```json
{
    "body": "You're definitely what I'd consider a \"power user\".  How many worksheets do you have?  Can you move your .sage directory temporarily, and then see if you get the same behavior?",
    "created_at": "2009-06-11T21:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-49998",
    "user": "boothby"
}
```

You're definitely what I'd consider a "power user".  How many worksheets do you have?  Can you move your .sage directory temporarily, and then see if you get the same behavior?



---

archive/issue_comments_049999.json:
```json
{
    "body": "That directory had 250 worksheets for admin, the only user account.  I used a new directory, and everything was very snappy.   So you are right, it must be related to the number of worksheets.  I still think its a bug - if there are no active worksheets it shouldn't take 10 minutes to save the notebook.",
    "created_at": "2009-06-12T02:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-49999",
    "user": "mhampton"
}
```

That directory had 250 worksheets for admin, the only user account.  I used a new directory, and everything was very snappy.   So you are right, it must be related to the number of worksheets.  I still think its a bug - if there are no active worksheets it shouldn't take 10 minutes to save the notebook.



---

archive/issue_comments_050000.json:
```json
{
    "body": "Agreed, that is a ridiculous amount of time for the notebook to quit -- but this pinpoints the problem.  (also, I can easily reproduce it now)",
    "created_at": "2009-06-16T20:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-50000",
    "user": "boothby"
}
```

Agreed, that is a ridiculous amount of time for the notebook to quit -- but this pinpoints the problem.  (also, I can easily reproduce it now)



---

archive/issue_comments_050001.json:
```json
{
    "body": "How bad is the problem in Sage 4.3.1?",
    "created_at": "2010-01-25T16:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-50001",
    "user": "mpatel"
}
```

How bad is the problem in Sage 4.3.1?



---

archive/issue_comments_050002.json:
```json
{
    "body": "I can't say exactly because after having this problem I changed the way I set up my servers to avoid having tons of worksheets and users.  Since then, I have not had a problem but I'm not sure that means the problem went away.  I am guessing that things have gotten better though since I have not had a hint of a problem recently.  I am OK with closing this ticket as invalid/fixed.",
    "created_at": "2010-01-25T19:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-50002",
    "user": "mhampton"
}
```

I can't say exactly because after having this problem I changed the way I set up my servers to avoid having tons of worksheets and users.  Since then, I have not had a problem but I'm not sure that means the problem went away.  I am guessing that things have gotten better though since I have not had a hint of a problem recently.  I am OK with closing this ticket as invalid/fixed.



---

archive/issue_comments_050003.json:
```json
{
    "body": "William -- Is this a problem with `sagenb.org`?",
    "created_at": "2010-01-25T19:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-50003",
    "user": "mpatel"
}
```

William -- Is this a problem with `sagenb.org`?



---

archive/issue_comments_050004.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-27T01:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-50004",
    "user": "mpatel"
}
```

Resolution: invalid



---

archive/issue_comments_050005.json:
```json
{
    "body": "For now, at least, I'm closing this ticket as invalid.  Feel free to reopen it!",
    "created_at": "2010-01-27T01:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6262#issuecomment-50005",
    "user": "mpatel"
}
```

For now, at least, I'm closing this ticket as invalid.  Feel free to reopen it!
