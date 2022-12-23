# Issue 3898: Make an optional, self contained gcc 4.3.1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3898

Original creator: mabshoff

Original creation time: 2008-08-19 17:17:37

Assignee: mabshoff

As the title says. Make sure to first build static versions of gmp and mpfr to link against those instead of the Sage ones.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-23 01:06:44

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-23 01:06:44

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha0/gcc-4.3.1.spkg

builds find on x86-64 Linux with recent enough glibcs. It should also work on x86 and Itanium.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 09:56:50

I have an updated spkg at

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p0.spkg

that is about half the size. It now installs into $SAGE_LOCAL/toolchain and needs a matching patch to set $PATH and $LD_LIBRARY_PATH correctly to work properly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 11:06:08

The above spkg will fail in case the Sage build directory is on another mount than the tmp dir since the symbolic link across mounts will fail. That is the reason that it failed on SkyNet with the same error across the board.

I am working on gcc-4.3.1.p1.spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 21:52:14

The spkg at

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p0.spkg

now builds on various Skynet machines. I still need to add some magic to make the toolchain automatically integrated into sage-env.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 21:53:04

The spkg is obviously

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p1.spkg

Sorry :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 04:54:23

And now there is 

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p2.spkg

I still need to provide an update with the toolchain env being copied into the right place to make this work automatically.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-30 19:33:16

Gcc 4.3.2 is out, so update to latest upstream.

Cheers,

Michael


---

Comment by was created at 2008-11-27 07:36:30


```
23:32 < wstein-682> there's no gcc-4.3.2 spkg, so why did you write "neeeds review"?
23:32 < wstein-682> can I change 3898 to "needs work"?
23:32 < mabshoff> It need to update.
23:32 < mabshoff> Yes
23:32 < wstein-682> since it's not done as stated inthe summary?
23:33 < mabshoff> I need to do two things:
23:33 < mabshoff> (a) update to gcc 4.3.2 (quick)
23:33 < mabshoff> (b) create custom toolchain.sh scripts for x86, x86-64 and Itanium.
23:33 < mabshoff> Next time I build on SkyNet I will do so.
23:34 < mabshoff> And definitely before SD 12 due to obvious reasons :)
```



---

Comment by mabshoff created at 2009-02-15 07:13:57

Changing priority from blocker to critical.


---

Comment by mabshoff created at 2009-02-15 07:13:57

gcc 4.3.3 is out, so this needs to be fixed anyway.

Cheers,

Michael


---

Comment by drkirkby created at 2009-12-16 22:18:24

Despite not being the latest release, 4.3.4 is arguably the most stable release to date. 

Dave


---

Comment by was created at 2009-12-19 07:48:25

Hi David, are you thinking of making an spkg?  I think it would be well worth making one.  I've changed the title to 4.3.4.


---

Comment by bober created at 2012-03-21 00:02:45

Changing status from needs_work to needs_review.


---

Comment by bober created at 2012-03-21 00:02:45

This is really old and we are now adding a new gcc spkg, so this ticket should be closed.


---

Comment by roed created at 2012-03-21 00:03:45

Changing status from needs_review to positive_review.


---

Comment by roed created at 2012-03-21 00:03:45

I agree: this should be closed.


---

Comment by jdemeyer created at 2012-03-21 11:33:03

Resolution: duplicate
