# Issue 1550: use libecm instead of pexpect+ecm binary

archive/issues_001550.json:
```json
{
    "body": "Assignee: @williamstein\n\nI noticed the GMP-ECM interface currently calls the ecm binary through a text interface, with command line \nparameters, and gets results by parsing the output of ecm.\n\nIt would be much better and more efficient to use the C interface libecm (see the ecm.h header file, and the\necmfactor.c file distributed without GMP-ECM). Note that the C interface already returns information about the\nfound factor and the cofactor (prime, composite). Also, the libecm.a file is already compiled by SAGE.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1550\n\n",
    "created_at": "2007-12-17T13:46:48Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "use libecm instead of pexpect+ecm binary",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1550",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

I noticed the GMP-ECM interface currently calls the ecm binary through a text interface, with command line 
parameters, and gets results by parsing the output of ecm.

It would be much better and more efficient to use the C interface libecm (see the ecm.h header file, and the
ecmfactor.c file distributed without GMP-ECM). Note that the C interface already returns information about the
found factor and the cofactor (prime, composite). Also, the libecm.a file is already compiled by SAGE.

Issue created by migration from https://trac.sagemath.org/ticket/1550





---

archive/issue_comments_009857.json:
```json
{
    "body": "This is a great idea.  I thought that Yi Qiang already implemented something like this though, but evidently not (or it didn't get into sage).  I'll ping him again about this.",
    "created_at": "2008-01-21T11:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9857",
    "user": "https://github.com/williamstein"
}
```

This is a great idea.  I thought that Yi Qiang already implemented something like this though, but evidently not (or it didn't get into sage).  I'll ping him again about this.



---

archive/issue_comments_009858.json:
```json
{
    "body": "Needs serious improvement- just a minimal implementation, probably in the wrong directory...",
    "created_at": "2008-01-21T20:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9858",
    "user": "https://github.com/rlmill"
}
```

Needs serious improvement- just a minimal implementation, probably in the wrong directory...



---

archive/issue_comments_009859.json:
```json
{
    "body": "Attachment [libecm.patch](tarball://root/attachments/some-uuid/ticket1550/libecm.patch) by @rlmill created at 2008-01-21 20:56:18",
    "created_at": "2008-01-21T20:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9859",
    "user": "https://github.com/rlmill"
}
```

Attachment [libecm.patch](tarball://root/attachments/some-uuid/ticket1550/libecm.patch) by @rlmill created at 2008-01-21 20:56:18



---

archive/issue_comments_009860.json:
```json
{
    "body": "Patch on top of libecm.patch",
    "created_at": "2008-01-22T01:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9860",
    "user": "https://github.com/rlmill"
}
```

Patch on top of libecm.patch



---

archive/issue_comments_009861.json:
```json
{
    "body": "Attachment [libecm-2.patch](tarball://root/attachments/some-uuid/ticket1550/libecm-2.patch) by @zimmermann6 created at 2008-01-22 08:58:37\n\nReview: This is a great patch, which could in addition serve as example of how to interface a C\nlibrary with SAGE. Just a minor comment: the example ecmfactor(999, 0.0) always outputs (True, 27):\nfactors 2 and 3 are special within ECM. I would suggest a more difficult example, for instance\necmfactor(1022117, 10.0) which sometimes outputs (True, 1013), sometimes (True, 1009),\nsometimes (True, 1022117), or (False, None). However this might cause problems with the doctests:\nhow to check functions with non-deterministic output?",
    "created_at": "2008-01-22T08:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9861",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [libecm-2.patch](tarball://root/attachments/some-uuid/ticket1550/libecm-2.patch) by @zimmermann6 created at 2008-01-22 08:58:37

Review: This is a great patch, which could in addition serve as example of how to interface a C
library with SAGE. Just a minor comment: the example ecmfactor(999, 0.0) always outputs (True, 27):
factors 2 and 3 are special within ECM. I would suggest a more difficult example, for instance
ecmfactor(1022117, 10.0) which sometimes outputs (True, 1013), sometimes (True, 1009),
sometimes (True, 1022117), or (False, None). However this might cause problems with the doctests:
how to check functions with non-deterministic output?



---

archive/issue_comments_009862.json:
```json
{
    "body": "Here's an example (whenever 'random' occurs, the output is not checked against the expected output):\n\n\n```\nsage: ecmfactor(1022117, 10.0) # random output\n(True, 1022117)\n```\n",
    "created_at": "2008-01-22T17:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9862",
    "user": "https://github.com/rlmill"
}
```

Here's an example (whenever 'random' occurs, the output is not checked against the expected output):


```
sage: ecmfactor(1022117, 10.0) # random output
(True, 1022117)
```




---

archive/issue_comments_009863.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-23T04:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9863",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009864.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-23T04:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1550#issuecomment-9864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_events_003896.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-23T04:20:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1550",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1550#event-3896"
}
```
