# Issue 6933: readline-5.2.p7 builds as 32-bit on Solaris even if SAGE64=yes

Issue created by migration from https://trac.sagemath.org/ticket/6933

Original creator: drkirkby

Original creation time: 2009-09-15 09:27:56

Assignee: tbd

The title pretty much says it all. The spkg-install is ignoring SAGE64 unless the OS is Darwin (OS X). 

it currently has:


```

if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "Building 64 bit OSX version of Sage"
   CFLAGS="-O2 -g -m64 " && export CFLAGS
   LDFLAGS="-m64"
fi

```




---

Comment by mvngu created at 2009-09-17 22:13:32

Fixed by #6945.


---

Comment by mvngu created at 2009-09-17 22:13:32

Resolution: duplicate
