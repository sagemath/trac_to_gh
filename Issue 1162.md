# Issue 1162: [with patch] fix issues in RealField <-> RQDF conversions

archive/issues_001162.json:
```json
{
    "body": "Assignee: jkantor\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1162\n\n",
    "created_at": "2007-11-13T00:04:53Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "title": "[with patch] fix issues in RealField <-> RQDF conversions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1162",
    "user": "zimmerma"
}
```
Assignee: jkantor



Issue created by migration from https://trac.sagemath.org/ticket/1162





---

archive/issue_comments_007108.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-13T00:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7108",
    "user": "zimmerma"
}
```

Attachment



---

archive/issue_comments_007109.json:
```json
{
    "body": "The first chunk of the patch (patching polynomial_element.pyx) makes doctesting polynomial_element.pyx fail for me (on 32-bit x86 Linux).  (Plus, the first chunk seems unrelated to the other chunks, and to the bug report.  Maybe it was included by accident?)\n\nThe other two chunks look good to me.",
    "created_at": "2007-11-15T03:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7109",
    "user": "cwitty"
}
```

The first chunk of the patch (patching polynomial_element.pyx) makes doctesting polynomial_element.pyx fail for me (on 32-bit x86 Linux).  (Plus, the first chunk seems unrelated to the other chunks, and to the bug report.  Maybe it was included by accident?)

The other two chunks look good to me.



---

archive/issue_comments_007110.json:
```json
{
    "body": "Yes the first chunk was included by accident and is unrelated. About this first chunk, I do not understand why\nroots() gives different results on different architectures. It shouldn't if mpfr is used inside.",
    "created_at": "2007-11-22T08:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7110",
    "user": "zimmerma"
}
```

Yes the first chunk was included by accident and is unrelated. About this first chunk, I do not understand why
roots() gives different results on different architectures. It shouldn't if mpfr is used inside.



---

archive/issue_comments_007111.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-02T00:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7111",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_007112.json:
```json
{
    "body": "I've added my own patch for these issues.  It's based on Paul Zimmerman's patch (and includes the two chunks that I said \"look good\", above); but it also fixes issues with converting to complex, and adds some more doctests.",
    "created_at": "2007-12-02T00:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7112",
    "user": "cwitty"
}
```

I've added my own patch for these issues.  It's based on Paul Zimmerman's patch (and includes the two chunks that I said "look good", above); but it also fixes issues with converting to complex, and adds some more doctests.



---

archive/issue_comments_007113.json:
```json
{
    "body": "\n```\nwas-1162: #1162 is ready.\n[03:27am] was-1162: But it is hard to apply.\n[03:27am] mabshoff: ok\n[03:27am] was-1162: Basically apply each patch, ignore all the failed hunks.\n[03:28am] mabshoff: arrg.\n[03:28am] mabshoff: will do.\n[03:28am] was-1162: then go into real_mpfr.pyx and manually delete\n[03:28am] was-1162: 658        elif hasattr(x, '_mpfr_'):\n[03:28am] was-1162: 659            return x._mpfr_(self)\n[03:28am] was-1162: It's scary--\n[03:28am] mabshoff: +1\n[03:28am] was-1162: but *all* that is being done is that the rounding mode is being changed from Z to N in one place.\n[03:28am] was-1162: and some doctests are being changed to reflect this.\n[03:28am] mabshoff: ok\n```\n",
    "created_at": "2007-12-15T11:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7113",
    "user": "was"
}
```


```
was-1162: #1162 is ready.
[03:27am] was-1162: But it is hard to apply.
[03:27am] mabshoff: ok
[03:27am] was-1162: Basically apply each patch, ignore all the failed hunks.
[03:28am] mabshoff: arrg.
[03:28am] mabshoff: will do.
[03:28am] was-1162: then go into real_mpfr.pyx and manually delete
[03:28am] was-1162: 658        elif hasattr(x, '_mpfr_'):
[03:28am] was-1162: 659            return x._mpfr_(self)
[03:28am] was-1162: It's scary--
[03:28am] mabshoff: +1
[03:28am] was-1162: but *all* that is being done is that the rounding mode is being changed from Z to N in one place.
[03:28am] was-1162: and some doctests are being changed to reflect this.
[03:28am] mabshoff: ok
```




---

archive/issue_comments_007114.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7114",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_007115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T11:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1162#issuecomment-7115",
    "user": "mabshoff"
}
```

Resolution: fixed
