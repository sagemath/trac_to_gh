# Issue 6760: error in quaternion algebra ideal basis

archive/issues_006760.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage: R.<i,j,k> = QuaternionAlgebra(-1, -13)        \nsage: I = R.ideal([2+i, 3*i, 5*j, j+k]); I\nFractional ideal (2 + i, 3*i, j + k, 5*k)\nsage: I.free_module()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/sage-4.0/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py\", line 1503, in free_module\n    M = self.hermite_basis_matrix().row_module(ZZ)\nAttributeError: 'QuaternionFractionalIdeal_rational' object has no attribute 'hermite_basis_matrix'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6760\n\n",
    "created_at": "2009-08-16T08:49:58Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "error in quaternion algebra ideal basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6760",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd


```
sage: R.<i,j,k> = QuaternionAlgebra(-1, -13)        
sage: I = R.ideal([2+i, 3*i, 5*j, j+k]); I
Fractional ideal (2 + i, 3*i, j + k, 5*k)
sage: I.free_module()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/sage-4.0/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py", line 1503, in free_module
    M = self.hermite_basis_matrix().row_module(ZZ)
AttributeError: 'QuaternionFractionalIdeal_rational' object has no attribute 'hermite_basis_matrix'
```


Issue created by migration from https://trac.sagemath.org/ticket/6760





---

archive/issue_comments_055560.json:
```json
{
    "body": "Attachment [6760-quatalg-free-module.patch](tarball://root/attachments/some-uuid/ticket6760/6760-quatalg-free-module.patch) by @robertwb created at 2009-08-16 08:53:48\n\nI think this is the right fix, but someone more familiar with the code should take a look.",
    "created_at": "2009-08-16T08:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6760#issuecomment-55560",
    "user": "https://github.com/robertwb"
}
```

Attachment [6760-quatalg-free-module.patch](tarball://root/attachments/some-uuid/ticket6760/6760-quatalg-free-module.patch) by @robertwb created at 2009-08-16 08:53:48

I think this is the right fix, but someone more familiar with the code should take a look.



---

archive/issue_comments_055561.json:
```json
{
    "body": "Looks good to me.  I am adding a patch with a doctest (just the example that was given above).\n\nRobert, if you're happy with the second patch, please change this to a positive review.",
    "created_at": "2009-11-15T10:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6760#issuecomment-55561",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.  I am adding a patch with a doctest (just the example that was given above).

Robert, if you're happy with the second patch, please change this to a positive review.



---

archive/issue_comments_055562.json:
```json
{
    "body": "Attachment [trac_6760_doctest.patch](tarball://root/attachments/some-uuid/ticket6760/trac_6760_doctest.patch) by @aghitza created at 2009-11-15 10:20:17\n\napply after the previous patch",
    "created_at": "2009-11-15T10:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6760#issuecomment-55562",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6760_doctest.patch](tarball://root/attachments/some-uuid/ticket6760/trac_6760_doctest.patch) by @aghitza created at 2009-11-15 10:20:17

apply after the previous patch



---

archive/issue_comments_055563.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-16T18:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6760#issuecomment-55563",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T06:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6760#issuecomment-55564",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
