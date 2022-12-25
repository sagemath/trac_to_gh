# Issue 8445: sh: kpsewhich: not found -  Sage 4.3.4.alpha0 on Solaris

archive/issues_008445.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  mvngu @jaapspies @jhpalmieri @qed777 sage-combinat\n\n## Background\nAfter downloading the 4.3.4.alpha0.tar I applied some patches necessary to get this to build on Solaris 10 (SPARC). Namely: \n\n === Patches installed to allow Sage to build properly === \n* #7867 A patch for Python which allows Python modules to be built properly. \n* #8440 A patch for Python to allow the _multiprocessing module to build. \n\n === Patches installed to allow most all doctests to pass in 4.3.3 (a few fail in 4.3.4.alpha0 ===\n\n* #8374 Numerical noise in sage/symbolic/constants_c.pyx\n* #8375 Numerical noise in sage/symbolic/pynac.pyx\n* #8391 Change 'top' to 'prstat' on Solaris, othewise lots of doctests time out.\n* #8408 Update sqlite to the latest version (otherwise #8397, #8398, #8399, #8400 and #8401 all fail). \n\n == The problems == \n\nRunning the long doctests I see:\n\n\n```\nsage -t  -long \"devel/sage/sage/categories/finite_semigroups.py\"\nsh: kpsewhich: not found\nsh: kpsewhich: not found\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/finite_semigroups.py\", line 232:\n    sage: sorted(S.j_transversal_of_idempotents())\nExpected:\n    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']\nGot:\n    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']\n```\n\n\nSo there are two problems. \n* kpsewhich: not found \n* doctest failure\n\nBut #8180 was supposed to fix this kpsewhich issue, so I believe the fix is not working fully.  \n\nI'll create a ticket for the test failure if needed. But I believe I see this mentioned on sage-devel, so it looks like I'm not the only one with this issue. So a ticket for it probably exists already.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8445\n\n",
    "created_at": "2010-03-05T13:42:44Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "sh: kpsewhich: not found -  Sage 4.3.4.alpha0 on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8445",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  mvngu @jaapspies @jhpalmieri @qed777 sage-combinat

## Background
After downloading the 4.3.4.alpha0.tar I applied some patches necessary to get this to build on Solaris 10 (SPARC). Namely: 

 === Patches installed to allow Sage to build properly === 
* #7867 A patch for Python which allows Python modules to be built properly. 
* #8440 A patch for Python to allow the _multiprocessing module to build. 

 === Patches installed to allow most all doctests to pass in 4.3.3 (a few fail in 4.3.4.alpha0 ===

* #8374 Numerical noise in sage/symbolic/constants_c.pyx
* #8375 Numerical noise in sage/symbolic/pynac.pyx
* #8391 Change 'top' to 'prstat' on Solaris, othewise lots of doctests time out.
* #8408 Update sqlite to the latest version (otherwise #8397, #8398, #8399, #8400 and #8401 all fail). 

 == The problems == 

Running the long doctests I see:


```
sage -t  -long "devel/sage/sage/categories/finite_semigroups.py"
sh: kpsewhich: not found
sh: kpsewhich: not found
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/finite_semigroups.py", line 232:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
```


So there are two problems. 
* kpsewhich: not found 
* doctest failure

But #8180 was supposed to fix this kpsewhich issue, so I believe the fix is not working fully.  

I'll create a ticket for the test failure if needed. But I believe I see this mentioned on sage-devel, so it looks like I'm not the only one with this issue. So a ticket for it probably exists already.

Issue created by migration from https://trac.sagemath.org/ticket/8445





---

archive/issue_comments_075798.json:
```json
{
    "body": "The sage-combinat team might be interested in this ticket.",
    "created_at": "2010-03-05T13:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The sage-combinat team might be interested in this ticket.



---

archive/issue_comments_075799.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-05T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75799",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075800.json:
```json
{
    "body": "Here's a patch.  It's hard for me to doctest it on Solaris: I think the only machine I have access to is t2.math, but there isn't enough room in /scratch for me to install Sage.  So please test it out.  It works for me on several other machines, and on t2, if I `load` a file containing the relevant code, that works as well.\n\nThe patch also reformats the warning messages that get printed if tkz-berge.sty (etc.) are not present.",
    "created_at": "2010-03-05T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75800",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch.  It's hard for me to doctest it on Solaris: I think the only machine I have access to is t2.math, but there isn't enough room in /scratch for me to install Sage.  So please test it out.  It works for me on several other machines, and on t2, if I `load` a file containing the relevant code, that works as well.

The patch also reformats the warning messages that get printed if tkz-berge.sty (etc.) are not present.



---

archive/issue_comments_075801.json:
```json
{
    "body": "Attachment [trac_8445-kpsewhich-solaris.patch](tarball://root/attachments/some-uuid/ticket8445/trac_8445-kpsewhich-solaris.patch) by drkirkby created at 2010-03-06 16:12:04\n\nThank's John,\n\nI will test this, but it might take me a few days, as I have a very busy schedule this week. \n\nFortunately this is not a critical patch. \n\nDave",
    "created_at": "2010-03-06T16:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75801",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [trac_8445-kpsewhich-solaris.patch](tarball://root/attachments/some-uuid/ticket8445/trac_8445-kpsewhich-solaris.patch) by drkirkby created at 2010-03-06 16:12:04

Thank's John,

I will test this, but it might take me a few days, as I have a very busy schedule this week. 

Fortunately this is not a critical patch. 

Dave



---

archive/issue_comments_075802.json:
```json
{
    "body": "Changing assignee from drkirkby to @jhpalmieri.",
    "created_at": "2010-03-06T21:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75802",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from drkirkby to @jhpalmieri.



---

archive/issue_comments_075803.json:
```json
{
    "body": "John, \n\nI've tested this on Solaris, and find no more \"kpsewhich\" problems. So from my point of view it is working. \n\nHowever, I don't feel comfortable giving this a positive review, as I don't understand much of the code. \n\nPerhaps one of the others cc'ed on the ticket can look over this, keeping in mind that it does solve the problem I reported. \n\nDave",
    "created_at": "2010-03-06T21:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75803",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

John, 

I've tested this on Solaris, and find no more "kpsewhich" problems. So from my point of view it is working. 

However, I don't feel comfortable giving this a positive review, as I don't understand much of the code. 

Perhaps one of the others cc'ed on the ticket can look over this, keeping in mind that it does solve the problem I reported. 

Dave



---

archive/issue_comments_075804.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T23:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75804",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075805.json:
```json
{
    "body": "This change looks good to me.",
    "created_at": "2010-03-06T23:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75805",
    "user": "https://github.com/mwhansen"
}
```

This change looks good to me.



---

archive/issue_comments_075806.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-07T00:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8445#issuecomment-75806",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_020253.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-07T00:01:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8445",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8445#event-20253"
}
```
