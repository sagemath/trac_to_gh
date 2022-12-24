# Issue 4979: do not use xdg-open on Solaris to open the browser when starting the notebook

archive/issues_004979.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  dimpase mkoeppe\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/f037b3c4cc4509eb for a discussion about the problem.\n\nxdg-open is not available on Solaris, so we should be using a Solaris specific mechanism to open the default browser. It is unclear at least to me at the moment what this would be.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4979\n\n",
    "created_at": "2009-01-15T00:54:44Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "do not use xdg-open on Solaris to open the browser when starting the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4979",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  dimpase mkoeppe

See http://groups.google.com/group/sage-devel/browse_thread/thread/f037b3c4cc4509eb for a discussion about the problem.

xdg-open is not available on Solaris, so we should be using a Solaris specific mechanism to open the default browser. It is unclear at least to me at the moment what this would be.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4979





---

archive/issue_comments_037959.json:
```json
{
    "body": "We should use sdtwebclient for now on Solaris since it is the default way to open a url by the default system browser on Solaris:\n\n```\n-bash-3.00$ /usr/dt/bin/sdtwebclient --help\n/usr/dt/bin/sdtwebclient[117]: getopts: help bad option(s)\nUsage: sdtwebclient [-b browser] [-o browser_opts] url-string\n-bash-3.00$ man sdtwebclient\nNo manual entry for sdtwebclient. [:(]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-01-15T01:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4979#issuecomment-37959",
    "user": "mabshoff"
}
```

We should use sdtwebclient for now on Solaris since it is the default way to open a url by the default system browser on Solaris:

```
-bash-3.00$ /usr/dt/bin/sdtwebclient --help
/usr/dt/bin/sdtwebclient[117]: getopts: help bad option(s)
Usage: sdtwebclient [-b browser] [-o browser_opts] url-string
-bash-3.00$ man sdtwebclient
No manual entry for sdtwebclient. [:(]
```


Cheers,

Michael



---

archive/issue_comments_037960.json:
```json
{
    "body": "I've just seen a bug report of this on sci.math.symbolic and comp.unix.solaris. \n\nI found this bug report on comp.unix.solaris and sci.math.symbolic\n\nhttp://groups.google.com/group/comp.unix.solaris/msg/ce5b85e425cdcb90?hl=en\n\nI thought this has been fixed on a recent patch, but I must admit I can't find it. This obviously needs solving asap. I'll work on this. \n\n\nDave",
    "created_at": "2010-02-23T12:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4979#issuecomment-37960",
    "user": "drkirkby"
}
```

I've just seen a bug report of this on sci.math.symbolic and comp.unix.solaris. 

I found this bug report on comp.unix.solaris and sci.math.symbolic

http://groups.google.com/group/comp.unix.solaris/msg/ce5b85e425cdcb90?hl=en

I thought this has been fixed on a recent patch, but I must admit I can't find it. This obviously needs solving asap. I'll work on this. 


Dave



---

archive/issue_comments_037961.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-03T08:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4979#issuecomment-37961",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037962.json:
```json
{
    "body": "I propose to close this ancient ticket about deprecated SageNB. Agreed ?",
    "created_at": "2020-05-03T08:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4979#issuecomment-37962",
    "user": "chapoton"
}
```

I propose to close this ancient ticket about deprecated SageNB. Agreed ?



---

archive/issue_comments_037963.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-05-03T09:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4979#issuecomment-37963",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037964.json:
```json
{
    "body": "thanks. Closing as invalid.",
    "created_at": "2020-05-03T09:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4979#issuecomment-37964",
    "user": "chapoton"
}
```

thanks. Closing as invalid.



---

archive/issue_comments_037965.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-05-03T09:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4979#issuecomment-37965",
    "user": "chapoton"
}
```

Resolution: invalid
