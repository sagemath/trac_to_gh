# Issue 1241: absolute symbolic links left in "make install"

Issue created by migration from https://trac.sagemath.org/ticket/1241

Original creator: zimmerma

Original creation time: 2007-11-22 12:15:36

Assignee: mabshoff

Another problem reported by Emmanuel Thome: the following symbolic links are absolute with respect to the
build directory of SAGE, thus won't work any more after "make install":

```
$ find sage-2.8.13/ | while read f ; do [ -h "$f" ] && [ ! \
-e "$f" ] && ls -l "$f" ; done
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzc\
mp -> /tmp/sage-2.8.13/spkg/../local/bin/bzdiff
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzf\
grep -> /tmp/sage-2.8.13/spkg/../local/bin/bzgrep
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzl\
ess -> /tmp/sage-2.8.13/spkg/../local/bin/bzmore
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bze\
grep -> /tmp/sage-2.8.13/spkg/../local/bin/bzgrep
```



---

Comment by mabshoff created at 2007-11-22 21:39:43

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-22 21:39:43

I will take care of those issues.

Cheers,

Michael


---

Comment by zimmerma created at 2007-12-17 12:28:05

This problem seems fixed in sage-2.9:

```
bash-3.2$ pwd
/usr/local/sage-2.9/sage/local/bin
bash-3.2$ ls -l bz*
-rwxr-xr-x 1 zimmerma spaces 131001 2007-12-17 11:25 bzcat
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzcmp -> bzdiff
-rwxr-xr-x 1 zimmerma spaces   2128 2007-12-17 11:25 bzdiff
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzegrep -> bzgrep
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzfgrep -> bzgrep
-rwxr-xr-x 1 zimmerma spaces   1677 2007-12-17 11:25 bzgrep
-rwxr-xr-x 1 zimmerma spaces 131001 2007-12-17 11:25 bzip2
-rwxr-xr-x 1 zimmerma spaces  14861 2007-12-17 11:25 bzip2recover
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzless -> bzmore
-rwxr-xr-x 1 zimmerma spaces   1259 2007-12-17 11:25 bzmore
```



---

Comment by mabshoff created at 2007-12-17 19:08:46

William verified that this issue was fixed by 2.9.final.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-17 19:08:46

Resolution: fixed


---

Comment by mabshoff created at 2007-12-17 19:30:45

Paul Zimmermann also confirmed that the issue has been solved.

Cheers,

Michael
