# Issue 9735: Numerical noise on sage/stats/hmm/chmm.pyx on both Solaris x86 and OpenSolaris x86

archive/issues_009735.json:
```json
{
    "body": "Assignee: mvngu\n\nThe following test failure seen on both a Sun Ultra 27 running OpenSolaris 06/2009 and a Dell Optiplex 755 running Solaris 10 on the x86 processor. \n\n## On a Sun Ultra 27 running OpenSolaris\n* Sun Ultra 27 \n* 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. \n* 12 GB RAM\n* OpenSolaris 2009.06 snv_134b X86\n* Sage 4.5.3.alpha0\n* gcc 4.5.0\n\n```\nsage -t  -long devel/sage/sage/stats/hmm/chmm.pyx\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx\", line 570:\n    sage: m.viterbi([0,1,10,10,1])\nExpected:\n    ([0, 0, 1, 1, 0], -9.0604285688230899)\nGot:\n    ([0, 0, 1, 1, 0], -9.0604285688230917)\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx\", line 132:\n    sage: m.baum_welch(obs)\nExpected:\n    (-10.610333495739708, 14)\nGot:\n    (-10.61033349573971, 14)\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx\", line 134:\n    sage: m.log_likelihood(obs)\nExpected:\n    -10.610333495739708\nGot:\n    -10.61033349573971\n**********************************************************************\n2 items had failures:\n   1 of   7 in __main__.example_15\n   2 of  12 in __main__.example_2\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_chmm.py\n\t [2.9 s]\n```\n\n## On a Dell Optiplex 755 running Solaris 10 x86\n* Dell Optiplex 755\n* 2.4 GHz Quad-Core Intel Core Q6600 \n* 8 GB RAM\n* Solaris 10 x86 (update 5, 5/08)\n* gcc 4.5.1 configured to use the Sun linker and GNU assembler from binutils-2.20.1. \n* 32-bit build. \n* Using sage-4.5.2.rc1\n\n```\nsage -t  -long devel/sage/sage/stats/hmm/chmm.pyx\n**********************************************************************\nFile \"/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx\", line 570:\n    sage: m.viterbi([0,1,10,10,1])\nExpected:\n    ([0, 0, 1, 1, 0], -9.0604285688230899)\nGot:\n    ([0, 0, 1, 1, 0], -9.0604285688230917)\n**********************************************************************\nFile \"/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx\", line 132:\n    sage: m.baum_welch(obs)\nExpected:\n    (-10.610333495739708, 14)\nGot:\n    (-10.61033349573971, 14)\n**********************************************************************\nFile \"/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx\", line 134:\n    sage: m.log_likelihood(obs)\nExpected:\n    -10.610333495739708\nGot:\n    -10.61033349573971\n**********************************************************************\n2 items had failures:\n   1 of   7 in __main__.example_15\n   2 of  12 in __main__.example_2\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /home/palmieri/.sage_fulvia/tmp/.doctest_chmm.py\n\t [11.4 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9735\n\n",
    "created_at": "2010-08-12T16:55:29Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Numerical noise on sage/stats/hmm/chmm.pyx on both Solaris x86 and OpenSolaris x86",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9735",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: mvngu

The following test failure seen on both a Sun Ultra 27 running OpenSolaris 06/2009 and a Dell Optiplex 755 running Solaris 10 on the x86 processor. 

## On a Sun Ultra 27 running OpenSolaris
* Sun Ultra 27 
* 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 
* 12 GB RAM
* OpenSolaris 2009.06 snv_134b X86
* Sage 4.5.3.alpha0
* gcc 4.5.0

```
sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx
**********************************************************************
File "/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx", line 570:
    sage: m.viterbi([0,1,10,10,1])
Expected:
    ([0, 0, 1, 1, 0], -9.0604285688230899)
Got:
    ([0, 0, 1, 1, 0], -9.0604285688230917)
**********************************************************************
File "/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx", line 132:
    sage: m.baum_welch(obs)
Expected:
    (-10.610333495739708, 14)
Got:
    (-10.61033349573971, 14)
**********************************************************************
File "/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx", line 134:
    sage: m.log_likelihood(obs)
Expected:
    -10.610333495739708
Got:
    -10.61033349573971
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_15
   2 of  12 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_chmm.py
	 [2.9 s]
```

## On a Dell Optiplex 755 running Solaris 10 x86
* Dell Optiplex 755
* 2.4 GHz Quad-Core Intel Core Q6600 
* 8 GB RAM
* Solaris 10 x86 (update 5, 5/08)
* gcc 4.5.1 configured to use the Sun linker and GNU assembler from binutils-2.20.1. 
* 32-bit build. 
* Using sage-4.5.2.rc1

```
sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx
**********************************************************************
File "/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx", line 570:
    sage: m.viterbi([0,1,10,10,1])
Expected:
    ([0, 0, 1, 1, 0], -9.0604285688230899)
Got:
    ([0, 0, 1, 1, 0], -9.0604285688230917)
**********************************************************************
File "/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx", line 132:
    sage: m.baum_welch(obs)
Expected:
    (-10.610333495739708, 14)
Got:
    (-10.61033349573971, 14)
**********************************************************************
File "/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx", line 134:
    sage: m.log_likelihood(obs)
Expected:
    -10.610333495739708
Got:
    -10.61033349573971
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_15
   2 of  12 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/palmieri/.sage_fulvia/tmp/.doctest_chmm.py
	 [11.4 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/9735





---

archive/issue_comments_095033.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-12T22:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9735#issuecomment-95033",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_events_024376.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-08-12T22:04:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9735#event-24376"
}
```



---

archive/issue_comments_095034.json:
```json
{
    "body": "Attachment [trac_9735-chmm-noise.patch](tarball://root/attachments/some-uuid/ticket9735/trac_9735-chmm-noise.patch) by @jhpalmieri created at 2010-08-12 22:04:05\n\nHere's a patch.  This fixes the problem for me on fulvia, and test still pass on sage.math (for example).",
    "created_at": "2010-08-12T22:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9735#issuecomment-95034",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9735-chmm-noise.patch](tarball://root/attachments/some-uuid/ticket9735/trac_9735-chmm-noise.patch) by @jhpalmieri created at 2010-08-12 22:04:05

Here's a patch.  This fixes the problem for me on fulvia, and test still pass on sage.math (for example).



---

archive/issue_comments_095035.json:
```json
{
    "body": "Thanks for writing the doctest John. \n\nHere's a couple of things worth noting\n\n == Comments by others about this issue ==\n\n\n```\nFWIW, here is the exact expected result in (obtained from my own\nimplementation, no proof but seems to be the same):\n([0, 0, 1, 1, 0], -5/2*log(pi) - 15/2*log(2) - 1)\n\nand in high precision:\n([0, 0, 1, 1, 0],\n-9.0604285688230902559878092893189710396844880399901933346892)\n\n       Yann\n```\n\nand another from William Stein that:\n\n```\nI'm the upstream author of 100% of this code, and know precisely what\nit does, which is a sequence of floating point ops and calls to the\nmath library, which *of course* can be machine dependent.\n\nPut in dots.\n\n -- William\n```\n\n == Test results on my Sun Ultra 27 ==\n\nPrior to adding your patch I got a failure recorded in ptestlong.log, as noted in the ticket's description. After adding your patch, this passes. \n\n```\ndrkirkby@hawk:~/32/sage-4.5.3.alpha0$ ./sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx\nsage -t -long \"devel/sage/sage/stats/hmm/chmm.pyx\"          \n\t [11.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 11.2 seconds\n```\n\nSo positive review. \n\nDave",
    "created_at": "2010-08-13T04:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9735#issuecomment-95035",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thanks for writing the doctest John. 

Here's a couple of things worth noting

 == Comments by others about this issue ==


```
FWIW, here is the exact expected result in (obtained from my own
implementation, no proof but seems to be the same):
([0, 0, 1, 1, 0], -5/2*log(pi) - 15/2*log(2) - 1)

and in high precision:
([0, 0, 1, 1, 0],
-9.0604285688230902559878092893189710396844880399901933346892)

       Yann
```

and another from William Stein that:

```
I'm the upstream author of 100% of this code, and know precisely what
it does, which is a sequence of floating point ops and calls to the
math library, which *of course* can be machine dependent.

Put in dots.

 -- William
```

 == Test results on my Sun Ultra 27 ==

Prior to adding your patch I got a failure recorded in ptestlong.log, as noted in the ticket's description. After adding your patch, this passes. 

```
drkirkby@hawk:~/32/sage-4.5.3.alpha0$ ./sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx
sage -t -long "devel/sage/sage/stats/hmm/chmm.pyx"          
	 [11.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 11.2 seconds
```

So positive review. 

Dave



---

archive/issue_comments_095036.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-13T04:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9735#issuecomment-95036",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095037.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-16T21:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9735#issuecomment-95037",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_095038.json:
```json
{
    "body": "Sage 4.6.prealpha3, which includes this ticket, passed all tests (`ptestlong`) on 64-bit Fedora 13 (Core2, gcc 4.4.4), see also http://trac.sagemath.org/sage_trac/ticket/9343#comment:308 .",
    "created_at": "2010-08-23T14:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9735#issuecomment-95038",
    "user": "https://github.com/nexttime"
}
```

Sage 4.6.prealpha3, which includes this ticket, passed all tests (`ptestlong`) on 64-bit Fedora 13 (Core2, gcc 4.4.4), see also http://trac.sagemath.org/sage_trac/ticket/9343#comment:308 .



---

archive/issue_comments_095039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-24T02:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9735#issuecomment-95039",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024377.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-24T02:49:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9735",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9735#event-24377"
}
```
