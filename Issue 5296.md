# Issue 5296: Update the OS X Readme

Issue created by migration from https://trac.sagemath.org/ticket/5296

Original creator: GeorgSWeber

Original creation time: 2009-02-17 20:19:04

Assignee: mabshoff

CC:  mabshoff

With the switch to an app bundle distribution for Mac OS X, the file "$SAGE_ROOT/sage-README-osx.txt" contains obsolete parts (the "steps 4 - 6", and the last lines right at the end).

A -bdist'ed OS X .dmg contains another README.txt file of the same outdated content, probably it is just the first one copied during creation of the .dmg. 


---

Comment by mabshoff created at 2009-03-01 02:25:34

Better luck in 3.4.1.

Cheers,

Michael


---

Attachment


---

Comment by kcrisman created at 2009-09-23 20:21:54

Changing priority from critical to minor.


---

Comment by kcrisman created at 2009-09-23 20:21:54

I don't know how to check whether this "works", but at any rate once Sage is automatically distributed in the app bundle, this should go in. 

I'm also changing priority, since no one has complained in half a year.


---

Comment by GeorgSWeber created at 2009-09-24 22:40:00

I'm fine with changing the priority. As far as I remember, Michael Abshoff asked me to create this ticket. Unfortunately, nobody seems to want to work on "app-ifying" Sage on OS X since his leave.


---

Comment by iandrus created at 2009-11-27 21:10:40

Changing assignee from mabshoff to iandrus.


---

Comment by iandrus created at 2009-11-27 21:10:40

Now that I hopefully have a little more time I plan to work on "app-ifying" Sage.  What is preventing us from distributing sage in the app bundle automatically?  Is there a reason we don't just make SAGE_APP_BUNDLE=yes the default?


---

Comment by kcrisman created at 2009-11-28 04:25:32

Apparently there were some movement issues, that is to say moving the Sage installation within the computer didn't always work properly.  There is an open ticket about this, #5254.  #5261 is also related.  I like #7546, too - can't review it in detail now, but it would be great to finally get this taken care of, and I would be happy to help out with reviewing duties once I'm in a position to do so.


---

Comment by kcrisman created at 2009-12-08 15:33:25

Now that #5254, #5261, and #7546 are more or less resolved, we should resolve this situation.  Note that sage-bdist doesn't currently automatically make an app bundle yet, and this should probably be resolved on sage-devel, for the following reason: some people, perhaps many, will want to have both the notebook and command line options, but the current script makes the notebook only.  We should definitely eventually distribute a notebook-only one, but I'm not sure that should be the default until we have both available.  Ideally, this would be yet another environment variable for sage-bdist :)

But we're very, very close!  So much thanks to iandrus for making huge leaps over my initial small steps on all this.


---

Attachment


---

Comment by iandrus created at 2010-03-30 21:24:09

Changing status from needs_work to needs_review.


---

Comment by iandrus created at 2010-03-30 21:24:09

I'm not sure I made the readme any simpler, but at least it should be accurate once we start distributing the sage application.


---

Comment by jhpalmieri created at 2010-03-31 16:58:59

See also #6938.


---

Comment by kcrisman created at 2010-04-22 01:59:41

This looks fine to me.  Positive review if we ever actually distribute these.

What we really need to do is distribute the notebook binary and also just a regular (perhaps non-bundle) binary, but maybe this is a lot to host when it comes to mirrors?  

Or, again, figure out how to make the app bundle let you choose between command line and notebook.


---

Comment by kcrisman created at 2010-04-28 18:13:18

With respect to #6938, be sure to only do this with the copy in /local/bin .  The other one should probably be removed.


---

Comment by kcrisman created at 2010-09-08 14:41:21

#9873 is related, and may eventually supersede this.


---

Comment by mpatel created at 2010-09-28 11:24:10

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 11:24:10

## Release manager

Please close this ticket as a "duplicate" when #9873 is merged.


---

Comment by kcrisman created at 2010-09-29 18:45:34

Replying to [comment:12 mpatel]:
> == Release manager ==
> 
> Please close this ticket as a "duplicate" when #9873 is merged.

Or, 'merge' this one first and then #9873 (as noted in that ticket's comments).


---

Comment by kcrisman created at 2010-09-29 20:08:59

Replying to [comment:13 kcrisman]:
> Replying to [comment:12 mpatel]:
> > == Release manager ==
> > 
> > Please close this ticket as a "duplicate" when #9873 is merged.
> 
> Or, 'merge' this one first and then #9873 (as noted in that ticket's comments).
Sorry for the noise - jhpalmieri is right in his comments in #9873.  Treat as previously mentioned.


---

Comment by mpatel created at 2010-09-29 23:17:48

Resolution: duplicate
