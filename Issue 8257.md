# Issue 8257: cygwin: gd-2.0.35.p4 fails to build

Issue created by migration from https://trac.sagemath.org/ticket/8257

Original creator: was

Original creation time: 2010-02-13 20:04:09

Assignee: tbd

The gd-2.0.35.p4 spkg fails to build on cygwin.


---

Comment by was created at 2010-02-13 20:05:12

The errors are:

```
...
gcc -shared  .libs/gd.o .libs/gdfx.o .libs/gd_security.o .libs/gd_gd.o .libs/gd_gd2.o .libs/gd_io.o .libs/gd_io_dp.o .libs/gd_gif_in.o .libs/gd_gif_out.o .libs/gd_io_file.o .libs/gd_io_ss.o .libs/gd_jpeg.o .libs/gd_png.o .libs/gd_ss.o .libs/gd_topal.o .libs/gd_wbmp.o .libs/gdcache.o .libs/gdfontg.o .libs/gdfontl.o .libs/gdfontmb.o .libs/gdfonts.o .libs/gdfontt.o .libs/gdft.o .libs/gdhelpers.o .libs/gdkanji.o .libs/gdtables.o .libs/gdxpm.o .libs/wbmp.o  -L/home/wstein/build/sage-4.3.3.alpha0/local/lib /usr/lib/libiconv.dll.a /home/wstein/build/sage-4.3.3.alpha0/local/lib/libfreetype.dll.a -lz  -o .libs/cyggd-2.dll -Wl,--enable-auto-image-base -Xlinker --out-implib -Xlinker .libs/libgd.dll.a 
Creating library file: .libs/libgd.dll.a                                                                                   
.libs/gd_png.o: In function `gdPngErrorHandler':                                                                           
/home/wstein/build/sage-4.3.3.alpha0/spkg/build/gd-2.0.35.p4/src/gd_png.c:70: undefined reference to `_png_get_error_ptr'  
.libs/gd_png.o: In function `gdPngReadData':                                                                               
/home/wstein/build/sage-4.3.3.alpha0/spkg/build/gd-2.0.35.p4/src/gd_png.c:85: undefined reference to `_png_get_io_ptr'     
/home/wstein/build/sage-4.3.3.alpha0/spkg/build/gd-2.0.35.p4/src/gd_png.c:87: undefined reference to `_png_error'          
.libs/gd_png.o: In function `gdPngWriteData':   
```


Putting -lpng12  in the build line makes the line complete without errors.  So that's a hint.


---

Comment by was created at 2010-02-13 20:29:11

Upgrading to gd-2.0.36rc1 didn't help.


---

Comment by mhansen created at 2010-04-06 17:39:41

I believe the failure is caused by a bad version of expr.  I'm attaching a  wrapper script that needs to be put in `$SAGE_LOCAL/bin`.  I'm not sure where the best place to put this script is. In the gd spkg?  In something like base?


---

Attachment


---

Comment by mhansen created at 2010-04-27 04:20:23

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-04-27 04:20:23

I've put an spkg up at http://sage.math.washington.edu/home/mhansen/cygwin_port/gd-2.0.35.p5.spkg


---

Comment by was created at 2010-05-26 00:29:33

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-26 00:55:24

Resolution: fixed
