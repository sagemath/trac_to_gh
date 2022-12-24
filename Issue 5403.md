# Issue 5403: fix "from ... import *" in class QuadraticForm (cf #4470)

archive/issues_005403.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are a number of \"from ... import *\" in the new quadratic forms code. This messes up tab completion (among other issues).\n\nThe attached patch fixes the issue by explicitly listing every function defined in the quadratic forms files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5403\n\n",
    "created_at": "2009-02-28T21:30:35Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "fix \"from ... import *\" in class QuadraticForm (cf #4470)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5403",
    "user": "tornaria"
}
```
Assignee: mabshoff

There are a number of "from ... import *" in the new quadratic forms code. This messes up tab completion (among other issues).

The attached patch fixes the issue by explicitly listing every function defined in the quadratic forms files.

Issue created by migration from https://trac.sagemath.org/ticket/5403





---

archive/issue_comments_041739.json:
```json
{
    "body": "Attachment [patch.QF.fix_import_star](tarball://root/attachments/some-uuid/ticket5403/patch.QF.fix_import_star) by tornaria created at 2009-02-28 21:31:14\n\npatch to fix import * issues in quadratic forms",
    "created_at": "2009-02-28T21:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41739",
    "user": "tornaria"
}
```

Attachment [patch.QF.fix_import_star](tarball://root/attachments/some-uuid/ticket5403/patch.QF.fix_import_star) by tornaria created at 2009-02-28 21:31:14

patch to fix import * issues in quadratic forms



---

archive/issue_comments_041740.json:
```json
{
    "body": "There are still some issues in the attached patch. I'm working on that now.",
    "created_at": "2009-02-28T22:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41740",
    "user": "tornaria"
}
```

There are still some issues in the attached patch. I'm working on that now.



---

archive/issue_comments_041741.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-28T22:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41741",
    "user": "tornaria"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041742.json:
```json
{
    "body": "Changing assignee from mabshoff to tornaria.",
    "created_at": "2009-02-28T22:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41742",
    "user": "tornaria"
}
```

Changing assignee from mabshoff to tornaria.



---

archive/issue_comments_041743.json:
```json
{
    "body": "Attachment [patch.QF.fix_import_star.2nd](tarball://root/attachments/some-uuid/ticket5403/patch.QF.fix_import_star.2nd) by tornaria created at 2009-02-28 22:54:25\n\n2nd version of the patch, stilll some issue with deepcopy",
    "created_at": "2009-02-28T22:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41743",
    "user": "tornaria"
}
```

Attachment [patch.QF.fix_import_star.2nd](tarball://root/attachments/some-uuid/ticket5403/patch.QF.fix_import_star.2nd) by tornaria created at 2009-02-28 22:54:25

2nd version of the patch, stilll some issue with deepcopy



---

archive/issue_comments_041744.json:
```json
{
    "body": "Changing component from algebra to quadratic forms.",
    "created_at": "2009-03-01T02:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41744",
    "user": "mabshoff"
}
```

Changing component from algebra to quadratic forms.



---

archive/issue_comments_041745.json:
```json
{
    "body": "This would be nice to fix since on every first startup after moving Sage or cloning python will complain about those imports.\n\nI am also marking the patch as needs work until it is ready for review. That way the patch will not be lost :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41745",
    "user": "mabshoff"
}
```

This would be nice to fix since on every first startup after moving Sage or cloning python will complain about those imports.

I am also marking the patch as needs work until it is ready for review. That way the patch will not be lost :)

Cheers,

Michael



---

archive/issue_comments_041746.json:
```json
{
    "body": "Attachment [patch.QF.fix_import_star.3rd](tarball://root/attachments/some-uuid/ticket5403/patch.QF.fix_import_star.3rd) by tornaria created at 2009-03-01 04:15:26\n\n3rd version of the patch, tests pass now",
    "created_at": "2009-03-01T04:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41746",
    "user": "tornaria"
}
```

Attachment [patch.QF.fix_import_star.3rd](tarball://root/attachments/some-uuid/ticket5403/patch.QF.fix_import_star.3rd) by tornaria created at 2009-03-01 04:15:26

3rd version of the patch, tests pass now



---

archive/issue_comments_041747.json:
```json
{
    "body": "In the 3rd patch I added a fix for issue with copying and caching which for some weird reason didn't show up before. \n\nAll quadratic_form tests pass with this patch applied (NOT incremental, just get the 3rd one).",
    "created_at": "2009-03-01T04:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41747",
    "user": "tornaria"
}
```

In the 3rd patch I added a fix for issue with copying and caching which for some weird reason didn't show up before. 

All quadratic_form tests pass with this patch applied (NOT incremental, just get the 3rd one).



---

archive/issue_comments_041748.json:
```json
{
    "body": "Changing assignee from tornaria to mabshoff.",
    "created_at": "2009-03-01T04:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41748",
    "user": "tornaria"
}
```

Changing assignee from tornaria to mabshoff.



---

archive/issue_comments_041749.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-03-01T04:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41749",
    "user": "tornaria"
}
```

Changing status from assigned to new.



---

archive/issue_comments_041750.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T04:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41750",
    "user": "tornaria"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041751.json:
```json
{
    "body": "Changing assignee from mabshoff to tornaria.",
    "created_at": "2009-03-01T04:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41751",
    "user": "tornaria"
}
```

Changing assignee from mabshoff to tornaria.



---

archive/issue_comments_041752.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T04:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41752",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_041753.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T04:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41753",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T04:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41754",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041755.json:
```json
{
    "body": "Attachment [trac_5403_patch.QF.fix_import_star.3rd.patch](tarball://root/attachments/some-uuid/ticket5403/trac_5403_patch.QF.fix_import_star.3rd.patch) by mabshoff created at 2009-03-02 04:08:57\n\nThis is a properly named version of Gonzalo's third patch",
    "created_at": "2009-03-02T04:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5403#issuecomment-41755",
    "user": "mabshoff"
}
```

Attachment [trac_5403_patch.QF.fix_import_star.3rd.patch](tarball://root/attachments/some-uuid/ticket5403/trac_5403_patch.QF.fix_import_star.3rd.patch) by mabshoff created at 2009-03-02 04:08:57

This is a properly named version of Gonzalo's third patch
