# Issue 3429: New linbox 1.1.6 spkg

Issue created by migration from Trac.

Original creator: cpernet

Original creation time: 2008-06-15 20:13:43

Assignee: cpernet

Upgrade linbox to 1.1.6 release.
The new release includes the sage interface, so the new spkg should shave out the old linbox_wrap.



---

Comment by cpernet created at 2008-06-15 20:16:27

Changing status from new to assigned.


---

Comment by cpernet created at 2008-06-15 20:16:27

The proposed new linbox spkg is available at
http:/sage.math.washington.edu/home/pernet/linbox-1.1.6rc0.spkg


---

Comment by craigcitro created at 2008-06-15 21:56:11

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-06-26 03:44:04

The spkg builds fine for me on OSX and Linux x86-64 and doctests fine. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 03:44:17

Resolution: fixed


---

Comment by mabshoff created at 2008-06-26 03:44:17

Merged in Sage 3.0.4.alpha1


---

Attachment

Fix the new naming convention (include files and libraries) for linbox-1.1.6rc0


---

Comment by cpernet created at 2008-06-27 21:19:29

Changing priority from major to blocker.


---

Comment by cpernet created at 2008-06-27 21:19:29

Changing type from enhancement to defect.


---

Comment by cpernet created at 2008-06-27 21:19:29

Reopening this ticket, since I forgot to update the sage hooks on the linbox library.
Everything went well on installations that had the previous library installed. So the problem only proped up when doing a fresh install.
See [http://groups.google.fr/group/sage-devel/browse_thread/thread/a7067a9a6c9464fc](http://groups.google.fr/group/sage-devel/browse_thread/thread/a7067a9a6c9464fc)

I am attaching a patch fixing this.


---

Comment by cpernet created at 2008-06-27 21:19:50

Resolution changed from fixed to 


---

Comment by cpernet created at 2008-06-27 21:19:50

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-06-30 04:58:13

Positive review on update_new_linbox_interface.patch. After applying to a fresh build of 3.0.4.alpha1 the Sage library builds and passes doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-30 04:58:26

Resolution: fixed


---

Comment by mabshoff created at 2008-06-30 04:58:26

Merged update_new_linbox_interface.patch in Sage 3.0.4.alpha2
