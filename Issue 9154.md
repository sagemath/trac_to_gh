# Issue 9154: boehm_gc (still, still) fails to build on Cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-06 03:50:06

Assignee: tbd

CC:  leif

This is a followup to #9067.  Amazingly,  the BoehmGC spkg: boehm_gc-7.1.p5.spkg in Sage 4.4.3 does not work.  

I'm trying building now with the boehm_gc-7.1.p4.spkg in /home/mhansen/sage-4.3.5/spkg/standard on winxp2, and it quickly gets passed the problem that boehm_gc-7.1.p5.spkg exhibits, and so far seems to work.


---

Comment by drkirkby created at 2010-08-02 04:33:31

Did it work? 

Since libtool is used, all compiler warnings are dirrected to /dev/null. There's an option on libtool to enable the warnings, though I forget what it is.


---

Comment by mhansen created at 2010-08-17 04:38:08

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-08-17 04:38:08

There is a new spkg at http://boxen.math.washington.edu/home/mhansen/boehm_gc-7.1.p7.spkg which worked for me on winxp2.


---

Comment by dimpase created at 2011-04-22 06:45:41

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2011-04-22 06:45:41

works for me with SAGE_CHECK=yes on Windows 7.
It's a Cygwin-specific change. Positive review.


---

Comment by jdemeyer created at 2011-05-03 12:28:35

Resolution: fixed


---

Comment by jdemeyer created at 2011-05-06 08:52:28

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-05-06 08:52:28

SPKG.txt needs to be updated to mention this ticket.


---

Comment by jdemeyer created at 2011-05-06 08:52:28

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-05-19 08:32:56

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-05-19 08:33:03

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2011-05-19 11:15:12

Replying to [comment:7 jdemeyer]:
> SPKG.txt needs to be updated to mention this ticket.

done.


---

Comment by dimpase created at 2011-05-19 11:15:12

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-05-24 08:47:26

Where is the spkg?

The requested URL `/home/dima/boehm_gc-7.1.p7.spkg` was not found on this server.


---

Comment by jdemeyer created at 2011-05-24 08:47:26

Changing status from positive_review to needs_work.


---

Comment by dimpase created at 2011-05-24 09:09:02

Changing status from needs_work to positive_review.


---

Comment by dimpase created at 2011-05-24 09:09:02

Replying to [comment:11 jdemeyer]:
> Where is the spkg?
> 
> The requested URL `/home/dima/boehm_gc-7.1.p7.spkg` was not found on this server.

Mea culpa. Fixed the URL.


---

Comment by jdemeyer created at 2011-05-31 17:06:59

Resolution: fixed
