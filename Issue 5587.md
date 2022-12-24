# Issue 5587: input of hexadecimal integers is corrupted

archive/issues_005587.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: 0xabcdf\n703711\nsage: 0xabcdef\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/zimmerma/.sage/temp/toto.loria.fr/11913/_home_zimmerma__sage_init_sage_0.py in <module>()\n\n/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:22110)()\n\n/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:21326)()\n\n/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7473)()\n\n/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7976)()\n\nTypeError: Unable to convert x (='0xabcdef') to real number.\n```\n\nI understand that Sage tries to recognize a floating-point number\ndue to the 'e', but then how to input a hexadecimal integer?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5587\n\n",
    "created_at": "2009-03-22T21:50:42Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "input of hexadecimal integers is corrupted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5587",
    "user": "zimmerma"
}
```
Assignee: somebody


```
sage: 0xabcdf
703711
sage: 0xabcdef
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/zimmerma/.sage/temp/toto.loria.fr/11913/_home_zimmerma__sage_init_sage_0.py in <module>()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:22110)()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:21326)()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7473)()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7976)()

TypeError: Unable to convert x (='0xabcdef') to real number.
```

I understand that Sage tries to recognize a floating-point number
due to the 'e', but then how to input a hexadecimal integer?

Issue created by migration from https://trac.sagemath.org/ticket/5587





---

archive/issue_comments_043547.json:
```json
{
    "body": "Looks like this is fixed in Sage 4.1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: 0xabcdf\n703711\nsage: 0xabcdef\n11259375\n```\n\nI'm closing this ticket as fixed.",
    "created_at": "2009-07-26T03:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5587#issuecomment-43547",
    "user": "mvngu"
}
```

Looks like this is fixed in Sage 4.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 0xabcdf
703711
sage: 0xabcdef
11259375
```

I'm closing this ticket as fixed.



---

archive/issue_comments_043548.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-26T03:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5587#issuecomment-43548",
    "user": "mvngu"
}
```

Resolution: fixed
