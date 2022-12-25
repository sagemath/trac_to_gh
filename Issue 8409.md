# Issue 8409: Fix build and doctest issues for Solaris 10 (SPARC) in 32-bit mode.

archive/issues_008409.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  mvngu\n\nAs of Sage 4.3.3, Sage will not build on Solaris 10 (SPARC). This lists all the items which I'm aware are needed to allow Sage to build, and pass all then normal doctests, excluding the long ones.   \n\n == Hardware used for testing ==\n\nSince 't2' is rather slow, a somewhat ancient and low-spec Sun Blade 1000 was used for these tests. \n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Patches needed to build Sage 4.4.3 on Solaris 10 (SPARC) ==\n\nSage will not build without **all** of the following patches. \n\n* #7867 A patch for Python, which solves an issue from #6583.\n* #8191 Addition of iconv, which was needed following an update to R. \n* #8285 Update R's spkg-install to work on Solaris.\n* #8363 Remove a useless check for mpir in cddlib which breaks Solaris build. \n* #8371 Patch to allow pyprocessing to build on Solaris - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely, so #8371 may be unnecessary). \n\n == Patches needed for Sage to pass all the normal (not long) doctests ==\n\n* #8374 Numerical noise in sage/symbolic/constants_c.pyx\n* #8375 Numerical noise in sage/symbolic/pynac.pyx\n* #8391 Change 'top' to 'prstat' on Solaris, othewise lots of doctests time out.\n* #8408 Update sqlite to the latest version (otherwise #8397, #8398, #8399, #8400 and #8401 all fail).\n\n\n == Long doctests ==\n\nAll long doctests pass, with the exception of the following, which is #8416 \n\n```\nsage -t  -long \"devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py\"\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [3.0 s]\n```\n\n == Other changes ==\n\nIt was necessary to increase SAGE_TIMEOUT. The longest test is taking 460 s on the Blade 1000. Despite the relative age and cost of the T5240 (t2) and my Blade 1000 (redstart), the T5240 is designed for a very different task to what it is used for, so some of the doctests will take longer on 't2'. I would suggest a minimum timeout of 2000 s would be necessary to be sure of no failures due to the lack of speed in 't2'. \n\nAlthough I did increase SAGE_TIMEOUT_LONG to 10000 s from the default 1800, this was no absolutely necessary, as all tests completed in less than 1800 s, although the longest took 1764.9 s, so would have been very close to timing out. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/8409\n\n",
    "closed_at": "2010-07-12T22:55:49Z",
    "created_at": "2010-03-01T16:12:56Z",
    "labels": [
        "component: porting: solaris",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Fix build and doctest issues for Solaris 10 (SPARC) in 32-bit mode.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8409",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  mvngu

As of Sage 4.3.3, Sage will not build on Solaris 10 (SPARC). This lists all the items which I'm aware are needed to allow Sage to build, and pass all then normal doctests, excluding the long ones.   

 == Hardware used for testing ==

Since 't2' is rather slow, a somewhat ancient and low-spec Sun Blade 1000 was used for these tests. 

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Patches needed to build Sage 4.4.3 on Solaris 10 (SPARC) ==

Sage will not build without **all** of the following patches. 

* #7867 A patch for Python, which solves an issue from #6583.
* #8191 Addition of iconv, which was needed following an update to R. 
* #8285 Update R's spkg-install to work on Solaris.
* #8363 Remove a useless check for mpir in cddlib which breaks Solaris build. 
* #8371 Patch to allow pyprocessing to build on Solaris - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely, so #8371 may be unnecessary). 

 == Patches needed for Sage to pass all the normal (not long) doctests ==

* #8374 Numerical noise in sage/symbolic/constants_c.pyx
* #8375 Numerical noise in sage/symbolic/pynac.pyx
* #8391 Change 'top' to 'prstat' on Solaris, othewise lots of doctests time out.
* #8408 Update sqlite to the latest version (otherwise #8397, #8398, #8399, #8400 and #8401 all fail).


 == Long doctests ==

All long doctests pass, with the exception of the following, which is #8416 

```
sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [3.0 s]
```

 == Other changes ==

It was necessary to increase SAGE_TIMEOUT. The longest test is taking 460 s on the Blade 1000. Despite the relative age and cost of the T5240 (t2) and my Blade 1000 (redstart), the T5240 is designed for a very different task to what it is used for, so some of the doctests will take longer on 't2'. I would suggest a minimum timeout of 2000 s would be necessary to be sure of no failures due to the lack of speed in 't2'. 

Although I did increase SAGE_TIMEOUT_LONG to 10000 s from the default 1800, this was no absolutely necessary, as all tests completed in less than 1800 s, although the longest took 1764.9 s, so would have been very close to timing out. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/8409





---

archive/issue_comments_075216.json:
```json
{
    "body": "As reported at #8416 this doctest pass after I rebuilt the Sage library completely. So I believe all doctests should now pass on Solaris 10 - including the long ones. \n\nWe will have to wait and see.",
    "created_at": "2010-03-03T02:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75216",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

As reported at #8416 this doctest pass after I rebuilt the Sage library completely. So I believe all doctests should now pass on Solaris 10 - including the long ones. 

We will have to wait and see.



---

archive/issue_comments_075217.json:
```json
{
    "body": "As of 4.4.alpha1 or alpha2, there are several long doctests which still fail on t2:\n\n```\n        sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py # 2 doctests failed\n        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py # File not found\n        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # File not found\n        sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py # File not found\n        sage -t  -long devel/sage/sage/categories/coxeter_groups.py # File not found\n```\nAll but the first are timeouts; I'll increase SAGE_TIMEOUT_LONG and see what happens.  I don't know what causes the first; I'll open a ticket: #8749.\n\nAs it stands, I'm not sure what we can do about this ticket, so I'm pushing it to Sage 5.0.",
    "created_at": "2010-04-23T05:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75217",
    "user": "https://github.com/jhpalmieri"
}
```

As of 4.4.alpha1 or alpha2, there are several long doctests which still fail on t2:

```
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py # 2 doctests failed
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py # File not found
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # File not found
        sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py # File not found
        sage -t  -long devel/sage/sage/categories/coxeter_groups.py # File not found
```
All but the first are timeouts; I'll increase SAGE_TIMEOUT_LONG and see what happens.  I don't know what causes the first; I'll open a ticket: #8749.

As it stands, I'm not sure what we can do about this ticket, so I'm pushing it to Sage 5.0.



---

archive/issue_events_020150.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-23T05:16:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20150"
}
```



---

archive/issue_comments_075218.json:
```json
{
    "body": "With longer SAGE_TIMEOUT_LONG, tests pass:\n\n```\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py\n         [2238.6 s]\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\n         [3010.0 s]\nsage -t  -long devel/sage/sage/modular/ssmod/ssmod.py\n         [2336.2 s]\nsage -t  -long devel/sage/sage/categories/coxeter_groups.py\n         [3101.2 s]\n```\nexcept for the ones tracked at #8749 and #8750.",
    "created_at": "2010-04-23T14:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75218",
    "user": "https://github.com/jhpalmieri"
}
```

With longer SAGE_TIMEOUT_LONG, tests pass:

```
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py
         [2238.6 s]
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
         [3010.0 s]
sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py
         [2336.2 s]
sage -t  -long devel/sage/sage/categories/coxeter_groups.py
         [3101.2 s]
```
except for the ones tracked at #8749 and #8750.



---

archive/issue_events_020151.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-27T14:24:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20151"
}
```



---

archive/issue_events_020152.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-27T14:24:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "milestone": "sage-4.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20152"
}
```



---

archive/issue_comments_075219.json:
```json
{
    "body": "Once #8749 is fixed, can we close this?",
    "created_at": "2010-04-27T14:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75219",
    "user": "https://github.com/jhpalmieri"
}
```

Once #8749 is fixed, can we close this?



---

archive/issue_comments_075220.json:
```json
{
    "body": "Note a 4.4.3 blocker.",
    "created_at": "2010-06-03T04:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75220",
    "user": "https://github.com/williamstein"
}
```

Note a 4.4.3 blocker.



---

archive/issue_events_020153.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-03T04:13:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "milestone": "sage-4.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20153"
}
```



---

archive/issue_events_020154.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-03T04:13:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20154"
}
```



---

archive/issue_comments_075221.json:
```json
{
    "body": "As of sage 4.4.4, #9127 is the only outstanding doctest issue and that would appear to be related to the low speed of the machines used to perform a test - it creates a timeout. \n\nOnce that is fixed, this ticket can be closed.",
    "created_at": "2010-06-05T19:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75221",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

As of sage 4.4.4, #9127 is the only outstanding doctest issue and that would appear to be related to the low speed of the machines used to perform a test - it creates a timeout. 

Once that is fixed, this ticket can be closed.



---

archive/issue_comments_075222.json:
```json
{
    "body": "This can now be closed. All issues have been resolved, and Sage certainly does build on Solaris 10 (SPARC) while passing all doc tests. \n\nThere are still issues on OpenSolaris, and when building in 64-bits, but all the 32-bit issues have been resolved. I added \"in 32-bit mode\" to the title, so its clear not all issues have been resolved. \n\n#9026 tracks some of the other Solaris/OpenSolaris related issues. #9281 lists the passes and failures for SAGE_CHECK to work on OpenSolaris x64. \n\nDave",
    "created_at": "2010-07-12T22:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75222",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This can now be closed. All issues have been resolved, and Sage certainly does build on Solaris 10 (SPARC) while passing all doc tests. 

There are still issues on OpenSolaris, and when building in 64-bits, but all the 32-bit issues have been resolved. I added "in 32-bit mode" to the title, so its clear not all issues have been resolved. 

#9026 tracks some of the other Solaris/OpenSolaris related issues. #9281 lists the passes and failures for SAGE_CHECK to work on OpenSolaris x64. 

Dave



---

archive/issue_events_020155.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-07-12T22:55:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20155"
}
```



---

archive/issue_comments_075223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-12T22:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8409#issuecomment-75223",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Resolution: fixed



---

archive/issue_events_020156.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-07-13T07:07:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20156"
}
```



---

archive/issue_events_020157.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-07-13T07:07:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8409",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8409#event-20157"
}
```
