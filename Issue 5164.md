# Issue 5164: NTL.spkg: Set SHAREDFALGS to -fnocommon on Darwin

archive/issues_005164.json:
```json
{
    "body": "Assignee: mabshoff\n\nIn #5161 I removed some global SHAREDFLAGS setting from sage-env. NTL on Darwin needs -fnocommon to work around some linker stupidity.\n\nspkg coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5164\n\n",
    "created_at": "2009-02-03T05:00:34Z",
    "labels": [
        "porting",
        "blocker",
        "bug"
    ],
    "title": "NTL.spkg: Set SHAREDFALGS to -fnocommon on Darwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5164",
    "user": "mabshoff"
}
```
Assignee: mabshoff

In #5161 I removed some global SHAREDFLAGS setting from sage-env. NTL on Darwin needs -fnocommon to work around some linker stupidity.

spkg coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5164





---

archive/issue_comments_039574.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-03T05:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39574",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039575.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha5/ntl-5.4.2.p6.spkg\n\nfixes the problem.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T18:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39575",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha5/ntl-5.4.2.p6.spkg

fixes the problem.

Cheers,

Michael



---

archive/issue_comments_039576.json:
```json
{
    "body": "No issues with building on other OSes Fedora 9, Fedora 10 and Ubuntu 8.10, 32 bits\n\nJaap",
    "created_at": "2009-02-03T19:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39576",
    "user": "jsp"
}
```

No issues with building on other OSes Fedora 9, Fedora 10 and Ubuntu 8.10, 32 bits

Jaap



---

archive/issue_comments_039577.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T19:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39577",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_comments_039578.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-03T19:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39578",
    "user": "mabshoff"
}
```

Resolution: fixed
