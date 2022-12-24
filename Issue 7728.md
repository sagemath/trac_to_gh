# Issue 7728: Make matrix factorizations immutable and cached

archive/issues_007728.json:
```json
{
    "body": "Assignee: was\n\nThe attached patch (based on 4.3.rc0):\n\n- changes Cholesky (all/most matrices) and SVD, QR and LU factorizations (double_dense only) so that the returned resulting matrices are immutable\n- adds caching for Cholesky, SVD and QR\n- adds pickle-able caching for LU (and it is likely there was a a bug with pickling/unpickling a matrix with a cached factorization which this patch fixes...)\n- improves doctests for SVD and QR (I wanted to more easily check that my changes didn't cause regressions...)\n- adds methods `zero_at` and `round` to dense double matrices (used in said doctests)\n\nI hope the doctest improvements can be accepted as part of the patch even if I didn't bother to split it up.\n\nNote that when dealing with matrix factorization doctesting, just avoiding 0 in the input goes very far with creating readable tests.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7728\n\n",
    "created_at": "2009-12-17T21:22:36Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "Make matrix factorizations immutable and cached",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7728",
    "user": "dagss"
}
```
Assignee: was

The attached patch (based on 4.3.rc0):

- changes Cholesky (all/most matrices) and SVD, QR and LU factorizations (double_dense only) so that the returned resulting matrices are immutable
- adds caching for Cholesky, SVD and QR
- adds pickle-able caching for LU (and it is likely there was a a bug with pickling/unpickling a matrix with a cached factorization which this patch fixes...)
- improves doctests for SVD and QR (I wanted to more easily check that my changes didn't cause regressions...)
- adds methods `zero_at` and `round` to dense double matrices (used in said doctests)

I hope the doctest improvements can be accepted as part of the patch even if I didn't bother to split it up.

Note that when dealing with matrix factorization doctesting, just avoiding 0 in the input goes very far with creating readable tests.


Issue created by migration from https://trac.sagemath.org/ticket/7728





---

archive/issue_comments_066395.json:
```json
{
    "body": "Attachment [trac_7728-immutablefactors.patch](tarball://root/attachments/some-uuid/ticket7728/trac_7728-immutablefactors.patch) by dagss created at 2009-12-17 21:25:05",
    "created_at": "2009-12-17T21:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66395",
    "user": "dagss"
}
```

Attachment [trac_7728-immutablefactors.patch](tarball://root/attachments/some-uuid/ticket7728/trac_7728-immutablefactors.patch) by dagss created at 2009-12-17 21:25:05



---

archive/issue_comments_066396.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-17T21:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66396",
    "user": "dagss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066397.json:
```json
{
    "body": "OK, this likely need some more docs about the caching aspect...",
    "created_at": "2009-12-19T22:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66397",
    "user": "dagss"
}
```

OK, this likely need some more docs about the caching aspect...



---

archive/issue_comments_066398.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-19T22:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66398",
    "user": "dagss"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066399.json:
```json
{
    "body": "Attachment [trac_7728-immutablefactors.2.patch](tarball://root/attachments/some-uuid/ticket7728/trac_7728-immutablefactors.2.patch) by dagss created at 2009-12-21 15:12:06\n\nLast attachment contains the same changes + a little more docs.\n\nLU was previously cached, so this just makes things more consistent by caching all decompositions -- easier to remember.\n\nI also plan to make use of the caching if I get around to fixing #4932, see my comment there, short story: `solve_left` should be able to use the results of a call to `LU()`, which makes caching a lot more important.",
    "created_at": "2009-12-21T15:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66399",
    "user": "dagss"
}
```

Attachment [trac_7728-immutablefactors.2.patch](tarball://root/attachments/some-uuid/ticket7728/trac_7728-immutablefactors.2.patch) by dagss created at 2009-12-21 15:12:06

Last attachment contains the same changes + a little more docs.

LU was previously cached, so this just makes things more consistent by caching all decompositions -- easier to remember.

I also plan to make use of the caching if I get around to fixing #4932, see my comment there, short story: `solve_left` should be able to use the results of a call to `LU()`, which makes caching a lot more important.



---

archive/issue_comments_066400.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-21T15:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66400",
    "user": "dagss"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066401.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-21T19:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66401",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066402.json:
```json
{
    "body": "Bravo, this is an awesome patch!  Positive review.\n\n\nComment for future work by somebody.  I don't like this:\n\n```\n987\t            U, S, V -- immutable matrices such that $A = U*S*V.conj().transpose()$ \n988\t                       where U and V are orthogonal and S is zero off of the diagonal. \n```\n\n\nIt's not your fault -- it was like that before.  But it is wrong in so many ways wrt to Sphinx (e.g., dollar signs?  V.conj().transpose() in math mode?  variables should be listed separately, etc.",
    "created_at": "2009-12-21T19:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66402",
    "user": "was"
}
```

Bravo, this is an awesome patch!  Positive review.


Comment for future work by somebody.  I don't like this:

```
987	            U, S, V -- immutable matrices such that $A = U*S*V.conj().transpose()$ 
988	                       where U and V are orthogonal and S is zero off of the diagonal. 
```


It's not your fault -- it was like that before.  But it is wrong in so many ways wrt to Sphinx (e.g., dollar signs?  V.conj().transpose() in math mode?  variables should be listed separately, etc.



---

archive/issue_comments_066403.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> It's not your fault -- it was like that before.  But it is wrong in so many ways wrt to Sphinx (e.g., dollar signs?  V.conj().transpose() in math mode?  variables should be listed separately, etc.\n\nJust a small comment: I believe that we can now use dollar signs for math input in Sphinx, so that shouldn't be a problem.",
    "created_at": "2009-12-21T21:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66403",
    "user": "AlexGhitza"
}
```

Replying to [comment:4 was]:
> It's not your fault -- it was like that before.  But it is wrong in so many ways wrt to Sphinx (e.g., dollar signs?  V.conj().transpose() in math mode?  variables should be listed separately, etc.

Just a small comment: I believe that we can now use dollar signs for math input in Sphinx, so that shouldn't be a problem.



---

archive/issue_comments_066404.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7728#issuecomment-66404",
    "user": "mhansen"
}
```

Resolution: fixed
