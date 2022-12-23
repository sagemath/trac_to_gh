# Issue 1604: more locale problems with python exposed by matplotlib

archive/issues_001604.json:
```json
{
    "body": "Assignee: was\n\nOn a linux box the function setlocale in locale.py sometimes files for some weird locals, which breaks matplotlib.   We patch the python spkg so instead of giving an error in that case, it just uses the default locale.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1604\n\n",
    "created_at": "2007-12-27T02:12:30Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "more locale problems with python exposed by matplotlib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1604",
    "user": "was"
}
```
Assignee: was

On a linux box the function setlocale in locale.py sometimes files for some weird locals, which breaks matplotlib.   We patch the python spkg so instead of giving an error in that case, it just uses the default locale.

Issue created by migration from https://trac.sagemath.org/ticket/1604





---

archive/issue_comments_010192.json:
```json
{
    "body": "The updated spkg is at \n\n  http://sagemath.org/packages/standard/python-2.5.1.p11.spkg\n\nIf you just do \"sage -upgrade\" before making the next version of Sage,\nyou'll get this fixed package.",
    "created_at": "2007-12-27T02:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1604#issuecomment-10192",
    "user": "was"
}
```

The updated spkg is at 

  http://sagemath.org/packages/standard/python-2.5.1.p11.spkg

If you just do "sage -upgrade" before making the next version of Sage,
you'll get this fixed package.



---

archive/issue_comments_010193.json:
```json
{
    "body": "The promised patch is missing.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T17:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1604#issuecomment-10193",
    "user": "mabshoff"
}
```

The promised patch is missing.

Cheers,

Michael



---

archive/issue_comments_010194.json:
```json
{
    "body": "The updated spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/python-2.5.1.p12.spkg\n\ncontains this fix.",
    "created_at": "2008-01-21T06:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1604#issuecomment-10194",
    "user": "mabshoff"
}
```

The updated spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/python-2.5.1.p12.spkg

contains this fix.



---

archive/issue_comments_010195.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T06:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1604#issuecomment-10195",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_010196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T06:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1604#issuecomment-10196",
    "user": "mabshoff"
}
```

Resolution: fixed
