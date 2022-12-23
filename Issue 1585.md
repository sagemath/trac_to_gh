# Issue 1585: fix file permissions in guava

Issue created by migration from https://trac.sagemath.org/ticket/1585

Original creator: rlm

Original creation time: 2007-12-22 01:26:31

Assignee: was


```
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava_light.jpg'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava.jpg'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava.ps'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/leon_guava_manual.pdf'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/README'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/manual.tex'? y
```



---

Comment by rlm created at 2007-12-22 01:27:44

also

```
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/libreadline.so.5.2'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/libhistory.so.5.2'? y
```



---

Comment by rlm created at 2007-12-22 20:42:35

I've fixed the files in guava


---

Comment by mabshoff created at 2008-01-13 19:10:54

After #1752 the permission issues with `libreadline` and `libhistory` are also gone:

```
sage-2.10.alpha3$ ls -al local/lib/libreadline.* local/lib/libhistory.*
-rwxr-xr-x 1 mabshoff 1090  157594 2008-01-11 12:20 local/lib/libhistory.a
lrwxrwxrwx 1 mabshoff 1090      15 2008-01-11 12:21 local/lib/libhistory.so -> libhistory.so.5
lrwxrwxrwx 1 mabshoff 1090      17 2008-01-11 12:21 local/lib/libhistory.so.5 -> libhistory.so.5.2
-rwxr-xr-x 1 mabshoff 1090   97893 2008-01-11 12:21 local/lib/libhistory.so.5.2
-rwxr-xr-x 1 mabshoff 1090 1084724 2008-01-11 12:20 local/lib/libreadline.a
lrwxrwxrwx 1 mabshoff 1090      16 2008-01-11 12:21 local/lib/libreadline.so -> libreadline.so.5
lrwxrwxrwx 1 mabshoff 1090      18 2008-01-11 12:21 local/lib/libreadline.so.5 -> libreadline.so.5.2
-rwxr-xr-x 1 mabshoff 1090  626992 2008-01-11 12:21 local/lib/libreadline.so.5.2
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-13 19:10:54

Resolution: fixed
