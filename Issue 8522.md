# Issue 8522: Optional package  libcocoa openmpi-1.1.4 fails to install on Solaris 10 SPARC

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-13 14:35:25

Assignee: tbd

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.3.4.alpha1
 * Patch #8509 removing the -o option to grep to allow packages to install. 

 == The problem with the optional openmpi-1.1.4 ==

First it should be noted this is an old version of OpenMPI, so it would be worth trying an upgrade first. But the version in Sage fails with:


```
 g++ -DHAVE_CONFIG_H -I. -I. -I../../../opal/include -I../../../orte/include -I../../../ompi/include -I../../../ompi/include -I../../.. -D_REENTRANT -O3 -DNDEBUG -finline-functions -MT comm.lo -MD -MP -MF .deps/comm.Tpo -c comm.cc  -fPIC -DPIC -o .libs/comm.o
In file included from ../../../ompi/mpi/cxx/mpicxx.h:150,
                 from ../../../ompi/include/mpi.h:1760,
                 from comm.cc:21:
../../../ompi/mpi/cxx/request_inln.h: In static member function 'static MPI::Grequest MPI::Grequest::Start(int (*)(void*, MPI::Status&), int (*)(void*), int (*)(void*, bool), void*)':
../../../ompi/mpi/cxx/request_inln.h:347: warning: declaration 'struct MPI::Grequest_intercept_t' does not declare anything
/bin/bash ../../../libtool --tag=CXX --mode=link g++  -O3 -DNDEBUG -finline-functions   -export-dynamic   -o libmpi_cxx.la -rpath /export/home/drkirkby/sage-4.3.4.alpha1/local/lib  mpicxx.lo intercepts.lo comm.lo  -lsocket -lnsl  -lrt -lm -lthread
g++ -shared -nostdlib -export-dynamic   /usr/local/gcc-4.4.3/lib/gcc/sparc-sun-solaris2.10/4.4.3/crti.o /usr/ccs/lib/values-Xa.o /usr/local/gcc-4.4.3/lib/gcc/sparc-sun-solaris2.10/4.4.3/crtbegin.o  .libs/mpicxx.o .libs/intercepts.o .libs/comm.o  -Wl,-R -Wl,/usr/local/gcc-4.4.3/lib -Wl,-R -Wl,/usr/local/gcc-4.4.3/lib -lsocket -lnsl -lrt -lthread -L/export/home/drkirkby/sage-4.3.4.alpha1/local/lib -L/usr/local/gcc-4.4.3/lib/gcc/sparc-sun-solaris2.10/4.4.3 -L/usr/ccs/lib -L/usr/local/gcc-4.4.3/lib/gcc/sparc-sun-solaris2.10/4.4.3/../../.. /usr/local/gcc-4.4.3/lib/libstdc++.so -lm -lgcc_s /usr/local/gcc-4.4.3/lib/gcc/sparc-sun-solaris2.10/4.4.3/crtend.o /usr/local/gcc-4.4.3/lib/gcc/sparc-sun-solaris2.10/4.4.3/crtn.o  -Wl,-h -Wl,libmpi_cxx.so.0 -o .libs/libmpi_cxx.so.0.0.0
ld: fatal: entry point symbol `xport-dynamic' is undefined
collect2: ld returned 1 exit status
make[3]: *** [libmpi_cxx.la] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/spkg/build/openmpi-1.1.4/ompi/mpi/cxx'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/spkg/build/openmpi-1.1.4/ompi/mpi'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/spkg/build/openmpi-1.1.4/ompi'
make: *** [all-recursive] Error 1
Error building

real    21m31.771s
user    11m52.285s
sys     10m38.154s
sage: An error occurred while installing openmpi-1.1.4
```



---

Comment by maldun created at 2011-01-08 23:10:24

Does the package I posted on #8537 work?


---

Comment by vbraun created at 2011-01-12 02:39:18

Not fixed by #8537, but at least it now dies at a different location

```
make[2]: Entering directory `/home/vbraun/mark/sage-4.6.1.alpha2/spkg/build/openmpi-1.4.3/src/opal/tools/wrappers'
depbase=`echo opal_wrapper.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`;\
        gcc "-DEXEEXT=\"\"" -I. -I../../../opal/include -I../../../orte/include -I../../../ompi/include -I../../../opal/mca/paffinity/linux/plpa/src/libplpa   -I../../..  -D_REENTRANT  -O3 -DNDEBUG -finline-functions -fno-strict-aliasing  -fvisibility=hidden -MT opal_wrapper.o -MD -MP -MF $depbase.Tpo -c -o opal_wrapper.o opal_wrapper.c &&\
        mv -f $depbase.Tpo $depbase.Po
/bin/bash ../../../libtool --tag=CC   --mode=link gcc  -O3 -DNDEBUG -finline-functions -fno-strict-aliasing  -fvisibility=hidden  -export-dynamic   -o opal_wrapper opal_wrapper.o ../../../opal/libopen-pal.la -lsocket -lnsl  -lrt -lm -lthread
libtool: link: gcc -O3 -DNDEBUG -finline-functions -fno-strict-aliasing -fvisibility=hidden -o .libs/opal_wrapper opal_wrapper.o  ../../../opal/.libs/libopen-pal.so -lsocket -lnsl -lrt -lm -lthread -R/home/vbraun/mark/sage-4.6.1.alpha2/local/lib
opal_wrapper.o: In function `main':
opal_wrapper.c:(.text+0xb0c): undefined reference to `opal_basename'
opal_wrapper.c:(.text+0x1700): undefined reference to `opal_few'
../../../opal/.libs/libopen-pal.so: undefined reference to `mca_base_select'
../../../opal/.libs/libopen-pal.so: undefined reference to `mca_base_component_list_item_t_class'
../../../opal/.libs/libopen-pal.so: undefined reference to `lt_dlexit'
../../../opal/.libs/libopen-pal.so: undefined reference to `lt_dlclose'
../../../opal/.libs/libopen-pal.so: undefined reference to `mca_base_components_close'
../../../opal/.libs/libopen-pal.so: undefined reference to `mca_base_components_open'
../../../opal/.libs/libopen-pal.so: undefined reference to `lt_dlinit'
collect2: ld returned 1 exit status
make[2]: *** [opal_wrapper] Error 1
make[2]: Leaving directory `/home/vbraun/mark/sage-4.6.1.alpha2/spkg/build/openmpi-1.4.3/src/opal/tools/wrappers'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/vbraun/mark/sage-4.6.1.alpha2/spkg/build/openmpi-1.4.3/src/opal'
make: *** [all-recursive] Error 1
Error building
```

Tested on mark/skynet.


---

Comment by vbraun created at 2011-01-12 02:39:18

Changing status from new to needs_work.


---

Comment by maldun created at 2011-01-12 22:29:00

Replying to [comment:3 vbraun]:
> Not fixed by #8537, but at least it now dies at a different location
>...
> Tested on mark/skynet.

What happens if the options in the old spkg-install are reactivated?


---

Comment by drkirkby created at 2011-03-03 00:39:00

This fails on OpenSolaris x86 too - I created a separate ticket for that. See #10866 

The error message is different. 

Dave


---

Comment by drkirkby created at 2011-03-03 12:09:44

Resolution: wontfix


---

Comment by drkirkby created at 2011-03-03 12:09:44

Since much of this is against an old version of OpenMPI, I've closed this and opened a new ticket for the current issues #10869 seen on Solaris 10 SPARC.
