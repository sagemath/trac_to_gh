# Issue 9989: Pari fails to build on AIX - using wrong extension for libraries.

Issue created by migration from https://trac.sagemath.org/ticket/9990

Original creator: drkirkby

Original creation time: 2010-09-23 22:25:56

Assignee: drkirkby

CC:  jdemeyer

The Pari svn snapshot 12577 is failing to build properly on AIX. *If the Pari developers would like access to AIX hardware (I don't think they have it), then I can provide access to my personal RS/6000*

 == Hardware and software ==
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1 with Pari  svn snapshot 12577, with some fixes applied in Sage. 

 == The Problem ==
A full build log is attached, but the main problem seems to be that Pari is using the conventional `.so` for the extension of shared libraries, whereas on AIX, IBM use `.a` for shared libraries. 

```
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -I. -I../src/headers -fPIC -o thue.o ../src/modules/thue.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -I. -I../src/headers -I../src/graph -o gp_init.o ../src/gp/gp_init.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -I. -I../src/headers -DDL_DFLT_NAME=NULL -o highlvl.o ../src/gp/highlvl.c
rm -f libpari-gmp-2.4.so.3.0.0
gcc  -o "/home/users/drkirkby/sage-4.6.alpha1/spkg/build/pari-2.4.3.svn-12577.p5/src/Oaix-ppc"/libpari-gmp-2.4.so.3.0.0 -shared  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -fP
IC -Wl,-r  mp.o mpinl.o F2x.o FF.o Flx.o FpE.o FpV.o FpX.o Qfb.o RgV.o RgX.o ZV.o ZX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bb_group.o bibli1.o bibli2.o
bit.o buch1.o buch2.o buch3.o buch4.o concat.o ellanal.o elliptic.o galconj.o gen1.o gen2.o gen3.o hnf_snf.o ifactor1.o lll.o perm.o polarit1.o polarit2.o polarit3.o prime.o random.o rootpol.o s
ubcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o compile.o default.o errmsg.o es.o eval.o hash.o init.o intnum.o members.o pariinl.o parse.o sumiter.o DedekZeta.o Hensel.o QX_fact
or.o aprcl.o elldata.o ellsea.o galois.o galpol.o groupid.o krasner.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o  -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -lgmp
if test "libpari-gmp-2.4.so.3.0.0" != "libpari.so"; then          rm -f libpari.so;       ln -s libpari-gmp-2.4.so.3.0.0 libpari.so; fi
if test "libpari-gmp-2.4.so.3.0.0" != "libpari-gmp-2.4.so.3"; then        rm -f libpari-gmp-2.4.so.3;     ln -s libpari-gmp-2.4.so.3.0.0 libpari-gmp-2.4.so.3; fi
rm -f gp-dyn
gcc  -o gp-dyn -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -Wl,-brtl  gp.o gp_init.o gp_rl.o highlvl.o whatnow.o plotport.o plotnull.o  -L"/home/users/drkirkby/sage-4.6.alpha1/
spkg/build/pari-2.4.3.svn-12577.p5/src/Oaix-ppc" -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -lreadline -L/home/users/drkirkby/sage-4.6.alpha1/local/lib/ -ltermcap -L"/home/users/drkirkby/s
age-4.6.alpha1/local/lib" -lpari  -lm
ld: 0711-434 SEVERE ERROR: Shared object /home/users/drkirkby/sage-4.6.alpha1/spkg/build/pari-2.4.3.svn-12577.p5/src/Oaix-ppc/libpari.so
        The shared object has no .loader section and is being ignored.
collect2: ld returned 12 exit status
make[3]: *** [gp-dyn] Error 1
make[3]: Target `gp' not remade because of errors.
make[3]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/pari-2.4.3.svn-12577.p5/src/Oaix-ppc'
make[2]: *** [gp] Error 2
make[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/pari-2.4.3.svn-12577.p5/src'
Error building GP

```



---

Comment by leif created at 2010-09-24 12:24:41

The extension `.so` doesn't seem to be the problem, since apparently the loader recognizes it as a shared library.

The extension `.a` for _shared_ libraries is of course a bit odd since PARI also builds a static version which typically has the same name ending with `.a`...


---

Comment by drkirkby created at 2010-09-24 12:56:29

Replying to [comment:1 leif]:
> The extension `.so` doesn't seem to be the problem, since apparently the loader recognizes it as a shared library.
> 
> The extension `.a` for _shared_ libraries is of course a bit odd since PARI also builds a static version which typically has the same name ending with `.a`...

I wonder what the logic is for having both shared and static? I'd rather use the right extension on the right platform. I can discuss this with the Pari developers after getting clarification from some AIX experts on comp.unix.aix - they are a *very* helpful bunch.


---

Comment by leif created at 2010-09-24 13:28:19

Replying to [comment:2 drkirkby]:
> I wonder what the logic is for having both shared and static?

For an executable that doesn't make that much sense, but `gp-sta`[tic] is tested against `gp-dyn`[amic], which isn't bad.

And since PARI is (also) a library, it's pretty normal to build both. (Every proper library does this, at least if you `--enable-shared` and `--enable-static`, depending on what the defaults are.)


---

Comment by drkirkby created at 2010-09-26 13:55:20

I've reported this upstream:


```
Bug#1102: Acknowledgement (Build failure on AIX 5.3 - shared object has no .loader section)
```


The bug reported included a log against the latest snapshot, which shows the same problem. 

Dave


---

Comment by drkirkby created at 2010-09-28 22:52:14

I got this from Bill Allombert, a Pari developer:


```
Could you try to deactivate shared libraries by using
./Configure --static
```


That solves the problem - Pari then installs ok. I will create a patch. 

Dave


---

Comment by jdemeyer created at 2010-09-29 08:05:46

Replying to [comment:7 drkirkby]:
> I got this from Bill Allombert, a Pari developer:
> 
> {{{
> Could you try to deactivate shared libraries by using
> ./Configure --static
> }}}
> 
> That solves the problem - Pari then installs ok.

Did you only try to compile PARI/GP stand-alone, or also within Sage?  Because I don't know whether it is possible to compile Sage statically.


---

Comment by jdemeyer created at 2010-09-29 08:11:13

Replying to [comment:7 drkirkby]:
> I will create a patch. 

If you do create a new pari spkg, please base it on the one at #9959: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg)


---

Comment by drkirkby created at 2010-09-29 08:40:54

Replying to [comment:8 jdemeyer]:
> Replying to [comment:7 drkirkby]:
> > I got this from Bill Allombert, a Pari developer:
> > 
> > {{{
> > Could you try to deactivate shared libraries by using
> > ./Configure --static
> > }}}
> > 
> > That solves the problem - Pari then installs ok.
> 
> Did you only try to compile PARI/GP stand-alone, or also within Sage?  Because I don't know whether it is possible to compile Sage statically.

Only outside of Sage at this point. Some of the ATLAS libraries are only stati, but Sage links to them ok. Since Sage will not build fully on AIX, it's hard to know for sure what problems might present themselves at a later date, but I doubt a static Pari library would be one of them. 

I later found out that it appears that on AIX the .a files are archives which can contain both static and shared objects. But using .so as an extension for shared objects is not a problem in itself.


---

Comment by drkirkby created at 2010-09-29 14:48:37

Replying to [comment:9 jdemeyer]:
> Replying to [comment:7 drkirkby]:
> > I will create a patch. 
> 
> If you do create a new pari spkg, please base it on the one at #9959: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg)

No problem. This should be a very low-risk patch, as it will be specific to AIX. But I have some other more important things to do now, so it will have to wait. 

Dave


---

Comment by jdemeyer created at 2012-06-01 21:54:48

"No feedback yet." is totally not correct here.  Most applicable would be "Developers sort-of acknowledge the bug but don't really care enough to fix it"


---

Comment by fbissey created at 2012-06-02 10:52:24

I believe "-Wl,-r" is incorrect, "-Wl,-brtl" may have to be added for the linking to happen, as in the linking of binary.


---

Comment by fbissey created at 2012-06-02 11:33:09

And with a little bit of fiddling in Oaix-ppc/Makefile

```
frb15@p1n14-c /hpc/scratch/frb15/work/pari-2.5.1 :nano -w Oaix-ppc/Makefile 
frb15@p1n14-c /hpc/scratch/frb15/work/pari-2.5.1 :gmake gp
Making gp in Oaix-ppc
gmake[1]: Entering directory `/hpc/scratch/frb15/work/pari-2.5.1/Oaix-ppc'
rm -f libpari-gmp.so.2.5.1
gcc  -o "/hpc/scratch/frb15/work/pari-2.5.1/Oaix-ppc"/libpari-gmp.so.2.5.1 -shared  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -fPIC -Wl,-brtl mp.o mpinl.o F2x.o FF.o Flx.o FpE.o FpV.o FpX.o Hensel.o QX_factor.o Qfb.o RgV.o RgX.o ZV.o ZX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bb_group.o bibli1.o bibli2.o bit.o buch1.o buch2.o buch3.o buch4.o concat.o ellanal.o elliptic.o galconj.o gen1.o gen2.o gen3.o hnf_snf.o ifactor1.o lll.o nffactor.o perm.o polarit1.o polarit2.o polarit3.o prime.o random.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o compile.o default.o errmsg.o es.o eval.o hash.o init.o intnum.o members.o paricfg.o pariinl.o parse.o sumiter.o DedekZeta.o aprcl.o elldata.o ellsea.o galois.o galpol.o groupid.o krasner.o kummer.o mpqs.o part.o stark.o subfield.o thue.o  -L/usr/local/lib -lgmp -lm 
if test "libpari-gmp.so.2.5.1" != "libpari.so"; then      rm -f libpari.so;       ln -s libpari-gmp.so.2.5.1 libpari.so; fi
if test "libpari-gmp.so.2.5.1" != "libpari-gmp.so.3"; then        rm -f libpari-gmp.so.3;         ln -s libpari-gmp.so.2.5.1 libpari-gmp.so.3; fi
rm -f gp-dyn
gcc  -o gp-dyn -L"/hpc/scratch/frb15/work/pari-2.5.1/Oaix-ppc" -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -Wl,-brtl  gp.o gp_init.o gp_rl.o highlvl.o whatnow.o plotX.o plotport.o -Wl,-blibpath:"/hpc/scratch/frb15/work/pari-2.5.1"/Oaix-ppc:"/usr/local/lib":/usr/lib:/usr/local/lib:/usr/local/pkg/readline/6.2_p1/lib32 -L/usr/local/pkg/readline/6.2_p1/lib32 -lreadline -L/usr/lib/ -lncurses -lpari -L/usr/lib -lX11   -lm 
ld: 0711-224 WARNING: Duplicate symbol: .bcopy
ld: 0711-345 Use the -bloadmap or -bnoquiet option to obtain more information.
rm -f ../gp
ln -s Oaix-ppc/gp-dyn ../gp
gmake[1]: Leaving directory `/hpc/scratch/frb15/work/pari-2.5.1/Oaix-ppc'
```

The warning is about the fact that bcopy is in both libreadline and libc. Probably because I have both libreadline.a and .so at the moment and .a would have chosen over .so. That's minor compared to some other stuff like the fact that it segfault:

```
/hpc/scratch/frb15/work/pari-2.5.1 :./gp
  ***   bug in PARI/GP (Segmentation Fault), please report
### Errors on startup, exiting...
```

For info that's on a power7 machine running aix-6.1(TL6) with gcc-4.6.3 [compiled on another LPAR on the same machine running TL7].


---

Comment by jdemeyer created at 2018-10-17 13:04:30

Closing as obsolete.


---

Comment by jdemeyer created at 2018-10-17 13:04:30

Resolution: wontfix
