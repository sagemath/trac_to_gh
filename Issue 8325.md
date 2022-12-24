# Issue 8325: Sphinx warning: 'Could not parse cython argspec'

archive/issues_008325.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri\n\nSphinx warnings from building the HTML reference manual include:\n\n```\nmatrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL: Could not parse cython argspec\nplot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3d.export_jmol: Could not parse cython argspec\n```\n\n\nRelated: #8244.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8325\n\n",
    "created_at": "2010-02-22T05:45:15Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Sphinx warning: 'Could not parse cython argspec'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8325",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  jhpalmieri

Sphinx warnings from building the HTML reference manual include:

```
matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL: Could not parse cython argspec
plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3d.export_jmol: Could not parse cython argspec
```


Related: #8244.

Issue created by migration from https://trac.sagemath.org/ticket/8325





---

archive/issue_comments_073890.json:
```json
{
    "body": "Alternate way to get Cython argspec.  sage repo.",
    "created_at": "2010-02-22T05:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73890",
    "user": "mpatel"
}
```

Alternate way to get Cython argspec.  sage repo.



---

archive/issue_comments_073891.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-22T05:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73891",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073892.json:
```json
{
    "body": "Attachment [trac_8325-cython_argspec.patch](tarball://root/attachments/some-uuid/ticket8325/trac_8325-cython_argspec.patch) by mpatel created at 2010-02-22 05:58:34\n\nThe patch should work for the cases in the description.",
    "created_at": "2010-02-22T05:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73892",
    "user": "mpatel"
}
```

Attachment [trac_8325-cython_argspec.patch](tarball://root/attachments/some-uuid/ticket8325/trac_8325-cython_argspec.patch) by mpatel created at 2010-02-22 05:58:34

The patch should work for the cases in the description.



---

archive/issue_comments_073893.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-24T22:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73893",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073894.json:
```json
{
    "body": "Should patches like this also come with a corresponding one to sagenb.misc.sageinspect, as in #8324?\n\nLooks good, no warnings when building the reference manual for these two files, and the relevant pages look good.  Nice solution.",
    "created_at": "2010-02-24T22:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73894",
    "user": "jhpalmieri"
}
```

Should patches like this also come with a corresponding one to sagenb.misc.sageinspect, as in #8324?

Looks good, no warnings when building the reference manual for these two files, and the relevant pages look good.  Nice solution.



---

archive/issue_comments_073895.json:
```json
{
    "body": "(Is it dangerous to use \"exec\" here?  It looks okay to me, but I feel as though I should always be suspicious of using it.)",
    "created_at": "2010-02-24T22:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73895",
    "user": "jhpalmieri"
}
```

(Is it dangerous to use "exec" here?  It looks okay to me, but I feel as though I should always be suspicious of using it.)



---

archive/issue_comments_073896.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> (Is it dangerous to use \"exec\" here?  It looks okay to me, but I feel as though I should always be suspicious of using it.)\nI think you're right.  The `exec`'d code could have bad side effects.  I'm about to attach a patch that uses [comment:ticket:8244:5 this AST code], instead.",
    "created_at": "2010-02-25T07:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73896",
    "user": "mpatel"
}
```

Replying to [comment:3 jhpalmieri]:
> (Is it dangerous to use "exec" here?  It looks okay to me, but I feel as though I should always be suspicious of using it.)
I think you're right.  The `exec`'d code could have bad side effects.  I'm about to attach a patch that uses [comment:ticket:8244:5 this AST code], instead.



---

archive/issue_comments_073897.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-25T07:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73897",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_073898.json:
```json
{
    "body": "Attachment [trac_8325-cython_argspec.2.patch](tarball://root/attachments/some-uuid/ticket8325/trac_8325-cython_argspec.2.patch) by mpatel created at 2010-02-25 07:36:11\n\nAST version.  sage repo.",
    "created_at": "2010-02-25T07:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73898",
    "user": "mpatel"
}
```

Attachment [trac_8325-cython_argspec.2.patch](tarball://root/attachments/some-uuid/ticket8325/trac_8325-cython_argspec.2.patch) by mpatel created at 2010-02-25 07:36:11

AST version.  sage repo.



---

archive/issue_comments_073899.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-25T07:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73899",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073900.json:
```json
{
    "body": "I've attached the AST version, which seems to work for me, although I have no formal training in computer science.  If the patch looks good, I'll add a sagenb repository patch.",
    "created_at": "2010-02-25T07:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73900",
    "user": "mpatel"
}
```

I've attached the AST version, which seems to work for me, although I have no formal training in computer science.  If the patch looks good, I'll add a sagenb repository patch.



---

archive/issue_comments_073901.json:
```json
{
    "body": "On one hand, this seems to fix the two particular doctests in question.  On the other, it's not perfect. I can see two problems, one of which I know how to fix:\n\n- if the source has the (unlikely) form `def f({(1,2,3): True}): ...`, then this version (and all previous versions) will think that the arg spec ends after `(1,2,3):`.  The function `_sage_getargspec_from_ast` can actually handle this kind of thing, though, so I think we should pass the entire source code to it, rather than truncate at the first `):`.  That is, delete line 470 and change line 471 from\n\n```\nproxy = 'def dummy' + source[beg:end] + '\\n    return' \n```\n\n to\n\n```\nproxy = 'def dummy' + source[beg:] + '\\n    return' \n```\n\n\n- if the docstring has type information, it can't handle it.  I don't know what to do about this, or if it's worth it.\n\nShould we fix the first problem and then go ahead with this?  I also notice that the methods for `SageArgSpecVisitor` don't have doctests.  Is that possible for these sorts of things?  I know nothing about ast.",
    "created_at": "2010-03-04T05:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73901",
    "user": "jhpalmieri"
}
```

On one hand, this seems to fix the two particular doctests in question.  On the other, it's not perfect. I can see two problems, one of which I know how to fix:

- if the source has the (unlikely) form `def f({(1,2,3): True}): ...`, then this version (and all previous versions) will think that the arg spec ends after `(1,2,3):`.  The function `_sage_getargspec_from_ast` can actually handle this kind of thing, though, so I think we should pass the entire source code to it, rather than truncate at the first `):`.  That is, delete line 470 and change line 471 from

```
proxy = 'def dummy' + source[beg:end] + '\n    return' 
```

 to

```
proxy = 'def dummy' + source[beg:] + '\n    return' 
```


- if the docstring has type information, it can't handle it.  I don't know what to do about this, or if it's worth it.

Should we fix the first problem and then go ahead with this?  I also notice that the methods for `SageArgSpecVisitor` don't have doctests.  Is that possible for these sorts of things?  I know nothing about ast.



---

archive/issue_comments_073902.json:
```json
{
    "body": "Attachment [trac_8325-cython_argspec.3.patch](tarball://root/attachments/some-uuid/ticket8325/trac_8325-cython_argspec.3.patch) by mpatel created at 2010-03-04 08:45:05\n\nAnother clause.  More doctests.  Apply only this patch.   sage repo.",
    "created_at": "2010-03-04T08:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73902",
    "user": "mpatel"
}
```

Attachment [trac_8325-cython_argspec.3.patch](tarball://root/attachments/some-uuid/ticket8325/trac_8325-cython_argspec.3.patch) by mpatel created at 2010-03-04 08:45:05

Another clause.  More doctests.  Apply only this patch.   sage repo.



---

archive/issue_comments_073903.json:
```json
{
    "body": "V3:\n\n* Implements your idea to pass the entire source code.  I've included the previous version as a fallback, since `LLL` has a Cython-only construct:\n\n```python\nR = <Matrix_integer_dense>self.new_matrix(entries=map(ZZ,A.list()))\n```\n\n\n* Has extra, more direct doctests of `SageArgSpecVisitor`'s methods.\n\nI don't mind leaving the second problem for another day.",
    "created_at": "2010-03-04T09:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73903",
    "user": "mpatel"
}
```

V3:

* Implements your idea to pass the entire source code.  I've included the previous version as a fallback, since `LLL` has a Cython-only construct:

```python
R = <Matrix_integer_dense>self.new_matrix(entries=map(ZZ,A.list()))
```


* Has extra, more direct doctests of `SageArgSpecVisitor`'s methods.

I don't mind leaving the second problem for another day.



---

archive/issue_comments_073904.json:
```json
{
    "body": "Looks good.  All doctests pass, fixes the two problems.",
    "created_at": "2010-03-04T20:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73904",
    "user": "jhpalmieri"
}
```

Looks good.  All doctests pass, fixes the two problems.



---

archive/issue_comments_073905.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T20:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73905",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073906.json:
```json
{
    "body": "For SageNB's `sageinspect.py`.  sagenb repo.",
    "created_at": "2010-03-04T23:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73906",
    "user": "mpatel"
}
```

For SageNB's `sageinspect.py`.  sagenb repo.



---

archive/issue_comments_073907.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-04T23:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73907",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_073908.json:
```json
{
    "body": "Attachment [sagenb_8325-cython_argspec.patch](tarball://root/attachments/some-uuid/ticket8325/sagenb_8325-cython_argspec.patch) by mpatel created at 2010-03-04 23:46:46\n\nI've attached a version for SageNB.",
    "created_at": "2010-03-04T23:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73908",
    "user": "mpatel"
}
```

Attachment [sagenb_8325-cython_argspec.patch](tarball://root/attachments/some-uuid/ticket8325/sagenb_8325-cython_argspec.patch) by mpatel created at 2010-03-04 23:46:46

I've attached a version for SageNB.



---

archive/issue_comments_073909.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-04T23:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73909",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073910.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-05T01:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73910",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073911.json:
```json
{
    "body": "Unless I'm misunderstanding, the sagenb patch needs work: all of the doctests in the patch import from `sage.misc.sageinspect` rather than from `sagenb...`.",
    "created_at": "2010-03-05T01:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73911",
    "user": "jhpalmieri"
}
```

Unless I'm misunderstanding, the sagenb patch needs work: all of the doctests in the patch import from `sage.misc.sageinspect` rather than from `sagenb...`.



---

archive/issue_comments_073912.json:
```json
{
    "body": "Fix doctest imports.  Replaces previous sagenb patch.",
    "created_at": "2010-03-05T01:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73912",
    "user": "mpatel"
}
```

Fix doctest imports.  Replaces previous sagenb patch.



---

archive/issue_comments_073913.json:
```json
{
    "body": "Attachment [sagenb_8325-cython_argspec.2.patch](tarball://root/attachments/some-uuid/ticket8325/sagenb_8325-cython_argspec.2.patch) by mpatel created at 2010-03-05 01:26:41\n\nOops.  Sorry about that.  V2 is up.",
    "created_at": "2010-03-05T01:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73913",
    "user": "mpatel"
}
```

Attachment [sagenb_8325-cython_argspec.2.patch](tarball://root/attachments/some-uuid/ticket8325/sagenb_8325-cython_argspec.2.patch) by mpatel created at 2010-03-05 01:26:41

Oops.  Sorry about that.  V2 is up.



---

archive/issue_comments_073914.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-05T01:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73914",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073915.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-05T02:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73915",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073916.json:
```json
{
    "body": "I've merged the Sage library patch.  When this is merged in the notebook, we can close this ticket.",
    "created_at": "2010-03-06T09:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73916",
    "user": "mhansen"
}
```

I've merged the Sage library patch.  When this is merged in the notebook, we can close this ticket.



---

archive/issue_comments_073917.json:
```json
{
    "body": "Remove assignee mvngu.",
    "created_at": "2010-03-06T09:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73917",
    "user": "mhansen"
}
```

Remove assignee mvngu.



---

archive/issue_comments_073918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T05:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73918",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_073919.json:
```json
{
    "body": "Merged sagenb patch V2 in sagenb-0.7.5.3, which will be at #8435.",
    "created_at": "2010-03-09T05:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8325#issuecomment-73919",
    "user": "mpatel"
}
```

Merged sagenb patch V2 in sagenb-0.7.5.3, which will be at #8435.
