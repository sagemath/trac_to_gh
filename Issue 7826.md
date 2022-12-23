# Issue 7826: [with spkg] mpfi ignores SAGE64

archive/issues_007826.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jsp\n\nmpfi like many packages ignores the setting of SAGE64. mpfi clears CFLAGS, so even setting environment variables will not allow this to build. Hence spkg-install needed updating. \n\nI left some remarks for the package maintainer, on how to get rid of the SAGE64 junk. \n\nAn updated package can be found at the following address. All changes are checked in. \n\nSee:\nhttp://boxen.math.washington.edu/home/kirkby/portability/mpfi-1.3.4-cvs20071125.p8/\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7826\n\n",
    "created_at": "2010-01-03T03:05:51Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "[with spkg] mpfi ignores SAGE64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7826",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jsp

mpfi like many packages ignores the setting of SAGE64. mpfi clears CFLAGS, so even setting environment variables will not allow this to build. Hence spkg-install needed updating. 

I left some remarks for the package maintainer, on how to get rid of the SAGE64 junk. 

An updated package can be found at the following address. All changes are checked in. 

See:
http://boxen.math.washington.edu/home/kirkby/portability/mpfi-1.3.4-cvs20071125.p8/


Issue created by migration from https://trac.sagemath.org/ticket/7826





---

archive/issue_comments_067741.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-06T00:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67741",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067742.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-25T22:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67742",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_067743.json:
```json
{
    "body": "David, please can you explain how to reproduce the defect, and thus how to check your patch\nsolves it?",
    "created_at": "2010-02-25T22:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67743",
    "user": "zimmerma"
}
```

David, please can you explain how to reproduce the defect, and thus how to check your patch
solves it?



---

archive/issue_comments_067744.json:
```json
{
    "body": "The issue seems to be fixed:\n\n[http://trac.sagemath.org/sage_trac/ticket/8069](http://trac.sagemath.org/sage_trac/ticket/8069)\n\nAn example of a communication failure?\n\nSorry,\n\nJaap",
    "created_at": "2010-02-25T22:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67744",
    "user": "jsp"
}
```

The issue seems to be fixed:

[http://trac.sagemath.org/sage_trac/ticket/8069](http://trac.sagemath.org/sage_trac/ticket/8069)

An example of a communication failure?

Sorry,

Jaap



---

archive/issue_comments_067745.json:
```json
{
    "body": "It looks like this has been fixed, but the idea was to do exactly what was done on OS X. i.e. add the flag -m64 if the environment variable SAGE64 is set to \"yes\"\n\ndave",
    "created_at": "2010-02-25T22:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67745",
    "user": "drkirkby"
}
```

It looks like this has been fixed, but the idea was to do exactly what was done on OS X. i.e. add the flag -m64 if the environment variable SAGE64 is set to "yes"

dave



---

archive/issue_comments_067746.json:
```json
{
    "body": "> It looks like this has been fixed, but the idea was to do exactly what was done on OS X. i.e. add the flag -m64 if the environment variable SAGE64 is set to \"yes\" \n\nDave, do you want to submit a patch, or should we close that ticket?\n\nPaul",
    "created_at": "2010-02-25T22:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67746",
    "user": "zimmerma"
}
```

> It looks like this has been fixed, but the idea was to do exactly what was done on OS X. i.e. add the flag -m64 if the environment variable SAGE64 is set to "yes" 

Dave, do you want to submit a patch, or should we close that ticket?

Paul



---

archive/issue_comments_067747.json:
```json
{
    "body": "There is a patch in the directory http://boxen.math.washington.edu/home/kirkby/portability/mpfi-1.3.4-cvs20071125.p8/ but I think the issue has been resolved on another ticket, so I believe this can be closed. \n\nDave",
    "created_at": "2010-02-25T22:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67747",
    "user": "drkirkby"
}
```

There is a patch in the directory http://boxen.math.washington.edu/home/kirkby/portability/mpfi-1.3.4-cvs20071125.p8/ but I think the issue has been resolved on another ticket, so I believe this can be closed. 

Dave



---

archive/issue_comments_067748.json:
```json
{
    "body": "> so I believe this can be  closed\n\nHow to tell the release manager? (I've been told I am not allowed to close a ticket.)",
    "created_at": "2010-02-25T23:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67748",
    "user": "zimmerma"
}
```

> so I believe this can be  closed

How to tell the release manager? (I've been told I am not allowed to close a ticket.)



---

archive/issue_comments_067749.json:
```json
{
    "body": "Replying to [comment:7 zimmerma]:\n> > so I believe this can be  closed\n> \n> How to tell the release manager? (I've been told I am not allowed to close a ticket.)\n\nMaybe the owner can? Dave?\n\nJaap",
    "created_at": "2010-02-25T23:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67749",
    "user": "jsp"
}
```

Replying to [comment:7 zimmerma]:
> > so I believe this can be  closed
> 
> How to tell the release manager? (I've been told I am not allowed to close a ticket.)

Maybe the owner can? Dave?

Jaap



---

archive/issue_comments_067750.json:
```json
{
    "body": "No, I am not allowed to close the ticket, despite the fact I opened it. But I can leave a note for the release manager to close it. \n\n == Note to Release Manager ==\n\n**Another ticket, #8069 was created by Jaap to fix the same issue. Since the issue has been resolved, this ticket can be closed.**\n\nDave",
    "created_at": "2010-02-26T00:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67750",
    "user": "drkirkby"
}
```

No, I am not allowed to close the ticket, despite the fact I opened it. But I can leave a note for the release manager to close it. 

 == Note to Release Manager ==

**Another ticket, #8069 was created by Jaap to fix the same issue. Since the issue has been resolved, this ticket can be closed.**

Dave



---

archive/issue_comments_067751.json:
```json
{
    "body": "Replying to [comment:9 drkirkby]:\n> No, I am not allowed to close the ticket, despite the fact I opened it. But I can leave a note for the release manager to close it. \n> \n\nWhy not? I remember that I closed tickets some time ago.\n\nJaap",
    "created_at": "2010-02-26T00:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67751",
    "user": "jsp"
}
```

Replying to [comment:9 drkirkby]:
> No, I am not allowed to close the ticket, despite the fact I opened it. But I can leave a note for the release manager to close it. 
> 

Why not? I remember that I closed tickets some time ago.

Jaap



---

archive/issue_comments_067752.json:
```json
{
    "body": "I got told off for doing this this other day (see #8201), though in that case I marked someone elses ticket as \"wontfix\". \n\nIt was pointed out to me by Alex that the trac guidelines \n\nhttp://wiki.sagemath.org/devel/TracGuidelines \n\ndo not permit you to close tickets. \n\nMore specifically, the paragraph about closing tickets: \"No Closing Or Invalidating: Unless you have admin powers in trac (which includes all the people who have ever done releases of Sage), do not close tickets unless you are explicitly told to do so. Since we have email notification now this has become less of an issue. If you think that a ticket is invalid or has been fixed, just comment on it and the current release manager will take a look and close it if appropriate.\" \n\nI'll drop an email on sage-devel and ask someone to close it, or someone might give me permission to close it, in which case I'll do it. \n\nDave",
    "created_at": "2010-02-26T00:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67752",
    "user": "drkirkby"
}
```

I got told off for doing this this other day (see #8201), though in that case I marked someone elses ticket as "wontfix". 

It was pointed out to me by Alex that the trac guidelines 

http://wiki.sagemath.org/devel/TracGuidelines 

do not permit you to close tickets. 

More specifically, the paragraph about closing tickets: "No Closing Or Invalidating: Unless you have admin powers in trac (which includes all the people who have ever done releases of Sage), do not close tickets unless you are explicitly told to do so. Since we have email notification now this has become less of an issue. If you think that a ticket is invalid or has been fixed, just comment on it and the current release manager will take a look and close it if appropriate." 

I'll drop an email on sage-devel and ask someone to close it, or someone might give me permission to close it, in which case I'll do it. 

Dave



---

archive/issue_comments_067753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T19:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67753",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_067754.json:
```json
{
    "body": "Close as fixed by #8069.",
    "created_at": "2010-06-05T19:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7826#issuecomment-67754",
    "user": "mvngu"
}
```

Close as fixed by #8069.
