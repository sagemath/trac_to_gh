# Issue 1552: Fix gnuplot building on OS 10.5.1

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2007-12-17 14:57:32

Assignee: was

http://groups.google.com/group/sage-devel/browse_thread/thread/69b117b9d959f569?hl=en


---

Comment by mabshoff created at 2007-12-17 16:20:46

Well, there isn't much we can do to fix this since:

```
* Permission to modify the software is granted, but not the right to
* distribute the complete modified source code.  Modifications are to
* be distributed as patches to the released version.  Permission to
* distribute binaries produced by compiling modified sources is granted,
* provided you
*   1. distribute the corresponding source modifications from the
*    released version in the form of a patch file along with the binaries,
*   2. add special version identification to distinguish your version
*    in addition to the base release version number,
*   3. provide your name and address as the primary contact for the
*    support of your modified version, and
*   4. retain our contact information in regard to use of the base
*    software.
* Permission to distribute the released version of the source code along
* with corresponding source modifications in the form of a patch file is
* granted with same provisions 2 through 4 for binary distributions.
*
* This software is provided "as is" without express or implied warranty
* to the extent permitted by applicable law.
```

We could try updating to gnuplot 4.2.2. It has been discussed around here before that the name gnuplot is very misleading since this isn't a GNU project at all.

Cheers,

Michael


---

Comment by was created at 2008-02-17 22:28:23

Resolution: wontfix


---

Comment by was created at 2008-02-17 22:28:23

We won't fix this because of the lame gnuplot license.  Also Sage doesn't link in 
gnuplot in any binary way, so whatever standard system-wide way one might use to install gnuplot will work fine with sage if it works at all.
