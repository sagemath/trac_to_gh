# Issue 8090: genus2reduction no building on Open Solaris x64. (32/64 bit issue)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-27 04:38:31

Assignee: drkirkby

CC:  jsp

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.3.1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 

## The problem

```
Compiling genus2reduction.c
In file included from /export/home/drkirkby/sage-4.3.1/local/include/pari/pari.h:76,
                 from genus2reduction.c:18:
../src/kernel/none/level1.h: In function ‘evallg’:
../src/kernel/none/level1.h:180: warning: left shift count >= width of type
<SNIP>
genus2reduction.c:1825: warning: left shift count >= width of type
genus2reduction.c:1825: warning: left shift count >= width of type
genus2reduction.c:1830: warning: left shift count >= width of type
genus2reduction.c:1834: warning: left shift count >= width of type
genus2reduction.c:1834: warning: left shift count >= width of type
genus2reduction.c: In function ‘factmz’:
genus2reduction.c:2022: warning: left shift count >= width of type
genus2reduction.c:2024: warning: left shift count >= width of type
genus2reduction.c:2033: warning: left shift count >= width of type
genus2reduction.c:2033: warning: right shift count >= width of type
genus2reduction.c:2037: warning: left shift count >= width of type
genus2reduction.c:2041: warning: left shift count >= width of type
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libpari.so: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to genus2reduction
collect2: ld returned 1 exit status
Error building genus2reduction

real	0m0.930s
user	0m0.882s
sys	0m0.041s
sage: An error occurred while installing genus2reduction-0.3.p5
```

 == Probably reason ==
This looks like a 32/64 bit issue, as the ELFCLASS is wrong. I suspect this is building 32-bit, not 64-bit, though its not obvious as all one sees is:

```
Compiling genus2reduction.c
```

with no idea what compiler is being used. 


---

Attachment


---

Comment by jsp created at 2010-01-27 20:39:40

There is a patch and an spkg.

[http://boxen.math.washington.edu/home/jsp/ports/genus2reduction-0.3.p6.spkg](http://boxen.math.washington.edu/home/jsp/ports/genus2reduction-0.3.p6.spkg)

You gave it a positive review.
http://trac.sagemath.org/sage_trac/ticket/8061#comment:2

So I think this is a dup.

Jaap


---

Comment by drkirkby created at 2010-01-28 14:47:57

Yes, you are correct. This is a duplicate. I'm marking it as a duplicate.


---

Comment by drkirkby created at 2010-01-28 14:47:57

Resolution: duplicate
