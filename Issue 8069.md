# Issue 8069: New mpfi-1.3.4-cvs20071125.p8.spkg works with Open Solaris 64 bit

archive/issues_008069.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirby was\n\nYet another correction. SAGE64=yes works also on Open Solaris 64 bit.\n\nThe spkg is here:\n[http://boxen.math.washington.edu/home/jsp/ports/mpfi-1.3.4-cvs20071125.p8.spkg](http://boxen.math.washington.edu/home/jsp/ports/mpfi-1.3.4-cvs20071125.p8.spkg)\n\n\n\n```\nmake[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8/src'\nmake[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8/src'\n\nreal\t0m15.129s\nuser\t0m7.916s\nsys\t0m6.259s\nSuccessfully installed mpfi-1.3.4-cvs20071125.p8\nYou can safely delete the temporary build directory\n/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing mpfi-1.3.4-cvs20071125.p8.spkg\njaap@opensolaris:~/Downloads/sage-4.3.1$ \n\n\n```\n\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/8069\n\n",
    "created_at": "2010-01-26T00:01:49Z",
    "labels": [
        "porting",
        "major",
        "enhancement"
    ],
    "title": "New mpfi-1.3.4-cvs20071125.p8.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8069",
    "user": "jsp"
}
```
Assignee: drkirkby

CC:  drkirby was

Yet another correction. SAGE64=yes works also on Open Solaris 64 bit.

The spkg is here:
[http://boxen.math.washington.edu/home/jsp/ports/mpfi-1.3.4-cvs20071125.p8.spkg](http://boxen.math.washington.edu/home/jsp/ports/mpfi-1.3.4-cvs20071125.p8.spkg)



```
make[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8/src'
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8/src'

real	0m15.129s
user	0m7.916s
sys	0m6.259s
Successfully installed mpfi-1.3.4-cvs20071125.p8
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing mpfi-1.3.4-cvs20071125.p8.spkg
jaap@opensolaris:~/Downloads/sage-4.3.1$ 


```


Jaap

Issue created by migration from https://trac.sagemath.org/ticket/8069





---

archive/issue_comments_070710.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T00:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70710",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070711.json:
```json
{
    "body": "without some way to be able to see what you have changed, it is difficult to review. Again, without a patch, it could never be integrated with anyone else that might change this package\n\nDave",
    "created_at": "2010-01-26T11:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70711",
    "user": "drkirkby"
}
```

without some way to be able to see what you have changed, it is difficult to review. Again, without a patch, it could never be integrated with anyone else that might change this package

Dave



---

archive/issue_comments_070712.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-26T11:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70712",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070713.json:
```json
{
    "body": "Attachment [mpfr-2.4.1.p1.patch](tarball://root/attachments/some-uuid/ticket8069/mpfr-2.4.1.p1.patch) by jsp created at 2010-01-26 18:34:07",
    "created_at": "2010-01-26T18:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70713",
    "user": "jsp"
}
```

Attachment [mpfr-2.4.1.p1.patch](tarball://root/attachments/some-uuid/ticket8069/mpfr-2.4.1.p1.patch) by jsp created at 2010-01-26 18:34:07



---

archive/issue_comments_070714.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T18:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70714",
    "user": "jsp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070715.json:
```json
{
    "body": "Attachment [mpfi-1.3.4-cvs20071125.p8.patch](tarball://root/attachments/some-uuid/ticket8069/mpfi-1.3.4-cvs20071125.p8.patch) by jsp created at 2010-01-26 18:53:16",
    "created_at": "2010-01-26T18:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70715",
    "user": "jsp"
}
```

Attachment [mpfi-1.3.4-cvs20071125.p8.patch](tarball://root/attachments/some-uuid/ticket8069/mpfi-1.3.4-cvs20071125.p8.patch) by jsp created at 2010-01-26 18:53:16



---

archive/issue_comments_070716.json:
```json
{
    "body": "Sorry! Clicked on the wrong file!\n\nJaap",
    "created_at": "2010-01-26T18:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70716",
    "user": "jsp"
}
```

Sorry! Clicked on the wrong file!

Jaap



---

archive/issue_comments_070717.json:
```json
{
    "body": "This is fine.",
    "created_at": "2010-01-27T02:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70717",
    "user": "drkirkby"
}
```

This is fine.



---

archive/issue_comments_070718.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T02:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70718",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070719.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-01-27T04:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70719",
    "user": "drkirkby"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_070720.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8069#issuecomment-70720",
    "user": "mpatel"
}
```

Resolution: fixed
