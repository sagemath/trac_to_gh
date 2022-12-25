# Issue 7996: Invisible Text With Dark Theme (White on White Text)

archive/issues_007996.json:
```json
{
    "body": "Assignee: acleone\n\nEditing cells with a dark theme makes the text invisible (white text on a white background).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7996\n\n",
    "created_at": "2010-01-19T08:14:39Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Invisible Text With Dark Theme (White on White Text)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7996",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```
Assignee: acleone

Editing cells with a dark theme makes the text invisible (white text on a white background).

Issue created by migration from https://trac.sagemath.org/ticket/7996





---

archive/issue_comments_069727.json:
```json
{
    "body": "Removes the background-color:white from the css",
    "created_at": "2010-01-19T08:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69727",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Removes the background-color:white from the css



---

archive/issue_comments_069728.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T08:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69728",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069729.json:
```json
{
    "body": "Attachment [trac_7996-invisible_text.patch](tarball://root/attachments/some-uuid/ticket7996/trac_7996-invisible_text.patch) by acleone created at 2010-01-19 08:37:47",
    "created_at": "2010-01-19T08:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69729",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Attachment [trac_7996-invisible_text.patch](tarball://root/attachments/some-uuid/ticket7996/trac_7996-invisible_text.patch) by acleone created at 2010-01-19 08:37:47



---

archive/issue_comments_069730.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T08:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69730",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069731.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-19T08:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69731",
    "user": "https://github.com/TimDumol"
}
```

LGTM.



---

archive/issue_events_019147.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-22T14:59:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7996#event-19147"
}
```



---

archive/issue_events_019148.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T01:01:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7996#event-19148"
}
```



---

archive/issue_comments_069732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69732",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_069733.json:
```json
{
    "body": "With the default color settings in IE8, this makes an active cell's background bluish-grey (lower contrast) but an inactive cell's background is white (higher contrast).  Many users may expect the opposite.  We may get comments.\n\nI'm leaving this closed and will merge it into SageNB 0.7.",
    "created_at": "2010-01-25T02:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69733",
    "user": "https://github.com/qed777"
}
```

With the default color settings in IE8, this makes an active cell's background bluish-grey (lower contrast) but an inactive cell's background is white (higher contrast).  Many users may expect the opposite.  We may get comments.

I'm leaving this closed and will merge it into SageNB 0.7.



---

archive/issue_comments_069734.json:
```json
{
    "body": "Perhaps a better patch would be to leave the \"background-color\" white and set the \"color\" to black.\n\nSee trac_7996-invisible_text.v2.patch - (apply it after the first patch).",
    "created_at": "2010-01-25T02:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69734",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Perhaps a better patch would be to leave the "background-color" white and set the "color" to black.

See trac_7996-invisible_text.v2.patch - (apply it after the first patch).



---

archive/issue_comments_069735.json:
```json
{
    "body": "Apply after the first patch",
    "created_at": "2010-01-25T02:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69735",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Apply after the first patch



---

archive/issue_comments_069736.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-01-25T02:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69736",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_069737.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-01-25T02:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69737",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from closed to new.



---

archive/issue_events_019149.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/acleone",
    "created_at": "2010-01-25T02:43:59Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7996#event-19149"
}
```



---

archive/issue_comments_069738.json:
```json
{
    "body": "Attachment [trac_7996-invisible_text.v2.patch](tarball://root/attachments/some-uuid/ticket7996/trac_7996-invisible_text.v2.patch) by acleone created at 2010-01-25 02:43:59",
    "created_at": "2010-01-25T02:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69738",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Attachment [trac_7996-invisible_text.v2.patch](tarball://root/attachments/some-uuid/ticket7996/trac_7996-invisible_text.v2.patch) by acleone created at 2010-01-25 02:43:59



---

archive/issue_comments_069739.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T02:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69739",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069740.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-25T03:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69740",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069741.json:
```json
{
    "body": "Great!  Now it just happens in Opera 10 (with with or without V2).\n\nI'll merge the pair.",
    "created_at": "2010-01-25T03:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69741",
    "user": "https://github.com/qed777"
}
```

Great!  Now it just happens in Opera 10 (with with or without V2).

I'll merge the pair.



---

archive/issue_comments_069742.json:
```json
{
    "body": "Feel free to post a fix for O10 or simply leave it for the future.  My main motivation here is that I *think* that significantly more notebook users connect with IE than with O.  But I may be wrong.",
    "created_at": "2010-01-25T03:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69742",
    "user": "https://github.com/qed777"
}
```

Feel free to post a fix for O10 or simply leave it for the future.  My main motivation here is that I *think* that significantly more notebook users connect with IE than with O.  But I may be wrong.



---

archive/issue_comments_069743.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T03:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7996#issuecomment-69743",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019150.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T03:40:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7996",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7996#event-19150"
}
```
