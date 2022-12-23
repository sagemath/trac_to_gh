# Issue 5788: Fix MPIR build problem on OSX 10.4 exposed by linbox

archive/issues_005788.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn OSX 10.4 a problem in libgmpxx.la leads to linbox linking gmpxx, mpir **and** gmp at the same time resulting in duplicate symbol errors. The latest upstream release (MPIR 1.0) fixes that.\n\nSpkg coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5788\n\n",
    "created_at": "2009-04-15T00:52:01Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "Fix MPIR build problem on OSX 10.4 exposed by linbox",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5788",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On OSX 10.4 a problem in libgmpxx.la leads to linbox linking gmpxx, mpir **and** gmp at the same time resulting in duplicate symbol errors. The latest upstream release (MPIR 1.0) fixes that.

Spkg coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5788





---

archive/issue_comments_045306.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-18T07:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5788#issuecomment-45306",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045307.json:
```json
{
    "body": "The spkg at \n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/gmp-mpir-1.1.spkg\n\nfixes this problem, a couple other test failures reported in IRC and face-to-face and updates to the latest upstream release.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T07:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5788#issuecomment-45307",
    "user": "mabshoff"
}
```

The spkg at 

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/gmp-mpir-1.1.spkg

fixes this problem, a couple other test failures reported in IRC and face-to-face and updates to the latest upstream release.

Cheers,

Michael



---

archive/issue_comments_045308.json:
```json
{
    "body": "Extracting the Sage 3.4.rc3 tarball, replacing the gmp-mpir spkg with this \"rc4\" one (and as only other change replacing the atlas spkg also with the \"rc4\" version from #5219), Sage builds fine (!) and for \"make test\" all tests pass.\n\nTested on my MacIntel OS X 10.4.11 / Xcode 2.5 box / \"daily work\" installation (but TeX being in the path should be of no concern here).\n\nCheers, gsw",
    "created_at": "2009-04-18T13:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5788#issuecomment-45308",
    "user": "GeorgSWeber"
}
```

Extracting the Sage 3.4.rc3 tarball, replacing the gmp-mpir spkg with this "rc4" one (and as only other change replacing the atlas spkg also with the "rc4" version from #5219), Sage builds fine (!) and for "make test" all tests pass.

Tested on my MacIntel OS X 10.4.11 / Xcode 2.5 box / "daily work" installation (but TeX being in the path should be of no concern here).

Cheers, gsw



---

archive/issue_comments_045309.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc4.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T23:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5788#issuecomment-45309",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc4.

Cheers,

Michael



---

archive/issue_comments_045310.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T23:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5788#issuecomment-45310",
    "user": "mabshoff"
}
```

Resolution: fixed
