# Issue 4798: Update Cython to 0.10.3 (latest stable upstream)

archive/issues_004798.json:
```json
{
    "body": "Assignee: robertwb\n\nThis is from #4639:\n\n```\nInstall cython-0.10.3.spkg at http://sage.math.washington.edu/home/robertwb/cython/ ,\nwhich contains a fix to http://trac.cython.org/cython_trac/ticket/162 and I think is \nthe underlying cause here (and probably elsewhere). \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4798\n\n",
    "created_at": "2008-12-14T17:08:53Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Update Cython to 0.10.3 (latest stable upstream)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4798",
    "user": "mabshoff"
}
```
Assignee: robertwb

This is from #4639:

```
Install cython-0.10.3.spkg at http://sage.math.washington.edu/home/robertwb/cython/ ,
which contains a fix to http://trac.cython.org/cython_trac/ticket/162 and I think is 
the underlying cause here (and probably elsewhere). 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4798





---

archive/issue_comments_036380.json:
```json
{
    "body": "The spkg looks good, a -ba works fine and doctests pass. This release significantly reduces the leaks from #4639, even though some leak remains to be fixed. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T17:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4798#issuecomment-36380",
    "user": "mabshoff"
}
```

The spkg looks good, a -ba works fine and doctests pass. This release significantly reduces the leaks from #4639, even though some leak remains to be fixed. Positive review.

Cheers,

Michael



---

archive/issue_comments_036381.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T17:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4798#issuecomment-36381",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc0



---

archive/issue_comments_036382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T17:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4798#issuecomment-36382",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036383.json:
```json
{
    "body": "Note: I'd rather not consider this the final 0.10.3 until I finish tracking down that memory leak, which may involve another Cython fix. (If 3.2.2 is released, before then, this should probably be 0.10.2p0)",
    "created_at": "2008-12-15T18:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4798#issuecomment-36383",
    "user": "robertwb"
}
```

Note: I'd rather not consider this the final 0.10.3 until I finish tracking down that memory leak, which may involve another Cython fix. (If 3.2.2 is released, before then, this should probably be 0.10.2p0)



---

archive/issue_comments_036384.json:
```json
{
    "body": "Ok,\n\nI think we can live with 0.10.2.p0 in tree and will rename it in my 3.2.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T18:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4798#issuecomment-36384",
    "user": "mabshoff"
}
```

Ok,

I think we can live with 0.10.2.p0 in tree and will rename it in my 3.2.2.rc0.

Cheers,

Michael



---

archive/issue_comments_036385.json:
```json
{
    "body": "Ok, the renamed spkg is now at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/rc0/cython-0.10.2.p0.spkg\n\nand is in 3.2.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T18:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4798#issuecomment-36385",
    "user": "mabshoff"
}
```

Ok, the renamed spkg is now at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/rc0/cython-0.10.2.p0.spkg

and is in 3.2.2.rc0.

Cheers,

Michael
