# Issue 2987: [with patch; needs review] Debian build support for zn_poly

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-04-21 06:32:09

Assignee: tabbott

I've made a Debian package for zn_poly.  Patch is attached.  


---

Attachment


---

Comment by mabshoff created at 2008-04-21 07:03:38

Tim, ther is some predecessor patch missing. Neither the 0.4.1.p0 nor the 0.8.p0 spkg has any dist/debian directory. So, is there another patch?

Cheers,

Michael


---

Comment by tabbott created at 2008-04-21 15:55:23

Ahh, I did 3 commits and "hg export"ed all 3 to make this patch file.  Lower down in the patch file it creates the directories.  Maybe this doesn't actually work.


---

Comment by mabshoff created at 2008-04-22 03:43:19

Tim,

for mercurial you cannot concatenate patches - at least not in the order you did with this patch. I cut the three patches apart and applied them to 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/final/zn_poly-0.8.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-22 03:43:38

Resolution: fixed


---

Comment by mabshoff created at 2008-04-22 03:43:38

Merged in Sage 3.0.final
