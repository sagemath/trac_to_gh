# Issue 9338: upgrade PyCrypto to upstream 2.1.0

archive/issues_009338.json:
```json
{
    "body": "Assignee: tbd\n\nAs the subject says. The latest version also fixes the issue with ARC2 reported at http://www.securityfocus.com/bid/33674/info. Currently, the PyCrypto spkg maintains patches for this issue. Upgrading to the latest upstream version would mean we no longer need to maintain those patches in the spkg itself.\n\n**Apply:**\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/pycrypto/pycrypto-2.1.0.spkg\n\nChanges in this upgraded spkg include:\n\n* Upgrade to PyCrypto 2.1.0.\n* The bug at http://www.securityfocus.com/bid/33674/info is fixed in PyCrypto 2.1.0, so remove patches/ARC2.c and patches/ARC2.c.patch.\n* Flesh out and update the file SPKG.txt.\n* Add spkg-check to run the test suite of PyCrypto.\n* Add a check to spkg-install to check that PyCrypto installs fine.\n\nMake sure to update #9281 when spkg-check runs the test suite fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9338\n\n",
    "closed_at": "2010-08-09T09:38:15Z",
    "created_at": "2010-06-25T19:24:19Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "upgrade PyCrypto to upstream 2.1.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

As the subject says. The latest version also fixes the issue with ARC2 reported at http://www.securityfocus.com/bid/33674/info. Currently, the PyCrypto spkg maintains patches for this issue. Upgrading to the latest upstream version would mean we no longer need to maintain those patches in the spkg itself.

**Apply:**

http://sage.math.washington.edu/home/mvngu/spkg/standard/pycrypto/pycrypto-2.1.0.spkg

Changes in this upgraded spkg include:

* Upgrade to PyCrypto 2.1.0.
* The bug at http://www.securityfocus.com/bid/33674/info is fixed in PyCrypto 2.1.0, so remove patches/ARC2.c and patches/ARC2.c.patch.
* Flesh out and update the file SPKG.txt.
* Add spkg-check to run the test suite of PyCrypto.
* Add a check to spkg-install to check that PyCrypto installs fine.

Make sure to update #9281 when spkg-check runs the test suite fine.

Issue created by migration from https://trac.sagemath.org/ticket/9338





---

archive/issue_comments_088086.json:
```json
{
    "body": "I'm still testing this spkg, so it's not ready for review.",
    "created_at": "2010-06-25T20:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm still testing this spkg, so it's not ready for review.



---

archive/issue_comments_088087.json:
```json
{
    "body": "The test results are summarized below. I only ran the spkg-check script of the PyCrypto spkg. This was tested with Sage 4.4.4. With the exception of cicero.skynet, all machines reported here are 64-bit.\n\n1. bsd.math: Mac OS X 10.6.4, GCC 4.2.1, Dual-Core Intel Xeon `@` 2.66 GHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n2. cicero.skynet: 32-bit Fedora 12, GCC 4.5.0, Intel(R) Pentium(R) 4 CPU `@` 2.66GHz\n   * build: yes\n   * doctest: one failure in `libs/mwrank/mwrank.pyx`, as reported [here](https://groups.google.com/group/sage-release/browse_thread/thread/20dcc2ac0c5b978c)\n   * spkg-check: pass\n3. cleo.skynet: Red Hat Enterprise Linux Server 5.3, GCC 4.5.0, IA-64 Itanium 2 `@` 1594.000726 MHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n4. eno.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(R) CPU E5345 `@` 2.33GHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n5. flavius.skynet: Fedora 12, GCC 4.5.0, AMD Opteron(tm) Processor 248 `@` 2193.570 MHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n6. gcc11.fsffrance: Debian 5.0, GCC 4.3.2, Dual-Core AMD Opteron(tm) Processor 2212 `@` 2000.085 MHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n7. gcc16.fsffrance: Debian 5.0, GCC 4.3.2, Quad-Core AMD Opteron(tm) Processor 8354 `@` 2194.496 MHz\n   * build: yes\n   * doctest: [2 failures](https://groups.google.com/group/sage-release/browse_thread/thread/7a8a2e2af0eafde7) in `schemes/elliptic_curves/lseries_ell.py`\n   * spkg-check: pass\n8. gcc100.fsffrance: Debian 5.0, GCC 4.3.2, AMD Opteron(tm) Processor 252 `@` 2600.011 MHz\n   * build: yes\n   * doctest: failures in `modules/free_module.py`\n   * spkg-check: pass\n9. iras.skynet: SUSE Linux Enterprise Server 10 SP1, GCC 4.5.0, IA-64 `@` 1594.000683 MHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n10. lena.skynet: Fedora 12, GCC 4.5.0, AMD Phenom(tm) II X4 940 Processor `@` 3000.000 MHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n11. menas.skynet: openSUSE 11.1, GCC 4.5.0, Intel(R) Core(TM)2 Quad CPU Q6600 `@` 2.40GHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n12. rh.math: Ubuntu 10.04 LTS, GCC 4.4.3, Six-Core AMD Opteron(tm) Processor 8439 SE `@` 800.000 MHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n13. sage.math: Ubuntu 8.04.4 LTS, GCC 4.2.4, Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n14. sextus.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(TM) CPU `@` 3.60GHz\n   * build: yes\n   * doctest: pass\n   * spkg-check: pass\n15. taurus.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(R) CPU X5570 `@` 2.93GHz\n   * build: no, due to Linbox failing to build on taurus. This is a known issue. But forcing an installation of the PyCrypto spkg with \"./sage -f <...>\", and then running spkg-check, worked fine.\n   * doctest: N/A since Sage 4.4.4 fails to build on taurus\n   * spkg-check: pass",
    "created_at": "2010-06-26T10:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The test results are summarized below. I only ran the spkg-check script of the PyCrypto spkg. This was tested with Sage 4.4.4. With the exception of cicero.skynet, all machines reported here are 64-bit.

1. bsd.math: Mac OS X 10.6.4, GCC 4.2.1, Dual-Core Intel Xeon `@` 2.66 GHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
2. cicero.skynet: 32-bit Fedora 12, GCC 4.5.0, Intel(R) Pentium(R) 4 CPU `@` 2.66GHz
   * build: yes
   * doctest: one failure in `libs/mwrank/mwrank.pyx`, as reported [here](https://groups.google.com/group/sage-release/browse_thread/thread/20dcc2ac0c5b978c)
   * spkg-check: pass
3. cleo.skynet: Red Hat Enterprise Linux Server 5.3, GCC 4.5.0, IA-64 Itanium 2 `@` 1594.000726 MHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
4. eno.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(R) CPU E5345 `@` 2.33GHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
5. flavius.skynet: Fedora 12, GCC 4.5.0, AMD Opteron(tm) Processor 248 `@` 2193.570 MHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
6. gcc11.fsffrance: Debian 5.0, GCC 4.3.2, Dual-Core AMD Opteron(tm) Processor 2212 `@` 2000.085 MHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
7. gcc16.fsffrance: Debian 5.0, GCC 4.3.2, Quad-Core AMD Opteron(tm) Processor 8354 `@` 2194.496 MHz
   * build: yes
   * doctest: [2 failures](https://groups.google.com/group/sage-release/browse_thread/thread/7a8a2e2af0eafde7) in `schemes/elliptic_curves/lseries_ell.py`
   * spkg-check: pass
8. gcc100.fsffrance: Debian 5.0, GCC 4.3.2, AMD Opteron(tm) Processor 252 `@` 2600.011 MHz
   * build: yes
   * doctest: failures in `modules/free_module.py`
   * spkg-check: pass
9. iras.skynet: SUSE Linux Enterprise Server 10 SP1, GCC 4.5.0, IA-64 `@` 1594.000683 MHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
10. lena.skynet: Fedora 12, GCC 4.5.0, AMD Phenom(tm) II X4 940 Processor `@` 3000.000 MHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
11. menas.skynet: openSUSE 11.1, GCC 4.5.0, Intel(R) Core(TM)2 Quad CPU Q6600 `@` 2.40GHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
12. rh.math: Ubuntu 10.04 LTS, GCC 4.4.3, Six-Core AMD Opteron(tm) Processor 8439 SE `@` 800.000 MHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
13. sage.math: Ubuntu 8.04.4 LTS, GCC 4.2.4, Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
14. sextus.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(TM) CPU `@` 3.60GHz
   * build: yes
   * doctest: pass
   * spkg-check: pass
15. taurus.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(R) CPU X5570 `@` 2.93GHz
   * build: no, due to Linbox failing to build on taurus. This is a known issue. But forcing an installation of the PyCrypto spkg with "./sage -f <...>", and then running spkg-check, worked fine.
   * doctest: N/A since Sage 4.4.4 fails to build on taurus
   * spkg-check: pass



---

archive/issue_comments_088088.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-26T10:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88088",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088089.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-06-26T10:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88089",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_088090.json:
```json
{
    "body": "I'm still waiting for build/test results on t2.math.",
    "created_at": "2010-06-26T10:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88090",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm still waiting for build/test results on t2.math.



---

archive/issue_comments_088091.json:
```json
{
    "body": "Build fine on t2.math and `spkg-check` of PyCrypto passes. This is now ready for review.",
    "created_at": "2010-06-27T10:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88091",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Build fine on t2.math and `spkg-check` of PyCrypto passes. This is now ready for review.



---

archive/issue_comments_088092.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-06-27T10:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_088093.json:
```json
{
    "body": "Also build fine on Cygwin (`winxp2`) and spkg-check pass.",
    "created_at": "2010-06-27T18:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Also build fine on Cygwin (`winxp2`) and spkg-check pass.



---

archive/issue_comments_088094.json:
```json
{
    "body": "You have clearly tested this thoroughly Minh - I wish all Sage developers were like you. \n\nI just tested it on two systems:\n\n* OpenSolaris 2009.06 on a 3.33 GHz Intel W3580 Xeon. 64-bit build. All tests in `spkg-check` pass. Since Sage crashes immediately on startup, I can't comment on doctests. \n* Solaris 10 on a Sun Blade 2000, with two Sun UltraSPARC III+ processors. 64-bit build. All tests in `spkg-check` pass. Since Sage is unstable on 64-bit Solaris 10 on SPARC, it's pointless me running any doctests. (Sage does now just about work on 64-bit SPARC. I got it running for the first time yesterday, so needless to say, it is far from perfect). \n\n`hg status`\n\nshows no problems, so positive review.\n\nDave",
    "created_at": "2010-07-16T21:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88094",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

You have clearly tested this thoroughly Minh - I wish all Sage developers were like you. 

I just tested it on two systems:

* OpenSolaris 2009.06 on a 3.33 GHz Intel W3580 Xeon. 64-bit build. All tests in `spkg-check` pass. Since Sage crashes immediately on startup, I can't comment on doctests. 
* Solaris 10 on a Sun Blade 2000, with two Sun UltraSPARC III+ processors. 64-bit build. All tests in `spkg-check` pass. Since Sage is unstable on 64-bit Solaris 10 on SPARC, it's pointless me running any doctests. (Sage does now just about work on 64-bit SPARC. I got it running for the first time yesterday, so needless to say, it is far from perfect). 

`hg status`

shows no problems, so positive review.

Dave



---

archive/issue_comments_088095.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T21:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88095",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088096.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9338#issuecomment-88096",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023019.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:38:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9338",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9338#event-23019"
}
```
