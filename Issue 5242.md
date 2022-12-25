# Issue 5242: [with patch, positive review] generic_power can now handle semi-groups

archive/issues_005242.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: generic power\n\nThe former implementation of generic_power_c made two assumptions\n- `not a` is well defined for any element a\n- There is a one\nThese two assumptions do not always always hold. So I reorganized the initial code which handle particular cases so that:\n- it does not call \"not a\" when the exponent n is different from zero\n- it delegates to ~a the responsibility of raising an error when the exponent n is negative and a is not invertible. This allows for monoids with partially defined inversion (e.g. the multiplicative monoid of Z/12Z).\n\nThis modification revealed a problem in matrices: the empty matrix 0x0 modulo 2 was tested to be non invertible! I changed the test to the correct value. \n\nInvestigating this revealed many other inconsistencies with matrices; those will be taken care of in a subsequent patch.   \n\nIssue created by migration from https://trac.sagemath.org/ticket/5242\n\n",
    "closed_at": "2009-02-15T07:17:26Z",
    "created_at": "2009-02-12T13:20:31Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] generic_power can now handle semi-groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5242",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: generic power

The former implementation of generic_power_c made two assumptions
- `not a` is well defined for any element a
- There is a one
These two assumptions do not always always hold. So I reorganized the initial code which handle particular cases so that:
- it does not call "not a" when the exponent n is different from zero
- it delegates to ~a the responsibility of raising an error when the exponent n is negative and a is not invertible. This allows for monoids with partially defined inversion (e.g. the multiplicative monoid of Z/12Z).

This modification revealed a problem in matrices: the empty matrix 0x0 modulo 2 was tested to be non invertible! I changed the test to the correct value. 

Investigating this revealed many other inconsistencies with matrices; those will be taken care of in a subsequent patch.   

Issue created by migration from https://trac.sagemath.org/ticket/5242





---

archive/issue_comments_040097.json:
```json
{
    "body": "Proposal of patch for generic power",
    "created_at": "2009-02-12T13:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40097",
    "user": "https://github.com/hivert"
}
```

Proposal of patch for generic power



---

archive/issue_comments_040098.json:
```json
{
    "body": "Attachment [generic_power_fix_semigroup-5242-submitted.patch](tarball://root/attachments/some-uuid/ticket5242/generic_power_fix_semigroup-5242-submitted.patch) by mabshoff created at 2009-02-12 13:50:42",
    "created_at": "2009-02-12T13:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40098",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [generic_power_fix_semigroup-5242-submitted.patch](tarball://root/attachments/some-uuid/ticket5242/generic_power_fix_semigroup-5242-submitted.patch) by mabshoff created at 2009-02-12 13:50:42



---

archive/issue_comments_040099.json:
```json
{
    "body": "Changing assignee from tbd to @hivert.",
    "created_at": "2009-02-13T18:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40099",
    "user": "https://github.com/hivert"
}
```

Changing assignee from tbd to @hivert.



---

archive/issue_comments_040100.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T18:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40100",
    "user": "https://github.com/hivert"
}
```

Changing status from new to assigned.



---

archive/issue_events_012170.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2009-02-13T18:54:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5242#event-12170"
}
```



---

archive/issue_comments_040101.json:
```json
{
    "body": "I would prefer not to have implicit casting of general types to booleans.  Can we not have \"if n==0\" or \"if n.is_zero()\" instead of \"if not n\", and similar?  Remember that Sage code is all visible to users, so we should avoid obscure programming idioms.",
    "created_at": "2009-02-14T14:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40101",
    "user": "https://github.com/JohnCremona"
}
```

I would prefer not to have implicit casting of general types to booleans.  Can we not have "if n==0" or "if n.is_zero()" instead of "if not n", and similar?  Remember that Sage code is all visible to users, so we should avoid obscure programming idioms.



---

archive/issue_comments_040102.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\nYes Sure. I more than agree with you. Remember that I didn't wrote this code, I just reorganize the order in which the tests are done. I'll soon propose another patch with a better idiom.",
    "created_at": "2009-02-14T15:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40102",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:5 cremona]:
Yes Sure. I more than agree with you. Remember that I didn't wrote this code, I just reorganize the order in which the tests are done. I'll soon propose another patch with a better idiom.



---

archive/issue_comments_040103.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\nActually it seems that for n it is possible because we know its type. On the contrary it is not possible for a. Indeed a can be a plain Python int (wich forbid the use of `a.is_zero()`) of any type eg polynomial with forbid the use of `== 0` so I don't know what else to do (I'm far from being a cython expert) :\n\n```\n sage -t  \"devel/sage-combinat/sage/rings/polynomial/polydict.pyx\"\n**********************************************************************\nFile \"/usr/local/sage/devel/sage-combinat/sage/rings/polynomial/polydict.pyx\", line 695:\n    sage: (f-f)**0\nExpected:\n    Traceback (most recent call last):\n    ...\n    ArithmeticError: 0^0 is undefined.\nGot:\n    PolyDict with representation {0: 1}\n```\n\nSo if there is no better suggestion I'll stick with the current patch.",
    "created_at": "2009-02-14T15:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40103",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:5 cremona]:
Actually it seems that for n it is possible because we know its type. On the contrary it is not possible for a. Indeed a can be a plain Python int (wich forbid the use of `a.is_zero()`) of any type eg polynomial with forbid the use of `== 0` so I don't know what else to do (I'm far from being a cython expert) :

```
 sage -t  "devel/sage-combinat/sage/rings/polynomial/polydict.pyx"
**********************************************************************
File "/usr/local/sage/devel/sage-combinat/sage/rings/polynomial/polydict.pyx", line 695:
    sage: (f-f)**0
Expected:
    Traceback (most recent call last):
    ...
    ArithmeticError: 0^0 is undefined.
Got:
    PolyDict with representation {0: 1}
```

So if there is no better suggestion I'll stick with the current patch.



---

archive/issue_comments_040104.json:
```json
{
    "body": "I just tested my current 3.3.rc1 merge tree with this patch and\n\n```\nAll tests passed!\n```\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T16:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I just tested my current 3.3.rc1 merge tree with this patch and

```
All tests passed!
```

Cheers,

Michael



---

archive/issue_comments_040105.json:
```json
{
    "body": "Patch reads good, I suggest to open another ticket for the style issue.",
    "created_at": "2009-02-14T17:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40105",
    "user": "https://github.com/malb"
}
```

Patch reads good, I suggest to open another ticket for the style issue.



---

archive/issue_comments_040106.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40106",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040107.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-15T07:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5242#issuecomment-40107",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012171.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-15T07:17:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5242",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5242#event-12171"
}
```
