# Issue 4966: Switch gmp to eMPIRe svn1555

archive/issues_004966.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mwhansen\n\nThe eMPIRe.spkg is nearly a drop in for the old gmp-4.2.1.spkg. There are a couple doctests to fix (see upcoming patches) and the ecmgmp.spkg also needs a bump since it requires a recompile. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4966\n\n",
    "created_at": "2009-01-12T06:19:49Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Switch gmp to eMPIRe svn1555",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @mwhansen

The eMPIRe.spkg is nearly a drop in for the old gmp-4.2.1.spkg. There are a couple doctests to fix (see upcoming patches) and the ecmgmp.spkg also needs a bump since it requires a recompile. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4966





---

archive/issue_comments_037718.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-12T06:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037719.json:
```json
{
    "body": "The spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/spkgs/gmp-mpir-svn1555.spkg\n\nTo review also apply the two patches I will add momentarily. One also needs to force a rebuild of ecmgmp and the libecm extension. During the upgrade this will be accomplished via #5016.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T16:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg can be found at

http://sage.math.washington.edu/home/mabshoff/spkgs/gmp-mpir-svn1555.spkg

To review also apply the two patches I will add momentarily. One also needs to force a rebuild of ecmgmp and the libecm extension. During the upgrade this will be accomplished via #5016.

Cheers,

Michael



---

archive/issue_comments_037720.json:
```json
{
    "body": "Attachment [trac_4966_doc.patch](tarball://root/attachments/some-uuid/ticket4966/trac_4966_doc.patch) by mabshoff created at 2009-01-18 16:59:05",
    "created_at": "2009-01-18T16:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4966_doc.patch](tarball://root/attachments/some-uuid/ticket4966/trac_4966_doc.patch) by mabshoff created at 2009-01-18 16:59:05



---

archive/issue_comments_037721.json:
```json
{
    "body": "Attachment [trac_4966_sage.patch](tarball://root/attachments/some-uuid/ticket4966/trac_4966_sage.patch) by mabshoff created at 2009-01-18 17:01:24\n\nNote that the spkg is larger than the old one due to two things:\n\n* we are shipping a copy of yasm to build MPIR since the one in the system is usually too buggy to work\n* we are shipping Brian Gladman's VS 2008 build files\n\nThe spkg has been tested on\n\n* FC 9 x86\n* FC 9, OpenSUSE 10.3 x86-64\n* RHEL 5.2, SLES 10 Itanium\n* Solaris 10 Sparc and x86\n* OSX 10.4 ppc\n* OSX 10.5 x86 *and* x86-64\n* YDL 6.1 PS3 (a G5 variant)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T17:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4966_sage.patch](tarball://root/attachments/some-uuid/ticket4966/trac_4966_sage.patch) by mabshoff created at 2009-01-18 17:01:24

Note that the spkg is larger than the old one due to two things:

* we are shipping a copy of yasm to build MPIR since the one in the system is usually too buggy to work
* we are shipping Brian Gladman's VS 2008 build files

The spkg has been tested on

* FC 9 x86
* FC 9, OpenSUSE 10.3 x86-64
* RHEL 5.2, SLES 10 Itanium
* Solaris 10 Sparc and x86
* OSX 10.4 ppc
* OSX 10.5 x86 *and* x86-64
* YDL 6.1 PS3 (a G5 variant)

Cheers,

Michael



---

archive/issue_comments_037722.json:
```json
{
    "body": "REVIEW:\n\n(1) All doctests pass with the applied patches.\n\n(2) \nJust for fun I checked to see how bad the xgcd speed regression is:\n\n```\nBEFORE (with GMP):\nsage: n = ZZ.random_element(0,2^(2^20)); m = ZZ.random_element(0,2^(2^20))\nsage: time k = m.xgcd(n)\nCPU times: user 0.73 s, sys: 0.00 s, total: 0.73 s\nWall time: 0.74 s\n\n\nAFTER (with eMPIRe):\nsage: n = ZZ.random_element(0,2^(2^20)); m = ZZ.random_element(0,2^(2^20))\nsage: time k = m.xgcd(n)\nCPU times: user 2.39 s, sys: 0.00 s, total: 2.39 s\nWall time: 2.39 s\n```\n\n\nI did some multiplication timings (by multiplying m, n as above and bigger) and empire is always about 3-5% FASTER.\n\npreliminary *positive review*.\n\nI will look this over again a little more carefully, but so far it looks very very good.",
    "created_at": "2009-01-18T20:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37722",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

(1) All doctests pass with the applied patches.

(2) 
Just for fun I checked to see how bad the xgcd speed regression is:

```
BEFORE (with GMP):
sage: n = ZZ.random_element(0,2^(2^20)); m = ZZ.random_element(0,2^(2^20))
sage: time k = m.xgcd(n)
CPU times: user 0.73 s, sys: 0.00 s, total: 0.73 s
Wall time: 0.74 s


AFTER (with eMPIRe):
sage: n = ZZ.random_element(0,2^(2^20)); m = ZZ.random_element(0,2^(2^20))
sage: time k = m.xgcd(n)
CPU times: user 2.39 s, sys: 0.00 s, total: 2.39 s
Wall time: 2.39 s
```


I did some multiplication timings (by multiplying m, n as above and bigger) and empire is always about 3-5% FASTER.

preliminary *positive review*.

I will look this over again a little more carefully, but so far it looks very very good.



---

archive/issue_comments_037723.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T02:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37723",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037724.json:
```json
{
    "body": "Merged two patches and the spkg in Sage 3.3.alpha0\n\nMike: Note that there are doctest changes in the doc repo, too.",
    "created_at": "2009-01-19T02:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37724",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged two patches and the spkg in Sage 3.3.alpha0

Mike: Note that there are doctest changes in the doc repo, too.



---

archive/issue_comments_037725.json:
```json
{
    "body": "I found one buglet that slipped by, i.e. we need to unset PYTHON since Yasm gets confused by it. I also did not check in the changes to spkg-install, so I did so.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T02:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4966#issuecomment-37725",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I found one buglet that slipped by, i.e. we need to unset PYTHON since Yasm gets confused by it. I also did not check in the changes to spkg-install, so I did so.

Cheers,

Michael
