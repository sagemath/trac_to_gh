# Issue 3645: tutorial: make documentation for .n() more prominent

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-07-11 22:00:04

Assignee: tba

Keywords: tutorial, editor_mhansen

In response to the discussion in the thread

[http://groups.google.com/group/sage-support/browse_frm/thread/3c6972e69d1b80d8](http://groups.google.com/group/sage-support/browse_frm/thread/3c6972e69d1b80d8)

I've tried to make the documentation for the .n() method more prominent.


---

Comment by jhpalmieri created at 2008-07-11 22:01:39

(Oh, and I made one other little change: in the notebook interface, the documentation link is called "Help", not "Documentation", so I changed the tutorial to reflect this.)


---

Attachment


---

Comment by cremona created at 2008-07-11 22:07:02

Looks good to me!


---

Attachment

REFEREE REPORT:

I've added a patch that
  1. Note that capital N is a synomym for n?
  2. Note that digits is the number of *decimal* digits?

With that I give this a positive review. 

 -- William


---

Comment by jhpalmieri created at 2008-07-25 02:20:20

One small change: I changed William's new example to use N(-), since we didn't have an example like that yet.

This new patch replaces all of the other patches (I thought that would be easier than having to apply three patches).


---

Comment by mabshoff created at 2008-07-30 23:21:27

Resolution: fixed


---

Attachment

Merged 3645-newest.patch in Sage 3.1.alpha0
