# Issue 7021: [with patch; needs review] Update prereq from 0.3 to 0.4

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 01:28:38

Assignee: tbd

CC:  was mvngu

This is an updated version of the code which does the preliminary checks of the Sage build. 

The update consists of two files, which should be installed as:
 * $SAGE_HOME/spkg/base/prereq-0.4-install
 * $SAGE_HOME/spkg/base/prereq-0.4.tar

Note there is no need to extract the tar file, and so have a directory $SAGE_HOME/spkg/base/prereq-0.4, though this was done on prereq-0.3. The tar files contents gets extracted to $SAGE_HOME/spkg/build/prereq-0.4 during the build process. 

The tar file contains a configure script, configure.ac, and several macros. 

*Changes to the configure script*
 * Adds AC_COPYRIGHT([GPL version 2])
 * Uses several autoconf macros, mainly taken from [the autoconf macro archive](http://www.nongnu.org/autoconf-archive/). This are better written than the pseudo-autoconf macros of the earlier configure.ac file. The macros get extracted to the directory  $SAGE_HOME/spkg/build/prereq-0.4/m4
 * The configure script allows one to try to build Sage with a non GNU compiler. A warning is issued, but the configure script does not exit as before. 
 * If gcc is used as the C compiler, the configure script checks it is at least gcc 4.0.1
 * If gcc is used as the C compiler, the configure script checks that g++ is used as the C++ compiler. You are not permitted to mix GNU and non-GNU compilers. 
 * If gcc and g++ are used, the configure script checks they are of the same version. It is not easily possible to do this with the Fortran compiler. 
 * If SAGE_FORTRAN is set, the configure script checks the binary actually exists. 
 * If SAGE_FORTRAN_LIB is set, the configure script checks the library actually exists. 
 * The configure script checks perl is at least version 5.6.0. I could not work out what the original code was supposed to do, but 5.6.0 is quite old, so everyone should have at least that. 
 * Tests for the Sun linker. I'm not sure the test is very good, and while it attempts to export SAGE_LINKER, I'm not sure whether this will actually work. (It probably needs a bit more work, but I'll leave it for now).

*Changes to prereq-0.4-install*
 * Issue a warning on OS X to use Apple's latest XCode, and provide a link to [http://developer.apple.com/TOOLS/Xcode/](http://developer.apple.com/TOOLS/Xcode/)(http://developer.apple.com/TOOLS/Xcode/)
 * Specific messages are issued if one tries to build Sage on any of these operating systems, to encourage developers. A 'catch-all' is used for other operating systems. SAGE_PORT needs to be set to a non-empty value to proceed with any of these. 
   * AIX
   * HP-UX
   * Tru64
   * IRIX
   * FreeBSD 
 * Exit codes on errors are changed from -1 to 1, as -1 is an invalid value. 
 * Less checks are performed on a makefile. More is done in the configure script. 
 * Changes comments about Sage being support on Cygwin several months ago (around March 2007), to several years ago.
 * VirtualBox gets a mention if one tries to use cygwin
 * If one of the following commands are not found, the script says to install them or put them in  your path. The previous wording said they had to be installed, but in some cases might not be in the path. (m4 on Solaris is in /usr/ccs/bin, which many people may not know about)

If this is updated, it can close at least two tickets - #6701 and #3384


---

Comment by drkirkby created at 2009-09-27 01:32:25

tar file to be installed as $SAGE_HOME/spkg/base


---

Attachment

executable shell script to install as $SAGE_HOME/spkg/base/prereq-0.4-install


---

Comment by was created at 2009-09-27 05:56:51

* I read "prereq-0.4-install" and was very happy with everything I saw.

 * in configure.ac it says: "# Very loosly based on configure.ac in prereq-0.3, of unknown author.".  The "unknown author" is me (=William Stein). 


Anyway, I've read it all and give this a *big thumbs up* assuming it actually works.  Regarding, actually working, I'd be happy with us just dropping this in an alpha and see.


---

Comment by mvngu created at 2009-09-27 06:22:20

Would this updated spkg invalidate the GCC 3.4.x requirement for ratpoint at #6580?


---

Comment by GeorgSWeber created at 2009-09-27 07:48:25

> Would this updated spkg invalidate the GCC 3.4.x requirement for ratpoint at #6580?

Probably we need a clear decision from our BDFL here, whether Sage continues to officially support being built with GCC 3.4.x, or not.

Cygwin's default compiler is GCC 3.4.4, by the way (but GCC 4.3.x seems to be available at least as an optional package). Currently, GCC 3.4.x works pretty fine. The original reason to force ">= 4.0.1" was to rule out GCC 4.0.0 with which many problems occur, but I guess this could be done without kicking GCC 3.4.x entirely.

Cheers,
Georg


---

Comment by GeorgSWeber created at 2009-09-27 07:50:49

Ups,

I misinterpreted the comment about #6580, reading the comments there, this decision already has been made, sorry for the noise.


---

Comment by mvngu created at 2009-09-28 07:11:45

I did some general clean up to the file `prereq-0.4-install`. The changes include:

 * spell check
 * format code in a consistent manner
 
An updated `prereq-0.4-install` is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/base/prereq-0.4-install

Use that updated `prereq-0.4-install` file together with David's tarball `prereq-0.4.tar`.


---

Comment by drkirkby created at 2009-09-28 16:01:19

Thank you to Minh for tidying this up a bit. I've made a few changes to it, though have kept the version number the same. The revised version can be found at 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.4/

The script prereq-0.4-install must have execute permission. 

*Please use the version at http://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.4/ and not the files attached here.* 

 * Check's for the program 'ar' as that is needed. 
 * Inform a user there is no support for Cygwin, but there is active work to support Cygwin. 
 * More complex testing of the compiler version, and what it does. This should help anyone wishing to fix ratpoints, without risking allowing anyone to mess up their build, unless they are blind!
   * Exits with a message gcc is too old if the gcc version is below 3.4.0
   * Exits with a message the compiler is too buggy, if the gcc version is 4.0.0
   * Warns the user that gcc will not build Sage, but allows the build to continue for gcc 3.4.x. This will allow ratpoints to be debugged, without allowing a casual user to build with a gcc 3.4.x by mistake. 
   * Allows the build to continue if gcc is version 4.0.1 or later. 
 * Credits William with writing the version 0.3 of prereq. 
 * No longer checks for 'xtar' it was a leftover by mistake.
 * No longer checks if the linker is the GNU linker or not. My check was not reliable and I'll wait until I have something better before adding that. 
 * Makes the message about using the latest XCode on Darwin a bit more obvious - before it could easily have been missed. 

If anyone else can think of any sanity checks that need to be made, then these can perhaps be added. But I'd like to get this into Sage asap, as this code really does help find lots of bugs in Sage, as it allows one to try building Sage with the Sun compiler, which uncovers all sorts of bugs.


---

Comment by was created at 2009-10-04 02:45:31

This is such a major improvement -- and fairly safe -- I would really like this in 4.1.2 so I'm upgrading this to blocker.


---

Comment by was created at 2009-10-04 02:45:31

Changing priority from major to blocker.


---

Comment by drkirkby created at 2009-10-04 09:06:14

William, since you believe this is fairly safe and a major improvement, can you update it to 'positive review'? And thank you for the comments!


---

Comment by GeorgSWeber created at 2009-10-04 15:01:45

Reviewer report:

1. There is a .bak-file in the tar-file in http://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.4/ and a subdirectory "autom4te.cache", one might want to remove this file and this (entire) subdirectory.

2. In "prereq-0.4-install", line 135, one might want to remove William's name and email-adress, just leave "email sage-devel" there (this has been another ticket already for all the Sage library code AFAIK).

3. "prereq-0.4-install" is not executable, take care that it is.

4. In configure.ac, line 22, please change AC_COPYRIGHT([GPL version 2]) into AC_COPYRIGHT([GPL version 2, or (at your option) any later version]), and regenerate configure to reflect the update.

5. (maybe a non-issue) In configure.ac, line 44, possibly missing parentheses after: AC_PROG_CPP

I tried to do the test cases on my Mac, there's some gcc-3.3 and g++-3.3 in /usr/bin/ additionally to the usual gcc(-4.0) and g++(-4.0). All in all, this looks good to me. IMHO the only blocker is 4. (the one about the license), the other findings are pretty unimportant.


---

Comment by drkirkby created at 2009-10-04 18:46:58

Thank you. I will address tommorow - I am going out in about 15 minutes. 

There was one other change I was intending making. If one tries to build on Cywin, with SAGE_PORT not set, it will exit, but there is no message that tells you that you can bypass it by setting SAGE_PORT. (It will work if you know this, but it would be sensible to let someone know). 

I have made prereq-install executable on the web site, but when I download it, it looses the exe permissions. I dont think there is anything I can do about that - whoever adds it to sage will have to do that. 


dave.


---

Comment by was created at 2009-10-04 18:59:55

> I have made prereq-install executable on the web site, but when I download it, it
> looses the exe permissions. I dont think there is anything I can do about that - whoever adds it to sage will have to do that.

Yep, that's reasonable.


---

Comment by drkirkby created at 2009-10-05 11:27:06

Thank you for all your comments. In light of these, and some thoughts I had, I've made a few changes. 

 * I removed the configure.ac.bak file, which was an oversight on my part. 
 * I left the directory _autom4te.cache_, as that is something created by _autoreconf_ and is not simply a left-over from me typing _configure_. However, I did remove the file _autom4te.cache/requests_ as it says at the top of the file that it can be safely removed. There is nothing to indicate to me that it is safe to remove the other files in the directory _autom4te.cache_, so I think they are best left. 
 * I removed Williams's name, but suggested sage-support was emailed, not sage-devel, as the failure to find the files checked for (make, ar, perl, m4, ranlib, tar and gcc) are really support issues, not developer issues. I provided a link to the Google group sage-support.
 * I added 'g++' to that list of files too, just in case someone has GCC built for only compiling C, and not C++.
 * I do not believe there should be any parentheses after AC_PROG_CPP see [the autoconf manual](http://www.gnu.org/software/autoconf/manual/html_node/C-Compiler.html) Hence I left that unchanged. 
 * I changed the license as suggested, though I'm not convinced that was really necessary, as the GPL 2 specifically says you can use a later version. 
 * There were two places CYGWIN were checked. Both said it was not supported, and both caused it to exit. I removed the second check, but left the first, which will now exits unless SAGE_PORT is exported. If someone really wants to build on cygwin, we should not stop them. The code now has:


```
if [ "$SAGE_PORT" = "" ]; then
    if [ `uname | sed -e 's/WIN.\+/WIN/'` = "CYGWIN" ]; then
        echo "Unfortunately, building SAGE on Cygwin is not currently supported,"
        echo "though we are actively working on supporting it.  If you would like"
        echo "to help with the porting effort, please post to"
        echo ""
        echo "   http://groups.google.com/group/sage-windows"
        echo ""
        echo "Also, see http://trac.sagemath.org/sage_trac/ticket/6743"
        echo "In the meantime, to run Sage on Windows, please use"
        echo "a virtualization solution instead, such as VMware."
        echo "To get past this message, export the variable 'SAGE_PORT' to"
        echo "something non-empty."
        exit 1
    elif [ `uname` = "SunOS" -a "`uname -p`" != "sparc" ]; then

```


 * I changed one line of code
   

```
 elif [ `uname` != "SunOS" -a `uname` != "Darwin" -a `uname` != "Linux" ]; then
```


to


```
    elif [ `uname` != "SunOS" ] && [ `uname` != "Darwin" ] && [ `uname` != "Linux" ]; then
```

as I understand the former is not portable if there is more than one '-a'. Since this code is run by /bin/sh, and not bash, we can't assume that more that one '-a' will work. 

The changes can be found on the web at:
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.4-3rd-try/
but if you download the files, the execute permissions on prereq-0.4-install will be lost, so they will need to be added back manually. 

If you are happy with those changes, could you please check them in my name. If you take the files from sage.math from the directory


```
/home/kirkby/Solaris-fixes/prereq-0.4-3rd-try/
```


then the permissions should be ok.  

There is an issue which I noticed, which might want addressing later, but I have left, as it probably needs some discussion. 

If one wished to build Sage on a platform without GCC, it would fail due to the checks for gcc and g++, *even if one's aim was to use another compiler*. When I try to build Sage with Sun Studio, it would actually be advantages to *not* have gcc in my path, as then I would spot the bits of code that rely on gcc. Perhaps it might be sensible to not check gcc and g++ if SAGE_PORT was defined to something non-empty. Anyway, for now at least, having gcc and g++ is a requirement, even if you wished to improve sage so it does not rely on gcc, but used better compilers when available.


---

Comment by GeorgSWeber created at 2009-10-05 20:52:07

Good work, positive review!


---

Comment by drkirkby created at 2009-10-07 08:46:26

When implemented, in additon to the two tickets mentioned above, I found another one this can close. I believe all these 3 can be closed. 

 * #6707   	 Sage will try to build on compilers known to be too old.
 * #6701   	 prereq-0.3.tar has many issues and needs updating.
 * #3384   	 Issues a warning for all unsupported / poorly supported operating systems.

Dave


---

Comment by was created at 2009-10-07 15:42:41

I've merged the code from http://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.4-3rd-try/ into sage-4.1.2.rc1.alpha3.


---

Comment by was created at 2009-10-07 15:42:41

Resolution: fixed


---

Comment by was created at 2009-10-07 15:44:10

I have closed #6707, #6701, and #3384.


---

Comment by chapoton created at 2017-07-19 08:51:09

unique name please
