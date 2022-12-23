# Issue 6037: Major Upgrade to QuadraticForm Local Density Routines

archive/issues_006037.json:
```json
{
    "body": "Assignee: justin\n\nCC:  mabshoff wstein tornaria\n\nCompletely rewritten and doctested Local densities routines according to a consistent interface (and algorithms) described in the attached PDF file.\n\nPatch to follow very shortly!\n\nIssue created by migration from https://trac.sagemath.org/ticket/6037\n\n",
    "created_at": "2009-05-14T10:03:59Z",
    "labels": [
        "quadratic forms",
        "major",
        "enhancement"
    ],
    "title": "Major Upgrade to QuadraticForm Local Density Routines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6037",
    "user": "jonhanke"
}
```
Assignee: justin

CC:  mabshoff wstein tornaria

Completely rewritten and doctested Local densities routines according to a consistent interface (and algorithms) described in the attached PDF file.

Patch to follow very shortly!

Issue created by migration from https://trac.sagemath.org/ticket/6037





---

archive/issue_comments_048076.json:
```json
{
    "body": "Description of the inputs and algorithms used in QF local density routines",
    "created_at": "2009-05-14T10:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6037#issuecomment-48076",
    "user": "jonhanke"
}
```

Description of the inputs and algorithms used in QF local density routines



---

archive/issue_comments_048077.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-14T21:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6037#issuecomment-48077",
    "user": "jonhanke"
}
```

Attachment



---

archive/issue_comments_048078.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-14T21:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6037#issuecomment-48078",
    "user": "jonhanke"
}
```

Attachment



---

archive/issue_comments_048079.json:
```json
{
    "body": "Attachment\n\nLaTeX file used to create the PDF writeup",
    "created_at": "2009-05-15T18:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6037#issuecomment-48079",
    "user": "jonhanke"
}
```

Attachment

LaTeX file used to create the PDF writeup



---

archive/issue_comments_048080.json:
```json
{
    "body": "Looks nice. For the record, the following exported member functions (of QuadraticForm) have been renamed/removed:\n- `reindex_vector_from_extraction` was removed\n- `count_modp__by_gauss_sum` was renamed to `count_modp_solutions__by_Gauss_sum`.\n- `local_good_density_congruence_even__experimental` was removed.\n- `VecIncrement__deprecated` was removed.\n- `local_solution_type__deprecated` was removed.\n- `CountAllLocalTypesNaive__deprecated` was removed.\n- `count_local_type` was renamed to `count_congruence_solutions`.\n- `count_local_good_type` was renamed to `count_congruence_solutions__good_type`.\n- `count_local_zero_type` was renamed to `count_congruence_solutions__zero_type`.\n- `count_local_bad_type` was renamed to `count_congruence_solutions__bad_type`.\n- `count_local_bad_typeI` was renamed to `count_congruence_solutions__bad_type_I`.\n- `count_local_bad_typeII` was renamed to `count_congruence_solutions__bad_type_II`.\n- `local_good_density` was removed.\n- `local_zero_density` was removed.\n- `local_bad_density` was removed.\n- `local_badI_density` was removed.\n- `local_badII_density` was removed.\n\nI think the `__deprecated` and `__experimental` functions need no comment. For the renamed functions, though, it may be nice to add a compatibility wrapper with deprecation warning... (where and how?)\n\nJon, internal routines should be using names starting with an underscore (that's the python convention).",
    "created_at": "2009-05-19T00:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6037#issuecomment-48080",
    "user": "tornaria"
}
```

Looks nice. For the record, the following exported member functions (of QuadraticForm) have been renamed/removed:
- `reindex_vector_from_extraction` was removed
- `count_modp__by_gauss_sum` was renamed to `count_modp_solutions__by_Gauss_sum`.
- `local_good_density_congruence_even__experimental` was removed.
- `VecIncrement__deprecated` was removed.
- `local_solution_type__deprecated` was removed.
- `CountAllLocalTypesNaive__deprecated` was removed.
- `count_local_type` was renamed to `count_congruence_solutions`.
- `count_local_good_type` was renamed to `count_congruence_solutions__good_type`.
- `count_local_zero_type` was renamed to `count_congruence_solutions__zero_type`.
- `count_local_bad_type` was renamed to `count_congruence_solutions__bad_type`.
- `count_local_bad_typeI` was renamed to `count_congruence_solutions__bad_type_I`.
- `count_local_bad_typeII` was renamed to `count_congruence_solutions__bad_type_II`.
- `local_good_density` was removed.
- `local_zero_density` was removed.
- `local_bad_density` was removed.
- `local_badI_density` was removed.
- `local_badII_density` was removed.

I think the `__deprecated` and `__experimental` functions need no comment. For the renamed functions, though, it may be nice to add a compatibility wrapper with deprecation warning... (where and how?)

Jon, internal routines should be using names starting with an underscore (that's the python convention).



---

archive/issue_comments_048081.json:
```json
{
    "body": "Merged patch-2__QF_local_densities__3.4.1.patch in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T00:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6037#issuecomment-48081",
    "user": "mabshoff"
}
```

Merged patch-2__QF_local_densities__3.4.1.patch in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048082.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T00:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6037#issuecomment-48082",
    "user": "mabshoff"
}
```

Resolution: fixed
