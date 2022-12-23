# Issue 5998: add fxsr to cpuflags.txt

Issue created by migration from https://trac.sagemath.org/ticket/5998

Original creator: was

Original creation time: 2009-05-06 18:26:44

Assignee: mabshoff


```


On Wed, May 6, 2009 at 7:01 AM, gemili <> wrote:
>
> Thank you for the fast answer.
>
> 1.) One of my computers is a  five year old "Fujitsu-Siemens Livebook
> C1110D"
> 1a) I tried WindowsXP, SP3 --> SAGE 3.4.1 did not work.
> 1b) I tried WindowsXP, SP2 --> SAGE 3.4.1 did not work.
> 1c) I tried the "Sage LiveCD" (which has its own UNIX operation
> system) on this computer and it also didn't work. Maybe it is a hint,
> that the problem is independent from the Operating system (but it can
> be also a problem with the LiveCD).
>
> 1d) Following is the result of cat   /proc/cpuinfo for this computer:
> processor: : 0
> vendor_id: GenuineIntel
> cpu family: 6
> model: 9
> model name: Intel(R) Pentium(R) M processor 1400Mhz
> stepping: 5
> cpu Mhz: 1399.177
> cache size: 1024 kB
> fdiv_bug: no
> hlt_bug: no
> f00f_bug: no
> coma_bug: no
> fpu: yes
> fpu_exeption: yes
> cupid level: 2
> wp: yes
> flags: fpu vme de pse tsc msr mce cx8 apic sep mtrr pge mca cmov pat
> clflush dts acpi mmx fxsr sse sse2 up
> bogomips: 2803.98
>
> 2.) Second computer is a Desktop with WindowsXP, SP3.
> 2a) When starting SAGE 3.4.1, it will not work and I receive the error
> message concerning the sse2 flag. (I don't receive this message with
> the above mentioned Siemens Laptop, No 1.). The message is
> "Warning! This Sage install was build on a machine that supports
> instructions  that are not available on this   computer. Sage will
> likely fail with Illegal Instruction errors! The following processor
> flags were on the build machine
>  but are not on this vomputer:   sse2 "
>
> 2b) Following is the result of this Desktop:
>
> processor: : 0
> vendor_id: AuthenticAMD
> cpu family: 6
> model: 8
> model name: AMD Athlon (TM) XP2200+
> stepping: 1
> cpu Mhz: 1799.135
> cache size: 256 kB
> fdiv_bug: no
> hlt_bug: no
> f00f_bug: no
> coma_bug: no
> fpu: yes
> fpu_exeption: yes
> cupid level: 1
> wp: yes
> flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov
> pat pse36 mmx fxsr sse syscall mmxext 3dnowext 3dnow up ts
> bogomips: 3615.72
>
> 3) The third computer is also a Desktop. SAGE 3.4.1 is running on this
> computer under WindowsXP, Service Pack 2.
>
> 3a) Cpuinfo reports the following flages: "fpu vme de pse tsc msr pae
> mce cx8 apic sep mtrr pge cmov pat clflush acpi mmx fxse sse sse2 nx
> up pni rng rng_en ace ace_en."
>
>
> RESULT:
> Computer No 1 has the sse2 flag, but doesn't run SAGE 3.4.1 (SAGE
> 3.2.3 did run). Computer No. 2 doen't have the sse2 flag and doesn't
> run SAGE 3.4.1. Computer No. 3 has the ss2 flag and runs SAGE 3.4.1.
>

Computer no 2 should not be able to run Sage, so let's ignore that for now.

Compute 1: doesn't run Sage

Computer 3: runs Sage

We have

# computer 1
sage: a = "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge cmov pat clflush acpi mmx fxse sse sse2 nx up pni rng rng_en ace ace_en."
# computer 3
sage: b = "fpu vme de pse tsc msr mce cx8 apic sep mtrr pge mca cmov pat clflush dts acpi mmx fxsr sse sse2 up"
sage: a = set(a.split())
sage: b = set(b.split())

# what (1) has the (3) doesn't:
sage: ' '.join([x for x in a if x not in b])
'fxse nx rng_en pae ace_en. rng pni ace'

# what (3) has the (1) doesn't:
sage: ' '.join([x for x in b if x not in a])
'fxsr mca dts'

This suggests that fxsr, mca, or dts is relevant.  My build machine has all those flags, but your machine (1) doesn't.

fxsr is: "FXSAVE/FXRSTOR. (The FXSAVE instruction writes the current state of the x87 FPU, MMX technology, Streaming SIMD Extensions, and Streaming SIMD Extensions 2 data, control, and status registers to the destination operand. The destination is a 512-byte memory location. FXRSTOR will restore the state saves)."

dts is your digital thermal sensor, which is irrelevant. 

mca is "Machine Check Architecture."  No clue.

This is from http://blog.hbcom.info/archives/152/.   

Your testing thus suggests that fxsr is really important, and we should be explicitly checking for it and not allowing Sage to run if the user doesn't have it.  Also, we should look to see what part(s) of sage actually use it. 


> The result seams to be independent from SP2 or SP3.
>
> Maybe it would be a good idea to compile Sage without the sse2 flag
> (whatever it is...)
>
> Hopefully it helps.
> Gemili

```



---

Comment by mabshoff created at 2009-05-06 21:38:34

I doubt `fxsr` is relevant here since it has been around for well over 10 years or so, but MPIR is just build with too modern an instruction set. Unless someone gets me properly disassembled gdb backtraces we cannot determine which instruction is relevant here.


---

Comment by was created at 2010-01-17 11:00:45

I agree with mabshoff's remark above that we shouldn't add fxsr, even though it would be really easy.  Also, more compelling is that fxsr has never come up otherwise on any Sage mailing list.  I'm closing this as wontfix.


---

Comment by was created at 2010-01-17 11:00:45

Resolution: wontfix
