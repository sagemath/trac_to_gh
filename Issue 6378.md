# Issue 6378: make sage -merge more user-friendly

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-06-21 19:32:32

Assignee: tbd

CC:  craigcitro leif

A few features would be nice to add to sage -merge:

 1. Ask all questions at the start instead of between tickets (that way, the user can kick off the process and just wait until it finishes, instead of having to check back every 20 minutes)
 1. Display comments with the patches
 1. Email a final report

Also, sage -merge doesn't properly handle the '-a -f' combination.  Fix that.


---

Comment by boothby created at 2009-06-21 19:38:53

The above adds all but the email functionality.  I'll add that in pretty soon.


---

Comment by boothby created at 2009-06-21 19:39:26

Changing type from defect to enhancement.


---

Comment by boothby created at 2009-06-21 19:39:26

Changing component from algebra to build.


---

Comment by boothby created at 2009-06-21 19:39:26

Changing priority from major to minor.


---

Comment by boothby created at 2009-06-22 21:01:58

Using `sage -merge`, I managed to hose the system pretty hard.  I'm pretty sure that an exception occurred which resulted in a bad patch not getting popped after some sort of failure.  Hopefully, part 2  will prevent that from happening again.  Part 3 fixes a typo in part 2.


---

Comment by craigcitro created at 2009-06-22 23:00:14

I guess I'm a little confused -- you've mentioned that the problem you were hitting is that the script would often forget to pop patches from the queue, yet you've removed code that pops patches in several places. That seems confusing to me ... in particular, in 4 places in the second patch above, you've removed code that pops patches -- why?


---

Attachment

flattened & based on 4.0.2


---

Comment by boothby created at 2009-06-26 05:49:48

note, the 4 places I removed code to pop patches is actually handed in the calling function -- hence, it should be more robust, not less as a result.


---

Comment by craigcitro created at 2009-08-28 07:22:22

I'm generally happy with Tom's changes. In fact, one should note that no patch of his needs merged -- these changes are already live in sage 4.1 and 4.1.1. Looks like someone's been editing trunk. (`*tsk tsk*`)

My referee report comes in the form of two new patches, one for the bin repo, and the other for the main repo. The change to the main repo is tiny -- it's just changing `sage/misc/hg.py` to use the new `subprocess` module instead of `popen3`, because the deprecation warning is annoying to see in the output of `sage -merge`. I could easily be convinced to move this to a new ticket, if people would prefer that. 

The patch to the bin repo does the following:

 * remove a dirty hack involving `tee` by using python's `subprocess` module
 * add a few comments about the hackish parsing of trac pages
 * use `urllib2` to parse urls
 * be (unnecessarily?) pedantic about `os.path.join` instead of explicit use of `/`
 * clean up some spacing and indentation issues
 * add an option to e-mail when a run of `sage -merge -a` finishes

I ran some tests, but I didn't do any exhaustive testing on `sage.math`, which should probably be done. (I'm currently on vacation, and without good internet access.)


---

Comment by craigcitro created at 2009-08-28 07:22:40

apply to bin repo


---

Attachment

apply to main repo


---

Attachment

Question:  how well is this documented?  As well as all the functions in the scripts having docstrings, I think we need to have this all properly in the developers manual.  Recently I wanted to demonstrate the merge feature to a newcomer, and found that I couldn't remember what all the command line options were, and could not find them documented.  (Of course, it is possible that they are somewhere!  I remember seeing them in a sage-devel post, but that is hardly acceptable!)


---

Comment by craigcitro created at 2009-08-31 14:36:44

This is a very good point. I wrote up an explanation at `wiki.sagemath.org/release`, but there should be some documentation in the source itself. I'll work on that and post another patch -- after all, documentation makes things *much* more user-friendly. `:)`


---

Comment by cremona created at 2009-08-31 15:50:33

Great -- I also meant that when you get this:

```
Usage: sage -merge <ticket_number>
For more advanced usage, see the file /home/john/sage-4.1.1/local/bin/sage-apply-ticket.
```

then as well as finding something human-readable in that script file, there could be more usage instructions in (say) the reference manual.

That should go for all the other command-line options, of course: a sort of "man sage"-type output.

Anyway, adding a reference to wiki.sagemath.org/release would already be useful!


---

Comment by leif created at 2010-01-31 23:23:51

Replying to [comment:9 craigcitro]:
> I wrote up an explanation at `wiki.sagemath.org/release`, but there should be some documentation in the source itself. I'll work on that and post another patch -- after all, documentation makes things *much* more user-friendly. `:)`


Meanwhile(?) http://wiki.sagemath.org/release appears to be a dead link.

http://wiki.sagemath.org/devel/ReleaseManagement is all I've found.

[I really love trac... I *did not* delete `work_issues` (it was empty; same for `upstream`).]

-Leif


---

Comment by craigcitro created at 2010-02-01 17:00:35

Hi Leif,

Yep, you're right -- someone moved that content and didn't leave a link. You're right -- the content was moved to the second link you mention. I've left a note pointing people to the right place on the wiki ...

Thanks!


---

Comment by timdumol created at 2010-04-18 13:20:09

Rebase on #8712. Apply this patch only. See comments for more info.


---

Attachment

The patch to the main Sage respository is unneeded now, as it's been fixed already by sage-4.4.alpha0. The patch to the scripts repository works fine, except for the email part. It doesn't get the mail argument. Calling it with, say,


```
sage -merge -a -e timdumol`@`gmail.com
```


results in an error after merging everything, stating that the email address, which is the null string (''), is invalid.

This patch rebases it on #8712, while adding the requested documentation. This seems to detect the email argument.


---

Comment by jhpalmieri created at 2010-06-23 21:15:33

This needs a little rebasing because of my referee's patch at #8712.  See the new patch; this replaces the previous one(s).

Otherwise, I'm happy with it.


---

Attachment

use this patch only


---

Comment by jhpalmieri created at 2010-06-23 21:23:09

(The only differences between my patch and the previous one are at the top, the printing of the help messages.)

See #9319 for a follow-up.


---

Comment by jhpalmieri created at 2010-07-22 22:36:13

I'm willing to give timdumol's version a positive review.  If someone can review mine (the help messages on lines 95-110 are the only difference), that would be appreciated.


---

Comment by leif created at 2010-07-22 23:39:13

Replying to [comment:16 jhpalmieri]:
> I'm willing to give timdumol's version a positive review.  If someone can review mine (the help messages on lines 95-110 are the only difference), that would be appreciated.

Hmmm, I'm ok with John's new help messages, but when will more return codes be tested?

I can't tell if this ticket is that urgent s.t. we should postpone such to the follow-up.

At least there is already one... (#9319) ;-)


---

Comment by jdemeyer created at 2012-08-13 12:35:33

Changing component from build to scripts.


---

Comment by jdemeyer created at 2013-05-22 09:24:20

`sage -merge` is gone.


---

Comment by jdemeyer created at 2013-05-22 09:24:20

Resolution: invalid
