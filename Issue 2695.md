# Issue 2695: ensure that we have sufficient amounts of RAM to build Sage

Issue created by migration from https://trac.sagemath.org/ticket/2695

Original creator: mabshoff

Original creation time: 2008-03-28 06:09:41

Assignee: mabshoff


```
[06:27] <mabshoff> wstein: toothpaste's problem is RAM, not [only] disk space.
[06:27] <wstein> RAM. Wow.
[06:27] <mabshoff> gcc isn't very efficient.
[06:27] <wstein> his problem might be lack of a toothbrush.
[06:27] <mabshoff> And it fails in eclib, so linbox_wrap will be worst.
[06:28] <wstein> Wow, I see.
[06:28] <wstein> Dang C++ templates.
[06:28] <mabshoff> RTFL :)
[06:28] <wstein> what does rtfl stand for?
[06:28] <wstein> read the frickin' L?
[06:28] <mabshoff> read the fine log ;) [edited :)]
[06:28] <wstein> ahh.
[06:28] <wstein> good point.
[06:28] <mabshoff> That was a new failure.
[06:29] <wstein> Maybe we should check for at least 1GB ram right at the beginning
[06:29] <mabshoff> I guess the hosted VMs in his case have a rather small, hardcoded limit.
[06:29] <wstein> of the build, and if the user has less, give an error?
[06:29] <mabshoff> probably, but 700 MB seems enough.
[06:29] <wstein> OK, we could check for that.
[06:29] <wstein> And test that it works using ulimit.
[06:29] <wstein> That's the sort of thing autohell never does...
[06:32] <mabshoff> I am not sure if ulimit tests if you have that much memory available.
[06:33] <mabshoff> It just limits the max allocatable amount.
[06:33] <wstein> We could just write a small C program that malloc's 700MB.
[06:33] <wstein> if it fails, then sage doesn't build further.
[06:33] <mabshoff> Yeah. 
[06:34] <wstein> If this actually sounds like a good idea to you, paste this log in a trac ticket.
[06:34] <mabshoff> :)
[06:34] <wstein> If it doesn't, just ignore it.  I leave it up to your taste to decide.
[06:34] <mabshoff> printf("You cheapskate, buy your computer more RAM!");
[06:34] <mabshoff> :)
[06:35] <wstein> :-)
```



---

Comment by mabshoff created at 2008-03-28 06:09:50

Changing status from new to assigned.


---

Comment by dfdeshom created at 2008-03-28 14:20:42

FYI, I have 700MB of Ram and I'm able to build Sage fine (as of 2.10.2, I think). So... aim lower :)


---

Comment by jbmohler created at 2008-03-31 14:31:10

I have 512 mb in my laptop and 2.10.x built/upgraded perfectly fine and I'm currently 'sage -upgrade'ing to 2.11 and I got past linbox_wrap.  Only 100kb of swap is currently showing as used.


---

Comment by mabshoff created at 2008-03-31 14:50:12

Replying to [comment:3 jbmohler]:
> I have 512 mb in my laptop and 2.10.x built/upgraded perfectly fine and I'm currently 'sage -upgrade'ing to 2.11 and I got past linbox_wrap.  Only 100kb of swap is currently showing as used.

Hi Joel,

the amount of RAM required for linbox_wrap does depend on the gcc released. I have seen 700 MB, but even 350MB is an unreasonable amount of memory to compile that bit of code. To resolve this ticket we should check the amount of memory available and emit a warning if we consider the amount too low. It might be 0.5GB for now.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 18:19:35

Changing type from defect to enhancement.


---

Comment by leif created at 2013-04-25 13:03:21

FWIW, with enough (and fast :) ) swap space, Sage 5.x (still) builds on 32-bit machines with 512 MB RAM (and Gnome or some other GUI running).




Another issue is that meanwhile a few [long] doctests are really poor, in eating up nearly 2x 2 GB (Sage + `gp`).  Others just allocate that much, without actually using it (such that they'll fail with `ulimit -v` for no real reason).

768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.


---

Comment by jdemeyer created at 2013-04-25 13:13:12

Replying to [comment:6 leif]:
> 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.
for large values of "a while" I guess...


---

Comment by leif created at 2013-04-25 13:28:21

Replying to [comment:7 jdemeyer]:
> Replying to [comment:6 leif]:
> > 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.
> for large values of "a while" I guess...

Nope;  I actually wanted to add "not that long ago"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).


---

Comment by leif created at 2013-04-25 13:30:52

P.S.:  W.r.t. the doctests, the "winners" in memory consumption used to be those in `schemes/elliptic_curves/`, with definitely less than 400 MB (300-350 I think).


---

Comment by jdemeyer created at 2013-05-19 13:03:55

Replying to [comment:8 leif]:
> Nope;  I actually wanted to add "not that long ago"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).
I don't believe you, the Heegner tests exist longer than that and always required around 2GB of memory.


---

Comment by leif created at 2013-05-19 16:16:40

Replying to [comment:10 jdemeyer]:
> Replying to [comment:8 leif]:
> > Nope;  I actually wanted to add "not that long ago"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).
> I don't believe you, the Heegner tests exist longer than that and always required around 2GB of memory.

I'm especially sure about the tests in `schemes/elliptic_curves/`, since these used to be the record holders, as mentioned. :-)

This is just one example of a couple of doctests where PARI tries to *allocate* a huge amount of memory, but actually *uses* only a fraction of it.  (You might have to set up enough swap space to run these tests, but you'll usually not experience swapping even with just 512 MB RAM, say.)


---

Comment by leif created at 2013-05-19 16:23:52

... like I already mentioned [comment:6 above]:
> [...] Others just allocate that much, without actually using it (such that they'll fail with `ulimit -v` for no real reason).
> 
> 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago. [...]


---

Comment by jdemeyer created at 2013-06-13 12:40:54

Similar to #1517, I don't think it's up to Sage to decide how much RAM is enough.


---

Comment by jdemeyer created at 2013-06-13 12:40:54

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-13 12:42:09

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:20:42

Resolution: wontfix
