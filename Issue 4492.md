# Issue 4492: block_matrix reacts inconsistently with 0

archive/issues_004492.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  craigcitro jason davidloeffler\n\nUsing ZZ(0) as an element of the list passed to block_matrix appears to be a special case somehow and throws an exception rather than creating the matrix seems reasonable to me.\n\n\n```\nsage: i=MatrixSpace(ZZ,2,2)(1)\nsage: i\n\n[1 0]\n[0 1]\nsage: block_matrix([1,i,1,1])  # this works as I expect\n\n[1 0|1 0]\n[0 1|0 1]\n[---+---]\n[1 0|1 0]\n[0 1|0 1]\nsage: block_matrix([0,i,1,1])  # this doesn't ... why is 0 special\n...\nValueError: Insufficient information to determine dimensions.\n```\n\nThis feels to me like a hazardous inconsistency.\n\nPerhaps I should also add that I don't really like that it just blithely assumes I want a square matrix (although I did in my actual usage).  Ticket #2429 addresses that issue more wholeheartedly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4492\n\n",
    "created_at": "2008-11-11T15:17:25Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "block_matrix reacts inconsistently with 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4492",
    "user": "jbmohler"
}
```
Assignee: tbd

CC:  craigcitro jason davidloeffler

Using ZZ(0) as an element of the list passed to block_matrix appears to be a special case somehow and throws an exception rather than creating the matrix seems reasonable to me.


```
sage: i=MatrixSpace(ZZ,2,2)(1)
sage: i

[1 0]
[0 1]
sage: block_matrix([1,i,1,1])  # this works as I expect

[1 0|1 0]
[0 1|0 1]
[---+---]
[1 0|1 0]
[0 1|0 1]
sage: block_matrix([0,i,1,1])  # this doesn't ... why is 0 special
...
ValueError: Insufficient information to determine dimensions.
```

This feels to me like a hazardous inconsistency.

Perhaps I should also add that I don't really like that it just blithely assumes I want a square matrix (although I did in my actual usage).  Ticket #2429 addresses that issue more wholeheartedly.

Issue created by migration from https://trac.sagemath.org/ticket/4492





---

archive/issue_comments_033179.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2008-11-14T06:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33179",
    "user": "jason"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_033180.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2008-11-14T06:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33180",
    "user": "jason"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_033181.json:
```json
{
    "body": "So I figured out what is going wrong here. Patch to come shortly.",
    "created_at": "2010-01-18T05:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33181",
    "user": "sdietzel"
}
```

So I figured out what is going wrong here. Patch to come shortly.



---

archive/issue_comments_033182.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T19:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33182",
    "user": "sdietzel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_033183.json:
```json
{
    "body": "I think that in the doctest you give there actually is insufficient information, because you can't deduce the width of the left blocks, so an exception is in my opinion the right thing to do there.\n\nIn the example in this ticket, it seems to break because it tries to deduce the block dimensions in a single pass through the cells. In this pass, it only determines the size of column 2 and rows 1 and 2. It might need multiple passes to find all information.",
    "created_at": "2010-01-19T04:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33183",
    "user": "wjp"
}
```

I think that in the doctest you give there actually is insufficient information, because you can't deduce the width of the left blocks, so an exception is in my opinion the right thing to do there.

In the example in this ticket, it seems to break because it tries to deduce the block dimensions in a single pass through the cells. In this pass, it only determines the size of column 2 and rows 1 and 2. It might need multiple passes to find all information.



---

archive/issue_comments_033184.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-19T04:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33184",
    "user": "wjp"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033185.json:
```json
{
    "body": "Attachment [4492_doctest_nonsquare0_block.patch](tarball://root/attachments/some-uuid/ticket4492/4492_doctest_nonsquare0_block.patch) by wjp created at 2010-01-19 18:19:40\n\nRobert Bradshaw suggested adding an example that explicitly shows zero blocks may be non-square. I added a patch that adds that to the docstring of `block_matrix`.",
    "created_at": "2010-01-19T18:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33185",
    "user": "wjp"
}
```

Attachment [4492_doctest_nonsquare0_block.patch](tarball://root/attachments/some-uuid/ticket4492/4492_doctest_nonsquare0_block.patch) by wjp created at 2010-01-19 18:19:40

Robert Bradshaw suggested adding an example that explicitly shows zero blocks may be non-square. I added a patch that adds that to the docstring of `block_matrix`.



---

archive/issue_comments_033186.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T18:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33186",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033187.json:
```json
{
    "body": "Attachment [trac_4492.patch](tarball://root/attachments/some-uuid/ticket4492/trac_4492.patch) by was created at 2010-01-26 18:56:59\n\napply *only* this patch (don't apply wjp's)",
    "created_at": "2010-01-26T18:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33187",
    "user": "was"
}
```

Attachment [trac_4492.patch](tarball://root/attachments/some-uuid/ticket4492/trac_4492.patch) by was created at 2010-01-26 18:56:59

apply *only* this patch (don't apply wjp's)



---

archive/issue_comments_033188.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-26T19:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33188",
    "user": "wjp"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033189.json:
```json
{
    "body": "This breaks the following example:\n\nsage: B = Matrix(ZZ,3,2,[1,2,3,4,5,6])\nsage: block_matrix([0,1,B,1])\n\nThe problem is that it turns the 0 at the top into a 2x2 zero matrix while\nit should be a 3x2 zero matrix, but that can only be deduced after processing the ones further on.",
    "created_at": "2010-01-26T19:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33189",
    "user": "wjp"
}
```

This breaks the following example:

sage: B = Matrix(ZZ,3,2,[1,2,3,4,5,6])
sage: block_matrix([0,1,B,1])

The problem is that it turns the 0 at the top into a 2x2 zero matrix while
it should be a 3x2 zero matrix, but that can only be deduced after processing the ones further on.



---

archive/issue_comments_033190.json:
```json
{
    "body": "Oops, sorry for the broken formatting. Clean version:\n\n\n```\nsage: B = Matrix(ZZ,3,2,[1,2,3,4,5,6])\nsage: block_matrix([0,1,B,1]) \n```\n",
    "created_at": "2010-01-26T19:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33190",
    "user": "wjp"
}
```

Oops, sorry for the broken formatting. Clean version:


```
sage: B = Matrix(ZZ,3,2,[1,2,3,4,5,6])
sage: block_matrix([0,1,B,1]) 
```




---

archive/issue_comments_033191.json:
```json
{
    "body": "I tried to write a patch for this, but ran into some trouble with the last doctest:\n\n\n```\n        sage: B = matrix(QQ, 2, 3, range(6))\n        sage: block_matrix([~A, B, B, ~A], subdivide=False)\n        [-5/12   3/8     0     1     2]\n        [  1/4  -1/8     3     4     5]\n        [    0     1     2 -5/12   3/8]\n        [    3     4     5   1/4  -1/8]\n```\n\n\nIn this case there are no real columns as such, and I'm not sure how we should behave if there were an extra row with `'1 0'` below the `'~A B'` and `'B ~A'` rows. Should that give a 3x3 identity matrix and a 3x2 zero matrix, or a 2x2 identity matrix and a 2x2 identity matrix? Maybe undefined behaviour, or an exception?\n\nMy current attempt raises an exception for this doctest that the column widths are inconsistent.",
    "created_at": "2010-01-29T10:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33191",
    "user": "wjp"
}
```

I tried to write a patch for this, but ran into some trouble with the last doctest:


```
        sage: B = matrix(QQ, 2, 3, range(6))
        sage: block_matrix([~A, B, B, ~A], subdivide=False)
        [-5/12   3/8     0     1     2]
        [  1/4  -1/8     3     4     5]
        [    0     1     2 -5/12   3/8]
        [    3     4     5   1/4  -1/8]
```


In this case there are no real columns as such, and I'm not sure how we should behave if there were an extra row with `'1 0'` below the `'~A B'` and `'B ~A'` rows. Should that give a 3x3 identity matrix and a 3x2 zero matrix, or a 2x2 identity matrix and a 2x2 identity matrix? Maybe undefined behaviour, or an exception?

My current attempt raises an exception for this doctest that the column widths are inconsistent.



---

archive/issue_comments_033192.json:
```json
{
    "body": "For those interested, my current work-in-progress patch is at\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/sage_WIP_block_matrix.patch",
    "created_at": "2010-01-29T15:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33192",
    "user": "wjp"
}
```

For those interested, my current work-in-progress patch is at

http://www.math.leidenuniv.nl/~wpalenst/sage/sage_WIP_block_matrix.patch



---

archive/issue_comments_033193.json:
```json
{
    "body": "Further work in progress (replacing the previous patch). This also addresses #2429.\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/block_matrix_2.patch",
    "created_at": "2011-01-11T20:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33193",
    "user": "wjp"
}
```

Further work in progress (replacing the previous patch). This also addresses #2429.

http://www.math.leidenuniv.nl/~wpalenst/sage/block_matrix_2.patch



---

archive/issue_comments_033194.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-12T01:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33194",
    "user": "wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033195.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-12T21:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33195",
    "user": "aly.deines"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033196.json:
```json
{
    "body": "The following tests failed:\n\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  devel/sage/sage/matrix/matrix2.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/combinat/designs/incidence_structures.py # 1 doctests failed\n\tsage -t  devel/sage/sage/crypto/lattice.py # 9 doctests failed\n\tsage -t  devel/sage/sage/combinat/matrices/hadamard_matrix.py # 1 doctests failed\n----------------------------------------------------------------------\n\n```\n",
    "created_at": "2011-01-12T21:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33196",
    "user": "aly.deines"
}
```

The following tests failed:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  devel/sage/sage/matrix/matrix2.pyx # 2 doctests failed
	sage -t  devel/sage/sage/combinat/designs/incidence_structures.py # 1 doctests failed
	sage -t  devel/sage/sage/crypto/lattice.py # 9 doctests failed
	sage -t  devel/sage/sage/combinat/matrices/hadamard_matrix.py # 1 doctests failed
----------------------------------------------------------------------

```




---

archive/issue_comments_033197.json:
```json
{
    "body": "Attachment [4492_block_matrix.patch](tarball://root/attachments/some-uuid/ticket4492/4492_block_matrix.patch) by wjp created at 2011-01-12 21:55:41\n\nblock_matrix rewrite. Replaces all previous patches.",
    "created_at": "2011-01-12T21:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33197",
    "user": "wjp"
}
```

Attachment [4492_block_matrix.patch](tarball://root/attachments/some-uuid/ticket4492/4492_block_matrix.patch) by wjp created at 2011-01-12 21:55:41

block_matrix rewrite. Replaces all previous patches.



---

archive/issue_comments_033198.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-12T21:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33198",
    "user": "wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033199.json:
```json
{
    "body": "Oops, sorry about that. New patch up that fixes those.",
    "created_at": "2011-01-12T21:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33199",
    "user": "wjp"
}
```

Oops, sorry about that. New patch up that fixes those.



---

archive/issue_comments_033200.json:
```json
{
    "body": "Attachment [trac_4492-block-matrix-reviewer.patch](tarball://root/attachments/some-uuid/ticket4492/trac_4492-block-matrix-reviewer.patch) by rbeezer created at 2011-01-13 06:30:46\n\nLooks real nice.  I've added some edits in a reviewer patch.\n\nI'll run full tests overnight (with reviewer patch), and then will be ready to give this a positive review (subject to acceptance of my reviewer edits).",
    "created_at": "2011-01-13T06:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33200",
    "user": "rbeezer"
}
```

Attachment [trac_4492-block-matrix-reviewer.patch](tarball://root/attachments/some-uuid/ticket4492/trac_4492-block-matrix-reviewer.patch) by rbeezer created at 2011-01-13 06:30:46

Looks real nice.  I've added some edits in a reviewer patch.

I'll run full tests overnight (with reviewer patch), and then will be ready to give this a positive review (subject to acceptance of my reviewer edits).



---

archive/issue_comments_033201.json:
```json
{
    "body": "All tests in `sage/devel` pass with reviewer patch applied.  So I am all clear on a positive review.  Once the reviewer patch gets a review, this can be flipped to \"positive review\".\n\nNice contribution - this will be very useful.\n\nRob",
    "created_at": "2011-01-13T18:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33201",
    "user": "rbeezer"
}
```

All tests in `sage/devel` pass with reviewer patch applied.  So I am all clear on a positive review.  Once the reviewer patch gets a review, this can be flipped to "positive review".

Nice contribution - this will be very useful.

Rob



---

archive/issue_comments_033202.json:
```json
{
    "body": "Attachment [4492_typo.patch](tarball://root/attachments/some-uuid/ticket4492/4492_typo.patch) by wjp created at 2011-01-13 18:54:31",
    "created_at": "2011-01-13T18:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33202",
    "user": "wjp"
}
```

Attachment [4492_typo.patch](tarball://root/attachments/some-uuid/ticket4492/4492_typo.patch) by wjp created at 2011-01-13 18:54:31



---

archive/issue_comments_033203.json:
```json
{
    "body": "How should the patches be applied?  If I try either of the last two by themselves, they don't apply.",
    "created_at": "2011-01-13T18:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33203",
    "user": "aly.deines"
}
```

How should the patches be applied?  If I try either of the last two by themselves, they don't apply.



---

archive/issue_comments_033204.json:
```json
{
    "body": "The last three, in order:\n\nApply 4492_block_matrix.patch, trac_4492-block-matrix-reviewer.patch, 4492_typo.patch",
    "created_at": "2011-01-13T19:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33204",
    "user": "wjp"
}
```

The last three, in order:

Apply 4492_block_matrix.patch, trac_4492-block-matrix-reviewer.patch, 4492_typo.patch



---

archive/issue_comments_033205.json:
```json
{
    "body": "The reviewer patch looks good, and passes all tests for me too. The doctests and documentation it adds are really clarifying. (I did add a very minor patch on top of it fixing two small typos.)",
    "created_at": "2011-01-13T19:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33205",
    "user": "wjp"
}
```

The reviewer patch looks good, and passes all tests for me too. The doctests and documentation it adds are really clarifying. (I did add a very minor patch on top of it fixing two small typos.)



---

archive/issue_comments_033206.json:
```json
{
    "body": "It looks good and all tests pass for me too.",
    "created_at": "2011-01-13T19:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33206",
    "user": "aly.deines"
}
```

It looks good and all tests pass for me too.



---

archive/issue_comments_033207.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T19:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33207",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033208.json:
```json
{
    "body": "This needs to be rebased to sage-4.6.2.alpha1",
    "created_at": "2011-01-25T08:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33208",
    "user": "jdemeyer"
}
```

This needs to be rebased to sage-4.6.2.alpha1



---

archive/issue_comments_033209.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-25T08:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33209",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_033210.json:
```json
{
    "body": "rebased to 4.6.2.alpha1",
    "created_at": "2011-01-25T09:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33210",
    "user": "wjp"
}
```

rebased to 4.6.2.alpha1



---

archive/issue_comments_033211.json:
```json
{
    "body": "Attachment [4492_block_matrix_rebased.patch](tarball://root/attachments/some-uuid/ticket4492/4492_block_matrix_rebased.patch) by wjp created at 2011-01-25 09:23:47",
    "created_at": "2011-01-25T09:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33211",
    "user": "wjp"
}
```

Attachment [4492_block_matrix_rebased.patch](tarball://root/attachments/some-uuid/ticket4492/4492_block_matrix_rebased.patch) by wjp created at 2011-01-25 09:23:47



---

archive/issue_comments_033212.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-25T09:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33212",
    "user": "wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033213.json:
```json
{
    "body": "Rebased patch attached. (No actual changes, just the context of one of the hunks had changed.)",
    "created_at": "2011-01-25T09:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33213",
    "user": "wjp"
}
```

Rebased patch attached. (No actual changes, just the context of one of the hunks had changed.)



---

archive/issue_comments_033214.json:
```json
{
    "body": "Attachment [trac_4492-doctest-number-field.patch](tarball://root/attachments/some-uuid/ticket4492/trac_4492-doctest-number-field.patch) by rbeezer created at 2011-01-26 00:38:45\n\nRebased patches apply fine and Sage builds.\n\nHowever 3 doctests fail.  These can be traced to #10433 that snuck into 4.6.2.alpha1 while this was in-progress.  ;-)  Specifically one 2x2 block matrix built at line 2366 of `sage/rings/number_field/number_field_ideal.py`\n\nLatest patch rearranges the block matrix construction to meet new requirements for more explicit lists for the block matrix.  I've cc'ed David Loeffler if he wants to check off on just that one change.  Passes all tests now in sage/rings.  All work here is on 4.6.2.alpha1.\n\nWould somebody like to retest the whole package now?",
    "created_at": "2011-01-26T00:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33214",
    "user": "rbeezer"
}
```

Attachment [trac_4492-doctest-number-field.patch](tarball://root/attachments/some-uuid/ticket4492/trac_4492-doctest-number-field.patch) by rbeezer created at 2011-01-26 00:38:45

Rebased patches apply fine and Sage builds.

However 3 doctests fail.  These can be traced to #10433 that snuck into 4.6.2.alpha1 while this was in-progress.  ;-)  Specifically one 2x2 block matrix built at line 2366 of `sage/rings/number_field/number_field_ideal.py`

Latest patch rearranges the block matrix construction to meet new requirements for more explicit lists for the block matrix.  I've cc'ed David Loeffler if he wants to check off on just that one change.  Passes all tests now in sage/rings.  All work here is on 4.6.2.alpha1.

Would somebody like to retest the whole package now?



---

archive/issue_comments_033215.json:
```json
{
    "body": "(The change to number field code looks fine to me.)",
    "created_at": "2011-01-26T08:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33215",
    "user": "davidloeffler"
}
```

(The change to number field code looks fine to me.)



---

archive/issue_comments_033216.json:
```json
{
    "body": "I will test the patches.",
    "created_at": "2011-01-26T10:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33216",
    "user": "jdemeyer"
}
```

I will test the patches.



---

archive/issue_comments_033217.json:
```json
{
    "body": "I've also run tests with 4.6.2-alpha2 + this ticket, and all tests passed.",
    "created_at": "2011-01-26T11:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33217",
    "user": "wjp"
}
```

I've also run tests with 4.6.2-alpha2 + this ticket, and all tests passed.



---

archive/issue_comments_033218.json:
```json
{
    "body": "Yep, tests are okay.",
    "created_at": "2011-01-26T22:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33218",
    "user": "jdemeyer"
}
```

Yep, tests are okay.



---

archive/issue_comments_033219.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-27T05:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33219",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033220.json:
```json
{
    "body": "David - thanks for the quick check.\n\nJeroen, Willem - thanks for the testing.\n\nSounds like the latest patch has been tested and everybody is OK with all of this, so I'm going to switch this back to positive review.",
    "created_at": "2011-01-27T05:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33220",
    "user": "rbeezer"
}
```

David - thanks for the quick check.

Jeroen, Willem - thanks for the testing.

Sounds like the latest patch has been tested and everybody is OK with all of this, so I'm going to switch this back to positive review.



---

archive/issue_comments_033221.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-27T09:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4492#issuecomment-33221",
    "user": "jdemeyer"
}
```

Resolution: fixed
