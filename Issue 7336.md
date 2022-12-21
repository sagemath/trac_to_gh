# Issue 7336: boehm_gc fails to build on Cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-28 19:36:07

Assignee: tbd

CC:  was

It fails with 

```
  /bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o libcord.la -rpath /home/mhansen/sage-4.2/local/lib -version-info 1:3:0 -no-undefined cord/cordbscs.lo cord/cordprnt.lo cord/cordtest.lo cord/cordxtra.lo ./libgc.la 

  *** Warning: This system can not link to static lib archive ./libgc.la.
  *** I have the capability to make that library automatically link in when
  *** you link to this library.  But I can only do this if you have a
  *** shared version of the library, which you do not appear to have.
  rm -fr  .libs/libcord.dll.a
  gcc -shared  cord/.libs/cordbscs.o cord/.libs/cordprnt.o cord/.libs/cordtest.o cord/.libs/cordxtra.o   -o .libs/cygcord-1.dll -Wl,--enable-auto-image-base -Xlinker --out-implib -Xlinker .libs/libcord.dll.a
  Creating library file: .libs/libcord.dll.a
  cord/.libs/cordbscs.o: In function `CORD_from_fn':
  /home/mhansen/sage-4.2/spkg/build/boehm_gc-7.1.p2/src/cord/cordbscs.c:288: undefined reference to `_GC_malloc_atomic'
  /home/mhansen/sage-4.2/spkg/build/boehm_gc-7.1.p2/src/cord/cordbscs.c:298: undefined reference to `_GC_malloc'
  cord/.libs/cordbscs.o: In function `CORD_substr_closure':
  /home/mhansen/sage-4.2/spkg/build/boehm_gc-7.1.p2/src/cord/cordbscs.c:344: undefined reference to `_GC_malloc'
```


This can be fixed by setting THREADDLLIBS to be empty.

I'll post an updated spkg here shortly.


---

Comment by mhansen created at 2009-11-06 05:30:43

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-06 05:30:43

The spkg with the above change (active only when $UNAME = "CYGWIN") can be found at http://sage.math.washington.edu/home/mhansen/boehm_gc-7.1.p3.spkg .


---

Comment by was created at 2010-02-07 05:57:47

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-02-07 05:57:47

Mike, I was trying to referee this, but the spkg is missing.  Did you delete it?  Can you repost it somewhere?


---

Comment by mhansen created at 2010-02-07 06:01:04

It should be up now.


---

Comment by mhansen created at 2010-02-07 06:01:20

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-02-15 05:29:27

An updated spkg is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/boehm/boehm_gc-7.1.p4.spkg

This includes Mike's changes at http://sage.math.washington.edu/home/mhansen/boehm_gc-7.1.p3.spkg, but based on the `boehm_gc` spkg in Sage 4.3.3.alpha0.


---

Comment by mvngu created at 2010-02-16 04:56:58

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-16 04:56:58

I rebased Mike's spkg, reviewed it, built it on Cygwin (winxp1 on boxen.math). The build went fine.


---

Comment by mvngu created at 2010-02-16 04:57:35

Resolution: fixed


---

Comment by mvngu created at 2010-02-16 04:57:35

Merged in the standard spkg repository.


---

Comment by was created at 2010-05-27 02:57:48

I just tried this spkg on cygwin and it fails:


```

deps/cordxtra.Tpo -c cord/cordxtra.c -o cord/cordxtra.o >/dev/null 2>&1

/bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o libcord.la -rpath /home/wstein/sage-4.4.3.alpha0/local/lib -version-info !1:3:0 -no-undefined cord/cordbscs.lo cord/cordprnt.lo cord/cordtest.lo cord/cordxtra.lo ./libgc.la 

*** Warning: This system can not link to static lib archive ./libgc.la.

*** I have the capability to make that library automatically link in when

*** you link to this library.  But I can only do this if you have a

*** shared version of the library, which you do not appear to have.

gcc -shared  cord/.libs/cordbscs.o cord/.libs/cordprnt.o cord/.libs/cordtest.o cord/.libs/cordxtra.o   -o .libs/cygcord-1.dll -Wl,--enable-auto-image-base -Xlinker --out-implib -Xlinker .libs/libcord.dll.a

Creating library file: .libs/libcord.dll.acord/.libs/cordbscs.o: In function `CORD_from_fn':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:288: undefined reference to `_GC_malloc_atomic'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:298: undefined reference to `_GC_malloc'

cord/.libs/cordbscs.o: In function `CORD_substr_closure':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:344: undefined reference to `_GC_malloc'

cord/.libs/cordbscs.o: In function `CORD_cat_char_star':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:214: undefined reference to `_GC_malloc'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:159: undefined reference to `_GC_malloc_atomic'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:190: undefined reference to `_GC_malloc_atomic'

cord/.libs/cordbscs.o: In function `CORD_cat':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:255: undefined reference to `_GC_malloc'

cord/.libs/cordbscs.o: In function `CORD_substr_checked':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:367: undefined reference to `_GC_malloc_atomic'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordbscs.c:438: undefined reference to `_GC_malloc_atomic'

cord/.libs/cordprnt.o: In function `CORD_vsprintf':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordprnt.c:276: undefined reference to `_GC_malloc_atomic'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordprnt.c:220: undefined reference to `_GC_malloc_atomic'

cord/.libs/cordtest.o: In function `main':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordtest.c:229: undefined reference to `_GC_add_roots'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordtest.c:229: undefined reference to `_GC_gcollect'

cord/.libs/cordxtra.o: In function `CORD_from_file_lazy_inner':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:565: undefined reference to `_GC_malloc'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:585: undefined reference to `_GC_register_finalizer'

cord/.libs/cordxtra.o: In function `CORD_lf_func':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:547: undefined reference to `_GC_malloc_atomic'

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:549: undefined reference to `_GC_call_with_alloc_lock'

cord/.libs/cordxtra.o: In function `CORD_ec_flush_buf':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:416: undefined reference to `_GC_malloc_atomic'

cord/.libs/cordxtra.o: In function `CORD_cat_char':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:63: undefined reference to `_GC_malloc_atomic'

cord/.libs/cordxtra.o: In function `CORD_from_char_star':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:241: undefined reference to `_GC_malloc_atomic'

cord/.libs/cordxtra.o: In function `CORD_to_char_star':

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src/cord/!cordxtra.c:227: undefined reference to `_GC_malloc_atomic'

collect2: ld returned 1 exit status

make![1]: *** [libcord.la] Error 1

make![1]: Leaving directory `/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4/src'

make: *** [all-recursive] Error 1

Error building BoehmGC.

real    23m11.613s

user    4m16.141s

sys     14m45.815s

sage: An error occurred while installing boehm_gc-7.1.p4

Please email sage-devel !http://groups.google.com/group/sage-devel

explaining the problem and send the relevant part of

of /home/wstein/sage-4.4.3.alpha0/install.log.  Describe your computer, operating system, etc.

If you want to try to fix the problem yourself, *don't* just cd to

/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4 and type 'make check' or whatever is appropriate.

Instead, the following commands setup all environment variables

correctly and load a subshell for you to debug the error:

(cd '/home/wstein/sage-4.4.3.alpha0/spkg/build/boehm_gc-7.1.p4' && '/home/wstein/sage-4.4.3.alpha0/sage' -sh)

When you are done debugging, you can type "exit" to leave the

subshell.

```



---

Comment by mhansen created at 2010-05-27 07:00:21

I think there was a typo in the spkg that Minh made.  There is an spkg at http://sage.math.washington.edu/home/mhansen/boehm_gc-7.1.p5.spkg that should work.  Testing now on winxp1.
