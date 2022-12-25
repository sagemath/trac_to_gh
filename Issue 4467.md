# Issue 4467: clean up or delete the (unused?) hanke extension

archive/issues_004467.json:
```json
{
    "body": "Assignee: mabshoff\n\nsetup.py contains\n\n```\nhanke = Extension(name = \"sage.libs.hanke.hanke\",\n              sources = [\"sage/libs/hanke/hanke.pyx\",\n                         \"sage/libs/hanke/wrap.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/Matrix_mpz.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/CountLocal2.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/CountLocal.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/Local_Constants.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/Local_Density_Front.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/Local_Density_Congruence.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/Local_Normal.cc\",\n                         \"sage/libs/hanke/Matrix_mpz/Local_Invariants.cc\",\n                         \"sage/libs/hanke/Utilities/string_utils.cc\",\n                         \"sage/libs/hanke/GMP_class_extras/mpz_class_extras.cc\",\n                         \"sage/libs/hanke/GMP_class_extras/vectors.cc\" ],\n                   libraries = [\"gmp\", \"gmpxx\", \"stdc++\"])\n```\n\nIt looks like dead code to me, so it should be deleted IMHO. In case John wants to use it for something he should be given the chance to rescue it.\n\nCheers,\n\nMcihael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4467\n\n",
    "created_at": "2008-11-08T05:51:58Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "clean up or delete the (unused?) hanke extension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

setup.py contains

```
hanke = Extension(name = "sage.libs.hanke.hanke",
              sources = ["sage/libs/hanke/hanke.pyx",
                         "sage/libs/hanke/wrap.cc",
                         "sage/libs/hanke/Matrix_mpz/Matrix_mpz.cc",
                         "sage/libs/hanke/Matrix_mpz/CountLocal2.cc",
                         "sage/libs/hanke/Matrix_mpz/CountLocal.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Constants.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Density_Front.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Density_Congruence.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Normal.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Invariants.cc",
                         "sage/libs/hanke/Utilities/string_utils.cc",
                         "sage/libs/hanke/GMP_class_extras/mpz_class_extras.cc",
                         "sage/libs/hanke/GMP_class_extras/vectors.cc" ],
                   libraries = ["gmp", "gmpxx", "stdc++"])
```

It looks like dead code to me, so it should be deleted IMHO. In case John wants to use it for something he should be given the chance to rescue it.

Cheers,

Mcihael

Issue created by migration from https://trac.sagemath.org/ticket/4467





---

archive/issue_comments_032916.json:
```json
{
    "body": "I talked to John Hanke and he told me that the code can be deleted since it is no longer used.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-08T20:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4467#issuecomment-32916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I talked to John Hanke and he told me that the code can be deleted since it is no longer used.

Cheers,

Michael



---

archive/issue_comments_032917.json:
```json
{
    "body": "Craig will remove the actual setup.py extension in a separate cleanup patch of setup.py\n\nCheers,\n\nMichael",
    "created_at": "2008-11-10T05:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4467#issuecomment-32917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig will remove the actual setup.py extension in a separate cleanup patch of setup.py

Cheers,

Michael



---

archive/issue_events_010094.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-10T05:19:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4467",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4467#event-10094"
}
```



---

archive/issue_comments_032918.json:
```json
{
    "body": "Attachment [trac_4467.patch](tarball://root/attachments/some-uuid/ticket4467/trac_4467.patch) by @jonhanke created at 2008-11-10 06:20:23\n\n+1 since the code removes dead code only.",
    "created_at": "2008-11-10T06:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4467#issuecomment-32918",
    "user": "https://github.com/jonhanke"
}
```

Attachment [trac_4467.patch](tarball://root/attachments/some-uuid/ticket4467/trac_4467.patch) by @jonhanke created at 2008-11-10 06:20:23

+1 since the code removes dead code only.



---

archive/issue_comments_032919.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-10T09:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4467#issuecomment-32919",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032920.json:
```json
{
    "body": "Merged in Sage 3.2.rc0",
    "created_at": "2008-11-10T09:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4467#issuecomment-32920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc0



---

archive/issue_events_010095.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-10T09:06:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4467",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4467#event-10095"
}
```
