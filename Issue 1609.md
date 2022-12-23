# Issue 1609: create an octave-3.0.0 optional spkg

Issue created by migration from https://trac.sagemath.org/ticket/1609

Original creator: was

Original creation time: 2007-12-27 05:41:22

Assignee: was




---

Comment by was created at 2007-12-27 05:41:26

Changing status from new to assigned.


---

Comment by was created at 2007-12-27 06:44:17

OK, I made a first attempt which I've posted here:

http://sage.math.washington.edu/home/was/build/octave-3.0.0.spkg

It builds for 70 minutes then dies with a mysterious C++ error:


```
m-sbm.o pic/op-b-sbm.o pic/op-cm-scm.o pic/op-cm-sm.o pic/op-cs-scm.o pic/op-cs-sm.o pic/op-m-scm.o pic/op-m-sm.o pic/op-s
bm-b.o pic/op-sbm-bm.o pic/op-sbm-sbm.o pic/op-scm-cm.o pic/op-scm-cs.o pic/op-scm-m.o pic/op-scm-s.o pic/op-scm-scm.o pic
/op-scm-sm.o pic/op-sm-cm.o pic/op-sm-cs.o pic/op-sm-m.o pic/op-sm-s.o pic/op-sm-scm.o pic/op-sm-sm.o pic/op-s-scm.o pic/o
p-s-sm.o pic/Array-os.o pic/Array-sym.o pic/Array-tc.o pic/oct-errno.o pic/builtins.o pic/ops.o ../libcruft/blas-xtra/pic/
xerbla.o -L../liboctave -loctave -L../libcruft -lcruft -lreadline  -lncurses -ldl -lz -lm  -L/home2/sage/build/sage-2.9/lo
cal/lib/ -L/home2/sage/build/sage-2.9/local/bin/../lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3/ -L/home2/sage/build/sage-2.
9/local/bin/../lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3 -L/home2/sage/build/sage-2.9/local/lib/../lib64 -L/home2/sage/bu
ild/sage-2.9/local/lib// -L/home2/sage/build/sage-2.9/local/lib -L/usr/lib/gcc// -L/lib/../lib64 -L/lib// -L/home2/sage/bu
ild/sage-2.9/local/bin/../lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3/// -L/usr/lib64/ -L/usr/lib64 -lz -lf95 -lm
rm -f liboctinterp.so.3.0.0
ln -s liboctinterp.so liboctinterp.so.3.0.0
gcc -c -I /home2/sage/build/sage-2.9/local/include/  -I. -I.. -I../liboctave -I../src -I../libcruft/misc  -DHAVE_CONFIG_H 
 -Wall -W -Wshadow -g -O2 main.c -o main.o
g++ -I /home2/sage/build/sage-2.9/local/include/  -I. -I.. -I../liboctave -I../src -I../libcruft/misc  -DHAVE_CONFIG_H  -W
all -W -Wshadow -Wold-style-cast -g -O2 -rdynamic \
        -L..  -fPIC -L /home2/sage/build/sage-2.9/local/lib/  -o octave \
        main.o  \   
        -L../liboctave -L../libcruft -L../src -Wl,-rpath -Wl,/home2/sage/build/sage-2.9/local/lib/octave-3.0.0 \
        -loctinterp -loctave  -lcruft   \
             \
           -llapack -lcblas -lf77blas -latlas \
         -lreadline  -lncurses -ldl -lz -lm  -L/home2/sage/build/sage-2.9/local/lib/ -L/home2/sage/build/sage-2.9/local/bi
n/../lib/gcc-lib/x86_64-unknown-linux-gnu/4.0.3/ -L/home2/sage/build/sage-2.9/local/bin/../lib/gcc-lib/x86_64-unknown-linu
x-gnu/4.0.3 -L/home2/sage/build/sage-2.9/local/lib/../lib64 -L/home2/sage/build/sage-2.9/local/lib// -L/home2/sage/build/s
age-2.9/local/lib -L/usr/lib/gcc// -L/lib/../lib64 -L/lib// -L/home2/sage/build/sage-2.9/local/bin/../lib/gcc-lib/x86_64-u
nknown-linux-gnu/4.0.3/// -L/usr/lib64/ -L/usr/lib64 -lz -lf95 -lm
/usr/lib/gcc/x86_64-linux-gnu/4.1.2/libstdc++.so: undefined reference to `_Unwind_GetIPInfo@GCC_4.2.0'
collect2: ld returned 1 exit status
make[2]: *** [octave] Error 1
make[2]: Leaving directory `/home2/sage/build/sage-2.9/spkg/build/octave-3.0.0/src/src'
make[1]: *** [src] Error 2
make[1]: Leaving directory `/home2/sage/build/sage-2.9/spkg/build/octave-3.0.0/src'
make: *** [all] Error 2
Error building octave.

real    70m21.139s  
user    40m31.256s  
sys     3m42.858s   
sage: An error occurred while installing octave-3.0.0

```



---

Comment by was created at 2007-12-27 06:44:30

I probably won't work on this further, so I hope somebody else will try.


---

Comment by was created at 2007-12-27 06:44:34

Changing status from assigned to new.


---

Comment by was created at 2007-12-27 07:15:38


```
> 
> Looking at the linker failure it indicates that you have a gcc 4.2
> somewhere (maybe installed into $SAGE_LOCAL via my gcc-4.2.1 spkg :))
> and the linker gets confused because it also links against a gcc 4.0.3
> runtime. If that is the case I can have a closer look. It seems that
> the build failed right at the end.

You're right; it's some sort of conflict like that though I don't think it's
gcc-4.2 versus gcc-4.0.3, but gcc-4.2.1 versus gcc 4.0.3 stuff that's
coming from the g95 binaries that we ship with Sage.   So probably
the way to build the Octave package would be to build Sage
using gfortran/gcc from your gcc-4.2.1.spkg, then build Octave. 
I don't know if there is a way around having to do that, which basically
means no optional Octave package.  

I don't think having an optional Octave package is critical since
it takes > 1 hour to build, and the Octave developers are extremely
good at making it easy to get Octave binaries for a wide range
of platforms. 

 -- William
```



---

Comment by magawake created at 2010-02-17 02:13:48

Changing keywords from "" to "octave".


---

Comment by magawake created at 2010-02-17 02:13:48

Not sure if this helps but I typically do:
./configure F77=gfortran

this seems to compile cleanly. 

If needed be, we can get the octave people involved. This is a nice and important package for many people.


---

Comment by drkirkby created at 2011-05-09 21:21:02

3.4.0 is the latest release, so there's not much point in trying to create a 3.0.0 package. 

Dave


---

Comment by drkirkby created at 2011-05-09 23:05:50

I thought I'd have a quick go at trying to make an Octave package, but I hit a problem pretty early on:


```
checking for sin in -lm... yes
checking whether we are using the GNU Fortran 77 compiler... yes
checking whether /export/home/drkirkby/sage-4.7.rc0/local/bin/sage_fortran accepts -g... yes
checking how to get verbose linking output from /export/home/drkirkby/sage-4.7.rc0/local/bin/sage_fortran... -v
checking for Fortran 77 libraries of /export/home/drkirkby/sage-4.7.rc0/local/bin/sage_fortran...  -L/usr/ccs/lib -L/usr/lib -L/export/home/drkirkby/sage-4.7.rc0/local/lib -L/usr/local/gcc-4.6.0/lib/gcc/i386-pc-solaris2.11/4.6.0 -L/usr/local/gcc-4.6.0/lib/gcc/i386-pc-solaris2.11/4.6.0/../../.. -lgfortran -lm -lquadmath
checking for dummy main to link with Fortran 77 libraries... unknown
configure: error: in `/export/home/drkirkby/sage-4.7.rc0/spkg/build/octave-3.4.0/src':
configure: error: linking to Fortran libraries from C fails
See `config.log' for more details
Error configuring GNU Octave

real	0m23.634s
user	0m9.304s
sys	0m8.385s
sage: An error occurred while installing octave-3.4.0
```


I don't know what BLAS library I'm supposed to configure this with. I have tried:


```
./configure --prefix="$SAGE_LOCAL" --with-glpk-includedir="$SAGE_LOCAL/include" --with-glpk-libdir="$SAGE_LOCAL/lib" --with-blas="SAGE_LOCAL/lib/libcblas.so" F77="$SAGE_FORTRAN"
```


but are unsure if the 'libcblas.so' is the right library. I tried another one (libblas.a), but had no luck with that either. If I omit the `--with-blas=` option, then it fails with:



```
configure: error: A BLAS library was detected but found incompatible with your Fortran 77 compiler settings.
```


I don't know how to get around this BLAS issue. 

I think it will need a bit of work to create this package. To get the best from Octave, you need a lot of libraries Sage does not include. It might be worth putting those libraries in an Octave package and building the libraries first. 

Dave


---

Comment by kcrisman created at 2011-06-28 16:02:58

Changing component from packages to optional packages.
