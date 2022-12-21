# Issue 2108: atlas tuning info for intel prescott cpus

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-02-08 10:36:48

Assignee: mabshoff

Attached file includes ATLAS tuning information for Intel prescott cpu's. It was generated using the instructions in ticket:1886.

Here is the sage-devel thread:

http://groups.google.com/group/sage-devel/msg/b61176e3e1a2189e

Since ATLAS doesn't detect my cpu properly, the architecture name it uses is `UNKNOWNx8632SSE3`. Should I do anything to change this?

Here is the output from `/proc/cpuinfo`:


```
vendor_id       : GenuineIntel
cpu family      : 15
model           : 6
model name      : Intel(R) Pentium(R) D CPU 3.40GHz
stepping        : 4
cpu MHz         : 3400.160
cache size      : 2048 KB
physical id     : 0
siblings        : 2
core id         : 1
cpu cores       : 2
fdiv_bug        : no
hlt_bug         : no
f00f_bug        : no
coma_bug        : no
fpu             : yes
fpu_exception   : yes
cpuid level     : 6
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe nx lm constant_tsc pni monitor ds_cpl est cid cx16 xtpr lahf_lm
bogomips        : 6800.17
```



---

Attachment

atlas tuning info for intel prescott


---

Comment by mabshoff created at 2008-02-12 18:31:03

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-12 18:31:03

Ok, we now need to add proper ATLAS detection of Prescott CPUs to merge this.

Cheers,

Michael


---

Comment by burcin created at 2008-03-16 13:39:48

tuning info after patching atlas to recognize new arch


---

Attachment

make atlas detect p4d arch


---

Attachment

attachment:atlas_arch_p4d.patch provides the detection, and attachment:P4D32SSE3.tgz is the new tuning info. 

Looking forward to a new atlas package. :)


---

Comment by mabshoff created at 2008-03-16 19:17:44

Replying to [comment:2 burcin]:
> attachment:atlas_arch_p4d.patch provides the detection, and attachment:P4D32SSE3.tgz is the new tuning info. 
> 
> Looking forward to a new atlas package. :)

Trac is buggy with attached tgz archives, so it is better to link them. I can get at those via directly accessing sagemath.org. The interesting tgz is now at

http://sage.math.washington.edu/home/mabshoff/ATLAS-tune/P4D32SSE3.tgz

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-20 10:56:57

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 10:56:57

Merged in Sage 2.11.alpha0 via #2260.
