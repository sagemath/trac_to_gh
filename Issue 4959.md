# Issue 4959: r's install_packages is broken in many variants of sage

archive/issues_004959.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jasongrout mvngu\n\nSee, e.g., this from sage-devel\n\n```\nI had a similar failure today, trying to:\n\nr.install_packages(\"adapt\")\n\nafter some fussing, runing ./sage as root, and using the notebook\ninterface I could get through the download phase, but same sorts of\nfailures in just as the gcc kicks in.  Seems several of the key R\nscripts have \"/home/wstein/...\"  hard wired in to R_HOME_XXX, which\nobviously will fail.  I tried editing the R startup scripts (among\nothers) but couldn't get it to work.\n\nBTW, I installed from the latest Debian tarball into a Debian/VMWARE\nmachine just today.  So installing R packages is still an issue.\n```\n\nSince most of the value of R is the huge list of third party packages, it's very important that this get fixed. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4959\n\n",
    "created_at": "2009-01-09T16:36:50Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "r's install_packages is broken in many variants of sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4959",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @jasongrout mvngu

See, e.g., this from sage-devel

```
I had a similar failure today, trying to:

r.install_packages("adapt")

after some fussing, runing ./sage as root, and using the notebook
interface I could get through the download phase, but same sorts of
failures in just as the gcc kicks in.  Seems several of the key R
scripts have "/home/wstein/..."  hard wired in to R_HOME_XXX, which
obviously will fail.  I tried editing the R startup scripts (among
others) but couldn't get it to work.

BTW, I installed from the latest Debian tarball into a Debian/VMWARE
machine just today.  So installing R packages is still an issue.
```

Since most of the value of R is the huge list of third party packages, it's very important that this get fixed. 

Issue created by migration from https://trac.sagemath.org/ticket/4959





---

archive/issue_comments_037622.json:
```json
{
    "body": "See also #5246, which reports an extremely similar problem.  \n\nIncidentally, I have not had this problem at all in downloading a number of packages, and others have reported success lately, so it is possible this was specific to a certain release because of weird hard coding of links environment variables.  This should be tested on a few different machines with packages that do not rely on the 'recommended' packages (see #2198 and #6532 for why).",
    "created_at": "2009-12-11T20:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37622",
    "user": "https://github.com/kcrisman"
}
```

See also #5246, which reports an extremely similar problem.  

Incidentally, I have not had this problem at all in downloading a number of packages, and others have reported success lately, so it is possible this was specific to a certain release because of weird hard coding of links environment variables.  This should be tested on a few different machines with packages that do not rely on the 'recommended' packages (see #2198 and #6532 for why).



---

archive/issue_comments_037623.json:
```json
{
    "body": "Incidentally, the R package above has been removed from R, it seems.   It also seems this person was using the Debian install, which is now of course woefully out of date.",
    "created_at": "2009-12-14T16:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37623",
    "user": "https://github.com/kcrisman"
}
```

Incidentally, the R package above has been removed from R, it seems.   It also seems this person was using the Debian install, which is now of course woefully out of date.



---

archive/issue_comments_037624.json:
```json
{
    "body": "On sage.math, after picking the mirror, I get one error message for trying to install 'abind' from the r console:\n\n```\nWarning message:\nIn doTryCatch(return(expr), name, parentenv, handler) :\n  unable to load shared library '/home/.../sage-4.3.r0-sage.math.washington.edu-x86_64-Linux/local/lib/R//modules//R_X11.so':\n  /scratch/mhansen/release/4.3/rc0/sage-4.3.rc0/local/lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3/libgcc_s.so.1: version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)\nSegmentation fault\n```\nbut a different one when trying to use the r.install_packages() interface, which I unfortunately deleted.",
    "created_at": "2009-12-14T16:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37624",
    "user": "https://github.com/kcrisman"
}
```

On sage.math, after picking the mirror, I get one error message for trying to install 'abind' from the r console:

```
Warning message:
In doTryCatch(return(expr), name, parentenv, handler) :
  unable to load shared library '/home/.../sage-4.3.r0-sage.math.washington.edu-x86_64-Linux/local/lib/R//modules//R_X11.so':
  /scratch/mhansen/release/4.3/rc0/sage-4.3.rc0/local/lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3/libgcc_s.so.1: version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)
Segmentation fault
```
but a different one when trying to use the r.install_packages() interface, which I unfortunately deleted.



---

archive/issue_comments_037625.json:
```json
{
    "body": "Here is the error message from that:\n\n```\nWarning messages:\n1: In file.create(f.tg) :\n  cannot create file '/scratch/mhansen/release/4.3/rc0/sage-4.3.rc0/local/lib/R/doc/html/packages.html', reason 'Permission denied'\n2: In tools:::unix.packages.html(.Library) :\n  cannot create HTML package index\n> \n```\nSo again there seem to be problems with hard links in the R installation, since my binary wasn't in /scratch and certainly not in mhansen's scratch.",
    "created_at": "2009-12-14T18:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37625",
    "user": "https://github.com/kcrisman"
}
```

Here is the error message from that:

```
Warning messages:
1: In file.create(f.tg) :
  cannot create file '/scratch/mhansen/release/4.3/rc0/sage-4.3.rc0/local/lib/R/doc/html/packages.html', reason 'Permission denied'
2: In tools:::unix.packages.html(.Library) :
  cannot create HTML package index
> 
```
So again there seem to be problems with hard links in the R installation, since my binary wasn't in /scratch and certainly not in mhansen's scratch.



---

archive/issue_comments_037626.json:
```json
{
    "body": "And see [here](http://groups.google.com/group/sage-devel/browse_thread/thread/7f81537bf81cc05c/dd5d592c0e27966c?q=)  for reports on several other platforms.",
    "created_at": "2009-12-27T03:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37626",
    "user": "https://github.com/kcrisman"
}
```

And see [here](http://groups.google.com/group/sage-devel/browse_thread/thread/7f81537bf81cc05c/dd5d592c0e27966c?q=)  for reports on several other platforms.



---

archive/issue_comments_037627.json:
```json
{
    "body": "The behavior with the version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6) continues to be the case on boxen.math after the upgrade at #6532.  On the plus side, it no longer refers to someone else's installation.\n\nHere is another interesting error which might help us - is it possible that a number of R packages require non-universal libraries?\n\n```\n* installing *source* package \u2018rgl\u2019 ...\nchecking for gcc... gcc -std=gnu99\nchecking for C compiler default output file name... a.out\nchecking whether the C compiler works... yes\nchecking whether we are cross compiling... no\nchecking for suffix of executables... \nchecking for suffix of object files... o\nchecking whether we are using the GNU C compiler... yes\nchecking whether gcc -std=gnu99 accepts -g... yes\nchecking for gcc -std=gnu99 option to accept ISO C89... none needed\nchecking how to run the C preprocessor... gcc -std=gnu99 -E\nchecking for gcc... (cached) gcc -std=gnu99\nchecking whether we are using the GNU C compiler... (cached) yes\nchecking whether gcc -std=gnu99 accepts -g... (cached) yes\nchecking for gcc -std=gnu99 option to accept ISO C89... (cached) none needed\nchecking for libpng-config... yes\nconfigure: using libpng-config\nconfigure: using libpng dynamic linkage\nchecking for X... libraries /usr/lib, headers /usr/include\nchecking GL/gl.h usability... no\nchecking GL/gl.h presence... no\nchecking for GL/gl.h... no\nchecking GL/glu.h usability... no\nchecking GL/glu.h presence... no\nchecking for GL/glu.h... no\nconfigure: error: missing required header GL/gl.h\nERROR: configuration failed for package \u2018rgl\u2019\n```\nThis was on boxen.math; on my own Mac I did not have any problems with this package (a package installed by the package 'depth', which I needed for some other computations).  This tells me that",
    "created_at": "2009-12-28T17:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37627",
    "user": "https://github.com/kcrisman"
}
```

The behavior with the version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6) continues to be the case on boxen.math after the upgrade at #6532.  On the plus side, it no longer refers to someone else's installation.

Here is another interesting error which might help us - is it possible that a number of R packages require non-universal libraries?

```
* installing *source* package ‘rgl’ ...
checking for gcc... gcc -std=gnu99
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables... 
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc -std=gnu99 accepts -g... yes
checking for gcc -std=gnu99 option to accept ISO C89... none needed
checking how to run the C preprocessor... gcc -std=gnu99 -E
checking for gcc... (cached) gcc -std=gnu99
checking whether we are using the GNU C compiler... (cached) yes
checking whether gcc -std=gnu99 accepts -g... (cached) yes
checking for gcc -std=gnu99 option to accept ISO C89... (cached) none needed
checking for libpng-config... yes
configure: using libpng-config
configure: using libpng dynamic linkage
checking for X... libraries /usr/lib, headers /usr/include
checking GL/gl.h usability... no
checking GL/gl.h presence... no
checking for GL/gl.h... no
checking GL/glu.h usability... no
checking GL/glu.h presence... no
checking for GL/glu.h... no
configure: error: missing required header GL/gl.h
ERROR: configuration failed for package ‘rgl’
```
This was on boxen.math; on my own Mac I did not have any problems with this package (a package installed by the package 'depth', which I needed for some other computations).  This tells me that



---

archive/issue_comments_037628.json:
```json
{
    "body": "With the Fortran issues in #7485 cleared up, #6532 seems to now work to fix this.  We can definitely get rid of the warning for OSX!  Look on #7521 for that.",
    "created_at": "2010-01-25T19:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37628",
    "user": "https://github.com/kcrisman"
}
```

With the Fortran issues in #7485 cleared up, #6532 seems to now work to fix this.  We can definitely get rid of the warning for OSX!  Look on #7521 for that.



---

archive/issue_events_011465.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-25T23:26:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4959#event-11465"
}
```



---

archive/issue_comments_037629.json:
```json
{
    "body": "Close as fixed by #6532.",
    "created_at": "2010-01-25T23:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #6532.



---

archive/issue_comments_037630.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T23:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4959#issuecomment-37630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
