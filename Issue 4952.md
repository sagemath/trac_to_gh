# Issue 4952: modulus issue in sage/rings/finite_field_ntl_gf2e.pyx

archive/issues_004952.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following was introduced by #4934:\n\n```\ncleo (ia64-Linux-rhel5-clisp-2.41)\n\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.2.3-ia64-Linux-rhel5-clisp-2.41/devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\",\nline 171:\n    sage: k.modulus()\nExpected:\n    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1\nGot:\n    x^17 + x^3 + 1\n**********************************************************************\n\neno (x86_64-Linux-fc)\n\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.2.3-x86_64-Linux-fc/devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\",\nline 171:\n    sage: k.modulus()\nExpected:\n    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1\nGot:\n    x^17 + x^3 + 1\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4952\n\n",
    "created_at": "2009-01-07T17:08:47Z",
    "labels": [
        "number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "modulus issue in sage/rings/finite_field_ntl_gf2e.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4952",
    "user": "mabshoff"
}
```
Assignee: @williamstein

The following was introduced by #4934:

```
cleo (ia64-Linux-rhel5-clisp-2.41)

**********************************************************************
File "/home/mariah/sage/sage-3.2.3-ia64-Linux-rhel5-clisp-2.41/devel/sage/sage/rings/finite_field_ntl_gf2e.pyx",
line 171:
    sage: k.modulus()
Expected:
    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
Got:
    x^17 + x^3 + 1
**********************************************************************

eno (x86_64-Linux-fc)

**********************************************************************
File "/home/mariah/sage/sage-3.2.3-x86_64-Linux-fc/devel/sage/sage/rings/finite_field_ntl_gf2e.pyx",
line 171:
    sage: k.modulus()
Expected:
    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
Got:
    x^17 + x^3 + 1
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4952





---

archive/issue_comments_037660.json:
```json
{
    "body": "I am no longer seeing this with the system compiler in 3.3.alpha6, but will try with gcc 4.3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T05:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4952#issuecomment-37660",
    "user": "mabshoff"
}
```

I am no longer seeing this with the system compiler in 3.3.alpha6, but will try with gcc 4.3.3.

Cheers,

Michael



---

archive/issue_comments_037661.json:
```json
{
    "body": "The issue has been fixed (or at least no longer happens) with Sage 3.3.alpha6 with the system gcc as well as gcc 4.3.3:\n\n```\nmabshoff@menas:~/build-3.3.alpha6/sage-3.3.alpha6-menas-gcc433> ./sage -t -long devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\nsage -t -long \"devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\"\n\t [5.2 s]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T07:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4952#issuecomment-37661",
    "user": "mabshoff"
}
```

The issue has been fixed (or at least no longer happens) with Sage 3.3.alpha6 with the system gcc as well as gcc 4.3.3:

```
mabshoff@menas:~/build-3.3.alpha6/sage-3.3.alpha6-menas-gcc433> ./sage -t -long devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
sage -t -long "devel/sage/sage/rings/finite_field_ntl_gf2e.pyx"
	 [5.2 s]
```


Cheers,

Michael



---

archive/issue_comments_037662.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-10T07:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4952#issuecomment-37662",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037663.json:
```json
{
    "body": "Hmm, to be 100% save I will also test eno and cleo with 3.3.rc0 using gcc 4.3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T07:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4952#issuecomment-37663",
    "user": "mabshoff"
}
```

Hmm, to be 100% save I will also test eno and cleo with 3.3.rc0 using gcc 4.3.3.

Cheers,

Michael
