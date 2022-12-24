# Issue 3649: Add option to disable the Notebook registration email

archive/issues_003649.json:
```json
{
    "body": "Assignee: boothby\n\nFrom https://groups.google.com/group/sage-support/browse_thread/thread/1fc876f97a69eb5e\n\n```\nWhen you sign up for a Sage Notebook account, Sage sends an e-mail to\nthe address you provide giving you a link to complete the\nregistration.\n\nFirst of all, the \"Sign up for a Sage Notebook account\" says that the\ne-mail is needed if you forget your password, but makes no mention of\nthe fact that the e-mail will be needed immediately to complete the\nregistration process. If Sage asks for a user's e-mail address, it\nshould correctly indicate what that e-mail address is for. Otherwise,\ne-mail from the Sage notebook is technically spam.\n\nSecondly, I am running the Sage notebook on a machine which my\ncollege's support staff will not allow to run a mail server (all of\nthe mail on campus needs to be handled by their own antiquated\nservers, which has less storage space than my iPod to store e-mail for\n2000 users). Is there any way to turn off the sending of e-mail from\nthe Sage Notebook?\n\n-- Greg\n\n-- \nGregory D. Landweber\nAssistant Professor of Mathematics\nBard College \n```\n\nRobert Bradshaw replied:\n\n```\nThanks for the clarification. This can easily be resolved by  \ncommenting out line ~1716 of sage/server/notebook/twist.py. This  \nshould probably be made optional and configurable somewhere.\n\n- Robert \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3649\n\n",
    "created_at": "2008-07-12T18:28:44Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Add option to disable the Notebook registration email",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3649",
    "user": "mabshoff"
}
```
Assignee: boothby

From https://groups.google.com/group/sage-support/browse_thread/thread/1fc876f97a69eb5e

```
When you sign up for a Sage Notebook account, Sage sends an e-mail to
the address you provide giving you a link to complete the
registration.

First of all, the "Sign up for a Sage Notebook account" says that the
e-mail is needed if you forget your password, but makes no mention of
the fact that the e-mail will be needed immediately to complete the
registration process. If Sage asks for a user's e-mail address, it
should correctly indicate what that e-mail address is for. Otherwise,
e-mail from the Sage notebook is technically spam.

Secondly, I am running the Sage notebook on a machine which my
college's support staff will not allow to run a mail server (all of
the mail on campus needs to be handled by their own antiquated
servers, which has less storage space than my iPod to store e-mail for
2000 users). Is there any way to turn off the sending of e-mail from
the Sage Notebook?

-- Greg

-- 
Gregory D. Landweber
Assistant Professor of Mathematics
Bard College 
```

Robert Bradshaw replied:

```
Thanks for the clarification. This can easily be resolved by  
commenting out line ~1716 of sage/server/notebook/twist.py. This  
should probably be made optional and configurable somewhere.

- Robert 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3649





---

archive/issue_comments_025806.json:
```json
{
    "body": "Changing assignee from boothby to TimothyClemans.",
    "created_at": "2008-07-14T00:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25806",
    "user": "TimothyClemans"
}
```

Changing assignee from boothby to TimothyClemans.



---

archive/issue_comments_025807.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-14T00:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25807",
    "user": "TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025808.json:
```json
{
    "body": "Lines to copy out are   \n\n\n```\n1984            # Send a confirmation message to the user.\n1985            try:\n1986                send_mail(self, fromaddr, destaddr, \"Sage Notebook Registration\",body)\n1987                waiting[key] = filled_in['username']\n1988            except ValueError:\n1989                pass\n```\n\n\nIf 3.0.6 comes out few days after August 1st then instead of copying this out I'll make the email inputbox optional by the admin with the default set to False.\n\n'email_system' = False",
    "created_at": "2008-07-14T00:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25808",
    "user": "TimothyClemans"
}
```

Lines to copy out are   


```
1984            # Send a confirmation message to the user.
1985            try:
1986                send_mail(self, fromaddr, destaddr, "Sage Notebook Registration",body)
1987                waiting[key] = filled_in['username']
1988            except ValueError:
1989                pass
```


If 3.0.6 comes out few days after August 1st then instead of copying this out I'll make the email inputbox optional by the admin with the default set to False.

'email_system' = False



---

archive/issue_comments_025809.json:
```json
{
    "body": "Attachment [extcode-3649_1.patch](tarball://root/attachments/some-uuid/ticket3649/extcode-3649_1.patch) by TimothyClemans created at 2008-08-03 22:10:21",
    "created_at": "2008-08-03T22:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25809",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3649_1.patch](tarball://root/attachments/some-uuid/ticket3649/extcode-3649_1.patch) by TimothyClemans created at 2008-08-03 22:10:21



---

archive/issue_comments_025810.json:
```json
{
    "body": "Point #1 addressed by extcode-3649_1.patch. I'm starting to address #2. I will make email optional. If email services are off then automated account recovery will be disabled.",
    "created_at": "2008-08-03T22:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25810",
    "user": "TimothyClemans"
}
```

Point #1 addressed by extcode-3649_1.patch. I'm starting to address #2. I will make email optional. If email services are off then automated account recovery will be disabled.



---

archive/issue_comments_025811.json:
```json
{
    "body": "Attachment [sage-3649.patch](tarball://root/attachments/some-uuid/ticket3649/sage-3649.patch) by TimothyClemans created at 2008-08-04 20:16:02",
    "created_at": "2008-08-04T20:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25811",
    "user": "TimothyClemans"
}
```

Attachment [sage-3649.patch](tarball://root/attachments/some-uuid/ticket3649/sage-3649.patch) by TimothyClemans created at 2008-08-04 20:16:02



---

archive/issue_comments_025812.json:
```json
{
    "body": "Note: there is a script for applying the various Notebook patches. The base is sage-3.0.6.\n\nhttp://sage.math.washington.edu/home/tclemans/uw_contract_work/apply_patches.sage",
    "created_at": "2008-08-04T20:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25812",
    "user": "TimothyClemans"
}
```

Note: there is a script for applying the various Notebook patches. The base is sage-3.0.6.

http://sage.math.washington.edu/home/tclemans/uw_contract_work/apply_patches.sage



---

archive/issue_comments_025813.json:
```json
{
    "body": "WOW, this is very very nice; works perfectly. \n\nEnthusiastic positive review.",
    "created_at": "2008-08-05T05:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25813",
    "user": "was"
}
```

WOW, this is very very nice; works perfectly. 

Enthusiastic positive review.



---

archive/issue_comments_025814.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T00:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25814",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025815.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-10T00:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3649#issuecomment-25815",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1
