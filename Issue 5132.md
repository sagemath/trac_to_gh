# Issue 5132: [with patch, needs review] real numbers don't support __mod__

archive/issues_005132.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: 10.0 % 2r\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/burcin/.sage/temp/karr/24765/_home_burcin__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\nTypeError: unsupported operand type(s) for %: 'sage.rings.real_mpfr.RealLiteral' and 'int'\n```\n\n\nA quick look through sage/rings/real_mpfr.pyx reveals that there is no `__mod__` method defined.\n\nMPFR documentation here:\n\nhttp://www.mpfr.org/mpfr-current/mpfr.html#Integer-Related-Functions\n\nsuggests that one of `mpfr_fmod()` or `mpfr_remainder()` should be used, depending on the desired rounding properties. Since I live blissfully in the exact arithmetic world, I have no idea which one is more suitable for Sage.\n\nNevertheless, a patch that uses `mpfr_remainder()` is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5132\n\n",
    "created_at": "2009-01-30T01:01:03Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] real numbers don't support __mod__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5132",
    "user": "https://github.com/burcin"
}
```
Assignee: somebody


```
sage: 10.0 % 2r
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/burcin/.sage/temp/karr/24765/_home_burcin__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

TypeError: unsupported operand type(s) for %: 'sage.rings.real_mpfr.RealLiteral' and 'int'
```


A quick look through sage/rings/real_mpfr.pyx reveals that there is no `__mod__` method defined.

MPFR documentation here:

http://www.mpfr.org/mpfr-current/mpfr.html#Integer-Related-Functions

suggests that one of `mpfr_fmod()` or `mpfr_remainder()` should be used, depending on the desired rounding properties. Since I live blissfully in the exact arithmetic world, I have no idea which one is more suitable for Sage.

Nevertheless, a patch that uses `mpfr_remainder()` is attached.

Issue created by migration from https://trac.sagemath.org/ticket/5132





---

archive/issue_comments_039165.json:
```json
{
    "body": "Attachment [trac_5132-mpfr_mod.patch](tarball://root/attachments/some-uuid/ticket5132/trac_5132-mpfr_mod.patch) by @zimmermann6 created at 2009-02-01 21:24:52\n\nThis is a duplicate of #825.",
    "created_at": "2009-02-01T21:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5132#issuecomment-39165",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_5132-mpfr_mod.patch](tarball://root/attachments/some-uuid/ticket5132/trac_5132-mpfr_mod.patch) by @zimmermann6 created at 2009-02-01 21:24:52

This is a duplicate of #825.



---

archive/issue_comments_039166.json:
```json
{
    "body": "Looks good to me.  This also fixes the broken example reported at #825.",
    "created_at": "2009-02-02T07:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5132#issuecomment-39166",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  This also fixes the broken example reported at #825.



---

archive/issue_events_011897.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-02T07:27:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5132",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5132#event-11897"
}
```



---

archive/issue_comments_039167.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T07:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5132#issuecomment-39167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_039168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T07:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5132#issuecomment-39168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
