# Issue 3944: replace "sage -upgrade" by "sage -expert_upgrade" and upgrade() by "expert_upgrade()"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-24 16:15:35

Assignee: mabshoff

I'm sick of people thinking "sage -upgrade" is supposed to work if you're a newbie user.  That was absolutely never the intention with the current design, and there's no way we should suggest it is.
New users, or those not familiar with building from source, should have to redownload rather than upgrade.   Maybe someday we'll have binary upgrades, but "sage -upgrade" certainly isn't that.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-08-24 17:08:56

Patch looks good to me.

Cheers,

Michael


---

Comment by malb created at 2008-08-24 23:21:20

to be honest, I don't like the name that much. If you insist on renaming the thing then maybe `dev_upgrade` or `developer_upgrade` could be a better choice than "expert". I wouldn't want to call myself an expert but I'll use that function.


---

Comment by was created at 2008-11-22 22:51:28

Resolution: wontfix
