# Issue 9388: Fix rubiks makefile

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2010-06-30 00:53:16

Assignee: GeorgSWeber

CC:  rlm

The current makefile for the rubiks spkg.

The makefile erroneously assumes that "mktemp" can be run with no arguments.  This is not the case on, at least, recent versions of Mac OS X.

The probable fix is to run "mktemp" with a template filename.  See the man page for details.



---

Attachment

Patch for rubiks' "spkg-install" script


---

Comment by justin created at 2010-06-30 03:59:14

Updated spkg (new "spkg-install")


---

Attachment

The patch file is just the fix for the file "spkg-install".  The "spkg" is a new spkg file with the changed "spkg-install" script.


---

Comment by justin created at 2010-06-30 04:05:06

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-06-30 10:50:06

Hi Jason, 
there's a few problems with this. 
 * There's no SPKG.txt entry to show what was changed. 
 * Patches should not be attached to the trac server, but instead given to a location where they can be found. 
 * Having looked into this more, 'mktemp' is not defined by POSIX so is not portable. We might find this screws up the FreeBSD port. 

I'll create another which avoid using it completely. 

Give me 15 minutes. 

Dave


---

Comment by drkirkby created at 2010-06-30 10:50:06

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-06-30 10:59:39

Sorry, Justin, not Jason. 

A portable fix is coming up very soon. 

Dave


---

Comment by drkirkby created at 2010-06-30 11:13:14

Here's a link to the next package, which has an updated SPKG.txt file and avoids the use of mktemp at all. 

http://boxen.math.washington.edu/home/kirkby/patches/rubiks-20070912.p12.spkg


---

Comment by drkirkby created at 2010-06-30 11:13:14

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-06-30 11:14:25

Mercurial patch which fully solves the rubiks makefile problem using only POSIX commands.


---

Attachment

David --- While credit for individual patches by definition goes to those who make them, the author block is for credit in the release notes, which should go to anyone who helped move the fix towards its final form. I think that Justin still deserves credit here for helping to hunt down the problem in the first place.

It might be that we're coming from different contexts, but it strikes me as rude to remove someone from the author block.


---

Comment by rlm created at 2010-07-01 17:50:23

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-01 18:14:55

Resolution: fixed


---

Comment by drkirkby created at 2010-07-01 18:30:58

Replying to [comment:6 rlm]:

> It might be that we're coming from different contexts, but it strikes me as rude to remove someone from the author block.

That certainly was not my intension. I was coming it from the point that an author could not review it, and it would make it possible for Justin to review it. 
If you look at a comment on sage-devel today, I specifically asked Francois to remove me from an author or #9097 since he had another idea on this, then I would be able to review it. 

Sorry if I caused any offense to Justin or yourself - that was certainly not my intension. 

Dave


---

Comment by rlm created at 2010-07-01 20:27:44

Replying to [comment:8 drkirkby]:
> That certainly was not my intension. I was coming it from the point that an author could not review it, and it would make it possible for Justin to review it. 
> If you look at a comment on sage-devel today, I specifically asked Francois to remove me from an author or #9097 since he had another idea on this, then I would be able to review it. 

I frequently see the same two people listed as author and reviewer. Often there are multiple patches, with (author, reviewer) switching between persons (a,b) and (b,a), for one example. I am sure you did not intend anything rude, I just wanted to bring it up to avoid misunderstanding. The author and reviewer fields on the trac server should be the union of anyone who feels that they have contributed to that part of the process. The only rule to follow strictly is that the author of a patch cannot review that patch, but as you have seen, trac tickets frequently become pretty complicated. One applies that rule patch by patch, not ticket by ticket.

> 
> Sorry if I caused any offense to Justin or yourself - that was certainly not my intension. 
> 

There is no offense here.

Cheers!
-- RLM
