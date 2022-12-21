# Issue 1475: notebook -- lprint() -- make an option so lprint is done automatically

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 15:28:19

Assignee: boothby


```
[07:23am] ikaruga2099: while make test is running.... do you know how to enable the auto latex output (as per the presentation on the website)? Currently, if I do latex(command), I get back text not a typeset equation...
[07:23am] william-doctest-: lprint()
[07:24am] ikaruga2099: oh.... is there a way to have that called automatically?
[07:26am] william-doctest-: Not *yet*.  It's planned.  I'll create a trac ticket.
```



---

Comment by was created at 2007-12-12 15:28:26

Changing type from defect to enhancement.


---

Comment by TimothyClemans created at 2008-02-23 22:37:30

Resolution: fixed


---

Comment by mabshoff created at 2008-02-24 02:44:24

Please do not randomly close tickets (even if they have been fixed) without either checking with William or the release manager in IRC. Instead mark the subject as "[probably fixed]" instead.

Cheers,

Michael


---

Comment by TimothyClemans created at 2008-02-24 02:50:01

This was merged in a while ago. It is the checkbox at the top in a given worksheet.


---

Comment by was created at 2008-02-24 04:46:39

Resolution changed from fixed to 


---

Comment by was created at 2008-02-24 04:46:39

This is not merged.  This is not the checkbox at the top. The idea would
be that there would be a user configuration panel with an option so that 
all worksheets would do latex printing by default.


---

Comment by was created at 2008-02-24 04:46:39

Changing status from closed to reopened.


---

Comment by TimothyClemans created at 2008-09-08 16:48:40

Relies on #3937


---

Comment by TimothyClemans created at 2008-11-11 20:29:13

Depends on #4135. Don't apply extcode-1475_1.patch


---

Attachment

I've attached a patch which is all of the previous ones folded together.  This code doesn't actually work; it creates the option, but setting it to True doesn't actually cause the output in the notebook to be typeset by default.

Also, please don't say that this depends on #4135 as it does not.

Using Mercurial queues would allow you to make single patches as opposed to multiple little ones and would allow you to see what actually depends on what.


---

Comment by was created at 2009-10-21 07:46:24

Resolution: duplicate


---

Comment by was created at 2009-10-21 07:46:24

Jason Grout implemented the same thing in the meantime, I think.
