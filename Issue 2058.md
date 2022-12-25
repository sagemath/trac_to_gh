# Issue 2058: [with patch, needs review] PolyBoRi evaluation

archive/issues_002058.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nKeywords: polybori\n\nWith the attached patches `8314.patch` (by burcin) and `8315.patch` (by malb) the following now works:\n\n\n```\nsage: B.<x,y,z> = BooleanPolynomialRing(3)\nsage: x.subs({x:y})\ny\nsage: x.subs({'x':y})\ny\nsage: x.subs(x=y)\ny\n```\n\n\nThe implementation is far from being perfect but at least the functionality is there now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2058\n\n",
    "created_at": "2008-02-05T17:05:33Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, needs review] PolyBoRi evaluation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2058",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

Keywords: polybori

With the attached patches `8314.patch` (by burcin) and `8315.patch` (by malb) the following now works:


```
sage: B.<x,y,z> = BooleanPolynomialRing(3)
sage: x.subs({x:y})
y
sage: x.subs({'x':y})
y
sage: x.subs(x=y)
y
```


The implementation is far from being perfect but at least the functionality is there now.

Issue created by migration from https://trac.sagemath.org/ticket/2058





---

archive/issue_comments_013287.json:
```json
{
    "body": "Attachment [8314.patch](tarball://root/attachments/some-uuid/ticket2058/8314.patch) by @malb created at 2008-02-05 17:05:53\n\nBurcin's original __call__ patch",
    "created_at": "2008-02-05T17:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13287",
    "user": "https://github.com/malb"
}
```

Attachment [8314.patch](tarball://root/attachments/some-uuid/ticket2058/8314.patch) by @malb created at 2008-02-05 17:05:53

Burcin's original __call__ patch



---

archive/issue_comments_013288.json:
```json
{
    "body": "my doctests/corrections for Burcin's patch",
    "created_at": "2008-02-05T17:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13288",
    "user": "https://github.com/malb"
}
```

my doctests/corrections for Burcin's patch



---

archive/issue_comments_013289.json:
```json
{
    "body": "Attachment [8315.patch](tarball://root/attachments/some-uuid/ticket2058/8315.patch) by @malb created at 2008-02-05 22:08:46\n\npatch to be applied on top of the other two to speed up subs method",
    "created_at": "2008-02-05T22:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13289",
    "user": "https://github.com/malb"
}
```

Attachment [8315.patch](tarball://root/attachments/some-uuid/ticket2058/8315.patch) by @malb created at 2008-02-05 22:08:46

patch to be applied on top of the other two to speed up subs method



---

archive/issue_comments_013290.json:
```json
{
    "body": "Attachment [8317.patch](tarball://root/attachments/some-uuid/ticket2058/8317.patch) by @malb created at 2008-02-06 14:55:38\n\nyet another patch (to be applied on to of the rest) which speeds up substitution and evalutation",
    "created_at": "2008-02-06T14:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13290",
    "user": "https://github.com/malb"
}
```

Attachment [8317.patch](tarball://root/attachments/some-uuid/ticket2058/8317.patch) by @malb created at 2008-02-06 14:55:38

yet another patch (to be applied on to of the rest) which speeds up substitution and evalutation



---

archive/issue_comments_013291.json:
```json
{
    "body": "`8316.patch` reorders the coercion by moving integers more to the front. Burcin, if that affects performance for other operations negatively, let me know and I can move it back.",
    "created_at": "2008-02-06T15:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13291",
    "user": "https://github.com/malb"
}
```

`8316.patch` reorders the coercion by moving integers more to the front. Burcin, if that affects performance for other operations negatively, let me know and I can move it back.



---

archive/issue_comments_013292.json:
```json
{
    "body": "reintroduces evaluation with aribitrary values again",
    "created_at": "2008-02-06T16:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13292",
    "user": "https://github.com/malb"
}
```

reintroduces evaluation with aribitrary values again



---

archive/issue_comments_013293.json:
```json
{
    "body": "Attachment [8318.patch](tarball://root/attachments/some-uuid/ticket2058/8318.patch) by @malb created at 2008-02-06 16:12:40\n\nPatch `8318.patch` addresses a concern burcin raised in a private conversation.",
    "created_at": "2008-02-06T16:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13293",
    "user": "https://github.com/malb"
}
```

Attachment [8318.patch](tarball://root/attachments/some-uuid/ticket2058/8318.patch) by @malb created at 2008-02-06 16:12:40

Patch `8318.patch` addresses a concern burcin raised in a private conversation.



---

archive/issue_comments_013294.json:
```json
{
    "body": "Burcin mentioned some issues in a private communication. Don't apply yet.",
    "created_at": "2008-02-14T23:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13294",
    "user": "https://github.com/malb"
}
```

Burcin mentioned some issues in a private communication. Don't apply yet.



---

archive/issue_comments_013295.json:
```json
{
    "body": "Attachment [trac_2058_superpatch.patch](tarball://root/attachments/some-uuid/ticket2058/trac_2058_superpatch.patch) by @malb created at 2008-02-26 17:58:19\n\nthis patch replaces **all** other patches and should address Burcin's off-record concerns",
    "created_at": "2008-02-26T17:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13295",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2058_superpatch.patch](tarball://root/attachments/some-uuid/ticket2058/trac_2058_superpatch.patch) by @malb created at 2008-02-26 17:58:19

this patch replaces **all** other patches and should address Burcin's off-record concerns



---

archive/issue_comments_013296.json:
```json
{
    "body": "Burcin, could you check if both `__call__` and `subs` now behave as you would expect? I am trying to get this patch (or a corrected version) into 2.10.3. You only need the *superpatch*.",
    "created_at": "2008-02-26T18:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13296",
    "user": "https://github.com/malb"
}
```

Burcin, could you check if both `__call__` and `subs` now behave as you would expect? I am trying to get this patch (or a corrected version) into 2.10.3. You only need the *superpatch*.



---

archive/issue_comments_013297.json:
```json
{
    "body": "add doctest to _eval",
    "created_at": "2008-02-26T19:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13297",
    "user": "https://github.com/burcin"
}
```

add doctest to _eval



---

archive/issue_comments_013298.json:
```json
{
    "body": "Attachment [booleanmonomial_eval_doctest.patch](tarball://root/attachments/some-uuid/ticket2058/booleanmonomial_eval_doctest.patch) by @burcin created at 2008-02-26 19:55:19\n\nMartin's patch looks good, it should be applied.\n\nattachment:booleanmonomial_eval_doctest.patch makes it conform to the \"all functions should have a doctest\" rule. :)",
    "created_at": "2008-02-26T19:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13298",
    "user": "https://github.com/burcin"
}
```

Attachment [booleanmonomial_eval_doctest.patch](tarball://root/attachments/some-uuid/ticket2058/booleanmonomial_eval_doctest.patch) by @burcin created at 2008-02-26 19:55:19

Martin's patch looks good, it should be applied.

attachment:booleanmonomial_eval_doctest.patch makes it conform to the "all functions should have a doctest" rule. :)



---

archive/issue_events_002219.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-26T21:36:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2058#event-2219"
}
```



---

archive/issue_comments_013299.json:
```json
{
    "body": "Merged trac_2058_superpatch.patch and booleanmonomial_eval_doctest.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-26T21:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13299",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_2058_superpatch.patch and booleanmonomial_eval_doctest.patch in Sage 2.10.3.rc0



---

archive/issue_comments_013300.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-26T21:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2058#issuecomment-13300",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
