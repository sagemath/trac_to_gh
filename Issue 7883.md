# Issue 7883: Added some functionality to ideals

archive/issues_007883.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @roed314\n\nAdded some functionality to ideals (is_maximal works more often now, and there's a new ideal class for univariate polynomial rings).  Changed the logic on what class is chosen for ideals so that it's easier to override with _ideal_class_.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7883\n\n",
    "created_at": "2010-01-09T20:07:10Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Added some functionality to ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7883",
    "user": "https://github.com/robertwb"
}
```
Assignee: @malb

CC:  @roed314

Added some functionality to ideals (is_maximal works more often now, and there's a new ideal class for univariate polynomial rings).  Changed the logic on what class is chosen for ideals so that it's easier to override with _ideal_class_.

Issue created by migration from https://trac.sagemath.org/ticket/7883





---

archive/issue_comments_068395.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-09T20:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68395",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068396.json:
```json
{
    "body": "Attachment [7585_7_ideal.patch](tarball://root/attachments/some-uuid/ticket7883/7585_7_ideal.patch) by @robertwb created at 2010-01-09 20:11:52\n\nThere's a lot of useful looking code in here, but it's unclear what exactly it does or it's intended to fix. Some more explanations would be nice, and the new behavior should be doctested. Especially for most of the changes in `sage/rings/ideal.py`\n\nWhat is the parameter in _ideal_class_ supposed to mean? (Then why is it 0 by default?) \n\nDepends on #7881?",
    "created_at": "2010-01-09T20:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68396",
    "user": "https://github.com/robertwb"
}
```

Attachment [7585_7_ideal.patch](tarball://root/attachments/some-uuid/ticket7883/7585_7_ideal.patch) by @robertwb created at 2010-01-09 20:11:52

There's a lot of useful looking code in here, but it's unclear what exactly it does or it's intended to fix. Some more explanations would be nice, and the new behavior should be doctested. Especially for most of the changes in `sage/rings/ideal.py`

What is the parameter in _ideal_class_ supposed to mean? (Then why is it 0 by default?) 

Depends on #7881?



---

archive/issue_comments_068397.json:
```json
{
    "body": "Attachment [7883_ideals.patch](tarball://root/attachments/some-uuid/ticket7883/7883_ideals.patch) by @roed314 created at 2010-02-23 15:04:02\n\nRebased against 4.3.3; may need 8218, 8332, 7880, but probably not.",
    "created_at": "2010-02-23T15:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68397",
    "user": "https://github.com/roed314"
}
```

Attachment [7883_ideals.patch](tarball://root/attachments/some-uuid/ticket7883/7883_ideals.patch) by @roed314 created at 2010-02-23 15:04:02

Rebased against 4.3.3; may need 8218, 8332, 7880, but probably not.



---

archive/issue_comments_068398.json:
```json
{
    "body": "I haven't made the changes Robert suggested, but I wanted to get an updated patch up since other finite field functionality depends on this.",
    "created_at": "2010-02-23T15:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68398",
    "user": "https://github.com/roed314"
}
```

I haven't made the changes Robert suggested, but I wanted to get an updated patch up since other finite field functionality depends on this.



---

archive/issue_comments_068399.json:
```json
{
    "body": "Part of a series:\n\n```\n8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335\n```\n\nI tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.",
    "created_at": "2010-02-23T17:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68399",
    "user": "https://github.com/roed314"
}
```

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.



---

archive/issue_comments_068400.json:
```json
{
    "body": "Tried this under 4.3.4.rc0 with 8218, 8332, 7880 applied. It applies fine but seven doctests fail. Moreover, I second Robert's criticism: it's not clear what all this new code is actually for. (The fact that other finite-field stuff depends on this doesn't change that.) Can we have a new patch with some more docstrings etc?",
    "created_at": "2010-03-17T22:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68400",
    "user": "https://github.com/loefflerd"
}
```

Tried this under 4.3.4.rc0 with 8218, 8332, 7880 applied. It applies fine but seven doctests fail. Moreover, I second Robert's criticism: it's not clear what all this new code is actually for. (The fact that other finite-field stuff depends on this doesn't change that.) Can we have a new patch with some more docstrings etc?



---

archive/issue_comments_068401.json:
```json
{
    "body": "Attachment [7883_fixes.patch](tarball://root/attachments/some-uuid/ticket7883/7883_fixes.patch) by @roed314 created at 2010-09-19 01:43:08\n\nAddresses referee comments",
    "created_at": "2010-09-19T01:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68401",
    "user": "https://github.com/roed314"
}
```

Attachment [7883_fixes.patch](tarball://root/attachments/some-uuid/ticket7883/7883_fixes.patch) by @roed314 created at 2010-09-19 01:43:08

Addresses referee comments



---

archive/issue_comments_068402.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-19T13:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68402",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068403.json:
```json
{
    "body": "Apply:\n\n\n```\n7883_ideals.patch\n7883_fixes.patch\n```\n\n\nProbably will not pass doctests unless you also apply the patches on #8333 and #8334.",
    "created_at": "2010-09-19T13:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68403",
    "user": "https://github.com/roed314"
}
```

Apply:


```
7883_ideals.patch
7883_fixes.patch
```


Probably will not pass doctests unless you also apply the patches on #8333 and #8334.



---

archive/issue_comments_068404.json:
```json
{
    "body": "Apply only this patch",
    "created_at": "2010-09-23T15:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68404",
    "user": "https://github.com/loefflerd"
}
```

Apply only this patch



---

archive/issue_comments_068405.json:
```json
{
    "body": "Attachment [trac_7883-ideals-folded.patch](tarball://root/attachments/some-uuid/ticket7883/trac_7883-ideals-folded.patch) by @loefflerd created at 2010-09-23 15:36:30\n\nI've uploaded a patch above which consists of \n- the two patches mentioned in roed's previous comment \n- the hunk from `7585_12_1_fixes.2.patch` (at #8334) that concerns `sage/rings/ring.pyx`\n- a tiny fix to remove the code in `ideal_1poly_field` that calls `residue_field`, since the residue fields code isn't going in until a subsequent patch.\n\nI have checked that this applies cleanly to 4.6.alpha1 and passes long doctests.",
    "created_at": "2010-09-23T15:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68405",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_7883-ideals-folded.patch](tarball://root/attachments/some-uuid/ticket7883/trac_7883-ideals-folded.patch) by @loefflerd created at 2010-09-23 15:36:30

I've uploaded a patch above which consists of 
- the two patches mentioned in roed's previous comment 
- the hunk from `7585_12_1_fixes.2.patch` (at #8334) that concerns `sage/rings/ring.pyx`
- a tiny fix to remove the code in `ideal_1poly_field` that calls `residue_field`, since the residue fields code isn't going in until a subsequent patch.

I have checked that this applies cleanly to 4.6.alpha1 and passes long doctests.



---

archive/issue_comments_068406.json:
```json
{
    "body": "Changing keywords from \"\" to \"ideals\".",
    "created_at": "2010-09-23T15:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68406",
    "user": "https://github.com/loefflerd"
}
```

Changing keywords from "" to "ideals".



---

archive/issue_comments_068407.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T15:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68407",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7883#issuecomment-68408",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
