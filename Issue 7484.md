# Issue 7484: Sage does not build on stock Ubuntu 9.10 without installing gfortran and setting SAGE_FORTRAN(_LIB)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-11-18 02:10:22

Assignee: tbd

CC:  schilly

Here's a patch for README.txt to document this:


```
--- README.txt.orig     2009-11-17 20:02:26.833640422 -0600
+++ README.txt  2009-11-17 20:07:26.763327405 -0600
`@``@` -47,6 +47,14 `@``@`
      >= 10.4.x and certain Linux distributions are 100% supported.
      See below for a complete list.
  
+     NOTE: If you're using Fortran on a platform for which the included g95 binaries
+     do not work (e.g., Itanium or Ubuntu 9.10), you must use a system-wide gfortran.
+     You must set the SAGE_FORTRAN and SAGE_FORTRAN_LIB environment variables before
+     making Sage.  Do this by typing
+
+          export SAGE_FORTRAN=/exact/path/to/gfortran
+          export SAGE_FORTRAN_LIB=/path/to/fortran/libs/libgfortran.so
+
    2. Extract the tarball:
           tar xvf sage-*.tar
 
`@``@` -75,13 +83,6 `@``@`
     Use Sage on Microsoft Windows via VMware.
     We do not always test on OS X 10.4, but Sage should work there fine.
 
-NOTE: If you're using Fortran on a platform without g95 binaries included
-      with Sage, e.g., Itanium, you must use a system-wide gfortran.  You 
-      have to explicitly tell the build process about the fortran
-      compiler and library location.  Do this by typing
-
-          export SAGE_FORTRAN=/exact/path/to/gfortran
-          export SAGE_FORTRAN_LIB=/path/to/fortran/libs/libgfortran.so
 
 NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS:
        PROCESSOR       OPERATING SYSTEM
```



---

Comment by jason created at 2009-11-18 02:13:08

Changing status from new to needs_review.


---

Comment by jason created at 2009-11-18 02:15:11

Regarding this ticket:


```
> Don't bother, since sage-4.3 should require the user has installed
> gfortran on *all* Linux platforms.


Okay, great.  If that doesn't happen, then I already made the ticket and patch:

http://trac.sagemath.org/sage_trac/ticket/7484

This can be closed (or modified) to indicate the need for gfortran on all platforms, whenever that patch is merged.
```



---

Comment by was created at 2009-11-18 07:15:13

See #7485


---

Comment by mvngu created at 2010-01-20 20:34:39

Due to #7485, Linux Fortran binaries are now removed from the Fortran spkg. This means that under Linux, Fortran is a pre-requisite for compiling Sage from source just as the GCC suite of compilers is a pre-requisite. The new [README.txt](http://trac.sagemath.org/sage_trac/attachment/ticket/7484/README.txt) states that Fortran is a pre-requisite for compiling Sage on Linux. This file is based on that in Sage 4.3.1.rc1. The diff file [README.diff](http://trac.sagemath.org/sage_trac/attachment/ticket/7484/README.diff) shows differences between the attached README.txt and the one in Sage 4.3.1.rc1. Don't apply this diff file. Just replace the current README.txt under SAGE_ROOT with the attached README.txt.


---

Comment by drkirkby created at 2010-01-21 12:36:44

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-21 12:36:44

I think it is important to add on platforms such as Solaris, AIX and HP-UX, where both 32 and 64-bit builds are supported, the library path *must* point to the 32-bit library if building 32-bit, and must point to a 64-bit library if building 64-bit. 

(How about OS X? Perhaps the fortran.spkg takes care of that.) 

On Solaris that will probably be the following, though this would need checking.


```
SAGE_FORTRAN=/path/to/gcc/install/directory/bin/gfortran (SPARC and x86)

SAGE_FORTRAN_LIB=/path/to/gcc/install/directory/lib/libgfortran.so (32-bit SPARC)
SAGE_FORTRAN_LIB=/path/to/gcc/install/directory/lib/sparcv9/libgfortran.so (64-bit SPARC)

SAGE_FORTRAN_LIB=/path/to/gcc/install/directory/lib/libgfortran.so (32-bit x86)
SAGE_FORTRAN_LIB=/path/to/gcc/install/directory/lib/amd64/libgfortran.so (64-bit x64)
```


Dave


---

Comment by was created at 2010-01-21 16:53:17

> (How about OS X? Perhaps the fortran.spkg takes care of that.) 

Do *NOT* require gfortran on OS X, since we still supply it with Sage.


---

Comment by drkirkby created at 2010-01-24 01:14:06

William, you said on sage-devel, on the subject of SAGE_FORTRAN and OS X. 

_Use the binary included in Sage if SAGE_FORTRAN is not specified. Otherwise, use the one pointed to by the that environment variable. _

http://groups.google.com/group/sage-devel/browse_thread/thread/e2867ea2efe7e052

Therefore, SAGE_FORTRAN_LIB might be important if someone wanted to use their own version of gcc, rather than the one in Sage. In which case, the question arises as to what would be the path to the library. Would it be different for 32 and 64-bit builds, as it is on Solaris and HP-UX? 

Dave


---

Comment by mvngu created at 2010-01-26 16:33:59

Ticket #8080 updates the [Installation Guide](http://www.sagemath.org/doc/installation) to require gfortran as a pre-requisite for compiling Sage on Linux.


---

Comment by mvngu created at 2010-02-14 18:49:53

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-02-14 18:49:53

Replying to [comment:5 drkirkby]:
> I think it is important to add on platforms such as Solaris, AIX and HP-UX, where both 32 and 64-bit builds are supported, the library path *must* point to the 32-bit library if building 32-bit, and must point to a 64-bit library if building 64-bit. 

Done. Fixed in the updated README.txt.





> (How about OS X? Perhaps the fortran.spkg takes care of that.) 

Also fixed in the updated README.txt. For Mac OS X, I have removed the reference to ticket #7095, as the issue contained therein has been fixed.


---

Comment by mvngu created at 2010-02-14 19:03:42

[README.txt](http://trac.sagemath.org/sage_trac/attachment/ticket/7484/README.txt) also fixes #8106.


---

Attachment

based on Sage 4.3.3.alpha0


---

Comment by mvngu created at 2010-02-15 03:59:05

based on Sage 4.3.3.alpha0


---

Comment by drkirkby created at 2010-02-21 06:01:12

Changing status from needs_review to needs_work.


---

Attachment

A few comments: Those in bold are specifically about Fortran. The others are not, so you can ignore them for this ticket, tough you might chose to update them, as they are minor changes:

 * Line 22: says Sage is distributed under the GPL, but does say what version. I believe it should be GPL 2 (or at your option any later version). 
 * Line 110 should make it clear Sage 4.3.0.1 does work on Solaris 10 SPARC and more recent versions nearly work. 
 * *Line 113 mentions gFortran. I believe the F should be changed to lower case*
 * Line 127 should make it clear this port is for x64. OpenSolaris does exist on SPARC, though I do not believe it has many users. 
 * *Lines 144 + 145. Again refers to a gFortran. Also, there is no reason gfortran needs to be installed system wide. Someone can create their own private copy of gcc with Fortran support.*
 * *Line 168. I think changing 32- to 32-bit would be preferable.*
 *  Line 299. I would change to simply Sage needs GCC >= 4.0.1
 * Line 300 seems a bit pointless, as long as we say Sage needs gcc >=4.0.1
 * Line 301 can be removed, as it is totally impossible to build Sage with that. The 'prereq' script will exit immediately with an error. 

Dave


---

Comment by mvngu created at 2010-03-17 11:34:49

From IRC:

```
04:31 < schilly> mvngu: the README.txt still says that arch linux is not 
                 supported. i guess we can drop that ^^
```



---

Comment by kcrisman created at 2010-05-26 20:53:28

README.txt was recently updated, so this will need to be rebased again.  Is the original problem still a problem, given the latest one?

With respect to drkirkby's comments, I think the following remain:
>  * Line 22: says Sage is distributed under the GPL, but does say what version. I believe it should be GPL 2 (or at your option any later version). 
This seems reasonable to change.
>  * *Lines 144 + 145. Again refers to a gFortran. Also, there is no reason gfortran needs to be installed system wide. Someone can create their own private copy of gcc with Fortran support.*
I have no idea if this is true, but at any rate we still use the phrase "system-wide" in line 137.
>  *  Line 299. I would change to simply Sage needs GCC >= 4.0.1
>  * Line 300 seems a bit pointless, as long as we say Sage needs gcc >=4.0.1
>  * Line 301 can be removed, as it is totally impossible to build Sage with that. The 'prereq' script will exit immediately with an error. 
These three seem to be a matter of taste.  As long as we accurately document what Sage builds with, we might as well leave it alone.  And warnings of things that fail are good if they prevent people from wasting time trying to make them fail :)


---

Comment by mhansen created at 2010-08-19 17:45:34

This has already been taken care of at least as of Sage 4.5.2.  I'm going to mark it as invalid now.


---

Comment by mhansen created at 2010-08-19 17:45:34

Resolution: invalid
