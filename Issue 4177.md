# Issue 4177: Put Sage version in Notebook

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-09-23 18:18:17

Assignee: boothby

Under the "Sage notebook" on the upper left in the home page as well as in the individual worksheets, it might be nice to have the Sage version number of that installation in a small font, to remember - as well as to enhance bug reports coming from non-installing users.


---

Attachment


---

Comment by kcrisman created at 2008-10-17 19:05:40

Since the word "Notebook" appears in slightly different height in Safari vs. Firefox, the placement looks better in Safari; even with that and using the smallest font size HTML supports it looks ok.


---

Comment by jhpalmieri created at 2008-10-17 20:56:54

Looks good to me, both the code and the appearance in Firefox on linux. One style question: is it any better to put the line

```
from   sage.version        import version
```

in the code for `html_banner` instead of at the top of the file? I'm a Python novice, so I have no idea which way is better.

I'll give it a positive review regardless of the location of the `import` statement.


---

Comment by mabshoff created at 2008-10-18 19:05:38

This patch breaks the twist.py doctest:

```
sage -t -long devel/sage/sage/server/notebook/twist.py      
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/twist.py", line 1505:
    sage: E.render(None)
Expected:
    <twisted.web2.http.Response code=200, streamlen=603>
Got:
    <twisted.web2.http.Response code=200, streamlen=701>
**********************************************************************
```

The fix is trivial, so I will post a reviewer patch in a second.

Cheers,

Michael


---

Attachment

The reviewer patch "..." the length since it will otherwise break from version to version.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 19:13:59

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 19:13:59

Merged in Sage 3.2.alpha0
