# Issue 6710: Numerous build issues on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/6710

Original creator: drkirkby

Original creation time: 2009-08-09 10:44:26

Assignee: tbd

CC:  david.kirkby@onetel.net dimpase

Sage can build on both SPARC and x86, but some issues remain. Some of these problems can affect other operating systems too. I added this as a trac ticket, mainly so I can keep a record of what what bugs remain and what get fixed. 

I've split the issues into two sections. Issues 1-7 will prevent Sage building on Solaris in some or all cases. Workarounds, hacks and updated .spkg files will get around these but have negative side effects. 

Issues 8 onwards are less serious and do not prevent Sage building on Solaris in any case at all. 

*CRITICAL BUGS - Stop Sage building in some/all cases*

1) The version of ECL in Sage will not build on Solaris SPARC. 
#6564

The latest ECL 9.8.1 fixes this. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1/

2) An update to Maxima is needed to allow the new ECL to be installed, as the old Maxima in Sage has a bug which the new ECL detects and rejects. 

#6699 

A new maxima SPKG can be found here. 
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0

3) There's an 'Error building 'modified sage library code' when including paripriv.h'

#6579

A hack of manually commenting out lines 258, 259 and 428 of 

$SAGE_HOME/local/include/pari/paripriv.h

will bypass  this. 

5) MPIR determines linker is GNU when it's Sun on some versions of Solaris x86.

#6539

6) MPIR tries to link in gmp on some versions of Solaris x86. 

#6706

7) Sage will not build if the Sun compiler suite is installed. Some code finds the Sun C++ compiler in /opt/SUNWspro/bin/CC and uses that. Temporarily renaming /opt/SUNWspro to something else will fix this, but needs root access. #6595

*LESS SERIOUS - which don't prevent Sage building on Solaris. *

8) There is a bug in Solaris 10 on sun4v machines which means memset() is broken. A patch to MPFR has been included, and will allow it to MPFR to build, but it will impact performance. 

I'm told by Sun this will be addressed in the next release of Solaris 
10, though I should personally have a patch earlier. 

9) ATLAS will not tune properly on a Sun T5240 ('t2') but will on my own sun4u machines. 

#6705

10) ATLAS dumps core on a Sun T5240 sun4v machine ('t2'). This does not appear to be a gcc 4.4.0 specific bug, as it works fine on my home machine. I added a patch to ATLAS 

#6276

to fix this, but the fix will impact performance, as some tuning data will be computed incorrect, as a 'reasonable' rather than 'optimal' value for one of the tuning parameters is returns. 

I added a second patch, which means the fix can be bypassed on machines where it is not an issue.

6558

11) There's a potential issue in polybori - 0.5rc.p8 and/or 0.5rc.p9 which will cause problems if the Sun compilers were used. 

6582

(There are other issues too with Sun compilers, but this is one I know of). 

12) No support for Sun compilers
#6703

Any attempt to use the Sun compiler suite will fail miserably at a very early stage, due to the configure script in prereq-0.3.tar 

It would be sensible to allow the use of the Sun compilers, but issue a warning that it is very likely to fail. Once we know where the problems lie, we can report these upstream. 

After I hacked the configure script to allow the Sun compilers to be used, I noticed the GNU ones were being used by some code, despite CC, CXX and SAGE_FORTRAN all being set to the Sun compilers. This indicates several packages are ignoring settings of CC, CXX and SAGE_FORTRAN. 

I intend creating a new configure.ac which address this and many other issues with the configure script. 

13) No support for 64-bit on Solaris
#6702

14) Several doctests fail. 
#6709

15) lcalc-20080205.p2 tries to suppress warnings from the assembler, but fails to do this on Solaris if gcc uses the Sun assembler, as the option passed to the assembler is invalid on with Sun's assembler. (Of course, its not sensible to bypass warnings). 

#6609

16) ATLAS has no tuning parameters for sun4v machines

#6705

17) Sage will try to build on compilers known to be too old.

#6707

This is related to #6701 and it not Solaris specific, though some things in 6701 are.

18) Top level README.txt is wrong regarding Solaris (in fact, also all operating systems). More serious errors regarding Solaris in README.txt

#6055


---

Comment by drkirkby created at 2009-08-10 19:32:24

Changing assignee from tbd to drkirkby.


---

Comment by kcrisman created at 2009-12-21 02:05:35

Can you try the new Maxima with this?  There isn't an spkg available yet but hopefully will be soon. See [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7)


---

Comment by mpatel created at 2010-09-01 10:18:02

How many of the open tickets mentioned in the description are still problems?


---

Comment by kcrisman created at 2011-08-19 13:51:47

Bump - a number of these have been closed, and perhaps some others are solved.  Since Solaris is now a supported platform at least some of the time, it would be helpful to have an update.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by chapoton created at 2020-07-14 16:30:03

Resolution: invalid
