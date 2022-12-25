# Issue 6241: numerical noise (very easy to fix) on cicero (redhat 9) i686 32-bit

archive/issues_006241.json:
```json
{
    "body": "Assignee: @williamstein\n\nNotice the 7 real part instead of 6 below:\n\n\n```\nPlease see /home/wstein/build/cicero/sage-4.0.1/tmp/test.log for the complete log from this test.\n[wstein@cicero sage-4.0.1]$ ./sage -t  \"devel/sage/sage/rings/number_field/number_field.py\"\nsage -t  \"devel/sage/sage/rings/number_field/number_field.py\"\n**********************************************************************\nFile \"/home/wstein/build/cicero/sage-4.0.1/devel/sage/sage/rings/number_field/number_field.py\", line 7295:\n    sage: e = K.embeddings(CC)[0]; e\nExpected:\n    Ring morphism:\n    From: Number Field in a with defining polynomial x^3 - 2\n    To:   Complex Field with 53 bits of precision\n    Defn: a |--> -0.629960524947436 - 1.09112363597172*I\nGot:\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 - 2\n      To:   Complex Field with 53 bits of precision\n      Defn: a |--> -0.629960524947437 - 1.09112363597172*I\n\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n**********************************************************************\n1 items had failures:\n   1 of  19 in __main__.example_180\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/build/cicero/sage-4.0.1/tmp/.doctest_number_field.py\n         [37.9 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/rings/number_field/number_field.py\"\nTotal time for all tests: 37.9 seconds\n[wstein@cicero sage-4.0.1]$ cat /etc/issue\nFedora release 9 (Sulphur)\nKernel \\r on an \\m (\\l)\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6241\n\n",
    "created_at": "2009-06-07T13:35:32Z",
    "labels": [
        "component: number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "numerical noise (very easy to fix) on cicero (redhat 9) i686 32-bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6241",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Notice the 7 real part instead of 6 below:


```
Please see /home/wstein/build/cicero/sage-4.0.1/tmp/test.log for the complete log from this test.
[wstein@cicero sage-4.0.1]$ ./sage -t  "devel/sage/sage/rings/number_field/number_field.py"
sage -t  "devel/sage/sage/rings/number_field/number_field.py"
**********************************************************************
File "/home/wstein/build/cicero/sage-4.0.1/devel/sage/sage/rings/number_field/number_field.py", line 7295:
    sage: e = K.embeddings(CC)[0]; e
Expected:
    Ring morphism:
    From: Number Field in a with defining polynomial x^3 - 2
    To:   Complex Field with 53 bits of precision
    Defn: a |--> -0.629960524947436 - 1.09112363597172*I
Got:
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> -0.629960524947437 - 1.09112363597172*I

  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
**********************************************************************
1 items had failures:
   1 of  19 in __main__.example_180
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/cicero/sage-4.0.1/tmp/.doctest_number_field.py
         [37.9 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/number_field/number_field.py"
Total time for all tests: 37.9 seconds
[wstein@cicero sage-4.0.1]$ cat /etc/issue
Fedora release 9 (Sulphur)
Kernel \r on an \m (\l)

```


Issue created by migration from https://trac.sagemath.org/ticket/6241





---

archive/issue_comments_049750.json:
```json
{
    "body": "this is already merged into 4.0.2.rc1, but needs to be reviewed.  it's pretty trivial.",
    "created_at": "2009-06-15T23:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6241#issuecomment-49750",
    "user": "https://github.com/williamstein"
}
```

this is already merged into 4.0.2.rc1, but needs to be reviewed.  it's pretty trivial.



---

archive/issue_comments_049751.json:
```json
{
    "body": "Attachment [trac_6241.patch](tarball://root/attachments/some-uuid/ticket6241/trac_6241.patch) by @williamstein created at 2009-06-16 00:07:04",
    "created_at": "2009-06-16T00:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6241#issuecomment-49751",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6241.patch](tarball://root/attachments/some-uuid/ticket6241/trac_6241.patch) by @williamstein created at 2009-06-16 00:07:04



---

archive/issue_comments_049752.json:
```json
{
    "body": "Yep, I can give that a positive review.",
    "created_at": "2009-06-16T05:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6241#issuecomment-49752",
    "user": "https://github.com/craigcitro"
}
```

Yep, I can give that a positive review.



---

archive/issue_events_006486.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2009-06-16T05:20:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6241",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6241#event-6486"
}
```



---

archive/issue_comments_049753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-16T05:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6241#issuecomment-49753",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed
