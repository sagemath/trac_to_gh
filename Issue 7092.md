# Issue 7092: build failure of pari-2.3.3.p1.spkg  with gcc-4.4.1 as distributed by Fedora 11

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2009-10-01 17:13:35

Assignee: mabshoff

Keywords: gcc

As from alpha0 building pari-2.3.3.p1.spkg faild to buil on Fedora 11, 32 bit.



```
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base3.o ../src/basemath/base3.c
gcc: Internal error: Killed (program cc1)
Please submit a full bug report.
See <http://bugzilla.redhat.com/bugzilla> for instructions.
make[3]: *** [base3.o] Error 1
make[3]: Leaving directory `/home/jaap/downloads/sage-4.1.2.rc0/spkg/build/pari-2.3.3.p1/src/Olinux-i686'
make[2]: *** [gp] Error 2
make[2]: Leaving directory `/home/jaap/downloads/sage-4.1.2.rc0/spkg/build/pari-2.3.3.p1/src'
Error building GP

real	37m26.888s
user	31m48.467s
sys	0m33.612s
sage: An error occurred while installing pari-2.3.3.p1

```



We see this with gcc-4.4,1:


```
[jaap`@`paix sage-4.1.2.rc0]$ gcc -v
Using built-in specs.
Target: i586-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre --enable-libgcj-multifile --enable-java-maintainer-mode --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --disable-libjava-multilib --with-ppl --with-cloog --with-tune=generic --with-arch=i586 --build=i586-redhat-linux
Thread model: posix
gcc version 4.4.1 20090725 (Red Hat 4.4.1-2) (GCC) 

```


A workaround: change OPTFLAGS=-O3 to OPTFLAGS=-O1 in the file src/config/get_cc

Jaap


---

Comment by was created at 2009-10-02 17:49:17

Changing priority from major to blocker.


---

Comment by mvngu created at 2009-10-03 05:34:00

New spkg up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p2.spkg


---

Comment by was created at 2009-10-03 09:00:50

Nope, but thanks for trying:

```
ers  -o base1.o ../src/basemath/base1.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base2.o ../src/basemath/base2.c
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base3.o ../src/basemath/base3.c
`     


`n`
cc1: out of memory allocating 248 bytes after a total of 2896711680 bytes
make[1]: *** [base3.o] Error 1
make[1]: Leaving directory `/home/wstein/build/sage-4.1.2.rc0/spkg/build/pari-2.3.3.p2/src/Olinux-i686'
make: *** [gp] Error 2
Error building GP

real	17m30.276s
user	1m35.578s
sys	0m31.822s
sage: An error occurred while installing pari-2.3.3.p2
Please email sage-devel http://groups.
```



---

Comment by was created at 2009-10-03 09:07:38

But we will get to the bottom of this!!


---

Comment by jsp created at 2009-10-03 09:13:57

This patch does not work because the file get_cc is copied to the wrong place.


```
cd src

cp "$TOP"/patches/get_dlld config/

# mabshoff: This patch is to get around problem in PPC 32-bit Linux build
# (but it is ok on any other machine)
cp "$TOP"/patches/get_dlcflags config/

# cwitty: disable -rpath
cp "$TOP"/patches/get_ld config/

# cwitty: disable TeX; allow bz2 compression
cp "$TOP"/patches/gphelp.in doc/

# mabshoff: copy over patched hnf routine (#2204)
cp "$TOP"/patches/alglin2.c src/basemath/

# Minh Van Nguyen: copy over patched get_cc (#7092)
cp "$TOP"/patches/get_cc src/config/get_cc

```

The last line should be:


```
cp "$TOP"/patches/get_cc config/get_cc

```



Jaap


---

Comment by mvngu created at 2009-10-03 09:23:29

Replying to [comment:5 jsp]:
> The last line should be:

```
cp "$TOP"/patches/get_cc config/get_cc
```

Thank you very much for this, Jaap. The updated spkg is up at 

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p3.spkg


---

Comment by jsp created at 2009-10-03 09:30:23

This patch worked.



```
real	0m42.758s
user	0m30.859s
sys	0m7.377s
Successfully installed pari-2.3.3.p3

```



So positive review.

Jaap


---

Comment by mvngu created at 2009-10-03 13:43:40

The package `pari-2.3.3.p3.spkg` doesn't compile on t2.math (SPARC Solaris 10) with GCC 4.4.1:

```
gcc  -o libpari-gmp.so.2.3.3 -shared  -O1 -Wall -fno-strict-aliasing -fomit-fra\
me-pointer     -Wl,-G,-h,libpari-gmp.so.2 mp.o mpinl.o Flx.o Qfb.o RgX.o alglin\
1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.\
o bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifact\
or1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o t\
rans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum\
.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o\
 mpqs.o nffactor.o part.o stark.o subfield.o thue.o -lc -lm -L/scratch/mvngu/sa\
ndbox/sage-4.1.2.rc0-7092-pari-cliquer/local/lib -lgmp
Text relocation remains                         referenced
    against symbol                  offset      in file
<unknown>                           0xcb0       alglin2.o

<SNIP>

__gmpn_mod_1                        0xf2a4      mp.o
ld: fatal: relocations remain against allocatable but non-writable sections
collect2: ld returned 1 exit status
make[3]: *** [libpari-gmp.so.2.3.3] Error 1
make[3]: Leaving directory `/scratch/mvngu/sandbox/sage-4.1.2.rc0-7092-pari-cli\
quer/spkg/build/pari-2.3.3.p3/src/Osolaris-none'
make[2]: *** [gp] Error 2
make[2]: Leaving directory `/scratch/mvngu/sandbox/sage-4.1.2.rc0-7092-pari-cli\
quer/spkg/build/pari-2.3.3.p3/src'
Error building GP

real    8m2.098s
user    6m48.688s
sys     1m5.711s
sage: An error occurred while installing pari-2.3.3.p3
```

An updated spkg is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p4.spkg

This package only patches the file `get_cc` on Linux systems.


---

Comment by jsp created at 2009-10-03 13:56:56

Hi,

Sure it was a kind of stupid doing things with get_cc in two places.


```
# As of PARI 2.3.3, the compiler flag -fPIC is not added on Solaris, but it
# needs to be.
if [ `uname` = "SunOS" ]; then
    sed 's/-fomit-frame-pointer/-fomit-frame-pointer -fPIC/g' src/config/get_cc > src/config/get_cc.$$
    mv src/config/get_cc.$$ src/config/get_cc
fi

```

Sorry I didn't see this before.

But now it will be a good (temporary?) workaround,

Jaap


---

Comment by was created at 2009-10-04 01:04:09

Resolution: fixed


---

Comment by was created at 2009-10-04 01:04:09

merged into 4.1.2.
