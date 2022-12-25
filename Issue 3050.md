# Issue 3050: notebook -- add "remember me" checkbox

archive/issues_003050.json:
```json
{
    "body": "Assignee: TimothyClemans\n\nPort the attached SVN patch from Knoboo to the Sage Notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3050\n\n",
    "created_at": "2008-04-28T16:48:26Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- add \"remember me\" checkbox",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3050",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: TimothyClemans

Port the attached SVN patch from Knoboo to the Sage Notebook.

Issue created by migration from https://trac.sagemath.org/ticket/3050





---

archive/issue_comments_020962.json:
```json
{
    "body": "The Knoboo people have this feature.  Timothy attached a patch that is relevant to their implementation, which might be of some use to whoever implements this for sage.",
    "created_at": "2008-04-29T16:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20962",
    "user": "https://github.com/williamstein"
}
```

The Knoboo people have this feature.  Timothy attached a patch that is relevant to their implementation, which might be of some use to whoever implements this for sage.



---

archive/issue_comments_020963.json:
```json
{
    "body": "I want to make it clear that this functionality is not in Knoboo currently. From Alex Clemesha, \"We will get this into knoboo as soon as the \"settings\" functionality\nstarts to settle into knoboo, because, (as you would probably agree), this only thing missing with the patch would be a way for the Admin user to set the \"expires time\" (instead of hard-coded).\"",
    "created_at": "2008-04-29T20:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20963",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I want to make it clear that this functionality is not in Knoboo currently. From Alex Clemesha, "We will get this into knoboo as soon as the "settings" functionality
starts to settle into knoboo, because, (as you would probably agree), this only thing missing with the patch would be a way for the Admin user to set the "expires time" (instead of hard-coded)."



---

archive/issue_comments_020964.json:
```json
{
    "body": "Attachment [extcode-3050.patch](tarball://root/attachments/some-uuid/ticket3050/extcode-3050.patch) by TimothyClemans created at 2008-05-17 15:42:00",
    "created_at": "2008-05-17T15:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20964",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [extcode-3050.patch](tarball://root/attachments/some-uuid/ticket3050/extcode-3050.patch) by TimothyClemans created at 2008-05-17 15:42:00



---

archive/issue_comments_020965.json:
```json
{
    "body": "Fixes #3155 also.",
    "created_at": "2008-05-17T15:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20965",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Fixes #3155 also.



---

archive/issue_comments_020966.json:
```json
{
    "body": "Warning: Depends on #3213",
    "created_at": "2008-05-17T15:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20966",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Warning: Depends on #3213



---

archive/issue_comments_020967.json:
```json
{
    "body": "REVIEW:\n\n1. It would be nice if you added a comment about what is going on in the modifications to twist.py.\n\n2. I don't actually understand how to test that this patch is actually doing something!  Could you give me simple step-by-step instructions to test out a situation where the behavior of something is different whether or not remember me is checked?   Does this feature only do anything when there are multiple accounts?  I tried what I thought was the obvious test, and it seems like Remember Me just doesn't work.  We can figure this out at the cafe today.",
    "created_at": "2008-05-17T16:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20967",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

1. It would be nice if you added a comment about what is going on in the modifications to twist.py.

2. I don't actually understand how to test that this patch is actually doing something!  Could you give me simple step-by-step instructions to test out a situation where the behavior of something is different whether or not remember me is checked?   Does this feature only do anything when there are multiple accounts?  I tried what I thought was the obvious test, and it seems like Remember Me just doesn't work.  We can figure this out at the cafe today.



---

archive/issue_comments_020968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T20:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20968",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020969.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T20:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20969",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.0.2.alpha1



---

archive/issue_events_003258.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-17T20:29:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3050#event-3258"
}
```



---

archive/issue_comments_020970.json:
```json
{
    "body": "Hi,\n\nI was just using Sage on my computer with this patch applied and having a lot of problems if I open and close my browser.  I get into a state where I absolutely can't login, etc.\n\nI.e., this patch is definitely not ready for prime time.  It will break the notebook for a lot of people in confusing ways. \n\nWe'll get it fixed though.",
    "created_at": "2008-05-18T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20970",
    "user": "https://github.com/williamstein"
}
```

Hi,

I was just using Sage on my computer with this patch applied and having a lot of problems if I open and close my browser.  I get into a state where I absolutely can't login, etc.

I.e., this patch is definitely not ready for prime time.  It will break the notebook for a lot of people in confusing ways. 

We'll get it fixed though.



---

archive/issue_comments_020971.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-18T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20971",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003259.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-05-18T16:32:31Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3050#event-3259"
}
```



---

archive/issue_comments_020972.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-18T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20972",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_020973.json:
```json
{
    "body": "new and includes sage-3050.patch and sage-3050_2.patch",
    "created_at": "2008-05-19T03:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20973",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

new and includes sage-3050.patch and sage-3050_2.patch



---

archive/issue_comments_020974.json:
```json
{
    "body": "Attachment [trac_3050-revised-sage-3050.patch](tarball://root/attachments/some-uuid/ticket3050/trac_3050-revised-sage-3050.patch) by TimothyClemans created at 2008-05-19 03:37:53\n\nI changed the cookie name to the static name \"nb_session\" in both the render for UserToplevel and in the function get_our_cookie in guard.py. I don't know if doing this fixes the problem.",
    "created_at": "2008-05-19T03:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20974",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [trac_3050-revised-sage-3050.patch](tarball://root/attachments/some-uuid/ticket3050/trac_3050-revised-sage-3050.patch) by TimothyClemans created at 2008-05-19 03:37:53

I changed the cookie name to the static name "nb_session" in both the render for UserToplevel and in the function get_our_cookie in guard.py. I don't know if doing this fixes the problem.



---

archive/issue_comments_020975.json:
```json
{
    "body": "The new patch works.",
    "created_at": "2008-05-19T03:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20975",
    "user": "https://github.com/williamstein"
}
```

The new patch works.



---

archive/issue_comments_020976.json:
```json
{
    "body": "The new patch still causes problems, where notebooks just \"don't work\".  This is very serious and would cause mass problems by users.",
    "created_at": "2008-05-19T05:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20976",
    "user": "https://github.com/williamstein"
}
```

The new patch still causes problems, where notebooks just "don't work".  This is very serious and would cause mass problems by users.



---

archive/issue_comments_020977.json:
```json
{
    "body": "Wait, I spoke too soon.  I was confused by another separate problem.",
    "created_at": "2008-05-19T05:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20977",
    "user": "https://github.com/williamstein"
}
```

Wait, I spoke too soon.  I was confused by another separate problem.



---

archive/issue_comments_020978.json:
```json
{
    "body": "Merged extcode-3050.patch and trac_3050-revised-sage-3050.patch in Sage 3.0.2.alpha1",
    "created_at": "2008-05-19T06:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged extcode-3050.patch and trac_3050-revised-sage-3050.patch in Sage 3.0.2.alpha1



---

archive/issue_comments_020979.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-19T06:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-20979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003260.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-19T06:07:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3050#event-3260"
}
```
