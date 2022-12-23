# Issue 5309: mark some doctests in misc/package.py #optional - internet

archive/issues_005309.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t -long \"devel/sage/sage/misc/package.py\"\n**********************************************************************\nFile \"/Users/wstein/build/build/sage-3.3.rc2/devel/sage/sage/misc/package.py\", line 50:\n    sage: sage.misc.package.install_all_optional_packages(dry_run=True)\nExpected:\n    Installing ...\n    []\nGot:\n    Using SAGE Server http://www.sagemath.org//packages\n    http://www.sagemath.org//packages/optional/list --> /Users/wstein/build/build/sage-3.3.rc2/tmp/list\n    [Errno socket error] (8, 'nodename nor servname provided, or not known')\n\nSOLUTION: This was caused by the networking being down during this test.   These tests should be marked # optional, since doctesting sage *must* not require an external network connection.  \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5309\n\n",
    "created_at": "2009-02-18T19:06:11Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "mark some doctests in misc/package.py #optional - internet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5309",
    "user": "was"
}
```
Assignee: mabshoff


```
sage -t -long "devel/sage/sage/misc/package.py"
**********************************************************************
File "/Users/wstein/build/build/sage-3.3.rc2/devel/sage/sage/misc/package.py", line 50:
    sage: sage.misc.package.install_all_optional_packages(dry_run=True)
Expected:
    Installing ...
    []
Got:
    Using SAGE Server http://www.sagemath.org//packages
    http://www.sagemath.org//packages/optional/list --> /Users/wstein/build/build/sage-3.3.rc2/tmp/list
    [Errno socket error] (8, 'nodename nor servname provided, or not known')

SOLUTION: This was caused by the networking being down during this test.   These tests should be marked # optional, since doctesting sage *must* not require an external network connection.  
```


Issue created by migration from https://trac.sagemath.org/ticket/5309





---

archive/issue_comments_040859.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-20T04:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5309#issuecomment-40859",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_040860.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T05:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5309#issuecomment-40860",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_040861.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T05:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5309#issuecomment-40861",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040862.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T05:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5309#issuecomment-40862",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael
