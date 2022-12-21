# Issue 5875: [with patch, needs review] Support tachyon on FreeBSD

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2009-04-23 08:50:16

Assignee: mabshoff

tachyon does include BSD support (though the code advises that it hasn't been tested for a while). Looking though the source code, there's no obvious bitrot so add FreeBSD support to the spkg-install script.

This patch does not include support for either threaded or 64-bit tachyon. The former shouldn't be too difficult to add and the MacOS-X port implies it is optional. The 64-bit support is solely an optimisation - a test to detect wrap-around of long integers is removed since wrap-around isn't possible with 64-bit longs.


---

Attachment


---

Comment by mhansen created at 2009-06-20 02:22:29

Looks good to me.

The spkg with the patch incorporated is at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p9.spkg


---

Comment by mhansen created at 2009-06-20 02:22:29

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-20 02:22:29

Changing assignee from mabshoff to mhansen.


---

Comment by rlm created at 2009-07-02 23:13:52

Resolution: fixed
