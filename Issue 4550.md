# Issue 4550: notebook -- removed unused NotebookSettings and UserSetting related code

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-11-19 16:59:54

Assignee: boothby

CC:  wjp

Depends on #4089


---

Attachment

Just out of curiosity, what is the justification for removing this code, besides "it currently isn't being used"?  For example, did you (Timothy) write new settings code that will replace this?   I think maybe (?) I wrote this code a long time ago as the framework that user and notebook settings code would go into, but never flushed that out.  So unless there is no code that is going to replace or some new design or *something*, I would like some sort of explanation about what the point of this is.


---

Comment by TimothyClemans created at 2008-12-07 02:04:26

I implemented Notebook and User settings without using the pre-existing framework. User Settings is already in Sage and Notebook Settings is #4551


---

Attachment


---

Comment by TimothyClemans created at 2008-12-21 20:59:32

apply sage-4550.patch (rebased)


---

Attachment

rebased on 4.1.2.alpha0


---

Comment by ddrake created at 2009-09-05 01:21:29

I'm going to try and go through this group of notebook patches and rebase them so we can at least discuss them.


---

Comment by mpatel created at 2009-10-10 07:30:23

See #4551 for a sagenb (cf. #6983) rebase that includes [attachment:trac_4550-2.patch].


---

Comment by mpatel created at 2009-10-23 07:17:56

Changing status from needs_review to needs_info.


---

Comment by mpatel created at 2009-10-23 07:17:56

#4551 subsumes this ticket.  Please close this one.


---

Comment by was created at 2009-12-09 14:28:26

Resolution: invalid
