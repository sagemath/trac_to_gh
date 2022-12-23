# Issue 4059: libm4ri configure is seriously broken on anything not x86

Issue created by migration from https://trac.sagemath.org/ticket/4059

Original creator: anakha

Original creation time: 2008-09-04 05:52:37

Assignee: mabshoff

Here is the tail of the build log for libm4ri. 


```
checking for a BSD-compatible install... /usr/bin/install -c
checking mm_malloc.h usability... no
checking mm_malloc.h presence... no
checking for mm_malloc.h... no
checking for a sed that does not truncate output... /usr/bin/sed
checking the number of available CPUs... 2 
checking the number of available CPUs... 2 
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
./configure: line 21425: test: !=: unary operator expected
checking for x86 cpuid 0x80000006 output... unknown
./configure: line 21618: 16#unknown: value too great for base (error token is "16#unknown")
Error configuring libm4ri

real	0m17.957s
user	0m3.904s
sys	0m8.981s
sage: An error occurred while installing libm4ri-20080901
```


The first error is a typo of a variable name and an unprotected expand of it in a shell test.  This test only occurs on systems that do not have

/sys/devices/system/cpu/cpu0/cache/index0/size

which are gratuitously assumed to all be running x86 except if the cpu vendor is Intel in which case they are assumed to not have a cache.  

And this leads us to the second problem, on non-x86 cpus, since the cache size cannot be discovered with cpuid, a later conversion of this cache size from hex fails miserably.

This is a mess.


---

Comment by mabshoff created at 2008-09-04 06:44:16

This ought to be fixed by the new spkg at #4042. Please try it out and let us know how it goes.

Cheers,

Michael


---

Comment by anakha created at 2008-09-04 07:29:04

(I should have done a search before creating this one, damn you late hours of the night)

Yes with this spkg it builds fine, but it does not detect the amount of cache.  I don't know if this is critical for m4ri, but mine does detect it.


```
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
checking the L1 cache size... 0 Bytes
checking the L2 cache size... 0 Bytes
checking whether make sets $(MAKE)... (cached) yes
```


I know that on this machine I have 32K L1 D-cache and 1M L2 cache.

Also the new package generates these warnings


```
gcc -DHAVE_CONFIG_H -I. -I./src -I/Volumes/Place/anakha/sage-3.1.2.alpha4/local/include/ -std=c99 -fPIC -I/Volumes/Place/anakha/sage-3.1.2.alpha4/local/include/ -L/Volumes/Place/anakha/sage-3.1.2.alpha4/local/lib -O2 -Wall -pedantic -g -MT brilliantrussian.lo -MD -MP -MF .deps/brilliantrussian.Tpo -c src/brilliantrussian.c  -fno-common -DPIC -o .libs/brilliantrussian.o
In file included from src/brilliantrussian.c:21:
src/misc.h:284:1: warning: "CPU_L2_CACHE" redefined
In file included from src/misc.h:33,
                 from src/brilliantrussian.c:21:
src/config.h:8:1: warning: this is the location of the previous definition
In file included from src/brilliantrussian.c:21:
src/misc.h:292:1: warning: "CPU_L1_CACHE" redefined
In file included from src/misc.h:33,
                 from src/brilliantrussian.c:21:
src/config.h:5:1: warning: this is the location of the previous definition
```


While the existence of the package at #4042 does lower the priority on this one, I think the cache detection parts should be merged. So I attached a patch against libm4ri-20080903 for the m4/ax_cache_size.m4 file to add the cache size detection code.  

There is also a test spkg here: http://celas.ath.cx/anakha/libm4ri-20080903.p0.spkg

Do not merge this spkg as I think it is too late for me to figure out how to properly rebuild the configure script.  Thus, it rebuilds itself every time you build the package making you suffer two times the configuration phase.


---

Comment by anakha created at 2008-09-04 07:29:04

Changing priority from critical to major.


---

Attachment

Patch against libm4ri-20080903 to enable cache detection on OS X 10.5


---

Comment by malb created at 2008-09-04 08:29:41

Thanks, I'll look into your cache detection code and merge it upstream. To my defense btw. this is a code snipped from the autoconf archive.


---

Comment by malb created at 2008-09-04 11:15:10

A new SPKG is available at

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080904.spkg

with the patch applied.

It builds and passes tests on:
 * my notebook (Linux, x86_64, Core2Duo)
 * cleo (Linux, ia64)
 * iras (Linux, ia64, L1 and L2 not detected) 
 * bsd (OSX, x86, L1 not detected)
 * sage.math (Linux, x86_64, Opteron)
 * VirtualBox (OpenSolaris, x86, Core2Duo, L1 and L2 not detected)

So it is still not perfect but should be better (OSX PPC support). I don't have access to a PPC box to test it.


---

Comment by anakha created at 2008-09-04 14:12:01

It works on my machine (OS X, ppc G5) and all tests pass.

A minor cosmetic change that it seems I forgot in my patch is to change the redirection in the sysctl lines to read:

> /dev/null 2>&1

because otherwise the cache size are printed on their own in the configure output.  This does not harm the results in any way but can be annoying when looking at the configure output (but who does that anyway :)


---

Comment by malb created at 2008-09-04 14:22:47

so 

  `/usr/sbin/sysctl -n hw.l2cachesize`

would become

  `/usr/sbin/sysctl -n hw.l2cachesize 2>&1`

My autoconf foo is limited and I can't test it due to the lack of PPC OSX. Note to self: This should also be used on x86 OSX since apparently Intel chips don't report L1 cache size using CPUID


---

Comment by anakha created at 2008-09-04 14:40:16

no, it would become 

`/usr/sbin/sysctl -n hw.l2cachesize > /dev/null 2>&1`

it is possible this would work on OS X x86 but I can't test it nor test how to use this test rather than the CPUID for that.


---

Comment by malb created at 2008-09-04 14:54:17

I've replaced the SPKG with an SPKG with that fix applied, could you test it?


---

Comment by mabshoff created at 2008-09-04 22:45:39

On bsd the new m4ri reports:

```
checking the number of available CPUs... 4 
checking the number of available CPUs... 4 
checking for x86 cpuid 0x0 output... (cached) a:756e6547:6c65746e:49656e69
checking for the processor vendor... (cached) Intel
checking for x86 cpuid 0x80000006 output... 0:0:10008040:0
checking the L1 cache size... 0 Bytes
checking the L2 cache size... 4194304 Bytes
```

But on a PPC OSX 10.4 box it fails with

```

checking the number of available CPUs... 1 
checking the number of available CPUs... 1 
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
524288
32768
second level name l1cachesize in hw.l1cachesize is invalid
second level name l1cachesize in hw.l1cachesize is invalid
./configure: line 21633: / 1024: syntax error: operand expected (error token is "/ 1024")
Error configuring libm4ri
```


Cheers,

Michael


---

Comment by anakha created at 2008-09-05 03:54:54

Apply trac_4059_v3.patch to the latest libm4ri-20080904.  Basically the 2 should not be there.

As for the other failure, could someone with 10.4 access run these commands and port the output:


```
$ sysctl -n hw.foo
$ echo $?
```



---

Attachment

Replying to [comment:10 mabshoff]:
> On bsd the new m4ri reports:
...
> checking the L1 cache size... 0 Bytes
> checking the L2 cache size... 4194304 Bytes

That's fine. Eventually, I should fix the L1 detection code though. IMHO, the whole cache detection needs to be refactored, but I don't want to do it just before a release.


---

Comment by malb created at 2008-09-05 10:05:48

Replying to [comment:11 anakha]:
> Apply trac_4059_v3.patch to the latest libm4ri-20080904.  Basically the 2 should not be there.

I've updated the SPKG at /home/malb/spkgs/libm4ri-20080904.spkg to include this patch.

> As for the other failure, could someone with 10.4 access run these commands and port the output:
> 
> {{{
> $ sysctl -n hw.foo
> $ echo $?
> }}}

Yep, I can do that later today.


---

Comment by malb created at 2008-09-05 14:14:41


```
martin-albrechts-computer:~ martinalbrecht$ sysctl -n hw.foo
second level name foo in hw.foo is invalid
martin-albrechts-computer:~ martinalbrecht$  echo $?
0
```



---

Comment by anakha created at 2008-09-05 16:29:21

This means sysctl does not return an error when the name is not found on 10.4 which lead to the above error encountered by mabshoff.

I hope trac_4059_v4.patch can fix this.


---

Attachment

I updated the SPKG again and tested in on OSX 10.4 on x86 (for this I disabled the CPUID technique so that this code is actually run) and it works. Good work!


---

Comment by anakha created at 2008-09-05 17:46:45

Ok perfect.  I think we have it now.


---

Comment by mabshoff created at 2008-09-06 00:29:17

Resolution: fixed


---

Comment by mabshoff created at 2008-09-06 00:29:17

Merged in Sage 3.1.2.rc0
