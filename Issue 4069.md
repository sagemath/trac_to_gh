# Issue 4069: support "application shortcut" in chrome and gears

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2008-09-06 14:47:46

Assignee: schilly

Some additional lines in the html-header enable proper handling of the sage notebook as a "desktop application". There, all elements from the browser UI are removed and it looks like an application with a shortcut on the desktop or start menu. This is probably more widespread used once HTML 5 ideas are used in other browsers as well.

I'll attach nice icons and a text to this ticket.

[read more here `@`google chrome webmasters/section 15.](http://www.google.com/chrome/intl/en/webmasters-faq.html#tools) and the link to the gears desktop api


---

Comment by ahupfer created at 2008-10-31 19:26:23

Implements a "Create Shortcut" link that is displayed in in the "list worksheets" view that is displayed if the user has installed Google Gears.

The images included need to be places in the data/extcode/notebook/images folder and provide the application shortcut image requested by gears.


---

Comment by ahupfer created at 2008-11-02 21:22:39

shortcut patch for extcode repository


---

Attachment

shortcut patch for main repository


---

Attachment

The images aren't in either of the patches. I think you have to do ` hg export --git `


---

Comment by TimothyClemans created at 2008-11-10 03:21:54

Depends on #3950


---

Comment by TimothyClemans created at 2008-11-10 03:47:50

Don't apply sage-4069_2.patch if #3950 not in. The first two patches work with the lastest sage-3.2. The last patch makes this work when #3950 is merged in.


---

Comment by mabshoff created at 2008-11-25 12:31:34

Mike,

any news on the ticket reviews you promised to Timothy? I want to hold off on this merge until #3950 is in, so until then this lovely ticket will bitrot :(

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-07 11:46:58

Now that #3950 is in this one can go in, but we need a rebase:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_4069_shortcut_sage.patch 
patching file sage/server/notebook/notebook.py
Hunk #2 FAILED at 1319.
Hunk #3 succeeded at 1324 (offset -44 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej
```

Once it is rebased it will go in.

Cheers,

Michael


---

Attachment

Rebased


---

Comment by TimothyClemans created at 2008-12-22 18:36:40

Apply shortcut_extcode.patch and sage-4069_2.patch


---

Comment by mabshoff created at 2008-12-23 21:03:07

Resolution: fixed


---

Comment by mabshoff created at 2008-12-23 21:03:07

Merged shortcut_extcode.patch and sage-4069_2.patch in Sage 3.2.3.alpha0
