# Issue 3591: notebook -- remove notebook.save()  from Logout

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-07-07 21:16:19

Assignee: TimothyClemans

On sagenb.org it takes several seconds to logout because in class Logout(resource.Resource) in twist.py notebook.save() is called. That is very bad.


---

Attachment

Also removed "child_logout = Logout()" from Toplevel resource because it's already in UserToplevel and anonymous users can't logout anyways.


---

Comment by ncalexan created at 2008-08-10 23:27:48

After discussion with was, this sounds good.  Apply!


---

Comment by mabshoff created at 2008-08-11 02:40:15

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 02:40:15

Resolution: fixed
