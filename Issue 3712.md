# Issue 3712: clisp+nohup eats ones disc

archive/issues_003712.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nABORT          :R364    Abort debug loop\nABORT          :R365    Abort debug loop\nABORT          :R366    Abort debug loop\nABORT          :R367    Abort debug loop\nABORT          :R368    Abort debug loop\nABORT          :R369    Abort debug loop\nABORT          :R370    Abort debug loop\nABORT          :R371    Abort debug loop\nABORT        tee: write e\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3712\n\n",
    "created_at": "2008-07-23T13:17:01Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "clisp+nohup eats ones disc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3712",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
ABORT          :R364    Abort debug loop
ABORT          :R365    Abort debug loop
ABORT          :R366    Abort debug loop
ABORT          :R367    Abort debug loop
ABORT          :R368    Abort debug loop
ABORT          :R369    Abort debug loop
ABORT          :R370    Abort debug loop
ABORT          :R371    Abort debug loop
ABORT        tee: write e
```


Issue created by migration from https://trac.sagemath.org/ticket/3712





---

archive/issue_comments_026350.json:
```json
{
    "body": "This is likely fixed by putting William's workaround in back into spkg-install. Nils Bruin hot a likely related issue on OSX 10.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-25T10:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3712#issuecomment-26350",
    "user": "mabshoff"
}
```

This is likely fixed by putting William's workaround in back into spkg-install. Nils Bruin hot a likely related issue on OSX 10.4.

Cheers,

Michael



---

archive/issue_comments_026351.json:
```json
{
    "body": "The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/clisp-2.46.p6.spkg\n\nreintroduces the old fix from the previous spkg. Notice that this spkg also fixes #3715.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T16:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3712#issuecomment-26351",
    "user": "mabshoff"
}
```

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/clisp-2.46.p6.spkg

reintroduces the old fix from the previous spkg. Notice that this spkg also fixes #3715.

Cheers,

Michael



---

archive/issue_comments_026352.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-29T16:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3712#issuecomment-26352",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-29T16:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3712#issuecomment-26353",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026354.json:
```json
{
    "body": "Merged in Sage 3.0.6.final",
    "created_at": "2008-07-29T16:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3712#issuecomment-26354",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.final
