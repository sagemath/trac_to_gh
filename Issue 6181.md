# Issue 6181: The r-2.6.1.p22 spkg was created on OSX hence contains a bunch of crap

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-02 06:35:41

Assignee: mabshoff

If you extract r-2.6.1.p22.spkg on Linux with "tar jxvf" you'll see lots of stuff like this:


```
r-2.6.1.p22/src/src/library/grid/man/grid.layout.Rd
r-2.6.1.p22/src/src/library/grid/man/._grid.lines.Rd
r-2.6.1.p22/src/src/library/grid/man/grid.lines.Rd
r-2.6.1.p22/src/src/library/grid/man/._grid.locator.Rd
r-2.6.1.p22/src/src/library/grid/man/grid.locator.Rd
r-2.6.1.p22/src/src/library/grid/man/._grid.ls.Rd
r-2.6.1.p22/src/src/library/grid/man/grid.ls.Rd
```


These ._ files are all caused by making the tarball on OS X, and shouldn't be there. 


---

Comment by jason created at 2009-09-16 16:35:00

#6280 is a dup of this.


---

Comment by jason created at 2009-09-16 16:35:08

Changing status from new to assigned.


---

Comment by jason created at 2009-09-16 16:35:08

Changing assignee from mabshoff to jason.


---

Comment by mvngu created at 2009-10-01 05:51:40

Closing this as a duplicate of #6280.


---

Comment by mvngu created at 2009-10-01 05:51:40

Resolution: duplicate
