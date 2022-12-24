# Issue 5797: raise coverage in matrix1.pyx to 100%

archive/issues_005797.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jason\n\nIn 3.4.1.rc2, matrix1.pyx is missing doctests and documentation. I'll attach a patch that covers all but two functions:\n\n`new_matrix` is just a wrapper around `matrix_space` and `MatrixSpace`. The documentation for `MatrixSpace` isn't complete enough for me to say exactly what all the parameters of `new_matrix` do. Can someone who knows more about this make a suggestion?\n\nThe function `_singular_` has no doctests (and the current docstring is deeply confusing) and -- surprise, surprise -- is broken. I'll open a separate ticket for that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5797\n\n",
    "created_at": "2009-04-16T03:22:05Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "raise coverage in matrix1.pyx to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5797",
    "user": "ddrake"
}
```
Assignee: mabshoff

CC:  jason

In 3.4.1.rc2, matrix1.pyx is missing doctests and documentation. I'll attach a patch that covers all but two functions:

`new_matrix` is just a wrapper around `matrix_space` and `MatrixSpace`. The documentation for `MatrixSpace` isn't complete enough for me to say exactly what all the parameters of `new_matrix` do. Can someone who knows more about this make a suggestion?

The function `_singular_` has no doctests (and the current docstring is deeply confusing) and -- surprise, surprise -- is broken. I'll open a separate ticket for that.

Issue created by migration from https://trac.sagemath.org/ticket/5797





---

archive/issue_comments_045480.json:
```json
{
    "body": "Attachment [trac_5797.patch](tarball://root/attachments/some-uuid/ticket5797/trac_5797.patch) by ddrake created at 2009-04-16 04:10:02",
    "created_at": "2009-04-16T04:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45480",
    "user": "ddrake"
}
```

Attachment [trac_5797.patch](tarball://root/attachments/some-uuid/ticket5797/trac_5797.patch) by ddrake created at 2009-04-16 04:10:02



---

archive/issue_comments_045481.json:
```json
{
    "body": "The attached patch adds doctests, documentation, and also fixes up a lot of the ReST formatting.\n\nI'm ignoring `_singular_` for now, since it's broken and I don't know enough to fix it. I do need advice on what to do for `new_matrix`.",
    "created_at": "2009-04-16T04:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45481",
    "user": "ddrake"
}
```

The attached patch adds doctests, documentation, and also fixes up a lot of the ReST formatting.

I'm ignoring `_singular_` for now, since it's broken and I don't know enough to fix it. I do need advice on what to do for `new_matrix`.



---

archive/issue_comments_045482.json:
```json
{
    "body": "The `_singular_` ticket is #5798.",
    "created_at": "2009-04-16T04:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45482",
    "user": "ddrake"
}
```

The `_singular_` ticket is #5798.



---

archive/issue_comments_045483.json:
```json
{
    "body": "Attachment [trac_5797-review.patch](tarball://root/attachments/some-uuid/ticket5797/trac_5797-review.patch) by cremona created at 2009-04-18 15:01:51\n\nreplaces previous",
    "created_at": "2009-04-18T15:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45483",
    "user": "cremona"
}
```

Attachment [trac_5797-review.patch](tarball://root/attachments/some-uuid/ticket5797/trac_5797-review.patch) by cremona created at 2009-04-18 15:01:51

replaces previous



---

archive/issue_comments_045484.json:
```json
{
    "body": "The patch applies fine (to 3.4.1.rc3) and the docs build and look ok.\n\nIt seems a pity not to have any doctest for new_matrix(), so I have added one.  I also added \"indirect doctest\" where necessary and a load(dumps) test, so that we now have\n\n```\nsage/matrix/matrix1.pyx\nSCORE sage/matrix/matrix1.pyx: 97% (36 of 37)\n\nMissing doctests:\n\t * _singular_(self, singular=None):\n```\n\n\nI put \"positive review\" despite adding a little.\n\nThe new patch replaces the first one.",
    "created_at": "2009-04-18T15:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45484",
    "user": "cremona"
}
```

The patch applies fine (to 3.4.1.rc3) and the docs build and look ok.

It seems a pity not to have any doctest for new_matrix(), so I have added one.  I also added "indirect doctest" where necessary and a load(dumps) test, so that we now have

```
sage/matrix/matrix1.pyx
SCORE sage/matrix/matrix1.pyx: 97% (36 of 37)

Missing doctests:
	 * _singular_(self, singular=None):
```


I put "positive review" despite adding a little.

The new patch replaces the first one.



---

archive/issue_comments_045485.json:
```json
{
    "body": "Well, the coverage is 97%, so let's adjust the summary ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T17:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45485",
    "user": "mabshoff"
}
```

Well, the coverage is 97%, so let's adjust the summary ;)

Cheers,

Michael



---

archive/issue_comments_045486.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> I put \"positive review\" despite adding a little.\n\nI'm not sure if I can/should review your changes, but they are fine and I approve. :)\n\nI didn't know about the \"indirect doctest\", nor really how to write a load/dumps test. Thanks for adding those.\n\nThank you also for writing the new_matrix doctest. Perhaps I should open another ticket for improving the MatrixSpace documentation.",
    "created_at": "2009-04-18T22:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45486",
    "user": "ddrake"
}
```

Replying to [comment:4 cremona]:
> I put "positive review" despite adding a little.

I'm not sure if I can/should review your changes, but they are fine and I approve. :)

I didn't know about the "indirect doctest", nor really how to write a load/dumps test. Thanks for adding those.

Thank you also for writing the new_matrix doctest. Perhaps I should open another ticket for improving the MatrixSpace documentation.



---

archive/issue_comments_045487.json:
```json
{
    "body": "Oops?\n\n```\nBuilding modified file sage/matrix/matrix1.pyx.\nExecute 1 commands (using 1 threads)\npython2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage-main -o sage/matrix/matrix1.c sage/matrix/matrix1.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\ninclude \"../ext/stdsage.pxi\"\ninclude \"../ext/python.pxi\"\n\nimport sage.modules.free_module\n\nTESTS::\n    ^\n------------------------------------------------------------\n```\n\nAdding appropriate `\"\"\"` fixes it.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T07:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45487",
    "user": "mabshoff"
}
```

Oops?

```
Building modified file sage/matrix/matrix1.pyx.
Execute 1 commands (using 1 threads)
python2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage-main -o sage/matrix/matrix1.c sage/matrix/matrix1.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
include "../ext/stdsage.pxi"
include "../ext/python.pxi"

import sage.modules.free_module

TESTS::
    ^
------------------------------------------------------------
```

Adding appropriate `"""` fixes it.

Cheers,

Michael



---

archive/issue_comments_045488.json:
```json
{
    "body": "Attachment [trac_5797-review-fixed.patch](tarball://root/attachments/some-uuid/ticket5797/trac_5797-review-fixed.patch) by ddrake created at 2009-04-22 07:59:36\n\nI moved John's misplaced TESTS block inside the file's header docstring. Coverage is now 97%, with only the missing Singular doctest.",
    "created_at": "2009-04-22T07:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45488",
    "user": "ddrake"
}
```

Attachment [trac_5797-review-fixed.patch](tarball://root/attachments/some-uuid/ticket5797/trac_5797-review-fixed.patch) by ddrake created at 2009-04-22 07:59:36

I moved John's misplaced TESTS block inside the file's header docstring. Coverage is now 97%, with only the missing Singular doctest.



---

archive/issue_comments_045489.json:
```json
{
    "body": "Sorry about that -- very mysterious as I certainly did test my own patch.  Thanks for fixing it.  john",
    "created_at": "2009-04-22T09:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45489",
    "user": "cremona"
}
```

Sorry about that -- very mysterious as I certainly did test my own patch.  Thanks for fixing it.  john



---

archive/issue_comments_045490.json:
```json
{
    "body": "Merged trac_5797-review-fixed.patch in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T06:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45490",
    "user": "mabshoff"
}
```

Merged trac_5797-review-fixed.patch in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_045491.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-23T06:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5797#issuecomment-45491",
    "user": "mabshoff"
}
```

Resolution: fixed
