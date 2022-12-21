# Issue 9202: update matplotlib

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-10 12:17:15

Assignee: tbd

CC:  drkirkby kcrisman

This spkg updates matplotlib to 0.99.3.  I've attached the patch as well (don't apply; it's just for reviewing purposes).

The new spkg is at http://sage.math.washington.edu/home/jason/matplotlib-0.99.3.spkg


---

Comment by jason created at 2010-06-10 12:26:11

Changing status from new to needs_work.


---

Comment by jason created at 2010-06-10 12:26:11

Hmmm...trying to run something from matplotlib says:


```
Traceback (most recent call last):    q=ax.scatter(x,y)
  File "", line 1, in <module>
    
  File "/private/var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Tmp-/tmp_3GqZ9/___code___.py", line 3, in <module>
    import matplotlib.pyplot as plt
  File "/Users/grout/sage/local/lib/python2.6/site-packages/matplotlib/pyplot.py", line 6, in <module>
    from matplotlib.figure import Figure, figaspect
  File "/Users/grout/sage/local/lib/python2.6/site-packages/matplotlib/figure.py", line 18, in <module>
    from axes import Axes, SubplotBase, subplot_class_factory
  File "/Users/grout/sage/local/lib/python2.6/site-packages/matplotlib/axes.py", line 12, in <module>
    import matplotlib.axis as maxis
  File "/Users/grout/sage/local/lib/python2.6/site-packages/matplotlib/axis.py", line 10, in <module>
    import matplotlib.font_manager as font_manager
  File "/Users/grout/sage/local/lib/python2.6/site-packages/matplotlib/font_manager.py", line 52, in <module>
    from matplotlib import ft2font
ImportError: dlopen(/Users/grout/sage/local/lib/python2.6/site-packages/matplotlib/ft2font.so, 2): Library not loaded: /opt/local/lib/libfreetype.6.dylib
  Referenced from: /Users/grout/sage/local/lib/python2.6/site-packages/matplotlib/ft2font.so
  Reason: Incompatible library version: ft2font.so requires version 11.0.0 or later, but libfreetype.6.dylib provides version 10.0.0
```


So somehow this is picking up my macports version of freetype.  That's a problem.


---

Comment by drkirkby created at 2010-06-10 13:06:42

Not working on Solaris either. It still reports:


```
REQUIRED DEPENDENCIES
                 numpy: 1.3.0
             freetype2: 9.7.3
```


Freetype is really confusing in that there are 3 numbers associated with a release. Then to make matters worst, sometimes it called freetype, and other times freetype2. I think they are the same. 

```
   release    libtool      so
  -------------------------------
     2.3.12     10.0.4    6.4.0
     2.3.11     9.22.3    6.3.22
     2.3.10     9.21.3    6.3.21
     2.3.9      9.20.3    6.3.20
     2.3.8      9.19.3    6.3.19
     2.3.7      9.18.3    6.3.18
     2.3.6      9.17.3    6.3.17
     2.3.5      9.16.3    6.3.16
     2.3.4      9.15.3    6.3.15
     2.3.3      9.14.3    6.3.14
     2.3.2      9.13.3    6.3.13
     2.3.1      9.12.3    6.3.12
     2.3.0      9.11.3    6.3.11
     2.2.1      9.10.3    6.3.10
     2.2.0      9.9.3     6.3.9
     2.1.10     9.8.3     6.3.8
     2.1.9      9.7.3     6.3.7
     2.1.8      9.6.3     6.3.6 
```


freetype2 9.7.3 is also known as version 2.1.8. Since Sage 4.4.3 includes freetype 2.3.5, matplotlib should report it has found freetype2 version 9.16.3 and not 9.7.3 as it does. 

Rather inconveniently, the version of freetype globally installed on sage.math and boxen.math are the same as in Sage. This makes the message from matplotlib about the version of freetype will be the same in either case. 

||                 |                 |
||-----------------|-----------------|
||*release version*|*libtool version*|
|Latest freeetype2|2.3.12|10.0.4|
|sage.math|2.3.5|9.16.3|
|In Sage 4.4.3|2.3.5|9.16.3|
|As supplied on Solaris 10 03/05|2.1.9|9.7.3|
*I think if you manage to get matplotlib to indicate it has found freetype2, but is unable to determine the version, I think you will have solved it.* At the moment matplotlib seems to be using pkg-config on Solaris and Linux (but not OS X) to look up the version, and find the directories of the include and library files. 

Dave


---

Comment by drkirkby created at 2010-06-10 13:36:56

I forgot to add, one other change that is needed, is a revised spkg-install, to ensure matplotlib builds 64-bit. 


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="-O2 -g -m64 "; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
fi
```


should be changed to:


```
if [ "x$SAGE64" = xyes ]; then
   echo "Building a 64-bit version of matplotlib"
   CFLAGS="-O2 -g -m64 "; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
fi
```



---

Comment by drkirkby created at 2010-06-10 13:36:56

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2010-06-10 23:29:23

See #9208 for an update to sage-env which fixes the problem of matplotlib finding the wrong version of freetype - it requires no modification to the matplotlib source at all. This will probably not work on OS X, as OS X does not appear to have the pkg-config command that both Solaris and Linux have. (This is based on observations on sage.math, boxen.math, t2.math, bsd.math and my own Sun Blade 1000 running Solaris 10 03/05)


---

Comment by drkirkby created at 2010-06-10 23:31:42

Replying to [comment:2 drkirkby]:

> *I think if you manage to get matplotlib to indicate it has found freetype2, but is unable to determine the version, I think you will have solved it.* At the moment matplotlib seems to be using pkg-config on Solaris and Linux (but not OS X) to look up the version, and find the directories of the include and library files. 
> 
> Dave 

The best solution looks to be to get pkg-config to work properly, which requires it knows where the Sage files are to be found. That is done by setting the variable PKG_CONFIG_PATH. 

Dave


---

Comment by jason created at 2010-06-11 06:14:25

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-06-11 06:14:25

I've uploaded a new spkg (same URL as in the description), and updated the patch attached to this ticket to reflect the total changes in this spkg.

Depends on #9208 and #9210 (both applied to the sage-scripts repository!) to correctly identify freetype, even after moving the Sage directory.


---

Comment by jason created at 2010-06-11 06:31:30

This spkg probably also solves #5873.


---

Comment by jason created at 2010-06-11 20:01:31

Yet another update, this time cleaning out a lot of the patches and replacing our kludges with matplotlib-supported setup config files.  I also put in the latest SVN, which has some fixes we've requested, and make the setup config files work.

The link in the description points to the new spkg: http://sage.math.washington.edu/home/jason/matplotlib-0.99.3-svn8415.spkg


---

Comment by drkirkby created at 2010-06-11 20:42:16

This version from svn is causing a problem on the following system, which we should report to the developers. 

 * Sun Blade 1000
 * 2 x 900 MHz
 * 2 GB RAM
 * Solaris 10 03/05 
 

```
/usr/include/stdlib.h:144: error: declaration of C function 'void swab(const char*, char*, ssize_t)' conflicts with
/usr/include/unistd.h:480: error: previous declaration 'void swab(const void*, void*, ssize_t)' here
error: command 'gcc' failed with exit status 1
Error building matplotlib package.
```


The Solaris header files are a lot stricter about what they do/do not declare than most systems, depending on the mode of compilation. An inspection of stdlib.h shows the problem. 


```
extern int putenv(char *);
extern void setkey(const char *);
#endif /* defined(__EXTENSIONS__) || !defined(_STRICT_STDC) ... */

/*
 * swab() has historically been in <stdlib.h> as delivered from AT&T
 * and continues to be visible in the default compilation environment.
 * As of Issue 4 of the X/Open Portability Guides, swab() was declared
 * in <unistd.h>. As a result, with respect to X/Open namespace the
 * swab() declaration in this header is only visible for the XPG3
 * environment.
 */
#if (defined(__EXTENSIONS__) || \
        (!defined(_STRICT_STDC__) && !defined(_POSIX_C_SOURCE))) && \
        (!defined(_XOPEN_SOURCE) || (defined(_XPG3) && !defined(_XPG4)))
#ifndef _SSIZE_T
#define _SSIZE_T
#if defined(_LP64) || defined(_I32LPx)
typedef long    ssize_t;        /* size of something in bytes or -1 */
#else
typedef int     ssize_t;        /* (historical version) */
#endif
#endif  /* !_SSIZE_T */

extern void swab(const char *, char *, ssize_t);
#endif /* defined(__EXTENSIONS__) || !defined(_STRICT_STDC) ... */
```


and in unistd.h


```
#if defined(_XPG4)
/* __EXTENSIONS__ makes the SVID Third Edition prototype in stdlib.h visible */
extern void swab(const void *_RESTRICT_KYWD, void *_RESTRICT_KYWD, ssize_t);
#endif /* defined(_XPG4) */
```


As such, I think your previous version, based on the stable release, rather than a SVN snapshot is preferable. 

I'm attaching the two relevant header files to this ticket.


---

Comment by drkirkby created at 2010-06-11 20:42:16

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-06-11 20:43:36

/usr/include/unistd.h from Solaris 10 on SPARC (03/05 release)


---

Attachment

/usr/include/stdlib.h from Solaris 10 on SPARC (03/05 release)


---

Attachment

I've stuck a bug report, with a link to this on the matplotlib mailing list.


---

Comment by drkirkby created at 2010-06-11 21:31:34

I'd be happy to give your previous package, matplotlib-0.99.3.spkg (md5 checksum 2c8660d9d40f6759ece89c074bc0a351) positive review

Dave


---

Comment by jason created at 2010-06-11 21:32:17

Why don't you go ahead and do that, and I'll open up another ticket for the svn version.


---

Comment by jason created at 2010-06-11 21:37:55

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-06-11 21:39:40

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-11 21:39:40

Done. This is fine.


---

Comment by jason created at 2010-06-11 21:40:42

Changing type from defect to enhancement.


---

Comment by jason created at 2010-06-11 21:40:42

I've opened up #9221 for the SVN spkg.  Future updates for matplotlib should probably be based on the spkg up at #9221.


---

Comment by rlm created at 2010-06-25 15:44:52

Resolution: fixed


---

Comment by kcrisman created at 2011-08-19 16:44:23

Replying to [comment:7 jason]:
> This spkg probably also solves #5873.
Or at least some of it?  The [ticket](https://github.com/matplotlib/matplotlib/issues/225) upstream for one piece of it is now at github, but did this fix the searching for matplotlib issue?  

Sorry for the necropost.
