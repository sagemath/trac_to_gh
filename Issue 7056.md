# Issue 7056: Fix build issues so Sage builds with the Sun Studio Compiler suite.

archive/issues_007056.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @fchapoton\n\nSun's compiler on Solaris produces faster code than gcc, and is more reliable with 64-bit code than gcc. This ticket outlines the issues that need to be resolved to get Sage to build on Sun Studio, and are specific to Sun Studio. As more are discovered, I'll add them to the description, so it's easy to them all, rather than find them buried well down the page. \n\nIn many cases, the bugs can potentially affect all compilers, but are only observed on Sun Studio. \n\nThe hostname of at least one machine \n\n|            |            |             |        |         |         |                |              |        |\n|------------|------------|-------------|--------|---------|---------|----------------|--------------|--------|\n|**Hostname**|**Hardware**|**Processor**|**CPUs**|**Cores**|**Speed**|**Architecture**|**OS version**|Compiler|\n|swan|Sun Blade 2000|UltraSPARC-III+|2|2|1200 MHz|sun4u|Solaris 10 update 7|Sun Studio 12.1|\n|t2|Sun T5240|SPARC T2+|2|16|1167 MHz|sun4v|Solaris 10 update 7|Sun Studio 12|\n|main-webserver|Sun Ultra 60|UltraSPARC-II|2|2| 450 MHz |sun4u|Solaris 10 update 4||\n\nThe actual bugs found, along with the trac number are listed below. The hostname is marked as N/A if they are expected to be seen on any Solaris host, but if they are only expected to be seen on some hosts, then the hostname on which the bug was found are listed. \n\n|               |            |          |           |\n|---------------|------------|----------|-----------|\n|**Description**|**hostname**|**Trac #**|**Note(s)**|\n|                             ||     | |\n|-----------------------------||-----|-|\n|Update prereq from 0.3 to 0.4||#7021|1|\n|zn_poly-0.9 uses gcc, irrespective of setting of CC||#7039|2|\n|symmetrica ignores CC||#7032|2|\n|ATLAS ignores CC variable, then dumps core when trying to build with Sun Studio on Solaris|swan|#7048|2,3|\n|Flint ignores CC and CXX||#7024|2|\n|lapack sends GNU option -fPIC to Sun fortran compiler||#7047||\n|eclib 20080310.p7 has code Sun's C++ compiler does not understand||#7044||\n|Code actually in Sage (not other project) ignores CC and uses gcc||#7040|2|\n|ntl 5.4.2.p9 passes -fPIC to Sun linker with Sun Studio||#7043||\n|givaro 3.2.13rc2 says GMP is not installed, even though MPIR is|swan|#7025|4,5|\n|linbox 1.1.6.p0 says GMP is not installed, even though MPIR is|swan|#7026|4,5|\n|R sends the correct Sun flags to C and C++ compilers, but not Fortran||#7035||\n|GAP purposely unsets CC which screws up Sun Studio build||#7041|6|\n|libm4ri thinks the C compiler is broken|swan|#7037||\n|rubiks ignroes CXX and uses g++ even if CXX is Sun compiler||#7036||\n|ratpoints 2.1.2.p2 ignores CC and uses gcc whatever||#7038|2|\n|ibfplll can't find _gmpz_init in -lgmp||#7033|5|\n**Notes**\n\n1) This update should have benefits to Sage on any platform, with any compiler. It is however **absolutely essential** this is fixed for Sun Studio. \n\n2) Although discovered when testing with Sun Studio, the bug relates to the failure of a program to properly observe CC, CXX or SAGE_FORTRAN, so it can be expected to exist with any compiler.\n\n3) The core dump was observed on hostname 'swan'. The failure to observe CC can be expected on any platform, but dumping core may be only on this machine. \n\n4) Checked only on the hostname. This may or may not be specific to that machine.\n\n5) Tickets #7025, #7026 and #7033 are very closely related, as they all relate to a failure of a program to reconsise GMP being installed. Of course, it is not installed, but MPIR is, which is a substitute. \n\n6) Although easy to fix, to do some introduces a major impact on the time to build Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7056\n\n",
    "created_at": "2009-09-28T20:23:10Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix build issues so Sage builds with the Sun Studio Compiler suite.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7056",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @fchapoton

Sun's compiler on Solaris produces faster code than gcc, and is more reliable with 64-bit code than gcc. This ticket outlines the issues that need to be resolved to get Sage to build on Sun Studio, and are specific to Sun Studio. As more are discovered, I'll add them to the description, so it's easy to them all, rather than find them buried well down the page. 

In many cases, the bugs can potentially affect all compilers, but are only observed on Sun Studio. 

The hostname of at least one machine 

|            |            |             |        |         |         |                |              |        |
|------------|------------|-------------|--------|---------|---------|----------------|--------------|--------|
|**Hostname**|**Hardware**|**Processor**|**CPUs**|**Cores**|**Speed**|**Architecture**|**OS version**|Compiler|
|swan|Sun Blade 2000|UltraSPARC-III+|2|2|1200 MHz|sun4u|Solaris 10 update 7|Sun Studio 12.1|
|t2|Sun T5240|SPARC T2+|2|16|1167 MHz|sun4v|Solaris 10 update 7|Sun Studio 12|
|main-webserver|Sun Ultra 60|UltraSPARC-II|2|2| 450 MHz |sun4u|Solaris 10 update 4||

The actual bugs found, along with the trac number are listed below. The hostname is marked as N/A if they are expected to be seen on any Solaris host, but if they are only expected to be seen on some hosts, then the hostname on which the bug was found are listed. 

|               |            |          |           |
|---------------|------------|----------|-----------|
|**Description**|**hostname**|**Trac #**|**Note(s)**|
|                             ||     | |
|-----------------------------||-----|-|
|Update prereq from 0.3 to 0.4||#7021|1|
|zn_poly-0.9 uses gcc, irrespective of setting of CC||#7039|2|
|symmetrica ignores CC||#7032|2|
|ATLAS ignores CC variable, then dumps core when trying to build with Sun Studio on Solaris|swan|#7048|2,3|
|Flint ignores CC and CXX||#7024|2|
|lapack sends GNU option -fPIC to Sun fortran compiler||#7047||
|eclib 20080310.p7 has code Sun's C++ compiler does not understand||#7044||
|Code actually in Sage (not other project) ignores CC and uses gcc||#7040|2|
|ntl 5.4.2.p9 passes -fPIC to Sun linker with Sun Studio||#7043||
|givaro 3.2.13rc2 says GMP is not installed, even though MPIR is|swan|#7025|4,5|
|linbox 1.1.6.p0 says GMP is not installed, even though MPIR is|swan|#7026|4,5|
|R sends the correct Sun flags to C and C++ compilers, but not Fortran||#7035||
|GAP purposely unsets CC which screws up Sun Studio build||#7041|6|
|libm4ri thinks the C compiler is broken|swan|#7037||
|rubiks ignroes CXX and uses g++ even if CXX is Sun compiler||#7036||
|ratpoints 2.1.2.p2 ignores CC and uses gcc whatever||#7038|2|
|ibfplll can't find _gmpz_init in -lgmp||#7033|5|
**Notes**

1) This update should have benefits to Sage on any platform, with any compiler. It is however **absolutely essential** this is fixed for Sun Studio. 

2) Although discovered when testing with Sun Studio, the bug relates to the failure of a program to properly observe CC, CXX or SAGE_FORTRAN, so it can be expected to exist with any compiler.

3) The core dump was observed on hostname 'swan'. The failure to observe CC can be expected on any platform, but dumping core may be only on this machine. 

4) Checked only on the hostname. This may or may not be specific to that machine.

5) Tickets #7025, #7026 and #7033 are very closely related, as they all relate to a failure of a program to reconsise GMP being installed. Of course, it is not installed, but MPIR is, which is a substitute. 

6) Although easy to fix, to do some introduces a major impact on the time to build Sage.

Issue created by migration from https://trac.sagemath.org/ticket/7056





---

archive/issue_comments_058291.json:
```json
{
    "body": "Should be closed as outdated.",
    "created_at": "2020-04-01T14:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7056#issuecomment-58291",
    "user": "https://github.com/mkoeppe"
}
```

Should be closed as outdated.



---

archive/issue_comments_058292.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-01T14:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7056#issuecomment-58292",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058293.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-01T14:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7056#issuecomment-58293",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_058294.json:
```json
{
    "body": "agreed again",
    "created_at": "2020-04-01T14:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7056#issuecomment-58294",
    "user": "https://github.com/fchapoton"
}
```

agreed again



---

archive/issue_events_007276.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-04-01T14:21:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7056",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7056#event-7276"
}
```
