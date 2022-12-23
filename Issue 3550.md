# Issue 3550: notebook -- make saving and loading state of the notebook vastly faster and scale better

Issue created by migration from https://trac.sagemath.org/ticket/3550

Original creator: was

Original creation time: 2008-07-04 09:01:50

Assignee: boothby

This is an alternative to #3456.  It takes the view that the notebook is more like a web page -- lots of pages as text files -- than a database.    

This is a simple solution that is completely implemented in this patch.


---

Attachment

first patch -- does everything but needs more testing and documentation


---

Comment by was created at 2008-07-04 11:18:58


```
BEFORE: 
  TIME: Several *minutes* to store.
  SPACE: 310MB.

AFTER THIS PATCH, which automigrates the sage notebook:
  TIME: 6.7 seconds to save (on sage.math)
  SPACE: 8.8MB.
```


So basically everything is about 30 times faster / smaller. 

The main problem is that I might have introduced bugs, and of course 7 seconds
is a lot longer than nothing.  But this seems like a worthwhile payback for
3 hours of work.

NOTE: There are no doctests yet, since those are very strange to write for the notebook.


---

Comment by was created at 2008-07-04 11:25:40

this should do it (modulo doctests)


---

Attachment


---

Comment by was created at 2008-07-05 17:57:51

add doctests and made sure all existing tests pass


---

Comment by was created at 2008-07-05 17:58:13

Changing keywords from "" to "editor_wstein".


---

Attachment

This is now fully ready for review.


---

Comment by mabshoff created at 2008-07-06 00:06:48

This code has gone live on sagenb.org, so it seems to work. William has also merged a bundle into my Sage 3.0.4.alpha2 tree since there was a conflict with one of Timothy's patches.

Cheers,

Michael


---

Attachment

Merged sage-3550-part1.patch to sage-3550-part4.patch in Sage 3.0.4.alpha2

Cheers,

Michael


---

Comment by boothby created at 2008-07-06 20:16:33

excellent!


---

Comment by mabshoff created at 2008-07-06 20:18:18

Resolution: fixed


---

Comment by mabshoff created at 2008-07-06 20:18:18

Merged in Sage 3.0.4.alpha2
