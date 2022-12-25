# Issue 8440: Removal of pyprocessing causing problems as _multiprocessing not building on Solaris

archive/issues_008440.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @mwhansen @jhpalmieri @williamstein mvngu @jaapspies\n\nSince #6503 removed pyprocessing from Sage, multiprocessing (or perhaps _multiprocessing) is needed, but this is not building on Solaris 10 SPARC. \n\n```\ngcc -fPIC -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -DHAVE_SEM_OPEN=1 -DHAVE_FD_TRANSFER=1 -DHAVE_SEM_TIMEDWAIT=1 -IModules/_multiprocessing -I. -I/export\n/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/./Include -I. -IInclude -I./Include -I/export/home/drkirkby/32/sage-4.3.4.alpha0/local/include -I/usr/local/include\n-I/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Include -I/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src -c /export/home/drkirkb\ny/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c -o build/temp.solaris-2.10-sun4u-2.6/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/bu\nild/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.o\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c: In function 'multiprocessing_sendfd':\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:100: warning: implicit declaration of function 'CMSG_SPACE'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:110: error: 'struct msghdr' has no member named 'msg_control'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:111: error: 'struct msghdr' has no member named 'msg_controllen'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:114: warning: implicit declaration of function 'CMSG_FIRSTHDR'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:114: warning: assignment makes pointer from integer without a cast\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:117: warning: implicit declaration of function 'CMSG_LEN'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:118: error: 'struct msghdr' has no member named 'msg_controllen'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:119: warning: implicit declaration of function 'CMSG_DATA'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c: In function 'multiprocessing_recvfd':\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:145: error: 'struct msghdr' has no member named 'msg_control'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:146: error: 'struct msghdr' has no member named 'msg_controllen'\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:149: warning: assignment makes pointer from integer without a cast\n/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:153: error: 'struct msghdr' has no member named 'msg_controllen'\n```\n\nFurther down the log, the fact the _multiprocessing module has failed to build is clearly stated:\n\n```\nFailed to find the necessary bits to build these modules:\n_bsddb\t\t   _hashlib\t\t_ssl\n_tkinter\t   bsddb185\t\tgdbm\nlinuxaudiodev\t   ossaudiodev\nTo find the necessary bits, look in setup.py in detect_modules() for the module's name.\n\n\nFailed to build these modules:\n_curses\t\t   _curses_panel\t_multiprocessing\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8440\n\n",
    "closed_at": "2010-03-06T19:35:21Z",
    "created_at": "2010-03-04T23:56:41Z",
    "labels": [
        "component: porting: solaris",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Removal of pyprocessing causing problems as _multiprocessing not building on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8440",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @mwhansen @jhpalmieri @williamstein mvngu @jaapspies

Since #6503 removed pyprocessing from Sage, multiprocessing (or perhaps _multiprocessing) is needed, but this is not building on Solaris 10 SPARC. 

```
gcc -fPIC -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -DHAVE_SEM_OPEN=1 -DHAVE_FD_TRANSFER=1 -DHAVE_SEM_TIMEDWAIT=1 -IModules/_multiprocessing -I. -I/export
/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/./Include -I. -IInclude -I./Include -I/export/home/drkirkby/32/sage-4.3.4.alpha0/local/include -I/usr/local/include
-I/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Include -I/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src -c /export/home/drkirkb
y/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c -o build/temp.solaris-2.10-sun4u-2.6/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/bu
ild/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.o
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c: In function 'multiprocessing_sendfd':
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:100: warning: implicit declaration of function 'CMSG_SPACE'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:110: error: 'struct msghdr' has no member named 'msg_control'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:111: error: 'struct msghdr' has no member named 'msg_controllen'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:114: warning: implicit declaration of function 'CMSG_FIRSTHDR'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:114: warning: assignment makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:117: warning: implicit declaration of function 'CMSG_LEN'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:118: error: 'struct msghdr' has no member named 'msg_controllen'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:119: warning: implicit declaration of function 'CMSG_DATA'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c: In function 'multiprocessing_recvfd':
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:145: error: 'struct msghdr' has no member named 'msg_control'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:146: error: 'struct msghdr' has no member named 'msg_controllen'
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:149: warning: assignment makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.3.4.alpha0/spkg/build/python-2.6.4.p7/src/Modules/_multiprocessing/multiprocessing.c:153: error: 'struct msghdr' has no member named 'msg_controllen'
```

Further down the log, the fact the _multiprocessing module has failed to build is clearly stated:

```
Failed to find the necessary bits to build these modules:
_bsddb		   _hashlib		_ssl
_tkinter	   bsddb185		gdbm
linuxaudiodev	   ossaudiodev
To find the necessary bits, look in setup.py in detect_modules() for the module's name.


Failed to build these modules:
_curses		   _curses_panel	_multiprocessing
```


Issue created by migration from https://trac.sagemath.org/ticket/8440





---

archive/issue_comments_075649.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-05T03:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75649",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075650.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-05T03:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75650",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_075651.json:
```json
{
    "body": "The solution to this problem is found in the old pyprocessing package, where it says:\n\n```\n#   HAVE_FD_TRANSFER\n#     Set this to 1 to compile functions for transferring file\n#     descriptors between processes over an AF_UNIX socket using a\n#     control message with type SCM_RIGHTS.  On Unix the pickling of \n#     of socket and connection objects depends on this feature.\n#\n#     If you get errors about missing CMSG_* macros then you should\n#     set this to 0.\n```\n\nThis is not as well documented in Python's setup.py, but by setting \n\n```\nHAVE_FD_TRANSFER=0\n```\n\nin Python's top-level setup.py, the problem goes away. Python's build then reports:\n\n```\nFailed to build these modules:\n_curses\t\t_curses_panel\n```\nThe _multiprocessing module is now building ok. \n\nThe new setup.py has a Solaris-specific section, which I added. However, so reviewers can be even more confident this will only affect Solaris, the patch is only applied on Solaris. \n\nI also took time to address a minor issue at #8356, where '--without-libpng' was used, despite the fact the option is no longer recognised. \n\n == Notes for Release Manager ==\n**Prerequisites:**\n\n* #7867 (This already has positive review)\n\nThis patch should be applied on top of the changes at #7867\n\nOnce this ticket is closed, #8356 may be closed too. \n\nIt would be appreciated if #8374, #8375, 8391 and #8404 could also be integrated into the next alpha, as that would have a high probability of allowing all doc tests to pass. All these tickets have positive review.",
    "created_at": "2010-03-05T03:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75651",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The solution to this problem is found in the old pyprocessing package, where it says:

```
#   HAVE_FD_TRANSFER
#     Set this to 1 to compile functions for transferring file
#     descriptors between processes over an AF_UNIX socket using a
#     control message with type SCM_RIGHTS.  On Unix the pickling of 
#     of socket and connection objects depends on this feature.
#
#     If you get errors about missing CMSG_* macros then you should
#     set this to 0.
```

This is not as well documented in Python's setup.py, but by setting 

```
HAVE_FD_TRANSFER=0
```

in Python's top-level setup.py, the problem goes away. Python's build then reports:

```
Failed to build these modules:
_curses		_curses_panel
```
The _multiprocessing module is now building ok. 

The new setup.py has a Solaris-specific section, which I added. However, so reviewers can be even more confident this will only affect Solaris, the patch is only applied on Solaris. 

I also took time to address a minor issue at #8356, where '--without-libpng' was used, despite the fact the option is no longer recognised. 

 == Notes for Release Manager ==
**Prerequisites:**

* #7867 (This already has positive review)

This patch should be applied on top of the changes at #7867

Once this ticket is closed, #8356 may be closed too. 

It would be appreciated if #8374, #8375, 8391 and #8404 could also be integrated into the next alpha, as that would have a high probability of allowing all doc tests to pass. All these tickets have positive review.



---

archive/issue_comments_075652.json:
```json
{
    "body": "I forgot to put the location of the package\n\nhttp://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg\n\nPatch will be attached in a minute",
    "created_at": "2010-03-05T03:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75652",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I forgot to put the location of the package

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg

Patch will be attached in a minute



---

archive/issue_comments_075653.json:
```json
{
    "body": "Attachment [8440-python.patch](tarball://root/attachments/some-uuid/ticket8440/8440-python.patch) by drkirkby created at 2010-03-05 03:28:03\n\nMercurial patch",
    "created_at": "2010-03-05T03:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75653",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [8440-python.patch](tarball://root/attachments/some-uuid/ticket8440/8440-python.patch) by drkirkby created at 2010-03-05 03:28:03

Mercurial patch



---

archive/issue_comments_075654.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-05T04:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075655.json:
```json
{
    "body": "The updated package [python-2.6.4.p7.spkg](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg) needs a minor clean up:\n\n```\n[mvngu@sage python-2.6.4.p7]$ hg status\n? patches/locale.pyc\n```\nThat is, we don't place Python bytecode under revision control. Nor do we put any binary or Python bytecode under the directory \"patches/\".",
    "created_at": "2010-03-05T04:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The updated package [python-2.6.4.p7.spkg](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg) needs a minor clean up:

```
[mvngu@sage python-2.6.4.p7]$ hg status
? patches/locale.pyc
```
That is, we don't place Python bytecode under revision control. Nor do we put any binary or Python bytecode under the directory "patches/".



---

archive/issue_comments_075656.json:
```json
{
    "body": "Hi Minh, \nI need to go out very soon and get a train, so don't have time to fully investigate this, but there appears there may be something wrong on the math's computer setup, as what I am putting there, and what I can see in the browser are not the same. (This could be the fact the ZIL log is disabled - complex story, and one I need to discuss again with William). \n\n\nThere **should** be a .spkg in the directory http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/ \n\nwhich does (for me at least) **not** have any such file or problem. There **should** be a directory below that where I extracted the file. But when I look with the browser, I can **not**  see any of it! So in summary. \n\n* I don't see the problem you do. \n* Changes I am making on the file system do not appear to be reflected in what I can see from my browser. \n\nIf you look at this location, you might find the package, but I'm totally confused. I think the file system might be messed up. \n\n```\nkirkby@t2:[/home/kirkby/portability/python-2.6.4.p7] $ ls \npython-2.6.4.p7       python-2.6.4.p7.spkg\nkirkby@t2:[/home/kirkby/portability/python-2.6.4.p7] $ \n```\n\nI will have to look later, as I need to go out now. \n\nDave",
    "created_at": "2010-03-05T08:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75656",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi Minh, 
I need to go out very soon and get a train, so don't have time to fully investigate this, but there appears there may be something wrong on the math's computer setup, as what I am putting there, and what I can see in the browser are not the same. (This could be the fact the ZIL log is disabled - complex story, and one I need to discuss again with William). 


There **should** be a .spkg in the directory http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/ 

which does (for me at least) **not** have any such file or problem. There **should** be a directory below that where I extracted the file. But when I look with the browser, I can **not**  see any of it! So in summary. 

* I don't see the problem you do. 
* Changes I am making on the file system do not appear to be reflected in what I can see from my browser. 

If you look at this location, you might find the package, but I'm totally confused. I think the file system might be messed up. 

```
kirkby@t2:[/home/kirkby/portability/python-2.6.4.p7] $ ls 
python-2.6.4.p7       python-2.6.4.p7.spkg
kirkby@t2:[/home/kirkby/portability/python-2.6.4.p7] $ 
```

I will have to look later, as I need to go out now. 

Dave



---

archive/issue_comments_075657.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-03-05T15:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75657",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_075658.json:
```json
{
    "body": "I managed to look at this in more detail today. The reason the directory was not visable was a permissions problem, and nothing to do with file system errors. \n\nI still can't understand why you see this odd file, as I don't:\n\n```\nkirkby@sage:~/portability/python-2.6.4.p7/python-2.6.4.p7$ ls patches/locale.pyc\nls: cannot access patches/locale.pyc: No such file or directory\nkirkby@sage:~/portability/python-2.6.4.p7/python-2.6.4.p7$ hg status\n\n```",
    "created_at": "2010-03-05T15:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75658",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I managed to look at this in more detail today. The reason the directory was not visable was a permissions problem, and nothing to do with file system errors. 

I still can't understand why you see this odd file, as I don't:

```
kirkby@sage:~/portability/python-2.6.4.p7/python-2.6.4.p7$ ls patches/locale.pyc
ls: cannot access patches/locale.pyc: No such file or directory
kirkby@sage:~/portability/python-2.6.4.p7/python-2.6.4.p7$ hg status

```



---

archive/issue_comments_075659.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-06T12:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75659",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_075660.json:
```json
{
    "body": "Minh, \n\ncould you double- check you are using the same package as me, since I simply can't see this spurious file.",
    "created_at": "2010-03-06T12:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75660",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Minh, 

could you double- check you are using the same package as me, since I simply can't see this spurious file.



---

archive/issue_comments_075661.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> could you double- check you are using the same package as me, since I simply can't see this spurious file. \n\n\nI have re-checked [python-2.6.4.p7.spkg](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg) and indeed it's OK by me. I have no idea why I received the warning about a bytecode file under the directory `patches/`. What I would usually do is take an spkg that has been compressed or just tarball'd, and unpack it. Then I would go through that unpacked spkg with Mercurial to make sure that Mercurial is happy with the repository under consideration. I have built [python-2.6.4.p7.spkg](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg) on the following:\n\n* bsd.math\n* Cygwin (winxp1 on boxen.math)\n* rosemary.math\n* sage.math\n* t2.math\n\nOn all systems/platforms that I tested, the said Python package builds as claimed. Where relevant (i.e. bsd.math, rosemary.math, sage.math), all doctests passed.",
    "created_at": "2010-03-06T19:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75661",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:7 drkirkby]:
> could you double- check you are using the same package as me, since I simply can't see this spurious file. 


I have re-checked [python-2.6.4.p7.spkg](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg) and indeed it's OK by me. I have no idea why I received the warning about a bytecode file under the directory `patches/`. What I would usually do is take an spkg that has been compressed or just tarball'd, and unpack it. Then I would go through that unpacked spkg with Mercurial to make sure that Mercurial is happy with the repository under consideration. I have built [python-2.6.4.p7.spkg](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg) on the following:

* bsd.math
* Cygwin (winxp1 on boxen.math)
* rosemary.math
* sage.math
* t2.math

On all systems/platforms that I tested, the said Python package builds as claimed. Where relevant (i.e. bsd.math, rosemary.math, sage.math), all doctests passed.



---

archive/issue_comments_075662.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T19:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75662",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T19:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75663",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_020239.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-06T19:35:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8440#event-20239"
}
```



---

archive/issue_comments_075664.json:
```json
{
    "body": "#8356 can be closed too following the inclusion of this updated python package. \n\n\ndave",
    "created_at": "2010-03-07T01:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8440#issuecomment-75664",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#8356 can be closed too following the inclusion of this updated python package. 


dave
