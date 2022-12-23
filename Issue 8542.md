# Issue 8542: Pynac does not build a DLL on Cygwin

Issue created by migration from https://trac.sagemath.org/ticket/8542

Original creator: mhansen

Original creation time: 2010-03-15 05:27:50

Assignee: tbd

However, if I go into src/ginac/.libs and run


```
gcc -shared -L/home/mhansen/sage-4.3.3.alpha0/local//lib -L/home/mhansen/sage-4.3.3.alpha0/local/lib/python2.6/config -o libpynac.dll *.o -lstdc++ -lpython2.6
```


a working DLL gets built.  The trick would be to figure out how to get autotools to do this for us.


---

Comment by mhansen created at 2010-03-15 08:16:52

It basically comes down to adding the following changes


```
diff -r 1cf1634d68b0 configure.ac
--- a/configure.ac	Sun Mar 14 20:20:48 2010 -0800
+++ b/configure.ac	Mon Mar 15 00:15:49 2010 -0800
@@ -71,6 +71,7 @@
 AC_PROG_CXXCPP
 AC_PROG_INSTALL
 AM_PROG_LIBTOOL
+AC_LIBTOOL_WIN32_DLL
 
 dnl Check for data types which are needed by the hash function 
 dnl (golden_ratio_hash).
diff -r 1cf1634d68b0 ginac/Makefile.am
--- a/ginac/Makefile.am	Sun Mar 14 20:20:48 2010 -0800
+++ b/ginac/Makefile.am	Mon Mar 15 00:15:49 2010 -0800
@@ -10,7 +10,7 @@
   pseries.cpp print.cpp symbol.cpp symmetry.cpp tensor.cpp \
   utils.cpp wildcard.cpp \
   remember.h tostring.h utils.h compiler.h
-libpynac_la_LDFLAGS = -version-info $(LT_VERSION_INFO) -release $(LT_RELEASE)
+libpynac_la_LDFLAGS = -version-info $(LT_VERSION_INFO) -release $(LT_RELEASE) -no-undefined
 ginacincludedir = $(includedir)/pynac
 ginacinclude_HEADERS = ginac.h add.h archive.h assertion.h basic.h class_info.h \
   clifford.h color.h constant.h container.h ex.h expair.h expairseq.h \
```


and fixing the fallout by making sure that Python gets linked in.


---

Comment by burcin created at 2010-04-02 14:59:06

Shall I include the diff above in the next Pynac release?

I could have done this for the version I just released (#8644) if I had known earlier...


---

Comment by mhansen created at 2010-04-02 19:12:46

No, not quite yet.  Basically, we'll also have the stuff to autotools to detect where Python is, etc.


---

Attachment


---

Comment by mhansen created at 2010-05-03 13:33:54

I'll post the spkg shortly.


---

Comment by mhansen created at 2010-05-04 23:32:13

There's an spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.13.spkg, but it needs to have changes committed / SPKG.txt made / version number updated.


---

Comment by burcin created at 2010-05-05 02:16:38

Replying to [comment:6 mhansen]:
> There's an spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.13.spkg, but it needs to have changes committed / SPKG.txt made / version number updated.

I'll take a look at these and merge #8651 as well.


---

Comment by burcin created at 2010-05-05 15:56:17

Changing assignee from tbd to burcin.


---

Comment by burcin created at 2010-05-05 15:56:17

Changing keywords from "" to "pynac".


---

Comment by burcin created at 2010-05-05 15:56:17

Both patches, for pynac and Sage, look good to me.

Building the new pynac package fails with the following error:


```
...
/usr/lib/gcc/x86_64-pc-linux-gnu/4.3.4/../../../../x86_64-pc-linux-gnu/bin/ld: /home/burcin/sage/sage-4.4.1.alpha2-patched/local/lib/python2.6/config/libpython2.6.a(abstract.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
/home/burcin/sage/sage-4.4.1.alpha2-patched/local/lib/python2.6/config/libpython2.6.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
make[2]: *** [libpynac.la] Error 1
make[2]: Leaving directory `/home/burcin/sage/sage-4.4.1.alpha2-patched/spkg/build/pynac-0.1.13/src/ginac'
...
```


Do we have a python package that uses `-fPIC`?


---

Comment by mhansen created at 2010-05-05 16:03:49

Does this work for you http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg ?


---

Comment by burcin created at 2010-05-05 18:15:52

It works! I'll put your changes on the latest spkg included in sage (including the patch for #8753), merge some other fixes (#8651, maybe #8775), bump the version to 2.0 and make a new package.


---

Comment by mhansen created at 2010-05-05 18:21:19

I'll test the Python spkg on other systems.


---

Comment by burcin created at 2010-05-06 04:14:37

New pynac package containing Mike's function table and autoconf patches is available at #8903 or directly from:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg

The package also requires patches from #8651, #8775 and #8688.


---

Comment by burcin created at 2010-05-06 04:14:37

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-06 04:15:40

Great work Mike! Cygwin, here we come!


---

Comment by burcin created at 2010-05-06 04:15:40

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-28 19:31:10

Resolution: fixed
