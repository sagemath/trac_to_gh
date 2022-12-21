# Issue 2334: $SAGE_LOCAL/include/eclib has wrong permissions

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-27 19:08:17

Assignee: mabshoff


```
drwx------ 2 malb georgesk 4.0K 2008-01-29 14:33 eclib
^^^^^^^^^^^
```



---

Comment by mabshoff created at 2008-03-09 06:56:41

It boils down to a stupid thinko in spkg-install:

```
diff -r 06dc1250f0ad spkg-install
--- a/spkg-install      Sat Feb 09 12:45:02 2008 -0800
+++ b/spkg-install      Sat Mar 08 22:49:06 2008 -0800
`@``@` -88,5 +88,5 `@``@` strip "$SAGE_LOCAL"/bin/tconic"$EXE_NAME
 strip "$SAGE_LOCAL"/bin/tconic"$EXE_NAME"

 cd "$SAGE_LOCAL"/include
-chown 755 eclib
+chmod 755 eclib
 chmod 644 eclib/*
```


The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc3/eclib-20080127.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-09 06:56:41

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-09 07:07:08

With the new spkg I get:

```
sage-2.10.3.rc3$ ls -ald local/include/eclib/
drwxr-xr-x 2 mabshoff 1090 4096 2008-03-08 22:59 local/include/eclib/
```


Cheers,

Michael


---

Comment by gfurnish created at 2008-03-09 07:40:26

Positive review


---

Comment by mabshoff created at 2008-03-09 07:40:55

Merged in Sage 2.10.3.rc3


---

Comment by mabshoff created at 2008-03-09 07:40:55

Resolution: fixed
