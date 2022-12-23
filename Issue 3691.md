# Issue 3691: Fix permission issues in $SAGE_LOCAL/bin repo

Issue created by migration from https://trac.sagemath.org/ticket/3691

Original creator: mabshoff

Original creation time: 2008-07-21 06:03:35

Assignee: mabshoff


```
cp: cannot open `/home/was/s/local/bin/sage-rebase_sage.sh' for reading: Permission denied
cp: cannot open `/home/was/s/local/bin/sage-server-web' for reading: Permission denied
cp: cannot open `/home/was/s/local/bin/phc' for reading: Permission denied
```



---

Comment by mabshoff created at 2008-07-21 08:00:46

Oops, as it turned out this is a specific issue with William's install:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -al sage-rebase_sage.sh 
-rwxr-xr-x 1 mabshoff 1090 424 2008-07-16 21:05 sage-rebase_sage.sh
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la sage-server-web
-rwxr-xr-x 1 mabshoff 1090 702 2008-07-21 00:56 sage-server-web
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la /home/was/s/local/bin/sage-rebase_sage.sh 
-rwx--x--x 1 was was 424 2008-05-05 06:51 /home/was/s/local/bin/sage-rebase_sage.sh
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la /home/was/s/local/bin/sage-server-web 
-rwx--x--x 1 was was 702 2008-07-16 16:21 /home/was/s/local/bin/sage-server-web
```

On a fresh install is not an issue. It seems likely that some stupidity in hg caused this.

Ergo: wontfix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 08:00:46

Resolution: wontfix
