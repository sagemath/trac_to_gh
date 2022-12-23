# Issue 8440: Removal of pyprocessing causing problems as _multiprocessing not building on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/8440

Original creator: drkirkby

Original creation time: 2010-03-04 23:56:41

Assignee: drkirkby

CC:  mhansen jhpalmieri was mvngu jsp

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


There is potentially a solution available here. 

http://bugs.python.org/issue3110

However, it appears there was a typo there, so that had to be changed. 

http://svn.python.org/view?view=rev&revision=73767

The latest header is at:

http://svn.python.org/view/python/trunk/Modules/_multiprocessing/multiprocessing.h

Whether this will fix the issue is unknown, but it looks at least related.


---

Comment by drkirkby created at 2010-03-05 03:23:06

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-03-05 03:23:06

Changing priority from major to blocker.


---

Comment by drkirkby created at 2010-03-05 03:23:06

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
*Prerequisites:*

 * #7867 (This already has positive review)

This patch should be applied on top of the changes at #7867

Once this ticket is closed, #8356 may be closed too. 

It would be appreciated if #8374, #8375, 8391 and #8404 could also be integrated into the next alpha, as that would have a high probability of allowing all doc tests to pass. All these tickets have positive review.


---

Comment by drkirkby created at 2010-03-05 03:26:40

I forgot to put the location of the package

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg

Patch will be attached in a minute


---

Attachment

Mercurial patch


---

Comment by mvngu created at 2010-03-05 04:03:12

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-03-05 04:03:12

The updated package [python-2.6.4.p7.spkg](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg) needs a minor clean up:

```
[mvngu@sage python-2.6.4.p7]$ hg status
? patches/locale.pyc
```

That is, we don't place Python bytecode under revision control. Nor do we put any binary or Python bytecode under the directory "patches/".


---

Comment by drkirkby created at 2010-03-05 08:52:19

Hi Minh, 
I need to go out very soon and get a train, so don't have time to fully investigate this, but there appears there may be something wrong on the math's computer setup, as what I am putting there, and what I can see in the browser are not the same. (This could be the fact the ZIL log is disabled - complex story, and one I need to discuss again with William). 


There *should* be a .spkg in the directory http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/ 

which does (for me at least) *not* have any such file or problem. There *should* be a directory below that where I extracted the file. But when I look with the browser, I can *not*  see any of it! So in summary. 

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

Comment by drkirkby created at 2010-03-05 15:17:16

Changing status from needs_work to needs_info.


---

Comment by drkirkby created at 2010-03-05 15:17:16

I managed to look at this in more detail today. The reason the directory was not visable was a permissions problem, and nothing to do with file system errors. 

I still can't understand why you see this odd file, as I don't:


```
kirkby@sage:~/portability/python-2.6.4.p7/python-2.6.4.p7$ ls patches/locale.pyc
ls: cannot access patches/locale.pyc: No such file or directory
kirkby@sage:~/portability/python-2.6.4.p7/python-2.6.4.p7$ hg status

```



---

Comment by drkirkby created at 2010-03-06 12:28:21

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-03-06 12:28:21

Minh, 

could you double- check you are using the same package as me, since I simply can't see this spurious file.


---

Comment by mvngu created at 2010-03-06 19:06:36

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

Comment by mvngu created at 2010-03-06 19:06:36

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 19:35:21

Resolution: fixed


---

Comment by drkirkby created at 2010-03-07 01:34:51

#8356 can be closed too following the inclusion of this updated python package. 


dave
