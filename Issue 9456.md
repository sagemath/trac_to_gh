# Issue 9456: zlib should be a prerequisite for libpng

Issue created by migration from https://trac.sagemath.org/ticket/9456

Original creator: jhpalmieri

Original creation time: 2010-07-08 15:21:45

Assignee: tbd

CC:  drkirkby

From the libpng INSTALL file:

```
Before installing libpng, you must first install zlib
```

So fix the file "deps" accordingly.  (This issue arose when building spkg's in parallel: the build failed when it reached libpng because zlib wasn't installed yet.)


---

Comment by drkirkby created at 2010-07-08 15:37:14

That's perfectly logical. Positive review.


---

Comment by drkirkby created at 2010-07-08 15:37:14

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-08 15:37:27

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-07-22 23:17:25

I'm upgrading this to a blocker because there is a patch and I hit it every time I try to build sage on the skynet machine iras with parallel spkg building: the build fails on libpng, then I have to restart it.  (Usually libpng and zlib are built at the same time on this machine, so after libpng fails, zlib builds successfully, so running "make" again works fine.)


---

Comment by jhpalmieri created at 2010-07-22 23:17:25

Changing priority from major to blocker.


---

Comment by ddrake created at 2010-07-23 00:00:37

I've put the deps file here in SAGE_ROOT/spkg/standard for 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-23 00:00:37

Resolution: fixed


---

Comment by drkirkby created at 2010-07-26 09:50:42

I'm sorry, I have screwed up here, and attached these files to the wrong ticket! Instead of attaching them to #9598, I've attached them here. 

Since this has not been merged, it's probably not a fatal screw up. Sorry. 

I will attempt to put the files back as they should be.


---

Comment by drkirkby created at 2010-07-26 09:51:47

Replying to [comment:5 drkirkby]:

> Since this has not been merged, it's probably not a fatal screw up. Sorry. 

I mean it has been merged, so it should not be a big deal. But I will attempt to put the files back as they should be.


---

Comment by drkirkby created at 2010-07-26 10:04:10

I've tried to correct this, but have failed. I'm going to delete this, and raise it on sage-devel. 

Dave


---

Attachment

spkg/standard/deps file, written by John and merged into sage-4.5.2.alpha1 which I overwrote by mistake. I'm 99% sure this is right.


---

Attachment

diff of spkg/standard/deps written by john which I overwrote by mistake. I'm 99% sure this is right.


---

Comment by drkirkby created at 2010-07-26 10:42:21

I believe these are correct. Perhaps someone else can check. 

Dave
