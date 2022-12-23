# Issue 2199: [with patch; needs review] Copyright files for Debian packages

Issue created by migration from https://trac.sagemath.org/ticket/2199

Original creator: tabbott

Original creation time: 2008-02-17 21:32:17

Assignee: tabbott

I'm attaching Mercurial patches for the copyright files for many Debian packages.  The ones I'm not attaching have various verification or missing data issues; I'll be adding separate tickets for those.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-04-01 20:09:12

Merged iml-copyright.2.patch in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 20:41:42

Re genus2reduction-copyright2.patch:

```
[22:07] <mabshoff> wstein: genus2reduction is GPL V3? Is that really the case?
[22:07] <wstein> No.
[22:07] <wstein> genus2reduction is gpl v2+
[22:07] <mabshoff> ok, then that patch by Tim is *wrong*
[22:07] <wstein> I got it licened way way before gpl v3 ever existed.
```


Cheers,

Michael


---

Comment by tabbott created at 2008-04-01 20:50:54

Unless I'm mistaken, the patch says gplv2+, not gplv3.  I'm looking at

http://trac.sagemath.org/sage_trac/attachment/ticket/2199/genus2reduction-copyright.patch

At least one of us is confused.


---

Comment by mabshoff created at 2008-04-01 20:54:08

Replying to [comment:4 tabbott]:
> Unless I'm mistaken, the patch says gplv2+, not gplv3.  I'm looking at
> 
> http://trac.sagemath.org/sage_trac/attachment/ticket/2199/genus2reduction-copyright.patch
> 
> At least one of us is confused.

And that would be me. Sorry, got too many patches in play and tabs open in firefox :)

Cheers.

Michael


---

Comment by mabshoff created at 2008-04-01 20:54:17

Merged linbox-copyright.patch in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 21:20:38

Merged eclib-copyright.patch in eclib-20080310.p1


---

Comment by mabshoff created at 2008-04-02 00:24:20

Merged flint-copyright.patch in Sage 3.0.alpha0


---

Attachment


---

Comment by tabbott created at 2008-04-07 06:13:51

John Stone sent me the following email, so I've generated a copyright file for tachyon.

Date: Fri, 4 Apr 2008 14:32:34 -0500
From: John Stone <johns`@`ks.uiuc.edu>
To: Timothy G Abbott <tabbott`@`MIT.EDU>
X-Spam-Score: 0.12
Subject: Re: tachyon license
Parts/Attachments:
   1 Shown    60 lines  Text
   2   OK     28 lines  Text
----------------------------------------


Tim,
  Please find attached an updated Tachyon license which you are free
to use with any of the existing releases I've made.  I provided this to
Intel so they could include Tachyon with their open source TBB release
as well.  (they are using an older rev of Tachyon so a new release
didn't help their situation)

I'll try and get a new release package posted soon.

Cheers,
  John Stone
  johns`@`ks.uiuc.edu
  john.stone`@`gmail.com

/*
 * Copyright (c) 1994-2008 John E. Stone
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. The name of the author may not be used to endorse or promote products
 *    derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */


---

Comment by mabshoff created at 2008-04-11 22:39:46

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-11 22:39:46

I will also slip all of the above into all the spkgs for 3.0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-11 22:39:46

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-04-11 22:39:46

Changing assignee from tabbott to mabshoff.


---

Comment by mabshoff created at 2008-04-12 17:55:49

I merged all outstanding patched into the spkgs in Sage 3.0.alpha4. I did not increment the patch level to avoid rebuilds on upgrade.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-12 17:55:49

Resolution: fixed
