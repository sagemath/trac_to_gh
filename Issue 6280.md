# Issue 6280: the R r-2.6.1.p22.spkg spkg is full of OS X crap ._ files

Issue created by migration from https://trac.sagemath.org/ticket/6280

Original creator: was

Original creation time: 2009-06-14 09:23:08

Assignee: mabshoff


```
tar jxvf r-2.6.1.p22.spkg
...
r-2.6.1.p22/src/tools/config.guess
r-2.6.1.p22/src/tools/._config.rpath
r-2.6.1.p22/src/tools/config.rpath
r-2.6.1.p22/src/tools/._config.sub
r-2.6.1.p22/src/tools/config.sub
r-2.6.1.p22/src/tools/._copy-if-change
r-2.6.1.p22/src/tools/copy-if-change
r-2.6.1.p22/src/tools/._GETCONFIG
r-2.6.1.p22/src/tools/GETCONFIG
r-2.6.1.p22/src/tools/._GETDISTNAME
r-2.6.1.p22/src/tools/GETDISTNAME
r-2.6.1.p22/src/tools/._GETMAKEVAL
r-2.6.1.p22/src/tools/GETMAKEVAL
r-2.6.1.p22/src/tools/._getsp.class
r-2.6.1.p22/src/tools/getsp.class
r-2.6.1.p22/src/tools/._getsp.java
r-2.6.1.p22/src/tools/getsp.java
r-2.6.1.p22/src/tools/._GETVERSION
r-2.6.1.p22/src/tools/GETVERSION
r-2.6.1.p22/src/tools/._help2man.pl
r-2.6.1.p22/src/tools/help2man.pl
r-2.6.1.p22/src/tools/._install-info.pl
r-2.6.1.p22/src/tools/install-info.pl
r-2.6.1.p22/src/tools/._install-sh
r-2.6.1.p22/src/tools/install-sh
r-2.6.1.p22/src/tools/._keywords2html.pl
r-2.6.1.p22/src/tools/keywords2html.pl
r-2.6.1.p22/src/tools/._ldAIX4
r-2.6.1.p22/src/tools/ldAIX4
r-2.6.1.p22/src/tools/._link-recommended
r-2.6.1.p22/src/tools/link-recommended
r-2.6.1.p22/src/tools/._linkcheck.pl
r-2.6.1.p22/src/tools/linkcheck.pl
r-2.6.1.p22/src/tools/._ltmain.sh
r-2.6.1.p22/src/tools/ltmain.sh
r-2.6.1.p22/src/tools/._Makefile.in
r-2.6.1.p22/src/tools/Makefile.in
r-2.6.1.p22/src/tools/._mdate-sh
r-2.6.1.p22/src/tools/mdate-sh
r-2.6.1.p22/src/tools/._missing
r-2.6.1.p22/src/tools/missing
r-2.6.1.p22/src/tools/._move-if-change
r-2.6.1.p22/src/tools/move-if-change
r-2.6.1.p22/src/tools/._pkg2tex.pl
r-2.6.1.p22/src/tools/pkg2tex.pl
r-2.6.1.p22/src/tools/._Rdnewer.pl
r-2.6.1.p22/src/tools/Rdnewer.pl
r-2.6.1.p22/src/tools/._README
r-2.6.1.p22/src/tools/README
r-2.6.1.p22/src/tools/._rsync-recommended
r-2.6.1.p22/src/tools/rsync-recommended
r-2.6.1.p22/src/tools/._updatefat
r-2.6.1.p22/src/tools/updatefat
r-2.6.1.p22/src/._VERSION
r-2.6.1.p22/src/VERSION
```


Notice all the ._'s.  These are the result of improperly building the spkg on an OS X box.   They all need to be deleted.


---

Comment by jason created at 2009-09-16 16:34:02

This is a dup of #6181.


---

Comment by jason created at 2009-09-16 16:35:15

Changing status from new to assigned.


---

Comment by jason created at 2009-09-16 16:35:15

Changing assignee from mabshoff to jason.


---

Comment by mvngu created at 2009-10-01 06:01:32

Closing this as wontfix. We have upgraded to R version 2.9.2 in Sage 4.1.2.alpha3. See ticket #6972.


---

Comment by mvngu created at 2009-10-01 06:01:32

Resolution: wontfix
