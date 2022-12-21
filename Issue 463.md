# Issue 463: sage -upgrade:  make it more flexible

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-19 19:32:14

Assignee: was


```
[12:25] <william> interesting feature idea:
[12:25] <william> extend the "sage -upgrade" command so you an give the directory or URL
[12:26] <william> of any other installed version of SAGE, and it will pull everything from there.
[12:26] <william> install any newer spkg's and pull from any active repo.
[12:26] <malb> definitely nice for sysadmins I guess
```



---

Attachment

somewhat orthogonal -- changes to use "sage -br" instead of "sage -ba" on upgrade.  apply to sage repo.


---

Attachment

apply to the scripts repo.


---

Comment by was created at 2008-11-27 01:27:02

To test this out try:

On an older sage install

```
sage -upgrade  # should do a standard upgrade to the latest version of sage
```


On a new sage install

```
sage -upgrade http://sage.math.washington.edu/home/was/build/sage-3.2.1.alpha1
```

to upgrade to the latest devel version.


---

Attachment


---

Attachment

Apply these to 3.2.1.alpha1:

```
sage-463.patch 
scripts-463-rebase-3.1.alpha1.patch 
scripts-463-rebase-3.2.1.alpha1-part2.patch 
```



---

Comment by mabshoff created at 2008-11-27 03:29:53

The three patches listed above look good to me. 

As William pointed out in IRC one can downgrade in which case a whole set of spkgs will be downloaded and then nothing is installed, but I am fine with that behavior. That might be fixed via some future ticket, but I don't think we should support downgrading. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 03:30:09

Merged in Sage 3.2.1.alpha2


---

Comment by mabshoff created at 2008-11-27 03:30:09

Resolution: fixed


---

Attachment


---

Attachment

Merged scripts-463-part3.patch and sage-463-part2.patch in Sage 3.2.1.alpah2


---

Comment by mabshoff created at 2008-11-27 06:29:20

And we merged on more fix: turn -br into -b

Cheers,

Michael
