# Issue 2772: Update Singular to 3-0-4-2

archive/issues_002772.json:
```json
{
    "body": "Assignee: malb\n\nThis version has GCC 4.3 support.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2772\n\n",
    "created_at": "2008-04-02T15:33:08Z",
    "labels": [
        "commutative algebra",
        "blocker",
        "enhancement"
    ],
    "title": "Update Singular to 3-0-4-2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2772",
    "user": "malb"
}
```
Assignee: malb

This version has GCC 4.3 support.

Issue created by migration from https://trac.sagemath.org/ticket/2772





---

archive/issue_comments_019052.json:
```json
{
    "body": "A new SPKG is available at:\n\n  http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080404.spkg\n\nHowever, this is not ready for inclusion yet, because of some problem with the GCD. It works correctly from Singular but not correctly via the libSingular interface. I'm working on it.",
    "created_at": "2008-04-04T13:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19052",
    "user": "malb"
}
```

A new SPKG is available at:

  http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080404.spkg

However, this is not ready for inclusion yet, because of some problem with the GCD. It works correctly from Singular but not correctly via the libSingular interface. I'm working on it.



---

archive/issue_comments_019053.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-05T16:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19053",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_019054.json:
```json
{
    "body": "A new SPKG is available at:\n\n   http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080405.spkg\n\nwhich in combination with the attached patch should pass all doctests.",
    "created_at": "2008-04-05T16:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19054",
    "user": "malb"
}
```

A new SPKG is available at:

   http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080405.spkg

which in combination with the attached patch should pass all doctests.



---

archive/issue_comments_019055.json:
```json
{
    "body": "The patch applies cleanly, the spkg compiles cleanly for me on OSX and Linux. Doctests pass. I did find two small issues:\n\n* I removed spkg-install.orig from the spkg\n* I also removed the comment that SPKG.txt is deprecated from that file.\n\nIn total: positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T02:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19055",
    "user": "mabshoff"
}
```

The patch applies cleanly, the spkg compiles cleanly for me on OSX and Linux. Doctests pass. I did find two small issues:

* I removed spkg-install.orig from the spkg
* I also removed the comment that SPKG.txt is deprecated from that file.

In total: positive review.

Cheers,

Michael



---

archive/issue_comments_019056.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T02:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19056",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019057.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T02:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19057",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
