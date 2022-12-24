# Issue 915: Make LinBox used PID_Integer instead of using old header as workaround

archive/issues_000915.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: LinBox gmp\n\nTo quote William from linbox-use:\n\n```\nI would also like to know the answer to this.  In SAGE were currently do this\nconversion by not using PID_Integer, and instead using an old header file\nfrom an old version of Linbox that defined a GMP Integer wrapper type.\nFast conversion to/from mpz_t is critical for what we're doing.\n```\n\nDave Saunders came up with the following suggestion:\n\n```\nPID_integer ZZ;\nSparseMatrix<PID_integer> A (ZZ,m,m);  //defines empty sparse matrix\n\nmpz_t x;\nmpz_init_set_ui(x, 5);\n\n\n// Assign x into A, avoiding conversions and double copy.\nmpz_set ( SpyInteger::get_mpz(A.refEntry(1,2)), x);\n\nZZ.write(std::cout, A.getEntry(1,2)) << std::endl;\n\n-dave\n\nPS.  A more direct function could be desirable.\n```\n\nThis ticket is related to #824. For details see http://groups.google.com/group/linbox-use/t/7a687e8e5a5f4a81\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/915\n\n",
    "created_at": "2007-10-18T03:04:35Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Make LinBox used PID_Integer instead of using old header as workaround",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/915",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Keywords: LinBox gmp

To quote William from linbox-use:

```
I would also like to know the answer to this.  In SAGE were currently do this
conversion by not using PID_Integer, and instead using an old header file
from an old version of Linbox that defined a GMP Integer wrapper type.
Fast conversion to/from mpz_t is critical for what we're doing.
```

Dave Saunders came up with the following suggestion:

```
PID_integer ZZ;
SparseMatrix<PID_integer> A (ZZ,m,m);  //defines empty sparse matrix

mpz_t x;
mpz_init_set_ui(x, 5);


// Assign x into A, avoiding conversions and double copy.
mpz_set ( SpyInteger::get_mpz(A.refEntry(1,2)), x);

ZZ.write(std::cout, A.getEntry(1,2)) << std::endl;

-dave

PS.  A more direct function could be desirable.
```

This ticket is related to #824. For details see http://groups.google.com/group/linbox-use/t/7a687e8e5a5f4a81

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/915





---

archive/issue_comments_005617.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-18T03:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/915#issuecomment-5617",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005618.json:
```json
{
    "body": "Attachment [trac915.patch](tarball://root/attachments/some-uuid/ticket915/trac915.patch) by cpernet created at 2008-02-17 02:39:43\n\nRemove the usage of GMP-Integer implementation of Z",
    "created_at": "2008-02-17T02:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/915#issuecomment-5618",
    "user": "cpernet"
}
```

Attachment [trac915.patch](tarball://root/attachments/some-uuid/ticket915/trac915.patch) by cpernet created at 2008-02-17 02:39:43

Remove the usage of GMP-Integer implementation of Z



---

archive/issue_comments_005619.json:
```json
{
    "body": "Attachment [trac915.2.patch](tarball://root/attachments/some-uuid/ticket915/trac915.2.patch) by cpernet created at 2008-02-17 02:49:05\n\nRemove the work-around with gmp-integers",
    "created_at": "2008-02-17T02:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/915#issuecomment-5619",
    "user": "cpernet"
}
```

Attachment [trac915.2.patch](tarball://root/attachments/some-uuid/ticket915/trac915.2.patch) by cpernet created at 2008-02-17 02:49:05

Remove the work-around with gmp-integers



---

archive/issue_comments_005620.json:
```json
{
    "body": "Patch looks good to me :)",
    "created_at": "2008-03-03T04:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/915#issuecomment-5620",
    "user": "mabshoff"
}
```

Patch looks good to me :)



---

archive/issue_comments_005621.json:
```json
{
    "body": "Merged Clement's patch in\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc1/linbox-1.1.5rc2.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T04:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/915#issuecomment-5621",
    "user": "mabshoff"
}
```

Merged Clement's patch in

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc1/linbox-1.1.5rc2.p0.spkg

Cheers,

Michael



---

archive/issue_comments_005622.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T04:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/915#issuecomment-5622",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc1



---

archive/issue_comments_005623.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T04:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/915#issuecomment-5623",
    "user": "mabshoff"
}
```

Resolution: fixed
