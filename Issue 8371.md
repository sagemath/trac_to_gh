# Issue 8371: Error building pyprocessing on Solaris SPARC after changes to python.

Issue created by migration from https://trac.sagemath.org/ticket/8371

Original creator: drkirkby

Original creation time: 2010-02-25 23:25:45

Assignee: drkirkby

*== The computer hardware & software ==
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


---

Comment by drkirkby created at 2010-03-01 15:20:53

The revised spkg can be found at:

http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/pyprocessing-0.52.p1/pyprocessing-0.52.p1.spkg

The Mercurial patch is attached.


---

Comment by drkirkby created at 2010-03-01 15:21:36

Mercurial patch


---

Attachment


---

Comment by drkirkby created at 2010-03-01 15:21:56

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-03-01 16:28:02

Updating to blocker, as this essential for a succesful Solaris build. However, if #6503 is merged, then this can be ignored, as that intends removing all of pyprocessing. But the ticket is 8 months old.


---

Comment by drkirkby created at 2010-03-01 16:28:02

Changing priority from major to blocker.


---

Comment by mvngu created at 2010-03-03 02:03:51

Resolution: wontfix


---

Comment by mvngu created at 2010-03-03 02:03:51

Closing this as wontfix since #6503 removes pyprocessing from the standard spkg repository.
