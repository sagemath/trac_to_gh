# Issue 5151: linear codes decoding algorithms in Sage

archive/issues_005151.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe goal of this patch is to move some more of the algorithms in (the GAP package for error-correcting codes) Guava over to Sage. Currently Guava is included in Sage (in fact, Guava is the only GAP package included in Sage), but once the commands are implemented in Python (or Cython) it will be possible to remove Guava from Sage, while keeping Guava as an optional package. \n\nThe patch adds a new file/module with 2 decoding methods implemented but does not import it into the namespace. Instead, methods from linear_code import them locally as needed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5151\n\n",
    "created_at": "2009-02-01T21:11:09Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "linear codes decoding algorithms in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5151",
    "user": "@wdjoyner"
}
```
Assignee: @rlmill

The goal of this patch is to move some more of the algorithms in (the GAP package for error-correcting codes) Guava over to Sage. Currently Guava is included in Sage (in fact, Guava is the only GAP package included in Sage), but once the commands are implemented in Python (or Cython) it will be possible to remove Guava from Sage, while keeping Guava as an optional package. 

The patch adds a new file/module with 2 decoding methods implemented but does not import it into the namespace. Instead, methods from linear_code import them locally as needed.

Issue created by migration from https://trac.sagemath.org/ticket/5151





---

archive/issue_comments_039409.json:
```json
{
    "body": "to be applied to 3.3.alpha3",
    "created_at": "2009-02-01T21:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39409",
    "user": "@wdjoyner"
}
```

to be applied to 3.3.alpha3



---

archive/issue_comments_039410.json:
```json
{
    "body": "Attachment [trac-5151-decoder.patch](tarball://root/attachments/some-uuid/ticket5151/trac-5151-decoder.patch) by @wdjoyner created at 2009-02-01 21:37:47",
    "created_at": "2009-02-01T21:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39410",
    "user": "@wdjoyner"
}
```

Attachment [trac-5151-decoder.patch](tarball://root/attachments/some-uuid/ticket5151/trac-5151-decoder.patch) by @wdjoyner created at 2009-02-01 21:37:47



---

archive/issue_comments_039411.json:
```json
{
    "body": "Some suggestions:\n\n* The function `weight_order` doesn't get used anywhere, and should probably be removed from the patch. Also, you should remove the commented lines in `syndrome`.\n\n* The docs for `coset_leader` are identical to those for `syndrome` up to the examples. Perhaps this needs to be updated.\n\n* The patch file itself looks funny, since the\n\n```\n# HG changeset patch\n# User David Joyner <wdjoyner@gmail.com>\n# Date 1233523816 18000\n# Node ID d5554b7ab8b14d7b369a200284355d135f319271\n# Parent  d949d3b0e84312be26ede6df676eece1bac738f0\nadded decoder - wdj\n```\n\n   block shows up twice.",
    "created_at": "2009-02-04T23:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39411",
    "user": "@rlmill"
}
```

Some suggestions:

* The function `weight_order` doesn't get used anywhere, and should probably be removed from the patch. Also, you should remove the commented lines in `syndrome`.

* The docs for `coset_leader` are identical to those for `syndrome` up to the examples. Perhaps this needs to be updated.

* The patch file itself looks funny, since the

```
# HG changeset patch
# User David Joyner <wdjoyner@gmail.com>
# Date 1233523816 18000
# Node ID d5554b7ab8b14d7b369a200284355d135f319271
# Parent  d949d3b0e84312be26ede6df676eece1bac738f0
added decoder - wdj
```

   block shows up twice.



---

archive/issue_comments_039412.json:
```json
{
    "body": "to be applied to 3.3.alpha3. Ignore previous patch.",
    "created_at": "2009-02-04T23:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39412",
    "user": "@wdjoyner"
}
```

to be applied to 3.3.alpha3. Ignore previous patch.



---

archive/issue_comments_039413.json:
```json
{
    "body": "Attachment [trac-5151-decoder2.patch](tarball://root/attachments/some-uuid/ticket5151/trac-5151-decoder2.patch) by @wdjoyner created at 2009-02-04 23:51:35\n\nOkay, I redid the patch following these instructions.\n\nIt will now not pass sage -t because now it gets lots of print statements \"Warning: this should never happen\" (from gap.py I think), followed by the correct answer. So the gap interface seems to be printing this message but the code I wrote is returning the correct answer. (After building guava \"manually\", sage -t -long has the same problem.)",
    "created_at": "2009-02-04T23:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39413",
    "user": "@wdjoyner"
}
```

Attachment [trac-5151-decoder2.patch](tarball://root/attachments/some-uuid/ticket5151/trac-5151-decoder2.patch) by @wdjoyner created at 2009-02-04 23:51:35

Okay, I redid the patch following these instructions.

It will now not pass sage -t because now it gets lots of print statements "Warning: this should never happen" (from gap.py I think), followed by the correct answer. So the gap interface seems to be printing this message but the code I wrote is returning the correct answer. (After building guava "manually", sage -t -long has the same problem.)



---

archive/issue_comments_039414.json:
```json
{
    "body": "Apply after other patch",
    "created_at": "2009-02-05T23:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39414",
    "user": "@rlmill"
}
```

Apply after other patch



---

archive/issue_comments_039415.json:
```json
{
    "body": "Attachment [trac-5151-fix.patch](tarball://root/attachments/some-uuid/ticket5151/trac-5151-fix.patch) by @rlmill created at 2009-02-05 23:14:20\n\nI can't reproduce those errors, so positive review.",
    "created_at": "2009-02-05T23:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39415",
    "user": "@rlmill"
}
```

Attachment [trac-5151-fix.patch](tarball://root/attachments/some-uuid/ticket5151/trac-5151-fix.patch) by @rlmill created at 2009-02-05 23:14:20

I can't reproduce those errors, so positive review.



---

archive/issue_comments_039416.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39416",
    "user": "mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_039417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-07T01:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39417",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039418.json:
```json
{
    "body": "Merged trac-5151-decoder2.patch and trac-5151-fix.patch in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T01:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5151#issuecomment-39418",
    "user": "mabshoff"
}
```

Merged trac-5151-decoder2.patch and trac-5151-fix.patch in Sage 3.3.alpha6.

Cheers,

Michael
