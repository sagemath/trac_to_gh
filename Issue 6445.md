# Issue 6445: pari 2.3.3.p0 problem on 't2' but not my home machine (similar setups!!)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-06-29 16:27:37

Assignee: tbd

Keywords: solaris pari

Well, is is a bit of an odd one. 

I built gcc 4.4.0 to use the Sun linker & assembler on my home machine (Sun Blade 2000, Solaris 10 update 6) and it built 61 packages without issue (see list at the bottom).

On 't2', I only get 6 built



```
dir-0.1
prereq-0.3
bzip2-1.0.5
sage_scripts-4.1.alpha2
conway_polynomials-0.2
mpir-1.2.p4
termcap-1.3.1.p0
readline-5.2.p6
```


Before pari is generating more than 94,000 error messages! 



```
Building and install PARI
make[2]: Entering directory `/tmp/tmp/sage-4.1.alpha2/spkg/build/pari-2.3.3.p0/src'
Making gp in Osolaris-none
make[3]: Entering directory `/tmp/tmp/sage-4.1.alpha2/spkg/build/pari-2.3.3.p0/src/Osolaris-none'
../config/genkernel ../src/kernel/none/asm0.h > parilvl0.h
cat ../src/kernel/gmp/tune.h ../src/kernel/gmp/int.h ../src/kernel/none/level1.h > parilvl1.h
cat parilvl0.h parilvl1.h > pariinl.h
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/language -I/tmp/tmp/sage-4.1.alpha2/local/include -o gp.o ../src/gp/gp.c
cd ../src/desc && /usr/bin/perl merge_822 ../functions/*/* > def-solaris-none-20099.tmp
mv ../src/desc/def-solaris-none-20099.tmp ../src/desc/pari.desc
cd ../src/desc && /usr/bin/perl gen_proto gp pari.desc > gp_init-solaris-none-20099.tmp
mv ../src/desc/gp_init-solaris-none-20099.tmp ../src/gp/gp_init.h
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/graph -o gp_init.o ../src/gp/gp_init.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/language -I/tmp/tmp/sage-4.1.alpha2/local/include -o gp_rl.o ../src/gp/gp_rl.c
cd ../src/desc && /usr/bin/perl gen_proto highlevel pari.desc > highlvl-solaris-none-20099.tmp
mv ../src/desc/highlvl-solaris-none-20099.tmp ../src/gp/highlvl.h
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -DDL_DFLT_NAME=NULL -o highlvl.o ../src/gp/highlvl.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -o whatnow.o ../src/gp/whatnow.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/graph -o plotport.o ../src/graph/plotport.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o plotnull.o ../src/graph/plotnull.c
cat ../src/kernel/gmp/mp.c ../src/kernel/none/cmp.c ../src/kernel/none/gcdll.c ../src/kernel/none/ratlift.c ../src/kernel/none/invmod.c ../src/kernel/gmp/gcd.c ../src/kernel/none/mp_indep.c ../src/kernel/none/add.c > mp.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer     -I. -I../src/headers -I/tmp/tmp/sage-4.1.alpha2/local/include -o mp.o mp.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o mpinl.o ../src/kernel/none/mpinl.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o Flx.o ../src/basemath/Flx.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o Qfb.o ../src/basemath/Qfb.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o RgX.o ../src/basemath/RgX.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o alglin1.o ../src/basemath/alglin1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o alglin2.o ../src/basemath/alglin2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o arith1.o ../src/basemath/arith1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o arith2.o ../src/basemath/arith2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base1.o ../src/basemath/base1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base2.o ../src/basemath/base2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base3.o ../src/basemath/base3.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base4.o ../src/basemath/base4.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base5.o ../src/basemath/base5.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o bibli1.o ../src/basemath/bibli1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o bibli2.o ../src/basemath/bibli2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o buch1.o ../src/basemath/buch1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o buch2.o ../src/basemath/buch2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o buch3.o ../src/basemath/buch3.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o buch4.o ../src/basemath/buch4.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o galconj.o ../src/basemath/galconj.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o gen1.o ../src/basemath/gen1.cgcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o gen2.o ../src/basemath/gen2.cgcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o gen3.o ../src/basemath/gen3.cgcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o ifactor1.o ../src/basemath/ifactor1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o perm.o ../src/basemath/perm.cgcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o polarit1.o ../src/basemath/polarit1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o polarit2.o ../src/basemath/polarit2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o polarit3.o ../src/basemath/polarit3.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o rootpol.o ../src/basemath/rootpol.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o subcyclo.o ../src/basemath/subcyclo.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o subgroup.o ../src/basemath/subgroup.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o trans1.o ../src/basemath/trans1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o trans2.o ../src/basemath/trans2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o trans3.o ../src/basemath/trans3.c
cd ../src/desc && /usr/bin/perl gen_member pari.desc > members-solaris-none-20099.tmp
mv ../src/desc/members-solaris-none-20099.tmp ../src/language/members.h
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o anal.o ../src/language/anal.cgcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o compat.o ../src/language/compat.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o default.o ../src/language/default.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o errmsg.o ../src/language/errmsg.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o es.o ../src/language/es.c
cd ../src/desc && /usr/bin/perl gen_proto basic pari.desc > init-solaris-none-20099.tmp
mv ../src/desc/init-solaris-none-20099.tmp ../src/language/init.h
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o init.o ../src/language/init.cgcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o intnum.o ../src/language/intnum.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o members.o ../src/language/members.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o sumiter.o ../src/language/sumiter.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o aprcl.o ../src/modules/aprcl.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o elldata.o ../src/modules/elldata.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o elliptic.o ../src/modules/elliptic.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o galois.o ../src/modules/galois.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o groupid.o ../src/modules/groupid.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o kummer.o ../src/modules/kummer.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o mpqs.o ../src/modules/mpqs.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o nffactor.o ../src/modules/nffactor.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o part.o ../src/modules/part.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o stark.o ../src/modules/stark.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o subfield.o ../src/modules/subfield.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o thue.o ../src/modules/thue.c
rm -f libpari-gmp.so.2.3.3
gcc  -o libpari-gmp.so.2.3.3 -shared  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer     -Wl,-G,-h,libpari-gmp.so.2 mp.o mpinl.o Flx.o Qfb.o RgX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.o bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifactor1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o -lc -lm -L/tmp/tmp/sage-4.1.alpha2/local/lib -lgmp
Text relocation remains                         referenced
    against symbol                  offset      in file
<unknown>                           0x76c       alglin2.o
<unknown>                           0x770       alglin2.o
<unknown>                           0x774       alglin2.o

<SNIP out over 94,000 errors>

__gmpn_mul_1                        0xdea0      mp.o
__gmpn_mul_1                        0xdf24      mp.o
__gmpn_mul_1                        0xdfa8      mp.o
__gmpn_mul_1                        0xe02c      mp.o
__gmpn_mul_1                        0xfa84      mp.o
__gmpn_mul_1                        0xfb14      mp.o
__gmpn_mul_1                        0xfd28      mp.o
__gmpn_mul_1                        0xfdac      mp.o
__gmpn_mul_1                        0xfe2c      mp.o
__gmpn_mul_1                        0xfea8      mp.o
__gmpn_mul_1                        0xff20      mp.o
__gmpn_mul_1                        0xff98      mp.o
__gmpn_rshift                       0x48f4      mp.o
__gmpn_rshift                       0xe710      mp.o
__gmpn_rshift                       0xec7c      mp.o
__gmpn_gcd                          0x9b2c      mp.o
__gmpn_gcdext                       0xbd90      mp.o
__gmpn_gcdext                       0xcef4      mp.o
__gmpn_add_n                        0xb888      mp.o
__gmpn_sub_n                        0xb3d8      mp.o
__gmpn_mod_1                        0x21dc      mp.o
__gmpn_mod_1                        0x9640      mp.o
__gmpn_mod_1                        0xe220      mp.o
ld: fatal: relocations remain against allocatable but non-writable sections
collect2: ld returned 1 exit status
make[3]: *** [libpari-gmp.so.2.3.3] Error 1
make[3]: Leaving directory `/tmp/tmp/sage-4.1.alpha2/spkg/build/pari-2.3.3.p0/src/Osolaris-none'
make[2]: *** [gp] Error 2
make[2]: Leaving directory `/tmp/tmp/sage-4.1.alpha2/spkg/build/pari-2.3.3.p0/src'
Error building GP
```


Just for the record, on my home machine, which uses a later version of Solaris 10, but identical versions of Sage and gcc, I got this many packages installed before problems. 

Anyway, this is an issue which appears to be unique to t2, so will not to be resolved. 


```
dir-0.1
prereq-0.3
bzip2-1.0.5
sage_scripts-4.1.alpha2
conway_polynomials-0.2
mpir-1.2.p4
termcap-1.3.1.p0
readline-5.2.p6
pari-2.3.3.p0
ntl-5.4.2.p8
eclib-20080310.p7
graphs-20070722
elliptic_curves-0.1
extcode-4.1.alpha2
flint-1.3.0.p1
zlib-1.2.3.p4
sqlite-3.5.3.p4
libgpg_error-1.6.p0
libgcrypt-1.4.3.p0
opencdk-0.6.6
gnutls-2.2.1.p1
libpng-1.2.35
python-2.6.2.p0
freetype-2.3.5.p0
gd-2.0.35.p1
gdmodule-0.56.p5
fortran-20071120.p5
lapack-20071123.p0
atlas-3.8.3.p5
gsl-1.10.p1
iml-1.0.1.p11
ipython-0.9.1.p0
givaro-3.2.13rc2
linbox-1.1.6
f2c-20070816.p1
blas-20070724
numpy-1.3.0
matplotlib-0.98.5.3rc0-svn6910.p3
mercurial-1.1.2
mpfr-2.4.1
mpfi-1.3.4-cvs20071125.p7
pexpect-2.0.p3
pycrypto-2.0.1.p3
pynac-0.1.8.p1
cython-0.11.1.p0
sympy-0.6.4
zodb3-3.7.0.p1
networkx-0.99.p1-fake_really-0.36
quaddouble-2.2.p9
python_gnutls-1.1.4.p3
twisted-8.2.0
singular-3-1-0-2-20090618
scons-1.2.0
symmetrica-2.0.p4
libfplll-3.0.12.p0
boost-cropped-1.34.1
polybori-0.5rc.p8
rpy-1.0.1.p2
r-2.6.1.p22
rubiks-20070912.p8
libm4ri-20090617
ecm-6.2.1.p0
zn_poly-0.9.p1
ghmm-20080813.p0
pyprocessing-0.52
docutils-0.5
setuptools-0.6c9
jinja-1.2


```



---

Comment by drkirkby created at 2009-06-29 16:43:59

Changing status from new to assigned.


---

Comment by drkirkby created at 2009-06-29 16:43:59

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-06-29 16:43:59

I should have stated, this is with sage-4.1.alpha2


---

Comment by drkirkby created at 2009-06-30 14:12:01

This has now been resolved, thanks to Marc Glisse's help after I posted the query to comp.unix.solaris. The PARI code was missing the gcc compiler flag -fPIC. Why PARI built on my own Blade 2000 but not on the 16-core T5240 (t2.math.washington.edu) is not clear to me. 

Here's a patch, which adds -fPIC to one of the files used to generate the Makefile that PARI uses.

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/pari/

Basically all my patch does is to add this to the top of spkg-install, which adds -fPIC

```
# As of PARI 2.3.3, the compiler flag -fPIC is not added on Solaris, but it needs to be. It basically adds:
if [ `uname` = "SunOS" ]; then
  sed 's/-fomit-frame-pointer/-fomit-frame-pointer -fPIC/g' src/config/get_cc > src/config/get_cc.$$
  mv src/config/get_cc.$$ src/config/get_cc
fi
```

and remove that below

```
# PARI doesn't set PIC correctly on Solaris, so we do this.
  if [ `uname` = "SunOS" ]; then
   CFLAGS=$CFLAGS" -fPIC"
   export CFLAGS
fi
```

since the latter code was not working, despite it's obvious attempts to add -fPIC

David Kirkby


---

Comment by drkirkby created at 2009-06-30 14:12:01

Changing keywords from "solaris pari" to "solaris pari fPIC".


---

Comment by drkirkby created at 2009-07-15 12:58:15

It was noted by Minh Nguyen that there were a couple of junk files (spkg-install.orig & spkg-install.patch). These have now been removed. 

The package can be found at 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/pari/pari-2.3.3.p1.spkg

Could someone add that with hg for me, as I don't yet know how to use it (sorry). 

I meaningful comment would be "Adds -fPIC to allow building on Solaris. Removes a previous unsuccessful attempt at adding -fPIC"


Dave


---

Comment by mvngu created at 2009-07-15 13:50:15

Replying to [comment:3 drkirkby]:
> It was noted by Minh Nguyen that there were a couple of junk files (spkg-install.orig & spkg-install.patch). These have now been removed. 
> 
> The package can be found at 
> 
> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/pari/pari-2.3.3.p1.spkg
> 
> Could someone add that with hg for me, as I don't yet know how to use it (sorry). 
> 
> I meaningful comment would be "Adds -fPIC to allow building on Solaris. Removes a previous unsuccessful attempt at adding -fPIC"

I've committed the changes in your name. I also did some minor formatting and fixed some typos. The new spkg is up at
http://sage.math.washington.edu/home/mvngu/patch/pari-2.3.3.p1.spkg
Wow! The new spkg with your changes successfully builds on t2 and sage.math. All tests passed on sage.math. Thanks, David!


---

Comment by drkirkby created at 2009-07-15 15:55:54

Thank you too. The changes were limited to Solaris, so should have no effect on another platform. 

Dave


---

Comment by mvngu created at 2009-07-16 10:26:00

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:28:42

Resolution: fixed
