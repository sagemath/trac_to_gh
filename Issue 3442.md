# Issue 3442: is_normal for permutation groups gives wrong answer

archive/issues_003442.json:
```json
{
    "body": "Assignee: joyner\n\nThe example in the docstring for `is_normal` in `sage/groups/perm_gps/permgroup.py` in sage-3.0.3.alpha2 is wrong.\n\n\n```\n\n        Return True if the group self is a normal subgroup of other.\n\n        EXAMPLES:\n            sage: G = PermutationGroup(['(1,2,3)(4,5)'])\n            sage: H = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])\n            sage: G.is_normal(H)\n            True\n```\n\n\n(Aside: isn't it more natural to let H be a subgroup of G instead of the other way around?)\n\nG is not a normal subgroup of H since conjugation by (1,2,3,4,5) does not map G to G.\n\nOther example:\n\n```\nsage: G = SymmetricGroup(3); G.1\n(1,2)\nsage: H = G.subgroup( [ G.1 ] )\nsage: H.is_normal(G)\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3442\n\n",
    "created_at": "2008-06-16T22:37:41Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "is_normal for permutation groups gives wrong answer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3442",
    "user": "wjp"
}
```
Assignee: joyner

The example in the docstring for `is_normal` in `sage/groups/perm_gps/permgroup.py` in sage-3.0.3.alpha2 is wrong.


```

        Return True if the group self is a normal subgroup of other.

        EXAMPLES:
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: H = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_normal(H)
            True
```


(Aside: isn't it more natural to let H be a subgroup of G instead of the other way around?)

G is not a normal subgroup of H since conjugation by (1,2,3,4,5) does not map G to G.

Other example:

```
sage: G = SymmetricGroup(3); G.1
(1,2)
sage: H = G.subgroup( [ G.1 ] )
sage: H.is_normal(G)
True
```


Issue created by migration from https://trac.sagemath.org/ticket/3442





---

archive/issue_comments_024282.json:
```json
{
    "body": "Yes, the documentation is wrong (the function is okay). My fault. Sorry.\n\n\n```\ngap> G := Group([(1,2,3)(4,5)]);\nGroup([ (1,2,3)(4,5) ])\ngap> H := Group([(1,2,3)(4,5), (1,2,3,4,5)]);\nGroup([ (1,2,3)(4,5), (1,2,3,4,5) ])\ngap> IsNormal(H,G);\nfalse\n```\n\nThe docstring should read\n\n\n```\nReturn True if the group other is a normal subgroup of self.\n\nEXAMPLES: \n    sage: G = PermutationGroup(['(1,2,3)(4,5)'])\n    sage: H = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])\n    sage: H.is_normal(G)\n    False\n```\n",
    "created_at": "2008-06-16T23:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24282",
    "user": "wdj"
}
```

Yes, the documentation is wrong (the function is okay). My fault. Sorry.


```
gap> G := Group([(1,2,3)(4,5)]);
Group([ (1,2,3)(4,5) ])
gap> H := Group([(1,2,3)(4,5), (1,2,3,4,5)]);
Group([ (1,2,3)(4,5), (1,2,3,4,5) ])
gap> IsNormal(H,G);
false
```

The docstring should read


```
Return True if the group other is a normal subgroup of self.

EXAMPLES: 
    sage: G = PermutationGroup(['(1,2,3)(4,5)'])
    sage: H = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
    sage: H.is_normal(G)
    False
```




---

archive/issue_comments_024283.json:
```json
{
    "body": "docstring patch bases on 3.0.3.rc0",
    "created_at": "2008-06-17T17:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24283",
    "user": "wdj"
}
```

docstring patch bases on 3.0.3.rc0



---

archive/issue_comments_024284.json:
```json
{
    "body": "Attachment [9860.patch](tarball://root/attachments/some-uuid/ticket3442/9860.patch) by wdj created at 2008-06-17 17:46:07\n\nA patch for this docstring error is posted which is based on sage-3.0.3.rc0. \n\nInstall and sage -testall passed for sage-3.0.3.rc0. Also, this patch passed using sage -t. However, running sage -testall on this patch resulted in a lock-up on padic_lseries.py. I'll try again but think this is an unrelated issue.\n\nI could create another patch which does reordering of the methods alphabetically (as was done earlier). However, it seems I'm the only one who cares, so unless someone yells, I'll drop that idea.",
    "created_at": "2008-06-17T17:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24284",
    "user": "wdj"
}
```

Attachment [9860.patch](tarball://root/attachments/some-uuid/ticket3442/9860.patch) by wdj created at 2008-06-17 17:46:07

A patch for this docstring error is posted which is based on sage-3.0.3.rc0. 

Install and sage -testall passed for sage-3.0.3.rc0. Also, this patch passed using sage -t. However, running sage -testall on this patch resulted in a lock-up on padic_lseries.py. I'll try again but think this is an unrelated issue.

I could create another patch which does reordering of the methods alphabetically (as was done earlier). However, it seems I'm the only one who cares, so unless someone yells, I'll drop that idea.



---

archive/issue_comments_024285.json:
```json
{
    "body": "I reran sage -testall and all tests passed on this patch.",
    "created_at": "2008-06-17T19:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24285",
    "user": "wdj"
}
```

I reran sage -testall and all tests passed on this patch.



---

archive/issue_comments_024286.json:
```json
{
    "body": "Wouldn't not changing the function itself mean that now is_normal claims that S_5 is normal in `< (1,2,3)(4,5) >`, even though it isn't even a subgroup?",
    "created_at": "2008-06-17T21:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24286",
    "user": "wjp"
}
```

Wouldn't not changing the function itself mean that now is_normal claims that S_5 is normal in `< (1,2,3)(4,5) >`, even though it isn't even a subgroup?



---

archive/issue_comments_024287.json:
```json
{
    "body": "According to the GAP documentation for the function IsNormal (which is what is_normal wraps):\n\n\n```\nIsNormal( G, U ) O\n\nreturns true if the group G normalizes the group U and false otherwise.\n\nA group G normalizes a group U if and only if for every g \u2208 G and u \u2208 U the element ug is a member of U. Note that U need not be a subgroup of G. \n```\n\n\nSo the docstring, as corrected in the patch, is correct but does not tell the full story. Do you think it should be further elaborated?",
    "created_at": "2008-06-17T23:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24287",
    "user": "wdj"
}
```

According to the GAP documentation for the function IsNormal (which is what is_normal wraps):


```
IsNormal( G, U ) O

returns true if the group G normalizes the group U and false otherwise.

A group G normalizes a group U if and only if for every g ∈ G and u ∈ U the element ug is a member of U. Note that U need not be a subgroup of G. 
```


So the docstring, as corrected in the patch, is correct but does not tell the full story. Do you think it should be further elaborated?



---

archive/issue_comments_024288.json:
```json
{
    "body": "I think naming the current function '`normalizes`' would be better. A new `is_normal` function could then check if 'self' is a normal subgroup of 'other' (by doing `self.is_subgroup(other) and other.normalizes(self)` ?). This would be more consistent with how `is_subgroup`, `is_subring`, `is_subspace` order their arguments, IMO.",
    "created_at": "2008-06-19T07:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24288",
    "user": "wjp"
}
```

I think naming the current function '`normalizes`' would be better. A new `is_normal` function could then check if 'self' is a normal subgroup of 'other' (by doing `self.is_subgroup(other) and other.normalizes(self)` ?). This would be more consistent with how `is_subgroup`, `is_subring`, `is_subspace` order their arguments, IMO.



---

archive/issue_comments_024289.json:
```json
{
    "body": "again, based on 3.0.3.rc0. Should be applied after 9860.",
    "created_at": "2008-06-19T11:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24289",
    "user": "wdj"
}
```

again, based on 3.0.3.rc0. Should be applied after 9860.



---

archive/issue_comments_024290.json:
```json
{
    "body": "Attachment [9861.patch](tarball://root/attachments/some-uuid/ticket3442/9861.patch) by wdj created at 2008-06-19 11:06:53\n\nDone. Please apply 9860 then 9861 to sage-3.0.3.rc0 to get the behavior you requested.",
    "created_at": "2008-06-19T11:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24290",
    "user": "wdj"
}
```

Attachment [9861.patch](tarball://root/attachments/some-uuid/ticket3442/9861.patch) by wdj created at 2008-06-19 11:06:53

Done. Please apply 9860 then 9861 to sage-3.0.3.rc0 to get the behavior you requested.



---

archive/issue_comments_024291.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-20T05:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24291",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_024292.json:
```json
{
    "body": "Attachment [trac_3442_swap_arguments.patch](tarball://root/attachments/some-uuid/ticket3442/trac_3442_swap_arguments.patch) by wjp created at 2008-06-20 19:16:53",
    "created_at": "2008-06-20T19:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24292",
    "user": "wjp"
}
```

Attachment [trac_3442_swap_arguments.patch](tarball://root/attachments/some-uuid/ticket3442/trac_3442_swap_arguments.patch) by wjp created at 2008-06-20 19:16:53



---

archive/issue_comments_024293.json:
```json
{
    "body": "I've added a third patch (apply after 9860 and 9861) that swaps the arguments to `is_normal`.\n\nIt makes `H.is_normal(G)` mean: H is a normal subgroup of G.\n\n(This is consistent with functions like `is_subgroup`, `is_subspace`.)",
    "created_at": "2008-06-20T19:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24293",
    "user": "wjp"
}
```

I've added a third patch (apply after 9860 and 9861) that swaps the arguments to `is_normal`.

It makes `H.is_normal(G)` mean: H is a normal subgroup of G.

(This is consistent with functions like `is_subgroup`, `is_subspace`.)



---

archive/issue_comments_024294.json:
```json
{
    "body": "I give the last patch a positive review, wjp gave the prior patches a positive review -> **positive review**.",
    "created_at": "2008-07-02T20:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24294",
    "user": "malb"
}
```

I give the last patch a positive review, wjp gave the prior patches a positive review -> **positive review**.



---

archive/issue_comments_024295.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.4.alpha2",
    "created_at": "2008-07-03T03:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24295",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.0.4.alpha2



---

archive/issue_comments_024296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-03T03:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3442#issuecomment-24296",
    "user": "mabshoff"
}
```

Resolution: fixed
