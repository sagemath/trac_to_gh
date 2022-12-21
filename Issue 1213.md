# Issue 1213: strange unused file sage/plot/mpl_wrapper.py should be fixed or deleted

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-20 05:16:21

Assignee: was

I think that mpl_wrapper.py is obsolete, dead code.  Nothing else in Sage refers to it, it talks about an optional matplotlib package (when matplotlib has been standard in Sage for quite a while), and it mentions downloading matplotlib from UCSD.

Also, in mpl_wrapper.py it mentions the "sage -mpl" option.  In sage-sage, it says

```
    echo "  -mpl          -- run with matplotlib support (requires optional matplotlib package)"
```

but "sage -mpl" does not act obviously different than just "sage".  I'm guessing that all the "-mpl" stuff should be removed from sage-sage, as well.


---

Comment by mabshoff created at 2007-12-26 02:56:36

This is easy enough to do and still a problem with 2.9.1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 22:55:58

Bug Day 10 material?

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-24 02:17:18

We should probably also nuke

```
-rw-r--r-- 1 mabshoff 1090 16115 2007-12-20 17:13 plot3dsoya.py
-rw-r--r-- 1 mabshoff 1090  3054 2007-12-20 17:13 plot3dsoya_wrap.py
```


Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-24 02:17:18

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-05-24 02:17:18

Changing status from new to assigned.


---

Attachment

I tried deleting this file, and all indications are good.  Here's a patch that kills it.


---

Comment by mabshoff created at 2008-08-31 04:54:50

Patch looks good to me.

Cheers,

Michael


---

Attachment


---

Comment by jwmerrill created at 2008-08-31 05:10:15

The new patch also gets rid of the -mpl command line argument, since it doesn't appear to do anything.


---

Comment by mabshoff created at 2008-08-31 05:12:02

Positive review on the scripts repo patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 05:14:11

Merged both patches in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-31 05:14:11

Resolution: fixed
