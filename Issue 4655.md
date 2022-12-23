# Issue 4655: doctest failure in plot.py with 3.2.1.rc0 on 64-bit SuSe linux

archive/issues_004655.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plot\n\nThis test fails in 3.2.1.rc0:\n\n```\njec@host-57-89%./sage -t  \"devel/sage/sage/plot/plot.py\"\nsage -t  \"devel/sage/sage/plot/plot.py\"                     \n**********************************************************************\nFile \"/home/jec/sage-3.2.1.rc0/devel/sage/sage/plot/plot.py\", line 2283:\n    sage: adaptive_refinement(sin, (0,0), (pi,0), adaptive_tolerance=0.01)\nExpected:\n    [(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi, 0.831469612302545...), (0.375*pi, 0.92387953251128674), (0.4375*pi, 0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546), (0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218), (0.875*pi, 0.3826834323650898...)]\nGot:\n    [(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi, 0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi, 0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254535), (0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218), (0.875*pi, 0.38268343236508989)]\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_47\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/jec/sage-3.2.1.rc0/tmp/.doctest_plot.py\n\t [38.8 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage/sage/plot/plot.py\"\nTotal time for all tests: 38.8 seconds\n```\n\non this machine:\n\n```\njec@host-57-89%cat /proc/version \nLinux version 2.6.18.8-0.3-default (geeko@buildhost) (gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)) #1 SMP Tue Apr 17 08:42:35 UTC 2007\n```\n\nwith this cpu (*4):\n\n```\nprocessor\t: 3\nvendor_id\t: AuthenticAMD\ncpu family\t: 15\nmodel\t\t: 65\nmodel name\t: Dual-Core AMD Opteron(tm) Processor 2220\nstepping\t: 3\ncpu MHz\t\t: 2800.168\ncache size\t: 1024 KB\nphysical id\t: 1\nsiblings\t: 2\ncore id\t\t: 1\ncpu cores\t: 2\nfpu\t\t: yes\nfpu_exception\t: yes\ncpuid level\t: 1\nwp\t\t: yes\nflags\t\t: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt rdtscp lm 3dnowext 3dnow pni cx16 lahf_lm cmp_legacy svm cr8_legacy\nbogomips\t: 5600.76\nTLB size\t: 1024 4K pages\nclflush size\t: 64\ncache_alignment\t: 64\naddress sizes\t: 40 bits physical, 48 bits virtual\npower management: ts fid vid ttp tm stc\n```\n\n\nStrange: to me the \"...\" processing should have dealt with that!\n\nIssue created by migration from https://trac.sagemath.org/ticket/4655\n\n",
    "created_at": "2008-11-29T18:36:05Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "doctest failure in plot.py with 3.2.1.rc0 on 64-bit SuSe linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4655",
    "user": "cremona"
}
```
Assignee: was

Keywords: plot

This test fails in 3.2.1.rc0:

```
jec@host-57-89%./sage -t  "devel/sage/sage/plot/plot.py"
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
jec@host-57-89%cat /proc/version 
Linux version 2.6.18.8-0.3-default (geeko@buildhost) (gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)) #1 SMP Tue Apr 17 08:42:35 UTC 2007
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

Issue created by migration from https://trac.sagemath.org/ticket/4655





---

archive/issue_comments_035056.json:
```json
{
    "body": "Changing component from graphics to doctest.",
    "created_at": "2008-11-30T07:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35056",
    "user": "mabshoff"
}
```

Changing component from graphics to doctest.



---

archive/issue_comments_035057.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2008-11-30T07:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35057",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_035058.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-30T07:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35058",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_035059.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-30T07:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35059",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035060.json:
```json
{
    "body": "John's problem is caused by\n\n```\n0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546), (0.75*pi, 0.70710678118654757), \n0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254535), (0.75*pi, 0.70710678118654757), \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T07:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35060",
    "user": "mabshoff"
}
```

John's problem is caused by

```
0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546), (0.75*pi, 0.70710678118654757), 
0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254535), (0.75*pi, 0.70710678118654757), 
```


Cheers,

Michael



---

archive/issue_comments_035061.json:
```json
{
    "body": "I have a temporary account on John's machine, and have tested the attached patch on it.",
    "created_at": "2008-11-30T19:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35061",
    "user": "was"
}
```

I have a temporary account on John's machine, and have tested the attached patch on it.



---

archive/issue_comments_035062.json:
```json
{
    "body": "Attachment\n\nOK, so William's patch worked for me, but that's not much of a test since I tested on the same machine as he did (after applying to 3.2.1.rc0).  But I also applied it on a 32-bit linux machine and it worked fine there too.  It would be a good idea to test it elsewhere, I think.",
    "created_at": "2008-11-30T20:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35062",
    "user": "cremona"
}
```

Attachment

OK, so William's patch worked for me, but that's not much of a test since I tested on the same machine as he did (after applying to 3.2.1.rc0).  But I also applied it on a 32-bit linux machine and it worked fine there too.  It would be a good idea to test it elsewhere, I think.



---

archive/issue_comments_035063.json:
```json
{
    "body": "I have access to two more machines (varro and menas IIRC) where there is numerical noise in plot.py, so I will test it there shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T20:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35063",
    "user": "mabshoff"
}
```

I have access to two more machines (varro and menas IIRC) where there is numerical noise in plot.py, so I will test it there shortly.

Cheers,

Michael



---

archive/issue_comments_035064.json:
```json
{
    "body": "I am seeing the same failure as John on menas:\n\n```\n0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546), (0.75*pi, \n0.98078528040323043), (0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254535), (0.75*pi, \n```\n\nOn varro we have a slightly different problem:\n\n```\n[(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,\n[(0.125*pi, 0.38268343236508978), (0.1875*pi, 0.55557023301960218), (0.25*pi, 0.70710678118654757), (0.3125*pi, \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T23:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35064",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035065.json:
```json
{
    "body": "Attachment\n\ntrac_4655.2.patch is a slightly updated version of John's patch that also fixes the varro issue. To test apply that patch only.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T00:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35065",
    "user": "mabshoff"
}
```

Attachment

trac_4655.2.patch is a slightly updated version of John's patch that also fixes the varro issue. To test apply that patch only.

Cheers,

Michael



---

archive/issue_comments_035066.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T00:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35066",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_035067.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-12-01T00:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35067",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc1



---

archive/issue_comments_035068.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-01T00:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4655#issuecomment-35068",
    "user": "mabshoff"
}
```

Resolution: fixed
