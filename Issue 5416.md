# Issue 5416: [with patch, needs review] miscellaneous documentation fixes

archive/issues_005416.json:
```json
{
    "body": "Assignee: cwitty\n\nAs I was reviewing sphinxification patches, I noticed a lot of pre-existing issues in the documentation.  Instead of trying to fix these issues as part of sphinxification, I made notes to take care of things later.\n\nThis patch covers many of those defects.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5416\n\n",
    "created_at": "2009-03-01T23:53:17Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] miscellaneous documentation fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5416",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

As I was reviewing sphinxification patches, I noticed a lot of pre-existing issues in the documentation.  Instead of trying to fix these issues as part of sphinxification, I made notes to take care of things later.

This patch covers many of those defects.

Issue created by migration from https://trac.sagemath.org/ticket/5416





---

archive/issue_comments_041837.json:
```json
{
    "body": "Attachment [misc-doc-fixes.patch](tarball://root/attachments/some-uuid/ticket5416/misc-doc-fixes.patch) by mvngu created at 2009-03-02 04:46:10\n\nREFEREE REPORT\n\n\n\nThe patch **misc-doc-fixes.patch** applied OK against 3.4.alpha0 and the documentation built OK with the command:\n\n```\nsage -docbuild all html\n```\nI rebuilt the entire set of documentation because the patch touches files spanning the reference manual, the tutorial, the programming guide, and so on. Although the patch fixes a load of formatting issues and typos, I can still see (in the patch itself) that some typos are not fixed. I'm not saying that the patch introduces any new formatting issues or typos; just that it misses some that I can see in the patch itself. For example,  the patch has the following line to fix `sage/rings/polynomial/pbori.pyx`:\n\n```\n@@ -1148,7 +1148,7 @@\n     def _magma_init_(self, magma):\n         r\"\"\"\n         Return a a string which when evaluated with Magma returns a Magma\n-        representaion of this boolean polynomial ring.\n+        representation of this boolean polynomial ring.\n         \n         INPUT:\n```\nwhere one should note the line \"Return a a string which\". Another example concerning the file `sage/rings/real_mpfi.pyx` that the patch touches:\n\n```\n@@ -3789,7 +3789,7 @@\n #              1.6449340668482264364724151666460251892    # 64-bit\n \n #         Note that the number of bits of precision in the constructor only\n-#         effects the internel precision of the pari number, not the number\n+#         effects the internal precision of the pari number, not the number\n #         of digits that gets displayed.  To increase that you must\n #         use \\code{pari.set_real_precision}.\n```\nNote the line \n\n```\n+#         effects the internal precision of the pari number, not the number\n```\nwhere \"effects\" should be \"affects\". I have no time to fix these now, but if anyone does, please open another ticket for that. I can give this patch a positive review for the problems that it fixes.",
    "created_at": "2009-03-02T04:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5416#issuecomment-41837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [misc-doc-fixes.patch](tarball://root/attachments/some-uuid/ticket5416/misc-doc-fixes.patch) by mvngu created at 2009-03-02 04:46:10

REFEREE REPORT



The patch **misc-doc-fixes.patch** applied OK against 3.4.alpha0 and the documentation built OK with the command:

```
sage -docbuild all html
```
I rebuilt the entire set of documentation because the patch touches files spanning the reference manual, the tutorial, the programming guide, and so on. Although the patch fixes a load of formatting issues and typos, I can still see (in the patch itself) that some typos are not fixed. I'm not saying that the patch introduces any new formatting issues or typos; just that it misses some that I can see in the patch itself. For example,  the patch has the following line to fix `sage/rings/polynomial/pbori.pyx`:

```
@@ -1148,7 +1148,7 @@
     def _magma_init_(self, magma):
         r"""
         Return a a string which when evaluated with Magma returns a Magma
-        representaion of this boolean polynomial ring.
+        representation of this boolean polynomial ring.
         
         INPUT:
```
where one should note the line "Return a a string which". Another example concerning the file `sage/rings/real_mpfi.pyx` that the patch touches:

```
@@ -3789,7 +3789,7 @@
 #              1.6449340668482264364724151666460251892    # 64-bit
 
 #         Note that the number of bits of precision in the constructor only
-#         effects the internel precision of the pari number, not the number
+#         effects the internal precision of the pari number, not the number
 #         of digits that gets displayed.  To increase that you must
 #         use \code{pari.set_real_precision}.
```
Note the line 

```
+#         effects the internal precision of the pari number, not the number
```
where "effects" should be "affects". I have no time to fix these now, but if anyone does, please open another ticket for that. I can give this patch a positive review for the problems that it fixes.



---

archive/issue_comments_041838.json:
```json
{
    "body": "Unfortunately some of the fixes interact with other documentation fixes, likely due to some of the issues already being fixed via other patches:\n\n```\npatching file sage/matrix/matrix_modn_dense.pyx\nHunk #1 FAILED at 1.\n1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_modn_dense.pyx.rej\npatching file sage/matrix/matrix_modn_sparse.pyx\nHunk #1 FAILED at 1.\n1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_modn_sparse.pyx.rej\npatching file sage/matrix/matrix_real_double_dense.pyx\npatching file sage/modules/free_module_element.pyx\npatching file sage/rings/arith.py\nHunk #1 succeeded at 197 (offset 1 line).\nHunk #2 FAILED at 963.\nHunk #3 FAILED at 1603.\nHunk #4 succeeded at 1654 (offset 12 lines).\n2 out of 4 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej\npatching file sage/rings/complex_number.pyx\nHunk #1 succeeded at 305 with fuzz 1.\npatching file sage/rings/finite_field.py\npatching file sage/rings/finite_field_element.py\npatching file sage/rings/ideal.py\nHunk #1 succeeded at 337 (offset 4 lines).\nHunk #2 succeeded at 365 (offset 4 lines).\nHunk #3 FAILED at 579.\nHunk #4 FAILED at 985.\n2 out of 4 hunks FAILED -- saving rejects to file sage/rings/ideal.py.rej\npatching file sage/rings/integer.pyx\n```\n\nPlease rebase against 3.4.rc0 out in a couple hours.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T05:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5416#issuecomment-41838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Unfortunately some of the fixes interact with other documentation fixes, likely due to some of the issues already being fixed via other patches:

```
patching file sage/matrix/matrix_modn_dense.pyx
Hunk #1 FAILED at 1.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_modn_dense.pyx.rej
patching file sage/matrix/matrix_modn_sparse.pyx
Hunk #1 FAILED at 1.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_modn_sparse.pyx.rej
patching file sage/matrix/matrix_real_double_dense.pyx
patching file sage/modules/free_module_element.pyx
patching file sage/rings/arith.py
Hunk #1 succeeded at 197 (offset 1 line).
Hunk #2 FAILED at 963.
Hunk #3 FAILED at 1603.
Hunk #4 succeeded at 1654 (offset 12 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej
patching file sage/rings/complex_number.pyx
Hunk #1 succeeded at 305 with fuzz 1.
patching file sage/rings/finite_field.py
patching file sage/rings/finite_field_element.py
patching file sage/rings/ideal.py
Hunk #1 succeeded at 337 (offset 4 lines).
Hunk #2 succeeded at 365 (offset 4 lines).
Hunk #3 FAILED at 579.
Hunk #4 FAILED at 985.
2 out of 4 hunks FAILED -- saving rejects to file sage/rings/ideal.py.rej
patching file sage/rings/integer.pyx
```

Please rebase against 3.4.rc0 out in a couple hours.

Cheers,

Michael



---

archive/issue_comments_041839.json:
```json
{
    "body": "Attachment [misc-doc-fixes-rebased.patch](tarball://root/attachments/some-uuid/ticket5416/misc-doc-fixes-rebased.patch) by cwitty created at 2009-03-03 17:14:39",
    "created_at": "2009-03-03T17:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5416#issuecomment-41839",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [misc-doc-fixes-rebased.patch](tarball://root/attachments/some-uuid/ticket5416/misc-doc-fixes-rebased.patch) by cwitty created at 2009-03-03 17:14:39



---

archive/issue_comments_041840.json:
```json
{
    "body": "I rebased the patch against 3.4.rc0.  I also took the opportunity to fix one of the issues raised by mvngu (the other had already been fixed in rc0).",
    "created_at": "2009-03-03T17:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5416#issuecomment-41840",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I rebased the patch against 3.4.rc0.  I also took the opportunity to fix one of the issues raised by mvngu (the other had already been fixed in rc0).



---

archive/issue_comments_041841.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\n\nThe newly rebased patch **misc-doc-fixes-rebased.patch** applied OK against 3.4.rc0. The documentation rebuilds fine and all doctests passed with the options\n\n```\n-t -long\n```\nHowever, I still see a number of typos in the patch, problems that are NOT introduced by the patch itself. These should be addressed in another ticket, which I plan to do unless someone beats me to it. I can give the rebased patch a positive review for the problems that it fixes.",
    "created_at": "2009-03-04T04:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5416#issuecomment-41841",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT




The newly rebased patch **misc-doc-fixes-rebased.patch** applied OK against 3.4.rc0. The documentation rebuilds fine and all doctests passed with the options

```
-t -long
```
However, I still see a number of typos in the patch, problems that are NOT introduced by the patch itself. These should be addressed in another ticket, which I plan to do unless someone beats me to it. I can give the rebased patch a positive review for the problems that it fixes.



---

archive/issue_comments_041842.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-04T22:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5416#issuecomment-41842",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041843.json:
```json
{
    "body": "Merged misc-doc-fixes-rebased.patch in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T22:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5416#issuecomment-41843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged misc-doc-fixes-rebased.patch in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_events_012615.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-04T22:30:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5416",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5416#event-12615"
}
```
