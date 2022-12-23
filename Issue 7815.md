# Issue 7815: Flint fails to build 64-bit on Open Solaris

archive/issues_007815.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jst rlm\n\nThere are several problems in the Flint spkg-install and makefile which prevent it building 64-bit on any platform other than OS X. Apart from the usual changes of adding -m64 to CFLAGS, the makefile has previously been changed to make it work on OS X. However, it does not work on Open Solaris in 64-bit mode, as the -m64 flag is not being added where it should be. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7815\n\n",
    "created_at": "2010-01-02T06:21:14Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "Flint fails to build 64-bit on Open Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7815",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jst rlm

There are several problems in the Flint spkg-install and makefile which prevent it building 64-bit on any platform other than OS X. Apart from the usual changes of adding -m64 to CFLAGS, the makefile has previously been changed to make it work on OS X. However, it does not work on Open Solaris in 64-bit mode, as the -m64 flag is not being added where it should be. 



Issue created by migration from https://trac.sagemath.org/ticket/7815





---

archive/issue_comments_067620.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T06:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67620",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067621.json:
```json
{
    "body": "Here's an updated spkg which corrects the faults. It essentially does that by adding the environment variable CXXFLAG64 to the Makefile. This will add -m64 whenever SAGE64 is set to yes. If you look at the makefile you will see -m64 has been hard-coded when building the library on OS X, but not for other platforms. \n\nThe changes have been checked in with 'hg'\n\nRevised .spkg and diff can be found at\n\nhttp://boxen.math.washington.edu/home/kirkby/portability/flint-1.5.0.p3/\n\nDave",
    "created_at": "2010-01-02T06:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67621",
    "user": "drkirkby"
}
```

Here's an updated spkg which corrects the faults. It essentially does that by adding the environment variable CXXFLAG64 to the Makefile. This will add -m64 whenever SAGE64 is set to yes. If you look at the makefile you will see -m64 has been hard-coded when building the library on OS X, but not for other platforms. 

The changes have been checked in with 'hg'

Revised .spkg and diff can be found at

http://boxen.math.washington.edu/home/kirkby/portability/flint-1.5.0.p3/

Dave



---

archive/issue_comments_067622.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T01:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67622",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067623.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T02:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67623",
    "user": "drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067624.json:
```json
{
    "body": "Make sure CFLAG64 and CXXFLAG64 are both exported to -m64 when testing this. It relies on that, which will happen automatically very soon I hope, when my updates to sage-env get incorporated.",
    "created_at": "2010-01-06T02:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67624",
    "user": "drkirkby"
}
```

Make sure CFLAG64 and CXXFLAG64 are both exported to -m64 when testing this. It relies on that, which will happen automatically very soon I hope, when my updates to sage-env get incorporated.



---

archive/issue_comments_067625.json:
```json
{
    "body": "This depends on  #7818 so should not be applied until that is applied.",
    "created_at": "2010-01-13T07:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67625",
    "user": "drkirkby"
}
```

This depends on  #7818 so should not be applied until that is applied.



---

archive/issue_comments_067626.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-14T08:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67626",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067627.json:
```json
{
    "body": "Everything works on boxen, and I trust dkirkby on the Open Solaris end.",
    "created_at": "2010-01-14T08:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67627",
    "user": "rlm"
}
```

Everything works on boxen, and I trust dkirkby on the Open Solaris end.



---

archive/issue_comments_067628.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T08:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67628",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_067629.json:
```json
{
    "body": "Not only does it work on Open Solaris on x86 hardware, but I just tried for the first time to build a 64-bit version of Sage on a Sun Blade 2000 with a pair of UltraSPARC III+ CPUs running Solaris 10. This was based on the 4.3.1.alpha2 source code, but with this patch added. There are warnings issued during the 64-bit SPARC build that there are no 64-bit assembly routines, so C is used. But apart from that, Flint is now at least building on:\n\n* 32-bit Solaris 10 SPARC \n* 64-bit Solaris 10 SPARC\n* 64-bit Open Solaris x86",
    "created_at": "2010-01-14T09:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7815#issuecomment-67629",
    "user": "drkirkby"
}
```

Not only does it work on Open Solaris on x86 hardware, but I just tried for the first time to build a 64-bit version of Sage on a Sun Blade 2000 with a pair of UltraSPARC III+ CPUs running Solaris 10. This was based on the 4.3.1.alpha2 source code, but with this patch added. There are warnings issued during the 64-bit SPARC build that there are no 64-bit assembly routines, so C is used. But apart from that, Flint is now at least building on:

* 32-bit Solaris 10 SPARC 
* 64-bit Solaris 10 SPARC
* 64-bit Open Solaris x86
