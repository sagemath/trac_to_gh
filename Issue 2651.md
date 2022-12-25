# Issue 2651: rewrite matrix() constructor

archive/issues_002651.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently the code in matrix() is pretty convoluted.  This patch is an attempt to make that code much more organized and make it easier to tackle adding features to matrix() and fixing bugs.\n\nAdditionally, this patch has quite a few more doctests testing corner casesof matrix().\n\nI am going to run testall on this to make sure that it doesn't mess anything major up.  Right now it should pretty much be a drop-in replacement, except that some corner cases are handled more consistently.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2651\n\n",
    "created_at": "2008-03-22T22:58:36Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "rewrite matrix() constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2651",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Currently the code in matrix() is pretty convoluted.  This patch is an attempt to make that code much more organized and make it easier to tackle adding features to matrix() and fixing bugs.

Additionally, this patch has quite a few more doctests testing corner casesof matrix().

I am going to run testall on this to make sure that it doesn't mess anything major up.  Right now it should pretty much be a drop-in replacement, except that some corner cases are handled more consistently.



Issue created by migration from https://trac.sagemath.org/ticket/2651





---

archive/issue_comments_018175.json:
```json
{
    "body": "Attachment [sr_matrix.patch](tarball://root/attachments/some-uuid/ticket2651/sr_matrix.patch) by @malb created at 2008-03-25 19:48:39",
    "created_at": "2008-03-25T19:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18175",
    "user": "https://github.com/malb"
}
```

Attachment [sr_matrix.patch](tarball://root/attachments/some-uuid/ticket2651/sr_matrix.patch) by @malb created at 2008-03-25 19:48:39



---

archive/issue_comments_018176.json:
```json
{
    "body": "On [sage-devel] Jason wrote:\n> More specifically, for sr.py, matrix() is called from lines 1775 and\n> 1779 with a list of lists.  The code appears to flatten \"l\" into a flat\n> list, but the flatten command on the preceding lines specifies to only\n> flatten Vector_modn_dense things, so the list \"l\" is not flattened.\n\nThe attached patch `sr_matrix.patch` should fix that issue.",
    "created_at": "2008-03-25T19:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18176",
    "user": "https://github.com/malb"
}
```

On [sage-devel] Jason wrote:
> More specifically, for sr.py, matrix() is called from lines 1775 and
> 1779 with a list of lists.  The code appears to flatten "l" into a flat
> list, but the flatten command on the preceding lines specifies to only
> flatten Vector_modn_dense things, so the list "l" is not flattened.

The attached patch `sr_matrix.patch` should fix that issue.



---

archive/issue_comments_018177.json:
```json
{
    "body": "apply instead of previous matrix-refactor.patch patches",
    "created_at": "2008-03-25T21:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18177",
    "user": "https://github.com/jasongrout"
}
```

apply instead of previous matrix-refactor.patch patches



---

archive/issue_comments_018178.json:
```json
{
    "body": "Attachment [matrix-refactor.3.patch](tarball://root/attachments/some-uuid/ticket2651/matrix-refactor.3.patch) by @jasongrout created at 2008-03-25 21:22:43\n\nmatrix-refactor.3.patch is ready to be reviewed.  sr_matrix.patch should be also applied to fix lots of doctests since the new matrix() is a bit stricter on syntax.\n\nThere is an issue remaining with transform.pyx (line 44) calling matrix(3,1,elts), where elts is a list containing a RDF vector of 3 elements instead of elts being a list of 3 RDF numbers.  I'm opening another ticket for this bug.",
    "created_at": "2008-03-25T21:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18178",
    "user": "https://github.com/jasongrout"
}
```

Attachment [matrix-refactor.3.patch](tarball://root/attachments/some-uuid/ticket2651/matrix-refactor.3.patch) by @jasongrout created at 2008-03-25 21:22:43

matrix-refactor.3.patch is ready to be reviewed.  sr_matrix.patch should be also applied to fix lots of doctests since the new matrix() is a bit stricter on syntax.

There is an issue remaining with transform.pyx (line 44) calling matrix(3,1,elts), where elts is a list containing a RDF vector of 3 elements instead of elts being a list of 3 RDF numbers.  I'm opening another ticket for this bug.



---

archive/issue_comments_018179.json:
```json
{
    "body": "The transform.pyx bug is now #2667.",
    "created_at": "2008-03-25T21:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18179",
    "user": "https://github.com/jasongrout"
}
```

The transform.pyx bug is now #2667.



---

archive/issue_comments_018180.json:
```json
{
    "body": "One question I have for the patch: Should I be passing back ValueError when I do?  Or should it be TypeError or some other error?",
    "created_at": "2008-03-25T21:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18180",
    "user": "https://github.com/jasongrout"
}
```

One question I have for the patch: Should I be passing back ValueError when I do?  Or should it be TypeError or some other error?



---

archive/issue_comments_018181.json:
```json
{
    "body": "This is a good change!\n\nI'm no Python expert, but I like your choice of ValueError over TypeError.  I think the paragraph \"The entries\" in the INPUT: section could be revised a little to improve clarity.\n\nIn your example\n\n```\nsage: m=matrix(QQ,3,{(1,1): 2}); m; m.parent() \n[0 0]\n[0 2]\n[0 0]\n...\n```\n\nI expected to see a 3x3 matrix.  Your other examples that have only one size input produce square matrices (particularly the empty-dict input argument!).  I'm not sure what the \"right\" behavior is, but I wanted to make sure you are.\n\nI don't see any examples/tests of passing in a Sage object and using the _matrix_() attribute to get a matrix.",
    "created_at": "2008-03-26T17:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18181",
    "user": "https://github.com/rhinton"
}
```

This is a good change!

I'm no Python expert, but I like your choice of ValueError over TypeError.  I think the paragraph "The entries" in the INPUT: section could be revised a little to improve clarity.

In your example

```
sage: m=matrix(QQ,3,{(1,1): 2}); m; m.parent() 
[0 0]
[0 2]
[0 0]
...
```

I expected to see a 3x3 matrix.  Your other examples that have only one size input produce square matrices (particularly the empty-dict input argument!).  I'm not sure what the "right" behavior is, but I wanted to make sure you are.

I don't see any examples/tests of passing in a Sage object and using the _matrix_() attribute to get a matrix.



---

archive/issue_comments_018182.json:
```json
{
    "body": "* the matrix(3,{(1,1): 2}) example is posted to sage-devel for a vote.\n  * v=vector; matrix(v) is an example of passing a sage object.  We probably ought to have another one, maybe a graph?  Do you want to post a quick patch?\n\nsage: g=graphs.CycleGraph(4)\nsage: matrix(g)\n\nor something like that, maybe?",
    "created_at": "2008-03-26T18:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18182",
    "user": "https://github.com/jasongrout"
}
```

* the matrix(3,{(1,1): 2}) example is posted to sage-devel for a vote.
  * v=vector; matrix(v) is an example of passing a sage object.  We probably ought to have another one, maybe a graph?  Do you want to post a quick patch?

sage: g=graphs.CycleGraph(4)
sage: matrix(g)

or something like that, maybe?



---

archive/issue_comments_018183.json:
```json
{
    "body": "Attachment [matrix-refactor-extra.patch](tarball://root/attachments/some-uuid/ticket2651/matrix-refactor-extra.patch) by @rhinton created at 2008-03-29 00:31:11\n\nApply on top of latest matrix-refactor.patch.  Contains doc rewording, extra doctest matrix(graph), redefines matrix(int,dict) according to sage-devel vote.",
    "created_at": "2008-03-29T00:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18183",
    "user": "https://github.com/rhinton"
}
```

Attachment [matrix-refactor-extra.patch](tarball://root/attachments/some-uuid/ticket2651/matrix-refactor-extra.patch) by @rhinton created at 2008-03-29 00:31:11

Apply on top of latest matrix-refactor.patch.  Contains doc rewording, extra doctest matrix(graph), redefines matrix(int,dict) according to sage-devel vote.



---

archive/issue_comments_018184.json:
```json
{
    "body": "Note:\n\nPart of the end patches for this ticket should revert the second patch on #2597, since it is a quick fix.",
    "created_at": "2008-03-29T01:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18184",
    "user": "https://github.com/rlmill"
}
```

Note:

Part of the end patches for this ticket should revert the second patch on #2597, since it is a quick fix.



---

archive/issue_comments_018185.json:
```json
{
    "body": "Apply on top of other patches.  Fixes doctests that fail due to semantic change in call to matrix(int, dict).  (Semantic change voted +2, -0 on sage-devel.)",
    "created_at": "2008-03-29T05:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18185",
    "user": "https://github.com/rhinton"
}
```

Apply on top of other patches.  Fixes doctests that fail due to semantic change in call to matrix(int, dict).  (Semantic change voted +2, -0 on sage-devel.)



---

archive/issue_comments_018186.json:
```json
{
    "body": "Attachment [matrix-refactor-fix-other-tests.patch](tarball://root/attachments/some-uuid/ticket2651/matrix-refactor-fix-other-tests.patch) by @rhinton created at 2008-03-29 05:07:27\n\nAlong with the patch for #2667, a \"sage -t -long devel/sage/sage\" passes with no failures for me.  I think this patch is ready as soon as someone can review my changes.",
    "created_at": "2008-03-29T05:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18186",
    "user": "https://github.com/rhinton"
}
```

Attachment [matrix-refactor-fix-other-tests.patch](tarball://root/attachments/some-uuid/ticket2651/matrix-refactor-fix-other-tests.patch) by @rhinton created at 2008-03-29 05:07:27

Along with the patch for #2667, a "sage -t -long devel/sage/sage" passes with no failures for me.  I think this patch is ready as soon as someone can review my changes.



---

archive/issue_comments_018187.json:
```json
{
    "body": "The patches above all apply cleanly and all doctests (-long) pass if the patch at #2667 is applied as well.  I positively review the additional patches (and mine too :).  Since rhinton positively reviewed the core patch, I'm going to change the title to positive review.",
    "created_at": "2008-03-29T22:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18187",
    "user": "https://github.com/jasongrout"
}
```

The patches above all apply cleanly and all doctests (-long) pass if the patch at #2667 is applied as well.  I positively review the additional patches (and mine too :).  Since rhinton positively reviewed the core patch, I'm going to change the title to positive review.



---

archive/issue_comments_018188.json:
```json
{
    "body": "Attachment [trac_2651_vector_comment.patch](tarball://root/attachments/some-uuid/ticket2651/trac_2651_vector_comment.patch) by @jasongrout created at 2008-03-31 14:17:50\n\nChanges a comment to reflect current documentation.",
    "created_at": "2008-03-31T14:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18188",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_2651_vector_comment.patch](tarball://root/attachments/some-uuid/ticket2651/trac_2651_vector_comment.patch) by @jasongrout created at 2008-03-31 14:17:50

Changes a comment to reflect current documentation.



---

archive/issue_comments_018189.json:
```json
{
    "body": "To clarify, apply all the patches above in order and also apply the patch at #2667.",
    "created_at": "2008-03-31T14:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18189",
    "user": "https://github.com/jasongrout"
}
```

To clarify, apply all the patches above in order and also apply the patch at #2667.



---

archive/issue_comments_018190.json:
```json
{
    "body": "Patch looks good and passes doctests in sage 2.11. This rewrite was much needed!",
    "created_at": "2008-03-31T19:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18190",
    "user": "https://github.com/dfdeshom"
}
```

Patch looks good and passes doctests in sage 2.11. This rewrite was much needed!



---

archive/issue_comments_018191.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-31T19:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018192.json:
```json
{
    "body": "Merged all five patches in Sage 3.0.alpha0",
    "created_at": "2008-03-31T19:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2651#issuecomment-18192",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all five patches in Sage 3.0.alpha0



---

archive/issue_events_002842.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-31T19:15:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2651",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2651#event-2842"
}
```
