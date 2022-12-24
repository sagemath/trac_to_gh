# Issue 3050: notebook -- add "remember me" checkbox

archive/issues_003050.json:
```json
{
    "body": "Assignee: TimothyClemans\n\nPort the attached SVN patch from Knoboo to the Sage Notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3050\n\n",
    "created_at": "2008-04-28T16:48:26Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- add \"remember me\" checkbox",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3050",
    "user": "TimothyClemans"
}
```
Assignee: TimothyClemans

Port the attached SVN patch from Knoboo to the Sage Notebook.

Issue created by migration from https://trac.sagemath.org/ticket/3050





---

archive/issue_comments_021005.json:
```json
{
    "body": "The Knoboo people have this feature.  Timothy attached a patch that is relevant to their implementation, which might be of some use to whoever implements this for sage.",
    "created_at": "2008-04-29T16:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21005",
    "user": "was"
}
```

The Knoboo people have this feature.  Timothy attached a patch that is relevant to their implementation, which might be of some use to whoever implements this for sage.



---

archive/issue_comments_021006.json:
```json
{
    "body": "I want to make it clear that this functionality is not in Knoboo currently. From Alex Clemesha, \"We will get this into knoboo as soon as the \"settings\" functionality\nstarts to settle into knoboo, because, (as you would probably agree), this only thing missing with the patch would be a way for the Admin user to set the \"expires time\" (instead of hard-coded).\"",
    "created_at": "2008-04-29T20:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21006",
    "user": "TimothyClemans"
}
```

I want to make it clear that this functionality is not in Knoboo currently. From Alex Clemesha, "We will get this into knoboo as soon as the "settings" functionality
starts to settle into knoboo, because, (as you would probably agree), this only thing missing with the patch would be a way for the Admin user to set the "expires time" (instead of hard-coded)."



---

archive/issue_comments_021007.json:
```json
{
    "body": "Attachment [extcode-3050.patch](tarball://root/attachments/some-uuid/ticket3050/extcode-3050.patch) by TimothyClemans created at 2008-05-17 15:42:00",
    "created_at": "2008-05-17T15:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21007",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3050.patch](tarball://root/attachments/some-uuid/ticket3050/extcode-3050.patch) by TimothyClemans created at 2008-05-17 15:42:00



---

archive/issue_comments_021008.json:
```json
{
    "body": "Fixes #3155 also.",
    "created_at": "2008-05-17T15:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21008",
    "user": "TimothyClemans"
}
```

Fixes #3155 also.



---

archive/issue_comments_021009.json:
```json
{
    "body": "Warning: Depends on #3213",
    "created_at": "2008-05-17T15:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21009",
    "user": "TimothyClemans"
}
```

Warning: Depends on #3213



---

archive/issue_comments_021010.json:
```json
{
    "body": "REVIEW:\n\n1. It would be nice if you added a comment about what is going on in the modifications to twist.py.\n\n2. I don't actually understand how to test that this patch is actually doing something!  Could you give me simple step-by-step instructions to test out a situation where the behavior of something is different whether or not remember me is checked?   Does this feature only do anything when there are multiple accounts?  I tried what I thought was the obvious test, and it seems like Remember Me just doesn't work.  We can figure this out at the cafe today.",
    "created_at": "2008-05-17T16:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21010",
    "user": "was"
}
```

REVIEW:

1. It would be nice if you added a comment about what is going on in the modifications to twist.py.

2. I don't actually understand how to test that this patch is actually doing something!  Could you give me simple step-by-step instructions to test out a situation where the behavior of something is different whether or not remember me is checked?   Does this feature only do anything when there are multiple accounts?  I tried what I thought was the obvious test, and it seems like Remember Me just doesn't work.  We can figure this out at the cafe today.



---

archive/issue_comments_021011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T20:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21011",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021012.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T20:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21012",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.0.2.alpha1



---

archive/issue_comments_021013.json:
```json
{
    "body": "Hi,\n\nI was just using Sage on my computer with this patch applied and having a lot of problems if I open and close my browser.  I get into a state where I absolutely can't login, etc.\n\nI.e., this patch is definitely not ready for prime time.  It will break the notebook for a lot of people in confusing ways. \n\nWe'll get it fixed though.",
    "created_at": "2008-05-18T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21013",
    "user": "was"
}
```

Hi,

I was just using Sage on my computer with this patch applied and having a lot of problems if I open and close my browser.  I get into a state where I absolutely can't login, etc.

I.e., this patch is definitely not ready for prime time.  It will break the notebook for a lot of people in confusing ways. 

We'll get it fixed though.



---

archive/issue_comments_021014.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-18T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21014",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_021015.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-18T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21015",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_021016.json:
```json
{
    "body": "new and includes sage-3050.patch and sage-3050_2.patch",
    "created_at": "2008-05-19T03:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21016",
    "user": "TimothyClemans"
}
```

new and includes sage-3050.patch and sage-3050_2.patch



---

archive/issue_comments_021017.json:
```json
{
    "body": "Attachment [trac_3050-revised-sage-3050.patch](tarball://root/attachments/some-uuid/ticket3050/trac_3050-revised-sage-3050.patch) by TimothyClemans created at 2008-05-19 03:37:53\n\nI changed the cookie name to the static name \"nb_session\" in both the render for UserToplevel and in the function get_our_cookie in guard.py. I don't know if doing this fixes the problem.",
    "created_at": "2008-05-19T03:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21017",
    "user": "TimothyClemans"
}
```

Attachment [trac_3050-revised-sage-3050.patch](tarball://root/attachments/some-uuid/ticket3050/trac_3050-revised-sage-3050.patch) by TimothyClemans created at 2008-05-19 03:37:53

I changed the cookie name to the static name "nb_session" in both the render for UserToplevel and in the function get_our_cookie in guard.py. I don't know if doing this fixes the problem.



---

archive/issue_comments_021018.json:
```json
{
    "body": "The new patch works.",
    "created_at": "2008-05-19T03:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21018",
    "user": "was"
}
```

The new patch works.



---

archive/issue_comments_021019.json:
```json
{
    "body": "The new patch still causes problems, where notebooks just \"don't work\".  This is very serious and would cause mass problems by users.",
    "created_at": "2008-05-19T05:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21019",
    "user": "was"
}
```

The new patch still causes problems, where notebooks just "don't work".  This is very serious and would cause mass problems by users.



---

archive/issue_comments_021020.json:
```json
{
    "body": "Wait, I spoke too soon.  I was confused by another separate problem.",
    "created_at": "2008-05-19T05:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21020",
    "user": "was"
}
```

Wait, I spoke too soon.  I was confused by another separate problem.



---

archive/issue_comments_021021.json:
```json
{
    "body": "Merged extcode-3050.patch and trac_3050-revised-sage-3050.patch in Sage 3.0.2.alpha1",
    "created_at": "2008-05-19T06:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21021",
    "user": "mabshoff"
}
```

Merged extcode-3050.patch and trac_3050-revised-sage-3050.patch in Sage 3.0.2.alpha1



---

archive/issue_comments_021022.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-19T06:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3050#issuecomment-21022",
    "user": "mabshoff"
}
```

Resolution: fixed
