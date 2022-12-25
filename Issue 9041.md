# Issue 9041: python fails to build _socket on OpenSolaris x64, so pygments fails to build.

archive/issues_009041.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @robertwb\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.4.2\n* gcc 4.4.4\n\n## How gcc 4.4.4 was configured\nSince the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. \n\n```\ndrkirkby@hawk:~/sage-4.4.2$ gcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC) \n```\n\ngcc 4.3.4 was failing to build iconv. \n\n## How the Sage build was attempted\n* 64-bit build. SAGE64 was set to \"yes\"\n* #9008 update zlib to latest upstream release to allow a 64-bit library to be built. \n* #9009 update mercurial spkg to build 64-bit.\n* #7982 update sage_fortran so it can build 64-bit binaries.\n* Run 'make -k' to skip over errors, to allow one to find the errors quickly. \n\n\n## The problem\nThis a problem with python rather than pygments and is **very** similar to #9022. Since python is not building _socket, so some other parts of Sage fail to build if they need _socket. \n\n```\nygments-0.11.1.p0/.hg/undo.branch\npygments-0.11.1.p0/.hg/00changelog.i\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC)\n****************************************************\nTraceback (most recent call last):\n  File \"setup.py\", line 4, in <module>\n    ez_setup.use_setuptools()\n  File \"/export/home/drkirkby/sage-4.4.2/spkg/build/pygments-0.11.1.p0/src/ez_setup.py\", line 78, in use_setuptools\n    egg = download_setuptools(version, download_base, to_dir, download_delay)\n  File \"/export/home/drkirkby/sage-4.4.2/spkg/build/pygments-0.11.1.p0/src/ez_setup.py\", line 105, in download_setuptools\n    import urllib2, shutil\n  File \"/export/home/drkirkby/sage-4.4.2/local/lib/python/urllib2.py\", line 92, in <module>\n    import httplib\n  File \"/export/home/drkirkby/sage-4.4.2/local/lib/python/httplib.py\", line 70, in <module>\n    import socket\n  File \"/export/home/drkirkby/sage-4.4.2/local/lib/python/socket.py\", line 46, in <module>\n    import _socket\nImportError: No module named _socket\nError installing Pygments.\n\nreal    0m0.028s\nuser    0m0.013s\nsys     0m0.014s\nsage: An error occurred while installing pygments-0.11.1.p0\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9041\n\n",
    "created_at": "2010-05-25T01:01:29Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "python fails to build _socket on OpenSolaris x64, so pygments fails to build.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9041",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @robertwb

## Build environment
* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
* OpenSolaris 2009.06 snv_111b X86
* Sage 4.4.2
* gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 

```
drkirkby@hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```

gcc 4.3.4 was failing to build iconv. 

## How the Sage build was attempted
* 64-bit build. SAGE64 was set to "yes"
* #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
* #9009 update mercurial spkg to build 64-bit.
* #7982 update sage_fortran so it can build 64-bit binaries.
* Run 'make -k' to skip over errors, to allow one to find the errors quickly. 


## The problem
This a problem with python rather than pygments and is **very** similar to #9022. Since python is not building _socket, so some other parts of Sage fail to build if they need _socket. 

```
ygments-0.11.1.p0/.hg/undo.branch
pygments-0.11.1.p0/.hg/00changelog.i
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC)
****************************************************
Traceback (most recent call last):
  File "setup.py", line 4, in <module>
    ez_setup.use_setuptools()
  File "/export/home/drkirkby/sage-4.4.2/spkg/build/pygments-0.11.1.p0/src/ez_setup.py", line 78, in use_setuptools
    egg = download_setuptools(version, download_base, to_dir, download_delay)
  File "/export/home/drkirkby/sage-4.4.2/spkg/build/pygments-0.11.1.p0/src/ez_setup.py", line 105, in download_setuptools
    import urllib2, shutil
  File "/export/home/drkirkby/sage-4.4.2/local/lib/python/urllib2.py", line 92, in <module>
    import httplib
  File "/export/home/drkirkby/sage-4.4.2/local/lib/python/httplib.py", line 70, in <module>
    import socket
  File "/export/home/drkirkby/sage-4.4.2/local/lib/python/socket.py", line 46, in <module>
    import _socket
ImportError: No module named _socket
Error installing Pygments.

real    0m0.028s
user    0m0.013s
sys     0m0.014s
sage: An error occurred while installing pygments-0.11.1.p0
```

Issue created by migration from https://trac.sagemath.org/ticket/9041





---

archive/issue_events_022140.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-05-25T14:57:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9041#event-22140"
}
```



---

archive/issue_comments_083562.json:
```json
{
    "body": "I've since reported this as a bug\n\nhttp://bugs.python.org/issue8852\n\nand with the aid of a Python developer, I have managed to find a workaround.",
    "created_at": "2010-05-30T05:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83562",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've since reported this as a bug

http://bugs.python.org/issue8852

and with the aid of a Python developer, I have managed to find a workaround.



---

archive/issue_comments_083563.json:
```json
{
    "body": "The failure of _socket to build is also causing ipython to fail to build - see #9022. Once I've produced a patch, hopefully both ipython and pygments will build ok. \n\nDave",
    "created_at": "2010-05-30T05:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83563",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The failure of _socket to build is also causing ipython to fail to build - see #9022. Once I've produced a patch, hopefully both ipython and pygments will build ok. 

Dave



---

archive/issue_comments_083564.json:
```json
{
    "body": "The updated spkg is now ready for review at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg\n\nThe attached patch looks huge, since it includes a huge C file (patches/Modules.socketmodule.c) which is largely untouched from the original Python file (Modules/socketmodule.c) Only the following 3 files really need to be looked at \n* SPKG.txt\n* spkg-install\n* patches/Modules.socketmodule.diff (the diff from the original python file). \n\nThis contains a fix from Robert Bradsure for #9042, which I've given positive review to. \n\nThe new python package has been tested on the following platforms, and found to work ok. \n\n == Testing on OS X (bsd.math) ==\nThe test was performed using Sage 4.4.2\n\n```\nSleeping for three seconds before testing python\nmath module OK\nhashlib module imported\n\nreal\t5m26.771s\nuser\t2m13.789s\nsys\t0m40.901s\nSuccessfully installed python-2.6.4.p9\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing python-2.6.4.p9.spkg\n```\nI've checked that _socket builds - it is not listed in the list of either:\n* Modules where Python could not find the necessary parts, **or**\n* Modules which failed to build\n\n == Testing on Linux (sage.math) ==\nThe test was performed using Sage 4.4.2\n\n```\nSleeping for three seconds before testing python\nmath module OK\nhashlib module imported\n\nreal\t4m5.736s\nuser\t2m21.730s\nsys\t0m39.420s\nSuccessfully installed python-2.6.4.p9\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing python-2.6.4.p9.spkg\n```\nAgain, the _socket module builds. \n\n == Testing on OpenSolaris 06/2009 build 134 on my Sun Ultra 27 (Xeon processor) ==\nThe test was performed using Sage 4.4.2.\n\n```\nmath module OK\nhashlib module imported\n\nreal\t1m35.872s\nuser\t1m17.241s\nsys\t0m12.711s\nSuccessfully installed python-2.6.4.p9\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p9\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing python-2.6.4.p9.spkg\n```\nObviously _socket builds there, otherwise I would not be submitted this as a patch!\n\n## Testing on Solaris 10 on SPARC (my own Sun Blade 1000)\nThe test was performed using Sage 4.4.rc0. Any differences between 4.4.rc0 and 4.4.2 should not affect the building of the python package. \n\nI've not bothered testing on the SPARC-based Sun T5240 't2.math', as I don't have a build of Sage on 't2'. But my own Sun Blade 1000 (SPARC based) has an older release of Solaris 10. The fact the python module builds on that, should ensure it builds on any later release of Solaris 10 on SPARC. \n\n```\nSleeping for three seconds before testing python\nmath module OK\nhashlib module imported\n\nreal    14m32.311s\nuser    11m15.781s\nsys     2m22.087s\nSuccessfully installed python-2.6.4.p9\n```\nAgain, the _socket module builds ok. \n\n\n## Notes to the release manager\n1) This package includes the fix from Robert Bradsure #9042. The patch must be applied after that at #9042. The package here at \nhttp://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg can replace Robert's python-2.6.4.p8.spkg\n\n2) Once this is closed #9022 can be closed too, since the root cause of the problem at #9022 is the same as here. A python module failed to build, so two parts of Sage would not build. \n\nDave",
    "created_at": "2010-05-30T09:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83564",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The updated spkg is now ready for review at 

http://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg

The attached patch looks huge, since it includes a huge C file (patches/Modules.socketmodule.c) which is largely untouched from the original Python file (Modules/socketmodule.c) Only the following 3 files really need to be looked at 
* SPKG.txt
* spkg-install
* patches/Modules.socketmodule.diff (the diff from the original python file). 

This contains a fix from Robert Bradsure for #9042, which I've given positive review to. 

The new python package has been tested on the following platforms, and found to work ok. 

 == Testing on OS X (bsd.math) ==
The test was performed using Sage 4.4.2

```
Sleeping for three seconds before testing python
math module OK
hashlib module imported

real	5m26.771s
user	2m13.789s
sys	0m40.901s
Successfully installed python-2.6.4.p9
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.4.p9.spkg
```
I've checked that _socket builds - it is not listed in the list of either:
* Modules where Python could not find the necessary parts, **or**
* Modules which failed to build

 == Testing on Linux (sage.math) ==
The test was performed using Sage 4.4.2

```
Sleeping for three seconds before testing python
math module OK
hashlib module imported

real	4m5.736s
user	2m21.730s
sys	0m39.420s
Successfully installed python-2.6.4.p9
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.4.p9.spkg
```
Again, the _socket module builds. 

 == Testing on OpenSolaris 06/2009 build 134 on my Sun Ultra 27 (Xeon processor) ==
The test was performed using Sage 4.4.2.

```
math module OK
hashlib module imported

real	1m35.872s
user	1m17.241s
sys	0m12.711s
Successfully installed python-2.6.4.p9
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p9
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.4.p9.spkg
```
Obviously _socket builds there, otherwise I would not be submitted this as a patch!

## Testing on Solaris 10 on SPARC (my own Sun Blade 1000)
The test was performed using Sage 4.4.rc0. Any differences between 4.4.rc0 and 4.4.2 should not affect the building of the python package. 

I've not bothered testing on the SPARC-based Sun T5240 't2.math', as I don't have a build of Sage on 't2'. But my own Sun Blade 1000 (SPARC based) has an older release of Solaris 10. The fact the python module builds on that, should ensure it builds on any later release of Solaris 10 on SPARC. 

```
Sleeping for three seconds before testing python
math module OK
hashlib module imported

real    14m32.311s
user    11m15.781s
sys     2m22.087s
Successfully installed python-2.6.4.p9
```
Again, the _socket module builds ok. 


## Notes to the release manager
1) This package includes the fix from Robert Bradsure #9042. The patch must be applied after that at #9042. The package here at 
http://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg can replace Robert's python-2.6.4.p8.spkg

2) Once this is closed #9022 can be closed too, since the root cause of the problem at #9022 is the same as here. A python module failed to build, so two parts of Sage would not build. 

Dave



---

archive/issue_comments_083565.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-30T09:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83565",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083566.json:
```json
{
    "body": "Since Mike Hansen had already created a python-2.6.4.p8.spkg which is in sage-4.4.3.alpha0, I've updated the python-2.6.4.p8.spkg from sage-4.4.3.alpha0 to include\n \n* Roberts changes\n* My own changes. \n\nIt is ready for review at http://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg",
    "created_at": "2010-05-30T21:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83566",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Since Mike Hansen had already created a python-2.6.4.p8.spkg which is in sage-4.4.3.alpha0, I've updated the python-2.6.4.p8.spkg from sage-4.4.3.alpha0 to include
 
* Roberts changes
* My own changes. 

It is ready for review at http://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg



---

archive/issue_comments_083567.json:
```json
{
    "body": "Mercurial patch to get _socket to build on OpenSolaris",
    "created_at": "2010-05-30T22:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83567",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch to get _socket to build on OpenSolaris



---

archive/issue_comments_083568.json:
```json
{
    "body": "Attachment [permit_underscore_socket_to_build.patch](tarball://root/attachments/some-uuid/ticket9041/permit_underscore_socket_to_build.patch) by @jaapspies created at 2010-06-12 12:16:52\n\nTested on OpenSolaris x86 and Fedora 12. With all other tests given, this is ok.\n\nPositive review.\n\nJaap",
    "created_at": "2010-06-12T12:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83568",
    "user": "https://github.com/jaapspies"
}
```

Attachment [permit_underscore_socket_to_build.patch](tarball://root/attachments/some-uuid/ticket9041/permit_underscore_socket_to_build.patch) by @jaapspies created at 2010-06-12 12:16:52

Tested on OpenSolaris x86 and Fedora 12. With all other tests given, this is ok.

Positive review.

Jaap



---

archive/issue_comments_083569.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-12T12:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83569",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083570.json:
```json
{
    "body": "#9295, which has received positive review, contains the changes here, and also add an spkg-check file. As such, there is no need for this to be merged. As soon as #9295 is closed, so this can be closed. \n\nDave",
    "created_at": "2010-06-21T20:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83570",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#9295, which has received positive review, contains the changes here, and also add an spkg-check file. As such, there is no need for this to be merged. As soon as #9295 is closed, so this can be closed. 

Dave



---

archive/issue_comments_083571.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83571",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_022141.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-25T15:49:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9041#event-22141"
}
```



---

archive/issue_comments_083572.json:
```json
{
    "body": "To give proper credit, I'm closing this as if I've merged the changes here. See #9295.",
    "created_at": "2010-06-25T15:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9041#issuecomment-83572",
    "user": "https://github.com/rlmill"
}
```

To give proper credit, I'm closing this as if I've merged the changes here. See #9295.
