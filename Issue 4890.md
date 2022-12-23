# Issue 4890: get rid of nauty's stupid interactive license agreement in the optional spkg install

Issue created by migration from https://trac.sagemath.org/ticket/4890

Original creator: was

Original creation time: 2008-12-30 07:28:07

Assignee: mabshoff

I hate stuff like this:


```
*     B. D. McKay, nauty User's Guide (Version 2.4),
*         http://cs.anu.edu.au/~bdm/nauty/.
Do you accept nauty's license agreement, listed above? (y/n)
```


and as an argument against it note that a _lot_ of stuff in optional isn't gpl compatible, is binary only, etc., but we never have any explicit agreements like the above for anything else. 


---

Comment by mabshoff created at 2008-12-30 10:52:00

This was done explicitly because Nauty is non-free. I would much rather move non-free stuff to its own repo than to just install it without pointing out the license. 

Cheers,

Michael


---

Comment by wdj created at 2008-12-30 12:34:49

Is this in gap_packages* only? If so, would be easiest to simply remove grape?


---

Comment by mabshoff created at 2008-12-30 12:38:14

Replying to [comment:2 wdj]:
> Is this in gap_packages* only? If so, would be easiest to simply remove grape?

What is "this"?

We are talking about spkg-install of the nauty.spkg.

Cheers,

Michael


---

Comment by wdj created at 2008-12-30 13:53:45

Oh.

I was looking here
http://wiki.sagemath.org/optional_packages_available_for_SAGE
and not here
http://www.sagemath.org/packages/optional/ 
:-)


---

Comment by was created at 2008-12-30 18:56:32

I've put a new spkg here:

http://sage.math.washington.edu/home/was/patches/nauty-24b7.p1.spkg

It does much more than just fix the problem cited in the title of this ticket.  It also:

 * Reorganize the spkg to the format we've standardized on.
 * Create Mercurial repository.
 * Make the install process way more robust with much better error checking.
 * Support MAKE environment variable.

To test it you'll also need to use

```
export SAGE_CHECK=1
```

to have it run its test suite.


---

Comment by was created at 2008-12-30 23:26:00

some comments:

 1. David Joyner asked about gap, since Nauty is *also* in Gap-packages, so it also gets installed there.  Of course there, there is no stupid interactive message.

 2. I know that the reason for the message is because it is not a "GPL-compatible license".  However, that can be said for several of the things in optional (gap-packages, openssl, kash3, graphviz), but none of the others have a stupid interactive message.

 3. Even Debian doesn't have stupid interactive license agreements.  They have a "non-free" repo that every normal user justs adds (it's very easy to add), and henceforth one automatically has those packages available by default.

 4. Why distinguish between GPL-compatible and non-GPL-compatible for whether or not we have an interactive message?

Even if we put things in a different repository, it won't in any way effect the user experience, since install_package(...) just queries all repositories.  It will make management of repositories more difficult.  

I view half the point of optional as being a place where we can put non-GPL-compatible code like nauty, but for which it is still very easy for users to install it.


---

Comment by mabshoff created at 2008-12-30 23:34:38

I would still not call this interactive error message "stupid" since it was done deliberately. Nauty is not only non-free, but its license prohibits its use for works involving primarily military applications, so this is not about non-GPL vs. GPL. If we also ship it in the optional gap.spkg it looks like we will need to do some auditing there, too.

Cheers,

Michael


---

Comment by was created at 2009-01-01 03:00:13

> I would still not call this interactive error message "stupid" since it was done 
> deliberately. 

I think interactive license agreements are annoying.    They are all done deliberately. 

> Nauty is not only non-free, but its license prohibits its use for 
> works involving primarily military applications, so this is not about 
> non-GPL vs. GPL. 

Nauty is free as in beer, but the free license it is under is not "libre" i.e., not OSI approved and not GPL-compatible.  Nauty's license is: "Permission is hereby given for use and/or distribution with the exception of sale for profit or application with nontrivial military significance." There are essentially no other restrictions.   

Since we have a fundamental disagreement here, this will need to be discussed on sage-devel and possibly voted on.


---

Comment by jason created at 2009-02-03 21:33:32

I posted a message to sage-devel to start a discussion.  We'll see how it goes.

I made the original spkg.  The result of some good discussion at that time was that an interactive license was needed, so that's what I did.  Personally, I don't care either way; I guess Robert's code has weaned me off of nauty for now.


---

Comment by was created at 2009-03-15 22:57:41

Resolution: invalid


---

Comment by was created at 2009-03-15 22:57:41

I'm closing this as invalid based on the discussion.  The fix should be to remove the nauty spkg entirely, or rename it with "-nonfree".
