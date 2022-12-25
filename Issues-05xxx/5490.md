# Issue 5490: [with patch, positive review] add capabilities to compute the day of Easter

archive/issues_005490.json:
```json
{
    "body": "Assignee: psinis\n\nCC:  @cswiercz\n\nKeywords: finance, dates\n\nCalculates the date for Easter according to any of three methods: Western, Eastern Orthodox, and Julian.\n\n(Critical for future libraries which will introduce business date calculations)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5490\n\n",
    "closed_at": "2009-03-25T09:41:24Z",
    "created_at": "2009-03-11T22:19:28Z",
    "labels": [
        "component: finance"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] add capabilities to compute the day of Easter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5490",
    "user": "https://trac.sagemath.org/admin/accounts/users/psinis"
}
```
Assignee: psinis

CC:  @cswiercz

Keywords: finance, dates

Calculates the date for Easter according to any of three methods: Western, Eastern Orthodox, and Julian.

(Critical for future libraries which will introduce business date calculations)

Issue created by migration from https://trac.sagemath.org/ticket/5490





---

archive/issue_comments_042550.json:
```json
{
    "body": "Attachment [easter.patch](tarball://root/attachments/some-uuid/ticket5490/easter.patch) by mabshoff created at 2009-03-11 23:20:20",
    "created_at": "2009-03-11T23:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [easter.patch](tarball://root/attachments/some-uuid/ticket5490/easter.patch) by mabshoff created at 2009-03-11 23:20:20



---

archive/issue_comments_042551.json:
```json
{
    "body": "What is the use of the date of Easter in the Julian calender? I mean business wise?",
    "created_at": "2009-03-12T02:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42551",
    "user": "https://github.com/jaapspies"
}
```

What is the use of the date of Easter in the Julian calender? I mean business wise?



---

archive/issue_comments_042552.json:
```json
{
    "body": "Replying to [comment:2 jsp]:\n> What is the use of the date of Easter in the Julian calender? I mean business wise?\n\n\nI cannot think of a bank holiday that uses the Julian calendar in any major currency.\nChecked Russia but even there they are on the new Orthodox calendar.\nWhat is the preference here-- should I remove Julian?",
    "created_at": "2009-03-12T05:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42552",
    "user": "https://trac.sagemath.org/admin/accounts/users/psinis"
}
```

Replying to [comment:2 jsp]:
> What is the use of the date of Easter in the Julian calender? I mean business wise?


I cannot think of a bank holiday that uses the Julian calendar in any major currency.
Checked Russia but even there they are on the new Orthodox calendar.
What is the preference here-- should I remove Julian?



---

archive/issue_comments_042553.json:
```json
{
    "body": "Replying to [comment:3 psinis]:\n> Replying to [comment:2 jsp]:\n> > What is the use of the date of Easter in the Julian calender? I mean business wise?\n\n> \n> I cannot think of a bank holiday that uses the Julian calendar in any major currency.\n> Checked Russia but even there they are on the new Orthodox calendar.\n> What is the preference here-- should I remove Julian?\n>  \n\n\nYou should start a discussion on the sage devel list, I think.\nThere you will find more people who might be interested.\n\nCheers,\n\nJaap",
    "created_at": "2009-03-12T21:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42553",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:3 psinis]:
> Replying to [comment:2 jsp]:
> > What is the use of the date of Easter in the Julian calender? I mean business wise?

> 
> I cannot think of a bank holiday that uses the Julian calendar in any major currency.
> Checked Russia but even there they are on the new Orthodox calendar.
> What is the preference here-- should I remove Julian?
>  


You should start a discussion on the sage devel list, I think.
There you will find more people who might be interested.

Cheers,

Jaap



---

archive/issue_comments_042554.json:
```json
{
    "body": "Tests pass:\n\n```\nsage -t  \"devel/sage-5490/sage/finance/easter.py\"           \n\t [2.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2.0 seconds\n```\n\nI also manually checked the dates (just in case) for the next several years and all three cases seem to hold.\n\nIf this module is going to be critical for future libraries, as the ticket description says, then should it perhaps be automatically imported? Just curious.\n\n```\n# finance/all.py\n...\nfrom easter import easter\n```",
    "created_at": "2009-03-16T00:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42554",
    "user": "https://github.com/cswiercz"
}
```

Tests pass:

```
sage -t  "devel/sage-5490/sage/finance/easter.py"           
	 [2.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.0 seconds
```

I also manually checked the dates (just in case) for the next several years and all three cases seem to hold.

If this module is going to be critical for future libraries, as the ticket description says, then should it perhaps be automatically imported? Just curious.

```
# finance/all.py
...
from easter import easter
```



---

archive/issue_comments_042555.json:
```json
{
    "body": "thank you Chris for checking! \nI think we can safely leave Julian in there -- it doesn't bloat the code, nor does it make the method signature unwieldy.\n\nWhat's the next step...?",
    "created_at": "2009-03-17T08:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42555",
    "user": "https://trac.sagemath.org/admin/accounts/users/psinis"
}
```

thank you Chris for checking! 
I think we can safely leave Julian in there -- it doesn't bloat the code, nor does it make the method signature unwieldy.

What's the next step...?



---

archive/issue_comments_042556.json:
```json
{
    "body": "Replying to [comment:6 psinis]:\n> What's the next step...?\n\n\nEr...whatever you like, I suppose!",
    "created_at": "2009-03-17T12:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42556",
    "user": "https://github.com/cswiercz"
}
```

Replying to [comment:6 psinis]:
> What's the next step...?


Er...whatever you like, I suppose!



---

archive/issue_comments_042557.json:
```json
{
    "body": "Replying to [comment:6 psinis]:\n> What's the next step...?\n\n\nIf you mean the next step in this patch getting into Sage: now that it has a positive review, Michael Abshoff will eventually make sure that it merges properly and doesn't cause trouble in unforeseen places, and then it will be in the next release of Sage (either 3.4.1 or 3.4.2).",
    "created_at": "2009-03-17T21:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42557",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:6 psinis]:
> What's the next step...?


If you mean the next step in this patch getting into Sage: now that it has a positive review, Michael Abshoff will eventually make sure that it merges properly and doesn't cause trouble in unforeseen places, and then it will be in the next release of Sage (either 3.4.1 or 3.4.2).



---

archive/issue_comments_042558.json:
```json
{
    "body": "Replying to [comment:8 AlexGhitza]:\n> Replying to [comment:6 psinis]:\n> > What's the next step...?\n\n> \n> If you mean the next step in this patch getting into Sage: now that it has a positive review, Michael Abshoff will eventually make sure that it merges properly and doesn't cause trouble in unforeseen places, and then it will be in the next release of Sage (either 3.4.1 or 3.4.2).\n\n\nAh, yes. I misunderstood! Once someone has given your ticket a positive review then the rest is out of your hands. You're done and can go on to do more exciting things!",
    "created_at": "2009-03-17T21:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42558",
    "user": "https://github.com/cswiercz"
}
```

Replying to [comment:8 AlexGhitza]:
> Replying to [comment:6 psinis]:
> > What's the next step...?

> 
> If you mean the next step in this patch getting into Sage: now that it has a positive review, Michael Abshoff will eventually make sure that it merges properly and doesn't cause trouble in unforeseen places, and then it will be in the next release of Sage (either 3.4.1 or 3.4.2).


Ah, yes. I misunderstood! Once someone has given your ticket a positive review then the rest is out of your hands. You're done and can go on to do more exciting things!



---

archive/issue_comments_042559.json:
```json
{
    "body": "```\n# finance/all.py\n...\nfrom easter import easter\n```\n\nI don't think easter should be in the global namespace, but in finance.easter.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T22:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
# finance/all.py
...
from easter import easter
```

I don't think easter should be in the global namespace, but in finance.easter.

Cheers,

Michael



---

archive/issue_events_012843.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-25T09:41:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5490#event-12843"
}
```



---

archive/issue_comments_042560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T09:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042561.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T09:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5490#issuecomment-42561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_events_012844.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-25T09:41:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5490",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5490#event-12844"
}
```
