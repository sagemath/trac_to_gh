# Issue 7337: PolyBoRi fails to build on cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-28 19:37:45

Assignee: tbd

CC:  was

It fails with 


```
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:70: undefined reference to `_png_get_error_ptr'
  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngReadData':
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:85: undefined reference to `_png_get_io_ptr'
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:87: undefined reference to `_png_error'
  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngWriteData':
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:94: undefined reference to `_png_get_io_ptr'
  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdImageCreateFromPngCtx':
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:152: undefined reference to `_png_check_sig'
```


This can be fixed by adding png12 and z to the list of libraries needed when gd is present.

I'll post an spkg shortly.



---

Comment by mhansen created at 2010-02-17 08:12:09

This no longer fails with Cygwin 1.7.


---

Comment by mhansen created at 2010-02-17 08:12:09

Resolution: invalid


---

Comment by mhansen created at 2010-05-26 20:20:36

Resolution changed from invalid to 


---

Comment by mhansen created at 2010-05-26 20:20:36

Changing status from closed to new.


---

Comment by mhansen created at 2010-05-26 20:20:36

So, it turns out this is still an issue.


---

Comment by mhansen created at 2010-05-26 20:29:08

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-05-26 20:29:08

There's an spkg which should fix this at http://sage.math.washington.edu/home/mhansen/polybori-0.6.4.p1.spkg


---

Comment by was created at 2010-05-26 23:08:12

looks good


---

Comment by was created at 2010-05-26 23:08:12

Resolution: fixed
