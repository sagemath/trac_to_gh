# Issue 1425: wrong automatic simplification of pow

archive/issues_001425.json:
```json
{
    "body": "Assignee: was\n\nThe following simplification is wrong in my opinion:\n\n```\nsage: pow(pow(z,2),1/3)\nz^(2/3)\n```\n\nFor example for z = -1, pow(pow(-1,2),1/3) gives 1, but pow(-1,2/3) should give -1/2+sqrt(3)/2*I\n(it gives currently 1 in sage, which is another bug in my opinion):\n\n```\nsage: pow(-1,2/3)\n1\n```\n\n\nIndeed pow(z,a/b) for a and b integers is defined to be pow(pow(z,1/b),a), where pow(z,1/b) is the\nprincipal b-th root of z, i.e., in the argument domain (-pi/b, pi/b]. Thus the other simplification\npow(pow(z,1/b),a) -> pow(z, a/b) is valid, but pow(pow(z,a),1/b) -> pow(z,a/b) is not.\nIt suffices to consider the case a=b to understand this:\n\n```\nsage: pow(pow(z,2),1/2)\nabs(z)\nsage: pow(pow(z,3),1/3)\nz\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1425\n\n",
    "created_at": "2007-12-08T10:07:59Z",
    "labels": [
        "calculus",
        "critical",
        "bug"
    ],
    "title": "wrong automatic simplification of pow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1425",
    "user": "zimmerma"
}
```
Assignee: was

The following simplification is wrong in my opinion:

```
sage: pow(pow(z,2),1/3)
z^(2/3)
```

For example for z = -1, pow(pow(-1,2),1/3) gives 1, but pow(-1,2/3) should give -1/2+sqrt(3)/2*I
(it gives currently 1 in sage, which is another bug in my opinion):

```
sage: pow(-1,2/3)
1
```


Indeed pow(z,a/b) for a and b integers is defined to be pow(pow(z,1/b),a), where pow(z,1/b) is the
principal b-th root of z, i.e., in the argument domain (-pi/b, pi/b]. Thus the other simplification
pow(pow(z,1/b),a) -> pow(z, a/b) is valid, but pow(pow(z,a),1/b) -> pow(z,a/b) is not.
It suffices to consider the case a=b to understand this:

```
sage: pow(pow(z,2),1/2)
abs(z)
sage: pow(pow(z,3),1/3)
z
```


Issue created by migration from https://trac.sagemath.org/ticket/1425





---

archive/issue_comments_009180.json:
```json
{
    "body": "This is likely deep in the core of Maxima, so a serious pain (= basically impossible) etc to fix in a way that would really work.  It could be reported to maxima, but could we even convince them that it is a bug?  (Hopefully).\n\n\n```\n(%i3) ((-1)^2)^(1/3);\n(%o3)                                  1\n(%i4) (-1)^(2/3);\n(%o4)                                  1\n```\n",
    "created_at": "2007-12-10T05:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9180",
    "user": "was"
}
```

This is likely deep in the core of Maxima, so a serious pain (= basically impossible) etc to fix in a way that would really work.  It could be reported to maxima, but could we even convince them that it is a bug?  (Hopefully).


```
(%i3) ((-1)^2)^(1/3);
(%o3)                                  1
(%i4) (-1)^(2/3);
(%o4)                                  1
```




---

archive/issue_comments_009181.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2007-12-10T05:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9181",
    "user": "was"
}
```

Changing priority from critical to major.



---

archive/issue_comments_009182.json:
```json
{
    "body": "I sent an email to the maxima mailing list.",
    "created_at": "2007-12-10T23:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9182",
    "user": "mhansen"
}
```

I sent an email to the maxima mailing list.



---

archive/issue_comments_009183.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-11T02:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9183",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_009184.json:
```json
{
    "body": "\n```\n (%i1) domain : complex$\n\n (%i2) (x^2)^(1/3);\n (%o2) (x^2)^(1/3)\n\n (%i3) ((-1)^2)^(1/3);\n (%o3) 1\n\n (%i4) (-1)^(2/3);\n (%o4) (-1)^(2/3)\n\n (%i5) rectform(%);\n (%o5) (sqrt(3)*%i)/2-1/2\n```\n",
    "created_at": "2007-12-11T02:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9184",
    "user": "mhansen"
}
```


```
 (%i1) domain : complex$

 (%i2) (x^2)^(1/3);
 (%o2) (x^2)^(1/3)

 (%i3) ((-1)^2)^(1/3);
 (%o3) 1

 (%i4) (-1)^(2/3);
 (%o4) (-1)^(2/3)

 (%i5) rectform(%);
 (%o5) (sqrt(3)*%i)/2-1/2
```




---

archive/issue_comments_009185.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-11T02:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9185",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009186.json:
```json
{
    "body": "Unfortunately, this causes another major problem:\n\n\n```\n(%i13) domain: complex$\n(%i14) radcan( sqrt(x^2) - x );\n(%o14)                                 0\n(%i15) domain: real$\n(%i16) radcan( sqrt(x^2) - x );\n(%o16)                            abs(x) - x\n```\n\n\nwhich causes\n\n```\nsage: bool(sqrt(x^2) == x)\nTrue\n```\n",
    "created_at": "2007-12-11T03:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9186",
    "user": "mhansen"
}
```

Unfortunately, this causes another major problem:


```
(%i13) domain: complex$
(%i14) radcan( sqrt(x^2) - x );
(%o14)                                 0
(%i15) domain: real$
(%i16) radcan( sqrt(x^2) - x );
(%o16)                            abs(x) - x
```


which causes

```
sage: bool(sqrt(x^2) == x)
True
```




---

archive/issue_comments_009187.json:
```json
{
    "body": "Attachment [1425.patch](tarball://root/attachments/some-uuid/ticket1425/1425.patch) by mhansen created at 2007-12-14 06:45:36",
    "created_at": "2007-12-14T06:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9187",
    "user": "mhansen"
}
```

Attachment [1425.patch](tarball://root/attachments/some-uuid/ticket1425/1425.patch) by mhansen created at 2007-12-14 06:45:36



---

archive/issue_comments_009188.json:
```json
{
    "body": "It looks like this patch leaves maxima with its default \"real\" domain until the first call to simplify_radical, and then maxima is changed to use the \"complex\" domain.  That doesn't seem right; shouldn't there be a chunk of code somewhere to change to the \"complex\" domain on startup?",
    "created_at": "2007-12-15T02:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9188",
    "user": "cwitty"
}
```

It looks like this patch leaves maxima with its default "real" domain until the first call to simplify_radical, and then maxima is changed to use the "complex" domain.  That doesn't seem right; shouldn't there be a chunk of code somewhere to change to the "complex" domain on startup?



---

archive/issue_comments_009189.json:
```json
{
    "body": "Oops, I forgot to commit sage/interfaces/r.py .  I've posted a patch with that change.",
    "created_at": "2007-12-15T07:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9189",
    "user": "mhansen"
}
```

Oops, I forgot to commit sage/interfaces/r.py .  I've posted a patch with that change.



---

archive/issue_comments_009190.json:
```json
{
    "body": "Attachment [1425-2.patch](tarball://root/attachments/some-uuid/ticket1425/1425-2.patch) by was created at 2007-12-15 10:48:55\n\nI do *not* like 1425-2.patch.  We should *not* set complex domain for *all* maxima interfaces -- only for the one used by the calculus package.",
    "created_at": "2007-12-15T10:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9190",
    "user": "was"
}
```

Attachment [1425-2.patch](tarball://root/attachments/some-uuid/ticket1425/1425-2.patch) by was created at 2007-12-15 10:48:55

I do *not* like 1425-2.patch.  We should *not* set complex domain for *all* maxima interfaces -- only for the one used by the calculus package.



---

archive/issue_comments_009191.json:
```json
{
    "body": "Attachment [trac-1425-referee.patch](tarball://root/attachments/some-uuid/ticket1425/trac-1425-referee.patch) by was created at 2007-12-15 13:41:16",
    "created_at": "2007-12-15T13:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9191",
    "user": "was"
}
```

Attachment [trac-1425-referee.patch](tarball://root/attachments/some-uuid/ticket1425/trac-1425-referee.patch) by was created at 2007-12-15 13:41:16



---

archive/issue_comments_009192.json:
```json
{
    "body": "NOTE!!   Apply only 1425.patch and trac-125-refeee.patch.\n\nDO NOT apply 1425-2.patch.",
    "created_at": "2007-12-15T13:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9192",
    "user": "was"
}
```

NOTE!!   Apply only 1425.patch and trac-125-refeee.patch.

DO NOT apply 1425-2.patch.



---

archive/issue_comments_009193.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T13:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9193",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009194.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T13:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1425#issuecomment-9194",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.
