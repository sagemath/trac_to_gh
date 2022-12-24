# Issue 4197: weird ntl finite field modulus caching bug.

archive/issues_004197.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb\n\nI thought we slayed this, but on eno we have this weird failure:\n\n\n```\nsage -t -long devel/sage/sage/rings/finite_field_ntl_gf2e.pyx**********************************************************************\nFile \"/home/wstein/eno/build/sage-3.1.3.alpha1/tmp/finite_field_ntl_gf2e.py\",\nline 167:\n   sage: k.modulus()\nExpected:\n   x^1024 + x^19 + x^6 + x + 1\nGot:\n   x^1024 + x^16 + x^15 + x^14 + x^13 + x^11 + x^10 + x^9 + x^7 + x^6 + x^2\n**********************************************************************\n1 items had failures:\n  1 of  10 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file\n/home/wstein/eno/build/sage-3.1.3.alpha1/tmp/.doctest_finite_field_ntl_gf2e.py\n        [1.2 s]\n\nThis machine is:\n[wstein@eno eno]$ cat /etc/issue\nFedora release 8 (Werewolf)\nKernel \\r on an \\m\n\n[wstein@eno eno]$ uname -a\nLinux eno 2.6.24.5-85.fc8 #1 SMP Sat Apr 19 11:18:09 EDT 2008 x86_64\nx86_64 x86_64 GNU/Linux\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4197\n\n",
    "created_at": "2008-09-25T23:33:46Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "weird ntl finite field modulus caching bug.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4197",
    "user": "@williamstein"
}
```
Assignee: somebody

CC:  @robertwb

I thought we slayed this, but on eno we have this weird failure:


```
sage -t -long devel/sage/sage/rings/finite_field_ntl_gf2e.pyx**********************************************************************
File "/home/wstein/eno/build/sage-3.1.3.alpha1/tmp/finite_field_ntl_gf2e.py",
line 167:
   sage: k.modulus()
Expected:
   x^1024 + x^19 + x^6 + x + 1
Got:
   x^1024 + x^16 + x^15 + x^14 + x^13 + x^11 + x^10 + x^9 + x^7 + x^6 + x^2
**********************************************************************
1 items had failures:
  1 of  10 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file
/home/wstein/eno/build/sage-3.1.3.alpha1/tmp/.doctest_finite_field_ntl_gf2e.py
        [1.2 s]

This machine is:
[wstein@eno eno]$ cat /etc/issue
Fedora release 8 (Werewolf)
Kernel \r on an \m

[wstein@eno eno]$ uname -a
Linux eno 2.6.24.5-85.fc8 #1 SMP Sat Apr 19 11:18:09 EDT 2008 x86_64
x86_64 x86_64 GNU/Linux
```


Issue created by migration from https://trac.sagemath.org/ticket/4197





---

archive/issue_comments_030463.json:
```json
{
    "body": "Attachment [trac-4197.patch](tarball://root/attachments/some-uuid/ticket4197/trac-4197.patch) by @williamstein created at 2008-09-25 23:36:52",
    "created_at": "2008-09-25T23:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4197#issuecomment-30463",
    "user": "@williamstein"
}
```

Attachment [trac-4197.patch](tarball://root/attachments/some-uuid/ticket4197/trac-4197.patch) by @williamstein created at 2008-09-25 23:36:52



---

archive/issue_comments_030464.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-09-25T23:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4197#issuecomment-30464",
    "user": "@williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_030465.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nWe ought to check why weakref all the sudden is causing those failures. Maybe Cython is involved?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T00:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4197#issuecomment-30465",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

We ought to check why weakref all the sudden is causing those failures. Maybe Cython is involved?

Cheers,

Michael



---

archive/issue_comments_030466.json:
```json
{
    "body": "Oops, now it gets picked up by the reports.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T00:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4197#issuecomment-30466",
    "user": "mabshoff"
}
```

Oops, now it gets picked up by the reports.

Cheers,

Michael



---

archive/issue_comments_030467.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T04:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4197#issuecomment-30467",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030468.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-26T04:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4197#issuecomment-30468",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2
