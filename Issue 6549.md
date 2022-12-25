# Issue 6549: reinstate some doctests in schemes/plane_curves/affine_curve.py

archive/issues_006549.json:
```json
{
    "body": "Assignee: tbd\n\nSome doctests in `schemes/plane_curves/affine_curve.py` are marked \"not tested\" with the comment that they crash on OS X intel.  This appears to not be the case any more:\n\n```\naghitza@192-168-1-2:~/opt/sage-4.1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: x, y = (GF(17)['x,y']).gens()\nsage: C = Curve(x^2+y^5+x*y-19)\nsage: v = C.rational_points(algorithm='bn')\nsage: w = C.rational_points(algorithm='enum')\nsage: len(v)\n20\nsage: v == w\nTrue\nsage: \nExiting SAGE (CPU time 0m0.23s, Wall time 1m59.83s).\nExiting spawned Singular process.\naghitza@192-168-1-2:~/opt/sage-4.1$ uname -a\nDarwin 192-168-1-2.tpgi.com.au 9.7.0 Darwin Kernel Version 9.7.0: Tue Mar 31 22:52:17 PDT 2009; root:xnu-1228.12.14~1/RELEASE_I386 i386\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6549\n\n",
    "created_at": "2009-07-17T14:12:32Z",
    "labels": [
        "component: doctest coverage",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "reinstate some doctests in schemes/plane_curves/affine_curve.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6549",
    "user": "https://github.com/aghitza"
}
```
Assignee: tbd

Some doctests in `schemes/plane_curves/affine_curve.py` are marked "not tested" with the comment that they crash on OS X intel.  This appears to not be the case any more:

```
aghitza@192-168-1-2:~/opt/sage-4.1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x, y = (GF(17)['x,y']).gens()
sage: C = Curve(x^2+y^5+x*y-19)
sage: v = C.rational_points(algorithm='bn')
sage: w = C.rational_points(algorithm='enum')
sage: len(v)
20
sage: v == w
True
sage: 
Exiting SAGE (CPU time 0m0.23s, Wall time 1m59.83s).
Exiting spawned Singular process.
aghitza@192-168-1-2:~/opt/sage-4.1$ uname -a
Darwin 192-168-1-2.tpgi.com.au 9.7.0 Darwin Kernel Version 9.7.0: Tue Mar 31 22:52:17 PDT 2009; root:xnu-1228.12.14~1/RELEASE_I386 i386
```

Issue created by migration from https://trac.sagemath.org/ticket/6549





---

archive/issue_comments_053298.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-17T14:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6549#issuecomment-53298",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053299.json:
```json
{
    "body": "Changing assignee from tbd to @aghitza.",
    "created_at": "2009-07-17T14:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6549#issuecomment-53299",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @aghitza.



---

archive/issue_comments_053300.json:
```json
{
    "body": "Looks good. Works fine on my MacBook Pro, and also seems to work fine on sage.math. My one potential complaint: I think there's a missing level of nesting in the docstring. That is, I think the three bullets after \"algorithm\" should be in a sub-list. (I recognize that this patch doesn't touch the docstring other than the doctests, but I still think they should be fixed since we're here.)",
    "created_at": "2009-08-17T06:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6549#issuecomment-53300",
    "user": "https://github.com/craigcitro"
}
```

Looks good. Works fine on my MacBook Pro, and also seems to work fine on sage.math. My one potential complaint: I think there's a missing level of nesting in the docstring. That is, I think the three bullets after "algorithm" should be in a sub-list. (I recognize that this patch doesn't touch the docstring other than the doctests, but I still think they should be fixed since we're here.)



---

archive/issue_comments_053301.json:
```json
{
    "body": "Attachment [trac_6549.patch](tarball://root/attachments/some-uuid/ticket6549/trac_6549.patch) by @aghitza created at 2009-08-17 12:04:27",
    "created_at": "2009-08-17T12:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6549#issuecomment-53301",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6549.patch](tarball://root/attachments/some-uuid/ticket6549/trac_6549.patch) by @aghitza created at 2009-08-17 12:04:27



---

archive/issue_comments_053302.json:
```json
{
    "body": "Docstring fixed, new patch replaces the old.",
    "created_at": "2009-08-17T12:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6549#issuecomment-53302",
    "user": "https://github.com/aghitza"
}
```

Docstring fixed, new patch replaces the old.



---

archive/issue_comments_053303.json:
```json
{
    "body": "Nice.",
    "created_at": "2009-08-17T18:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6549#issuecomment-53303",
    "user": "https://github.com/craigcitro"
}
```

Nice.



---

archive/issue_events_015447.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-25T04:12:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6549#event-15447"
}
```



---

archive/issue_comments_053304.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T04:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6549#issuecomment-53304",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
