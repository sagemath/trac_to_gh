# Issue 8939: matrix classes for flint polynomials

archive/issues_008939.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @malb jpflori\n\nAttached patch adds templated matrix classes for FLINT's `fmpz_poly` and `zmod_poly` structs.\n\nAt the moment there is no extra functionality provided by the classes, but fast nullspace (over the fraction field), and hopefully inverse implementations will be coming soon. In any case, this should be a good basis for implementing fast algorithms for these matrices.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8939\n\n",
    "created_at": "2010-05-09T22:52:10Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "matrix classes for flint polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8939",
    "user": "https://github.com/burcin"
}
```
Assignee: jason, was

CC:  @malb jpflori

Attached patch adds templated matrix classes for FLINT's `fmpz_poly` and `zmod_poly` structs.

At the moment there is no extra functionality provided by the classes, but fast nullspace (over the fraction field), and hopefully inverse implementations will be coming soon. In any case, this should be a good basis for implementing fast algorithms for these matrices.

Issue created by migration from https://trac.sagemath.org/ticket/8939





---

archive/issue_comments_082177.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-09T22:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82177",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082178.json:
```json
{
    "body": "Attachment [trac_8939-matrix_template-4.4.2.patch](tarball://root/attachments/some-uuid/ticket8939/trac_8939-matrix_template-4.4.2.patch) by @burcin created at 2010-05-22 10:41:03\n\nrebased to 4.4.2",
    "created_at": "2010-05-22T10:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82178",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8939-matrix_template-4.4.2.patch](tarball://root/attachments/some-uuid/ticket8939/trac_8939-matrix_template-4.4.2.patch) by @burcin created at 2010-05-22 10:41:03

rebased to 4.4.2



---

archive/issue_comments_082179.json:
```json
{
    "body": "I uploaded a new patch rebased to 4.4.2.",
    "created_at": "2010-05-22T10:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82179",
    "user": "https://github.com/burcin"
}
```

I uploaded a new patch rebased to 4.4.2.



---

archive/issue_comments_082180.json:
```json
{
    "body": "I get one doctest failure with this patch applied on top of 4.4.2:\n\n```\n**********************************************************************\nFile \"/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/modules/free_module.py\", line 1125:\n    sage: V.base_extend(QQ)\nExpected:\n    Vector space of dimension 7 over Rational Field\nGot:\n    V\n```",
    "created_at": "2010-06-03T14:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82180",
    "user": "https://github.com/malb"
}
```

I get one doctest failure with this patch applied on top of 4.4.2:

```
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/modules/free_module.py", line 1125:
    sage: V.base_extend(QQ)
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
```



---

archive/issue_comments_082181.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-03T15:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82181",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082182.json:
```json
{
    "body": "The patch looks good. However, I'd prefer to have a bit more documentation.\n\n* I think there should be doctests in `fmpz_poly_linkage.pxi`. I know our policy does not require it, but it seems like a good pplace to put some\n* It would be nice to write a bit about how all the files (templates etc.) relate to each other, e.g. some documentation in `matrix_dense_template.pxi` which makes it explains a bit how to use it. (I guess I should do the same for the polynomial template thing.)\n*  I cannot see the \"fast nullspace\"",
    "created_at": "2010-06-03T15:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82182",
    "user": "https://github.com/malb"
}
```

The patch looks good. However, I'd prefer to have a bit more documentation.

* I think there should be doctests in `fmpz_poly_linkage.pxi`. I know our policy does not require it, but it seems like a good pplace to put some
* It would be nice to write a bit about how all the files (templates etc.) relate to each other, e.g. some documentation in `matrix_dense_template.pxi` which makes it explains a bit how to use it. (I guess I should do the same for the polynomial template thing.)
*  I cannot see the "fast nullspace"



---

archive/issue_comments_082183.json:
```json
{
    "body": "Attachment [trac_8939-matrix_template-4.4.2-part2.patch](tarball://root/attachments/some-uuid/ticket8939/trac_8939-matrix_template-4.4.2-part2.patch) by @burcin created at 2010-09-25 19:52:58\n\naddress referee comments",
    "created_at": "2010-09-25T19:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82183",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8939-matrix_template-4.4.2-part2.patch](tarball://root/attachments/some-uuid/ticket8939/trac_8939-matrix_template-4.4.2-part2.patch) by @burcin created at 2010-09-25 19:52:58

address referee comments



---

archive/issue_comments_082184.json:
```json
{
    "body": "Replying to [comment:4 malb]:\n> The patch looks good. However, I'd prefer to have a bit more documentation.\n\n \n>  * I think there should be doctests in `fmpz_poly_linkage.pxi`. I know our policy does not require it, but it seems like a good pplace to put some\n\n\nDone. I added a new file `sage/libs/flint/fmpz_poly_linkage_tests.pyx` with python functions wrapping the `celement_*()` functions. I don't know how to test the `celement_{construct,destruct}()` functions, so they are omitted.\n\n>  * It would be nice to write a bit about how all the files (templates etc.) relate to each other, e.g. some documentation in `matrix_dense_template.pxi` which makes it explains a bit how to use it. (I guess I should do the same for the polynomial template thing.)\n\n\nDone, with a brief description at the beginning of `matrix_dense_template.pxi`.\n\n>  *  I cannot see the \"fast nullspace\"\n\n\nThis will be on a different ticket, when I get around to cleaning it up...",
    "created_at": "2010-09-25T19:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82184",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:4 malb]:
> The patch looks good. However, I'd prefer to have a bit more documentation.

 
>  * I think there should be doctests in `fmpz_poly_linkage.pxi`. I know our policy does not require it, but it seems like a good pplace to put some


Done. I added a new file `sage/libs/flint/fmpz_poly_linkage_tests.pyx` with python functions wrapping the `celement_*()` functions. I don't know how to test the `celement_{construct,destruct}()` functions, so they are omitted.

>  * It would be nice to write a bit about how all the files (templates etc.) relate to each other, e.g. some documentation in `matrix_dense_template.pxi` which makes it explains a bit how to use it. (I guess I should do the same for the polynomial template thing.)


Done, with a brief description at the beginning of `matrix_dense_template.pxi`.

>  *  I cannot see the "fast nullspace"


This will be on a different ticket, when I get around to cleaning it up...



---

archive/issue_comments_082185.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-25T19:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82185",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082186.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-23T17:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82186",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082187.json:
```json
{
    "body": "This patch bitrotted a lot (sorry for not not reviewing your changes earlier!):\n\n```\napplying trac_8939-matrix_template-4.4.2-part2.patch\npatching file module_list.py\nHunk #1 succeeded at 501 with fuzz 2 (offset 18 lines).\nunable to find 'sage/libs/flint/fmpz_poly_linkage.pxi' for patching\n2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/fmpz_poly_linkage.pxi.rej\nunable to find 'sage/matrix/matrix_dense_template.pxi' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sage/matrix/matrix_dense_template.pxi.rej\npatch failed, unable to continue (try -v)\nsage/libs/flint/fmpz_poly_linkage.pxi: No such file or directory\nsage/matrix/matrix_dense_template.pxi: No such file or directory\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8939-matrix_template-4.4.2-part2.patch\n```",
    "created_at": "2010-11-23T17:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82187",
    "user": "https://github.com/malb"
}
```

This patch bitrotted a lot (sorry for not not reviewing your changes earlier!):

```
applying trac_8939-matrix_template-4.4.2-part2.patch
patching file module_list.py
Hunk #1 succeeded at 501 with fuzz 2 (offset 18 lines).
unable to find 'sage/libs/flint/fmpz_poly_linkage.pxi' for patching
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/fmpz_poly_linkage.pxi.rej
unable to find 'sage/matrix/matrix_dense_template.pxi' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/matrix/matrix_dense_template.pxi.rej
patch failed, unable to continue (try -v)
sage/libs/flint/fmpz_poly_linkage.pxi: No such file or directory
sage/matrix/matrix_dense_template.pxi: No such file or directory
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8939-matrix_template-4.4.2-part2.patch
```



---

archive/issue_events_021826.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8939#event-21826"
}
```



---

archive/issue_events_021827.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8939#event-21827"
}
```



---

archive/issue_events_021828.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8939#event-21828"
}
```



---

archive/issue_comments_082188.json:
```json
{
    "body": "Wouldn't it be better now to wrap `fmpz_mat`, `fmpz_poly_mat`, `fmpq_mat`, `nmod_poly_mat` instead? Or do we need to do both to preserve existing features?",
    "created_at": "2014-03-15T08:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8939#issuecomment-82188",
    "user": "https://github.com/mezzarobba"
}
```

Wouldn't it be better now to wrap `fmpz_mat`, `fmpz_poly_mat`, `fmpq_mat`, `nmod_poly_mat` instead? Or do we need to do both to preserve existing features?



---

archive/issue_events_021829.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8939#event-21829"
}
```



---

archive/issue_events_021830.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8939#event-21830"
}
```



---

archive/issue_events_021831.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8939#event-21831"
}
```



---

archive/issue_events_021832.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8939",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8939#event-21832"
}
```
