# Issue 8980: gac script hardcodes build path

Issue created by migration from Trac.

Original creator: wjlaffin

Original creation time: 2010-05-17 00:50:06

Assignee: tbd


```
wjlaffin`@`dellbees$ pwd
/sage/local/lib/gap-4.4.12/bin/x86_64-unknown-linux-gnu-gcc
wjlaffin`@`dellbees$ grep build -n gac
54:gap_bin=/sage/spkg/build/gap-4.4.12.p3/src/bin/x86_64-unknown-linux-gnu-gcc
```


Changing the bin path to the path given by pwd fixes the problem. Needs a robust fix.


---

Comment by jdemeyer created at 2017-09-22 13:49:11

Resolution: invalid


---

Comment by jdemeyer created at 2017-09-22 13:49:11

Obsolete
