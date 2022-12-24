# Issue 7092: build failure of pari-2.3.3.p1.spkg  with gcc-4.4.1 as distributed by Fedora 11

archive/issues_007092.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: gcc\n\nAs from alpha0 building pari-2.3.3.p1.spkg faild to buil on Fedora 11, 32 bit.\n\n\n\n```\ngcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base3.o ../src/basemath/base3.c\ngcc: Internal error: Killed (program cc1)\nPlease submit a full bug report.\nSee <http://bugzilla.redhat.com/bugzilla> for instructions.\nmake[3]: *** [base3.o] Error 1\nmake[3]: Leaving directory `/home/jaap/downloads/sage-4.1.2.rc0/spkg/build/pari-2.3.3.p1/src/Olinux-i686'\nmake[2]: *** [gp] Error 2\nmake[2]: Leaving directory `/home/jaap/downloads/sage-4.1.2.rc0/spkg/build/pari-2.3.3.p1/src'\nError building GP\n\nreal\t37m26.888s\nuser\t31m48.467s\nsys\t0m33.612s\nsage: An error occurred while installing pari-2.3.3.p1\n\n```\n\n\n\nWe see this with gcc-4.4,1:\n\n\n```\n[jaap@paix sage-4.1.2.rc0]$ gcc -v\nUsing built-in specs.\nTarget: i586-redhat-linux\nConfigured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre --enable-libgcj-multifile --enable-java-maintainer-mode --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --disable-libjava-multilib --with-ppl --with-cloog --with-tune=generic --with-arch=i586 --build=i586-redhat-linux\nThread model: posix\ngcc version 4.4.1 20090725 (Red Hat 4.4.1-2) (GCC) \n\n```\n\n\nA workaround: change OPTFLAGS=-O3 to OPTFLAGS=-O1 in the file src/config/get_cc\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/7092\n\n",
    "created_at": "2009-10-01T17:13:35Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "build failure of pari-2.3.3.p1.spkg  with gcc-4.4.1 as distributed by Fedora 11",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7092",
    "user": "jsp"
}
```
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
[jaap@paix sage-4.1.2.rc0]$ gcc -v
Using built-in specs.
Target: i586-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre --enable-libgcj-multifile --enable-java-maintainer-mode --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --disable-libjava-multilib --with-ppl --with-cloog --with-tune=generic --with-arch=i586 --build=i586-redhat-linux
Thread model: posix
gcc version 4.4.1 20090725 (Red Hat 4.4.1-2) (GCC) 

```


A workaround: change OPTFLAGS=-O3 to OPTFLAGS=-O1 in the file src/config/get_cc

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/7092





---

archive/issue_comments_058605.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-10-02T17:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58605",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_058606.json:
```json
{
    "body": "New spkg up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p2.spkg",
    "created_at": "2009-10-03T05:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58606",
    "user": "mvngu"
}
```

New spkg up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p2.spkg



---

archive/issue_comments_058607.json:
```json
{
    "body": "Nope, but thanks for trying:\n\n```\ners  -o base1.o ../src/basemath/base1.c\ngcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base2.o ../src/basemath/base2.c\ngcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o base3.o ../src/basemath/base3.c\n`     \n\n\n`n`\ncc1: out of memory allocating 248 bytes after a total of 2896711680 bytes\nmake[1]: *** [base3.o] Error 1\nmake[1]: Leaving directory `/home/wstein/build/sage-4.1.2.rc0/spkg/build/pari-2.3.3.p2/src/Olinux-i686'\nmake: *** [gp] Error 2\nError building GP\n\nreal\t17m30.276s\nuser\t1m35.578s\nsys\t0m31.822s\nsage: An error occurred while installing pari-2.3.3.p2\nPlease email sage-devel http://groups.\n```\n",
    "created_at": "2009-10-03T09:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58607",
    "user": "was"
}
```

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

archive/issue_comments_058608.json:
```json
{
    "body": "But we will get to the bottom of this!!",
    "created_at": "2009-10-03T09:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58608",
    "user": "was"
}
```

But we will get to the bottom of this!!



---

archive/issue_comments_058609.json:
```json
{
    "body": "This patch does not work because the file get_cc is copied to the wrong place.\n\n\n```\ncd src\n\ncp \"$TOP\"/patches/get_dlld config/\n\n# mabshoff: This patch is to get around problem in PPC 32-bit Linux build\n# (but it is ok on any other machine)\ncp \"$TOP\"/patches/get_dlcflags config/\n\n# cwitty: disable -rpath\ncp \"$TOP\"/patches/get_ld config/\n\n# cwitty: disable TeX; allow bz2 compression\ncp \"$TOP\"/patches/gphelp.in doc/\n\n# mabshoff: copy over patched hnf routine (#2204)\ncp \"$TOP\"/patches/alglin2.c src/basemath/\n\n# Minh Van Nguyen: copy over patched get_cc (#7092)\ncp \"$TOP\"/patches/get_cc src/config/get_cc\n\n```\n\nThe last line should be:\n\n\n```\ncp \"$TOP\"/patches/get_cc config/get_cc\n\n```\n\n\n\nJaap",
    "created_at": "2009-10-03T09:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58609",
    "user": "jsp"
}
```

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

archive/issue_comments_058610.json:
```json
{
    "body": "Replying to [comment:5 jsp]:\n> The last line should be:\n\n```\ncp \"$TOP\"/patches/get_cc config/get_cc\n```\n\nThank you very much for this, Jaap. The updated spkg is up at \n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p3.spkg",
    "created_at": "2009-10-03T09:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58610",
    "user": "mvngu"
}
```

Replying to [comment:5 jsp]:
> The last line should be:

```
cp "$TOP"/patches/get_cc config/get_cc
```

Thank you very much for this, Jaap. The updated spkg is up at 

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p3.spkg



---

archive/issue_comments_058611.json:
```json
{
    "body": "This patch worked.\n\n\n\n```\nreal\t0m42.758s\nuser\t0m30.859s\nsys\t0m7.377s\nSuccessfully installed pari-2.3.3.p3\n\n```\n\n\n\nSo positive review.\n\nJaap",
    "created_at": "2009-10-03T09:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58611",
    "user": "jsp"
}
```

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

archive/issue_comments_058612.json:
```json
{
    "body": "The package `pari-2.3.3.p3.spkg` doesn't compile on t2.math (SPARC Solaris 10) with GCC 4.4.1:\n\n```\ngcc  -o libpari-gmp.so.2.3.3 -shared  -O1 -Wall -fno-strict-aliasing -fomit-fra\\\nme-pointer     -Wl,-G,-h,libpari-gmp.so.2 mp.o mpinl.o Flx.o Qfb.o RgX.o alglin\\\n1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.\\\no bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifact\\\nor1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o t\\\nrans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum\\\n.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o\\\n mpqs.o nffactor.o part.o stark.o subfield.o thue.o -lc -lm -L/scratch/mvngu/sa\\\nndbox/sage-4.1.2.rc0-7092-pari-cliquer/local/lib -lgmp\nText relocation remains                         referenced\n    against symbol                  offset      in file\n<unknown>                           0xcb0       alglin2.o\n\n<SNIP>\n\n__gmpn_mod_1                        0xf2a4      mp.o\nld: fatal: relocations remain against allocatable but non-writable sections\ncollect2: ld returned 1 exit status\nmake[3]: *** [libpari-gmp.so.2.3.3] Error 1\nmake[3]: Leaving directory `/scratch/mvngu/sandbox/sage-4.1.2.rc0-7092-pari-cli\\\nquer/spkg/build/pari-2.3.3.p3/src/Osolaris-none'\nmake[2]: *** [gp] Error 2\nmake[2]: Leaving directory `/scratch/mvngu/sandbox/sage-4.1.2.rc0-7092-pari-cli\\\nquer/spkg/build/pari-2.3.3.p3/src'\nError building GP\n\nreal    8m2.098s\nuser    6m48.688s\nsys     1m5.711s\nsage: An error occurred while installing pari-2.3.3.p3\n```\n\nAn updated spkg is up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/pari-2.3.3.p4.spkg\n\nThis package only patches the file `get_cc` on Linux systems.",
    "created_at": "2009-10-03T13:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58612",
    "user": "mvngu"
}
```

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

archive/issue_comments_058613.json:
```json
{
    "body": "Hi,\n\nSure it was a kind of stupid doing things with get_cc in two places.\n\n\n```\n# As of PARI 2.3.3, the compiler flag -fPIC is not added on Solaris, but it\n# needs to be.\nif [ `uname` = \"SunOS\" ]; then\n    sed 's/-fomit-frame-pointer/-fomit-frame-pointer -fPIC/g' src/config/get_cc > src/config/get_cc.$$\n    mv src/config/get_cc.$$ src/config/get_cc\nfi\n\n```\n\nSorry I didn't see this before.\n\nBut now it will be a good (temporary?) workaround,\n\nJaap",
    "created_at": "2009-10-03T13:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58613",
    "user": "jsp"
}
```

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

archive/issue_comments_058614.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-04T01:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58614",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_058615.json:
```json
{
    "body": "merged into 4.1.2.",
    "created_at": "2009-10-04T01:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7092#issuecomment-58615",
    "user": "was"
}
```

merged into 4.1.2.
