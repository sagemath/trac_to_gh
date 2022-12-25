# Issue 2108: atlas tuning info for intel prescott cpus

archive/issues_002108.json:
```json
{
    "body": "Assignee: mabshoff\n\nAttached file includes ATLAS tuning information for Intel prescott cpu's. It was generated using the instructions in ticket:1886.\n\nHere is the sage-devel thread:\n\nhttp://groups.google.com/group/sage-devel/msg/b61176e3e1a2189e\n\nSince ATLAS doesn't detect my cpu properly, the architecture name it uses is `UNKNOWNx8632SSE3`. Should I do anything to change this?\n\nHere is the output from `/proc/cpuinfo`:\n\n\n```\nvendor_id       : GenuineIntel\ncpu family      : 15\nmodel           : 6\nmodel name      : Intel(R) Pentium(R) D CPU 3.40GHz\nstepping        : 4\ncpu MHz         : 3400.160\ncache size      : 2048 KB\nphysical id     : 0\nsiblings        : 2\ncore id         : 1\ncpu cores       : 2\nfdiv_bug        : no\nhlt_bug         : no\nf00f_bug        : no\ncoma_bug        : no\nfpu             : yes\nfpu_exception   : yes\ncpuid level     : 6\nwp              : yes\nflags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe nx lm constant_tsc pni monitor ds_cpl est cid cx16 xtpr lahf_lm\nbogomips        : 6800.17\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2108\n\n",
    "created_at": "2008-02-08T10:36:48Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "atlas tuning info for intel prescott cpus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2108",
    "user": "https://github.com/burcin"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2108





---

archive/issue_comments_013714.json:
```json
{
    "body": "Attachment [UNKNOWNx8632SSE3.tgz](tarball://root/attachments/some-uuid/ticket2108/UNKNOWNx8632SSE3.tgz) by @burcin created at 2008-02-08 10:37:16\n\natlas tuning info for intel prescott",
    "created_at": "2008-02-08T10:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13714",
    "user": "https://github.com/burcin"
}
```

Attachment [UNKNOWNx8632SSE3.tgz](tarball://root/attachments/some-uuid/ticket2108/UNKNOWNx8632SSE3.tgz) by @burcin created at 2008-02-08 10:37:16

atlas tuning info for intel prescott



---

archive/issue_comments_013715.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-12T18:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013716.json:
```json
{
    "body": "Ok, we now need to add proper ATLAS detection of Prescott CPUs to merge this.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-12T18:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, we now need to add proper ATLAS detection of Prescott CPUs to merge this.

Cheers,

Michael



---

archive/issue_comments_013717.json:
```json
{
    "body": "tuning info after patching atlas to recognize new arch",
    "created_at": "2008-03-16T13:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13717",
    "user": "https://github.com/burcin"
}
```

tuning info after patching atlas to recognize new arch



---

archive/issue_comments_013718.json:
```json
{
    "body": "Attachment [P4D32SSE3.tgz](tarball://root/attachments/some-uuid/ticket2108/P4D32SSE3.tgz) by @burcin created at 2008-03-16 13:41:25\n\nmake atlas detect p4d arch",
    "created_at": "2008-03-16T13:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13718",
    "user": "https://github.com/burcin"
}
```

Attachment [P4D32SSE3.tgz](tarball://root/attachments/some-uuid/ticket2108/P4D32SSE3.tgz) by @burcin created at 2008-03-16 13:41:25

make atlas detect p4d arch



---

archive/issue_comments_013719.json:
```json
{
    "body": "Attachment [atlas_arch_p4d.patch](tarball://root/attachments/some-uuid/ticket2108/atlas_arch_p4d.patch) by @burcin created at 2008-03-16 13:45:39\n\nattachment:atlas_arch_p4d.patch provides the detection, and attachment:P4D32SSE3.tgz is the new tuning info. \n\nLooking forward to a new atlas package. :)",
    "created_at": "2008-03-16T13:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13719",
    "user": "https://github.com/burcin"
}
```

Attachment [atlas_arch_p4d.patch](tarball://root/attachments/some-uuid/ticket2108/atlas_arch_p4d.patch) by @burcin created at 2008-03-16 13:45:39

attachment:atlas_arch_p4d.patch provides the detection, and attachment:P4D32SSE3.tgz is the new tuning info. 

Looking forward to a new atlas package. :)



---

archive/issue_comments_013720.json:
```json
{
    "body": "Replying to [comment:2 burcin]:\n> attachment:atlas_arch_p4d.patch provides the detection, and attachment:P4D32SSE3.tgz is the new tuning info. \n> \n> Looking forward to a new atlas package. :)\n\nTrac is buggy with attached tgz archives, so it is better to link them. I can get at those via directly accessing sagemath.org. The interesting tgz is now at\n\nhttp://sage.math.washington.edu/home/mabshoff/ATLAS-tune/P4D32SSE3.tgz\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T19:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 burcin]:
> attachment:atlas_arch_p4d.patch provides the detection, and attachment:P4D32SSE3.tgz is the new tuning info. 
> 
> Looking forward to a new atlas package. :)

Trac is buggy with attached tgz archives, so it is better to link them. I can get at those via directly accessing sagemath.org. The interesting tgz is now at

http://sage.math.washington.edu/home/mabshoff/ATLAS-tune/P4D32SSE3.tgz

Cheers,

Michael



---

archive/issue_comments_013721.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T10:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002268.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-20T10:56:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2108#event-2268"
}
```



---

archive/issue_comments_013722.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0 via #2260.",
    "created_at": "2008-03-20T10:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2108#issuecomment-13722",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0 via #2260.
