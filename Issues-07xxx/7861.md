# Issue 7861: pynac not building on Open Solaris x64 (32-bit/64-bit mixup)

archive/issues_007861.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @robertwb burchin @williamstein @jhpalmieri\n\n == Build environment ==\n* Sun Ultra 27 (Intel Xeon W3580 3.333 GHz, 12 GB RAM)\n* OpenSolaris 06/2009 updated to snv_134. \n* Sage 4.3.3 (with a few packages hacked to work on 64-bit)\n* gcc 4.4.4 configured with Sun linker and GNU assembler from binutils version 2.20.\n* 64-bit build (i.e. SAGE64 set to \"yes\")\n\n == Notes ==\nI'll decide whether to report this upstream once I get some feedback from others what it might be. \n\n == The problem ==\nI believe the pynac is building 64-bit (using 'find' and greping for 32-bit binaries, I find none of them), but it is probably trying to link to a 32-bit library. The error messages are below. \n\n```\npynac-0.2.0.p3/src/config.guess\npynac-0.2.0.p3/spkg-install\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\n****************************************************\n****************************************************\n<SNIP>\nmv -f .deps/remember.Tpo .deps/remember.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT pseries.lo -MD -MP -MF .deps/pseries.Tpo -c -o pseries.lo pseries.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT pseries.lo -MD -MP -MF .deps/pseries.Tpo -c pseries.cpp  -fPIC -DPIC -o .libs/pseries.o\nmv -f .deps/pseries.Tpo .deps/pseries.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT print.lo -MD -MP -MF .deps/print.Tpo -c -o print.lo print.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT print.lo -MD -MP -MF .deps/print.Tpo -c print.cpp  -fPIC -DPIC -o .libs/print.o\nmv -f .deps/print.Tpo .deps/print.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT symbol.lo -MD -MP -MF .deps/symbol.Tpo -c -o symbol.lo symbol.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT symbol.lo -MD -MP -MF .deps/symbol.Tpo -c symbol.cpp  -fPIC -DPIC -o .libs/symbol.o\nmv -f .deps/symbol.Tpo .deps/symbol.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT symmetry.lo -MD -MP -MF .deps/symmetry.Tpo -c -o symmetry.lo symmetry.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT symmetry.lo -MD -MP -MF .deps/symmetry.Tpo -c symmetry.cpp  -fPIC -DPIC -o .libs/symmetry.o\nmv -f .deps/symmetry.Tpo .deps/symmetry.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT tensor.lo -MD -MP -MF .deps/tensor.Tpo -c -o tensor.lo tensor.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT tensor.lo -MD -MP -MF .deps/tensor.Tpo -c tensor.cpp  -fPIC -DPIC -o .libs/tensor.o\nmv -f .deps/tensor.Tpo .deps/tensor.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c -o utils.lo utils.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c utils.cpp  -fPIC -DPIC -o .libs/utils.o\nmv -f .deps/utils.Tpo .deps/utils.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT wildcard.lo -MD -MP -MF .deps/wildcard.Tpo -c -o wildcard.lo wildcard.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT wildcard.lo -MD -MP -MF .deps/wildcard.Tpo -c wildcard.cpp  -fPIC -DPIC -o .libs/wildcard.o\nmv -f .deps/wildcard.Tpo .deps/wildcard.Plo\n/bin/sh ../libtool --tag=CXX   --mode=link g++  -m64 -O2 -g -version-info 0:0:0 -release 0.2 -m64 -o libpynac.la -rpath /export/home/drkirkby/sage-4.4.3/local/lib py_funcs.lo add.lo archive.lo basic.lo clifford.lo color.lo constant.lo ex.lo expair.lo expairseq.lo exprseq.lo fail.lo fderivative.lo function.lo idx.lo indexed.lo inifcns.lo inifcns_trans.lo inifcns_gamma.lo inifcns_nstdsums.lo integral.lo lst.lo matrix.lo mul.lo ncmul.lo normal.lo numeric.lo operators.lo power.lo registrar.lo relational.lo remember.lo pseries.lo print.lo symbol.lo symmetry.lo tensor.lo utils.lo wildcard.lo -L/export/home/drkirkby/sage-4.4.3/local/lib/python2.6/config -lpython2.6 -lsocket -lnsl -ldl\nlibtool: link: g++ -shared -nostdlib -m64 /usr/lib/crti.o /usr/lib/values-Xa.o /usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/crtbegin.o  .libs/py_funcs.o .libs/add.o .libs/archive.o .libs/basic.o .libs/clifford.o .libs/color.o .libs/constant.o .libs/ex.o .libs/expair.o .libs/expairseq.o .libs/exprseq.o .libs/fail.o .libs/fderivative.o .libs/function.o .libs/idx.o .libs/indexed.o .libs/inifcns.o .libs/inifcns_trans.o .libs/inifcns_gamma.o .libs/inifcns_nstdsums.o .libs/integral.o .libs/lst.o .libs/matrix.o .libs/mul.o .libs/ncmul.o .libs/normal.o .libs/numeric.o .libs/operators.o .libs/power.o .libs/registrar.o .libs/relational.o .libs/remember.o .libs/pseries.o .libs/print.o .libs/symbol.o .libs/symmetry.o .libs/tensor.o .libs/utils.o .libs/wildcard.o   -Wl,-R -Wl,/usr/local/gcc-4.4.4/lib -Wl,-R -Wl,/usr/local/gcc-4.4.4/lib -L/export/home/drkirkby/sage-4.4.3/local/lib/python2.6/config -lpython2.6 -lsocket -lnsl -ldl -L/export/home/drkirkby/sage-4.4.3/local/lib -L/usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4 -L/usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../.. /usr/local/gcc-4.4.4/lib/libstdc++.so -lm -lgcc_s /usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/crtend.o /usr/lib/crtn.o  -m64 -m64   -Wl,-h -Wl,libpynac-0.2.so.0 -o .libs/libpynac-0.2.so.0.0.0\nld: fatal: file .libs/py_funcs.o: wrong ELF class: ELFCLASS64\nld: fatal: file processing errors. No output written to .libs/libpynac-0.2.so.0.0.0\ncollect2: ld returned 1 exit status\nmake[4]: *** [libpynac.la] Error 1\nmake[4]: Leaving directory `/export/home/drkirkby/sage-4.4.3/spkg/build/pynac-0.2.0.p3/src/ginac'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/export/home/drkirkby/sage-4.4.3/spkg/build/pynac-0.2.0.p3/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.4.3/spkg/build/pynac-0.2.0.p3/src'\nError building pynac.\n\nreal 1m26.752s\nuser 1m19.837s\nsys 0m5.230s\nsage: An error occurred while installing pynac-0.2.0.p3\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7861\n\n",
    "closed_at": "2010-08-09T09:36:53Z",
    "created_at": "2010-01-06T23:05:53Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "pynac not building on Open Solaris x64 (32-bit/64-bit mixup)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7861",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @robertwb burchin @williamstein @jhpalmieri

 == Build environment ==
* Sun Ultra 27 (Intel Xeon W3580 3.333 GHz, 12 GB RAM)
* OpenSolaris 06/2009 updated to snv_134. 
* Sage 4.3.3 (with a few packages hacked to work on 64-bit)
* gcc 4.4.4 configured with Sun linker and GNU assembler from binutils version 2.20.
* 64-bit build (i.e. SAGE64 set to "yes")

 == Notes ==
I'll decide whether to report this upstream once I get some feedback from others what it might be. 

 == The problem ==
I believe the pynac is building 64-bit (using 'find' and greping for 32-bit binaries, I find none of them), but it is probably trying to link to a 32-bit library. The error messages are below. 

```
pynac-0.2.0.p3/src/config.guess
pynac-0.2.0.p3/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
<SNIP>
mv -f .deps/remember.Tpo .deps/remember.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT pseries.lo -MD -MP -MF .deps/pseries.Tpo -c -o pseries.lo pseries.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT pseries.lo -MD -MP -MF .deps/pseries.Tpo -c pseries.cpp  -fPIC -DPIC -o .libs/pseries.o
mv -f .deps/pseries.Tpo .deps/pseries.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT print.lo -MD -MP -MF .deps/print.Tpo -c -o print.lo print.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT print.lo -MD -MP -MF .deps/print.Tpo -c print.cpp  -fPIC -DPIC -o .libs/print.o
mv -f .deps/print.Tpo .deps/print.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT symbol.lo -MD -MP -MF .deps/symbol.Tpo -c -o symbol.lo symbol.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT symbol.lo -MD -MP -MF .deps/symbol.Tpo -c symbol.cpp  -fPIC -DPIC -o .libs/symbol.o
mv -f .deps/symbol.Tpo .deps/symbol.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT symmetry.lo -MD -MP -MF .deps/symmetry.Tpo -c -o symmetry.lo symmetry.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT symmetry.lo -MD -MP -MF .deps/symmetry.Tpo -c symmetry.cpp  -fPIC -DPIC -o .libs/symmetry.o
mv -f .deps/symmetry.Tpo .deps/symmetry.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT tensor.lo -MD -MP -MF .deps/tensor.Tpo -c -o tensor.lo tensor.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT tensor.lo -MD -MP -MF .deps/tensor.Tpo -c tensor.cpp  -fPIC -DPIC -o .libs/tensor.o
mv -f .deps/tensor.Tpo .deps/tensor.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c -o utils.lo utils.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c utils.cpp  -fPIC -DPIC -o .libs/utils.o
mv -f .deps/utils.Tpo .deps/utils.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC    -m64 -O2 -g -MT wildcard.lo -MD -MP -MF .deps/wildcard.Tpo -c -o wildcard.lo wildcard.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.4.3/local/include/python2.6 -fPIC -m64 -O2 -g -MT wildcard.lo -MD -MP -MF .deps/wildcard.Tpo -c wildcard.cpp  -fPIC -DPIC -o .libs/wildcard.o
mv -f .deps/wildcard.Tpo .deps/wildcard.Plo
/bin/sh ../libtool --tag=CXX   --mode=link g++  -m64 -O2 -g -version-info 0:0:0 -release 0.2 -m64 -o libpynac.la -rpath /export/home/drkirkby/sage-4.4.3/local/lib py_funcs.lo add.lo archive.lo basic.lo clifford.lo color.lo constant.lo ex.lo expair.lo expairseq.lo exprseq.lo fail.lo fderivative.lo function.lo idx.lo indexed.lo inifcns.lo inifcns_trans.lo inifcns_gamma.lo inifcns_nstdsums.lo integral.lo lst.lo matrix.lo mul.lo ncmul.lo normal.lo numeric.lo operators.lo power.lo registrar.lo relational.lo remember.lo pseries.lo print.lo symbol.lo symmetry.lo tensor.lo utils.lo wildcard.lo -L/export/home/drkirkby/sage-4.4.3/local/lib/python2.6/config -lpython2.6 -lsocket -lnsl -ldl
libtool: link: g++ -shared -nostdlib -m64 /usr/lib/crti.o /usr/lib/values-Xa.o /usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/crtbegin.o  .libs/py_funcs.o .libs/add.o .libs/archive.o .libs/basic.o .libs/clifford.o .libs/color.o .libs/constant.o .libs/ex.o .libs/expair.o .libs/expairseq.o .libs/exprseq.o .libs/fail.o .libs/fderivative.o .libs/function.o .libs/idx.o .libs/indexed.o .libs/inifcns.o .libs/inifcns_trans.o .libs/inifcns_gamma.o .libs/inifcns_nstdsums.o .libs/integral.o .libs/lst.o .libs/matrix.o .libs/mul.o .libs/ncmul.o .libs/normal.o .libs/numeric.o .libs/operators.o .libs/power.o .libs/registrar.o .libs/relational.o .libs/remember.o .libs/pseries.o .libs/print.o .libs/symbol.o .libs/symmetry.o .libs/tensor.o .libs/utils.o .libs/wildcard.o   -Wl,-R -Wl,/usr/local/gcc-4.4.4/lib -Wl,-R -Wl,/usr/local/gcc-4.4.4/lib -L/export/home/drkirkby/sage-4.4.3/local/lib/python2.6/config -lpython2.6 -lsocket -lnsl -ldl -L/export/home/drkirkby/sage-4.4.3/local/lib -L/usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4 -L/usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../.. /usr/local/gcc-4.4.4/lib/libstdc++.so -lm -lgcc_s /usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/crtend.o /usr/lib/crtn.o  -m64 -m64   -Wl,-h -Wl,libpynac-0.2.so.0 -o .libs/libpynac-0.2.so.0.0.0
ld: fatal: file .libs/py_funcs.o: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to .libs/libpynac-0.2.so.0.0.0
collect2: ld returned 1 exit status
make[4]: *** [libpynac.la] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage-4.4.3/spkg/build/pynac-0.2.0.p3/src/ginac'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.4.3/spkg/build/pynac-0.2.0.p3/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.3/spkg/build/pynac-0.2.0.p3/src'
Error building pynac.

real 1m26.752s
user 1m19.837s
sys 0m5.230s
sage: An error occurred while installing pynac-0.2.0.p3

```


Issue created by migration from https://trac.sagemath.org/ticket/7861





---

archive/issue_comments_068028.json:
```json
{
    "body": "I've updated the title and description completely, to reflect the fact that the ticket was originally opened against a much earlier version of pynac, for which there was a completely different error message.",
    "created_at": "2010-06-05T21:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68028",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've updated the title and description completely, to reflect the fact that the ticket was originally opened against a much earlier version of pynac, for which there was a completely different error message.



---

archive/issue_comments_068029.json:
```json
{
    "body": "I've found a workaround for pynac failing to install on OpenSolaris, though it is not ideal. The workaround is only performed on Solaris or OpenSolaris and only for 64-bit builds. \n\nI've added the directory containing GCC's 64-bit libraries at the front of the linker search path, which for my particular installation is \n\n/usr/local/gcc-4.4.4-multilib/lib/amd64\n\nOn a SPARC system, the 'amd64' would be replaced by 'sparcv9'. The exact directory is determined using 'isainfo -n' and the path to gcc. \n\nOn a SPARC\n\n```\ndrkirkby@kestrel:~$ isainfo -n\nsparcv9\n```\nOn a Xeon\n\n```\ndrkirkby@hawk:~$ isainfo -n\namd64\n```\n\nLibtool, which is used by pynac should take care of all this - it should not be necessary for me to do it. But this works, though it would break if the directories containing the binaries (gcc, g++ etc) did not share the same parent as those containing the libraries. Fortunately, it is rare for people to install gcc that way. \n\n```\npynac-0.2.0.p4/src/pynac.pc.in\npynac-0.2.0.p4/src/COPYING\npynac-0.2.0.p4/src/aclocal.m4\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: /export/home/drkirkby/gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4-multilib --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.4.4-multilib --with-mpfr=/usr/local/gcc-4.4.4-multilib --disable-nls --enable-checking=release --enable-werror=no --enable-multilib --with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld\nThread model: posix\ngcc version 4.4.4 (GCC) \n****************************************************\nBuilding a 64-bit version of pynac\n64-bit libraries for GCC are assumed to be in /usr/local/gcc-4.4.4-multilib/lib/amd64\nso compiler flags -R/usr/local/gcc-4.4.4-multilib/lib/amd64 and -L/usr/local/gcc-4.4.4-multilib/lib/amd64 will be added\nWARNING - these assumptions may be incorrect if GCC was\nconfigured with options like --bindir=DIR or --libdir=DIR\nbut will be fine for most installations of gcc\nLong-term, a better solution needs to be found\nStarting build...\nRunning build_pynac...\nchecking for a BSD-compatible install... /usr/bin/ginstall -c\n<snip>\nconfig.status: creating config.h\nconfig.status: executing depfiles commands\nconfig.status: executing libtool commands\nConfiguration of GiNaC 0.2.0 done. Now type \"make\".\nmake  all-recursive\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'\nMaking all in ginac\nmake[2]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT py_funcs.lo -MD -MP -MF .deps/py_funcs.Tpo -c -o py_funcs.lo py_funcs.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -MT py_funcs.lo -MD -MP -MF .deps/py_funcs.Tpo -c py_funcs.cpp  -fPIC -DPIC -o .libs/py_funcs.o\nmv -f .deps/py_funcs.Tpo .deps/py_funcs.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT add.lo -MD -MP -MF .deps/add.Tpo -c -o add.lo add.cpp\nlibtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -MT add.lo -MD -MP -MF .deps/add.Tpo -c add.cpp  -fPIC -DPIC -o .libs/add.o\nmv -f .deps/add.Tpo .deps/add.Plo\n/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT archive.lo -MD -MP -MF .deps/archive.Tpo -c -o archive.lo archive.cpp\n```\n\nAfter some time, this builds. The test suite passes without error, though the fact the test suite finishes almost instantly makes me wonder if any tests are actually run. \n\n```\nDone installing pynac.\n\nreal\t0m39.461s\nuser\t0m33.296s\nsys\t0m4.679s\nSuccessfully installed pynac-0.2.0.p4\nRunning the test suite.\nTesting a 64-bit version of pynac\nMaking check in ginac\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'\nmake[1]: Nothing to be done for `check'.\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing pynac-0.2.0.p4.spkg\n```",
    "created_at": "2010-06-28T04:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68029",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've found a workaround for pynac failing to install on OpenSolaris, though it is not ideal. The workaround is only performed on Solaris or OpenSolaris and only for 64-bit builds. 

I've added the directory containing GCC's 64-bit libraries at the front of the linker search path, which for my particular installation is 

/usr/local/gcc-4.4.4-multilib/lib/amd64

On a SPARC system, the 'amd64' would be replaced by 'sparcv9'. The exact directory is determined using 'isainfo -n' and the path to gcc. 

On a SPARC

```
drkirkby@kestrel:~$ isainfo -n
sparcv9
```
On a Xeon

```
drkirkby@hawk:~$ isainfo -n
amd64
```

Libtool, which is used by pynac should take care of all this - it should not be necessary for me to do it. But this works, though it would break if the directories containing the binaries (gcc, g++ etc) did not share the same parent as those containing the libraries. Fortunately, it is rare for people to install gcc that way. 

```
pynac-0.2.0.p4/src/pynac.pc.in
pynac-0.2.0.p4/src/COPYING
pynac-0.2.0.p4/src/aclocal.m4
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
Configured with: /export/home/drkirkby/gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4-multilib --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.4.4-multilib --with-mpfr=/usr/local/gcc-4.4.4-multilib --disable-nls --enable-checking=release --enable-werror=no --enable-multilib --with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.4.4 (GCC) 
****************************************************
Building a 64-bit version of pynac
64-bit libraries for GCC are assumed to be in /usr/local/gcc-4.4.4-multilib/lib/amd64
so compiler flags -R/usr/local/gcc-4.4.4-multilib/lib/amd64 and -L/usr/local/gcc-4.4.4-multilib/lib/amd64 will be added
WARNING - these assumptions may be incorrect if GCC was
configured with options like --bindir=DIR or --libdir=DIR
but will be fine for most installations of gcc
Long-term, a better solution needs to be found
Starting build...
Running build_pynac...
checking for a BSD-compatible install... /usr/bin/ginstall -c
<snip>
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
Configuration of GiNaC 0.2.0 done. Now type "make".
make  all-recursive
make[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'
Making all in ginac
make[2]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT py_funcs.lo -MD -MP -MF .deps/py_funcs.Tpo -c -o py_funcs.lo py_funcs.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -MT py_funcs.lo -MD -MP -MF .deps/py_funcs.Tpo -c py_funcs.cpp  -fPIC -DPIC -o .libs/py_funcs.o
mv -f .deps/py_funcs.Tpo .deps/py_funcs.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT add.lo -MD -MP -MF .deps/add.Tpo -c -o add.lo add.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -MT add.lo -MD -MP -MF .deps/add.Tpo -c add.cpp  -fPIC -DPIC -o .libs/add.o
mv -f .deps/add.Tpo .deps/add.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT archive.lo -MD -MP -MF .deps/archive.Tpo -c -o archive.lo archive.cpp
```

After some time, this builds. The test suite passes without error, though the fact the test suite finishes almost instantly makes me wonder if any tests are actually run. 

```
Done installing pynac.

real	0m39.461s
user	0m33.296s
sys	0m4.679s
Successfully installed pynac-0.2.0.p4
Running the test suite.
Testing a 64-bit version of pynac
Making check in ginac
make[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'
make[1]: Nothing to be done for `check'.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'
make[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing pynac-0.2.0.p4.spkg
```



---

archive/issue_comments_068030.json:
```json
{
    "body": "This is NOT ready for review. William said running 'make test' was pointless, so I need to remove spkg-check",
    "created_at": "2010-06-28T05:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68030",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This is NOT ready for review. William said running 'make test' was pointless, so I need to remove spkg-check



---

archive/issue_comments_068031.json:
```json
{
    "body": "The package is here awaiting review now.",
    "created_at": "2010-06-28T06:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68031",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The package is here awaiting review now.



---

archive/issue_comments_068032.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T06:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68032",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068033.json:
```json
{
    "body": "Oops, I forgot to put the path to the .spkg \n\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p4.spkg",
    "created_at": "2010-06-28T08:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68033",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Oops, I forgot to put the path to the .spkg 


http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p4.spkg



---

archive/issue_comments_068034.json:
```json
{
    "body": "I'm changing this to needs work, as there is a simpler, more elegant and more reliable way to resolve this, by setting CC=\"gcc -m64\", CXX=\"g++ -m64\" as was done on libfplll in ticket #7864. \n\nI will rewrite this patch, to use the other method. \n\nDave",
    "created_at": "2010-07-14T16:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68034",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm changing this to needs work, as there is a simpler, more elegant and more reliable way to resolve this, by setting CC="gcc -m64", CXX="g++ -m64" as was done on libfplll in ticket #7864. 

I will rewrite this patch, to use the other method. 

Dave



---

archive/issue_comments_068035.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-14T16:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68035",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068036.json:
```json
{
    "body": "Attachment [7861.patch](tarball://root/attachments/some-uuid/ticket7861/7861.patch) by drkirkby created at 2010-07-16 16:06:05\n\nSimple change to export CC and CXX properly to build 64-bit on Solaris 10 and OpenSolaris",
    "created_at": "2010-07-16T16:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68036",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [7861.patch](tarball://root/attachments/some-uuid/ticket7861/7861.patch) by drkirkby created at 2010-07-16 16:06:05

Simple change to export CC and CXX properly to build 64-bit on Solaris 10 and OpenSolaris



---

archive/issue_comments_068037.json:
```json
{
    "body": "I'm attaching logs showing builds on Solaris 10 (SPARC) and OpenSolaris x64. The package is ready for review at http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p5.spkg\n\nDave",
    "created_at": "2010-07-16T16:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68037",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm attaching logs showing builds on Solaris 10 (SPARC) and OpenSolaris x64. The package is ready for review at http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p5.spkg

Dave



---

archive/issue_comments_068038.json:
```json
{
    "body": "Build log from a Sun Blade 2000 with UltraSPARC III+ processors",
    "created_at": "2010-07-16T16:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68038",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Build log from a Sun Blade 2000 with UltraSPARC III+ processors



---

archive/issue_comments_068039.json:
```json
{
    "body": "Attachment [pynac-0.2.0.p5.log.OpenSolaris_x64.txt](tarball://root/attachments/some-uuid/ticket7861/pynac-0.2.0.p5.log.OpenSolaris_x64.txt) by drkirkby created at 2010-07-16 16:51:52\n\nBuild log from a Sun Ultra 27 with an Intel Xeon processor",
    "created_at": "2010-07-16T16:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68039",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [pynac-0.2.0.p5.log.OpenSolaris_x64.txt](tarball://root/attachments/some-uuid/ticket7861/pynac-0.2.0.p5.log.OpenSolaris_x64.txt) by drkirkby created at 2010-07-16 16:51:52

Build log from a Sun Ultra 27 with an Intel Xeon processor



---

archive/issue_comments_068040.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-16T16:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68040",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068041.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-03T21:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68041",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068042.json:
```json
{
    "body": "The changes look good.  The spkg builds on a number of different machines, both 32-bit and 64-bit, and doctests pass.\n\nBy the way, with the old spkg, pynac didn't build properly on 64-bit Solaris (either sparc -- t2 -- or x86 -- fulvia), so it's not exclusively an OpenSolaris issue.  With the new spkg, it works.\n\n(Tested on t2 (32-bit), mark2 (32-bit), Mac OS X 10.6 (64-bit), sage.math (both with SAGE64='yes' and with SAGE64 unset), taurus (both with SAGE64='yes' and SAGE64 unset), cicero (32-bit), fulvia (both settings for SAGE64), and iras (64-bit machine? but with SAGE64 unset).)",
    "created_at": "2010-08-03T21:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68042",
    "user": "https://github.com/jhpalmieri"
}
```

The changes look good.  The spkg builds on a number of different machines, both 32-bit and 64-bit, and doctests pass.

By the way, with the old spkg, pynac didn't build properly on 64-bit Solaris (either sparc -- t2 -- or x86 -- fulvia), so it's not exclusively an OpenSolaris issue.  With the new spkg, it works.

(Tested on t2 (32-bit), mark2 (32-bit), Mac OS X 10.6 (64-bit), sage.math (both with SAGE64='yes' and with SAGE64 unset), taurus (both with SAGE64='yes' and SAGE64 unset), cicero (32-bit), fulvia (both settings for SAGE64), and iras (64-bit machine? but with SAGE64 unset).)



---

archive/issue_comments_068043.json:
```json
{
    "body": "Is this positive review okay?  I don't have access to an OpenSolaris machine, but I've tested it on lots of other platforms.  I may try to install an OpenSolaris virtual machine, but I don't know how hard it will be to install all of the relevant software (like an up-to-date gcc).",
    "created_at": "2010-08-03T21:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68043",
    "user": "https://github.com/jhpalmieri"
}
```

Is this positive review okay?  I don't have access to an OpenSolaris machine, but I've tested it on lots of other platforms.  I may try to install an OpenSolaris virtual machine, but I don't know how hard it will be to install all of the relevant software (like an up-to-date gcc).



---

archive/issue_comments_068044.json:
```json
{
    "body": "Replying to [comment:12 jhpalmieri]:\n> Is this positive review okay?  I don't have access to an OpenSolaris machine, but I've tested it on lots of other platforms.  \n\n\nI don't believe anyone can fault your positive review due to the fact you have not tested on OpenSolaris. \n\nFirst OpenSolaris is not an officially supported system. So that in itself is good enough reason not to fault you. But you have tested on several officially supported systems, as well as some unsupported ones. As you note, it does improve the situation on 64-bit SPARC and 64-bit x86. In fact, virtually all the changes I think that will be needed on one 64-bit variant of Solaris will be needed on another. \n\nSecondly, I've attached a log of the build on OpenSolaris, so it can be seen working there. \n\nA lot of reviewers are a lot less thorough than you John! \n\nI've had the odd people review my HP-UX patches too. I don't think anyone other than Minh has access to HP-UX. (Some of the MPFR developers have used my machine too)\n\n> I may try to install an OpenSolaris virtual machine, but I don't know how hard it will be to install all of the relevant software (like an up-to-date gcc).\n\n\nOpenSolaris has a package manager with a GUI interface which you can use to install software. By default, it gets packages from the offical Sun resource, which does not tend to have very up to update packages. But one can switch to the development server, and install from there, where there is a wider choice of packages. \n\nOne issue I have hit is that on my laptop (which has a 64-bit processor), I installed a 64-bit version of OpenSolaris as the host operating system. But due to some limitations in the BIOS, which Sony kindly added, they have disabled the instructions which allow one to install a 64-bit guest operating system. While that's not a problem with my XP installation, my Solaris 10 installation is limited to 32-bits when on my laptop. \n\nOn my desktop, there's no such limitation, so I can install 64-bit guest operating systems. \n\nAnyway, thank you for the review. I need to sort out zn_poly (#9358). I have a patch for that. Just need to upload it and mark it for review. \n\nDave",
    "created_at": "2010-08-03T22:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68044",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 jhpalmieri]:
> Is this positive review okay?  I don't have access to an OpenSolaris machine, but I've tested it on lots of other platforms.  


I don't believe anyone can fault your positive review due to the fact you have not tested on OpenSolaris. 

First OpenSolaris is not an officially supported system. So that in itself is good enough reason not to fault you. But you have tested on several officially supported systems, as well as some unsupported ones. As you note, it does improve the situation on 64-bit SPARC and 64-bit x86. In fact, virtually all the changes I think that will be needed on one 64-bit variant of Solaris will be needed on another. 

Secondly, I've attached a log of the build on OpenSolaris, so it can be seen working there. 

A lot of reviewers are a lot less thorough than you John! 

I've had the odd people review my HP-UX patches too. I don't think anyone other than Minh has access to HP-UX. (Some of the MPFR developers have used my machine too)

> I may try to install an OpenSolaris virtual machine, but I don't know how hard it will be to install all of the relevant software (like an up-to-date gcc).


OpenSolaris has a package manager with a GUI interface which you can use to install software. By default, it gets packages from the offical Sun resource, which does not tend to have very up to update packages. But one can switch to the development server, and install from there, where there is a wider choice of packages. 

One issue I have hit is that on my laptop (which has a 64-bit processor), I installed a 64-bit version of OpenSolaris as the host operating system. But due to some limitations in the BIOS, which Sony kindly added, they have disabled the instructions which allow one to install a 64-bit guest operating system. While that's not a problem with my XP installation, my Solaris 10 installation is limited to 32-bits when on my laptop. 

On my desktop, there's no such limitation, so I can install 64-bit guest operating systems. 

Anyway, thank you for the review. I need to sort out zn_poly (#9358). I have a patch for that. Just need to upload it and mark it for review. 

Dave



---

archive/issue_comments_068045.json:
```json
{
    "body": "## Note to the release manager\n\nJust add http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p5.spkg \n\nThere are no library patches needed, and nothing needs to be added to the package. It should just drop it and go.",
    "created_at": "2010-08-07T22:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68045",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

## Note to the release manager

Just add http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p5.spkg 

There are no library patches needed, and nothing needs to be added to the package. It should just drop it and go.



---

archive/issue_events_018793.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:36:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7861#event-18793"
}
```



---

archive/issue_comments_068046.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7861#issuecomment-68046",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
