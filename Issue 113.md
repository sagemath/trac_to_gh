# Issue 113: singular's omalloc has a screwed up licensed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-10-06 15:31:20

Assignee: was


```
You may be right -- This sucks, and I'm annoyed I missed this.  I'm extremely
annoyed that Singular describes itself on their front page as: "SINGULAR is a free
software under the GNU General Public Licence.", since it's a misleading lie.
 
The discussion mentions two problems:
 
   * MP's license -- not a problem, since I delete MP from the Singular tarball, and
     SAGE doesn't use it.
 
   * OMalloc -- I don't know what it is, but its license is a *major* problem.
 
As the thread you link to says, maybe there is a chance we could get around using omalloc...
 
Ideas?  I don't know anything about the details of how it is used yet.
 
On Fri, 06 Oct 2006 00:02:56 -0700, Martin Albrecht <malb`@`informatik.uni-bremen.de> wrote:
I just stumbled across a discussion on some Debian mailinglist
 
  http://www.mail-archive.com/debian-mentors%40lists.debian.org/msg45988.html
 
which detailed why Singular cannot be included with Debian: The omalloc
library of Singular is considered non-free:
 
singular-3-0-2-2006-09-17/omalloc/COPYING
-----------------------------------------
                       SINGULAR version 3-0-2
                       Package name:   omalloc
 
                      University of Kaiserslautern
 
      Department of Mathematics and  Centre for Computer Algebra
 
                  Author of this package: O. Bachmann
 
                        Copyright (C) 1999-2006
 
 
                               *NOTICE*
 
For this package the GPL does not apply. Permission of use within the
software SINGULAR is granted by the author. In addition to this
permission to modify the sources is granted to the copyright holders
of SINGULAR.
 
If you wish to use this package outside of SINGULAR or to modify it in
any way, please contact the author
"Olaf Bachmann" <obachman`@`mathematik.uni-kl.de>.
-----------------------------------------
 
This sounds like if this is a problem for SAGE, or doesn't it?
 
Martin
```



```
On Fri, 06 Oct 2006 06:50:29 -0700, David Joyner <wdjoyner`@`gmail.com> wrote:
 
 
Could be, but we aren't using omalloc outside of singular (as far
as I know) and they are distributed together.
Do you happen to know Bachmann? It wouldn't hurt to ask him if
he thinks it's an issue. In any case, this was already mentioned
(though vaguely) in SAGE's COPYING.txt file - that omalloc
has it's own copyright and license.
 
This is a major issue.  Certainly what we are doing is *not* illegal.
HOWEVER, it means that when we write:  "All components of SAGE are
licenesed under the GPL or a GPL compatible license (except jsmath
which is under the apache license), so *you* can modify anything
included in sage, make new releases, etc.", we are incorrect.
 
Either:
 
  (1) The author of omalloc changes the license, or
 
  (2) We remove the depenedency of singular on omalloc, or
 
  (3) We undertake the extremely painful task of removing singular
      from the core of SAGE (we'd switch to Macaulay2, which is "really"
      GPL'd).  Singular would remain as an optional package, since we
      make no claims about the licenses of optional packages.
 
A *crucial* aspect of SAGE is that anybody who downloads the core
tarball must be allowed to change any line of code in there, and make
new versions from the result.
 
 
William
```

 


---

Comment by was created at 2006-10-14 20:32:04

This has been resolved:

```
--------------------------------------
From: "Olaf Bachmann" <ADDRESS DELETED>
To: "William Stein" <wstein`@`gmail.com>
Received: by 10.78.157.6 with HTTP; Fri, 13 Oct 2006 01:03:49 -0700 (PDT)
Subject: Re: omalloc
Cc: singular`@`mathematik.uni-kl.de
 
Hi Wiliam,
sure, use and/or modify omalloc, no problem. `@`Singular team: I hereby ask
you to take away those special licensing restrictions of omalloc and to put
it under the same license as Singular.
 
Olaf
```



---

Comment by was created at 2006-10-14 20:32:04

Resolution: fixed
