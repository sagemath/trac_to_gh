# Issue 5431: [with patch, positive review] Command line parser fails on hex values with 'e'

archive/issues_005431.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb\n\n```\nsage: 0xe\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ryan/.sage/temp/fileserv/1535/_home_ryan__sage_init_sage_0.py in <module>()\n\n/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:21774)()\n\n/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:20990)()\n\n/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7454)()\n\n/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7957)()\n\nTypeError: Unable to convert x (='0xe') to real number.\n```\nThe same thing happens with \"0xE\".  It appears the parser sees the E/e and assumes it is a floating-point number instead of using the leading \"0x\".  \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5431\n\n",
    "closed_at": "2009-06-13T21:50:12Z",
    "created_at": "2009-03-03T19:18:40Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, positive review] Command line parser fails on hex values with 'e'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5431",
    "user": "https://github.com/rhinton"
}
```
Assignee: somebody

CC:  @robertwb

```
sage: 0xe
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ryan/.sage/temp/fileserv/1535/_home_ryan__sage_init_sage_0.py in <module>()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:21774)()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:20990)()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7454)()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7957)()

TypeError: Unable to convert x (='0xe') to real number.
```
The same thing happens with "0xE".  It appears the parser sees the E/e and assumes it is a floating-point number instead of using the leading "0x".  


Issue created by migration from https://trac.sagemath.org/ticket/5431





---

archive/issue_comments_041943.json:
```json
{
    "body": "Attachment [trac_5431.patch](tarball://root/attachments/some-uuid/ticket5431/trac_5431.patch) by @mwhansen created at 2009-06-05 01:32:59\n\nThis was fixed by the preparser rewrite work by robertwb.",
    "created_at": "2009-06-05T01:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5431#issuecomment-41943",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5431.patch](tarball://root/attachments/some-uuid/ticket5431/trac_5431.patch) by @mwhansen created at 2009-06-05 01:32:59

This was fixed by the preparser rewrite work by robertwb.



---

archive/issue_comments_041944.json:
```json
{
    "body": "Patch adds doctest.",
    "created_at": "2009-06-05T03:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5431#issuecomment-41944",
    "user": "https://github.com/robertwb"
}
```

Patch adds doctest.



---

archive/issue_events_012676.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-13T21:50:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5431",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5431#event-12676"
}
```



---

archive/issue_comments_041945.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5431#issuecomment-41945",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
