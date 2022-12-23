# Issue 7767: PARI thinks C compiler is broken on Open Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/7767

Original creator: drkirkby

Original creation time: 2009-12-26 03:39:14

Assignee: drkirkby

CC:  david.kirkby@onetel.net

On a Sun Ultra 27, running Open Solaris 06/2009 and gcc 4.3.4, I get the following error when trying to build PARI:

I've not looked yet, but the chances are it some GNUism passing inappropriate flags to the compiler. It might be a problem with pari, or it might be a problem in something Sage does, so at this point in time, I've not reported this upstream, despite the fact it might be an upstream bug. 


```
pari-2.3.3.p5/src/CHANGES-2.2
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_111b i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4/ --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
Configuring pari-2.3.3 (STABLE) 
Checking echo to see how to suppress newlines...
...using \c
Looking for some tools first ...
...ld is /usr/ccs/bin/ld
...zcat is /usr/bin/zcat
...gzip is /usr/bin/gzip
...ranlib is /usr/ccs/bin/ranlib
...perl is /usr/bin/perl
...I could not find emacs.
******************************************************************
* C compiler does not work. PARI/GP requires an ANSI C compiler! *
* Aborting.                                                      *
******************************************************************
Compiler was: gcc
ERROR - configure PARI with readline and gmp failed.

real	0m0.145s
user	0m0.047s
sys	0m0.053s
sage: An error occurred while installing pari-2.3.3.p5
```





---

Comment by jdemeyer created at 2010-08-01 16:11:53

Is this issue fixed by #9343?  If yes, we can close this ticket.


---

Comment by drkirkby created at 2010-09-28 02:06:55

Replying to [comment:1 jdemeyer]:
> Is this issue fixed by #9343?  If yes, we can close this ticket.
At this point in time, #9343 has not been merged to any stable release (only alphas), so I think currently this ticket should stay open. 

In theory  #9343 could be reverted, though I doubt that will happen.


---

Comment by leif created at 2010-09-28 22:23:42

Did you at least try it with PARI 2.3.*5* (which is e.g. included in Sage 4.5.3)?


---

Comment by jdemeyer created at 2013-10-03 10:20:31

Assuming this is fixed.


---

Comment by jdemeyer created at 2013-10-03 10:20:38

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-10-03 10:20:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-10-05 09:39:03

Resolution: worksforme
