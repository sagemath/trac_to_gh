# Issue 5481: devel/doc/output/* should be filtered from the list of files to doctest

archive/issues_005481.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mhansen\n\nThere can be many rst files under devel/doc/output - those should be filtered from the list of files to doctest since they are duplicate doctests from the main Sage library in many cases.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5481\n\n",
    "created_at": "2009-03-11T06:31:10Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "devel/doc/output/* should be filtered from the list of files to doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5481",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  mhansen

There can be many rst files under devel/doc/output - those should be filtered from the list of files to doctest since they are duplicate doctests from the main Sage library in many cases.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5481





---

archive/issue_comments_042524.json:
```json
{
    "body": "Has this been fixed?  The file sage-maketest looks good to me already.",
    "created_at": "2009-06-09T22:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42524",
    "user": "jhpalmieri"
}
```

Has this been fixed?  The file sage-maketest looks good to me already.



---

archive/issue_comments_042525.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42525",
    "user": "was"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_042526.json:
```json
{
    "body": "Maybe sage-ptest needs changing.  I'm still trying to figure out what the issue is here.",
    "created_at": "2009-06-16T03:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42526",
    "user": "jhpalmieri"
}
```

Maybe sage-ptest needs changing.  I'm still trying to figure out what the issue is here.



---

archive/issue_comments_042527.json:
```json
{
    "body": "Attachment [trac_5481_scripts.patch](tarball://root/attachments/some-uuid/ticket5481/trac_5481_scripts.patch) by jhpalmieri created at 2009-06-16 03:28:03\n\nHere's a patch.  (The first change -- deleting all.py and __init__.py -- comes from #6108.)",
    "created_at": "2009-06-16T03:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42527",
    "user": "jhpalmieri"
}
```

Attachment [trac_5481_scripts.patch](tarball://root/attachments/some-uuid/ticket5481/trac_5481_scripts.patch) by jhpalmieri created at 2009-06-16 03:28:03

Here's a patch.  (The first change -- deleting all.py and __init__.py -- comes from #6108.)



---

archive/issue_comments_042528.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-20T01:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42528",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_042529.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T01:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42529",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042530.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-20T01:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42530",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_042531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42531",
    "user": "boothby"
}
```

Resolution: fixed
