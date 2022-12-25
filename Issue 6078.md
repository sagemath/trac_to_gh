# Issue 6078: Add compatibility functions with deprecation warnings for QF code after doctest patch

archive/issues_006078.json:
```json
{
    "body": "Assignee: tbd\n\nThe patches at #5954, #6037 and #6040 bring doctest coverage for quadratic forms up to 100%. In this patch series some functions were removed or renamed, so we should add compatibility functions.\n\nThese are the functions I propose we should handle:\n- count_modp__by_gauss_sum renamed to count_modp_solutions__by_Gauss_sum.\n- count_local_type was renamed to count_congruence_solutions.\n- count_local_good_type was renamed to count_congruence_solutions__good_type.\n- count_local_zero_type was renamed to count_congruence_solutions__zero_type. \n- count_local_bad_type was renamed to count_congruence_solutions__bad_type. \n- count_local_bad_typeI was renamed to count_congruence_solutions__bad_type_I. \n- count_local_bad_typeII was renamed to count_congruence_solutions__bad_type_II.\n- GHY_mass_maximal was renamed to GHY_mass__maximal.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6078\n\n",
    "created_at": "2009-05-19T00:53:35Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Add compatibility functions with deprecation warnings for QF code after doctest patch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6078",
    "user": "https://github.com/tornaria"
}
```
Assignee: tbd

The patches at #5954, #6037 and #6040 bring doctest coverage for quadratic forms up to 100%. In this patch series some functions were removed or renamed, so we should add compatibility functions.

These are the functions I propose we should handle:
- count_modp__by_gauss_sum renamed to count_modp_solutions__by_Gauss_sum.
- count_local_type was renamed to count_congruence_solutions.
- count_local_good_type was renamed to count_congruence_solutions__good_type.
- count_local_zero_type was renamed to count_congruence_solutions__zero_type. 
- count_local_bad_type was renamed to count_congruence_solutions__bad_type. 
- count_local_bad_typeI was renamed to count_congruence_solutions__bad_type_I. 
- count_local_bad_typeII was renamed to count_congruence_solutions__bad_type_II.
- GHY_mass_maximal was renamed to GHY_mass__maximal.

Issue created by migration from https://trac.sagemath.org/ticket/6078





---

archive/issue_comments_048283.json:
```json
{
    "body": "Note, there are other functions which were removed, but most of them were not implemented, or wrongly implemented, badly or no documented, etc. It really makes no sense to keep them around.",
    "created_at": "2009-05-19T00:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6078#issuecomment-48283",
    "user": "https://github.com/tornaria"
}
```

Note, there are other functions which were removed, but most of them were not implemented, or wrongly implemented, badly or no documented, etc. It really makes no sense to keep them around.



---

archive/issue_comments_048284.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-05-19T00:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6078#issuecomment-48284",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_048285.json:
```json
{
    "body": "Changing assignee from tbd to justin.",
    "created_at": "2009-05-19T00:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6078#issuecomment-48285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from tbd to justin.



---

archive/issue_comments_048286.json:
```json
{
    "body": "Changing component from algebra to quadratic forms.",
    "created_at": "2009-05-19T00:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6078#issuecomment-48286",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebra to quadratic forms.



---

archive/issue_comments_048287.json:
```json
{
    "body": "This isn't critical for 4.0.",
    "created_at": "2009-05-28T06:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6078#issuecomment-48287",
    "user": "https://github.com/williamstein"
}
```

This isn't critical for 4.0.



---

archive/issue_comments_048288.json:
```json
{
    "body": "I don't see the point in doing this, since quadratic forms was only in Sage for a very short amount of time before making this API change.",
    "created_at": "2009-06-15T23:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6078#issuecomment-48288",
    "user": "https://github.com/williamstein"
}
```

I don't see the point in doing this, since quadratic forms was only in Sage for a very short amount of time before making this API change.



---

archive/issue_comments_048289.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-15T23:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6078#issuecomment-48289",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid
