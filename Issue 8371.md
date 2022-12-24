# Issue 8371: Error building pyprocessing on Solaris SPARC after changes to python.

archive/issues_008371.json:
```json
{
    "body": "Assignee: drkirkby\n\n == The computer hardware & software ==\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM \n* Solaris 10 03/2005 - the first release of Solaris 10. \n\n == The Sage software ==\nSage 4.3.3 which comes with python-2.6.4.p5 and pyprocessing-0.52.p0\n \n == The problem ==\nThis is a long story, so I'll keep it short. \n* #6583 \"Implement 2-isogeny descent over QQ natively in Sage using ratpoints\" was integrated into Sage 4.3.1.\n* The above patch, which was not properly checked on Solaris, broke the Solaris build as reported at #7867\n* Jaap Spies found this link http://bugs.python.org/issue1759169  which suggests this is a bug in python, which will be fixed in the next 2.6 release. But a patch is provided on the python web site. \n* #6503 is an 8-month old patch to remove pyprocessing from Sage, as the multiprocessing module, which has a slightly different API, is now part of Python 2.6. \n* The patch at http://bugs.python.org/issue1759169  was integrated into python-2.6.4.p5, but it broke the build of pyprocessing as below \n  {{{\ncopying doc/connection-objects.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc\ncopying doc/programming-guidelines.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc\ncopying doc/intro.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc\ncopying doc/CHANGES.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc\ncopying doc/html4css1.css -> build/lib.solaris-2.10-sun4u-2.6/processing/doc\ncopying doc/../index.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc/..\nrunning build_ext\nbuilding 'processing._processing' extension\ncreating build/temp.solaris-2.10-sun4u-2.6\ncreating build/temp.solaris-2.10-sun4u-2.6/src\ngcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_SEM_OPEN=1 -DHAVE_FD_TRANSFER=1 -DHAVE_SEM_TIMEDWAIT=1 -I/export/home/drkirkby/sage-4.3.3/local/include/python2.6 -c src/processing.c -o build/temp.solaris-2.10-sun4u-2.6/src/processing.o\nsrc/processing.c: In function 'processing_sendfd':\nsrc/processing.c:158: warning: implicit declaration of function 'CMSG_SPACE'\nsrc/processing.c:168: error: 'struct msghdr' has no member named 'msg_control'\nsrc/processing.c:169: error: 'struct msghdr' has no member named 'msg_controllen'\nsrc/processing.c:172: warning: implicit declaration of function 'CMSG_FIRSTHDR'\nsrc/processing.c:172: warning: assignment makes pointer from integer without a cast\nsrc/processing.c:175: warning: implicit declaration of function 'CMSG_LEN'\nsrc/processing.c:176: error: 'struct msghdr' has no member named 'msg_controllen'\nsrc/processing.c:177: warning: implicit declaration of function 'CMSG_DATA'\nsrc/processing.c: In function 'processing_recvfd':\nsrc/processing.c:203: error: 'struct msghdr' has no member named 'msg_control'\nsrc/processing.c:204: error: 'struct msghdr' has no member named 'msg_controllen'\nsrc/processing.c:207: warning: assignment makes pointer from integer without a cast\nsrc/processing.c:211: error: 'struct msghdr' has no member named 'msg_controllen'\nerror: command 'gcc' failed with exit status 1\n\nreal    0m0.791s\nuser    0m0.532s\nsys     0m0.189s\nsage: An error occurred while installing pyprocessing-0.52.p0\n   }}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/8371\n\n",
    "created_at": "2010-02-25T23:25:45Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "Error building pyprocessing on Solaris SPARC after changes to python.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8371",
    "user": "drkirkby"
}
```
Assignee: drkirkby

 == The computer hardware & software ==
* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM 
* Solaris 10 03/2005 - the first release of Solaris 10. 

 == The Sage software ==
Sage 4.3.3 which comes with python-2.6.4.p5 and pyprocessing-0.52.p0
 
 == The problem ==
This is a long story, so I'll keep it short. 
* #6583 "Implement 2-isogeny descent over QQ natively in Sage using ratpoints" was integrated into Sage 4.3.1.
* The above patch, which was not properly checked on Solaris, broke the Solaris build as reported at #7867
* Jaap Spies found this link http://bugs.python.org/issue1759169  which suggests this is a bug in python, which will be fixed in the next 2.6 release. But a patch is provided on the python web site. 
* #6503 is an 8-month old patch to remove pyprocessing from Sage, as the multiprocessing module, which has a slightly different API, is now part of Python 2.6. 
* The patch at http://bugs.python.org/issue1759169  was integrated into python-2.6.4.p5, but it broke the build of pyprocessing as below 
  {{{
copying doc/connection-objects.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc
copying doc/programming-guidelines.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc
copying doc/intro.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc
copying doc/CHANGES.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc
copying doc/html4css1.css -> build/lib.solaris-2.10-sun4u-2.6/processing/doc
copying doc/../index.html -> build/lib.solaris-2.10-sun4u-2.6/processing/doc/..
running build_ext
building 'processing._processing' extension
creating build/temp.solaris-2.10-sun4u-2.6
creating build/temp.solaris-2.10-sun4u-2.6/src
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_SEM_OPEN=1 -DHAVE_FD_TRANSFER=1 -DHAVE_SEM_TIMEDWAIT=1 -I/export/home/drkirkby/sage-4.3.3/local/include/python2.6 -c src/processing.c -o build/temp.solaris-2.10-sun4u-2.6/src/processing.o
src/processing.c: In function 'processing_sendfd':
src/processing.c:158: warning: implicit declaration of function 'CMSG_SPACE'
src/processing.c:168: error: 'struct msghdr' has no member named 'msg_control'
src/processing.c:169: error: 'struct msghdr' has no member named 'msg_controllen'
src/processing.c:172: warning: implicit declaration of function 'CMSG_FIRSTHDR'
src/processing.c:172: warning: assignment makes pointer from integer without a cast
src/processing.c:175: warning: implicit declaration of function 'CMSG_LEN'
src/processing.c:176: error: 'struct msghdr' has no member named 'msg_controllen'
src/processing.c:177: warning: implicit declaration of function 'CMSG_DATA'
src/processing.c: In function 'processing_recvfd':
src/processing.c:203: error: 'struct msghdr' has no member named 'msg_control'
src/processing.c:204: error: 'struct msghdr' has no member named 'msg_controllen'
src/processing.c:207: warning: assignment makes pointer from integer without a cast
src/processing.c:211: error: 'struct msghdr' has no member named 'msg_controllen'
error: command 'gcc' failed with exit status 1

real    0m0.791s
user    0m0.532s
sys     0m0.189s
sage: An error occurred while installing pyprocessing-0.52.p0
   }}}

Issue created by migration from https://trac.sagemath.org/ticket/8371





---

archive/issue_comments_074831.json:
```json
{
    "body": "The revised spkg can be found at:\n\nhttp://boxen.math.washington.edu/home/kirkby/Solaris-fixes/pyprocessing-0.52.p1/pyprocessing-0.52.p1.spkg\n\nThe Mercurial patch is attached.",
    "created_at": "2010-03-01T15:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74831",
    "user": "drkirkby"
}
```

The revised spkg can be found at:

http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/pyprocessing-0.52.p1/pyprocessing-0.52.p1.spkg

The Mercurial patch is attached.



---

archive/issue_comments_074832.json:
```json
{
    "body": "Mercurial patch",
    "created_at": "2010-03-01T15:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74832",
    "user": "drkirkby"
}
```

Mercurial patch



---

archive/issue_comments_074833.json:
```json
{
    "body": "Attachment [Solaris-specific-patch-for-pyprocessing.patch](tarball://root/attachments/some-uuid/ticket8371/Solaris-specific-patch-for-pyprocessing.patch) by drkirkby created at 2010-03-01 15:21:56",
    "created_at": "2010-03-01T15:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74833",
    "user": "drkirkby"
}
```

Attachment [Solaris-specific-patch-for-pyprocessing.patch](tarball://root/attachments/some-uuid/ticket8371/Solaris-specific-patch-for-pyprocessing.patch) by drkirkby created at 2010-03-01 15:21:56



---

archive/issue_comments_074834.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-01T15:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74834",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074835.json:
```json
{
    "body": "Updating to blocker, as this essential for a succesful Solaris build. However, if #6503 is merged, then this can be ignored, as that intends removing all of pyprocessing. But the ticket is 8 months old.",
    "created_at": "2010-03-01T16:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74835",
    "user": "drkirkby"
}
```

Updating to blocker, as this essential for a succesful Solaris build. However, if #6503 is merged, then this can be ignored, as that intends removing all of pyprocessing. But the ticket is 8 months old.



---

archive/issue_comments_074836.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-01T16:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74836",
    "user": "drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_074837.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-03-03T02:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74837",
    "user": "mvngu"
}
```

Resolution: wontfix



---

archive/issue_comments_074838.json:
```json
{
    "body": "Closing this as wontfix since #6503 removes pyprocessing from the standard spkg repository.",
    "created_at": "2010-03-03T02:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8371#issuecomment-74838",
    "user": "mvngu"
}
```

Closing this as wontfix since #6503 removes pyprocessing from the standard spkg repository.
