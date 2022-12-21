# Issue 5488: optional polymake package fails to build on OS X

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-11 17:45:15

Assignee: mabshoff

Using sage-3.4.rc0 on bsd.math (a standard OSX 10.5 intel-based mac), the optional polymake spkg totally fails to build:


```
g++   -I/Users/was/build/sage-3.4.rc0/local/lib  -I/Users/was/build/sage-3.4.rc0/local/lib  -o cdd_ch_float_client cdd_ch_float_client.o libpolytope.a ../../lib/libpoly.a  -lgmp 
ld: duplicate symbol _dd_free_global_constants in libpolytope.a(cdd_interface.o) and libpolytope.a(cdd_float_interface.o)

collect2: ld returned 1 exit status
make[3]: *** [cdd_ch_float_client] Error 1
make[2]: *** [do_all] Error 2
make[1]: *** [all] Error 2
make: *** [all] Error 2
Failed to configure.

real    2m40.027s
user    1m54.830s
sys     0m13.814s
sage: An error occurred while installing polymake-2.2.p5
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/was/build/sage-3.4.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/was/build/sage-3.4.rc0/spkg/build/polymake-2.2.p5 and type 'make'.
Instead type "/Users/was/build/sage-3.4.rc0/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/was/build/sage-3.4.rc0/spkg/build/polymake-2.2.p5
(When you are done debugging, you can type "exit" to leave the
subshell.)
was`@`bsd:~/build/sage-3.4.rc0$ 
```




---

Comment by kcrisman created at 2011-06-28 16:08:06

Changing component from packages to optional packages.


---

Comment by benjaminfjones created at 2012-05-26 04:25:12

Hmm... still fails to build inside sage-5.0 on Mac OS X all the way out here in the year 2012. I'm looking into producing a new spkg.


---

Comment by benjaminfjones created at 2012-05-26 04:25:12

Changing keywords from "" to "sd40.5".


---

Comment by benjaminfjones created at 2012-05-26 04:56:39

After futzing around with the spkg-install script, it seems that polymake depends on the system installation of perl. It doesn't build on Mac OS X because it can't find `Config.h` from the system perl installation.


---

Comment by benjaminfjones created at 2012-05-26 05:01:38

... more notes to myself ... the polymake Makefile complains:

```
can't locate perl's config.h: suspicious perl installation problem?
```

Do we need a development version of perl or perl sources installed to build polymake?


---

Comment by benjaminfjones created at 2012-05-26 05:40:58

On a system where `config.h` can be found, polymake still fails to build:

```
jonesbe`@`sage:~/sage/sage-5.0$ ./sage -f tmp/polymake-2.2.p6.spkg Calling sage-spkg on 'tmp/polymake-2.2.p6.spkg'polymake-2.2.p6====================================================Extracting package /home/jonesbe/sage/sage-5.0/tmp/polymake-2.2.p6.spkg-rw-r--r-- 1 jonesbe jonesbe 1502253 May 26 00:30 /home/jonesbe/sage/sage-5.0/tmp/polymake-2.2.p6.spkg
Finished extraction
****************************************************
Host system:
Linux sage 2.6.32 #1 SMP Fri Sep 2 21:08:57 CDT 2011 x86_64 GNU/Linux
****************************************************C compiler: gcc
C compiler version:
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.6/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Debian 4.6.3-1' --with-bugurl=file:///usr/share/doc/gcc-4.6/README.Bugs --enable-languages=c,c++,fortran,objc,obj-c++,go --prefix=/usr --program-suffix=-4.6 --enable-shared --enable-linker-build-id --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.6 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-plugin --enable-objc-gc --with-arch-32=i586 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnuThread model: posixgcc version 4.6.3 (Debian 4.6.3-1) ****************************************************Using gmp-5.0.4 to build polymakeUsing cddlib-094f.p11 to build polymakeChecking if your kit is complete...
Looks good
Writing Makefile for Poly::Ext
Writing MYMETA.yml
make[1]: Entering directory `/home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src/build/perlx-5.14.2-x86_64-linux-gnu-thread-multi'
/usr/bin/perl /usr/share/perl/5.14/ExtUtils/xsubpp  -typemap /usr/share/perl/5.14/ExtUtils/typemap  Ext.xs > Ext.xsc && mv Ext.xsc Ext.c
cc -c   -D_REENTRANT -D_GNU_SOURCE -DDEBIAN -fstack-protector -fno-strict-aliasing -pipe -I/usr/local/include -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -g   -DVERSION=\"\" -DXS_VERSION=\"\" -fPIC "-I/usr/lib/perl/5.14/CORE"   Ext.c
Ext.xs: In function ‘dump_me’:
Ext.xs:64:92: error: ‘XPVHV’ has no member named ‘xhv_name’
Ext.xs:67:134: error: ‘XPVAV’ has no member named ‘xav_flags’
make[1]: *** [Ext.o] Error 1
make[1]: Leaving directory `/home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src/build/perlx-5.14.2-x86_64-linux-gnu-thread-multi'
[ -d /home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src/build/perlx-5.14.2-x86_64-linux-gnu-thread-multi ] || perl /home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src/support/install.pl -d -m 755 /home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src/build/perlx-5.14.2-x86_64-linux-gnu-thread-multi
cd /home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src/build/perlx-5.14.2-x86_64-linux-gnu-thread-multi; TOP=/home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src perl /home/jonesbe/sage/sage-5.0/spkg/build/polymake-2.2.p6/src/perl/ext/Makefile.PL
cc -c   -D_REENTRANT -D_GNU_SOURCE -DDEBIAN -fstack-protector -fno-strict-aliasing -pipe -I/usr/local/include -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -g   -DVERSION=\"\" -DXS_VERSION=\"\" -fPIC "-I/usr/lib/perl/5.14/CORE"   Ext.c
Ext.xs: In function ‘dump_me’:
Ext.xs:64:92: error: ‘XPVHV’ has no member named ‘xhv_name’
Ext.xs:67:134: error: ‘XPVAV’ has no member named ‘xav_flags’
make[2]: *** [Ext.o] Error 1
make[1]: *** [all-perlx] Error 2
make: *** [all] Error 2
Failed to configure.
```


 Here is the (still broken) spkg in case anyone feels like diagnosing the build problem: http://sage.math.washington.edu/home/bjones/polymake-2.2.p6.spkg


---

Comment by vbraun created at 2012-05-28 14:36:59

I've packaged the current polymake 2.12 here:

http://www.stp.dias.ie/~vbraun/Sage/spkg/polymake-2.12.p0.spkg

It doesn't compile because it requires more than just our cropped boost. You can't even use the system boost install (on Fedora 16) because it conflicts with our boost version. See also https://groups.google.com/d/topic/sage-devel/s5FftN1hPB0/discussion


---

Comment by kcrisman created at 2013-02-14 02:05:26

See #13768 for something related. It relies on #13767 (additional boost headers).


---

Comment by kcrisman created at 2014-11-20 14:17:39

Volker, can you put your spkg up on a working link?  http://sage.math.washington.edu/home/vbraun/spkg/ seems appropriate.  Unfortunately the spkg link at #13768 also isn't working :( so it would be quite hard to test #14116.

(If you though it was appropriate, one could close this as a dup of #13768, but in principle these could also remain separate.)


---

Comment by kcrisman created at 2014-11-20 20:12:59

I'm going to ask to close this, because I was able to use #14116 to compile on Mac.  Now, to be fair, [the polymake doc](http://polymake.org/doku.php/howto/mac_compiling_nofink) [doesn't quite](http://polymake.org/doku.php/howto/mac) [support OS X 10.5](http://polymake.org/doku.php/download/start) but anyway I think we are in good shape with something, if I could get it to compile and work (via library interface only) on 10.7, which is not their top priority.


---

Comment by kcrisman created at 2014-11-20 20:12:59

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-11-20 20:13:06

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-11-20 20:22:58

New spkg link for the record: ​http://sage.math.washington.edu/home/vbraun/spkg/polymake-2.12.p0.spkg


---

Comment by vbraun created at 2014-11-28 18:38:31

Resolution: fixed
