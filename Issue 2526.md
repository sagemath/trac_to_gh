# Issue 2526: switch charpoly mod p back to linbox as default

Issue created by migration from https://trac.sagemath.org/ticket/2526

Original creator: mabshoff

Original creation time: 2008-03-15 02:08:59

Assignee: was

Due to problems with LinBox's charpoly mod p we switched the default implementation to use in 2.10.3 to the native Sage version. Since Linbox is about three times as fast switch back the default.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 02:09:19

This depends on #2525 to be merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 05:19:01

this patch straight up revers #2453


---

Attachment


---

Comment by cremona created at 2008-03-27 17:24:46

As I don't know what the problems were with the linbox function originally, or whether that problem has been fixed, I don't know whether switching the default back to linbox is a good idea!


---

Comment by mabshoff created at 2008-03-27 17:34:53

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-03-27 17:34:53

Replying to [comment:4 cremona]:
> As I don't know what the problems were with the linbox function originally, or whether that problem has been fixed, I don't know whether switching the default back to linbox is a good idea!

Hi John,

the bug in LinBox still hasn't been fixed. Hence this patch will not be applied until the LinBox.spkg with the bug fix will be merged in Sage. It looked initially that this would happen quickly, but that didn't go as planned. Since the bug is trivial and has a positive review it can be instantly merged once the upstream fix in LinBox has happened.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-27 17:34:53

Changing status from new to assigned.


---

Comment by cremona created at 2008-03-27 17:51:34

Sounds good -as long as it doesn't get forgotten!


---

Comment by mabshoff created at 2008-03-28 08:09:38

Replying to [comment:6 cremona]:
> Sounds good -as long as it doesn't get forgotten!

Nah, it is actually listed on my internal ToDo list. And I am sure Clement and William will also remember. Since it has a positive review it always pops up when I look for tickets than can be merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-04 01:09:33

An equivalent patch was merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-04 01:09:33

Resolution: fixed
