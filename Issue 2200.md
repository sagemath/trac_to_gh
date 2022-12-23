# Issue 2200: copyright documentation for various spkgs

Issue created by migration from https://trac.sagemath.org/ticket/2200

Original creator: tabbott

Original creation time: 2008-02-17 21:53:31

Assignee: tabbott

As part of adding Debian copyright files to all the Debian packages, I tried to verify the copyright status of all the SAGE dependencies I'm packaging for Debian.  The following are the list of packages for which I have questions about:

- givaro: I can only verify this is GPL2; is it supposed to be GPL3 compatible?

- genus2reduction: The genus2reduction package itself doesn't mention copyright; though the SAGE COPYING.txt file claims GPL...

- libm4ri: I can't find an upstream URL for this.  Is there one?

- tachyon: still has 4-clause BSD in the sources (It apparently hasn't been released since the author agreed to relicense to 3-clause over email; since the email is 6 months old, it might be useful to email John Stone again?).

- sympow: the copyright statement in the SAGE COPYING.txt differs from that in the sympow sources (the latter seems to not be a standard BSD license).



---

Comment by malb created at 2008-02-17 22:09:54

> - libm4ri: I can't find an upstream URL for this.  Is there one?

There is none. I basically maintain the code because Gregory Bard is too busy to do it. It definitely is GPLv2 or later, I got that from Gregory via e-mail.


---

Comment by was created at 2008-02-17 22:13:37

- givaro: this is GPL3 compatible because it's only copyright statement is that they include the GPL v2 COPYING file, which is itself GPL V3 compatible.  It says right in it "If the Program does not specify a version number of this License, you may choose any version ever published by the Free Software Foundation."

 - genus2reduction -- I'm the maintainer of that package

 - tachyon -- pinging the author again is a good idea.  could you do that?

 - libm4ri -- see the comment from malb

 - sympow -- you're right, he puts an additional restriction above standard bsd.
The additional restriction is 'If redistribution is done as a part of a compilation that has a more
 restrictive license (such as the GPL), then the fact that SYMPOW has
 a less restrictive license must be made clear to the recipient.
 For example, a line like (include bracketed text if SYMPOW is modified):
  "This compilation includes [a modification of] SYMPOW whose [original]
   code has a less-restrictive license than the entire compilation."
 should appear in a suitable place in the COPYING and/or LICENSE file.'; I don't
view that as GPL-incompatible -- it doesn't restrict usage at all.  It just says that the copyright on sympow can't be hidden. 

So, the sympow section in Sage's COPYING.txt should be changed. 

wiliam


---

Comment by was created at 2008-02-17 22:15:29

Regarding genus2reduction, i should probably get a clear copyright license statement from Qing Liu, who said to me only

```
From Qing.Liu@math.u-bordeaux1.fr Sat Jul 16 23:33:18 2005
Return-path: <Qing.Liu@math.u-bordeaux1.fr>

Hi William,

It will be a pleasure for me that you include genus2reduction in SAGE.
Note however that the program is not maintained anymore.  Please
feel free to make any technical modifications to make it compile
in recent systems.

Best regards,

Liu

```



---

Comment by mabshoff created at 2008-02-17 22:20:36

Replying to [comment:2 was]:
> So, the sympow section in Sage's COPYING.txt should be changed. 

That is #1172 and an easy credit.
 
> wiliam

Cheers,

Michael


---

Comment by tabbott created at 2008-02-17 22:39:23

libm4ri: I'll list sagemath.org as the URL then.  I've attached a patch to #2199.

givaro: Hmm, I hadn't realized that property of the GPL.  I've attached a patch to #2199.

genus2reduction: Okay, once you get something more clear from Qing Liu, it would probably be helpful for eventually getting into Debian if we were to include a COPYING file in the src/ directory. 

sympow: Okay, I've attached a patch to #2199 with the Sympow Debian copyright file.

tachyon: I've pinged the author.


---

Comment by was created at 2008-02-17 23:08:59

I've pinged the genus2reduction author.

William


---

Comment by was created at 2008-02-18 00:06:29

I've received written permission from Liu to GPL genus2reduction, and have done so.  The new package is here:

http://sage.math.washington.edu/home/was/patches/genus2reduction-0.3.p2.spkg

Please switch to this.


---

Comment by tabbott created at 2008-02-18 00:27:52

Okay, I've attached a Debian copyright file for genus2reduction to #2199.


---

Comment by mabshoff created at 2008-04-01 20:38:43

The genus2reduction.spkg has been merged a while ago. The issue about tachyon's BSD status should be on a new ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 20:38:43

Resolution: fixed
