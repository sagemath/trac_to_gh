# Issue 4644: No new prompt when doing a ./sage -sh

archive/issues_004644.json:
```json
{
    "body": "Assignee: was\n\nWe used to have:\n\n\n```\n[jaap@paix sage-3.1.1]$ ./sage -sh\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\nSage subshell$ exit\nexit\nExited Sage subshell.\n[jaap@paix sage-3.1.1]$ \n\n```\n\n\nBut in sage-3.2:\n\n\n```\n[jaap@paix sage-3.2]$ ./sage -sh\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\n[jaap@paix sage-3.2]$ \n\n```\n\n\nI've been bitten by this once more!\n\nJaap\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4644\n\n",
    "created_at": "2008-11-28T18:24:42Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "No new prompt when doing a ./sage -sh",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4644",
    "user": "jsp"
}
```
Assignee: was

We used to have:


```
[jaap@paix sage-3.1.1]$ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Sage subshell$ exit
exit
Exited Sage subshell.
[jaap@paix sage-3.1.1]$ 

```


But in sage-3.2:


```
[jaap@paix sage-3.2]$ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

[jaap@paix sage-3.2]$ 

```


I've been bitten by this once more!

Jaap




Issue created by migration from https://trac.sagemath.org/ticket/4644





---

archive/issue_comments_034956.json:
```json
{
    "body": "Hi Jaap, \n\nthis one should have gone to [sage-devel] since we need to find out what the bug is. Anmd having a discussion on the ticket sucks. But:\n\n* are you using bash as default login shell?\n* please post the output from sage-sage after changing \"#!/usr/bin/env bash\" to \"#!/usr/bin/env bash -x\"\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T18:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34956",
    "user": "mabshoff"
}
```

Hi Jaap, 

this one should have gone to [sage-devel] since we need to find out what the bug is. Anmd having a discussion on the ticket sucks. But:

* are you using bash as default login shell?
* please post the output from sage-sage after changing "#!/usr/bin/env bash" to "#!/usr/bin/env bash -x"

Cheers,

Michael



---

archive/issue_comments_034957.json:
```json
{
    "body": "Ok, sorry. We had a discussion long time ago. You said you were bitten by this many times!\n\nDue to #4512 mhansen:\nCould we at least have a PS1 that includes the current directory? I always hated it when I was on a machine where \"sage -sh\" didn't use my existing PS1.\n\n\nWe now have the trouble of finding out which shell we use!\n\n\n```\nExited Sage subshell.\n[jaap@paix sage-3.2.1.rc0]$ vi local/bin/sage-sage\n[jaap@paix sage-3.2.1.rc0]$ ./sage -sh\n/usr/bin/env: bash -x: No such file or directory\n[jaap@paix sage-3.2.1.rc0]$ which bash\n/bin/bash\n[jaap@paix sage-3.2.1.rc0]$ local/bin/sage-sage\n/usr/bin/env: bash -x: No such file or directory\n[jaap@paix sage-3.2.1.rc0]$ \n\n```\n\n\nJaap",
    "created_at": "2008-12-03T16:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34957",
    "user": "jsp"
}
```

Ok, sorry. We had a discussion long time ago. You said you were bitten by this many times!

Due to #4512 mhansen:
Could we at least have a PS1 that includes the current directory? I always hated it when I was on a machine where "sage -sh" didn't use my existing PS1.


We now have the trouble of finding out which shell we use!


```
Exited Sage subshell.
[jaap@paix sage-3.2.1.rc0]$ vi local/bin/sage-sage
[jaap@paix sage-3.2.1.rc0]$ ./sage -sh
/usr/bin/env: bash -x: No such file or directory
[jaap@paix sage-3.2.1.rc0]$ which bash
/bin/bash
[jaap@paix sage-3.2.1.rc0]$ local/bin/sage-sage
/usr/bin/env: bash -x: No such file or directory
[jaap@paix sage-3.2.1.rc0]$ 

```


Jaap



---

archive/issue_comments_034958.json:
```json
{
    "body": "Maybe we can have a PS1 that is different and includes the current directory!\n\nI've been bitten by this \"defect\" once more.\n\nJaap",
    "created_at": "2009-02-05T16:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34958",
    "user": "jsp"
}
```

Maybe we can have a PS1 that is different and includes the current directory!

I've been bitten by this "defect" once more.

Jaap



---

archive/issue_comments_034959.json:
```json
{
    "body": "From sage-devel:\n\n\n```\nWilliam Stein wrote:\n\n> The justification for the existence of \"./sage -sh\" is that you can\n> type \"exit\" to get out of that subshell, and all the Sage environment\n> variables are no longer defined.  Also, on some systems \"./sage -sh\"\n> changes the prompt as a reminder (it's a bug that it doesn't do this\n> on all systems).\n>\n+1\n\nThis is http://trac.sagemath.org/sage_trac/ticket/4644\nI opened 6 month ago.\n\nWe have to thank Mike Hansen and Craig Citro for this :)\n\nhttp://trac.sagemath.org/sage_trac/ticket/4512\n\nMike:\n> Could we at least have a PS1 that includes the current directory? I always hated it when I was on a machine where \"sage -sh\" didn't use my existing PS1.\n\nCraig:\n> Yeah, that would be very reasonable.\n\nJaap\n\n\n```\n",
    "created_at": "2009-06-09T15:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34959",
    "user": "jsp"
}
```

From sage-devel:


```
William Stein wrote:

> The justification for the existence of "./sage -sh" is that you can
> type "exit" to get out of that subshell, and all the Sage environment
> variables are no longer defined.  Also, on some systems "./sage -sh"
> changes the prompt as a reminder (it's a bug that it doesn't do this
> on all systems).
>
+1

This is http://trac.sagemath.org/sage_trac/ticket/4644
I opened 6 month ago.

We have to thank Mike Hansen and Craig Citro for this :)

http://trac.sagemath.org/sage_trac/ticket/4512

Mike:
> Could we at least have a PS1 that includes the current directory? I always hated it when I was on a machine where "sage -sh" didn't use my existing PS1.

Craig:
> Yeah, that would be very reasonable.

Jaap


```




---

archive/issue_comments_034960.json:
```json
{
    "body": "There's a suggested solution to this problem: http://groups.google.com/group/sage-devel/browse_thread/thread/384d4fe7dabb722c/\n\nI'll upload the patch from that thread in a moment.",
    "created_at": "2009-09-28T23:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34960",
    "user": "ddrake"
}
```

There's a suggested solution to this problem: http://groups.google.com/group/sage-devel/browse_thread/thread/384d4fe7dabb722c/

I'll upload the patch from that thread in a moment.



---

archive/issue_comments_034961.json:
```json
{
    "body": "Attachment [trac_4644.patch](tarball://root/attachments/some-uuid/ticket4644/trac_4644.patch) by ddrake created at 2009-09-28 23:15:38",
    "created_at": "2009-09-28T23:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34961",
    "user": "ddrake"
}
```

Attachment [trac_4644.patch](tarball://root/attachments/some-uuid/ticket4644/trac_4644.patch) by ddrake created at 2009-09-28 23:15:38



---

archive/issue_comments_034962.json:
```json
{
    "body": "I think this seems good.\n\nNote that the patch applies to the scripts repo.",
    "created_at": "2009-10-05T05:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34962",
    "user": "mhansen"
}
```

I think this seems good.

Note that the patch applies to the scripts repo.



---

archive/issue_comments_034963.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-13T20:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34963",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_034964.json:
```json
{
    "body": "merged into sage-4.1.2.",
    "created_at": "2009-10-13T20:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4644#issuecomment-34964",
    "user": "was"
}
```

merged into sage-4.1.2.
