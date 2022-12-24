# Issue 1978: update python-gnutls

archive/issues_001978.json:
```json
{
    "body": "Assignee: mabshoff\n\npython-gnutls needs to be updated to reflect the api changes in gnutls-2.2.1. \n\nAn experimental spkg can be found here:\n\nhttp://sage.math.washington.edu/home/yqiang/python-gnutls-1.1.4.p1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/1978\n\n",
    "created_at": "2008-01-30T04:40:18Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "update python-gnutls",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1978",
    "user": "yi"
}
```
Assignee: mabshoff

python-gnutls needs to be updated to reflect the api changes in gnutls-2.2.1. 

An experimental spkg can be found here:

http://sage.math.washington.edu/home/yqiang/python-gnutls-1.1.4.p1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/1978





---

archive/issue_comments_012821.json:
```json
{
    "body": "Changing assignee from mabshoff to yi.",
    "created_at": "2008-01-30T04:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1978#issuecomment-12821",
    "user": "yi"
}
```

Changing assignee from mabshoff to yi.



---

archive/issue_comments_012822.json:
```json
{
    "body": "There is at least one error with the spkg, namely that it needs to point to the newer gnutls libraries (ending in .23), AFAIK mabshoff fixed that already.",
    "created_at": "2008-01-30T06:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1978#issuecomment-12822",
    "user": "yi"
}
```

There is at least one error with the spkg, namely that it needs to point to the newer gnutls libraries (ending in .23), AFAIK mabshoff fixed that already.



---

archive/issue_comments_012823.json:
```json
{
    "body": "Ok, the spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc3/python_gnutls-1.1.4.p2.spkg\n\nshould fix all known issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1978#issuecomment-12823",
    "user": "mabshoff"
}
```

Ok, the spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc3/python_gnutls-1.1.4.p2.spkg

should fix all known issue.

Cheers,

Michael



---

archive/issue_comments_012824.json:
```json
{
    "body": "There is also an updated gnutls.spkg that makes sure the old `*[dylib|so].13.*` are gone:\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc3/gnutls-2.2.1.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T07:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1978#issuecomment-12824",
    "user": "mabshoff"
}
```

There is also an updated gnutls.spkg that makes sure the old `*[dylib|so].13.*` are gone:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc3/gnutls-2.2.1.p0.spkg

Cheers,

Michael



---

archive/issue_comments_012825.json:
```json
{
    "body": "Builds fine on OSX and start with `-notebook` as well as `-inotebook`. \n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T08:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1978#issuecomment-12825",
    "user": "mabshoff"
}
```

Builds fine on OSX and start with `-notebook` as well as `-inotebook`. 

Cheers,

Michael



---

archive/issue_comments_012826.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T09:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1978#issuecomment-12826",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012827.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc3. This ticket should be reopened if any problems pop up.",
    "created_at": "2008-01-30T09:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1978#issuecomment-12827",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc3. This ticket should be reopened if any problems pop up.
