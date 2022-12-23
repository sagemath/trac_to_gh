# Issue 8099: pari fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set

archive/issues_008099.json:
```json
{
    "body": "Assignee: drkirkby\n\nWithout setting CFLAGS=-m64 globally build is 32 bit.\n\nA patch is on its way.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8099\n\n",
    "created_at": "2010-01-27T23:19:34Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "pari fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8099",
    "user": "jsp"
}
```
Assignee: drkirkby

Without setting CFLAGS=-m64 globally build is 32 bit.

A patch is on its way.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8099





---

archive/issue_comments_071065.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-27T23:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71065",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071066.json:
```json
{
    "body": "Attachment\n\nAn spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/pari-2.3.3.p8.spkg](http://boxen.math.washington.edu/home/jsp/ports/pari-2.3.3.p8.spkg)\n\nJaap",
    "created_at": "2010-01-27T23:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71066",
    "user": "jsp"
}
```

Attachment

An spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/pari-2.3.3.p8.spkg](http://boxen.math.washington.edu/home/jsp/ports/pari-2.3.3.p8.spkg)

Jaap



---

archive/issue_comments_071067.json:
```json
{
    "body": "The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.\n\n A more accurate comment would be.\n\n* #8099 Ensures the compiler flag -m64 is added at any time SAGE64 was\n set to \"yes\" - previously this was only happening on OS X. This should aid\n building 64-bit on any platform, although it has only been tested on Open\n Solaris.\n\nIt's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt.\n\nIt would be good to see some evidence the patch actually works. Such as byshowing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and forothers, adding it does not generate 64-bit binaries. For zlib, adding -m64 stops the build of shared libraries.\n\nDave",
    "created_at": "2010-01-28T08:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71067",
    "user": "drkirkby"
}
```

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

archive/issue_comments_071068.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.\n> \n>  A more accurate comment would be.\n> \n>  * #8099 Ensures the compiler flag -m64 is added at any time SAGE64 was\n>  set to \"yes\" - previously this was only happening on OS X. This should aid\n>  building 64-bit on any platform, although it has only been tested on Open\n>  Solaris.\n> \n> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt.\n> \n\nThis was *exactly* what I did!\n\n> It would be good to see some evidence the patch actually works. Such as byshowing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and forothers, adding it does not generate 64-bit binaries. For zlib, adding -m64 stops the build of shared libraries.\n> \n\nI opened the ticket *because* without -m64 set pari build in 32 bit!\n\nJaap",
    "created_at": "2010-01-28T11:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71068",
    "user": "jsp"
}
```

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

archive/issue_comments_071069.json:
```json
{
    "body": "Replying to [comment:3 jsp]:\n> Replying to [comment:2 drkirkby]:\n> > The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.\n> > \n> >  A more accurate comment would be.\n> > \n> >  * #8099 Ensures the compiler flag -m64 is added at any time SAGE64 was\n> >  set to \"yes\" - previously this was only happening on OS X. This should aid\n> >  building 64-bit on any platform, although it has only been tested on Open\n> >  Solaris.\n> > \n> > It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt.\n> > \n> \n> This was *exactly* what I did!\n\nSorry. The only point I would make is that the trac ticket should go on the same bullet point. I must admit I don't see why it makes a huge difference, but I was told the file is parsed, and so the format is important. I must admit, I've no idea what parses it. \n \n> > It would be good to see some evidence the patch actually works. Such as byshowing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and forothers, adding it does not generate 64-bit binaries. For zlib, adding -m64 stops the build of shared libraries.\n> > \n> \n> I opened the ticket *because* without -m64 set pari build in 32 bit!\n\nBut the point I am making is that there is nothing to show that the library now builds 64-bit. Probably showing the output of the 'ldd' command before and after a patch would be best. I am the first to admit I have not always done this, but I intend to now, as I am aware just adding -m64 is not the magic solution to solve all these 64-bit issues.",
    "created_at": "2010-01-28T12:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71069",
    "user": "drkirkby"
}
```

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

archive/issue_comments_071070.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T13:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71070",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071071.json:
```json
{
    "body": "Positive review. Pari indicates:\n\n\n```\n==========================================================================\nBuilding for architecture: ix86 running solaris (x86-64/GMP kernel) 64-bit version\n==========================================================================\n```\n\nThe dynamic libraries are 64-bit:\n\n```\ndrkirkby@hawk:~/sage-4.3.1$  file local/lib/libpari*\nlocal/lib/libpari.a:\tcurrent ar archive, not a dynamic executable or shared object\nlocal/lib/libpari-gmp.so.2:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libpari-gmp.so.2.3.3:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libpari.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n```\n",
    "created_at": "2010-01-28T13:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71071",
    "user": "drkirkby"
}
```

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

archive/issue_comments_071072.json:
```json
{
    "body": "Ticket #7979 also has an updated package pari-2.3.3.p8.spkg. Perhaps the one at #7979 should be based on the updated spkg on this ticket.",
    "created_at": "2010-02-02T18:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71072",
    "user": "mvngu"
}
```

Ticket #7979 also has an updated package pari-2.3.3.p8.spkg. Perhaps the one at #7979 should be based on the updated spkg on this ticket.



---

archive/issue_comments_071073.json:
```json
{
    "body": "Replying to [comment:6 mvngu]:\n> Ticket #7979 also has an updated package pari-2.3.3.p8.spkg. Perhaps the one at #7979 should be based on the updated spkg on this ticket.\n\nSure :)! Let's get as much Open Solaris tickets merged as possible!\n\nJaap",
    "created_at": "2010-02-02T18:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71073",
    "user": "jsp"
}
```

Replying to [comment:6 mvngu]:
> Ticket #7979 also has an updated package pari-2.3.3.p8.spkg. Perhaps the one at #7979 should be based on the updated spkg on this ticket.

Sure :)! Let's get as much Open Solaris tickets merged as possible!

Jaap



---

archive/issue_comments_071074.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8099#issuecomment-71074",
    "user": "mpatel"
}
```

Resolution: fixed
