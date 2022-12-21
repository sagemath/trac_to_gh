# Issue 5218: Update Pyhton to 2.5.4

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-09 12:31:43

Assignee: mabshoff

Python 2.5.4 fixes a couple of security problems in Python 2.5.2. So let's update to it since the difference to 2.5.2 are minimal.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 12:31:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-16 05:04:01

An spkg is coming up :), but I needed to correct the spelling problem in the meantime.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 06:05:21

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/python-2.5.4.spkg

switches to Python 2.5.4. Note that no changes were made aside from 

 * rebasing the ctypes/__init__.py patch
 * update SPKG.txt, especially with patch information
 * rename two patches to be consistent with SPKG guidelines

Cheers,

Michael


---

Comment by mhampton created at 2009-02-16 11:31:41

I have not extensively tested this, but Michael says he has, and I have installed it and done some limited tests.  Seems to be fine.


---

Comment by mabshoff created at 2009-02-16 11:34:06

Resolution: fixed


---

Comment by mabshoff created at 2009-02-16 11:34:06

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 15:59:47

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-02-16 15:59:47

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-02-16 15:59:47

Unfortunately this introduced an unpleasant side effect since -sdist now does not include the hg repo in the sage-x.y.z.spkg. I know too little about distutils to deal with this in 3.3.rc1, so I am reverting the spkg until we fix the bug in setup.py.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 06:11:39

Bumped to 3.4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-27 23:10:34

Better luck in Sage 3.4.1.

Cheers,

Michael


---

Comment by mhansen created at 2009-05-28 20:25:26

A new spkg which fixes the sdist issue is at http://sage.math.washington.edu/home/mhansen/python-2.5.4.p0.spkg


---

Comment by was created at 2009-05-28 22:07:12

Note:
The patch that fixes this sdist issue is:

```
wstein`@`sage:~/tmp/python-2.5.4.p0$ diff src/Lib/distutils/command/sdist.py patches/sdist.py
350c350
<           * any RCS, CVS, .svn, .hg, .git, .bzr, _darcs directories
---
>           * any RCS, CVS, .svn, .git, .bzr, _darcs directories
357c357
<         self.filelist.exclude_pattern(r'(^|/)(RCS|CVS|\.svn|\.hg|\.git|\.bzr|_darcs)/.*', is_regex=1)
---
>         self.filelist.exclude_pattern(r'(^|/)(RCS|CVS|\.svn|\.git|\.bzr|_darcs)/.*', is_regex=1)
```


I'm concerned since I bet this problem will just come back later again when we upgrade to some newer python, since it seems that it is the intention of the python devs to make it impossible to include repo's in sdists.  Thus, in the long run, we may have to fix this by (1) doing sdist, then (2) extract the sdist tar ball and manually copying over the hg repo, then (3) remaking the sdist tar ball.    We already extract and remake the tar ball to go from .tar.gz to .tar.bz2 format, so this isn't so bad. 

So, positive review, but with a "just for the record" caveat.


---

Comment by mhansen created at 2009-05-29 04:25:28

I made http://sage.math.washington.edu/home/mhansen/python-2.5.4.p1.spkg which includes the fix done in sage-2.5.2.p9.spkg.


---

Comment by was created at 2009-05-29 13:36:46

This looks suspicous:

```
wstein`@`sage:~/tmp/python-2.5.4.p1$ hg status
? patches/posixmodule.c.patch.rej
```


Otherwise this looks perfect.  

http://sage.math.washington.edu/home/wstein/tmp/python-2.5.4.p1.spkg

is the spkg but with that rej file deleted.


---

Comment by kedlaya created at 2009-05-29 13:47:51

This also seems to fix some problems I was having in 64-bit Fedora 10: segmentation faults when trying to use tab completion, and mysterious "out of memory" errors. (I tried it against 4.0.rc1.)


---

Comment by mhansen created at 2009-05-29 17:33:57

Merged http://sage.math.washington.edu/home/wstein/tmp/python-2.5.4.p1.spkg in 4.0.rc2.


---

Comment by mhansen created at 2009-05-29 17:34:02

Resolution: fixed
