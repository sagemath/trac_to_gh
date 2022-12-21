# Issue 6363: [with patch, needs review] Display Sage version on notebook login page

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-06-20 12:21:47

Assignee: boothby

Cf. [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/3e8484254e3a1cfb).


---

Attachment


---

Comment by mpatel created at 2009-06-20 12:29:47

The patch displays the Sage version on the notebook login page, e.g.,

```
Sign into the Sage Notebook v4.0.2
```

in place of

```
Sign into the Sage Notebook
```



---

Comment by cremona created at 2009-06-20 13:31:23

Review: patch applies fine to 4.0.2 and does what it says.  I tried both from the command line (sage -notebook) and also using notebook() from Sage prompt.


---

Comment by rlm created at 2009-06-24 09:46:01

Resolution: fixed
