# Issue 2745: upgrade twisted to 8.0.1

archive/issues_002745.json:
```json
{
    "body": "Assignee: mabshoff\n\nA major new version of twisted has been released and I strongly recommend that we upgrade to it for sage-3.0.  There are a ton of new features and many bug fixes. Some specifics that are relevant to dsage are:\n\n- The reactor now has a blockingCallFromThread method for non-reactor threads\n  to use to wait for a reactor-scheduled call to return a result (#1042, #3030)\n- LoopingCall now allows you to specify the reactor to use to schedule new\n  calls, allowing much better testing techniques (#2633, #2634)\n- twisted.python.log now contains a Twisted log observer which can forward\n  messages to the Python logging system (#1351)\n- Log files now include seconds in the timestamps (#867)\n- PB now supports anonymous login (#439, #2312)\n- twisted.spread.jelly now supports decimal objects (#2920)\n- twisted.spread.jelly now supports all forms of sets (#2958)\n\nAlso, this release is easy_install'able. I don't know if we ever use easy_install to install packages or what the thought on it is. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2745\n\n",
    "created_at": "2008-04-01T00:42:44Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "upgrade twisted to 8.0.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2745",
    "user": "yi"
}
```
Assignee: mabshoff

A major new version of twisted has been released and I strongly recommend that we upgrade to it for sage-3.0.  There are a ton of new features and many bug fixes. Some specifics that are relevant to dsage are:

- The reactor now has a blockingCallFromThread method for non-reactor threads
  to use to wait for a reactor-scheduled call to return a result (#1042, #3030)
- LoopingCall now allows you to specify the reactor to use to schedule new
  calls, allowing much better testing techniques (#2633, #2634)
- twisted.python.log now contains a Twisted log observer which can forward
  messages to the Python logging system (#1351)
- Log files now include seconds in the timestamps (#867)
- PB now supports anonymous login (#439, #2312)
- twisted.spread.jelly now supports decimal objects (#2920)
- twisted.spread.jelly now supports all forms of sets (#2958)

Also, this release is easy_install'able. I don't know if we ever use easy_install to install packages or what the thought on it is. 


Issue created by migration from https://trac.sagemath.org/ticket/2745





---

archive/issue_comments_018865.json:
```json
{
    "body": "new package up at\n\nhttp://sage.math.washington.edu/home/yqiang/spkgs/twisted-8.0.1.spkg\n\nPlease review & test!",
    "created_at": "2008-04-05T23:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2745#issuecomment-18865",
    "user": "yi"
}
```

new package up at

http://sage.math.washington.edu/home/yqiang/spkgs/twisted-8.0.1.spkg

Please review & test!



---

archive/issue_comments_018866.json:
```json
{
    "body": "I guess the \"Summary\" is supposed to say SPGK.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T00:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2745#issuecomment-18866",
    "user": "mabshoff"
}
```

I guess the "Summary" is supposed to say SPGK.

Cheers,

Michael



---

archive/issue_comments_018867.json:
```json
{
    "body": "mhansen did play with this and did give it a positive review. It builds and installs fine for me. I added a mercurial repo and some other small bits.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T03:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2745#issuecomment-18867",
    "user": "mabshoff"
}
```

mhansen did play with this and did give it a positive review. It builds and installs fine for me. I added a mercurial repo and some other small bits.

Cheers,

Michael



---

archive/issue_comments_018868.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T03:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2745#issuecomment-18868",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_018869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T03:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2745#issuecomment-18869",
    "user": "mabshoff"
}
```

Resolution: fixed
