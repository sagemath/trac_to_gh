# Issue 3490: notebook -- improve registration error checking and reporting

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-06-21 04:48:49

Assignee: boothby

Keywords: editor_wstein

This is a follow up to #3483.

is_valid_username should be upgraded to follow this rule:

```
Your username must start with a letter and be between 4 and 32 characters long. You may only use letters, numbers, underscores, and one dot (.).
```


A new function, is_valid_password, should be added that follows this rule:

```
Your password must be between 6 and 32 characters long. Your password can not contain your username nor spaces.
```


Check to make sure the input for password and retype_password are the same.

Currently only one error is reported even if there is several of them. Report all errors to the user.

Don't loose the user's input except for password/retype_password when returning error reports.


---

Attachment


---

Attachment


---

Attachment

note: sage-3490_2.patch puts a somehow removed extract_title function


---

Comment by boothby created at 2008-06-24 07:15:41

nice


---

Comment by mabshoff created at 2008-06-25 06:34:13

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-25 06:34:13

Resolution: fixed
