# Issue 1240: wrong unix rights of some files

Issue created by migration from https://trac.sagemath.org/ticket/1240

Original creator: zimmerma

Original creation time: 2007-11-22 12:12:52

Assignee: mabshoff

[This was reported to me by Emmanuel Thome.]

When installing SAGE 2.8.13 on a multi-user site (make dist), the Unix rights of some files are wrong:

```
helene% find . ! -perm +004 | xargs ls -lLd
-rwx--x--x 1 zimmerma spaces    414 2007-11-22 08:56 ./local/bin/sage-rebase_sage.sh
-rwx--x--x 1 zimmerma spaces    702 2007-11-22 10:13 ./local/bin/sage-server-web
-rw------- 1 zimmerma spaces   5292 2007-11-22 09:09 ./local/include/cremona/cperiods.h
...
-rw-r----- 1 zimmerma spaces   1360 2006-10-26 20:26 ./local/share/moin/underlay/pages/SystemPagesSetup/attachments/all_languages.zip
...
```


Shouldn't all files be at least readable (r) by everybody?


---

Comment by mabshoff created at 2007-11-22 21:39:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-22 21:39:28

I will take care of those.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 11:03:16

Ok, I have fixed 

```
local/bin/sage-rebase_sage.sh
local/bin/sage-server-web
local/include/cremona/cperiods.h
```

and I will take care of the moin moin issue in 2.8.15.

Cheers,

Michael


---

Comment by zimmerma created at 2007-12-17 12:30:20

The moin issue is still there in 2.9 (28 files are concerned).


---

Comment by mabshoff created at 2007-12-19 10:48:57

The moinmoin issues are fixed in 

http://sage.math.washington.edu/home/mabshoff/moin-1.5.7.p2.spkg

Cheers,

Michael


---

Comment by rlm created at 2007-12-19 19:11:41

Resolution: fixed


---

Comment by rlm created at 2007-12-19 19:11:41

Merged in 2.9.1 alpha2


---

Comment by zimmerma created at 2010-03-04 13:54:01

Resolution changed from fixed to 


---

Comment by zimmerma created at 2010-03-04 13:54:01

Changing priority from major to blocker.


---

Comment by zimmerma created at 2010-03-04 13:54:01

Changing status from closed to new.


---

Comment by zimmerma created at 2010-03-04 13:54:01

I reopen this ticket, since this issue is back with Sage 4.3.3:

```
tarte% sage
**************************************************************************
You must compile Sage first using 'make' in the Sage root directory.
(If you have already compiled Sage, you must set the SAGE_ROOT variable in 
the file '/usr/local/sage-core2/sage').
**************************************************************************
```

This is due to wrong permissions (Sage was installed by Emmanuel Thome with `make dist`):

```
tiramisu ~ $ ls -l /usr/local/sage-core2/
total 29884
-rw-r--r--  2 thome caramel    71842 Mar  1 14:43 COPYING.txt
-rw-r--r--  2 thome caramel    11123 Mar  1 14:43 README.txt
drwxr-xr-x  8 thome caramel     4096 Mar  1 16:42 data
drwxr-xr-x  4 thome caramel     4096 Mar  1 15:58 devel
drwx------ 15 thome caramel     4096 Mar  3 22:01 examples
-rw-r--r--  1 thome caramel 30427884 Mar  1 17:04 install.log
drwx------  2 thome caramel     4096 Mar  3 22:01 ipython
drwx------ 12 thome caramel     4096 Mar  3 21:46 local
-rw-r--r--  2 thome caramel     2618 Feb 11 17:55 makefile
-rwxr-xr-x  2 thome caramel     1449 Feb 11 17:56 sage
-rw-r--r--  2 thome caramel     1622 Mar  1 14:43 sage-README-osx.txt
-rwxr-xr-x  2 thome caramel       38 Mar  1 14:43 sage-python
drwx------  6 thome caramel     4096 Mar  3 22:07 spkg
drwx------  2 thome caramel     4096 Mar  3 22:07 tmp
```

I declare this as a blocker since this issue should be fixed *once for all*
(and automatically checked before doing a release).


---

Comment by zimmerma created at 2010-03-04 13:55:54

Changing assignee from mabshoff to mvngu.


---

Comment by mvngu created at 2010-03-04 16:43:32

Resolution: fixed


---

Comment by mvngu created at 2010-03-04 16:43:32

Please do not reopen tickets that are already closed. Open another ticket for the specific issue related to this ticket and concerning Sage 4.3.3. Then reference this ticket from the newly opened ticket. The issue of the current ticket concerns Sage 2.9.1 and it has already been fixed for that release.


---

Comment by mvngu created at 2010-03-04 16:43:32

Changing priority from blocker to major.


---

Comment by zimmerma created at 2010-03-04 19:13:49

> Please do not reopen tickets that are already closed. Open another ticket ...

ok, see #8437.
