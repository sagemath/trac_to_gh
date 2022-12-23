# Issue 3967: Totallyreal "just print" feature added

Issue created by migration from https://trac.sagemath.org/ticket/3967

Original creator: jvoight

Original creation time: 2008-08-27 17:21:54

Assignee: was

CC:  craigcitro

I added a small feature to "just print" long lists of fields in totallyreal rather than storing them to memory.  Patch attached.


---

Attachment


---

Comment by mabshoff created at 2008-08-27 19:10:38

Craig,

you are the canonical person to review this small patch :)

Cheers,

Michael


---

Comment by craigcitro created at 2008-09-20 08:44:20

This looks good. I went ahead and re-based this on 3.1.2 with my patch from #4155 applied, since it makes sense to apply that first. 

John, you should at least glance to make sure I didn't mess anything up rewriting the patch, just for the sake of having a second set of eyes look at it.


---

Comment by jvoight created at 2008-09-20 17:04:30

Changing status from new to assigned.


---

Comment by jvoight created at 2008-09-20 17:04:30

Changing assignee from was to jvoight.


---

Comment by jvoight created at 2008-09-20 17:04:30

Yes, all looks well.  I'm reviewing #4155 now.  JV


---

Comment by jvoight created at 2008-09-20 17:05:22

Resolution: worksforme


---

Comment by jvoight created at 2008-09-20 17:05:35

Changing status from closed to reopened.


---

Comment by jvoight created at 2008-09-20 17:05:35

Resolution changed from worksforme to 


---

Comment by jvoight created at 2008-09-20 17:06:56

Sorry to be such a tool about changing the status of this ticket.  I wasn't sure what to set it to so as to indicate that it is ready for inclusion, once #4155 gets resolved.  JV


---

Comment by mabshoff created at 2008-09-20 20:45:30

Hi John,

FYI: the release manager closes a ticket once it is merged/determined to be invalied/etc.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-21 18:08:41

Craig,

the rebased patch is broken: Toward the end you do not rename jp to jp_file and hence things do not compile. I will fix this in my tree and do some valgrinding.

Cheers,

Michael


---

Comment by craigcitro created at 2008-09-21 20:20:21

Oops ... you were absolutely right, mabshoff. I've fixed it up, and tested it out.


---

Comment by craigcitro created at 2008-09-22 05:28:44

Rebased John's patch for 3.1.2, depends on trac #4155 (both patches)


---

Attachment

Merged trac-3967-rebase.patch in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 00:09:36

Resolution: fixed
