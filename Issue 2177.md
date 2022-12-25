# Issue 2177: [with patch; needs review] debianized jmol spkg

archive/issues_002177.json:
```json
{
    "body": "Assignee: @timabbott\n\nFor some reason the jmol directory shipped with SAGE does not contain the doc/ directory, which causes it to fail to build on Debian (or anything else, I'm pretty sure).  The current spkg-install script just copies the pre-built jmol jars, but presumably it'd be better to build our own (certainly Debian will want me to do this).\n\nThe doc/ directory is not large, so I'm not sure why it is missing, so I've obtained a copy of the doc directory from the jmol-11.5.2 upstream.  \n\nI also move the \"jmol/\" directory to \"src/\" for compliance with our new spkg format standards.\n\nI'll post a new SPKG later tonight.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2177\n\n",
    "created_at": "2008-02-16T04:33:51Z",
    "labels": [
        "component: debian-package",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch; needs review] debianized jmol spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2177",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

For some reason the jmol directory shipped with SAGE does not contain the doc/ directory, which causes it to fail to build on Debian (or anything else, I'm pretty sure).  The current spkg-install script just copies the pre-built jmol jars, but presumably it'd be better to build our own (certainly Debian will want me to do this).

The doc/ directory is not large, so I'm not sure why it is missing, so I've obtained a copy of the doc directory from the jmol-11.5.2 upstream.  

I also move the "jmol/" directory to "src/" for compliance with our new spkg format standards.

I'll post a new SPKG later tonight.


Issue created by migration from https://trac.sagemath.org/ticket/2177





---

archive/issue_comments_014259.json:
```json
{
    "body": ">  The current spkg-install script just copies the pre-built jmol \n> jars, but presumably it'd be better to build our own (certainly\n> Debian will want me to do this).\n\nWe also *VERY MUCH* want easy-to-build-from source java code\nfor this package. Note that there is a jmol optional src package\nhere:\n\n   http://sagemath.org/packages/optional/",
    "created_at": "2008-02-16T06:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2177#issuecomment-14259",
    "user": "https://github.com/williamstein"
}
```

>  The current spkg-install script just copies the pre-built jmol 
> jars, but presumably it'd be better to build our own (certainly
> Debian will want me to do this).

We also *VERY MUCH* want easy-to-build-from source java code
for this package. Note that there is a jmol optional src package
here:

   http://sagemath.org/packages/optional/



---

archive/issue_comments_014260.json:
```json
{
    "body": "JMol itself builds from source just fine if you install Sun Java (currently in Debian non-free) and ant.  It looks like the optional spkg has a bunch of dependencies that are shipped with the jmol spkg; so I guess that's what we're missing?  \n\nThe new spkg with Debian build support is available here:\nhttp://sage.math.washington.edu/home/tabbott/jmol-11.5.2.p1.spkg",
    "created_at": "2008-02-16T06:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2177#issuecomment-14260",
    "user": "https://github.com/timabbott"
}
```

JMol itself builds from source just fine if you install Sun Java (currently in Debian non-free) and ant.  It looks like the optional spkg has a bunch of dependencies that are shipped with the jmol spkg; so I guess that's what we're missing?  

The new spkg with Debian build support is available here:
http://sage.math.washington.edu/home/tabbott/jmol-11.5.2.p1.spkg



---

archive/issue_comments_014261.json:
```json
{
    "body": "I added a changelog entry to SPKG.txt, otherwise positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T17:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2177#issuecomment-14261",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I added a changelog entry to SPKG.txt, otherwise positive review.

Cheers,

Michael



---

archive/issue_comments_014262.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T17:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2177#issuecomment-14262",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014263.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-16T17:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2177#issuecomment-14263",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_events_002344.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-16T17:53:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2177",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2177#event-2344"
}
```



---

archive/issue_comments_014264.json:
```json
{
    "body": "Arrg, it was actually merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-16T18:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2177#issuecomment-14264",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Arrg, it was actually merged in Sage 2.10.2.alpha1
