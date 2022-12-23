# Issue 1883: Sage distribution includes Windows executables

Issue created by migration from https://trac.sagemath.org/ticket/1883

Original creator: cwitty

Original creation time: 2008-01-22 01:45:25

Assignee: mabshoff

My Sage installation includes 5 Windows executables: 

```
./local/lib/gap-4.4.10/bin/gapw95.exe
./local/lib/gap-4.4.10/bin/regtool.exe
./local/lib/gap-4.4.10/bin/._regtool.exe
./local/lib/gap-4.4.10/bin/rxvt.exe
./local/lib/gap-4.4.10/bin/._rxvt.exe
./local/lib/gap-4.4.10/bin/._gapw95.exe
./local/lib/python2.5/distutils/command/wininst-6.exe
./local/lib/python2.5/distutils/command/wininst-7.1.exe
```

(as well as three Macintosh resource forks for the corresponding Windows executable -- those files are doubly useless).

These files should be deleted from the corresponding spkgs.


---

Comment by mabshoff created at 2008-01-22 03:21:01

The updated gap spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/gap-4.4.10.p1.spkg

removes the executables, a number of DLLs and about 1500 other files created by OSX, i.e. `._*`. As a result it shrunk from 8.4mb to 7.0mb

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 05:54:17

The python spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/python-2.5.1.p13.spkg

removes the two executables mentioned above.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 05:54:55

Both spkgs merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-22 05:54:55

Resolution: fixed
