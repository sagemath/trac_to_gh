# Issue 2830: ace-5.0.spkg fails to install

Issue created by migration from Trac.

Original creator: dunfield

Original creation time: 2008-04-06 14:31:03

Assignee: mabshoff

The optional ace-5.0.spkg for the GAP component fails to install.  It tries to copy itself into the non-existent directory of GAP version 4.4.9 instead of the current version 4.4.10.

This can be fixed by changing line 3 of the spkg-install file to:


```
DEST="$SAGE_LOCAL"/lib/gap-4.4.10/pkg/
```


However, as mabshoff says:

''The proper fix in this  would be to use a variety of "newest_version". Right now it doesn't 
return the proper version you need: ''


```
$SAGE_ROOT/spkg/standard$ ./newest_version gap 
gap-4.4.10.p5 
```

_but after some discussion in debian-sage it now seems likely that we will switch to dashes for the patch level. _



---

Comment by mabshoff created at 2008-04-06 15:11:15

I have uploaded a slightly updated spkg into the repo. It adds a mercurial repo and an .hgignore file. I also renamed it to ace-5.0.p0.spkg since changes to existing packages need to increment the patch level. Otherwise updates are not installed.

The new spkg installs, so positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 15:11:46

Merged into the package repo and mirrored out.


---

Comment by mabshoff created at 2008-04-06 15:11:46

Resolution: fixed
