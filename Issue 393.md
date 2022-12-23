# Issue 393: Very strange behavior of QQ -> RealField() conversion.

archive/issues_000393.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: real, rational, coerce\n\nThere is something very wrong with this behavior of this code, which tries to convert 1/2 to a 2x2 matrix.  The problem seems not to be in the matrix code, but since it's hard to reproduce it appears in that form.\n\nIssue created by migration from https://trac.sagemath.org/ticket/393\n\n",
    "created_at": "2007-06-28T15:20:44Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Very strange behavior of QQ -> RealField() conversion.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/393",
    "user": "jonhanke"
}
```
Assignee: somebody

Keywords: real, rational, coerce

There is something very wrong with this behavior of this code, which tries to convert 1/2 to a 2x2 matrix.  The problem seems not to be in the matrix code, but since it's hard to reproduce it appears in that form.

Issue created by migration from https://trac.sagemath.org/ticket/393





---

archive/issue_comments_001928.json:
```json
{
    "body": "Attachment\n\nHere is the output of the attached routine, which essentially does the same thing 3 times and gets 3 different answers!\n\n\n```\njonhanke@[~/Documents/sage-2.6/devel/sage-qfdevel/sage/quadratic_forms]: sage -br\n\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n\nrunning install\nrunning build\nrunning build_py\ncopying sage/quadratic_forms/sage_errors__matrix_test.py -> build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms\nrunning build_ext\nrunning build_scripts\nrunning install_lib\ncopying build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms/sage_errors__matrix_test.py -> /Users/jonhanke/Documents/sage-2.6/local/lib/python2.5/site-packag\n\nsage: MatrixTest()\nFalse\n[0.000000000000000 0.000000000000000]\n[0.000000000000000 0.000000000000000]\n[0.500000000000000 0.000000000000000]\n[0.000000000000000 0.500000000000000]\n\nm1 is \n[0.000000000000000 0.000000000000000]\n[0.000000000000000 0.000000000000000]\n\nm2 is \n[0.000000000000000 0.000000000000000]\n[0.000000000000000 0.000000000000000]\nFalse\n\n\nm1 is \n[0.500000000000000 0.000000000000000]\n[0.000000000000000 0.500000000000000]\n\nm2 is \n[0.500000000000000 0.000000000000000]\n[0.000000000000000 0.500000000000000]\nFalse\n```\n",
    "created_at": "2007-06-28T15:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/393#issuecomment-1928",
    "user": "jonhanke"
}
```

Attachment

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

archive/issue_comments_001929.json:
```json
{
    "body": "This is just due to the difference between SAGE and Python.  When run from the command line or in a .sage file, SAGE will preprocess the file and change 1/2 to Integer(1)/Integer(2) to (correctly) form the rational 1/2.  When included or run form a .py file, it will remain as 1/2 which Python evaluates to 0.\n\nThere is also a typo in the second section of the attached file (m1 is printed twice).",
    "created_at": "2007-08-18T21:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/393#issuecomment-1929",
    "user": "mhansen"
}
```

This is just due to the difference between SAGE and Python.  When run from the command line or in a .sage file, SAGE will preprocess the file and change 1/2 to Integer(1)/Integer(2) to (correctly) form the rational 1/2.  When included or run form a .py file, it will remain as 1/2 which Python evaluates to 0.

There is also a typo in the second section of the attached file (m1 is printed twice).



---

archive/issue_comments_001930.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-08-18T21:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/393#issuecomment-1930",
    "user": "mhansen"
}
```

Resolution: invalid
