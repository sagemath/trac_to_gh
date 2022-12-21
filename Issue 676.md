# Issue 676: Solaris 10: fix python build

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 00:44:11

Assignee: mabshoff

Keywords: Solaris 10, python

We need to add

```
 --with-libs='-lrt -laio -lmd -lmp -lscf -lgen -ldoor -lgcc_s -L/lib/ -luutil -ldl -lm -lsocket -lnsl -lxnet'
```

on Solaris 10 only. It is not needed on Solaris 9.


---

Comment by mabshoff created at 2007-09-17 05:50:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-17 15:28:03

The problem seems to be Solaris 10 on amd64 specific. See 

http://www.mail-archive.com/openpkg-cvs`@`openpkg.org/msg13989.html

for a workaround like:

```
if [ ".`isainfo -k`" = .amd64 ]; then
 ADD extra configure flags
fi
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 12:48:23

This problem also exists on Solaris 10/Sparc. It would be interesting to see if Python 2.5.2 fixes this problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-27 07:23:11

Resolution: wontfix


---

Comment by mabshoff created at 2008-04-27 07:23:11

This is a non-issue with the Sun Compiler. So close it as won't fix. 

Cheers,

Micahell
