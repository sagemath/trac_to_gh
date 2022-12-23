# Issue 5869: Fix libgpg-error shared library name on FreeBSD

archive/issues_005869.json:
```json
{
    "body": "Assignee: tbd\n\nEnsure that a symlink is created from libgpg-error.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5869\n\n",
    "created_at": "2009-04-23T07:04:38Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Fix libgpg-error shared library name on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5869",
    "user": "pjeremy"
}
```
Assignee: tbd

Ensure that a symlink is created from libgpg-error.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.


Issue created by migration from https://trac.sagemath.org/ticket/5869





---

archive/issue_comments_046357.json:
```json
{
    "body": "Attachment\n\nI will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46357",
    "user": "mabshoff"
}
```

Attachment

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046358.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-04-23T08:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46358",
    "user": "pjeremy"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_046359.json:
```json
{
    "body": "Changing component from algebra to freebsd.",
    "created_at": "2009-04-23T08:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46359",
    "user": "pjeremy"
}
```

Changing component from algebra to freebsd.



---

archive/issue_comments_046360.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-20T07:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46360",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_046361.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T07:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46361",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046362.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/libgpg_error-1.6.p1.spkg .",
    "created_at": "2009-06-20T07:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46362",
    "user": "mhansen"
}
```

Looks good to me.

The spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/libgpg_error-1.6.p1.spkg .



---

archive/issue_comments_046363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46363",
    "user": "rlm"
}
```

Resolution: fixed
