# Issue 8296: getattr hack not failing graciously on descriptors / tab completion broken in emacs

archive/issues_008296.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: tab completion, dir, getattr\n\nThe getattr hack of #7921 to let extension types \"inherit\" from category does not fail graciously on descriptors.\n\nVisible effect: tab completion is broken under emacs:\n\n```\n   sage: n=1\n   sage: n.<tab>  # gives nothing\n```\n\nThis is a variant of #8223. Emacs does not use dir straight away, but instead calls _ip.IP.magic_psearch which is conservative and does not trust dir. So it actually tries to get all advertised attributes, and in particular the descriptor __weakref__ which failed on 1 and confused getattr.\n\nThe attached patch makes the getattr fail graciously in such situations.  It probably would be better for __weakref__ to not appear in dir in the first place, but at least this should fix the bug and variants thereof.\n\nAgain, better implementations of the getattr hack are most welcome. See comments in the code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8296\n\n",
    "closed_at": "2010-03-08T20:54:25Z",
    "created_at": "2010-02-17T21:12:53Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "getattr hack not failing graciously on descriptors / tab completion broken in emacs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8296",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: tab completion, dir, getattr

The getattr hack of #7921 to let extension types "inherit" from category does not fail graciously on descriptors.

Visible effect: tab completion is broken under emacs:

```
   sage: n=1
   sage: n.<tab>  # gives nothing
```

This is a variant of #8223. Emacs does not use dir straight away, but instead calls _ip.IP.magic_psearch which is conservative and does not trust dir. So it actually tries to get all advertised attributes, and in particular the descriptor __weakref__ which failed on 1 and confused getattr.

The attached patch makes the getattr fail graciously in such situations.  It probably would be better for __weakref__ to not appear in dir in the first place, but at least this should fix the bug and variants thereof.

Again, better implementations of the getattr hack are most welcome. See comments in the code.

Issue created by migration from https://trac.sagemath.org/ticket/8296





---

archive/issue_comments_073371.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-17T21:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8296#issuecomment-73371",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073372.json:
```json
{
    "body": "Attachment [trac_8296-fix-tab-completion-emacs-nt.patch](tarball://root/attachments/some-uuid/ticket8296/trac_8296-fix-tab-completion-emacs-nt.patch) by @nthiery created at 2010-02-17 21:50:50",
    "created_at": "2010-02-17T21:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8296#issuecomment-73372",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8296-fix-tab-completion-emacs-nt.patch](tarball://root/attachments/some-uuid/ticket8296/trac_8296-fix-tab-completion-emacs-nt.patch) by @nthiery created at 2010-02-17 21:50:50



---

archive/issue_comments_073373.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-08T17:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8296#issuecomment-73373",
    "user": "https://github.com/nthiery"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_073374.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-03-08T20:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8296#issuecomment-73374",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_073375.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-08T20:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8296#issuecomment-73375",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-08T20:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8296#issuecomment-73376",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_019857.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-08T20:54:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8296",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8296#event-19857"
}
```
