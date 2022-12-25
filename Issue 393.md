# Issue 393: Very strange behavior of QQ -> RealField() conversion.

archive/issues_000393.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: real, rational, coerce\n\nThere is something very wrong with this behavior of this code, which tries to convert 1/2 to a 2x2 matrix.  The problem seems not to be in the matrix code, but since it's hard to reproduce it appears in that form.\n\nIssue created by migration from https://trac.sagemath.org/ticket/393\n\n",
    "closed_at": "2007-08-18T21:40:13Z",
    "created_at": "2007-06-28T15:20:44Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "Very strange behavior of QQ -> RealField() conversion.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/393",
    "user": "https://github.com/jonhanke"
}
```
Assignee: somebody

Keywords: real, rational, coerce

There is something very wrong with this behavior of this code, which tries to convert 1/2 to a 2x2 matrix.  The problem seems not to be in the matrix code, but since it's hard to reproduce it appears in that form.

Issue created by migration from https://trac.sagemath.org/ticket/393





---

archive/issue_comments_001920.json:
```json
{
    "body": "Attachment [sage_errors__matrix_test.py](tarball://root/attachments/some-uuid/ticket393/sage_errors__matrix_test.py) by @jonhanke created at 2007-06-28 15:28:21\n\nHere is the output of the attached routine, which essentially does the same thing 3 times and gets 3 different answers!\n\n```\njonhanke@[~/Documents/sage-2.6/devel/sage-qfdevel/sage/quadratic_forms]: sage -br\n\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n\nrunning install\nrunning build\nrunning build_py\ncopying sage/quadratic_forms/sage_errors__matrix_test.py -> build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms\nrunning build_ext\nrunning build_scripts\nrunning install_lib\ncopying build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms/sage_errors__matrix_test.py -> /Users/jonhanke/Documents/sage-2.6/local/lib/python2.5/site-packag\n\nsage: MatrixTest()\nFalse\n[0.000000000000000 0.000000000000000]\n[0.000000000000000 0.000000000000000]\n[0.500000000000000 0.000000000000000]\n[0.000000000000000 0.500000000000000]\n\nm1 is \n[0.000000000000000 0.000000000000000]\n[0.000000000000000 0.000000000000000]\n\nm2 is \n[0.000000000000000 0.000000000000000]\n[0.000000000000000 0.000000000000000]\nFalse\n\n\nm1 is \n[0.500000000000000 0.000000000000000]\n[0.000000000000000 0.500000000000000]\n\nm2 is \n[0.500000000000000 0.000000000000000]\n[0.000000000000000 0.500000000000000]\nFalse\n```",
    "created_at": "2007-06-28T15:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/393#issuecomment-1920",
    "user": "https://github.com/jonhanke"
}
```

Attachment [sage_errors__matrix_test.py](tarball://root/attachments/some-uuid/ticket393/sage_errors__matrix_test.py) by @jonhanke created at 2007-06-28 15:28:21

Here is the output of the attached routine, which essentially does the same thing 3 times and gets 3 different answers!

```
jonhanke@[~/Documents/sage-2.6/devel/sage-qfdevel/sage/quadratic_forms]: sage -br

----------------------------------------------------------
sage: Building and installing modified SAGE library files.

running install
running build
running build_py
copying sage/quadratic_forms/sage_errors__matrix_test.py -> build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms
running build_ext
running build_scripts
running install_lib
copying build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms/sage_errors__matrix_test.py -> /Users/jonhanke/Documents/sage-2.6/local/lib/python2.5/site-packag

sage: MatrixTest()
False
[0.000000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000]
[0.500000000000000 0.000000000000000]
[0.000000000000000 0.500000000000000]

m1 is 
[0.000000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000]

m2 is 
[0.000000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000]
False


m1 is 
[0.500000000000000 0.000000000000000]
[0.000000000000000 0.500000000000000]

m2 is 
[0.500000000000000 0.000000000000000]
[0.000000000000000 0.500000000000000]
False
```



---

archive/issue_events_000937.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-18T21:22:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/393#event-937"
}
```



---

archive/issue_comments_001921.json:
```json
{
    "body": "This is just due to the difference between SAGE and Python.  When run from the command line or in a .sage file, SAGE will preprocess the file and change 1/2 to Integer(1)/Integer(2) to (correctly) form the rational 1/2.  When included or run form a .py file, it will remain as 1/2 which Python evaluates to 0.\n\nThere is also a typo in the second section of the attached file (m1 is printed twice).",
    "created_at": "2007-08-18T21:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/393#issuecomment-1921",
    "user": "https://github.com/mwhansen"
}
```

This is just due to the difference between SAGE and Python.  When run from the command line or in a .sage file, SAGE will preprocess the file and change 1/2 to Integer(1)/Integer(2) to (correctly) form the rational 1/2.  When included or run form a .py file, it will remain as 1/2 which Python evaluates to 0.

There is also a typo in the second section of the attached file (m1 is printed twice).



---

archive/issue_comments_001922.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-08-18T21:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/393#issuecomment-1922",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_000938.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-08-18T21:40:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/393#event-938"
}
```
