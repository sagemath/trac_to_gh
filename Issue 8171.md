# Issue 8171: New Cbc spkg with Cplex support

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-02-03 13:04:07

Assignee: tbd

CC:  malb schilly

This new spkg for Cbc includes several new lines in spkg-install to activate CPLEX support in the Coin Library.

It is to be found at : ~ncohen/cbc-2.3.p2.spkg

Nathann


---

Comment by ncohen created at 2010-02-03 13:05:56

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-02-26 11:11:06

I just updated the spkg to make it support multithreading through Cbc !

Nathann


---

Comment by drkirkby created at 2010-03-10 23:37:23

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-03-10 23:37:23

Since this is new, you need to state whether it is intended to go into experimental or optional. Also, since this is new, you should remove the .p2 from the spkg name and instead call it cbc-2.3.spkg.

If you update this, before it is committed to Sage, just replace it, or provide a new link. The patch number increments each time a new version is added to Sage - not each time you change your version. 

Dave


---

Comment by malb created at 2010-03-10 23:56:10

Sorry, there is some confusion here.

Replying to [comment:3 drkirkby]:
> Since this is new, you need to state whether it is intended to go into experimental or optional. 

The package is intended for optional, because that's where CBC is right now.

> Also, since this is new, you should remove the .p2 from the spkg name and instead 
> call it cbc-2.3.spkg.

As hinted above the SPKG is indeed not new but an update. The CPLEX support in the ticket #8172 is new but *this* ticket only updates the CBC SPKG to work with the new interface. A true update. There is and never will be a CPLEX SPKG because CPLEX is proprietary.

Hope that clarifies the situation somewhat.


---

Comment by drkirkby created at 2010-03-11 14:04:20

Yes, it does clarify this. I was under the impression this was a new package, rather than an update to a pre-existing one. 

I've stuck it back to needs review. I'm personally unable to review it, as it is outside my level of expertese.


---

Comment by drkirkby created at 2010-03-11 14:04:29

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-03-11 18:39:42

Harald, can you take a look at the SPKG? I tried it and it works but someone needs to check for the basics (hg status, SPKG.txt, etc.) and I'm busy for the next few days.


---

Comment by ncohen created at 2010-03-22 23:20:30

Finally ..... This package has been tested on t2 (Solaris). It compiles and runs ! :-)

As soon as this and #8172 are in Sage, it will be possible to work on the inclusion of SCIP !

Nathann


---

Comment by dimpase created at 2010-04-09 06:40:35

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2010-04-09 06:40:35

Replying to [comment:8 ncohen]:
> Finally ..... This package has been tested on t2 (Solaris). It compiles and runs ! :-)
> 
> As soon as this and #8172 are in Sage, it will be possible to work on the inclusion of SCIP !
> 
> Nathann

Positive review, all works, good, but please take care of the update I posted on
#8172

Thanks,
Dima


---

Comment by jhpalmieri created at 2010-04-20 22:55:26

Merged 2010/04/20.


---

Comment by jhpalmieri created at 2010-04-20 22:55:26

Resolution: fixed
