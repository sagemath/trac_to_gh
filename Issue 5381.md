# Issue 5381: Refactor matrix kernels

archive/issues_005381.json:
```json
{
    "body": "Assignee: @rbeezer\n\nCC:  @burcin\n\nKeywords: matrix kernel refactor\n\nFrom proposal on sage-devel:\n\nPlace the guts of kernel computations for each (specialized) class into a right_kernel() method, where it would seem to naturally belong.  Mostly these would replace kernel() methods that are computing left kernels.  A call to kernel() or left_kernel() should arrive at the top of the hierarchy where it would take a transpose and call the (specialized) right_kernel().  So there wouldn't be a change in behavior in routines currently calling kernel () or left_kernel(), and we would retain Sage's preference for the left by having the vanilla kernel() give back a left kernel.  The changes would be more efficient computationally and also make the code more expressive of what is really happening when and where.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5381\n\n",
    "created_at": "2009-02-26T03:24:43Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Refactor matrix kernels",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5381",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @rbeezer

CC:  @burcin

Keywords: matrix kernel refactor

From proposal on sage-devel:

Place the guts of kernel computations for each (specialized) class into a right_kernel() method, where it would seem to naturally belong.  Mostly these would replace kernel() methods that are computing left kernels.  A call to kernel() or left_kernel() should arrive at the top of the hierarchy where it would take a transpose and call the (specialized) right_kernel().  So there wouldn't be a change in behavior in routines currently calling kernel () or left_kernel(), and we would retain Sage's preference for the left by having the vanilla kernel() give back a left kernel.  The changes would be more efficient computationally and also make the code more expressive of what is really happening when and where.

Issue created by migration from https://trac.sagemath.org/ticket/5381





---

archive/issue_comments_041362.json:
```json
{
    "body": "Attachment [trac_5381_matrix_kernels.patch](tarball://root/attachments/some-uuid/ticket5381/trac_5381_matrix_kernels.patch) by @rbeezer created at 2009-03-08 23:29:31",
    "created_at": "2009-03-08T23:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41362",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_5381_matrix_kernels.patch](tarball://root/attachments/some-uuid/ticket5381/trac_5381_matrix_kernels.patch) by @rbeezer created at 2009-03-08 23:29:31



---

archive/issue_comments_041363.json:
```json
{
    "body": "This patch conflicts with #5408; I get a reject for that part.  Can you rebase this patch?  I'll look at it quickly before it bitrots this time!",
    "created_at": "2009-04-03T21:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41363",
    "user": "https://github.com/jasongrout"
}
```

This patch conflicts with #5408; I get a reject for that part.  Can you rebase this patch?  I'll look at it quickly before it bitrots this time!



---

archive/issue_comments_041364.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n\nHi Jason,\n\nThanks for looking at this.  I think the reject was my fault.  Partway through doing this I fixed a bug with #5408 and I don't think I got everything put back together right on this patch.  Apply just the new patch (version 2), and test matrices over ZZ with `algorithm='pari'` since that is where I had to reconstruct the mix-up.  I have tested this against all of the sage/matrix directory.\n\nThanks again - this will let me get to #5135.\n\nRob",
    "created_at": "2009-04-06T04:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41364",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:3 jason]:

Hi Jason,

Thanks for looking at this.  I think the reject was my fault.  Partway through doing this I fixed a bug with #5408 and I don't think I got everything put back together right on this patch.  Apply just the new patch (version 2), and test matrices over ZZ with `algorithm='pari'` since that is where I had to reconstruct the mix-up.  I have tested this against all of the sage/matrix directory.

Thanks again - this will let me get to #5135.

Rob



---

archive/issue_comments_041365.json:
```json
{
    "body": "Attachment [trac_5381_matrix_kernels_2.patch](tarball://root/attachments/some-uuid/ticket5381/trac_5381_matrix_kernels_2.patch) by @rbeezer created at 2009-04-06 04:27:29",
    "created_at": "2009-04-06T04:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41365",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_5381_matrix_kernels_2.patch](tarball://root/attachments/some-uuid/ticket5381/trac_5381_matrix_kernels_2.patch) by @rbeezer created at 2009-04-06 04:27:29



---

archive/issue_comments_041366.json:
```json
{
    "body": "Thanks for rebasing.  This is great work!  Positive review pending taking care of the following comments.\n\n* In matrix2.pyx, the exact same code is repeated for kernel() and for left_kernel().  I think it would be cleaner to just have kernel call left_kernel(), rather than repeating the code to compute and cache the left kernel.\n\n* In matrix_integer_dense.pyx, you add a note to kernel_matrix() that tells the user that the preferred method is to call an underscore function.  It seems odd to direct a user away from an API function to a function that is not an officially supported function.  This is especially odd because the reason is a speculative \"in case this function is deprecated in the future\".  To fix this, I would just delete the note about the deprecation.  If a user wants the left kernel matrix, then that's what they want; they'd rather have the function do the work of the transpose and the right kernel matrix.\n\n* A couple of the functions (I believe in matrix_integer_dense.pyx, for example) that are modified are left without doctests.  These should have at least minimal doctests, and preferably should have doctests for the corner cases (e.g., 0 rows or 0 columns in a matrix).\n\nDoctests pass in matrix/*.pyx.  They should be run on all of Sage for this one, though, since kernels are probably used in lots of places of Sage.",
    "created_at": "2009-04-15T05:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41366",
    "user": "https://github.com/jasongrout"
}
```

Thanks for rebasing.  This is great work!  Positive review pending taking care of the following comments.

* In matrix2.pyx, the exact same code is repeated for kernel() and for left_kernel().  I think it would be cleaner to just have kernel call left_kernel(), rather than repeating the code to compute and cache the left kernel.

* In matrix_integer_dense.pyx, you add a note to kernel_matrix() that tells the user that the preferred method is to call an underscore function.  It seems odd to direct a user away from an API function to a function that is not an officially supported function.  This is especially odd because the reason is a speculative "in case this function is deprecated in the future".  To fix this, I would just delete the note about the deprecation.  If a user wants the left kernel matrix, then that's what they want; they'd rather have the function do the work of the transpose and the right kernel matrix.

* A couple of the functions (I believe in matrix_integer_dense.pyx, for example) that are modified are left without doctests.  These should have at least minimal doctests, and preferably should have doctests for the corner cases (e.g., 0 rows or 0 columns in a matrix).

Doctests pass in matrix/*.pyx.  They should be run on all of Sage for this one, though, since kernels are probably used in lots of places of Sage.



---

archive/issue_comments_041367.json:
```json
{
    "body": "New patch (\"_3\") addresses all reviewer comments above, though I could only find one function that needed to have doctests added (`_kernel_matrix_using_pari`).\n\nPassed the following tests:\n\nsage -testall\n\nsage -t --randorder sage/matrix/*\n\nsage -docbuild reference pdf\n\n\nApply just this new (third) patch, which was built on 3.4.2.alpha0\n\nMinh - timings are getting a bit dated, but are probably still accurate, though most of the speedup came from improvments discovered in transposes while working through this.  You could say \"a 16% improvement in right kernels by eliminating paired transposes.\"",
    "created_at": "2009-04-27T03:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41367",
    "user": "https://github.com/rbeezer"
}
```

New patch ("_3") addresses all reviewer comments above, though I could only find one function that needed to have doctests added (`_kernel_matrix_using_pari`).

Passed the following tests:

sage -testall

sage -t --randorder sage/matrix/*

sage -docbuild reference pdf


Apply just this new (third) patch, which was built on 3.4.2.alpha0

Minh - timings are getting a bit dated, but are probably still accurate, though most of the speedup came from improvments discovered in transposes while working through this.  You could say "a 16% improvement in right kernels by eliminating paired transposes."



---

archive/issue_comments_041368.json:
```json
{
    "body": "Attachment [trac_5381_matrix_kernels_3.patch](tarball://root/attachments/some-uuid/ticket5381/trac_5381_matrix_kernels_3.patch) by @aghitza created at 2009-04-30 11:21:15\n\nThe latest patch addresses Jason's comments; it applies cleanly and passes testlong.",
    "created_at": "2009-04-30T11:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41368",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5381_matrix_kernels_3.patch](tarball://root/attachments/some-uuid/ticket5381/trac_5381_matrix_kernels_3.patch) by @aghitza created at 2009-04-30 11:21:15

The latest patch addresses Jason's comments; it applies cleanly and passes testlong.



---

archive/issue_comments_041369.json:
```json
{
    "body": "Merged trac_5381_matrix_kernels_3.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T13:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41369",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5381_matrix_kernels_3.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_041370.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T13:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5381#issuecomment-41370",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
