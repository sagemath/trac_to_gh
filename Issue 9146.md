# Issue 9146: cygwin: gd doesn't correctly link in libpng with sage-4.4.3.

archive/issues_009146.json:
```json
{
    "body": "Assignee: tbd\n\nThe fix involves copying over $SAGE_LOCAL/bin/cygpng12-0.dll to $SAGE_LOCAL/lib/\n\nIssue created by migration from https://trac.sagemath.org/ticket/9146\n\n",
    "created_at": "2010-06-05T04:53:49Z",
    "labels": [
        "porting: Cygwin",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "cygwin: gd doesn't correctly link in libpng with sage-4.4.3.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9146",
    "user": "was"
}
```
Assignee: tbd

The fix involves copying over $SAGE_LOCAL/bin/cygpng12-0.dll to $SAGE_LOCAL/lib/

Issue created by migration from https://trac.sagemath.org/ticket/9146





---

archive/issue_comments_085399.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-05T04:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85399",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085400.json:
```json
{
    "body": "There is an spkg at http://sage.math.washington.edu/home/mhansen/libpng-1.2.35.p2.spkg",
    "created_at": "2010-06-05T04:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85400",
    "user": "mhansen"
}
```

There is an spkg at http://sage.math.washington.edu/home/mhansen/libpng-1.2.35.p2.spkg



---

archive/issue_comments_085401.json:
```json
{
    "body": "I tried installing on linux and:\n\n\n```\n\nmake[2]: Leaving directory `/mnt/usb1/scratch/wstein/build/sage-4.4.3.rc0/spkg/build/libpng-1.2.35.p2/src'\nmake[1]: Leaving directory `/mnt/usb1/scratch/wstein/build/sage-4.4.3.rc0/spkg/build/libpng-1.2.35.p2/src'\n./spkg-install: line 55: syntax error near unexpected token `fi'\n./spkg-install: line 55: `fi'\n\n```\n",
    "created_at": "2010-06-05T05:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85401",
    "user": "was"
}
```

I tried installing on linux and:


```

make[2]: Leaving directory `/mnt/usb1/scratch/wstein/build/sage-4.4.3.rc0/spkg/build/libpng-1.2.35.p2/src'
make[1]: Leaving directory `/mnt/usb1/scratch/wstein/build/sage-4.4.3.rc0/spkg/build/libpng-1.2.35.p2/src'
./spkg-install: line 55: syntax error near unexpected token `fi'
./spkg-install: line 55: `fi'

```




---

archive/issue_comments_085402.json:
```json
{
    "body": "Fixed version:\n   http://sage.math.washington.edu/home/wstein/patches/libpng-1.2.35.p2.spkg",
    "created_at": "2010-06-05T05:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85402",
    "user": "was"
}
```

Fixed version:
   http://sage.math.washington.edu/home/wstein/patches/libpng-1.2.35.p2.spkg



---

archive/issue_comments_085403.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T05:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85403",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085404.json:
```json
{
    "body": "It doesn't work yet on Cygwin itself (on a clean install):\n\n```\n\nmake[2]: Leaving directory `/home/wstein/sage-4.4.3/spkg/build/libpng-1.2.35.p2/src'\ncp: cannot stat `/home/wstein/sage-4.4.3/local/bin/cygpng12-0.dll': No such file or directory\nError installing libpng\n\nreal    6m25.233s\nuser    1m28.601s\nsys     4m59.953s\n```\n",
    "created_at": "2010-06-05T05:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85404",
    "user": "was"
}
```

It doesn't work yet on Cygwin itself (on a clean install):

```

make[2]: Leaving directory `/home/wstein/sage-4.4.3/spkg/build/libpng-1.2.35.p2/src'
cp: cannot stat `/home/wstein/sage-4.4.3/local/bin/cygpng12-0.dll': No such file or directory
Error installing libpng

real    6m25.233s
user    1m28.601s
sys     4m59.953s
```




---

archive/issue_comments_085405.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-05T05:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85405",
    "user": "was"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_085406.json:
```json
{
    "body": "The above failure report is on cygwin upgraded to the latest version as of june 4, 2010.",
    "created_at": "2010-06-05T06:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85406",
    "user": "was"
}
```

The above failure report is on cygwin upgraded to the latest version as of june 4, 2010.



---

archive/issue_comments_085407.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-05T08:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85407",
    "user": "mhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085408.json:
```json
{
    "body": "The build completes successfully once \"file\" is installed in winxp3.  If \"file\" is not installed, then Cygwin has a difficult time making shared libraries.  This is why this wasn't an issue initially with my sage-4.3.5 install in winxp2.\n\nWe need to make \"file\" a preqreq.",
    "created_at": "2010-06-05T08:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85408",
    "user": "mhansen"
}
```

The build completes successfully once "file" is installed in winxp3.  If "file" is not installed, then Cygwin has a difficult time making shared libraries.  This is why this wasn't an issue initially with my sage-4.3.5 install in winxp2.

We need to make "file" a preqreq.



---

archive/issue_comments_085409.json:
```json
{
    "body": "Yes, winxp3 is missing a lot of prerequisites.  MPIR also fails to build there.",
    "created_at": "2010-06-05T14:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85409",
    "user": "was"
}
```

Yes, winxp3 is missing a lot of prerequisites.  MPIR also fails to build there.



---

archive/issue_comments_085410.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T14:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85410",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085411.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T00:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9146#issuecomment-85411",
    "user": "mhansen"
}
```

Resolution: fixed
