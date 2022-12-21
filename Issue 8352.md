# Issue 8352: twisted-8.2.0.p1 fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-02-24 21:07:49

Assignee: drkirkby

twisted builds in 32 bit mode on Open Solaris x64.

A fix is coming up.

Jaap




---

Comment by jsp created at 2010-02-24 21:17:04

Changing status from new to needs_review.


---

Attachment

The new spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/twisted-8.2.0.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/twisted-8.2.0.p2.spkg)

Jaap


---

Comment by drkirkby created at 2010-02-24 21:19:15

You might want to take a look at #7552 too, as that is an update to the twisted package. There are two tickets both updating twisted. I will put a note on that ticket about this one. 


I don't know the best way to handle this. I could give this positive review now (there is nothing wrong with it), but I'm not sure of the most logical way to do about this.


---

Comment by drkirkby created at 2010-02-25 03:49:29

With no response on how to handle this, I'm giving this positive review. I'll make a note on #7552 that these changes have been reviewed, and that the ticket will have to incorporate your changes.


---

Comment by mpatel created at 2010-02-25 07:59:54

The "p2" spkg at #7552 includes the patch.


---

Comment by jsp created at 2010-02-25 11:59:36

Replying to [comment:4 mpatel]:
> The "p2" spkg at #7552 includes the patch.

Meaning? Does this mean this ticket will be closed?

Jaap


---

Comment by drkirkby created at 2010-02-25 12:16:12

It can't be closed yet (and in any case you should not close it, but leave a message for the release manager to do so) until #7552 is merged. 

But looking at #7552, there does seem little reason that can't be reviewed quite easily. It would appear there were some minor issues with exactly how the changes were checked in via Mercurial, but otherwise it would appear that the ticket should be quite easy to review. I need to do something else just now, but I'll take a look at that later today. 

I think this will be resolved today. 

Dave


---

Comment by drkirkby created at 2010-02-25 13:20:27

*Note to release manager*

I've given #7552, (which is an update of the version of twisted) positive review. That ticket now incorporates these changes, so this ticket does not need incorporating now. I've added Jaap as an author on #7552. 

I've stuck this to 'needs info' as really it no longer needs reviewing. I believe it should be closed, but I'm not allowed to do that, so 'needs info' seemed the least confusing. 

Dave


---

Comment by drkirkby created at 2010-02-25 13:20:27

Changing status from needs_review to needs_info.


---

Comment by mvngu created at 2010-03-02 22:46:56

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 22:46:56

Close as fixed by #7552.
