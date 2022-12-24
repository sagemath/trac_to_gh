# Issue 2101: debianize various spkgs

archive/issues_002101.json:
```json
{
    "body": "Assignee: tabbott\n\nWe started with NTL:\n\nhttp://sage.math.washington.edu/home/mabshoff/SPKG-Debian/ntl-5.4.1.p11.spkg\n\nMore to come.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2101\n\n",
    "created_at": "2008-02-08T05:54:41Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "debianize various spkgs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2101",
    "user": "mabshoff"
}
```
Assignee: tabbott

We started with NTL:

http://sage.math.washington.edu/home/mabshoff/SPKG-Debian/ntl-5.4.1.p11.spkg

More to come.

Issue created by migration from https://trac.sagemath.org/ticket/2101





---

archive/issue_comments_013690.json:
```json
{
    "body": "More spkgs for merging:\nhttp://sage.math.washington.edu/home/tabbott/cddlib-094b.p1.spkg\nhttp://sage.math.washington.edu/home/tabbott/eclib-20080127.p0.spkg\nhttp://sage.math.washington.edu/home/tabbott/flintqs-20070817.p2.spkg\nhttp://sage.math.washington.edu/home/tabbott/givaro-3.2.6.p6.spkg\nhttp://sage.math.washington.edu/home/tabbott/iml-1.0.1.p9.spkg\nhttp://sage.math.washington.edu/home/tabbott/lcalc-20070107.p1.spkg\nhttp://sage.math.washington.edu/home/tabbott/libm4ri-20071224.p1.spkg\nhttp://sage.math.washington.edu/home/tabbott/palp-1.1.p1.spkg\nhttp://sage.math.washington.edu/home/tabbott/symmetrica-2.0.p1.spkg\nhttp://sage.math.washington.edu/home/tabbott/sympow-1.018.1.p4.spkg",
    "created_at": "2008-02-08T09:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2101#issuecomment-13690",
    "user": "tabbott"
}
```

More spkgs for merging:
http://sage.math.washington.edu/home/tabbott/cddlib-094b.p1.spkg
http://sage.math.washington.edu/home/tabbott/eclib-20080127.p0.spkg
http://sage.math.washington.edu/home/tabbott/flintqs-20070817.p2.spkg
http://sage.math.washington.edu/home/tabbott/givaro-3.2.6.p6.spkg
http://sage.math.washington.edu/home/tabbott/iml-1.0.1.p9.spkg
http://sage.math.washington.edu/home/tabbott/lcalc-20070107.p1.spkg
http://sage.math.washington.edu/home/tabbott/libm4ri-20071224.p1.spkg
http://sage.math.washington.edu/home/tabbott/palp-1.1.p1.spkg
http://sage.math.washington.edu/home/tabbott/symmetrica-2.0.p1.spkg
http://sage.math.washington.edu/home/tabbott/sympow-1.018.1.p4.spkg



---

archive/issue_comments_013691.json:
```json
{
    "body": "More spkgs few merging:\nhttp://sage.math.washington.edu/home/tabbott/flint-1.06.p1.spkg\nhttp://sage.math.washington.edu/home/tabbott/singular-3-0-4-1-20071209.p4.spkg\nhttp://sage.math.washington.edu/home/tabbott/libfplll-2.1.6-20071129.p1.spkg\nhttp://sage.math.washington.edu/home/tabbott/linbox-20070915.p4.spkg\nhttp://sage.math.washington.edu/home/tabbott/genus2reduction-0.3.p1.spkg",
    "created_at": "2008-02-09T04:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2101#issuecomment-13691",
    "user": "tabbott"
}
```

More spkgs few merging:
http://sage.math.washington.edu/home/tabbott/flint-1.06.p1.spkg
http://sage.math.washington.edu/home/tabbott/singular-3-0-4-1-20071209.p4.spkg
http://sage.math.washington.edu/home/tabbott/libfplll-2.1.6-20071129.p1.spkg
http://sage.math.washington.edu/home/tabbott/linbox-20070915.p4.spkg
http://sage.math.washington.edu/home/tabbott/genus2reduction-0.3.p1.spkg



---

archive/issue_comments_013692.json:
```json
{
    "body": "Quaddouble in Debian is too old and not in Lenny at all. I filed a bug.  Here's an updated spkg for quaddouble with sloppy Debian build support for now (I grabbed the debian/ directory from Debian but didn't fix the fact that shared libraries and .la files weren't being built.).  It needs testing on other distros.\n\nhttp://sage.math.washington.edu/home/tabbott/quaddouble-2.3.4.p1.spkg",
    "created_at": "2008-02-10T01:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2101#issuecomment-13692",
    "user": "tabbott"
}
```

Quaddouble in Debian is too old and not in Lenny at all. I filed a bug.  Here's an updated spkg for quaddouble with sloppy Debian build support for now (I grabbed the debian/ directory from Debian but didn't fix the fact that shared libraries and .la files weren't being built.).  It needs testing on other distros.

http://sage.math.washington.edu/home/tabbott/quaddouble-2.3.4.p1.spkg



---

archive/issue_comments_013693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-14T23:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2101#issuecomment-13693",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013694.json:
```json
{
    "body": "Merged all new spkgs but quaddouble-2.3.4.p1.spkg in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T23:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2101#issuecomment-13694",
    "user": "mabshoff"
}
```

Merged all new spkgs but quaddouble-2.3.4.p1.spkg in Sage 2.10.2.alpha0
