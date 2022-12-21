# Issue 157: Integers(2**31)(5) hangs on 32-bit  (fine on 64-bit, but something else is probably broken there)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-10-27 20:40:07

Assignee: robertwb


```
Hi William,
 
SAGE is great!  Long live SAGE!  Now a bug report 
 
Integers(2**31)(5) hangs on my Linux box.
 
Bug information: Integers(2**30)(5) works, Integers(2**31-1)(5) works, but
there's an ugly range after 2**31.  The offending code is in
integer_mod.pyx, but I can't debug it much further.  Here's a gdb
backtrace, which looks a little sparse:
 
bash-2.05b$ ./sage -gdb
--------------------------------------------------------
--------------------------------------------------------
 
/grad/sone/ncalexan/software/sage-1.4/local/bin/sage-gdb-pythonstartup
GNU gdb Red Hat Linux (6.0post-0.20040223.19rh)
Copyright 2004 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "i386-redhat-linux-gnu"...Using host
libthread_db library "/lib/tls/libthread_db.so.1".
 
[Thread debugging using libthread_db enabled]
[New Thread -1208072704 (LWP 7971)]
Python 2.5 (r25:51908, Oct 16 2006, 11:48:58)
[GCC 3.3.3 20040412 (Red Hat Linux 3.3.3-7)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Detaching after fork from child process 7996.
 
sage: Integers(2**31)(5)
 
Program received signal SIGFPE, Arithmetic exception.
[Switching to Thread -1208072704 (LWP 7971)]
0x0038ff14 in __gmp_exception ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
(gdb) bt
#0  0x0038ff14 in __gmp_exception ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#1  0xb7faf46c in ?? ()
#2  0xb2ca95ac in ?? ()
#3  0x003ba2e0 in ?? ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#4  0x0038ff5f in __gmp_divide_by_zero ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#5  0x00000002 in ?? ()
#6  0xb2ca95ac in ?? ()
#7  0x003ba2e0 in ?? ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#8  0x0039b2bd in __gmpz_fdiv_ui ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#9  0xb7faf46c in ?? ()
#10 0xb2ca95ac in ?? ()
#11 0x00000000 in ?? ()
 
Machine information:
 
It hangs under my Linux box:
 
$ uname -a
Linux tumor 2.6.10-1.9_FC2 #1 Thu Jan 13 17:54:57 EST 2005 i686 i686 i386
GNU/Linux
 
But works fine on the SAGE notebook hosted at modular and works fine on
SAGE 1.3.7 on my Mac OS X G4 Powerbook.
 
Sage information:  Fails under two versions, both built from source:
 
bash-2.05b$ ./sage
--------------------------------------------------------
--------------------------------------------------------
 
and
 
bash-2.05b$ ./sage
--------------------------------------------------------
--------------------------------------------------------
 
Thanks for the great work on SAGE, it is now my CAS of choice.
Nick Alexander
 
PS.  A question: how does `@`func_persist work, meaning where does it get
translated and into what code.  Is this mechanism general and used
elsewhere?
 }}}


---

Attachment

Lower bound on 64-bit integer_mod and (now working) example in doctest


---

Comment by robertwb created at 2006-10-27 20:56:17

Resolution: fixed


---

Comment by robertwb created at 2006-10-27 20:56:17

GMP doesn't have mpz_t --> long long functions, so it can only deal with the first 32 bits of the integer on 32 bit platforms. At most I need the 33rd bit, so this patch lowers the bound to use gmp in these cases.

The lower bound (2^31-1) is only a factor of sqrt(2) lower than the highest possible bound (sqrt(2^63-1)) for this class, so this does not affect efficency a very large of a range.

The crash was a div by zero error--gmp was trying to compute 5 mod 0.
