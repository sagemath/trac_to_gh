# Issue 9155: G.list() can be modified

archive/issues_009155.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @rbeezer @fchapoton\n\ncached_method should not be used with mutable return values\n\n\n```\nsage: G = SymmetricGroup(2)\nsage: elements = G.list()\nsage: elements.remove(G(\"()\"))\nsage: G.list()\n[(1,2)]\nsage: K = SymmetricGroup(2)\nsage: K.list()\n[(1,2)]\n```\n\n\nas reported at http://groups.google.com/group/sage-devel/browse_thread/thread/265e134a585cf2bf\n\nIssue created by migration from https://trac.sagemath.org/ticket/9155\n\n",
    "created_at": "2010-06-06T04:35:30Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.2",
    "title": "G.list() can be modified",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9155",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza

CC:  @rbeezer @fchapoton

cached_method should not be used with mutable return values


```
sage: G = SymmetricGroup(2)
sage: elements = G.list()
sage: elements.remove(G("()"))
sage: G.list()
[(1,2)]
sage: K = SymmetricGroup(2)
sage: K.list()
[(1,2)]
```


as reported at http://groups.google.com/group/sage-devel/browse_thread/thread/265e134a585cf2bf

Issue created by migration from https://trac.sagemath.org/ticket/9155





---

archive/issue_comments_085337.json:
```json
{
    "body": "See also #10927.",
    "created_at": "2014-03-15T13:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85337",
    "user": "https://github.com/mezzarobba"
}
```

See also #10927.



---

archive/issue_comments_085338.json:
```json
{
    "body": "This bug has been corrected. (#10927 is another thing,)",
    "created_at": "2016-04-22T12:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85338",
    "user": "https://github.com/jm58660"
}
```

This bug has been corrected. (#10927 is another thing,)



---

archive/issue_comments_085339.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-22T12:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85339",
    "user": "https://github.com/jm58660"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085340.json:
```json
{
    "body": "Test added as suggested in email.\n----\nNew commits:",
    "created_at": "2016-04-29T08:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85340",
    "user": "https://github.com/jm58660"
}
```

Test added as suggested in email.
----
New commits:



---

archive/issue_comments_085341.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2016-04-29T08:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85341",
    "user": "https://github.com/jm58660"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_085342.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2016-04-29T08:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85342",
    "user": "https://github.com/jm58660"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_085343.json:
```json
{
    "body": "Changing component from algebra to group theory.",
    "created_at": "2016-04-29T08:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85343",
    "user": "https://github.com/jm58660"
}
```

Changing component from algebra to group theory.



---

archive/issue_comments_085344.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-29T08:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85344",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085345.json:
```json
{
    "body": "ok, let it be, thanks",
    "created_at": "2016-04-29T08:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85345",
    "user": "https://github.com/fchapoton"
}
```

ok, let it be, thanks



---

archive/issue_comments_085346.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-05-01T16:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9155#issuecomment-85346",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
