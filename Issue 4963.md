# Issue 4963: Make a screen-full of whitespace at the bottom of the notebook cells

Issue created by migration from https://trac.sagemath.org/ticket/4963

Original creator: jason

Original creation time: 2009-01-11 00:55:31

Assignee: boothby

CC:  mhansen tclemans

Not having this causes interacts to jump off the page when updating, for example.  See http://groups.google.com/group/sage-devel/browse_thread/thread/51b538c8212fa2a/b61655921eb0ebab


---

Comment by jason created at 2009-01-11 00:58:45

Fixing this might also help in resolving #2629


---

Comment by jason created at 2009-01-14 08:01:53

Changing assignee from boothby to jason.


---

Comment by jason created at 2009-01-14 08:01:53

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-01-21 17:41:39

After testing with Firefox 2 and 3 and Safari on OSX.4 PPC, it seems to perform as advertised.  So positive review of its effect!  This is very useful to those of us who use interacts a lot in class, where the jumping away from the interact makes Sage look cheap as in beer, not free as in speech (or beer).

It does not resolve #2629 (though it makes it less likely to happen; see comments on #2629).

But I request another review or additional work, because the aesthetics of adding that margin-bottom 80% are still hackish at best.  For instance, very often the browser does not now jump to the next cell (where the focus has shifted), even if the jump would be fairly minimal but at the bottom of the browser.  Is this a somewhat different behavior than in the past?  It could be especially weird if someone hasn't used the notebook before, and hence doesn't know what happened to the focus after evaluating - again, if this is new behavior; perhaps it is not.

Given the discussion mentioned in the description, it sounds like this is not a big deal, but I don't feel comfortable giving final positive review on that aspect of things, since I haven't worked on the notebook, I just use it.


---

Comment by jason created at 2009-01-21 23:31:57

Before this patch, we still have problems with the browser scrolling not following the focus or tab-completion menu, like described above.  I thought maybe this fix would help, but apparently more needs to be done.

I did notice that this patch also extends the "Home" page of the notebook which lists the worksheets.  The problem there is that the "body" command used in each page is the same.  I've updated the patch to fix this.  This should probably be re-reviewed.  One thing that might be reviewed is that I actually changed *two* body elements; is one of them redundant?


---

Attachment


---

Comment by boothby created at 2009-01-22 18:59:11

That is, in fact, a large amount of space.  Well done.


---

Comment by mabshoff created at 2009-01-23 09:40:00

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 09:40:00

Resolution: fixed
