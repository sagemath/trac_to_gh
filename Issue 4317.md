# Issue 4317: relocation after make install is broken

Issue created by migration from https://trac.sagemath.org/ticket/4317

Original creator: zimmerma

Original creation time: 2008-10-18 15:22:07

Assignee: cwitty

To reproduce:

1) build sage from source, say in /tmp/sage-3.1.4

2) type make install DESTDIR=/usr/local/sage-3.1.4 (for example)

3) modify a file in /usr/local/sage-3.1.4, say integers.pyx (for example change the default base for digits)

4) run /usr/local/sage-3.1.4/bin/sage -br

5) try the modified function: the change has not been taken into account!

The fix is to rename /tmp/sage-3.1.4 into (say) /tmp/sage-3.1.4-old. It appears the relocation does
not work any more, or more precisely that sage first looks into the build directory if it still
exists.


---

Comment by mabshoff created at 2008-10-30 06:11:24


```
[11:04pm] mabshoff: craigcitro: so the problem happens when we deal with changed py files - not pyx?
[11:04pm] craigcitro: i haven't tested pyx
[11:04pm] mabshoff: ok
[11:04pm] craigcitro: got it.
[11:04pm] craigcitro: well, got halfway there, anyway
[11:04pm] mabshoff: Paul hits the same problem with pyx files, too.
[11:05pm] mabshoff: Excellent 
[11:05pm] craigcitro: there's a file called $SAGE_ROOT/local/lib/python-2.5/site-packages/easy-install.pth
[11:05pm] craigcitro: that file has your directory in it.
[11:05pm] craigcitro: kill the line with your directory, everything works.
[11:05pm] mabshoff: ah
[11:06pm] mabshoff: So that file needs to be updated when a moved Sage install is detected.
```



---

Comment by mabshoff created at 2008-10-30 06:16:12

Check out http://www.mail-archive.com/distutils-sig`@`python.org/msg05817.html

Also note that easy-install.pth is used in a bunch of places

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha2$ grep -r "easy-install.pth" *
install.log:Adding setuptools 0.6c8 to easy-install.pth file
install.log:Adding SQLAlchemy 0.4.6 to easy-install.pth file
install.log:Adding Jinja 1.2 to easy-install.pth file
install.log:Adding Pygments 0.11.1 to easy-install.pth file
install.log:Adding Sphinx 0.5dev-20081027 to easy-install.pth file
install.log:Adding docutils 0.5 to easy-install.pth file
install.log:Jinja 1.2 is already the active version in easy-install.pth
install.log:Pygments 0.11.1 is already the active version in easy-install.pth
```



---

Comment by mabshoff created at 2008-11-20 00:15:46

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-20 00:15:46

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-20 00:15:46

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2008-11-20 00:15:46

This really ought to get fixed for 3.2.1.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-12-01 08:51:36

Positive review. I fixed the spelling issue that Craig pointed out to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 08:52:59

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-12-01 08:52:59

Resolution: fixed
