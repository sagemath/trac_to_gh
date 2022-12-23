# Issue 8099: pari fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set

Issue created by migration from https://trac.sagemath.org/ticket/8099

Original creator: jsp

Original creation time: 2010-01-27 23:19:34

Assignee: drkirkby

Without setting CFLAGS=-m64 globally build is 32 bit.

A patch is on its way.

Jaap




---

Comment by jsp created at 2010-01-27 23:37:24

Changing status from new to needs_review.


---

Attachment

An spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/pari-2.3.3.p8.spkg](http://boxen.math.washington.edu/home/jsp/ports/pari-2.3.3.p8.spkg)

Jaap


---

Comment by drkirkby created at 2010-01-28 08:54:50

The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.

 A more accurate comment would be.

 * #8099 Ensures the compiler flag -m64 is added at any time SAGE64 was
 set to "yes" - previously this was only happening on OS X. This should aid
 building 64-bit on any platform, although it has only been tested on Open
 Solaris.

It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt.

It would be good to see some evidence the patch actually works. Such as byshowing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and forothers, adding it does not generate 64-bit binaries. For zlib, adding -m64 stops the build of shared libraries.

Dave


---

Comment by jsp created at 2010-01-28 11:07:42

Replying to [comment:2 drkirkby]:
> The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.
> 
>  A more accurate comment would be.
> 
>  * #8099 Ensures the compiler flag -m64 is added at any time SAGE64 was
>  set to "yes" - previously this was only happening on OS X. This should aid
>  building 64-bit on any platform, although it has only been tested on Open
>  Solaris.
> 
> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt.
> 

This was *exactly* what I did!

> It would be good to see some evidence the patch actually works. Such as byshowing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and forothers, adding it does not generate 64-bit binaries. For zlib, adding -m64 stops the build of shared libraries.
> 

I opened the ticket *because* without -m64 set pari build in 32 bit!

Jaap


---

Comment by drkirkby created at 2010-01-28 12:10:56

Replying to [comment:3 jsp]:
> Replying to [comment:2 drkirkby]:
> > The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.
> > 
> >  A more accurate comment would be.
> > 
> >  * #8099 Ensures the compiler flag -m64 is added at any time SAGE64 was
> >  set to "yes" - previously this was only happening on OS X. This should aid
> >  building 64-bit on any platform, although it has only been tested on Open
> >  Solaris.
> > 
> > It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt.
> > 
> 
> This was *exactly* what I did!

Sorry. The only point I would make is that the trac ticket should go on the same bullet point. I must admit I don't see why it makes a huge difference, but I was told the file is parsed, and so the format is important. I must admit, I've no idea what parses it. 
 
> > It would be good to see some evidence the patch actually works. Such as byshowing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and forothers, adding it does not generate 64-bit binaries. For zlib, adding -m64 stops the build of shared libraries.
> > 
> 
> I opened the ticket *because* without -m64 set pari build in 32 bit!

But the point I am making is that there is nothing to show that the library now builds 64-bit. Probably showing the output of the 'ldd' command before and after a patch would be best. I am the first to admit I have not always done this, but I intend to now, as I am aware just adding -m64 is not the magic solution to solve all these 64-bit issues.


---

Comment by drkirkby created at 2010-01-28 13:57:41

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-28 13:57:41

Positive review. Pari indicates:


```
==========================================================================
Building for architecture: ix86 running solaris (x86-64/GMP kernel) 64-bit version
==========================================================================
```

The dynamic libraries are 64-bit:

```
drkirkby@hawk:~/sage-4.3.1$  file local/lib/libpari*
local/lib/libpari.a:	current ar archive, not a dynamic executable or shared object
local/lib/libpari-gmp.so.2:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libpari-gmp.so.2.3.3:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libpari.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```



---

Comment by mvngu created at 2010-02-02 18:00:26

Ticket #7979 also has an updated package pari-2.3.3.p8.spkg. Perhaps the one at #7979 should be based on the updated spkg on this ticket.


---

Comment by jsp created at 2010-02-02 18:06:04

Replying to [comment:6 mvngu]:
> Ticket #7979 also has an updated package pari-2.3.3.p8.spkg. Perhaps the one at #7979 should be based on the updated spkg on this ticket.

Sure :)! Let's get as much Open Solaris tickets merged as possible!

Jaap


---

Comment by mpatel created at 2010-02-11 15:13:15

Resolution: fixed
