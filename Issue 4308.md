# Issue 4308: mpc spackage

archive/issues_004308.json:
```json
{
    "body": "Assignee: mabshoff\n\nI am planning to add arbitrary precision complex numbers using the MPC library\nhttp://www.multiprecision.org/mpc/.\n\nHere is a sage package based\nhttp://www.loria.fr/~thevenyp/mpc-0.5.spkg\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4308\n\n",
    "created_at": "2008-10-16T15:27:23Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "mpc spackage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4308",
    "user": "thevenyp"
}
```
Assignee: mabshoff

I am planning to add arbitrary precision complex numbers using the MPC library
http://www.multiprecision.org/mpc/.

Here is a sage package based
http://www.loria.fr/~thevenyp/mpc-0.5.spkg


Issue created by migration from https://trac.sagemath.org/ticket/4308





---

archive/issue_comments_031532.json:
```json
{
    "body": "I will review the spkg later on today.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T12:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31532",
    "user": "mabshoff"
}
```

I will review the spkg later on today.

Cheers,

Michael



---

archive/issue_comments_031533.json:
```json
{
    "body": "Do we have any sage interface code to go with this yet? I know some was produced at Sage days 10. \n\nThen these extensions should be added based in whether or not this package is installed `sage.misc.package.is_package_installed()`.",
    "created_at": "2008-10-30T21:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31533",
    "user": "@robertwb"
}
```

Do we have any sage interface code to go with this yet? I know some was produced at Sage days 10. 

Then these extensions should be added based in whether or not this package is installed `sage.misc.package.is_package_installed()`.



---

archive/issue_comments_031534.json:
```json
{
    "body": "Bindings are being written. The spkg should become optional so it is easily buildable from any Sage install. Once/If mpc is standard the mpc.spkg would also become standard.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T23:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31534",
    "user": "mabshoff"
}
```

Bindings are being written. The spkg should become optional so it is easily buildable from any Sage install. Once/If mpc is standard the mpc.spkg would also become standard.

Cheers,

Michael



---

archive/issue_comments_031535.json:
```json
{
    "body": "See #4446 for a patch implementing a partial interface (still work in progress).",
    "created_at": "2008-11-22T07:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31535",
    "user": "@aghitza"
}
```

See #4446 for a patch implementing a partial interface (still work in progress).



---

archive/issue_comments_031536.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. There is no .hg repository in the spkg.  You need to\n\n```\n$cd mpc-0.5\n$ hg init\n$ hg add spkg-install spkg-check SPKG.txt\n```\n\n\n2. The SPKG.txt doesn't list anybody or any contact info under \"package maintainer\". \n\n3. The SPKG.txt has an empty changelog.  This should at least list exactly which version of upstream is in the src subdirectory.   Typically when refereeing a patch, I like to verify that src/ contains the claimed upstream exactly, since I don't want some virus crap sneaking in.\n\n4. Speaking of crap, the src/src/ subdirectory is full of .o pre-compiled binary object files.  These need to all be deleted.\n\n```\nteragon-2:src wstein$ pwd\n/Users/wstein/tmp/mpc-0.5/src/src\nteragon-2:src wstein$ ls -1 *.o |wc -l\n      57\n```\n",
    "created_at": "2008-11-27T17:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31536",
    "user": "@williamstein"
}
```

REFEREE REPORT:

1. There is no .hg repository in the spkg.  You need to

```
$cd mpc-0.5
$ hg init
$ hg add spkg-install spkg-check SPKG.txt
```


2. The SPKG.txt doesn't list anybody or any contact info under "package maintainer". 

3. The SPKG.txt has an empty changelog.  This should at least list exactly which version of upstream is in the src subdirectory.   Typically when refereeing a patch, I like to verify that src/ contains the claimed upstream exactly, since I don't want some virus crap sneaking in.

4. Speaking of crap, the src/src/ subdirectory is full of .o pre-compiled binary object files.  These need to all be deleted.

```
teragon-2:src wstein$ pwd
/Users/wstein/tmp/mpc-0.5/src/src
teragon-2:src wstein$ ls -1 *.o |wc -l
      57
```




---

archive/issue_comments_031537.json:
```json
{
    "body": "Thanks for your review, the spkg has been changed accordingly.\n\nRegards,\n\nPhilippe",
    "created_at": "2008-11-28T17:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31537",
    "user": "thevenyp"
}
```

Thanks for your review, the spkg has been changed accordingly.

Regards,

Philippe



---

archive/issue_comments_031538.json:
```json
{
    "body": "Hi Philippe,\n\nI have reviewed your updated spkg. A couple comments:\n\n* Everything looks good, but some minor details I fixed\n* Checked in the changes you added to the repo in your name\n* added a .hgignore and added some small cleanups to spkg-install\n\nI also deleted the attached spkg since large files should not be attached to trac, but linked from some webspace. \n\nThe updated spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/mpc-0.5.p0.spkg\n\nIn case you improve/update the mpc.spkg please use that one as a base.\n\nSummary: positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T05:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31538",
    "user": "mabshoff"
}
```

Hi Philippe,

I have reviewed your updated spkg. A couple comments:

* Everything looks good, but some minor details I fixed
* Checked in the changes you added to the repo in your name
* added a .hgignore and added some small cleanups to spkg-install

I also deleted the attached spkg since large files should not be attached to trac, but linked from some webspace. 

The updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/mpc-0.5.p0.spkg

In case you improve/update the mpc.spkg please use that one as a base.

Summary: positive review.

Cheers,

Michael



---

archive/issue_comments_031539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T05:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31539",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031540.json:
```json
{
    "body": "Uploaded to the optional spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T05:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4308#issuecomment-31540",
    "user": "mabshoff"
}
```

Uploaded to the optional spkg repo.

Cheers,

Michael
