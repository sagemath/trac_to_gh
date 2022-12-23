# Issue 5867: Fix gd build on FreeBSD

archive/issues_005867.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn FreeBSD, libiconv will be installed in /usr/local/lib - which is not searched by default.  Explicitly add /usr/local/lib to LDFLAGS to ensure it is correctly detected by the gd configure script.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5867\n\n",
    "created_at": "2009-04-23T06:56:11Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "Fix gd build on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5867",
    "user": "pjeremy"
}
```
Assignee: mabshoff

On FreeBSD, libiconv will be installed in /usr/local/lib - which is not searched by default.  Explicitly add /usr/local/lib to LDFLAGS to ensure it is correctly detected by the gd configure script.

Issue created by migration from https://trac.sagemath.org/ticket/5867





---

archive/issue_comments_046345.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-23T07:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46345",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_046346.json:
```json
{
    "body": "I will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46346",
    "user": "mabshoff"
}
```

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046347.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T02:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46347",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046348.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this fix is at http://sage.math.washington.edu/home/mhansen/gd-2.0.35.p2.spkg",
    "created_at": "2009-06-20T02:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46348",
    "user": "mhansen"
}
```

Looks good to me.

The spkg with this fix is at http://sage.math.washington.edu/home/mhansen/gd-2.0.35.p2.spkg



---

archive/issue_comments_046349.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-20T02:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46349",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_046350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46350",
    "user": "rlm"
}
```

Resolution: fixed
