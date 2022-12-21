# Issue 3297: Make ccdlib produce a shared library

Issue created by migration from Trac.

Original creator: fbissey

Original creation time: 2008-05-25 09:19:49

Assignee: mabshoff

Tim Abbott made a patch to get cddlib to use libtools and easily
produce a shared library. Packaging the change for sage means not 
only patching several Makefile.am file but also adding a file 
ltmain.sh and regenerating configure.in, configure, aclocal.m4
and several Makefile.in.
I attach a tarball containing an updated patch folder and also 
a patch to spkg-install to use it. The new spkg-install only build
shared libraries. 


---

Comment by fbissey created at 2008-05-25 09:21:01

new patch folder


---

Attachment

patch to spkg-install


---

Comment by mabshoff created at 2008-05-25 13:26:10

We should update to the latest cddlib release while we are at it. I see no point in sticking all those files in patches into the mercurial repo since that means checking in 1.3MB of files that will be removed in the next upstream release anyway.

Please do not attach tar.gz archives to trac ticket since a bug prevents the download the easy way, i.e. just follow the link and you will see.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-25 13:45:22

I just checked and there are other conflicting changes to cddlib-0.94f. So I would greatly prefer for this to go upstream before we merge it back into Sage. The author of cddlib seems to be quite responsive, so let's try that route first.

Cheers,

Michael


---

Comment by fbissey created at 2008-05-25 20:49:21

OK I have a small patch against 0.94f somewhere, not a big change
compared to 0.94b but of course everything has to be regenerated
which is upstream job anyway. I'll see what I can do.

Cheers,
Francois


---

Comment by fbissey created at 2008-05-25 22:25:51

Sent an email upstream with a libtool patch against 0.94f.

Francois


---

Comment by craigcitro created at 2008-06-15 22:00:39

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-08-26 17:24:15

Tim,

the latest upstream release is cddlib-094f - did those patches get merged?

Cheers,

Michael


---

Comment by fbissey created at 2008-08-26 23:37:00

Hi Micheal,

the latest upstream release was already 094f when I filled the bug.
I sent a patch against 094f upstream but never got an answer.

Francois


---

Comment by was created at 2008-11-28 22:23:57

What's up with this?  It has been in limbo for 3 months!  Somebody do something.


---

Comment by mabshoff created at 2008-11-28 22:26:47

Replying to [comment:10 was]:
> What's up with this?  It has been in limbo for 3 months!  Somebody do something. 

Upstream is unresponsive. I don't see the point to copy over a massive amount of changes making the spkg at least twice as large. This is also purely a Debian thing, but we could just ship in place modified sources with instructions on how to get from upstream to this. Once upstream updates (if ever) we could sync.

Cheers,

Michael


---

Comment by was created at 2008-12-06 21:47:16

> Upstream is unresponsive. I don't see the point to copy over a massive amount of 
> changes making the spkg at least twice as large. This is also purely a Debian 
> thing, but we could just ship in place modified sources with instructions on how 
> to get from upstream to this. Once upstream updates (if ever) we could sync. 

I don't get the sense of any precise plan here, and I'm tempted to close this as invalid?  Thoughts?


---

Comment by sbarthelemy created at 2009-01-27 14:45:44

Here  a [new cddlib spkg](http://perso.crans.org/barthelemy/cddlib-094f.spkg), based on the current 094b.p3

I...
 * packaged upstream version 0.94f
 * removed some temporary files
 * adapted the allfaces.c patch
 * updated the SPKG changelog
 * did not update de dist/debian directory
 * did not integrate #3297 nor #3304
 * did not commit anything into the .hg repository


---

Comment by sbarthelemy created at 2009-01-27 16:09:29

Replying to [comment:13 sbarthelemy]:
> Here  a [new cddlib spkg](http://perso.crans.org/barthelemy/cddlib-094f.spkg), based on the current 094b.p3

I just discovered #1619 which is the proper place for my comment. I copied it there. Sorry for the noise.


---

Comment by mhampton created at 2009-10-29 19:08:47

Changing status from needs_review to needs_work.


---

Comment by mhampton created at 2009-10-29 19:08:47

I think #1619 removes some of the issues here, and so these patches would need to be rebased at least.  Someone might want to revive working on converting this to a shared library, so I don't think it should be closed, but I am changing it to needs work.


---

Comment by fbissey created at 2009-10-29 20:56:18

Replying to [comment:15 mhampton]:
> I think #1619 removes some of the issues here, and so these patches would need to be rebased at least.  Someone might want to revive working on converting this to a shared library, so I don't think it should be closed, but I am changing it to needs work.

OK I had done some of the work against 0.94f already but I guess skpg-install at least
will need to be rebased. I will look at it later today.


---

Comment by fbissey created at 2009-11-08 01:28:00

Took me longer than expected to get around this.
It is a big patch when you include all the necessary regenerated files.
Is it OK to attach it compressed (241K compressed, 1.1M uncompressed).
Also do we disable the static library or do we build both?


---

Comment by jdemeyer created at 2011-02-21 10:49:07

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-02-21 10:49:07

François Bissey wrote on sage-devel:

Just looked at SPKG.txt. #3297 has been supplanted in many ways so it should
be closed.


---

Comment by jdemeyer created at 2011-02-24 10:02:30

Resolution: invalid
