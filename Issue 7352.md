# Issue 7352: Update prereq to version 0.5

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-29 23:17:51

Assignee: tbd

Following my recent updates of the code for checking the prerequisites for Sage are present (#7021), here is a further refinement. Changes are:

*Changes to configure.ac*
 * Insists that the _configure_ script is created using autoconf 2.63 or later.
 * Checks for _latex_ and issues a gentle warning if it's not found, but makes it clear that _latex_ is not essential. 
 * Exits if gcc is not used as the C compiler, but g++ is used as the C++ compiler. (In _prereq-0.4_ an error message was generated if if gcc was used as the C compiler, but not g++ was not used as the C++ compiler. This addresses the other mixture, which I'd overlooked before). 
 * Issues a warning that Solaris is unsupported on version <10. 
   * If sun4c or sun4m hardware is used, it reports it is not possible to update to Solaris 10, and so problems might exist. 
   * If other Sun hardware is used, it advises people to update unless they have reasons for needing an old release of Solaris. 
  * Issues a warning that Darwin is too old on 5.x, 5.x.y, 6.x, 6.x.y, 7.x and 7.x.y. It states the oldest version of OS X on which Sage has been built is 10.4 (Tiger). The information about the relationship between Darwin and OS X is taken from  http://en.wikipedia.org/wiki/Darwin_(operating_system) 
  * Exits if _bash_ can not be found. 
    * Suggests _bash_ might be found in /opt/OpenSource/bin/ if the operating system is HP-UX. 
    * Suggests _bash_ might be found in /opt/pware/bin if the operating system is AIX. 
  

*Changes to prereq-0.5-install*
 * Checks for GNU tar and GNU make on Solaris, making suggestions where they might be found (/usr/sfw/bin) or obtained via source, Blastwave or Sunfreeware. 
 * Only uses the _-p_ option to _uname_ on Solaris. Previously the option was used on all platforms to check for Solaris on SPARC or x86. Since this option is not portable (not part of POSIX), it generated an error on HP-UX. 
 * Removed all the checks for programs like _gcc_, _ld_ since these were not portable, and always indicated the program was present on Solaris, even if it was not. 
 
The code may be found here. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.5-2nd-try/

Note both files need to be downloaded to $SAGE_ROOT/spkg/base, and the permissions on the script need to be 755. When it is downloaded via the web, the execute permissions will be lost.


---

Comment by drkirkby created at 2009-10-29 23:58:19

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-20 06:18:35

Looks good to me.


---

Comment by mhansen created at 2009-11-20 06:18:35

Resolution: fixed
