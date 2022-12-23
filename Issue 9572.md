# Issue 9572: SageNB 0.8.2

Issue created by migration from https://trac.sagemath.org/ticket/9572

Original creator: mpatel

Original creation time: 2010-07-22 03:40:26

Assignee: jason, was

CC:  acleone leif timdumol

This should include #9554 and perhaps other positively reviewed notebook tickets.


---

Comment by ddrake created at 2010-07-23 02:38:54

You might consider #8574 and #9512, which are both positively reviewed.


---

Comment by ddrake created at 2010-07-23 02:39:42

Replying to [comment:1 ddrake]:
> You might consider #8574 and #9512, which are both positively reviewed.

Er, I mean, #8754.


---

Comment by mpatel created at 2010-07-23 07:16:13

All long doctests pass for me on sage.math with 4.5.2.alpha0 + sagenb-0.8.2.spkg.  But given my current computer setup, I can't run the Selenium tests.


---

Comment by mpatel created at 2010-07-23 07:16:13

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-23 07:21:56

Remember to do http://trac.sagemath.org/sage_trac/ticket/9580#comment:2 ...


---

Comment by cwitty created at 2010-07-24 23:02:48

Changing status from needs_review to needs_work.


---

Comment by cwitty created at 2010-07-24 23:02:48

Doctests and selenium tests passed for me, using Firefox (well, Iceweasel) 3.6.4.  (Except for test_7434, which failed with both sagenb 0.8.1 and 0.8.2, presumably because I don't have Java set up on this machine.)

This will be a positive review once you fix #9580 :)


---

Comment by cwitty created at 2010-07-25 00:04:52

Actually, I found a bug: the "source editor" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).

Given the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.


---

Comment by mpatel created at 2010-07-25 07:56:27

In order to have a new SageNB package ready for 4.5.2, I've decided to change #9512's status to _needs_work_ and "unmerge" it from SageNB 0.8.2.  I've included #3342, #9554, and #9580 in an updated SageNB 0.8.2, which is available at the link in the description.

Note: I haven't added a patch level (e.g., `sagenb-0.8.2p0.spkg`), but I have renamed the previous version to `sagenb-0.8.2-9572.spkg`.


---

Comment by mpatel created at 2010-07-25 07:56:27

Changing status from needs_work to needs_review.


---

Comment by cwitty created at 2010-07-25 19:28:43

Doctests and selenium tests passed (except, again, for test_7434).

Positive review.


---

Comment by cwitty created at 2010-07-25 19:28:43

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-26 07:49:08

Resolution: fixed


---

Comment by mpatel created at 2010-07-27 02:12:56

Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.

(I should have followed [our own advice](http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5/0962395dd19cc9c6#0962395dd19cc9c6)!)


---

Comment by mpatel created at 2010-07-27 02:15:04

Replying to [comment:10 mpatel]:

> Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.

But if it's too late for 4.5.2.alpha1, we could, I think, just include the patch in 4.5.2.rc0.


---

Comment by ddrake created at 2010-07-27 02:41:59

Replying to [comment:10 mpatel]:
> Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.
> 
> (I should have followed [our own advice](http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5/0962395dd19cc9c6#0962395dd19cc9c6)!)

Yes, you should have. :)  You're lucky though, I managed to sneak it into alpha1.
