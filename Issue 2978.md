# Issue 2978: Rstats -- make it build with png support

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-21 02:34:11

Assignee: mabshoff

CC:  jdemeyer

On most platforms R with Sage does *not* build with png support.  Fix this and revert #2974 once this is fixed. 


---

Comment by mabshoff created at 2008-12-02 02:28:46

Now that we build libpng dynamically on all systems including OSX this seems like a good idea. This is also required to make the optional doctests in rpy pass.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-02 02:28:46

Changing status from new to assigned.


---

Comment by jason created at 2009-09-16 16:35:29

Changing assignee from mabshoff to jason.


---

Comment by jason created at 2009-09-16 16:35:29

Changing status from assigned to new.


---

Comment by kcrisman created at 2011-06-28 16:30:01

To release manager: This ticket is no longer valid.  There are still some issues with R and graphics on minimal Linux installs without certain libraries, but we have marked such doctests optional and have open tickets for re-enabling this in those cases.    

See for instance #8868 (most relevant) as well as #11249 and #11266.


---

Comment by kcrisman created at 2011-06-28 16:30:01

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-28 16:30:18

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-07-05 10:07:00

Resolution: worksforme
