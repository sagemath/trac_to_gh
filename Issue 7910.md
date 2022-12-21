# Issue 7910: mpir.1.2.2 fails to build on Open Solaris 06/2009 in VirtualBox no ABI=64

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-12 16:32:08

Assignee: GeorgSWeber

CC:  drkirkby goodwillhart@googlemail.com

Keywords: mpir Open Solaris

From sage-devel:


```
In Open Solaris in my VirtualBox running under Fedora 12 64 bit on an Intel i7 860:

Finished extraction
****************************************************
Host system
uname -a:
SunOS opensolaris 5.11 snv_111b i86pc i386 i86pc Solaris
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
Building 64 bit Solaris version
checking build system type... i486-pc-solaris2.11
checking host system type... i486-pc-solaris2.11
checking for a BSD-compatible install... /export/home/jaap/sage-bin/install -c
checking whether build environment is sane... yes
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether to enable maintainer-specific portions of Makefiles... no
configure: error: ABI=64 is not among the following valid choices: 32
Failed to configure.

real    0m1.743s
user    0m0.190s
sys     0m0.466s
sage: An error occurred while installing mpir-1.2.2

While building the following SAGE related exports are set:
sage subshell$ env | grep SAGE
SAGE_SERVER=http://www.sagemath.org/
SAGE_ORIG_LD_LIBRARY_PATH_SET=True
SAGE_DATA=/export/home/jaap/Downloads/sage-4.3.1.alpha1/data
DOT_SAGE=/export/home/jaap/.sage/
SAGE_LOCAL=/export/home/jaap/Downloads/sage-4.3.1.alpha1/local
SAGE_STARTUP_FILE=/export/home/jaap/.sage//init.sage
LC_MESSAGES=en_US.UTF-8
SAGE_ROOT=/export/home/jaap/Downloads/sage-4.3.1.alpha1
SAGE_PACKAGES=/export/home/jaap/Downloads/sage-4.3.1.alpha1/spkg
SAGE_ORIG_LD_LIBRARY_PATH=
SAGE_DOC=/export/home/jaap/Downloads/sage-4.3.1.alpha1/devel/sage/doc
SAGE_TESTDIR=/export/home/jaap/.sage//tmp
SAGE64=yes
/export/home/jaap/Downloads/sage-4.3.1.alpha1
sage subshell$ env | grep FLAG
LDFLAGS=
FCFLAG64=-m64
SHARED_FLAG=-shared
CXXFLAGS= -Wall -g -m64
FCFLAGS= -Wall -g -m64
SONAME_FLAG=-soname
CFLAGS= -Wall -g -m64
WHOLE_ARCHIVE_FLAG=--whole-archive
NO_WHOLE_ARCHIVE_FLAG=--no-whole-archive
CXXFLAG64=-m64
FPIC_FLAG=-fPIC
CFLAG64=-m64

I understand that FLAGS are not so relevant while building mpir.


The same Open Solaris on Dave Kirkby's box:

Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_111b i86pc i386 i86pc Solaris
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
Building 64 bit Solaris version
checking build system type... nehalem-pc-solaris2.11
checking host system type... nehalem-pc-solaris2.11
checking for a BSD-compatible install... /usr/bin/ginstall -c
checking whether build environment is sane... yes
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking ABI=64
checking compiler gcc  -Wall -g -m64 -Wall -g -m64 ... yes
checking for gcc... gcc
checking for C compiler default output file name... a.out

The build seems to work.

Help needed! Bill? 
```


Jaap



---

Comment by drkirkby created at 2010-01-13 02:38:53

Note Bill Hart said on sage-devel that your CPU is being mis-detected, as MPIR believes it is a 486 and there are of course no 64-bit 486's, which why it obviously does not offer a 64-bit ABI. 


```
checking build system type... i486-pc-solaris2.11
checking host system type... i486-pc-solaris2.11 
```

whereas on my system (a Xeon based machine)


```
checking build system type... nehalem-pc-solaris2.11
checking host system type... nehalem-pc-solaris2.11 
```


If this an autoconf macro, then perhaps the autoconf mailing list might be helpful. 

Dave


---

Comment by jsp created at 2010-01-13 10:40:18


```
jaap`@`opensolaris:~/Downloads/sage-4.3.1.alpha1$ /usr/sbin/psrinfo -v
Status of virtual processor 0 as of: 01/13/2010 11:25:49
  on-line since 01/12/2010 05:53:06.
  The i386 processor operates at 2780 MHz,
    and has an i387 compatible floating point processor.
Status of virtual processor 1 as of: 01/13/2010 11:25:49
  on-line since 01/12/2010 05:53:09.
  The i386 processor operates at 2780 MHz,
    and has an i387 compatible floating point processor.
jaap`@`opensolaris:~/Downloads/sage-4.3.1.alpha1$

This is in VirtualBox, so virtual processors?

But I have built dozens of ELF 64 programs!

```


Jaap


---

Comment by jsp created at 2010-01-13 10:58:45

Replying to [comment:2 jsp]:

```
> 
> {{{
> jaap`@`opensolaris:~/Downloads/sage-4.3.1.alpha1$ /usr/sbin/psrinfo -v
> Status of virtual processor 0 as of: 01/13/2010 11:25:49
>   on-line since 01/12/2010 05:53:06.
>   The i386 processor operates at 2780 MHz,
>     and has an i387 compatible floating point processor.
> Status of virtual processor 1 as of: 01/13/2010 11:25:49
>   on-line since 01/12/2010 05:53:09.
>   The i386 processor operates at 2780 MHz,
>     and has an i387 compatible floating point processor.
> jaap`@`opensolaris:~/Downloads/sage-4.3.1.alpha1$
> 
> This is in VirtualBox, so virtual processors?
> 
```


No on Fedora in VirtualBox the real thing seems to be recognized:



```
[jaap`@`pace ~]$ cat /proc/cpuinfo
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 30
model name	: Intel(R) Core(TM) i7 CPU         860  `@` 2.80GHz
stepping	: 5
cpu MHz		: 2949.200
cache size	: 0 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fdiv_bug	: no
hlt_bug		: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 5
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx lm constant_tsc pni lahf_lm
bogomips	: 5898.40
clflush size	: 64
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 30
model name	: Intel(R) Core(TM) i7 CPU         860  `@` 2.80GHz
stepping	: 5
cpu MHz		: 2949.200
cache size	: 0 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 2
apicid		: 1
initial apicid	: 1
fdiv_bug	: no
hlt_bug		: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 5
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx lm constant_tsc pni lahf_lm
bogomips	: 6129.93
clflush size	: 64
power management:


```


Jaap


---

Comment by jsp created at 2010-01-13 11:08:00

mpir-1.2.2 in Fedora 12:



```
gcc version 4.4.2 20091027 (Red Hat 4.4.2-7) (GCC)
****************************************************
checking build system type... i486-pc-linux-gnu
checking host system type... i486-pc-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking ABI=32
checking compiler gcc -m32 -O2 -fomit-frame-pointer ... yes
checking compiler gcc -m32 -O2 -fomit-frame-pointer has sizeof(long)==4... yes
checking compiler gcc -m32 -O2 -fomit-frame-pointer  -mtune=i486... yes
checking compiler gcc -m32 -O2 -fomit-frame-pointer -mtune=i486  -march=i486... yes
checking for gcc... gcc

```


So it looks like mpir finds a 486!

Jaap


---

Comment by jsp created at 2010-01-13 13:47:49

I take back fo former comment. I started the wrong virtual machine.

On Fedora 12 x86_64 in VirtualBox:



```
gcc version 4.4.2 20091222 (Red Hat 4.4.2-20) (GCC)
****************************************************
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for gawk... gawk
checking whether make -j2 sets $(MAKE)... yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking ABI=64
checking compiler gcc -O2 -m64 ... yes
checking compiler gcc -O2 -m64  -march=k8... yes


```



That seems to work.

Jaap


---

Comment by jsp created at 2010-01-13 18:31:06

I could install mpir with an ugly hack. Upstream there are some activities.

There is a patch for Linux.

Jaap


---

Comment by drkirkby created at 2010-01-13 18:59:15

I suspect a hack to the configure script directly should work. I'd just make it appear some low-spec 64-bit CPU, but the MPIR developers will I'm sure advise you the best immediate workaround.


---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing assignee from GeorgSWeber to jdemeyer.


---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing component from build to packages: standard.


---

Comment by jdemeyer created at 2018-03-02 13:52:38

Obsolete


---

Comment by jdemeyer created at 2018-03-02 13:52:38

Resolution: invalid
