# Issue 7779: typo in comment of Sage script

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-12-28 15:42:19

Assignee: mvngu

CC:  cremona

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/da735a05781e3945):

```
At the end of the script which runs sage there is this:

# This should kill all children of this process too.
# Uncomment this if you have trouble with orphans.
# Note that you'll get an annoying "Killed" message
# whenver Sage exists.
# kill -9 -$$

where the last but one line should read

# whenever Sage exits.

(2 typos!)
```




---

Attachment

based on Sage 4.3


---

Comment by mvngu created at 2009-12-28 15:44:35

previous version of sage script


---

Attachment

differences between sage.old and sage


---

Comment by mvngu created at 2009-12-28 15:48:59

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-12-28 15:48:59

The script `sage` is found under `SAGE_ROOT` so it is not under revision control. I have attached a new script `sage` which fixes the two typos reported above by cremona. The previous version of this script is attached as `sage.old`. And the differences between `sage.old` and `sage` are contained in `sage.patch`. Only the file `sage` needs to be applied; don't apply the patch file.


---

Comment by mvngu created at 2009-12-28 15:51:00

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 20:45:35

Resolution: fixed
