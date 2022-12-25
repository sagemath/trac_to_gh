# Issue 5393: pycrypto 2.0.1: integrate fix for http://www.securityfocus.com/bid/33674/info (security)

archive/issues_005393.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nPyCrypto ARC2 Module Buffer Overflow Vulnerability\n\nPyCrypto (Python Cryptography Toolkit) is prone to a buffer-overflow vulnerability because it fails to adequately verify user-supplied input.\n\nSuccessful exploits may allow attackers to execute arbitrary code in the context of applications using the vulnerable module. Failed attempts may lead to a denial-of-service condition.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5393\n\n",
    "created_at": "2009-02-27T16:38:36Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "pycrypto 2.0.1: integrate fix for http://www.securityfocus.com/bid/33674/info (security)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
PyCrypto ARC2 Module Buffer Overflow Vulnerability

PyCrypto (Python Cryptography Toolkit) is prone to a buffer-overflow vulnerability because it fails to adequately verify user-supplied input.

Successful exploits may allow attackers to execute arbitrary code in the context of applications using the vulnerable module. Failed attempts may lead to a denial-of-service condition.
```


Issue created by migration from https://trac.sagemath.org/ticket/5393





---

archive/issue_comments_041454.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-27T16:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5393#issuecomment-41454",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041455.json:
```json
{
    "body": "The commit to be applied can be found at \n\nhttp://gitweb.pycrypto.org/?p=crypto/pycrypto-2.x.git;a=commitdiff;h=d1c4875e1f220652fe7ff8358f56dee3b2aba31b\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T16:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5393#issuecomment-41455",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The commit to be applied can be found at 

http://gitweb.pycrypto.org/?p=crypto/pycrypto-2.x.git;a=commitdiff;h=d1c4875e1f220652fe7ff8358f56dee3b2aba31b

Cheers,

Michael



---

archive/issue_comments_041456.json:
```json
{
    "body": "The spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/rc0/pycrypto-2.0.1.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-03-03T00:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5393#issuecomment-41456",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/rc0/pycrypto-2.0.1.p3.spkg

Cheers,

Michael



---

archive/issue_comments_041457.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-03T00:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5393#issuecomment-41457",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041458.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-03T00:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5393#issuecomment-41458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
