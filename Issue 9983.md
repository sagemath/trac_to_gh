# Issue 9983: ECM fails to build on AIX 5.3 - A warning about linking a static library against a shared library

archive/issues_009983.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @fchapoton\n\nUsing the following system: \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* DDS-4 tape drive \n\nECL fails to build properly. See the attached log. A rather obvious part of the failure message is:\n\n\n\n```\n*** Warning: Linking the shared library libecm.la against the\n*** static library /home/users/drkirkby/sage-4.6.alpha1/local/lib/libgmp.a is not portable!\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9984\n\n",
    "created_at": "2010-09-23T20:34:12Z",
    "labels": [
        "porting: AIX or HP-UX",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ECM fails to build on AIX 5.3 - A warning about linking a static library against a shared library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9983",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  @fchapoton

Using the following system: 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* DDS-4 tape drive 

ECL fails to build properly. See the attached log. A rather obvious part of the failure message is:



```
*** Warning: Linking the shared library libecm.la against the
*** static library /home/users/drkirkby/sage-4.6.alpha1/local/lib/libgmp.a is not portable!
```



Issue created by migration from https://trac.sagemath.org/ticket/9984





---

archive/issue_comments_100321.json:
```json
{
    "body": "Build failure observed on an RS/6000 running AIX 5.3",
    "created_at": "2010-09-23T20:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9983#issuecomment-100321",
    "user": "drkirkby"
}
```

Build failure observed on an RS/6000 running AIX 5.3



---

archive/issue_comments_100322.json:
```json
{
    "body": "Attachment [ecm-6.2.1.p2.log](tarball://root/attachments/some-uuid/ticket9984/ecm-6.2.1.p2.log) by @jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9983#issuecomment-100322",
    "user": "@jdemeyer"
}
```

Attachment [ecm-6.2.1.p2.log](tarball://root/attachments/some-uuid/ticket9984/ecm-6.2.1.p2.log) by @jdemeyer created at 2013-08-13 15:35:53



---

archive/issue_comments_100323.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9983#issuecomment-100323",
    "user": "@embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100324.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9983#issuecomment-100324",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100325.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9983#issuecomment-100325",
    "user": "@mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_100326.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9983#issuecomment-100326",
    "user": "@fchapoton"
}
```

Resolution: invalid
