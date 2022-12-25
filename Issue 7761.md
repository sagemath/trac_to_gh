# Issue 7761: Python 2.6.2.p4 faills to build on Open Solaris

archive/issues_007761.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @williamstein david.kirkby@onetel.net mvngu\n\nKeywords: python open solaris\n\nI believe William is aware of this bug and said it can be fixed by installing OpenSSL or similar. But I am unable to find a trac ticket for it, so I thought I'd open one. It's interesting this issue does not arise on Solaris 10 (SPARC), despite OpenSSL libraries not being present there either. This bug seems to come up a lot on linux too, as a Google search shows. \n\nOn a Sun Ultra 27 (Intel Xeon processor), running Open Solaris 06/2009, I get the following problem when python is being built. \n\n\n```\ncopying build/scripts-2.6/pydoc -> /export/home/drkirkby/sage-4.3.rc2/local/bin\nchanging mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/2to3 to 755\nchanging mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/smtpd.py to 755\nchanging mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/idle to 755\nchanging mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/pydoc to 755\nrunning install_egg_info\nRemoving /export/home/drkirkby/sage-4.3.rc2/local/lib/python2.6/lib-dynload/Python-2.6.2-py2.6.egg-info\nWriting /export/home/drkirkby/sage-4.3.rc2/local/lib/python2.6/lib-dynload/Python-2.6.2-py2.6.egg-info\nif test -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python -o -h /export/home/drkirkby/sage-4.3.rc2/local/bin/python; \\\n\tthen rm -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python; \\\n\telse true; \\\n\tfi\n(cd /export/home/drkirkby/sage-4.3.rc2/local/bin; ln python2.6 python)\nrm -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python-config\n(cd /export/home/drkirkby/sage-4.3.rc2/local/bin; ln -s python2.6-config python-config)\n/usr/bin/ginstall -c -m 644 ./Misc/python.man \\\n\t\t/export/home/drkirkby/sage-4.3.rc2/local/share/man/man1/python.1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.rc2/spkg/build/python-2.6.2.p4/src'\nSleeping for three seconds before testing python\nTraceback (most recent call last):\n  File \"<string>\", line 1, in <module>\n  File \"/export/home/drkirkby/sage-4.3.rc2/local/lib/python/hashlib.py\", line 136, in <module>\n    md5 = __get_builtin_constructor('md5')\n  File \"/export/home/drkirkby/sage-4.3.rc2/local/lib/python/hashlib.py\", line 63, in __get_builtin_constructor\n    import _md5\nImportError: No module named _md5\n\nreal\t1m38.244s\nuser\t1m15.115s\nsys\t0m13.132s\nsage: An error occurred while installing python-2.6.2.p4\n\n```\n\n\nI'm not sure if this should be reported upstream or not. Some feedback on that might be useful. If so, I will report it to a python bug tracker or similar. The issue seems to arrise often enough. \n\nDave \n\nPS, to even get to this point, I had to delete the following list of files, to get around a gnutls issue in #7387.\n\n\n```\n    * SAGE_LOCAL/include/gcrypt-module.h\n    * SAGE_LOCAL/include/gpg-error.h\n    * SAGE_LOCAL/include/gcrypt.h\n    * SAGE_LOCAL/lib/libgcrypt*\n    * SAGE_LOCAL/lib/libgpg* \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7761\n\n",
    "created_at": "2009-12-24T16:45:17Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Python 2.6.2.p4 faills to build on Open Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7761",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @williamstein david.kirkby@onetel.net mvngu

Keywords: python open solaris

I believe William is aware of this bug and said it can be fixed by installing OpenSSL or similar. But I am unable to find a trac ticket for it, so I thought I'd open one. It's interesting this issue does not arise on Solaris 10 (SPARC), despite OpenSSL libraries not being present there either. This bug seems to come up a lot on linux too, as a Google search shows. 

On a Sun Ultra 27 (Intel Xeon processor), running Open Solaris 06/2009, I get the following problem when python is being built. 


```
copying build/scripts-2.6/pydoc -> /export/home/drkirkby/sage-4.3.rc2/local/bin
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/2to3 to 755
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/smtpd.py to 755
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/idle to 755
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/pydoc to 755
running install_egg_info
Removing /export/home/drkirkby/sage-4.3.rc2/local/lib/python2.6/lib-dynload/Python-2.6.2-py2.6.egg-info
Writing /export/home/drkirkby/sage-4.3.rc2/local/lib/python2.6/lib-dynload/Python-2.6.2-py2.6.egg-info
if test -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python -o -h /export/home/drkirkby/sage-4.3.rc2/local/bin/python; \
	then rm -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python; \
	else true; \
	fi
(cd /export/home/drkirkby/sage-4.3.rc2/local/bin; ln python2.6 python)
rm -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python-config
(cd /export/home/drkirkby/sage-4.3.rc2/local/bin; ln -s python2.6-config python-config)
/usr/bin/ginstall -c -m 644 ./Misc/python.man \
		/export/home/drkirkby/sage-4.3.rc2/local/share/man/man1/python.1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.rc2/spkg/build/python-2.6.2.p4/src'
Sleeping for three seconds before testing python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/export/home/drkirkby/sage-4.3.rc2/local/lib/python/hashlib.py", line 136, in <module>
    md5 = __get_builtin_constructor('md5')
  File "/export/home/drkirkby/sage-4.3.rc2/local/lib/python/hashlib.py", line 63, in __get_builtin_constructor
    import _md5
ImportError: No module named _md5

real	1m38.244s
user	1m15.115s
sys	0m13.132s
sage: An error occurred while installing python-2.6.2.p4

```


I'm not sure if this should be reported upstream or not. Some feedback on that might be useful. If so, I will report it to a python bug tracker or similar. The issue seems to arrise often enough. 

Dave 

PS, to even get to this point, I had to delete the following list of files, to get around a gnutls issue in #7387.


```
    * SAGE_LOCAL/include/gcrypt-module.h
    * SAGE_LOCAL/include/gpg-error.h
    * SAGE_LOCAL/include/gcrypt.h
    * SAGE_LOCAL/lib/libgcrypt*
    * SAGE_LOCAL/lib/libgpg* 
```


Issue created by migration from https://trac.sagemath.org/ticket/7761





---

archive/issue_comments_066709.json:
```json
{
    "body": "These problems go away if one builds in 64-bit mode, by exporting SAGE64 to yes. However, CFLAGS must be passed properly to Python, otherwise the -m64 does not get added as a CFLAG. That was only happening on OS X. \n\nThis updated spkg file adds:\n\n\n```\nCC=\"$CC $CFLAGS\"\n```\n\non the end of the configure line. Then, as long as CFLAGS contains -m64, so the package will build with 64-bit support. \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/",
    "created_at": "2010-01-02T09:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66709",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

These problems go away if one builds in 64-bit mode, by exporting SAGE64 to yes. However, CFLAGS must be passed properly to Python, otherwise the -m64 does not get added as a CFLAG. That was only happening on OS X. 

This updated spkg file adds:


```
CC="$CC $CFLAGS"
```

on the end of the configure line. Then, as long as CFLAGS contains -m64, so the package will build with 64-bit support. 

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/



---

archive/issue_comments_066710.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T09:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66710",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066711.json:
```json
{
    "body": "On my Open Solaris build still fails:\n\n```\nSleeping for three seconds before testing python\nTraceback (most recent call last):\n  File \"<string>\", line 1, in <module>\n  File \"/export/home/jaap/Downloads/sage-4.3/local/lib/python/hashlib.py\", line 136, in <module>\n    md5 = __get_builtin_constructor('md5')\n  File \"/export/home/jaap/Downloads/sage-4.3/local/lib/python/hashlib.py\", line 63, in __get_builtin_constructor\n    import _md5\nImportError: No module named _md5\n\nreal\t3m11.679s\nuser\t1m47.153s\nsys\t0m36.011s\nsage: An error occurred while installing python-2.6.2.p5\n\n```\n\n\nWhere is openssl supposed to be be installed?\n\n/usr/local/ssl did not work for me.\n\nJaap",
    "created_at": "2010-01-03T01:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66711",
    "user": "https://github.com/jaapspies"
}
```

On my Open Solaris build still fails:

```
Sleeping for three seconds before testing python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/export/home/jaap/Downloads/sage-4.3/local/lib/python/hashlib.py", line 136, in <module>
    md5 = __get_builtin_constructor('md5')
  File "/export/home/jaap/Downloads/sage-4.3/local/lib/python/hashlib.py", line 63, in __get_builtin_constructor
    import _md5
ImportError: No module named _md5

real	3m11.679s
user	1m47.153s
sys	0m36.011s
sage: An error occurred while installing python-2.6.2.p5

```


Where is openssl supposed to be be installed?

/usr/local/ssl did not work for me.

Jaap



---

archive/issue_comments_066712.json:
```json
{
    "body": "That is very odd. I just used OpenSSL's default location, which is /usr/local/ssl. Python knows to look there. I manged to get the following all built now in 64-bit mode.  \n\n```\ndrkirkby@hawk:~/sage-4.3/spkg/installed$ ls\nbzip2-1.0.5             libgcrypt-1.4.4.p1      python-2.6.2.p5\ncliquer-1.2.p2          libgpg_error-1.6.p3     readline-6.0.p1\nconway_polynomials-0.2  libpng-1.2.35.p0        sage_scripts-4.3\ndir-0.1                 mercurial-1.3.1.p0      scons-1.2.0\neclib-20080310.p8       mpir-1.2.2              sqlite-3.6.19.p0\nelliptic_curves-0.1     ntl-5.4.2.p9            termcap-1.3.1.p0\nextcode-4.3             opencdk-0.6.6.p3        zlib-1.2.3.p5\ngnutls-2.2.1.p5         pari-2.3.3.p5\ngraphs-20070722.p1      prereq-0.6\n```\n\nbefore Flint decided it did not want to play ball, and exited with an ELFCLASS problem (mixing of 32 and 64-bit objects). \n\nI did something like:\n\n```\n$ export SAGE64=yes\n$ export CFLAGS=-m64\n$ export CXFLAGS=-m64\n$ export FCFLAGS=-m64\n$ export SAGE_FORTRAN_LIB=/usr/local/lib/libgfortran.so\n$ make\n```\n\n\nI've got several gcc's on here, but just noticed the one which got this far was **not** using the GNU asssembler as I advised, but all Sun tools. Note the configure option '--with-build-time-tools=/usr/ccs/bin' Perhaps the GCC bugs are sorted out in 4.4.2 which allow it to work with the Sun assembler. \n\n```\ndrkirkby@hawk:~$ gcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ./configure --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.2 (GCC) \n```\n",
    "created_at": "2010-01-03T02:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66712",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That is very odd. I just used OpenSSL's default location, which is /usr/local/ssl. Python knows to look there. I manged to get the following all built now in 64-bit mode.  

```
drkirkby@hawk:~/sage-4.3/spkg/installed$ ls
bzip2-1.0.5             libgcrypt-1.4.4.p1      python-2.6.2.p5
cliquer-1.2.p2          libgpg_error-1.6.p3     readline-6.0.p1
conway_polynomials-0.2  libpng-1.2.35.p0        sage_scripts-4.3
dir-0.1                 mercurial-1.3.1.p0      scons-1.2.0
eclib-20080310.p8       mpir-1.2.2              sqlite-3.6.19.p0
elliptic_curves-0.1     ntl-5.4.2.p9            termcap-1.3.1.p0
extcode-4.3             opencdk-0.6.6.p3        zlib-1.2.3.p5
gnutls-2.2.1.p5         pari-2.3.3.p5
graphs-20070722.p1      prereq-0.6
```

before Flint decided it did not want to play ball, and exited with an ELFCLASS problem (mixing of 32 and 64-bit objects). 

I did something like:

```
$ export SAGE64=yes
$ export CFLAGS=-m64
$ export CXFLAGS=-m64
$ export FCFLAGS=-m64
$ export SAGE_FORTRAN_LIB=/usr/local/lib/libgfortran.so
$ make
```


I've got several gcc's on here, but just noticed the one which got this far was **not** using the GNU asssembler as I advised, but all Sun tools. Note the configure option '--with-build-time-tools=/usr/ccs/bin' Perhaps the GCC bugs are sorted out in 4.4.2 which allow it to work with the Sun assembler. 

```
drkirkby@hawk:~$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ./configure --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.2 (GCC) 
```




---

archive/issue_comments_066713.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n> That is very odd. I just used OpenSSL's default location, which is /usr/local/ssl. Python knows to look there. I manged to get the following all built now in 64-bit mode.  \n\nYou are right. The problem I have is again with ld\n\n\n```\nBN_mod_sqrt                         0x1159      /usr/local/lib/libcrypto.a(ecp_smpl.o)\nBN_kronecker                        0x119e      /usr/local/lib/libcrypto.a(ecp_smpl.o)\nBN_kronecker                        0x1f5       /usr/local/lib/libcrypto.a(bn_sqrt.o)\n.rodata (section)                   0x198       /usr/local/lib/libcrypto.a(bn_kron.o)\n.rodata (section)                   0x293       /usr/local/lib/libcrypto.a(bn_kron.o)\n.rodata.str1.1 (merged string section) 0x56             /usr/local/lib/libcrypto.a(bn_sqrt.o)\n.rodata.str1.1 (merged string section) 0x491            /usr/local/lib/libcrypto.a(bn_sqrt.o)\n.rodata.str1.1 (merged string section) 0x529            /usr/local/lib/libcrypto.a(bn_sqrt.o)\n.rodata.str1.1 (merged string section) 0x53e            /usr/local/lib/libcrypto.a(bn_sqrt.o)\nld: fatal: relocations remain against allocatable but non-writable sections\ncollect2: ld returned 1 exit status\n\n```\n\n\nI'll build a new gcc.\n\nJaap",
    "created_at": "2010-01-05T14:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66713",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:3 drkirkby]:
> That is very odd. I just used OpenSSL's default location, which is /usr/local/ssl. Python knows to look there. I manged to get the following all built now in 64-bit mode.  

You are right. The problem I have is again with ld


```
BN_mod_sqrt                         0x1159      /usr/local/lib/libcrypto.a(ecp_smpl.o)
BN_kronecker                        0x119e      /usr/local/lib/libcrypto.a(ecp_smpl.o)
BN_kronecker                        0x1f5       /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata (section)                   0x198       /usr/local/lib/libcrypto.a(bn_kron.o)
.rodata (section)                   0x293       /usr/local/lib/libcrypto.a(bn_kron.o)
.rodata.str1.1 (merged string section) 0x56             /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata.str1.1 (merged string section) 0x491            /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata.str1.1 (merged string section) 0x529            /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata.str1.1 (merged string section) 0x53e            /usr/local/lib/libcrypto.a(bn_sqrt.o)
ld: fatal: relocations remain against allocatable but non-writable sections
collect2: ld returned 1 exit status

```


I'll build a new gcc.

Jaap



---

archive/issue_comments_066714.json:
```json
{
    "body": "> .rodata.str1.1 (merged string section) 0x53e            /usr/local/lib/libcrypto.a(bn_sqrt.o)\n> ld: fatal: relocations remain against allocatable but non-writable sections\n> collect2: ld returned 1 exit status\n> \n> }}}\n> \n> I'll build a new gcc.\n> \n> Jaap\n> \nYes, I think building a new gcc is probably your best course of action. Several people have said gcc 4.3.4 is one of the more stable gcc's. \n\nI think ATLAS might dictate the use of the Sun assembler, as some of the assembly looks like it will only work with the GNU assembler. \n\nThe following has allowed me to build python with 'hashlib' support. Try building python with that. If it fails, try building OpenSSL with it. \n\nIf all else fails, I can make some tarbals of my gcc and binutils binaries, upload them, then you try those. Then we would have **exactly** the same build tools. But I don't believe such drastic measures should be necessary, but if they are helpful, I can do it. \n\n```\ndrkirkby@hawk:~/sage-4.3.1.alpha1$ gcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.3.4 (GCC) \n```\n",
    "created_at": "2010-01-07T17:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66714",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

> .rodata.str1.1 (merged string section) 0x53e            /usr/local/lib/libcrypto.a(bn_sqrt.o)
> ld: fatal: relocations remain against allocatable but non-writable sections
> collect2: ld returned 1 exit status
> 
> }}}
> 
> I'll build a new gcc.
> 
> Jaap
> 
Yes, I think building a new gcc is probably your best course of action. Several people have said gcc 4.3.4 is one of the more stable gcc's. 

I think ATLAS might dictate the use of the Sun assembler, as some of the assembly looks like it will only work with the GNU assembler. 

The following has allowed me to build python with 'hashlib' support. Try building python with that. If it fails, try building OpenSSL with it. 

If all else fails, I can make some tarbals of my gcc and binutils binaries, upload them, then you try those. Then we would have **exactly** the same build tools. But I don't believe such drastic measures should be necessary, but if they are helpful, I can do it. 

```
drkirkby@hawk:~/sage-4.3.1.alpha1$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.3.4 (GCC) 
```




---

archive/issue_comments_066715.json:
```json
{
    "body": "I'm sticking this to 'needs info' as I've noticed another problem in this package (incorrect usage of set -e), and might as well fix the other one at the same time.",
    "created_at": "2010-01-10T18:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66715",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm sticking this to 'needs info' as I've noticed another problem in this package (incorrect usage of set -e), and might as well fix the other one at the same time.



---

archive/issue_comments_066716.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-10T18:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66716",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_066717.json:
```json
{
    "body": "I'm slowly making progress building p5 on my Open Solaris in VirtualBox :)\n\n_ssl.o and ssl.so are now built. _hashlib.so failed on:\n\n\n\n```\ngcc -Wall -g -m64 -Wall -g -m64 -shared -L/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/lib -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I. -IInclude -I./Include -I/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/include build/temp.solaris-2.11-i86pc-2.6/export/home/jaap/Downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5/src/Modules/_hashopenssl.o -L/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/lib -L/usr/local/lib -lssl -lcrypto -o build/lib.solaris-2.11-i86pc-2.6/_hashlib.so\n*** WARNING: renaming \"_hashlib\" since importing it failed: ld.so.1: python: fatal: relocation error: file build/lib.solaris-2.11-i86pc-2.6/_hashlib.so: symbol EVP_MD_CTX_md: referenced symbol not found\n\n```\n\n\n\nJaap",
    "created_at": "2010-01-10T18:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66717",
    "user": "https://github.com/jaapspies"
}
```

I'm slowly making progress building p5 on my Open Solaris in VirtualBox :)

_ssl.o and ssl.so are now built. _hashlib.so failed on:



```
gcc -Wall -g -m64 -Wall -g -m64 -shared -L/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/lib -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I. -IInclude -I./Include -I/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/include build/temp.solaris-2.11-i86pc-2.6/export/home/jaap/Downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5/src/Modules/_hashopenssl.o -L/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/lib -L/usr/local/lib -lssl -lcrypto -o build/lib.solaris-2.11-i86pc-2.6/_hashlib.so
*** WARNING: renaming "_hashlib" since importing it failed: ld.so.1: python: fatal: relocation error: file build/lib.solaris-2.11-i86pc-2.6/_hashlib.so: symbol EVP_MD_CTX_md: referenced symbol not found

```



Jaap



---

archive/issue_comments_066718.json:
```json
{
    "body": "I finally got this going on Open Solaris in VirtualBox!\n\nThe problem was related to different ssl libraries.\n\nWe have to be sure there is only one openssl in the process.\n\nIn the end I only used the system ssl and libcrypto\n\nInstalling OpenSLL is probably not the solution in Open Solaris.\n\nIn the standard setup the spkg installs fine.\n\nSo positive review! But leaving it to needs_info. Waiting for David.\n\nJaap",
    "created_at": "2010-01-10T21:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66718",
    "user": "https://github.com/jaapspies"
}
```

I finally got this going on Open Solaris in VirtualBox!

The problem was related to different ssl libraries.

We have to be sure there is only one openssl in the process.

In the end I only used the system ssl and libcrypto

Installing OpenSLL is probably not the solution in Open Solaris.

In the standard setup the spkg installs fine.

So positive review! But leaving it to needs_info. Waiting for David.

Jaap



---

archive/issue_comments_066719.json:
```json
{
    "body": "OK, I see you updated the spkg in\n\n[http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/)\n\nLet me test this.\n\nJaap",
    "created_at": "2010-01-10T21:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66719",
    "user": "https://github.com/jaapspies"
}
```

OK, I see you updated the spkg in

[http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/)

Let me test this.

Jaap



---

archive/issue_comments_066720.json:
```json
{
    "body": "Updated package which \n\n* Fixes the issue on Open Solaris, though it relies on having the new sage-env patch #7818 installed. \n* Removes 'set -e' which was hiding an error message. \n* Added a check that the Itanium fix was actually applied properly. (That was the only thing which was not checked in spkg-install. Almost everything else was properly checked). \n\nThe updated version can be found at: \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/",
    "created_at": "2010-01-10T21:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66720",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Updated package which 

* Fixes the issue on Open Solaris, though it relies on having the new sage-env patch #7818 installed. 
* Removes 'set -e' which was hiding an error message. 
* Added a check that the Itanium fix was actually applied properly. (That was the only thing which was not checked in spkg-install. Almost everything else was properly checked). 

The updated version can be found at: 

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/



---

archive/issue_comments_066721.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-01-10T21:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66721",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066722.json:
```json
{
    "body": "Attachment [python-7761.patch](tarball://root/attachments/some-uuid/ticket7761/python-7761.patch) by drkirkby created at 2010-01-10 21:41:26",
    "created_at": "2010-01-10T21:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66722",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [python-7761.patch](tarball://root/attachments/some-uuid/ticket7761/python-7761.patch) by drkirkby created at 2010-01-10 21:41:26



---

archive/issue_comments_066723.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-10T23:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66723",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066724.json:
```json
{
    "body": "On Open Solaris:\n\n\n```\nSleeping for three seconds before testing python\nhashlib module imported\n\nreal\t2m45.196s\nuser\t1m48.948s\nsys\t0m32.524s\nSuccessfully installed python-2.6.2.p5\nYou can safely delete the temporary build directory\n/export/home/jaap/Downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing python-2.6.2.p5.spkg\njaap@opensolaris:~/Downloads/sage-4.3.1.alpha1$ \n\n\n```\n\n\nFedora 12:\n\n\n```\nSleeping for three seconds before testing python\nhashlib module imported\n\nreal\t2m2.042s\nuser\t1m51.869s\nsys\t0m17.783s\nSuccessfully installed python-2.6.2.p5\nYou can safely delete the temporary build directory\n/home/jaap/downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing python-2.6.2.p5.spkg\n[jaap@vrede sage-4.3.1.alpha1]$ \n\n```\n\n\nOverall this looks good! Hope this gets into sage-3.4.1.\n\nPositive review.\n\nJaap",
    "created_at": "2010-01-10T23:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66724",
    "user": "https://github.com/jaapspies"
}
```

On Open Solaris:


```
Sleeping for three seconds before testing python
hashlib module imported

real	2m45.196s
user	1m48.948s
sys	0m32.524s
Successfully installed python-2.6.2.p5
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.2.p5.spkg
jaap@opensolaris:~/Downloads/sage-4.3.1.alpha1$ 


```


Fedora 12:


```
Sleeping for three seconds before testing python
hashlib module imported

real	2m2.042s
user	1m51.869s
sys	0m17.783s
Successfully installed python-2.6.2.p5
You can safely delete the temporary build directory
/home/jaap/downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.2.p5.spkg
[jaap@vrede sage-4.3.1.alpha1]$ 

```


Overall this looks good! Hope this gets into sage-3.4.1.

Positive review.

Jaap



---

archive/issue_comments_066725.json:
```json
{
    "body": "Too late for sage-3.4.1, but we'll still merge it ;-)",
    "created_at": "2010-01-13T06:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66725",
    "user": "https://github.com/rlmill"
}
```

Too late for sage-3.4.1, but we'll still merge it ;-)



---

archive/issue_events_007975.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T06:10:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7761#event-7975"
}
```



---

archive/issue_comments_066726.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T06:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66726",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_066727.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-01-29T23:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66727",
    "user": "https://github.com/robertwb"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_007976.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-01-29T23:59:54Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7761#event-7976"
}
```



---

archive/issue_comments_066728.json:
```json
{
    "body": "Does this still rely on the (unresolved) #7818? Distutils pulls CFLAGS out of the makefile, so I'm not convince that \n\n\n```\nCC=\"$CC $CFLAGS\"\n```\n\n\nis the way to go if extension modules should pick them up as well (but maybe it picks up CC as well). Probably better to pass them into the autoconf script using the OPT variable.",
    "created_at": "2010-01-29T23:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66728",
    "user": "https://github.com/robertwb"
}
```

Does this still rely on the (unresolved) #7818? Distutils pulls CFLAGS out of the makefile, so I'm not convince that 


```
CC="$CC $CFLAGS"
```


is the way to go if extension modules should pick them up as well (but maybe it picks up CC as well). Probably better to pass them into the autoconf script using the OPT variable.



---

archive/issue_comments_066729.json:
```json
{
    "body": "Replying to [comment:15 robertwb]:\n> Does this still rely on the (unresolved) #7818? Distutils pulls CFLAGS out of the makefile, so I'm not convince that \n> \n> {{{\n> CC=\"$CC $CFLAGS\"\n> }}}\n> \n> is the way to go if extension modules should pick them up as well (but maybe it picks up CC as well). Probably better to pass them into the autoconf script using the OPT variable. \n\nI don't like the way you handle this. Dave made a point. It works on Open Solaris when CFLAGS contains -m64.\n\nIt maybe not sufficient, but it works here and let me have a working python.\n\nI think release managers are way due to resolve this issue: having two p5 patches.\n\nLet's get on!\n\nJaap",
    "created_at": "2010-01-30T01:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66729",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:15 robertwb]:
> Does this still rely on the (unresolved) #7818? Distutils pulls CFLAGS out of the makefile, so I'm not convince that 
> 
> {{{
> CC="$CC $CFLAGS"
> }}}
> 
> is the way to go if extension modules should pick them up as well (but maybe it picks up CC as well). Probably better to pass them into the autoconf script using the OPT variable. 

I don't like the way you handle this. Dave made a point. It works on Open Solaris when CFLAGS contains -m64.

It maybe not sufficient, but it works here and let me have a working python.

I think release managers are way due to resolve this issue: having two p5 patches.

Let's get on!

Jaap



---

archive/issue_comments_066730.json:
```json
{
    "body": "I'm just saying that the problems we have later on using setup.py to build extensions may have to do with the fact that Python is built with \"covert\" command line options that Distutils doesn't pick up. I figured this ticket needed to be re-opened 'cause if it never got in it's clearly shouldn't be closed. (At this point, we should probably make a p6 spkg.) I agree with the general goal behind #7818, but it has issues that I don't know how to fix, so shouldn't be a dependancy (unless that gets worked out first).",
    "created_at": "2010-01-30T03:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66730",
    "user": "https://github.com/robertwb"
}
```

I'm just saying that the problems we have later on using setup.py to build extensions may have to do with the fact that Python is built with "covert" command line options that Distutils doesn't pick up. I figured this ticket needed to be re-opened 'cause if it never got in it's clearly shouldn't be closed. (At this point, we should probably make a p6 spkg.) I agree with the general goal behind #7818, but it has issues that I don't know how to fix, so shouldn't be a dependancy (unless that gets worked out first).



---

archive/issue_comments_066731.json:
```json
{
    "body": "I can understand why this was not merged. I'm just in the process of updating #7818. I just need to double check everything. But the main change is that \n\n* The user can supply SAGE_CFLAGS to set some CFLAGS they want. Since they are not setting CFLAGS, them doing so will not risk corrupting the Sage environment. \n\n* CFLAGS will not be exported, but instead 'SAGE_COMMON_CFLAGS', which will contain what the user specific in SAGE_CFLAGS, plus those flags I deem sensible. \n\n* Any spkg-install script that wants to use these flags, would have to do so by explicitly doing so via. \n\nCFLAGS=\"$SAGE_COMOON_CFLAGS\"\n\nThat I believe will be safe. No package is forced to use my flags, but they can choose to. Hence I believe the changes to sage-env will be 100% safe, as they will not change any commonly used environment variables. \n\nSo that's what I intend to do with sage-env. Now to the specific of this package. \n\nPrior to writing this new package, I looked at Python's spkg-install to see how the 64-bit build has been enabled on OS X, and you can see it added -m64 to gcc, so \"gcc -m64\" was used as a compiler. Hence I basically used a similar method. \n\nHaving later looked more carefully at the python documentation, the way to pass flags is not the way it is done on the spkg-install for OS X, so whist it may work, it is not the right way to do it. \n\nI think the best solution is that I update sage-env, then update the python package, but in a way that is specific to Solaris, AIX and HP-UX. Then at a later date, we can try in an alpha0 to drop it in without it being specific to that platform. \n\nI think the ability to allow the user to pass their own flags is quite important, as they can use that to optimise gcc for thier processor. At the momemnt, 95% of Sage's code is being built for a generic processor, and not exploiting the features of anyones particular processor. \n\nSo let me update sage-env in a safe way, then update this, to make use of sage-env's changes, but only on some rarer platforms. \n\nI think in the short term, Jaap should not worry about setting CFLAGS globally if it allows a package to build. Progress can then be made. He can always break the build process manually at some point, and unset it, just before cython gets to work. \n\nLeave it with me. I'll make what I believe are sensible decisions, then others can comment of course. In the mean time, I'm happy with this not being merged just now. I do agree it is sub-optimal. \n\nDave",
    "created_at": "2010-01-30T04:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66731",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I can understand why this was not merged. I'm just in the process of updating #7818. I just need to double check everything. But the main change is that 

* The user can supply SAGE_CFLAGS to set some CFLAGS they want. Since they are not setting CFLAGS, them doing so will not risk corrupting the Sage environment. 

* CFLAGS will not be exported, but instead 'SAGE_COMMON_CFLAGS', which will contain what the user specific in SAGE_CFLAGS, plus those flags I deem sensible. 

* Any spkg-install script that wants to use these flags, would have to do so by explicitly doing so via. 

CFLAGS="$SAGE_COMOON_CFLAGS"

That I believe will be safe. No package is forced to use my flags, but they can choose to. Hence I believe the changes to sage-env will be 100% safe, as they will not change any commonly used environment variables. 

So that's what I intend to do with sage-env. Now to the specific of this package. 

Prior to writing this new package, I looked at Python's spkg-install to see how the 64-bit build has been enabled on OS X, and you can see it added -m64 to gcc, so "gcc -m64" was used as a compiler. Hence I basically used a similar method. 

Having later looked more carefully at the python documentation, the way to pass flags is not the way it is done on the spkg-install for OS X, so whist it may work, it is not the right way to do it. 

I think the best solution is that I update sage-env, then update the python package, but in a way that is specific to Solaris, AIX and HP-UX. Then at a later date, we can try in an alpha0 to drop it in without it being specific to that platform. 

I think the ability to allow the user to pass their own flags is quite important, as they can use that to optimise gcc for thier processor. At the momemnt, 95% of Sage's code is being built for a generic processor, and not exploiting the features of anyones particular processor. 

So let me update sage-env in a safe way, then update this, to make use of sage-env's changes, but only on some rarer platforms. 

I think in the short term, Jaap should not worry about setting CFLAGS globally if it allows a package to build. Progress can then be made. He can always break the build process manually at some point, and unset it, just before cython gets to work. 

Leave it with me. I'll make what I believe are sensible decisions, then others can comment of course. In the mean time, I'm happy with this not being merged just now. I do agree it is sub-optimal. 

Dave



---

archive/issue_comments_066732.json:
```json
{
    "body": "Replying to [comment:18 drkirkby]:\n> I can understand why this was not merged. I'm just in the process of updating #7818. I just need to double check everything. But the main change is that \n\nGreat. \n\n> Prior to writing this new package, I looked at Python's spkg-install to see how the 64-bit build has been enabled on OS X, and you can see it added -m64 to gcc, so \"gcc -m64\" was used as a compiler. Hence I basically used a similar method. \n\nAh, OK. For easy reference: \n\n\n```\n    if [ `uname` = \"Darwin\" ]; then\n        if [ \"$SAGE64\" = \"yes\" ]; then\n            echo \"64 bit OSX build enabled\"\n            OPT=\"-g -O3 -m64 -Wall -Wstrict-prototypes\"; export OPT\n            ./configure $EXTRAFLAGS --prefix=\"$SAGE_LOCAL\" --without-libpng \\\n\t    --enable-unicode=ucs4 --with-gcc=\"gcc -m64\" --disable-toolbox-glue\n        else\n            ./configure $EXTRAFLAGS --prefix=\"$SAGE_LOCAL\" --without-libpng \\\n\t    --enable-unicode=ucs4 --disable-toolbox-glue\n        fi\n    else\n        ./configure $EXTRAFLAGS --prefix=\"$SAGE_LOCAL\" --without-libpng --enable-unicode=ucs4 CC=\"$CC $CFLAGS\" CXX=\"$CXX $CXXFLAGS\"\n    fi\n```\n\n\nInterestingly, -m64 gets added to both OPT (used by Python and distutils in making CFLAGS) and gcc. I wonder if both are necessary, or if this is redundant (yielding two -m65s in the final command, which shouldn't hurt). In any case, hopefully we can do this in such a way that all the spkg-installs that are just \"python setup.py install\" won't have to have extra stuff added in there as well.",
    "created_at": "2010-01-30T05:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66732",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:18 drkirkby]:
> I can understand why this was not merged. I'm just in the process of updating #7818. I just need to double check everything. But the main change is that 

Great. 

> Prior to writing this new package, I looked at Python's spkg-install to see how the 64-bit build has been enabled on OS X, and you can see it added -m64 to gcc, so "gcc -m64" was used as a compiler. Hence I basically used a similar method. 

Ah, OK. For easy reference: 


```
    if [ `uname` = "Darwin" ]; then
        if [ "$SAGE64" = "yes" ]; then
            echo "64 bit OSX build enabled"
            OPT="-g -O3 -m64 -Wall -Wstrict-prototypes"; export OPT
            ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng \
	    --enable-unicode=ucs4 --with-gcc="gcc -m64" --disable-toolbox-glue
        else
            ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng \
	    --enable-unicode=ucs4 --disable-toolbox-glue
        fi
    else
        ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng --enable-unicode=ucs4 CC="$CC $CFLAGS" CXX="$CXX $CXXFLAGS"
    fi
```


Interestingly, -m64 gets added to both OPT (used by Python and distutils in making CFLAGS) and gcc. I wonder if both are necessary, or if this is redundant (yielding two -m65s in the final command, which shouldn't hurt). In any case, hopefully we can do this in such a way that all the spkg-installs that are just "python setup.py install" won't have to have extra stuff added in there as well.



---

archive/issue_comments_066733.json:
```json
{
    "body": "As a work around I changed Darwin to SunOS. This give a working cython!\n\nChecking other packages with python setup.py install.\n\nJaap",
    "created_at": "2010-01-30T12:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66733",
    "user": "https://github.com/jaapspies"
}
```

As a work around I changed Darwin to SunOS. This give a working cython!

Checking other packages with python setup.py install.

Jaap



---

archive/issue_comments_066734.json:
```json
{
    "body": "That seems fine. Whatever allows you to make progress. Specific issues can be sorted later. There are some quite interesting, and more complex tasks, such as #6028 to be solved. You might want to take a look at something more interesting, if you get fed up with adding -m64!\n\nDave",
    "created_at": "2010-01-30T13:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66734",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That seems fine. Whatever allows you to make progress. Specific issues can be sorted later. There are some quite interesting, and more complex tasks, such as #6028 to be solved. You might want to take a look at something more interesting, if you get fed up with adding -m64!

Dave



---

archive/issue_comments_066735.json:
```json
{
    "body": "Attachment [python-2.6.4.p6.patch](tarball://root/attachments/some-uuid/ticket7761/python-2.6.4.p6.patch) by @jaapspies created at 2010-02-23 14:33:49\n\nMade a new spkg work on Open nSolaris, leaving the OSX solution as is.\n\n[http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg)\n\nSee also the patch:\n[http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.patch](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.patch)\n\nOn 'hawk':\n\n\n```\n(cd /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin; ln python2.6 python)\nrm -f /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin/python-config\n(cd /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin; ln -s python2.6-config python-config)\n/usr/bin/ginstall -c -m 644 ./Misc/python.man \\\n                /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/share/man/man1/python.1\nSleeping for three seconds before testing python\nhashlib module imported\n/export/home/jaap/sage_port/sage-4.3.2.alpha1\n\n```\n\n\nBig question: does this work for Solaris 10?\n\nJaap",
    "created_at": "2010-02-23T14:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66735",
    "user": "https://github.com/jaapspies"
}
```

Attachment [python-2.6.4.p6.patch](tarball://root/attachments/some-uuid/ticket7761/python-2.6.4.p6.patch) by @jaapspies created at 2010-02-23 14:33:49

Made a new spkg work on Open nSolaris, leaving the OSX solution as is.

[http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg)

See also the patch:
[http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.patch](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.patch)

On 'hawk':


```
(cd /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin; ln python2.6 python)
rm -f /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin/python-config
(cd /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin; ln -s python2.6-config python-config)
/usr/bin/ginstall -c -m 644 ./Misc/python.man \
                /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/share/man/man1/python.1
Sleeping for three seconds before testing python
hashlib module imported
/export/home/jaap/sage_port/sage-4.3.2.alpha1

```


Big question: does this work for Solaris 10?

Jaap



---

archive/issue_comments_066736.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-23T14:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66736",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066737.json:
```json
{
    "body": "I see no reason this should not work on Linux, but have you checked it? I know  you have a linux build of Sage. Assuming you have checked it on Linux, then I'm happy to give it a positive review. It looks fine to me. \n\nIt does build on Solaris 10 in 32-bit mode on SPARC. I've not tested 64-bit mode, but there is currently no effort being put into a 64-bit port on SPARC, so there is no need for it to work there. \n\nPositive review, subject to confirmation from you that  you have tested this on Linux. \n\nDave",
    "created_at": "2010-02-23T17:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66737",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I see no reason this should not work on Linux, but have you checked it? I know  you have a linux build of Sage. Assuming you have checked it on Linux, then I'm happy to give it a positive review. It looks fine to me. 

It does build on Solaris 10 in 32-bit mode on SPARC. I've not tested 64-bit mode, but there is currently no effort being put into a 64-bit port on SPARC, so there is no need for it to work there. 

Positive review, subject to confirmation from you that  you have tested this on Linux. 

Dave



---

archive/issue_comments_066738.json:
```json
{
    "body": "Replying to [comment:23 drkirkby]:\n> I see no reason this should not work on Linux, but have you checked it? I know  you have a linux build of Sage. Assuming you have checked it on Linux, then I'm happy to give it a positive review. It looks fine to me. \n> \n> It does build on Solaris 10 in 32-bit mode on SPARC. I've not tested 64-bit mode, but there is currently no effort being put into a 64-bit port on SPARC, so there is no need for it to work there. \n> \n> Positive review, subject to confirmation from you that  you have tested this on Linux. \n> \n> Dave \n\n\nSure, I tested this on linux. But the change in spkg-install only affected SunOS. So\nI was not afraid it would break a linux build.\n\nJaap",
    "created_at": "2010-02-23T17:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66738",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:23 drkirkby]:
> I see no reason this should not work on Linux, but have you checked it? I know  you have a linux build of Sage. Assuming you have checked it on Linux, then I'm happy to give it a positive review. It looks fine to me. 
> 
> It does build on Solaris 10 in 32-bit mode on SPARC. I've not tested 64-bit mode, but there is currently no effort being put into a 64-bit port on SPARC, so there is no need for it to work there. 
> 
> Positive review, subject to confirmation from you that  you have tested this on Linux. 
> 
> Dave 


Sure, I tested this on linux. But the change in spkg-install only affected SunOS. So
I was not afraid it would break a linux build.

Jaap



---

archive/issue_comments_066739.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-23T18:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66739",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066740.json:
```json
{
    "body": "No problem. I think it would be ok, but there is no harm in checking. \n\nPositive review.",
    "created_at": "2010-02-23T18:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66740",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

No problem. I think it would be ok, but there is no harm in checking. 

Positive review.



---

archive/issue_comments_066741.json:
```json
{
    "body": "I'm taking myself off this as author, and adding myself as reviewer, as these changes by Jaap are his, and my earlier version was not working completely, so I feel justified in reviewing this. \n\nI'm going to delete the version I have on boxen, so not to cause any confusion. \n\nDave",
    "created_at": "2010-02-23T18:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66741",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm taking myself off this as author, and adding myself as reviewer, as these changes by Jaap are his, and my earlier version was not working completely, so I feel justified in reviewing this. 

I'm going to delete the version I have on boxen, so not to cause any confusion. 

Dave



---

archive/issue_comments_066742.json:
```json
{
    "body": "I see this ticket is marked as: Ticket #7761 (positive_review defect: fixed)\n\nFixed? At some time it was merged, but reopened.\n\nJaap",
    "created_at": "2010-02-23T18:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66742",
    "user": "https://github.com/jaapspies"
}
```

I see this ticket is marked as: Ticket #7761 (positive_review defect: fixed)

Fixed? At some time it was merged, but reopened.

Jaap



---

archive/issue_comments_066743.json:
```json
{
    "body": "Remove assignee drkirkby.",
    "created_at": "2010-02-23T20:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66743",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Remove assignee drkirkby.



---

archive/issue_comments_066744.json:
```json
{
    "body": "Yes, it got merged, but was changed by robertwb  from fixed to needs work. It relied on another patch (#7818) which itself caused problems by setting CFLAGS globally. So whilst my python version worked, the patch it relied on caused other problems. \n\nDave",
    "created_at": "2010-02-23T20:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66744",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Yes, it got merged, but was changed by robertwb  from fixed to needs work. It relied on another patch (#7818) which itself caused problems by setting CFLAGS globally. So whilst my python version worked, the patch it relied on caused other problems. 

Dave



---

archive/issue_comments_066745.json:
```json
{
    "body": "Merged [python-2.6.4.p6.spkg](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg) in the standard spkg repository.",
    "created_at": "2010-03-02T23:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7761#issuecomment-66745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [python-2.6.4.p6.spkg](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg) in the standard spkg repository.



---

archive/issue_events_007977.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T23:31:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7761",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7761#event-7977"
}
```
