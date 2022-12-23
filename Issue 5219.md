# Issue 5219: Build ATLAS on dist mode with SSE2 only

Issue created by migration from https://trac.sagemath.org/ticket/5219

Original creator: mabshoff

Original creation time: 2009-02-09 13:05:07

Assignee: mabshoff

Many times the binaries cause trouble since we are building ATLAS with SSE3. So add a special flag which given the following settings

 * SAGE_DIST_MODE=yes
 * SAGE_DIST_MODE_ISASET=SSE2

produce an SSE2 only binary. If those flags are set we also need to make sure that sage-flags are set to sse2 only, i.e. no pni, no ssse3 or sse4_*.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 13:05:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-16 12:13:21

This was not as simple than I thought it would be. To do this we need to do two things:

 * disable the SSE3 detection by making it return "FAILURE" unconditionally
 * select ARCH defaults that allow SSE2 on 32 and 64 bit boxen. ATLAS 3.8.2 only offers that for Hammer, i.e. ARCH=20.

When doing both of the above on sage.math we get an libatlas.a without any SSE3 instructions:


```
atlas-3.8.2.p2/Hammer/lib$ ~/SSE2-project/sse-2.bash libatlas.a 
found SSE2 addpd: 2
found SSE2 addsd: 2
found SSE2 movapd: 208
found SSE2 movlpd: 131
found SSE2 movsd: 4057
found SSE2 movupd: 1
found SSE2 mulpd: 2
found SSE2 mulsd: 2
found SSE2 orpd: 174
found SSE2 unpcklpd: 1
found SSE2 xorpd: 174
```


Contrast this with a PNI enabled ATLAS from the same machine:

```
atlas-3.8.2.p2/Hammer/lib$ ~/SSE2-project/sse-2.bash 
/scratch/mabshoff/sage-3.3.rc1/local/lib/libatlas.a 
found SSE2 pshufd: 394
found SSE2 addpd: 41840
found SSE2 addsd: 74197
found SSE2 andnpd: 3
found SSE2 andpd: 34
found SSE2 comisd: 1393
found SSE2 cvtsd2ss: 8
found SSE2 cvtsi2sd: 4
found SSE2 cvtss2sd: 20
found SSE2 divsd: 304
found SSE2 maxpd: 4
found SSE2 maxsd: 4
found SSE2 movapd: 108245
found SSE2 movhpd: 1092
found SSE2 movlpd: 1111
found SSE2 movmskpd: 8
found SSE2 movsd: 27295
found SSE2 movupd: 80
found SSE2 mulpd: 41882
found SSE2 mulsd: 79686
found SSE2 orpd: 1152
found SSE2 sqrtsd: 8
found SSE2 subsd: 1658
found SSE2 ucomisd: 1392
found SSE2 unpckhpd: 86
found SSE2 unpcklpd: 90
found SSE2 xorpd: 1151
found SSE3 haddpd: 1224
found SSE3 haddps: 530
found SSE3 movddup: 4
found SSE3 movshdup: 2
found SSE3 movsldup: 3
```

It is unclear how much of a performance penalty there is when selecting a Hammer ATLAS for a P4 arch, but it could be substantial. Someone needs to collect some numbers. It might be a good idea to tune the P4 kernels by selecting `-A 16`, but this would require adding tuning info for that config in 64 bits.

In the long term it might be beneficial to build ATLAS libs on various CPUs and then use a runtime selection to put the best version in LD_LIBRARY_PATH. 

I will build an spkg with the above changes since the SSE3 issue is really becoming a problem. One should note that for optimum performance one needs to build from sources. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-21 06:47:16

Ok, no need to do something stupid with the probes. Clint come to the rescue:

```
> * The other issue concerns selecting a maximum SSE level. Right now I
>can pick some Arch, but the SSE level up to SSE3 (==PNI) is determined
>by the probes. So even if I pick a PIII for example I end up with SSE3
>>support if the CPU supplies it. So far the trick I am using is to have
>the SSE probe unconditionally return "FAILURE", so that for example I
>get a SSE2 only ATLAS on a CPU with SSE3 or more. Obviously
>performance will suck, but in case of Sage it is between "illegal
>instructions" and working binaries, so performance  is something I can
>sacrifice for that.
>
>Is there a plan to make the SSE level selectable as a config option?

Not only is there a plan, but it's been available since 3.8.0!  It's not
the easiest thing to grok, because one machine obviously can support many
vector extensions.  Here is the line from 'configure --help':
  -V #    # = ((1<<vecISA1) | (1<<vecISA2) | ... | (1<<vecISAN))

Now, since xprint_enums for some reason doens't print these values out,
I can oh so conveniently scope ATLAS/CONFIG/include/atlconf.h for:
  enum ISAEXT {ISA_None=0, ISA_AV, ISA_SSE3, ISA_SSE2, ISA_SSE1, ISA_3DNow};

Therefore, if I want no vector code at all, I throw '-V -0'; if I want
SSE2 & 1 but not 3, I throw (1<<3)+(1<<4) = 8+16=24, so '-V 24', and
bingo: no SSE3 even on a machine that does SSE3!

Cheers,
Clint
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:31:17

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 18:33:03

This is a 3.4.1 blocker.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 18:33:03

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2009-04-18 06:55:36

The spkg that fixes three tickets (#5219, #5741, #5742) is at

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/atlas-3.8.3.p1.spkg

To test SSE2 only builds set SAGE_SIMD_MODE to "SSE2".

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 23:23:47

Merged in Sage 3.4.1.rc4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 23:23:47

Resolution: fixed
