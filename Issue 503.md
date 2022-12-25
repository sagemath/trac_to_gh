# Issue 503: 0^0 -- error or 1; and other exponentiation optimizations

archive/issues_000503.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/503\n\n",
    "created_at": "2007-08-28T21:41:00Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "0^0 -- error or 1; and other exponentiation optimizations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/503",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/503





---

archive/issue_comments_002505.json:
```json
{
    "body": "NOTE:  For polynomials x<sup>0</sup> should be 1 still.",
    "created_at": "2007-08-29T02:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2505",
    "user": "https://github.com/williamstein"
}
```

NOTE:  For polynomials x<sup>0</sup> should be 1 still.



---

archive/issue_comments_002506.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-29T23:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2506",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002507.json:
```json
{
    "body": "*mostly* fixed by the patch:\n\n[http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg)\n\nthe following files might still contain problems:\n\n```\nrings/integer.pyx\nrings/rational.pyx\n\ngroups/abelian_gps/abelian_group_element.py\ngroups/abelian_gps/dual_abelian_group_element.py\n\nrings/power_series_mpoly.pyx\nrings/power_series_poly.pyx\n\nschemes/generic/morphism.py\n\ncategories/morphism.pyx\ncategories/morphism.pyx\n\nrings/padics/padic_extension_generic_element.py\nrings/padics/padic_lazy_element.py\nrings/padics/valuation.py\nrings/padics/local_generic_element.pyx\nrings/padics/padic_capped_absolute_element.pyx\nrings/padics/padic_capped_relative_element.pyx\nrings/padics/padic_fixed_mod_element.pyx\n```\n",
    "created_at": "2007-08-29T23:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2507",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

*mostly* fixed by the patch:

[http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg)

the following files might still contain problems:

```
rings/integer.pyx
rings/rational.pyx

groups/abelian_gps/abelian_group_element.py
groups/abelian_gps/dual_abelian_group_element.py

rings/power_series_mpoly.pyx
rings/power_series_poly.pyx

schemes/generic/morphism.py

categories/morphism.pyx
categories/morphism.pyx

rings/padics/padic_extension_generic_element.py
rings/padics/padic_lazy_element.py
rings/padics/valuation.py
rings/padics/local_generic_element.pyx
rings/padics/padic_capped_absolute_element.pyx
rings/padics/padic_capped_relative_element.pyx
rings/padics/padic_fixed_mod_element.pyx
```




---

archive/issue_comments_002508.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2007-09-07T01:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2508",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from assigned to new.



---

archive/issue_comments_002509.json:
```json
{
    "body": "final patch (from me):\n\n[http://sage.math.washington.edu/home/boothby/my_patches/arith503.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith503.hg)\n\nnote:  the following files have no doctests, and are difficult to use -- hence have not been updated.  Once #610 is resolved, the pow methods there should be updated and this can be resolved.\n\n\n```\nrings/padics/padic_extension_generic_element.py\nrings/padics/padic_lazy_element.py\nrings/padics/valuation.py\nrings/padics/local_generic_element.pyx\nrings/padics/padic_capped_absolute_element.pyx\nrings/padics/padic_capped_relative_element.pyx\nrings/padics/padic_fixed_mod_element.pyx\n```\n",
    "created_at": "2007-09-07T01:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2509",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

final patch (from me):

[http://sage.math.washington.edu/home/boothby/my_patches/arith503.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith503.hg)

note:  the following files have no doctests, and are difficult to use -- hence have not been updated.  Once #610 is resolved, the pow methods there should be updated and this can be resolved.


```
rings/padics/padic_extension_generic_element.py
rings/padics/padic_lazy_element.py
rings/padics/valuation.py
rings/padics/local_generic_element.pyx
rings/padics/padic_capped_absolute_element.pyx
rings/padics/padic_capped_relative_element.pyx
rings/padics/padic_fixed_mod_element.pyx
```




---

archive/issue_comments_002510.json:
```json
{
    "body": "Changing assignee from boothby to @roed314.",
    "created_at": "2007-09-07T01:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2510",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from boothby to @roed314.



---

archive/issue_comments_002511.json:
```json
{
    "body": "Changing assignee from @roed314 to @robertwb.",
    "created_at": "2007-09-07T01:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2511",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from @roed314 to @robertwb.



---

archive/issue_comments_002512.json:
```json
{
    "body": "Attachment [power503.hg](tarball://root/attachments/some-uuid/ticket503/power503.hg) by @robertwb created at 2007-09-07 03:18:27\n\nFixed remaining instances of __pow__",
    "created_at": "2007-09-07T03:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2512",
    "user": "https://github.com/robertwb"
}
```

Attachment [power503.hg](tarball://root/attachments/some-uuid/ticket503/power503.hg) by @robertwb created at 2007-09-07 03:18:27

Fixed remaining instances of __pow__



---

archive/issue_comments_002513.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-07T03:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2513",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/503#issuecomment-2514",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000538.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T04:08:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/503",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/503#event-538"
}
```
