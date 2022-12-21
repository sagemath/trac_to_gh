# Issue 901: minor addition to prog.tex

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-10-15 01:06:27

Assignee: wdj

To view a hg patch bundle as a text file, you can use the
hg_sage.inspect('patchname.hg') command. This was added to 

http://www.sagemath.org/doc/html/prog/node72.html

The patch is at
http://sage.math.washington.edu/home/wdj/patches/prog.tex.hg

Though "inspect" seems to work on "source code" patches, it does not 
seem to work on doc patches.





---

Comment by cwitty created at 2007-10-15 02:36:13

To view a doc patch, you can use `hg_doc.inspect('pathname.hg')`.


---

Comment by was created at 2007-10-21 00:45:16

This patch is against hg_sage again.  So it doesn't have any documentation in it, as claimed.


---

Comment by wdj created at 2007-10-21 00:59:17

I think the new version of this patch 
http://sage.math.washington.edu/home/wdj/patches/prog.tex.hg
is the right one.


---

Comment by was created at 2007-10-21 01:51:47

same as #899 -- no changes found.


---

Comment by wdj created at 2007-10-21 02:56:08

Possibly they are both in the patch
http://sage.math.washington.edu/home/wdj/patches/inst-prog-2007-10-20.hg


---

Comment by cwitty created at 2007-10-27 04:55:07

Resolution: fixed
