# Issue 5256: [with patch, needs review] coherent handling of trivial matrices (depend on #5244, #5242).

archive/issues_005256.json:
```json
{
    "body": "Assignee: was\n\nCC:  sage-combinat\n\nKeywords: matrices, invert, determinant\n\nThere where a lot of inconsistency and bugs in the handling of trivial matrices.\nThe following patch aims to solve these and to check systematicly the coherence. Here is a selection of weirdness:\n* plain wrong answers\n\n```\nsage: m = matrix(SR, 1,1, [1])\nsage: m.inverse()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\nsage: m = matrix(RDF, 0,2)\nsage: m.inverse()\n[]\n```\n\n* Inconsistencies in the answers depending on the base ring\n\n```\nsage: m = matrix(RDF, 1,1)\nsage: m.inverse()\n---------------------------------------------------------------------------\nLinAlgError                               Traceback (most recent call last)\n```\n\n   whereas\n\n```\nsage: m = matrix(QQ, 1,1)\nsage: m.inverse()\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n```\n\n\nAside rewriting some error messages, changing some exception and working around several bug in particular in maxima's handling of matrix over SR, the main contribution of this patch lies in the function `test_trivial_matrices_inverse` in `sage/matrix/matrix_space.py` and its associated doctests. Trough a bunch of assertions this function indirectly checks the behavior of matrix spaces. Any new implementation of a kind of matrices should be checked be this function. \n\nPatch Author: Florent Hivert\n\nIssue created by migration from https://trac.sagemath.org/ticket/5256\n\n",
    "created_at": "2009-02-13T18:47:24Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] coherent handling of trivial matrices (depend on #5244, #5242).",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5256",
    "user": "hivert"
}
```
Assignee: was

CC:  sage-combinat

Keywords: matrices, invert, determinant

There where a lot of inconsistency and bugs in the handling of trivial matrices.
The following patch aims to solve these and to check systematicly the coherence. Here is a selection of weirdness:
* plain wrong answers

```
sage: m = matrix(SR, 1,1, [1])
sage: m.inverse()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

sage: m = matrix(RDF, 0,2)
sage: m.inverse()
[]
```

* Inconsistencies in the answers depending on the base ring

```
sage: m = matrix(RDF, 1,1)
sage: m.inverse()
---------------------------------------------------------------------------
LinAlgError                               Traceback (most recent call last)
```

   whereas

```
sage: m = matrix(QQ, 1,1)
sage: m.inverse()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
```


Aside rewriting some error messages, changing some exception and working around several bug in particular in maxima's handling of matrix over SR, the main contribution of this patch lies in the function `test_trivial_matrices_inverse` in `sage/matrix/matrix_space.py` and its associated doctests. Trough a bunch of assertions this function indirectly checks the behavior of matrix spaces. Any new implementation of a kind of matrices should be checked be this function. 

Patch Author: Florent Hivert

Issue created by migration from https://trac.sagemath.org/ticket/5256





---

archive/issue_comments_040332.json:
```json
{
    "body": "Changing assignee from was to hivert.",
    "created_at": "2009-02-13T18:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40332",
    "user": "hivert"
}
```

Changing assignee from was to hivert.



---

archive/issue_comments_040333.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T18:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40333",
    "user": "hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040334.json:
```json
{
    "body": "I'm really happy you did all this.  I'll look at this soon, unless someone else gets to it before me.\n\nIt'd be great to have a system-wide function that tested different Sage types for consistency on things like this.  That way, all someone would have to remember to do is add their new sage type to a doctest like:\n\n\n```\nsage: check_consistency(MY_NEW_TYPE)\nTrue\n```\n\n\nThat function would automatically call things like the function in this patch and other functions for vectors, polynomials, etc.",
    "created_at": "2009-02-13T19:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40334",
    "user": "jason"
}
```

I'm really happy you did all this.  I'll look at this soon, unless someone else gets to it before me.

It'd be great to have a system-wide function that tested different Sage types for consistency on things like this.  That way, all someone would have to remember to do is add their new sage type to a doctest like:


```
sage: check_consistency(MY_NEW_TYPE)
True
```


That function would automatically call things like the function in this patch and other functions for vectors, polynomials, etc.



---

archive/issue_comments_040335.json:
```json
{
    "body": "In his category framework, Nicolas Thiery wrote a very handy feature that allows one to add some plug in function to test properties on a parent object. For example in the category of groups there are among other the following methods (some are inherited from higher categories): \n- test_some_elements\n- test_associativity\n- test_unity\n- test_inverse\nThen once you have a group G you can ask for G.check() which lauch automatically all those tests. Unfortunately this is buried in the category framework and cannot be used right now. (see [sage-devel] Generic tests and categories 6 Feb 2009). In the mean time I do this by hands.",
    "created_at": "2009-02-13T20:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40335",
    "user": "hivert"
}
```

In his category framework, Nicolas Thiery wrote a very handy feature that allows one to add some plug in function to test properties on a parent object. For example in the category of groups there are among other the following methods (some are inherited from higher categories): 
- test_some_elements
- test_associativity
- test_unity
- test_inverse
Then once you have a group G you can ask for G.check() which lauch automatically all those tests. Unfortunately this is buried in the category framework and cannot be used right now. (see [sage-devel] Generic tests and categories 6 Feb 2009). In the mean time I do this by hands.



---

archive/issue_comments_040336.json:
```json
{
    "body": "New version with a corrected typo (thanks Jason)",
    "created_at": "2009-02-13T20:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40336",
    "user": "hivert"
}
```

New version with a corrected typo (thanks Jason)



---

archive/issue_comments_040337.json:
```json
{
    "body": "Attachment [empty_matrix_inverse-fh.patch](tarball://root/attachments/some-uuid/ticket5256/empty_matrix_inverse-fh.patch) by malb created at 2009-02-14 16:34:10\n\n**Review**\npatch looks good except\n* typo: \"seld\" -> \"self\" (2402)\n* docstring INPUT block of `test_trivial_matrices_inverse` does not conform to Sage's conventions\n* \"TODO: must be adapted to Nicolas check framework (see trac FIXME).\" The FIXME should probably be addressed\n\ni.e. all issues are trivial.\n\nI didn't run doctests yet, will do now.",
    "created_at": "2009-02-14T16:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40337",
    "user": "malb"
}
```

Attachment [empty_matrix_inverse-fh.patch](tarball://root/attachments/some-uuid/ticket5256/empty_matrix_inverse-fh.patch) by malb created at 2009-02-14 16:34:10

**Review**
patch looks good except
* typo: "seld" -> "self" (2402)
* docstring INPUT block of `test_trivial_matrices_inverse` does not conform to Sage's conventions
* "TODO: must be adapted to Nicolas check framework (see trac FIXME)." The FIXME should probably be addressed

i.e. all issues are trivial.

I didn't run doctests yet, will do now.



---

archive/issue_comments_040338.json:
```json
{
    "body": "I have doctested this patch on top of #5242 and #5244 in my current Sage 3.3.rc1 merge tree and:\n\n```\nAll tests passed!\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T16:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40338",
    "user": "mabshoff"
}
```

I have doctested this patch on top of #5242 and #5244 in my current Sage 3.3.rc1 merge tree and:

```
All tests passed!
```


Cheers,

Michael



---

archive/issue_comments_040339.json:
```json
{
    "body": "Replying to [comment:4 malb]:\nDone ! See the new patch. \n\nNote that I currently didn't had time to check it. It's currently being done on my machine but it takes times. I only change docs from the first version but who knows...",
    "created_at": "2009-02-14T17:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40339",
    "user": "hivert"
}
```

Replying to [comment:4 malb]:
Done ! See the new patch. 

Note that I currently didn't had time to check it. It's currently being done on my machine but it takes times. I only change docs from the first version but who knows...



---

archive/issue_comments_040340.json:
```json
{
    "body": "Reupped after malb request on irc.",
    "created_at": "2009-02-14T19:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40340",
    "user": "hivert"
}
```

Reupped after malb request on irc.



---

archive/issue_comments_040341.json:
```json
{
    "body": "Attachment [trivial_matrices_inverse-5256-submitted.patch](tarball://root/attachments/some-uuid/ticket5256/trivial_matrices_inverse-5256-submitted.patch) by mhansen created at 2009-02-14 23:37:21\n\nPositive review on trivial_matrices_inverse-5256-submitted.patch.",
    "created_at": "2009-02-14T23:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40341",
    "user": "mhansen"
}
```

Attachment [trivial_matrices_inverse-5256-submitted.patch](tarball://root/attachments/some-uuid/ticket5256/trivial_matrices_inverse-5256-submitted.patch) by mhansen created at 2009-02-14 23:37:21

Positive review on trivial_matrices_inverse-5256-submitted.patch.



---

archive/issue_comments_040342.json:
```json
{
    "body": "Note that there is #5274 for the TODO/FIXME.",
    "created_at": "2009-02-14T23:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40342",
    "user": "mhansen"
}
```

Note that there is #5274 for the TODO/FIXME.



---

archive/issue_comments_040343.json:
```json
{
    "body": "Merged trivial_matrices_inverse-5256-submitted.patch in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40343",
    "user": "mabshoff"
}
```

Merged trivial_matrices_inverse-5256-submitted.patch in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040344.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-15T07:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5256#issuecomment-40344",
    "user": "mabshoff"
}
```

Resolution: fixed
