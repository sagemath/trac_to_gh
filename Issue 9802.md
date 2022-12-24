# Issue 9802: Generalize and document the random_matrix constructor

archive/issues_009802.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  bwonderly @mwhansen @wdjoyner @jasongrout\n\nThis will vastly improve the documentation of the `random_matrix` command in common use cases (integers, rationals,...).\n\nIt will also allow for new, more specialized constructions, such as Billy Wonderly's work at #9720, #9754, #9820.\n\nSee #9720 for motivating discussion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9803\n\n",
    "created_at": "2010-08-26T00:27:48Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Generalize and document the random_matrix constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9802",
    "user": "@rbeezer"
}
```
Assignee: jason, was

CC:  bwonderly @mwhansen @wdjoyner @jasongrout

This will vastly improve the documentation of the `random_matrix` command in common use cases (integers, rationals,...).

It will also allow for new, more specialized constructions, such as Billy Wonderly's work at #9720, #9754, #9820.

See #9720 for motivating discussion.

Issue created by migration from https://trac.sagemath.org/ticket/9803





---

archive/issue_comments_096306.json:
```json
{
    "body": "Attachment [trac_9803-random-matrix-constructor-v1.patch](tarball://root/attachments/some-uuid/ticket9803/trac_9803-random-matrix-constructor-v1.patch) by @rbeezer created at 2010-08-26 22:16:20",
    "created_at": "2010-08-26T22:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96306",
    "user": "@rbeezer"
}
```

Attachment [trac_9803-random-matrix-constructor-v1.patch](tarball://root/attachments/some-uuid/ticket9803/trac_9803-random-matrix-constructor-v1.patch) by @rbeezer created at 2010-08-26 22:16:20



---

archive/issue_comments_096307.json:
```json
{
    "body": "Patch expands the functionality of the `random_matrix` routine.  A matrix space is used to accumulate the base ring, dimensions and representation (sparse/dense).  This can then be passed to the new `random_*_matrix` routines where a matrix can actually be constructed and returned.\n\nDocumentation for previous behavior greatly expanded, notably for integer and rational matrices.  New routines are demonstrated, with clear directions (links, imports) to expanded documentation.\n\nHad to handle density and sparse keywords in a backwards-compatible fashion, so they are \"popped\" out of the `kwds` dictionary and passed as before to the matrix randomize() routine.  The keywords are now required and won't work as positional arguments.  Had to adjust code in the group theory isomorphism code in a couple of modules as a result.  Also the `random_matrix` command was employed coincidentally in a doctest in the lazy import routine.  I think the new version works just as well as a test, so I changed the output.\n\nThis code below looks like some artifact of the switch to allowing/disallowing zero entries.  I've left it in, though it *never* gets called in any of the tests (I checked).  Before my changes, `density` had a default value of 1, so you would have to consciously pass in `None` to make this happen.  It was not documented.\n\n\n```\n        if density is None:\n            A.randomize(density=float(1), nonzero=False, *args, **kwds)\n        else:\n            A.randomize(density=density, nonzero=True, *args, **kwds)\n```\n\n\nOne fix in mod n dense matrix code.  Could not figure out how `range(25)` was doing anything useful, and it was ending up in the algorithm argument, so in the end I just removed it and the affected test passes.",
    "created_at": "2010-08-26T22:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96307",
    "user": "@rbeezer"
}
```

Patch expands the functionality of the `random_matrix` routine.  A matrix space is used to accumulate the base ring, dimensions and representation (sparse/dense).  This can then be passed to the new `random_*_matrix` routines where a matrix can actually be constructed and returned.

Documentation for previous behavior greatly expanded, notably for integer and rational matrices.  New routines are demonstrated, with clear directions (links, imports) to expanded documentation.

Had to handle density and sparse keywords in a backwards-compatible fashion, so they are "popped" out of the `kwds` dictionary and passed as before to the matrix randomize() routine.  The keywords are now required and won't work as positional arguments.  Had to adjust code in the group theory isomorphism code in a couple of modules as a result.  Also the `random_matrix` command was employed coincidentally in a doctest in the lazy import routine.  I think the new version works just as well as a test, so I changed the output.

This code below looks like some artifact of the switch to allowing/disallowing zero entries.  I've left it in, though it *never* gets called in any of the tests (I checked).  Before my changes, `density` had a default value of 1, so you would have to consciously pass in `None` to make this happen.  It was not documented.


```
        if density is None:
            A.randomize(density=float(1), nonzero=False, *args, **kwds)
        else:
            A.randomize(density=density, nonzero=True, *args, **kwds)
```


One fix in mod n dense matrix code.  Could not figure out how `range(25)` was doing anything useful, and it was ending up in the algorithm argument, so in the end I just removed it and the affected test passes.



---

archive/issue_comments_096308.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T22:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96308",
    "user": "@rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096309.json:
```json
{
    "body": "Attachment [trac_9803-random-matrix-constructor-v2.patch](tarball://root/attachments/some-uuid/ticket9803/trac_9803-random-matrix-constructor-v2.patch) by @rbeezer created at 2010-08-27 01:43:36\n\nStandalone patch",
    "created_at": "2010-08-27T01:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96309",
    "user": "@rbeezer"
}
```

Attachment [trac_9803-random-matrix-constructor-v2.patch](tarball://root/attachments/some-uuid/ticket9803/trac_9803-random-matrix-constructor-v2.patch) by @rbeezer created at 2010-08-27 01:43:36

Standalone patch



---

archive/issue_comments_096310.json:
```json
{
    "body": "First patch contained:\n\n\n```\ncolumns = parent.nrows()\n```\n\n\nwhich is just plain wrong, but also `columns` was never referenced (which is why the doctests were unaffected).  Its gone now.  Use just the v2 patch.",
    "created_at": "2010-08-27T01:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96310",
    "user": "@rbeezer"
}
```

First patch contained:


```
columns = parent.nrows()
```


which is just plain wrong, but also `columns` was never referenced (which is why the doctests were unaffected).  Its gone now.  Use just the v2 patch.



---

archive/issue_comments_096311.json:
```json
{
    "body": "Does this patch depend on any other patches?",
    "created_at": "2010-08-27T17:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96311",
    "user": "@wdjoyner"
}
```

Does this patch depend on any other patches?



---

archive/issue_comments_096312.json:
```json
{
    "body": "Replying to [comment:3 wdj]:\n> Does this patch depend on any other patches?\n\nAh, yes, totally forgot.  It needs to have #9720 (just the v4 patch) applied first.  Thanks.",
    "created_at": "2010-08-27T17:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96312",
    "user": "@rbeezer"
}
```

Replying to [comment:3 wdj]:
> Does this patch depend on any other patches?

Ah, yes, totally forgot.  It needs to have #9720 (just the v4 patch) applied first.  Thanks.



---

archive/issue_comments_096313.json:
```json
{
    "body": "Applied (with #9720) to 4.5.1 and passed sage -testall. Positive review as far as I see, but maybe Mike Hansen should weight in.",
    "created_at": "2010-08-28T19:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96313",
    "user": "@wdjoyner"
}
```

Applied (with #9720) to 4.5.1 and passed sage -testall. Positive review as far as I see, but maybe Mike Hansen should weight in.



---

archive/issue_comments_096314.json:
```json
{
    "body": "This looks good to me.",
    "created_at": "2010-08-30T03:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96314",
    "user": "@mwhansen"
}
```

This looks good to me.



---

archive/issue_comments_096315.json:
```json
{
    "body": "Replying to [comment:6 mhansen]:\n> This looks good to me.\n\nThanks for your input.  I think this is much improved organized this way, and I finally did something about the documentation for the `random_matrix()` command.  ;-)\n\nLooks like this can go to positive review along with the rest of Billy's work.",
    "created_at": "2010-08-30T03:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96315",
    "user": "@rbeezer"
}
```

Replying to [comment:6 mhansen]:
> This looks good to me.

Thanks for your input.  I think this is much improved organized this way, and I finally did something about the documentation for the `random_matrix()` command.  ;-)

Looks like this can go to positive review along with the rest of Billy's work.



---

archive/issue_comments_096316.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-30T03:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96316",
    "user": "@rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096317.json:
```json
{
    "body": "## Release Manager\n\n#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this\norder.",
    "created_at": "2010-09-03T06:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96317",
    "user": "bwonderly"
}
```

## Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this
order.



---

archive/issue_comments_096318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9802#issuecomment-96318",
    "user": "@qed777"
}
```

Resolution: fixed
