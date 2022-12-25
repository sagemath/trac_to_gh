# Issue 4877: [with spkg; needs work] update optional spkg to newest version of pyopenssl and get spkg into proper format

archive/issues_004877.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe new spkg is here:  \n    http://sage.math.washington.edu/home/was/patches/pyopenssl-0.8.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/4877\n\n",
    "closed_at": "2015-04-09T12:12:12Z",
    "created_at": "2008-12-24T20:37:22Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with spkg; needs work] update optional spkg to newest version of pyopenssl and get spkg into proper format",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4877",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

The new spkg is here:  
    http://sage.math.washington.edu/home/was/patches/pyopenssl-0.8.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4877





---

archive/issue_comments_036856.json:
```json
{
    "body": "William,\n\nthe spkg at\n\n http://sage.math.washington.edu/home/mabshoff/spkgs/pyopenssl-0.8.p0.spkg\n\nfixes various issues: Among them is a check for the openssl headers in $SAGE_LOCAL/include, which might or might not be too restrictive, i.e. since it doesn't allow the user to use the system openssl.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T17:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4877#issuecomment-36856",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

William,

the spkg at

 http://sage.math.washington.edu/home/mabshoff/spkgs/pyopenssl-0.8.p0.spkg

fixes various issues: Among them is a check for the openssl headers in $SAGE_LOCAL/include, which might or might not be too restrictive, i.e. since it doesn't allow the user to use the system openssl.

Cheers,

Michael



---

archive/issue_comments_036857.json:
```json
{
    "body": "This can also be resolved post 3.2.3 since it is unrelated to any code in the core of Sage.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T17:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4877#issuecomment-36857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This can also be resolved post 3.2.3 since it is unrelated to any code in the core of Sage.

Cheers,

Michael



---

archive/issue_events_011234.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-26T17:14:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11234"
}
```



---

archive/issue_comments_036858.json:
```json
{
    "body": "1. Could you change the error from having \"openssl.spkg\" to \"openssl SPKG\" or \"openssl spkg\".  I don't like \"openssl.spkg\" since it suggests that it is a filename, but there is no such file.   \n\nI tested the spkg on OS X and it works well there. \n\n2. The repo needs to be checked in:\n\nbsd:pyopenssl-0.8.p0 was$ hg status\nM SPKG.txt\nM spkg-install\n\n3. I have to admit being slightly torn.  If one had openssl system-wide, then those headers would work fine for installing pyopenssl.  So I'm not sure we should force people to use openssl.spkg...  Or at least, it would be nice if there were some option, kind of like our SAGE_PORT=yes flag that would let users try to install an spkg damn the torpedoes, full speed ahead.   So the error could be:\n\n\"You do not have the optional openssl spkg installed, so building pyopenssl may fail.  You should either install the pyopenssl spkg, or set the environment variable SAGE_NODEPCHECKS.\"\n\nThoughts?\n\nWilliam",
    "created_at": "2008-12-30T06:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4877#issuecomment-36858",
    "user": "https://github.com/williamstein"
}
```

1. Could you change the error from having "openssl.spkg" to "openssl SPKG" or "openssl spkg".  I don't like "openssl.spkg" since it suggests that it is a filename, but there is no such file.   

I tested the spkg on OS X and it works well there. 

2. The repo needs to be checked in:

bsd:pyopenssl-0.8.p0 was$ hg status
M SPKG.txt
M spkg-install

3. I have to admit being slightly torn.  If one had openssl system-wide, then those headers would work fine for installing pyopenssl.  So I'm not sure we should force people to use openssl.spkg...  Or at least, it would be nice if there were some option, kind of like our SAGE_PORT=yes flag that would let users try to install an spkg damn the torpedoes, full speed ahead.   So the error could be:

"You do not have the optional openssl spkg installed, so building pyopenssl may fail.  You should either install the pyopenssl spkg, or set the environment variable SAGE_NODEPCHECKS."

Thoughts?

William



---

archive/issue_events_011235.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11235"
}
```



---

archive/issue_events_011236.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11236"
}
```



---

archive/issue_events_011237.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11237"
}
```



---

archive/issue_events_011238.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11238"
}
```



---

archive/issue_events_011239.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11239"
}
```



---

archive/issue_events_011240.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11240"
}
```



---

archive/issue_events_011241.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11241"
}
```



---

archive/issue_events_011242.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11242"
}
```



---

archive/issue_comments_036859.json:
```json
{
    "body": "Obsolete",
    "created_at": "2015-04-09T10:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4877#issuecomment-36859",
    "user": "https://github.com/jdemeyer"
}
```

Obsolete



---

archive/issue_events_011243.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-04-09T10:05:57Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11243"
}
```



---

archive/issue_events_011244.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-04-09T10:05:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11244"
}
```



---

archive/issue_comments_036860.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-04-09T10:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4877#issuecomment-36860",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_036861.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-09T12:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4877#issuecomment-36861",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_011245.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-04-09T12:12:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4877",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4877#event-11245"
}
```
