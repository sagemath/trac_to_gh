# Issue 4655: doctest failure in plot.py with 3.2.1.rc0 on 64-bit SuSe linux

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-11-29 18:36:05

Assignee: was

Keywords: plot

This test fails in 3.2.1.rc0:

```
jec`@`host-57-89%./sage -t  "devel/sage/sage/plot/plot.py"
sage -t  "devel/sage/sage/plot/plot.py"                     
**********************************************************************
File "/home/jec/sage-3.2.1.rc0/devel/sage/sage/plot/plot.py", line 2283:
    sage: adaptive_refinement(sin, (0,0), (pi,0), adaptive_tolerance=0.01)
Expected:
    [(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi, 0.831469612302545...), (0.375*pi, 0.92387953251128674), (0.4375*pi, 0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546), (0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218), (0.875*pi, 0.3826834323650898...)]
Got:
    [(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi, 0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi, 0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254535), (0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218), (0.875*pi, 0.38268343236508989)]
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_47
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jec/sage-3.2.1.rc0/tmp/.doctest_plot.py
	 [38.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage/sage/plot/plot.py"
Total time for all tests: 38.8 seconds
```

on this machine:

```
jec`@`host-57-89%cat /proc/version 
Linux version 2.6.18.8-0.3-default (geeko`@`buildhost) (gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)) #1 SMP Tue Apr 17 08:42:35 UTC 2007
```

with this cpu (*4):

```
processor	: 3
vendor_id	: AuthenticAMD
cpu family	: 15
model		: 65
model name	: Dual-Core AMD Opteron(tm) Processor 2220
stepping	: 3
cpu MHz		: 2800.168
cache size	: 1024 KB
physical id	: 1
siblings	: 2
core id		: 1
cpu cores	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 1
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt rdtscp lm 3dnowext 3dnow pni cx16 lahf_lm cmp_legacy svm cr8_legacy
bogomips	: 5600.76
TLB size	: 1024 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 40 bits physical, 48 bits virtual
power management: ts fid vid ttp tm stc
```


Strange: to me the "..." processing should have dealt with that!


---

Comment by mabshoff created at 2008-11-30 07:15:49

Changing component from graphics to doctest.


---

Comment by mabshoff created at 2008-11-30 07:15:49

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-11-30 07:15:49

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-30 07:15:49

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-30 07:18:26

John's problem is caused by

```
0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546), (0.75*pi, 0.70710678118654757), 
0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254535), (0.75*pi, 0.70710678118654757), 
```


Cheers,

Michael


---

Comment by was created at 2008-11-30 19:53:45

I have a temporary account on John's machine, and have tested the attached patch on it.


---

Attachment

OK, so William's patch worked for me, but that's not much of a test since I tested on the same machine as he did (after applying to 3.2.1.rc0).  But I also applied it on a 32-bit linux machine and it worked fine there too.  It would be a good idea to test it elsewhere, I think.


---

Comment by mabshoff created at 2008-11-30 20:08:40

I have access to two more machines (varro and menas IIRC) where there is numerical noise in plot.py, so I will test it there shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 23:32:05

I am seeing the same failure as John on menas:

```
0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546), (0.75*pi, 
0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254535), (0.75*pi, 
```

On varro we have a slightly different problem:

```
[(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,
[(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654757), (0.3125*pi, 
```


Cheers,

Michael


---

Attachment

trac_4655.2.patch is a slightly updated version of John's patch that also fixes the varro issue. To test apply that patch only.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 00:37:06

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 00:37:20

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-12-01 00:37:20

Resolution: fixed
