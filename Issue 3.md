# Issue 3: control-enter doesn't work in the notebook in firefox on the mac

Issue created by migration from Trac.

Original creator: David Harvey <dmharvey@math.harvard.edu>

Original creation time: 2006-09-11 11:22:29

Assignee: somebody

Summary says it all.....

Firefox version string:

Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.6) Gecko/20060728 Firefox/1.5.0.6



---

Comment by was created at 2006-09-14 08:22:58

For the record it does work with Safari...


---

Comment by boothby created at 2006-09-14 18:24:53

Resolution: wontfix


---

Comment by boothby created at 2006-09-14 18:24:53

This bug is in firefox, not SAGE.

https://bugzilla.mozilla.org/show_bug.cgi?id=106048

Any reasonable workaround in my code would break future versions.  It would also require a rather massive rewrite of otherwise good (IMO) code.

In the meantime, mac users can pull the patch at my darcs repository entitled "firefox mac workaround: ctrl+enter -> alt+enter".

My repository is located at:
http://sage.math.washington.edu/home/boothby/sage/devel/sage
