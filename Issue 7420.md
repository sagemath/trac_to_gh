# Issue 7420: Fix uncaught infinite loop in coercion discovery

archive/issues_007420.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat @robertwb\n\nKeywords: coercion\n\n#5597 or #5598 introduced a potential infinite loop (and segfault) upon coercion discovery on a cyclic graph. The first occurence of such a graph was with the newly refactored symmetric functions.\n\nThe attached patch fixes this. By the way, it uses a dictionary rather than a list to hold the marks used (register_pair) to detect cycles.\n\nThe category patches #5981 depend on this!!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7420\n\n",
    "created_at": "2009-11-10T00:45:07Z",
    "labels": [
        "coercion",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Fix uncaught infinite loop in coercion discovery",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7420",
    "user": "@nthiery"
}
```
Assignee: @mwhansen

CC:  sage-combinat @robertwb

Keywords: coercion

#5597 or #5598 introduced a potential infinite loop (and segfault) upon coercion discovery on a cyclic graph. The first occurence of such a graph was with the newly refactored symmetric functions.

The attached patch fixes this. By the way, it uses a dictionary rather than a list to hold the marks used (register_pair) to detect cycles.

The category patches #5981 depend on this!!!

Issue created by migration from https://trac.sagemath.org/ticket/7420





---

archive/issue_comments_062438.json:
```json
{
    "body": "Attachment [trac_7420-fix-infinite-coercion-discovery-loop.patch](tarball://root/attachments/some-uuid/ticket7420/trac_7420-fix-infinite-coercion-discovery-loop.patch) by @nthiery created at 2009-11-10 00:48:04",
    "created_at": "2009-11-10T00:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62438",
    "user": "@nthiery"
}
```

Attachment [trac_7420-fix-infinite-coercion-discovery-loop.patch](tarball://root/attachments/some-uuid/ticket7420/trac_7420-fix-infinite-coercion-discovery-loop.patch) by @nthiery created at 2009-11-10 00:48:04



---

archive/issue_comments_062439.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-10T00:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62439",
    "user": "@nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062440.json:
```json
{
    "body": "I reviewed the change, and it looks good.\n\nRobert: please double check; I don't guarantee that all the invariants are preserved.",
    "created_at": "2009-11-10T00:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62440",
    "user": "@nthiery"
}
```

I reviewed the change, and it looks good.

Robert: please double check; I don't guarantee that all the invariants are preserved.



---

archive/issue_comments_062441.json:
```json
{
    "body": "Another option is to wrap that coerce_map_from call in a _register_pair try/except block.",
    "created_at": "2009-11-10T05:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62441",
    "user": "@mwhansen"
}
```

Another option is to wrap that coerce_map_from call in a _register_pair try/except block.



---

archive/issue_comments_062442.json:
```json
{
    "body": "Yes, calling _register_pair would work here, even a helper is_registered function might be better than using _coerce_test_dict directly. \n\nAlso, instead of \n\n\n```\n                connection = None \n                if EltPair(mor._domain, S, \"coerce\") not in _coerce_test_dict: \n                    connecting = mor._domain.coerce_map_from(S)\n                if connecting is not None: \n```\n\n\nit might be clearer to do \n\n\n```\n                if EltPair(mor._domain, S, \"coerce\") not in _coerce_test_dict: \n                    connecting = mor._domain.coerce_map_from(S)\n                    if connecting is not None: \n                        ...\n\n```\n",
    "created_at": "2009-11-10T07:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62442",
    "user": "@robertwb"
}
```

Yes, calling _register_pair would work here, even a helper is_registered function might be better than using _coerce_test_dict directly. 

Also, instead of 


```
                connection = None 
                if EltPair(mor._domain, S, "coerce") not in _coerce_test_dict: 
                    connecting = mor._domain.coerce_map_from(S)
                if connecting is not None: 
```


it might be clearer to do 


```
                if EltPair(mor._domain, S, "coerce") not in _coerce_test_dict: 
                    connecting = mor._domain.coerce_map_from(S)
                    if connecting is not None: 
                        ...

```




---

archive/issue_comments_062443.json:
```json
{
    "body": "This is a variant of the previous patch, using register_pair",
    "created_at": "2009-11-11T08:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62443",
    "user": "@nthiery"
}
```

This is a variant of the previous patch, using register_pair



---

archive/issue_comments_062444.json:
```json
{
    "body": "Attachment [trac_7420-fix-infinite-coercion-discovery-loop-2.patch](tarball://root/attachments/some-uuid/ticket7420/trac_7420-fix-infinite-coercion-discovery-loop-2.patch) by @nthiery created at 2009-11-11 08:44:48\n\nReplying to [comment:3 robertwb]:\n> Yes, calling _register_pair would work here\n\nI gave it a shot, and this works almost fine: all sage tests pass; except that for jack polynomials. Looking at it, it appears that the coercion model is picking a path which is *really* far from the shortest (see the attached log). The previous version was doing reasonably. This sounds like a pure piece of luck though, since in both cases, the strategy seems to be depth first search + limited selection among the first conversions found.\n\nRobert, Mike: from here, I see two options:\n- Either you spot something stupid I did in the second version of the patch, and then we go for it after fixing it.\n- Or we go for the first version of the patch for the moment (after applying Robert's suggestion for better indentation)\n\nIn both cases, after the category patches are in, we should definitely rewrite the coercion lookup to use a breath first search.",
    "created_at": "2009-11-11T08:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62444",
    "user": "@nthiery"
}
```

Attachment [trac_7420-fix-infinite-coercion-discovery-loop-2.patch](tarball://root/attachments/some-uuid/ticket7420/trac_7420-fix-infinite-coercion-discovery-loop-2.patch) by @nthiery created at 2009-11-11 08:44:48

Replying to [comment:3 robertwb]:
> Yes, calling _register_pair would work here

I gave it a shot, and this works almost fine: all sage tests pass; except that for jack polynomials. Looking at it, it appears that the coercion model is picking a path which is *really* far from the shortest (see the attached log). The previous version was doing reasonably. This sounds like a pure piece of luck though, since in both cases, the strategy seems to be depth first search + limited selection among the first conversions found.

Robert, Mike: from here, I see two options:
- Either you spot something stupid I did in the second version of the patch, and then we go for it after fixing it.
- Or we go for the first version of the patch for the moment (after applying Robert's suggestion for better indentation)

In both cases, after the category patches are in, we should definitely rewrite the coercion lookup to use a breath first search.



---

archive/issue_comments_062445.json:
```json
{
    "body": "Attachment [log](tarball://root/attachments/some-uuid/ticket7420/log) by @nthiery created at 2009-11-11 08:45:21\n\nLog showing a *long* conversion path",
    "created_at": "2009-11-11T08:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62445",
    "user": "@nthiery"
}
```

Attachment [log](tarball://root/attachments/some-uuid/ticket7420/log) by @nthiery created at 2009-11-11 08:45:21

Log showing a *long* conversion path



---

archive/issue_comments_062446.json:
```json
{
    "body": "I should mention: the error appearing in the log comes from the having the coercion go through\njack polynomials at t=-1; apparently, the scalar product is then non positive, which causes the error. I have to check the literature. Maybe we should forbid t=-1, or at least not declare the corresponding broken coercions.",
    "created_at": "2009-11-11T08:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62446",
    "user": "@nthiery"
}
```

I should mention: the error appearing in the log comes from the having the coercion go through
jack polynomials at t=-1; apparently, the scalar product is then non positive, which causes the error. I have to check the literature. Maybe we should forbid t=-1, or at least not declare the corresponding broken coercions.



---

archive/issue_comments_062447.json:
```json
{
    "body": "I'm going to move this to 4.3 where it's more relevant.",
    "created_at": "2009-11-13T04:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62447",
    "user": "@mwhansen"
}
```

I'm going to move this to 4.3 where it's more relevant.



---

archive/issue_comments_062448.json:
```json
{
    "body": "I'd say at this point go for the first version of the patch, but with an eye towards improving things in the multiple paths case. (A breath first search sounds like a good idea, but could be more expensive if paths \"all the way down\" have already been explored. Also, there's the notion of assigning a cost to a morphism which has not been exploited.)",
    "created_at": "2009-11-14T07:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62448",
    "user": "@robertwb"
}
```

I'd say at this point go for the first version of the patch, but with an eye towards improving things in the multiple paths case. (A breath first search sounds like a good idea, but could be more expensive if paths "all the way down" have already been explored. Also, there's the notion of assigning a cost to a morphism which has not been exploited.)



---

archive/issue_comments_062449.json:
```json
{
    "body": "I'll merge the first patch, and then look into a better solution.",
    "created_at": "2009-11-17T05:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62449",
    "user": "@mwhansen"
}
```

I'll merge the first patch, and then look into a better solution.



---

archive/issue_comments_062450.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T05:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62450",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062451.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T05:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62451",
    "user": "@mwhansen"
}
```

Resolution: fixed
