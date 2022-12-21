# Issue 5147: make plot output file in DOCTEST_MODE changeable for sage-mode.el

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-02-01 02:42:56

Assignee: mabshoff

Keywords: doctest plot output filename

Whilst incorporating sage-view.el into sage-mode.el, I needed to be able to change the output filename while in DOCTEST_MODE.  This tiny patches adds a module scope variable name with the output file name.


---

Attachment


---

Comment by ncalexan created at 2009-02-01 02:48:13

I see this as harmless, and it is very useful to me and users of sage-mode.el...


---

Comment by mhansen created at 2009-02-01 20:37:44

Looks good to me.


---

Comment by mabshoff created at 2009-02-02 02:57:51

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 02:57:51

Resolution: fixed
