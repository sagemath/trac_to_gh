# Issue 7553: document exactly where SAGE_FORTRAN is used

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-11-29 08:47:51

Assignee: mvngu

CC:  mhansen

As discussed at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f59fc5f7aef7448a) thread, we need to document exactly where the environment variable `SAGE_FORTRAN` is used. The file README.txt mentions this environment variable. It should also say something about where exactly this variable is used.


---

Comment by mvngu created at 2009-11-29 09:58:12

The attachment `README.txt` is based on Sage 4.3.alpha0 and contains some notes about the `SAGE_FORTRAN` environment variable. I have listed William Stein as co-author since some of those notes are based on his responses at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f59fc5f7aef7448a) thread. I also cleaned up the `README.txt` file, including:

 1. Fixing typos.
 1. Reformatting the text.

The file `README.txt` is found under `SAGE_ROOT`, which is not under revision control. There is no need to apply the attached patch `readme.patch`; it is there to show the differences between the old and new `README.txt` files. All you need to do is replace the `README.txt` file with the attached `README.txt`.


---

Comment by mvngu created at 2009-11-29 09:58:12

Changing status from new to needs_review.


---

Comment by drkirkby created at 2009-11-29 11:42:53

A couple of comments, one specific to the SAGE_FORTRAN, others more general. I believe the oppotunity should be taken to update the issue of gcc versions. The others can be left. 

 == Specific to SAGE_FORTRAN == 

The text:

_"If you're using Fortran on a platform without g95 binaries included e.g. Itanium, you must .."_ 

is a bit ambiguous. Itanium is a processor, on which many operating systems run. I personally consider Windows and Linux different platforms, despite they can both run on x86 processors. 

   * Microsoft Windows Server 2003 and 2008 runs on Itanium. 
   * HP-UX runs on Itanium
   * IA-64 Linux runs on Itanium
   * Debian Linux runs on Itanium
   * Redhat runs on Itanium. 

Is this a specific linux distribution you mean that does not come with Fortran binaries? If so, I would state which, or put "some linux distributions for Itanium". I doubt there is not one Linux distribution that does not come with the binaries. 

 * Solaris 10 does not ship with any Fortran binaries either, so I would add that as an example along with the Itanium. (Do not forget the number '10' there, as the latest OpenSolaris comes with Fortran binaries, though they are too old to build Sage). 

I think the SAGE_FORTRAN section should be after the information about supported and unsupported platforms. Currently the order is 

 * SUPPORTED
 * FORTRAN
 * NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS
 * NOT SUPPORTED

I would have kept all the platform specific things one after the other. 

 == Important to add ==

Somewhere I would mention you need gcc >=4.0.1. There is a discussion about this on Apple, but you do need >=4.0.1 on *any* platform. 

 == Not specific to SAGE_FORTRAN, but perhaps worth fixing, or leave to another time. == 

Under 'NOT SUPPORTED'

I would HP-UX and say there is some effort made on both FreeBSD and HP-UX

i.e. 

something like

NOT SUPPORTED 
 * Arch Linux
 * FreeBSD - port in progress. Further developers would speed the progress.  
 * Gentoo Linux
 * HP-UX  - a little work done. Further developers appreciated. 
 * Microsoft Windows (via Cygwin)
 * Microsoft Windows (via Visual Studio C++)
 * OpenSolaris (aka Solaris 11). A port will be completed in 2010. 
(I put them in alphabetical order)

Is it necessary to use clips on Solaris 10 x86?  I would have thought ECL would have built on that.  

Dave


---

Comment by mvngu created at 2009-11-30 23:25:01

See #7565 for a related ticket.


---

Comment by mvngu created at 2009-12-01 09:39:19

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-12-01 11:24:41

based on #7565


---

Attachment

differences between old and new README.txt; do not apply


---

Comment by mvngu created at 2009-12-01 11:32:32

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-12-01 11:32:32

A new `README.txt` is attached. It is based on #7565. The file `readme.patch` shows the differences between the `README.txt` at #7565 and the attached `README.txt`. Do not apply that patch. The new `README.txt` includes the following changes:

 1. Clean up the formatting of the file.
 1. Fix various typos.
 1. Document exactly where the `SAGE_FORTRAN` variable is used.
 1. Incorporate David Kirkby's suggestions.


---

Comment by mhansen created at 2009-12-02 19:11:56

Looks good to me.


---

Comment by mhansen created at 2009-12-02 19:11:56

Resolution: fixed
