# Issue 7420: Fix uncaught infinite loop in coercion discovery

archive/issues_007420.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat @robertwb\n\nKeywords: coercion\n\n#5597 or #5598 introduced a potential infinite loop (and segfault) upon coercion discovery on a cyclic graph. The first occurence of such a graph was with the newly refactored symmetric functions.\n\nThe attached patch fixes this. By the way, it uses a dictionary rather than a list to hold the marks used (register_pair) to detect cycles.\n\nThe category patches #5981 depend on this!!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7420\n\n",
    "created_at": "2009-11-10T00:45:07Z",
    "labels": [
        "component: coercion",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Fix uncaught infinite loop in coercion discovery",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7420",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_062323.json:
```json
{
    "body": "Attachment [trac_7420-fix-infinite-coercion-discovery-loop.patch](tarball://root/attachments/some-uuid/ticket7420/trac_7420-fix-infinite-coercion-discovery-loop.patch) by @nthiery created at 2009-11-10 00:48:04",
    "created_at": "2009-11-10T00:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62323",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7420-fix-infinite-coercion-discovery-loop.patch](tarball://root/attachments/some-uuid/ticket7420/trac_7420-fix-infinite-coercion-discovery-loop.patch) by @nthiery created at 2009-11-10 00:48:04



---

archive/issue_comments_062324.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-10T00:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62324",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062325.json:
```json
{
    "body": "I reviewed the change, and it looks good.\n\nRobert: please double check; I don't guarantee that all the invariants are preserved.",
    "created_at": "2009-11-10T00:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62325",
    "user": "https://github.com/nthiery"
}
```

I reviewed the change, and it looks good.

Robert: please double check; I don't guarantee that all the invariants are preserved.



---

archive/issue_comments_062326.json:
```json
{
    "body": "Another option is to wrap that coerce_map_from call in a _register_pair try/except block.",
    "created_at": "2009-11-10T05:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62326",
    "user": "https://github.com/mwhansen"
}
```

Another option is to wrap that coerce_map_from call in a _register_pair try/except block.



---

archive/issue_comments_062327.json:
```json
{
    "body": "Yes, calling _register_pair would work here, even a helper is_registered function might be better than using _coerce_test_dict directly. \n\nAlso, instead of \n\n\n```\n                connection = None \n                if EltPair(mor._domain, S, \"coerce\") not in _coerce_test_dict: \n                    connecting = mor._domain.coerce_map_from(S)\n                if connecting is not None: \n```\n\n\nit might be clearer to do \n\n\n```\n                if EltPair(mor._domain, S, \"coerce\") not in _coerce_test_dict: \n                    connecting = mor._domain.coerce_map_from(S)\n                    if connecting is not None: \n                        ...\n\n```\n",
    "created_at": "2009-11-10T07:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62327",
    "user": "https://github.com/robertwb"
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

archive/issue_comments_062328.json:
```json
{
    "body": "This is a variant of the previous patch, using register_pair",
    "created_at": "2009-11-11T08:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62328",
    "user": "https://github.com/nthiery"
}
```

This is a variant of the previous patch, using register_pair



---

archive/issue_comments_062329.json:
```json
{
    "body": "Attachment [trac_7420-fix-infinite-coercion-discovery-loop-2.patch](tarball://root/attachments/some-uuid/ticket7420/trac_7420-fix-infinite-coercion-discovery-loop-2.patch) by @nthiery created at 2009-11-11 08:44:48\n\nReplying to [comment:3 robertwb]:\n> Yes, calling _register_pair would work here\n\nI gave it a shot, and this works almost fine: all sage tests pass; except that for jack polynomials. Looking at it, it appears that the coercion model is picking a path which is *really* far from the shortest (see the attached log). The previous version was doing reasonably. This sounds like a pure piece of luck though, since in both cases, the strategy seems to be depth first search + limited selection among the first conversions found.\n\nRobert, Mike: from here, I see two options:\n- Either you spot something stupid I did in the second version of the patch, and then we go for it after fixing it.\n- Or we go for the first version of the patch for the moment (after applying Robert's suggestion for better indentation)\n\nIn both cases, after the category patches are in, we should definitely rewrite the coercion lookup to use a breath first search.",
    "created_at": "2009-11-11T08:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62329",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_062330.json:
```json
{
    "body": "Attachment [log](tarball://root/attachments/some-uuid/ticket7420/log) by @nthiery created at 2009-11-11 08:45:21\n\nLog showing a *long* conversion path",
    "created_at": "2009-11-11T08:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62330",
    "user": "https://github.com/nthiery"
}
```

Attachment [log](tarball://root/attachments/some-uuid/ticket7420/log) by @nthiery created at 2009-11-11 08:45:21

Log showing a *long* conversion path



---

archive/issue_comments_062331.json:
```json
{
    "body": "I should mention: the error appearing in the log comes from the having the coercion go through\njack polynomials at t=-1; apparently, the scalar product is then non positive, which causes the error. I have to check the literature. Maybe we should forbid t=-1, or at least not declare the corresponding broken coercions.",
    "created_at": "2009-11-11T08:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62331",
    "user": "https://github.com/nthiery"
}
```

I should mention: the error appearing in the log comes from the having the coercion go through
jack polynomials at t=-1; apparently, the scalar product is then non positive, which causes the error. I have to check the literature. Maybe we should forbid t=-1, or at least not declare the corresponding broken coercions.



---

archive/issue_comments_062332.json:
```json
{
    "body": "I'm going to move this to 4.3 where it's more relevant.",
    "created_at": "2009-11-13T04:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62332",
    "user": "https://github.com/mwhansen"
}
```

I'm going to move this to 4.3 where it's more relevant.



---

archive/issue_comments_062333.json:
```json
{
    "body": "I'd say at this point go for the first version of the patch, but with an eye towards improving things in the multiple paths case. (A breath first search sounds like a good idea, but could be more expensive if paths \"all the way down\" have already been explored. Also, there's the notion of assigning a cost to a morphism which has not been exploited.)",
    "created_at": "2009-11-14T07:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62333",
    "user": "https://github.com/robertwb"
}
```

I'd say at this point go for the first version of the patch, but with an eye towards improving things in the multiple paths case. (A breath first search sounds like a good idea, but could be more expensive if paths "all the way down" have already been explored. Also, there's the notion of assigning a cost to a morphism which has not been exploited.)



---

archive/issue_comments_062334.json:
```json
{
    "body": "I'll merge the first patch, and then look into a better solution.",
    "created_at": "2009-11-17T05:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62334",
    "user": "https://github.com/mwhansen"
}
```

I'll merge the first patch, and then look into a better solution.



---

archive/issue_comments_062335.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T05:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62335",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062336.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T05:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7420#issuecomment-62336",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
