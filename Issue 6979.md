# Issue 6979: improve sparse matrix/vector product

archive/issues_006979.json:
```json
{
    "body": "Assignee: was\n\nwe add ad hoc methods in matrix_sparse.pyx\n\nIssue created by migration from https://trac.sagemath.org/ticket/6979\n\n",
    "created_at": "2009-09-21T19:01:46Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "improve sparse matrix/vector product",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6979",
    "user": "ylchapuy"
}
```
Assignee: was

we add ad hoc methods in matrix_sparse.pyx

Issue created by migration from https://trac.sagemath.org/ticket/6979





---

archive/issue_comments_057714.json:
```json
{
    "body": "for the record:\n\n```\nsage: m=random_matrix(ZZ,1000,sparse=True,density=0.01)sage: m=random_matrix(GF(17),1000,sparse=True,density=0.01)\nsage: v=vector([randrange(100) for i in xrange(1000)])\n```\n\nbefore:\n\n```\nsage: timeit('m*v')\n5 loops, best of 3: 257 ms per loop\n```\n\nafter:\n\n```\ntimeit('m*v')\n5 loops, best of 3: 61 ms per loop\n```\n",
    "created_at": "2009-09-21T19:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57714",
    "user": "ylchapuy"
}
```

for the record:

```
sage: m=random_matrix(ZZ,1000,sparse=True,density=0.01)sage: m=random_matrix(GF(17),1000,sparse=True,density=0.01)
sage: v=vector([randrange(100) for i in xrange(1000)])
```

before:

```
sage: timeit('m*v')
5 loops, best of 3: 257 ms per loop
```

after:

```
timeit('m*v')
5 loops, best of 3: 61 ms per loop
```




---

archive/issue_comments_057715.json:
```json
{
    "body": "I added some doctests in a reviewer patch that ensure that the current return type behavior doesn't change without breaking something (i.e., notifying us that it changed).",
    "created_at": "2009-09-22T15:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57715",
    "user": "jason"
}
```

I added some doctests in a reviewer patch that ensure that the current return type behavior doesn't change without breaking something (i.e., notifying us that it changed).



---

archive/issue_comments_057716.json:
```json
{
    "body": "I got this doctest failure:\n\n```\nsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1423:\n    sage: M*G\nExpected:\n    (0, 0)\nGot:\n    (0, 0, 0)\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_30\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_multi_polynomial_ideal.py\n\t [15.4 s]\n```\n",
    "created_at": "2009-09-25T03:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57716",
    "user": "mvngu"
}
```

I got this doctest failure:

```
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py", line 1423:
    sage: M*G
Expected:
    (0, 0)
Got:
    (0, 0, 0)
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_30
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_multi_polynomial_ideal.py
	 [15.4 s]
```




---

archive/issue_comments_057717.json:
```json
{
    "body": "The code for both v*M and M*v has the result of type:\n\n        s = v.parent()(0) \n\nHowever, the dimension here is clearly wrong---we don't get a result the size of the vector, but the number of rows of M if computing M*v, and the number of columns of M if computing v*M.",
    "created_at": "2009-09-29T06:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57717",
    "user": "jason"
}
```

The code for both v*M and M*v has the result of type:

        s = v.parent()(0) 

However, the dimension here is clearly wrong---we don't get a result the size of the vector, but the number of rows of M if computing M*v, and the number of columns of M if computing v*M.



---

archive/issue_comments_057718.json:
```json
{
    "body": "oups, this was of course silly...\nHere is an updated patch replacing only mine.\nBoth patches need to be applied.",
    "created_at": "2009-09-29T10:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57718",
    "user": "ylchapuy"
}
```

oups, this was of course silly...
Here is an updated patch replacing only mine.
Both patches need to be applied.



---

archive/issue_comments_057719.json:
```json
{
    "body": "Thanks!\n\nI still think there is a problem.  For dense things, v*M gets its base ring from M, not v.  However, the above patch gets the base ring from v.  That's what my doctest patch tests.",
    "created_at": "2009-09-29T14:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57719",
    "user": "jason"
}
```

Thanks!

I still think there is a problem.  For dense things, v*M gets its base ring from M, not v.  However, the above patch gets the base ring from v.  That's what my doctest patch tests.



---

archive/issue_comments_057720.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-10T16:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57720",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057721.json:
```json
{
    "body": "The doctest\n\n\n```\nsage:  (m*v).parent() is m.row(0).parent()\n```\n\n\nlooks backwards to me (columns <-> rows).  A matrix-vector product should be a linear combination of the columns of the matrix, no?  I think the only reason it passes is that the matrix employed is square.  If I make the matrix rectangular, it fails.  If correct, the companion in the other method also needs fixing.\n\nThe original doctest patch has contributions to to `sage/matrix/matrix0.pyx` and `sage/matrix/matrix_sparse.pyx`, but the sparse tests are in the latest patch, but the \"0\" tests are not.\n\nWith some guidance, I'd look at this again for a review.",
    "created_at": "2010-04-06T04:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57721",
    "user": "rbeezer"
}
```

The doctest


```
sage:  (m*v).parent() is m.row(0).parent()
```


looks backwards to me (columns <-> rows).  A matrix-vector product should be a linear combination of the columns of the matrix, no?  I think the only reason it passes is that the matrix employed is square.  If I make the matrix rectangular, it fails.  If correct, the companion in the other method also needs fixing.

The original doctest patch has contributions to to `sage/matrix/matrix0.pyx` and `sage/matrix/matrix_sparse.pyx`, but the sparse tests are in the latest patch, but the "0" tests are not.

With some guidance, I'd look at this again for a review.



---

archive/issue_comments_057722.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-06T04:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57722",
    "user": "rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057723.json:
```json
{
    "body": "Attachment [trac_6979_sparse_matrix_vector_product.patch](tarball://root/attachments/some-uuid/ticket6979/trac_6979_sparse_matrix_vector_product.patch) by ylchapuy created at 2010-09-26 20:28:45\n\nbased on 4.5.3",
    "created_at": "2010-09-26T20:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57723",
    "user": "ylchapuy"
}
```

Attachment [trac_6979_sparse_matrix_vector_product.patch](tarball://root/attachments/some-uuid/ticket6979/trac_6979_sparse_matrix_vector_product.patch) by ylchapuy created at 2010-09-26 20:28:45

based on 4.5.3



---

archive/issue_comments_057724.json:
```json
{
    "body": "The matrices in the doctest are now rectangular, and the tests corrected accordingly.\n\nBoth `matrix0.pyx` and `matrix_sparse.pyx` are modified.\n\nReady for review (at last).",
    "created_at": "2010-09-26T20:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57724",
    "user": "ylchapuy"
}
```

The matrices in the doctest are now rectangular, and the tests corrected accordingly.

Both `matrix0.pyx` and `matrix_sparse.pyx` are modified.

Ready for review (at last).



---

archive/issue_comments_057725.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-26T20:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57725",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057726.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T20:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57726",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057727.json:
```json
{
    "body": "Looks good!  I deleted my patch, since you now have those doctests.\n\nPositive review.",
    "created_at": "2010-09-28T20:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57727",
    "user": "jason"
}
```

Looks good!  I deleted my patch, since you now have those doctests.

Positive review.



---

archive/issue_comments_057728.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6979#issuecomment-57728",
    "user": "mpatel"
}
```

Resolution: fixed
