# Issue 4310: [with patch, needs review] simplification of the coercion api

archive/issues_004310.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  mhansen craigcitro\n\nThe `_has_coerce_map_from_` has been deleted, and the `_coerce_map_from_` now can return a boolean or callable as well as a map. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4310\n\n",
    "created_at": "2008-10-16T18:15:20Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] simplification of the coercion api",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4310",
    "user": "robertwb"
}
```
Assignee: robertwb

CC:  mhansen craigcitro

The `_has_coerce_map_from_` has been deleted, and the `_coerce_map_from_` now can return a boolean or callable as well as a map. 

Issue created by migration from https://trac.sagemath.org/ticket/4310





---

archive/issue_comments_031557.json:
```json
{
    "body": "Attachment [4310-coerce-simplification.patch](tarball://root/attachments/some-uuid/ticket4310/4310-coerce-simplification.patch) by jason created at 2008-10-16 20:58:26\n\nGrammar comment: \"Deprecate\" is spelled with an e in the middle, not an i.\n\nDid you know that \"deprecate\" used to mean \"to pray against\" (as an evil) and comes from the latin roots de + precari (precari=\"to pray\").  I just learned that when I looked it up.  It certainly adds emphasis to deprecation statements if people are praying against the evil of whatever is being deprecated!  See http://www.merriam-webster.com/dictionary/deprecate",
    "created_at": "2008-10-16T20:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31557",
    "user": "jason"
}
```

Attachment [4310-coerce-simplification.patch](tarball://root/attachments/some-uuid/ticket4310/4310-coerce-simplification.patch) by jason created at 2008-10-16 20:58:26

Grammar comment: "Deprecate" is spelled with an e in the middle, not an i.

Did you know that "deprecate" used to mean "to pray against" (as an evil) and comes from the latin roots de + precari (precari="to pray").  I just learned that when I looked it up.  It certainly adds emphasis to deprecation statements if people are praying against the evil of whatever is being deprecated!  See http://www.merriam-webster.com/dictionary/deprecate



---

archive/issue_comments_031558.json:
```json
{
    "body": "Attachment [trac_4310.patch](tarball://root/attachments/some-uuid/ticket4310/trac_4310.patch) by mhansen created at 2008-11-21 16:53:17\n\nAfter a rebase and rebuild caused by parent.pxd, I think this is good.  It simplifies the coercion interface a fair amount.\n\nApply only trac_4310.patch",
    "created_at": "2008-11-21T16:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31558",
    "user": "mhansen"
}
```

Attachment [trac_4310.patch](tarball://root/attachments/some-uuid/ticket4310/trac_4310.patch) by mhansen created at 2008-11-21 16:53:17

After a rebase and rebuild caused by parent.pxd, I think this is good.  It simplifies the coercion interface a fair amount.

Apply only trac_4310.patch



---

archive/issue_comments_031559.json:
```json
{
    "body": "Minor nitpick from before still applies to trac_4310: Deprecate is spelled \"Depricate\" in the patch.  I wouldn't let that hold up the patch going in; just pointing it out.",
    "created_at": "2008-11-21T18:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31559",
    "user": "jason"
}
```

Minor nitpick from before still applies to trac_4310: Deprecate is spelled "Depricate" in the patch.  I wouldn't let that hold up the patch going in; just pointing it out.



---

archive/issue_comments_031560.json:
```json
{
    "body": "I have *got* to remember how to spell that word...",
    "created_at": "2008-11-21T19:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31560",
    "user": "robertwb"
}
```

I have *got* to remember how to spell that word...



---

archive/issue_comments_031561.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0 - I also fixed the spelling problem pointed out above.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T21:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31561",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0 - I also fixed the spelling problem pointed out above.

Cheers,

Michael



---

archive/issue_comments_031562.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T21:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31562",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031563.json:
```json
{
    "body": "For the record: I merged trac_4310.patch into Sage 3.2.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T21:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31563",
    "user": "mabshoff"
}
```

For the record: I merged trac_4310.patch into Sage 3.2.1.alpha0.

Cheers,

Michael
