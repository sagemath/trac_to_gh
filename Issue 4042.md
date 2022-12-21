# Issue 4042: libm4ri-20080901 fails to build on Itanium Linux

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-02 21:00:38

Assignee: malb

One example session:

```
checking for a sed that does not truncate output... /usr/bin/sed
checking the number of available CPUs... 4 
checking the number of available CPUs... 4 
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
./configure: line 21425: test: !=: unary operator expected
checking for x86 cpuid 0x80000006 output... unknown
./configure: line 21618: 16#unknown: value too great for base (error token is "16#unknown")
```


Cheers,

Michael


---

Comment by malb created at 2008-09-03 13:59:41

It does seem to build on *cleo*:

```
[malb`@`cleo sage-3.1.2.alpha4]$ cat /proc/cpuinfo
processor  : 0
vendor     : GenuineIntel
arch       : IA-64
family     : Itanium 2
model      : 0
revision   : 7
archrev    : 0
features   : branchlong, 16-byte atomic ops
cpu number : 0
cpu regs   : 4
cpu MHz    : 1594.000718
itc MHz    : 399.177970
BogoMIPS   : 3186.68
siblings   : 2
physical id: 0
core id    : 0
thread id  : 0
```



```
checking mm_malloc.h usability... no
checking mm_malloc.h presence... no
checking for mm_malloc.h... no
checking for a sed that does not truncate output... /bin/sed
checking the number of available CPUs... 4
checking the number of available CPUs... 4
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
checking the L1 cache size... 16384 Bytes
checking the L2 cache size... 1048576 Bytes
checking whether make sets $(MAKE)... (cached) yes
```



---

Comment by mabshoff created at 2008-09-03 15:03:31

Hmm, might this be a /bin/sh vs. /bin/bash issue?

Cheers,

Michael


---

Comment by malb created at 2008-09-03 18:48:12

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080903.spkg


```
[19:41] <malb> mabshoff I bow down to you insisting on porting, the Itanium did reveal real bugs
[19:41] <malb> All tests passed.
[19:41] <mabshoff> :)[19:42] <malb> okay all tests pass on cleo
[19:42] <malb> and it compiles on iras
[19:43] <malb> sage.math:/home/malb/spkgs/libm4ri-20080903.spkg
[19:43] <mabshoff> Nice. Is that the spkg at http://trac.sagemath.org/sage_trac/ticket/4042
```



---

Comment by mabshoff created at 2008-09-03 23:45:37

Positive review. It builds fine on OSX, Linux x86-64, Itanium and Solaris x86 and fixes the problem. Nice work malb :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-03 23:45:52

Resolution: fixed


---

Comment by mabshoff created at 2008-09-03 23:45:52

Merged in Sage 3.1.2.rc0
