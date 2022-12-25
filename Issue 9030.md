# Issue 9030: rubiks is building part 32-bit and part 64-bit on OpenSolaris x64.

archive/issues_009030.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jaapspies\n\n'rubiks' has code to attempt to build it 64-bit, but that does not seem to be fully functional, as parts are built 32-bit and parts are built 64-bit. \n\n```\nrubiks-20070912.p10/dist/debian/changelog\nrubiks-20070912.p10/spkg-install\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC) \n****************************************************\nBuilding a 64-bit version of rubiks\nCode will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.\nUsing CC=gcc\nUsing CXX=g++\nUsing FC=\nUsing F77=\nUsing SAGE_FORTRAN=/usr/local/gcc-4.4.4/bin/gfortran\nUsing SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.4/lib/amd64/libgfortran.so\nThe following environment variables will be exported\nUsing CFLAGS= -O2  -m64  -g  -Wall \nUsing CXXFLAGS= -O2  -m64  -g  -Wall \nUsing FCFLAGS= -O2  -m64  -g  -Wall \nUsing F77FLAGS= -O2  -m64  -g  -Wall \nUsing CPPFLAGS=\nUsing LDFLAGS= -m64 \nUsing ABI=\nconfigure scripts and/or makefiles might override these later\n \nBuilding Rubiks cube solvers\nfor dir in dietz/cu2 dietz/mcube dietz/solver dik reid; do \\\n\t\t(cd ${dir} && make all)\\\n\tdone\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.4.2/spkg/build/rubiks-20070912.p10/src/dietz/cu2'\ng++  -O2  -m64  -g  -Wall  -c cu2.cpp\ng++  -O2  -m64  -g  -Wall  -c main.cpp\ng++  -O2  -m64  -g  -Wall   -o cubex  cubex.o main.o\n<snip lots of 64-bit builds builds and lots of warnings>\ngcc  -O2  -m64  -g  -Wall    -m64   optimal.c   -o optimal\ngcc  -O2  -m64  -g  -Wall    -m64   twist.c   -o twist\n<snip>\ncp reid/optimal /export/home/drkirkby/sage-4.4.2/local/bin\ncp dietz/solver/cubex /export/home/drkirkby/sage-4.4.2/local/bin\ncp dietz/mcube/mcube /export/home/drkirkby/sage-4.4.2/local/bin\ncp dietz/cu2/cu2 /export/home/drkirkby/sage-4.4.2/local/bin\ncp dik/dikcube /export/home/drkirkby/sage-4.4.2/local/bin\ncp dik/size222 /export/home/drkirkby/sage-4.4.2/local/bin\n```\n\nWhen we check files, I note some are built 32-bit and some are built 64-bit. \n\n```\ndrkirkby@hawk:~/sage-4.4.2$ file local/bin/size222 \nlocal/bin/size222:\tELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available\ndrkirkby@hawk:~/sage-4.4.2$ file local/bin/optimal\nlocal/bin/optimal:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\n```\n\nI expect this would happen on any platform where the default is 32-bit, suggesting to me this never even worked 64-bit on OS X systems where 32-bit was the default. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9030\n\n",
    "created_at": "2010-05-24T07:52:15Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "rubiks is building part 32-bit and part 64-bit on OpenSolaris x64.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9030",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @aghitza

CC:  @jaapspies

'rubiks' has code to attempt to build it 64-bit, but that does not seem to be fully functional, as parts are built 32-bit and parts are built 64-bit. 

```
rubiks-20070912.p10/dist/debian/changelog
rubiks-20070912.p10/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
****************************************************
Building a 64-bit version of rubiks
Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.
Using CC=gcc
Using CXX=g++
Using FC=
Using F77=
Using SAGE_FORTRAN=/usr/local/gcc-4.4.4/bin/gfortran
Using SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.4/lib/amd64/libgfortran.so
The following environment variables will be exported
Using CFLAGS= -O2  -m64  -g  -Wall 
Using CXXFLAGS= -O2  -m64  -g  -Wall 
Using FCFLAGS= -O2  -m64  -g  -Wall 
Using F77FLAGS= -O2  -m64  -g  -Wall 
Using CPPFLAGS=
Using LDFLAGS= -m64 
Using ABI=
configure scripts and/or makefiles might override these later
 
Building Rubiks cube solvers
for dir in dietz/cu2 dietz/mcube dietz/solver dik reid; do \
		(cd ${dir} && make all)\
	done
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.2/spkg/build/rubiks-20070912.p10/src/dietz/cu2'
g++  -O2  -m64  -g  -Wall  -c cu2.cpp
g++  -O2  -m64  -g  -Wall  -c main.cpp
g++  -O2  -m64  -g  -Wall   -o cubex  cubex.o main.o
<snip lots of 64-bit builds builds and lots of warnings>
gcc  -O2  -m64  -g  -Wall    -m64   optimal.c   -o optimal
gcc  -O2  -m64  -g  -Wall    -m64   twist.c   -o twist
<snip>
cp reid/optimal /export/home/drkirkby/sage-4.4.2/local/bin
cp dietz/solver/cubex /export/home/drkirkby/sage-4.4.2/local/bin
cp dietz/mcube/mcube /export/home/drkirkby/sage-4.4.2/local/bin
cp dietz/cu2/cu2 /export/home/drkirkby/sage-4.4.2/local/bin
cp dik/dikcube /export/home/drkirkby/sage-4.4.2/local/bin
cp dik/size222 /export/home/drkirkby/sage-4.4.2/local/bin
```

When we check files, I note some are built 32-bit and some are built 64-bit. 

```
drkirkby@hawk:~/sage-4.4.2$ file local/bin/size222 
local/bin/size222:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available
drkirkby@hawk:~/sage-4.4.2$ file local/bin/optimal
local/bin/optimal:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
```

I expect this would happen on any platform where the default is 32-bit, suggesting to me this never even worked 64-bit on OS X systems where 32-bit was the default. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9030





---

archive/issue_comments_083434.json:
```json
{
    "body": "Changing assignee from @aghitza to drkirkby.",
    "created_at": "2010-05-24T18:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83434",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from @aghitza to drkirkby.



---

archive/issue_comments_083435.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2010-05-24T18:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83435",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_comments_083436.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83436",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083437.json:
```json
{
    "body": "As this is never linked in directly, there is no need (or advantage, as far as I can tell) to build this 64-bit for a fully functional Sage.",
    "created_at": "2010-05-25T05:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83437",
    "user": "https://github.com/robertwb"
}
```

As this is never linked in directly, there is no need (or advantage, as far as I can tell) to build this 64-bit for a fully functional Sage.



---

archive/issue_events_022097.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-05-25T14:57:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9030#event-22097"
}
```



---

archive/issue_comments_083438.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> As this is never linked in directly, there is no need (or advantage, as far as I can tell) to build this 64-bit for a fully functional Sage. \n\n\nI agree there is no technical advantage in using rubiks 64-bit. \n\nHowever, it seems rather unprofessional to have 4 out of the 6 binaries building 64-bit, and two of them building 32-bit. Having all rubiks binaries made 64-bit allows one to quickly find any binaries from any packages that are not being built properly, using a command like\n\n```\n$ find local -exec file {} \\; | grep 32-bit\n```\n\nas such, I believe it's desirable that a 64-bit build on OpenSolaris, Solaris or any other operating system for that matter creates only 64-bit objects.\n\nA revised package, which add the -m64 flag to the makefile is at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/rubiks-20070912.p11.spkg\n\nThere were a lot of files not in the repository (I believe this was my fault months ago), which I've checked in. As such, the patch is a lot longer than it needs to be to fix this particular problem. \n\nThe following line:\n\n```\nCFLAGS = -O -DLARGE_MEM -DVERBOSE\n```\ngets be changed to:\n\n```\nCFLAGS = ${CFLAG64} -O -DLARGE_MEM -DVERBOSE\n```\n\nusing 'sed'. \n\n$CFLAG64 is then set to -m64 if building 64-bit, so the -m64 gets added to the makefile. \n\n\nAfter building **all** the rubiks binaries are 64-bit. i.e.\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ file local/bin/size222 \nlocal/bin/size222:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available\ndrkirkby@hawk:~/sage-4.4.2$ file local/bin/dikcube\nlocal/bin/dikcube:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available\n```\n\nPreviously both were being built 32-bit (see the output of the find command shown above, where clearly there was a mix of 32-bit and 64-bit objects). \n\nThis has been compiled on sage.math and bsd.math as well as my own Sun Ultra 27 running OpenSolaris. \n\nDave",
    "created_at": "2010-05-28T23:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83438",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:3 robertwb]:
> As this is never linked in directly, there is no need (or advantage, as far as I can tell) to build this 64-bit for a fully functional Sage. 


I agree there is no technical advantage in using rubiks 64-bit. 

However, it seems rather unprofessional to have 4 out of the 6 binaries building 64-bit, and two of them building 32-bit. Having all rubiks binaries made 64-bit allows one to quickly find any binaries from any packages that are not being built properly, using a command like

```
$ find local -exec file {} \; | grep 32-bit
```

as such, I believe it's desirable that a 64-bit build on OpenSolaris, Solaris or any other operating system for that matter creates only 64-bit objects.

A revised package, which add the -m64 flag to the makefile is at 

http://boxen.math.washington.edu/home/kirkby/patches/rubiks-20070912.p11.spkg

There were a lot of files not in the repository (I believe this was my fault months ago), which I've checked in. As such, the patch is a lot longer than it needs to be to fix this particular problem. 

The following line:

```
CFLAGS = -O -DLARGE_MEM -DVERBOSE
```
gets be changed to:

```
CFLAGS = ${CFLAG64} -O -DLARGE_MEM -DVERBOSE
```

using 'sed'. 

$CFLAG64 is then set to -m64 if building 64-bit, so the -m64 gets added to the makefile. 


After building **all** the rubiks binaries are 64-bit. i.e.

```
drkirkby@hawk:~/sage-4.4.2$ file local/bin/size222 
local/bin/size222:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
drkirkby@hawk:~/sage-4.4.2$ file local/bin/dikcube
local/bin/dikcube:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
```

Previously both were being built 32-bit (see the output of the find command shown above, where clearly there was a mix of 32-bit and 64-bit objects). 

This has been compiled on sage.math and bsd.math as well as my own Sun Ultra 27 running OpenSolaris. 

Dave



---

archive/issue_comments_083439.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-28T23:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83439",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083440.json:
```json
{
    "body": "Attachment [rubiks-64-bit.patch](tarball://root/attachments/some-uuid/ticket9030/rubiks-64-bit.patch) by drkirkby created at 2010-05-30 22:58:47\n\nMercurial patch to ensure all files build 64-bit on OpenSolaris",
    "created_at": "2010-05-30T22:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83440",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [rubiks-64-bit.patch](tarball://root/attachments/some-uuid/ticket9030/rubiks-64-bit.patch) by drkirkby created at 2010-05-30 22:58:47

Mercurial patch to ensure all files build 64-bit on OpenSolaris



---

archive/issue_comments_083441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T16:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83441",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083442.json:
```json
{
    "body": "Is ok for me. Positive review.\n\nJaap",
    "created_at": "2010-06-10T16:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83442",
    "user": "https://github.com/jaapspies"
}
```

Is ok for me. Positive review.

Jaap



---

archive/issue_events_022098.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-25T15:48:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9030#event-22098"
}
```



---

archive/issue_comments_083443.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9030#issuecomment-83443",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
