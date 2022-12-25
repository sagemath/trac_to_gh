# Issue 4310: [with patch, positive review] simplification of the coercion api

archive/issues_004310.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @mwhansen @craigcitro\n\nThe `_has_coerce_map_from_` has been deleted, and the `_coerce_map_from_` now can return a boolean or callable as well as a map. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4310\n\n",
    "closed_at": "2008-11-21T21:32:56Z",
    "created_at": "2008-10-16T18:15:20Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, positive review] simplification of the coercion api",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4310",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

CC:  @mwhansen @craigcitro

The `_has_coerce_map_from_` has been deleted, and the `_coerce_map_from_` now can return a boolean or callable as well as a map. 

Issue created by migration from https://trac.sagemath.org/ticket/4310





---

archive/issue_comments_031495.json:
```json
{
    "body": "Attachment [4310-coerce-simplification.patch](tarball://root/attachments/some-uuid/ticket4310/4310-coerce-simplification.patch) by @jasongrout created at 2008-10-16 20:58:26\n\nGrammar comment: \"Deprecate\" is spelled with an e in the middle, not an i.\n\nDid you know that \"deprecate\" used to mean \"to pray against\" (as an evil) and comes from the latin roots de + precari (precari=\"to pray\").  I just learned that when I looked it up.  It certainly adds emphasis to deprecation statements if people are praying against the evil of whatever is being deprecated!  See http://www.merriam-webster.com/dictionary/deprecate",
    "created_at": "2008-10-16T20:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31495",
    "user": "https://github.com/jasongrout"
}
```

Attachment [4310-coerce-simplification.patch](tarball://root/attachments/some-uuid/ticket4310/4310-coerce-simplification.patch) by @jasongrout created at 2008-10-16 20:58:26

Grammar comment: "Deprecate" is spelled with an e in the middle, not an i.

Did you know that "deprecate" used to mean "to pray against" (as an evil) and comes from the latin roots de + precari (precari="to pray").  I just learned that when I looked it up.  It certainly adds emphasis to deprecation statements if people are praying against the evil of whatever is being deprecated!  See http://www.merriam-webster.com/dictionary/deprecate



---

archive/issue_comments_031496.json:
```json
{
    "body": "Attachment [trac_4310.patch](tarball://root/attachments/some-uuid/ticket4310/trac_4310.patch) by @mwhansen created at 2008-11-21 16:53:17\n\nAfter a rebase and rebuild caused by parent.pxd, I think this is good.  It simplifies the coercion interface a fair amount.\n\nApply only trac_4310.patch",
    "created_at": "2008-11-21T16:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31496",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4310.patch](tarball://root/attachments/some-uuid/ticket4310/trac_4310.patch) by @mwhansen created at 2008-11-21 16:53:17

After a rebase and rebuild caused by parent.pxd, I think this is good.  It simplifies the coercion interface a fair amount.

Apply only trac_4310.patch



---

archive/issue_comments_031497.json:
```json
{
    "body": "Minor nitpick from before still applies to trac_4310: Deprecate is spelled \"Depricate\" in the patch.  I wouldn't let that hold up the patch going in; just pointing it out.",
    "created_at": "2008-11-21T18:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31497",
    "user": "https://github.com/jasongrout"
}
```

Minor nitpick from before still applies to trac_4310: Deprecate is spelled "Depricate" in the patch.  I wouldn't let that hold up the patch going in; just pointing it out.



---

archive/issue_comments_031498.json:
```json
{
    "body": "I have *got* to remember how to spell that word...",
    "created_at": "2008-11-21T19:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31498",
    "user": "https://github.com/robertwb"
}
```

I have *got* to remember how to spell that word...



---

archive/issue_comments_031499.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0 - I also fixed the spelling problem pointed out above.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T21:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0 - I also fixed the spelling problem pointed out above.

Cheers,

Michael



---

archive/issue_events_009741.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-21T21:32:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4310#event-9741"
}
```



---

archive/issue_comments_031500.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T21:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31500",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031501.json:
```json
{
    "body": "For the record: I merged trac_4310.patch into Sage 3.2.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T21:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4310#issuecomment-31501",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: I merged trac_4310.patch into Sage 3.2.1.alpha0.

Cheers,

Michael
