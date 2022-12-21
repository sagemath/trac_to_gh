# Issue 7471: update the patches in the mpir spkg

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-15 18:02:44

Assignee: tbd


```

> 2009/11/15 Jason Moxham <>:
>>
>> Solved???
>>
>> jasonmoxham`@`debian5-32:/tmp/jason/mpir-1.2$ diff  config.guess
>> ../sage-4.2.1/spkg/standard/mpir-1.2.p9/src/config.guess
>> 660c660
>> < i?86-*-*|x86_64-*-*|amd64-*-*)
>> ---
>>> i?86-*-*|x86_64-*-*)
>> 755c755
>> <   rm -f ${dummy}032.s ${dummy}32.o ${dummy}32.c ${dummy}032.o ${dummy}064.s
>> ${dummy}64.o ${dummy}64.c ${dummy}064.o $dummy ${dummy}.exe
>> ---
>>>   rm -f ${dummy}032.s ${dummy}32.o ${dummy}32.c ${dummy}032.o ${dummy}064.s
>> ${dummy}64.o ${dummy}64.c ${dummy}064.o $dummy
>> jasonmoxham`@`debian5-32:/tmp/jason/mpir-1.2$ diff  mpn/x86/fat/fat.c
>> ../sage-4.2.1/spkg/standard/mpir-1.2.p9/src/mpn/x86/fat/fat.c
>> 141d140
>> <   __MPN(divrem_euclidean_qr_2_init),
>>
>> and perhaps some others ?
>> Please update sage mpir-1.2 with current mpir-1.2

Excellent, thanks for tracking this down!   

Now, I wonder what idiot messed up Sage's mpir-1.2 spkg by not updating the patches properly?

[... checks SPKG.txt ...]

### mpir-1.2 (William Stein, May 31, 2009)
 * Update to the latest MPIR 1.2 pre-release
 * Change "GMP" --> "MPIR" in various places.

Doh.  



2009/11/15 Bill Hart <>:
>
> I probably should put mpir-1.2.2 up actually, as it contained a
> FreeBSD fix specifically for Sage.
>
> I'll have to update the gplv3.txt and license info for mpf/set_str.c though.
>
> Give me a few minutes and I'll do it.

Thanks.   I can't work on this further until tonight because my internet connection is so horrible.  

> Bill.

William


---

Comment by was created at 2009-11-18 09:48:15

I just decided to look into http://trac.sagemath.org/sage_trac/ticket/7471 and try to actually fix our patches.  However, we don't patch mpir at all -- we just include plain vanilla upstream sources.  The mpir spkg was got by just taking the mpir tar ball from the mpir website, and extracting it into the src/ subdirectory.  So the discrepancy above must be because of getting a prerelease version of the tarball. 

Anyway, I just want to point out that it wasn't a problem with just forgetting to update some patches (as I suggested), since we have no patches.  We used to have tons with GMP, which is why I so quickly thought we had them still with MPIR.


---

Comment by was created at 2009-11-18 09:48:15

Changing status from new to needs_review.


---

Comment by was created at 2009-11-18 09:50:57

The new spkg is here: http://wstein.org/home/wstein/patches/mpir-1.2.2.spkg

All I did was put the latest vanilla spkg from http://mpir.org in the src directory.   There are no patches, so that's it.    I've not tested yet that this new spkg really solves the problem involving FAT binaries that started this ticket

 -- William


---

Comment by was created at 2009-11-18 17:21:00

I just tested this on the "debian32" virtual machine and it works:

```
wstein`@`debian5-32:/tmp/wstein/farm/sage-4.2.1$ export SAGE_FAT_BINARY="yes"
wstein`@`debian5-32:/tmp/wstein/farm/sage-4.2.1$ sage -f http://wstein.org/home/wstein/patches/mpir-1.2.2.spkg spkg/standard/pari-2.3.3.p5.spkg 
...
checking if the assembler knows about SSE2 instructions... yes
using ABI="32"
      CC="gcc -std=gnu99"
      CFLAGS="-m32 -O2 -fomit-frame-pointer"
      CPPFLAGS=""
      CXX="g++"
      CXXFLAGS="-m32 -O2 -fomit-frame-pointer"
      MPN_PATH=" x86/fat x86 generic"
checking for function prototypes... yes

...

real    1m23.877s
user    0m42.855s
sys     0m34.066s
Successfully installed pari-2.3.3.p5
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing pari-2.3.3.p5.spkg
```



---

Comment by was created at 2009-11-18 17:21:16

Changing priority from critical to blocker.


---

Comment by mhansen created at 2009-12-07 08:19:01

Resolution: fixed


---

Comment by mhansen created at 2009-12-07 08:19:01

Looks good to me.  Good work (to you and Jason Moxham) in tracking the confusing problem with Pari down.
