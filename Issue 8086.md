# Issue 8086: numpy fails to build on Open Solaris x64 - 32 / 64-bit mixup

archive/issues_008086.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)\n* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.\n* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. \n## The problem\nnumpy is failing to build. It looks like there is a mix of 32 and 64-bit objects. \n\n\n\n```\nnumpy-1.3.0.p2/src/setup.py\nnumpy-1.3.0.p2/src/MANIFEST.in\nnumpy-1.3.0.p2/.hgtags\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_111b i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.3.4 (GCC) \n****************************************************\nRunning from numpy source directory.\nF2PY Version 2\nblas_opt_info:\nblas_mkl_info:\n  libraries mkl,vml,guide not found in /export/home/drkirkby/sage-4.3.1/local/lib\n  NOT AVAILABLE\n\natlas_blas_threads_info:\nSetting PTATLAS=ATLAS\n  libraries ptf77blas,ptcblas,atlas not found in /export/home/drkirkby/sage-4.3.1/local/lib\n  NOT AVAILABLE\n\natlas_blas_info:\n  FOUND:\n    libraries = ['f77blas', 'cblas', 'atlas']\n    library_dirs = ['/export/home/drkirkby/sage-4.3.1/local/lib']\n    language = c\n    include_dirs = ['/export/home/drkirkby/sage-4.3.1/local/include']\n\n/export/home/drkirkby/sage-4.3.1/spkg/build/numpy-1.3.0.p2/src/numpy/distutils/command/config.py:361: DeprecationWarning: \n+++++++++++++++++++++++++++++++++++++++++++++++++\nUsage of get_output is deprecated: please do not \nuse it anymore, and avoid configuration checks \ninvolving running executable on the target machine.\n+++++++++++++++++++++++++++++++++++++++++++++++++\n\n  DeprecationWarning)\ncustomize Sage_FCompiler_1\ncustomize Sage_FCompiler_1\ncustomize Sage_FCompiler_1 using config\ncompiling '_configtest.c':\n\n/* This file is generated from numpy/distutils/system_info.py */\nvoid ATL_buildinfo(void);\nint main(void) {\n  ATL_buildinfo();\n  return 0;\n}\nC compiler: gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC\n\ncompile options: '-c'\ngcc: _configtest.c\ngcc _configtest.o -L/export/home/drkirkby/sage-4.3.1/local/lib -lf77blas -lcblas -latlas -o _configtest\nld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libf77blas.so: wrong ELF class: ELFCLASS64\nld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libcblas.so: wrong ELF class: ELFCLASS64\nld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libatlas.so: wrong ELF class: ELFCLASS64\nld: fatal: file processing errors. No output written to _configtest\ncollect2: ld returned 1 exit status\nld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libf77blas.so: wrong ELF class: ELFCLASS64\nld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libcblas.so: wrong ELF class: ELFCLASS64\nld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libatlas.so: wrong ELF class: ELFCLASS64\nld: fatal: file processing errors. No output written to _configtest\ncollect2: ld returned 1 exit status\nfailure.\nremoving: _configtest.c _configtest.o\nStatus: 255\nOutput: \n  FOUND:\n    libraries = ['f77blas', 'cblas', 'atlas']\n    library_dirs = ['/export/home/drkirkby/sage-4.3.1/local/lib']\n    language = c\n    define_macros = [('NO_ATLAS_INFO', 2)]\n    include_dirs = ['/export/home/drkirkby/sage-4.3.1/local/include']\n\nlapack_opt_info:\nlapack_mkl_info:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8086\n\n",
    "created_at": "2010-01-27T03:35:29Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "numpy fails to build on Open Solaris x64 - 32 / 64-bit mixup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8086",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies

## Build environment
* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
* OpenSolaris 2009.06 snv_111b X86
* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 
## The problem
numpy is failing to build. It looks like there is a mix of 32 and 64-bit objects. 



```
numpy-1.3.0.p2/src/setup.py
numpy-1.3.0.p2/src/MANIFEST.in
numpy-1.3.0.p2/.hgtags
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_111b i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
Running from numpy source directory.
F2PY Version 2
blas_opt_info:
blas_mkl_info:
  libraries mkl,vml,guide not found in /export/home/drkirkby/sage-4.3.1/local/lib
  NOT AVAILABLE

atlas_blas_threads_info:
Setting PTATLAS=ATLAS
  libraries ptf77blas,ptcblas,atlas not found in /export/home/drkirkby/sage-4.3.1/local/lib
  NOT AVAILABLE

atlas_blas_info:
  FOUND:
    libraries = ['f77blas', 'cblas', 'atlas']
    library_dirs = ['/export/home/drkirkby/sage-4.3.1/local/lib']
    language = c
    include_dirs = ['/export/home/drkirkby/sage-4.3.1/local/include']

/export/home/drkirkby/sage-4.3.1/spkg/build/numpy-1.3.0.p2/src/numpy/distutils/command/config.py:361: DeprecationWarning: 
+++++++++++++++++++++++++++++++++++++++++++++++++
Usage of get_output is deprecated: please do not 
use it anymore, and avoid configuration checks 
involving running executable on the target machine.
+++++++++++++++++++++++++++++++++++++++++++++++++

  DeprecationWarning)
customize Sage_FCompiler_1
customize Sage_FCompiler_1
customize Sage_FCompiler_1 using config
compiling '_configtest.c':

/* This file is generated from numpy/distutils/system_info.py */
void ATL_buildinfo(void);
int main(void) {
  ATL_buildinfo();
  return 0;
}
C compiler: gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC

compile options: '-c'
gcc: _configtest.c
gcc _configtest.o -L/export/home/drkirkby/sage-4.3.1/local/lib -lf77blas -lcblas -latlas -o _configtest
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libf77blas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libcblas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libatlas.so: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to _configtest
collect2: ld returned 1 exit status
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libf77blas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libcblas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libatlas.so: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to _configtest
collect2: ld returned 1 exit status
failure.
removing: _configtest.c _configtest.o
Status: 255
Output: 
  FOUND:
    libraries = ['f77blas', 'cblas', 'atlas']
    library_dirs = ['/export/home/drkirkby/sage-4.3.1/local/lib']
    language = c
    define_macros = [('NO_ATLAS_INFO', 2)]
    include_dirs = ['/export/home/drkirkby/sage-4.3.1/local/include']

lapack_opt_info:
lapack_mkl_info:
```


Issue created by migration from https://trac.sagemath.org/ticket/8086





---

archive/issue_comments_070855.json:
```json
{
    "body": "I do have a working numpy on your machine.\n\nThere is a numpy-1.3.0.p3.spkg in trac waiting to be merged.\n\nHere is a pre version of mine:\nhttp://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg\n\nWorks on Open Solaris.\n\nJaap",
    "created_at": "2010-01-27T10:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70855",
    "user": "@jaapspies"
}
```

I do have a working numpy on your machine.

There is a numpy-1.3.0.p3.spkg in trac waiting to be merged.

Here is a pre version of mine:
http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg

Works on Open Solaris.

Jaap



---

archive/issue_comments_070856.json:
```json
{
    "body": "Added patch file and updated spkg:\n\n[http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg)\n\nJaap",
    "created_at": "2010-01-27T15:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70856",
    "user": "@jaapspies"
}
```

Added patch file and updated spkg:

[http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg)

Jaap



---

archive/issue_comments_070857.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-27T15:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70857",
    "user": "@jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070858.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-05-30T16:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70858",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_070859.json:
```json
{
    "body": "Hi Jaap,\n\nI'm having a problem with this. I got a message about \"could not fork\". I even rebooted the machine once, thinking something was wrong, but everything else seems to work. \n\n\nIs this bit of code in the patch right? It looks wrong to me:\n\n\n```\necho \"#! /usr/bin/env bash\" > gcc \necho \"`which gcc` -m64 \" | sed 's/$/\\$@/' >> fake_gcc \n```\n\n\nShould the first line not write to the file 'fake_gcc' rather than 'gcc'? If so, since it gets copied to $SAGE_LOCAL/bin/gcc, why not write it directly there? \n\ni.e.\n\n\n```\necho \"#! /usr/bin/env bash\" > $SAGE_LOCAL/bin/gcc\necho \"`which gcc` -m64 \" | sed 's/$/\\$@/' >> $SAGE_LOCAL/bin/gcc \n```\n\n\nAlso, why use 'sed'? If I understand your intentions correctly, \n\n\n```\necho \"`which gcc` -m64 \\$@\"\n```\n\n\nwould achieve the same, but without invoking 'sed'. \n\nI would also add that 'which' is not a POSIX command, whereas 'command -v' gives you the same information, but in a standards complient way. This can be important, especially on Solaris 10, as the return code of 'which' is undefined on there. \n\n\n```\ndrkirkby@hawk:~$ echo \"`command -v gcc` -m64 \\$@\" \n/usr/local/gcc-4.4.4/bin/gcc -m64 $@\n```\n\n\nis more portable. \n\nHowever, I can't seem to get it to work. I'm not sure if I understand exactly what you are aiming to do here. Why do we need a fake gcc? \n\nDave",
    "created_at": "2010-05-30T16:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70859",
    "user": "drkirkby"
}
```

Hi Jaap,

I'm having a problem with this. I got a message about "could not fork". I even rebooted the machine once, thinking something was wrong, but everything else seems to work. 


Is this bit of code in the patch right? It looks wrong to me:


```
echo "#! /usr/bin/env bash" > gcc 
echo "`which gcc` -m64 " | sed 's/$/\$@/' >> fake_gcc 
```


Should the first line not write to the file 'fake_gcc' rather than 'gcc'? If so, since it gets copied to $SAGE_LOCAL/bin/gcc, why not write it directly there? 

i.e.


```
echo "#! /usr/bin/env bash" > $SAGE_LOCAL/bin/gcc
echo "`which gcc` -m64 " | sed 's/$/\$@/' >> $SAGE_LOCAL/bin/gcc 
```


Also, why use 'sed'? If I understand your intentions correctly, 


```
echo "`which gcc` -m64 \$@"
```


would achieve the same, but without invoking 'sed'. 

I would also add that 'which' is not a POSIX command, whereas 'command -v' gives you the same information, but in a standards complient way. This can be important, especially on Solaris 10, as the return code of 'which' is undefined on there. 


```
drkirkby@hawk:~$ echo "`command -v gcc` -m64 \$@" 
/usr/local/gcc-4.4.4/bin/gcc -m64 $@
```


is more portable. 

However, I can't seem to get it to work. I'm not sure if I understand exactly what you are aiming to do here. Why do we need a fake gcc? 

Dave



---

archive/issue_comments_070860.json:
```json
{
    "body": "Jaap, \n\nI can't get your patch to work, so have reimplemented this. I've completely removed the file fake_gcc from Numpy, and instead create the fake file dynamically with the correct path. \n\nI've also reported the issue to the Numpy bug database. \n\nhttp://projects.scipy.org/numpy/ticket/1525\n\nwhich should have been done years ago when the problem was first realised in OS X. \n\nHere's a package waiting for review, which I believe does fix the problem. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg\n\nDave",
    "created_at": "2010-06-28T08:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70860",
    "user": "drkirkby"
}
```

Jaap, 

I can't get your patch to work, so have reimplemented this. I've completely removed the file fake_gcc from Numpy, and instead create the fake file dynamically with the correct path. 

I've also reported the issue to the Numpy bug database. 

http://projects.scipy.org/numpy/ticket/1525

which should have been done years ago when the problem was first realised in OS X. 

Here's a package waiting for review, which I believe does fix the problem. 

http://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg

Dave



---

archive/issue_comments_070861.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-06-28T08:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70861",
    "user": "drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_070862.json:
```json
{
    "body": "## Great news\n\nI've found a much simpler solution to this, which totally avoids using any fake gcc files. Just compile with\n\nCC=\"gcc -m64\"\nexport CC\n\nand it works! I will attach a simpler patch in 15 minutes. I'm marking as \"needs work\" for now, as I need to do something else just now. \n\nDave",
    "created_at": "2010-07-30T09:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70862",
    "user": "drkirkby"
}
```

## Great news

I've found a much simpler solution to this, which totally avoids using any fake gcc files. Just compile with

CC="gcc -m64"
export CC

and it works! I will attach a simpler patch in 15 minutes. I'm marking as "needs work" for now, as I need to do something else just now. 

Dave



---

archive/issue_comments_070863.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-30T09:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70863",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070864.json:
```json
{
    "body": "Attachment [8086.patch](tarball://root/attachments/some-uuid/ticket8086/8086.patch) by drkirkby created at 2010-07-30 09:34:27\n\nMercurial patch which solves the Numpy build issues without any sort of hack. I think this would work on OS X too, but I'm not changing the OS X code now.",
    "created_at": "2010-07-30T09:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70864",
    "user": "drkirkby"
}
```

Attachment [8086.patch](tarball://root/attachments/some-uuid/ticket8086/8086.patch) by drkirkby created at 2010-07-30 09:34:27

Mercurial patch which solves the Numpy build issues without any sort of hack. I think this would work on OS X too, but I'm not changing the OS X code now.



---

archive/issue_comments_070865.json:
```json
{
    "body": "Here's the updated package. I believe this is a decent fix (at last). \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg\n\nI've reported this upstream \n\nhttp://projects.scipy.org/numpy/ticket/1525\n\nDave",
    "created_at": "2010-07-30T09:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70865",
    "user": "drkirkby"
}
```

Here's the updated package. I believe this is a decent fix (at last). 

http://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg

I've reported this upstream 

http://projects.scipy.org/numpy/ticket/1525

Dave



---

archive/issue_comments_070866.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-30T09:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70866",
    "user": "drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070867.json:
```json
{
    "body": "The changes look good.  The spkg builds on a number of different machines, both 32-bit and 64-bit, and doctests pass.\n\nBy the way, with the old spkg, numpy didn't build properly on 64-bit Solaris (either sparc -- t2 -- or x86 -- fulvia), so it's not exclusively an OpenSolaris issue.  With the new spkg, it works on fulvia.  I haven't gotten t2 (with SAGE64='yes') to build the prerequisite packages yet.  I'm working on that, and if there are issues building numpy, I'll revert the positive review.\n\n(Tested on t2 (32-bit), mark2 (32-bit), Mac OS X 10.6 (64-bit), sage.math (both with SAGE64='yes' and with SAGE64 unset), taurus (both with SAGE64='yes' and SAGE64 unset), cicero (32-bit), fulvia (both settings for SAGE64), and iras (64-bit machine? but with SAGE64 unset).)",
    "created_at": "2010-08-03T21:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70867",
    "user": "@jhpalmieri"
}
```

The changes look good.  The spkg builds on a number of different machines, both 32-bit and 64-bit, and doctests pass.

By the way, with the old spkg, numpy didn't build properly on 64-bit Solaris (either sparc -- t2 -- or x86 -- fulvia), so it's not exclusively an OpenSolaris issue.  With the new spkg, it works on fulvia.  I haven't gotten t2 (with SAGE64='yes') to build the prerequisite packages yet.  I'm working on that, and if there are issues building numpy, I'll revert the positive review.

(Tested on t2 (32-bit), mark2 (32-bit), Mac OS X 10.6 (64-bit), sage.math (both with SAGE64='yes' and with SAGE64 unset), taurus (both with SAGE64='yes' and SAGE64 unset), cicero (32-bit), fulvia (both settings for SAGE64), and iras (64-bit machine? but with SAGE64 unset).)



---

archive/issue_comments_070868.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-03T21:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70868",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070869.json:
```json
{
    "body": "## Note to the release manager\n\nAll changes are committed in the repository of the .spkg file. No library changes need to be made. Just drop in \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg",
    "created_at": "2010-08-07T22:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70869",
    "user": "drkirkby"
}
```

## Note to the release manager

All changes are committed in the repository of the .spkg file. No library changes need to be made. Just drop in 

http://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg



---

archive/issue_comments_070870.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8086#issuecomment-70870",
    "user": "@qed777"
}
```

Resolution: fixed
