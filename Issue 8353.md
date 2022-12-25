# Issue 8353: Adding height() and width() functions to square grid paths

archive/issues_008353.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @seblabbe sage-combinat\n\nKeywords: paths, height, width\n\nWhen dealing with word paths on the square grid, it is very useful to know their height and their width.\n\nIn particular, one can compute a bounding box for display purposes. This small ticket adds those two functionalities.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8353\n\n",
    "created_at": "2010-02-24T22:34:23Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Adding height() and width() functions to square grid paths",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8353",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```
Assignee: sage-combinat

CC:  @seblabbe sage-combinat

Keywords: paths, height, width

When dealing with word paths on the square grid, it is very useful to know their height and their width.

In particular, one can compute a bounding box for display purposes. This small ticket adds those two functionalities.

Issue created by migration from https://trac.sagemath.org/ticket/8353





---

archive/issue_comments_074479.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T10:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74479",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074480.json:
```json
{
    "body": "Needs review !",
    "created_at": "2010-02-25T10:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74480",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Needs review !



---

archive/issue_comments_074481.json:
```json
{
    "body": "I would suggest that the value be converted to RR before taking the max or min. You could add a comment explaining the reason of the conversion and that this bug is trac at a ticket number that you give.\n\nThe description of this ticket is not really the good place to put your comment. You can put it in a comment of the ticket instead or on sage-devel. I asked the question on sage-devel :\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/2557a48ad695b42e",
    "created_at": "2010-03-01T11:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74481",
    "user": "https://github.com/seblabbe"
}
```

I would suggest that the value be converted to RR before taking the max or min. You could add a comment explaining the reason of the conversion and that this bug is trac at a ticket number that you give.

The description of this ticket is not really the good place to put your comment. You can put it in a comment of the ticket instead or on sage-devel. I asked the question on sage-devel :
http://groups.google.com/group/sage-devel/browse_thread/thread/2557a48ad695b42e



---

archive/issue_comments_074482.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-01T11:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74482",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074483.json:
```json
{
    "body": "Thanks for your comments !\n\nI found an almost-clean solution for the problem raised by the triangular grid paths. Instead of computing directly the `height()` and `width()` functions, I introduced the `xmin()`, `xmax()`, `ymin()` and `ymax()` functions we talked about. They are called by the two first functions. To solve the problem for the triangular grid paths, I just redefined them by coercing the x- and y-coordinates to real values, so that the `max` and `min` functions be well-defined.\n\nI'll upload another patch in a few minutes. Needs review !",
    "created_at": "2010-03-01T15:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74483",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Thanks for your comments !

I found an almost-clean solution for the problem raised by the triangular grid paths. Instead of computing directly the `height()` and `width()` functions, I introduced the `xmin()`, `xmax()`, `ymin()` and `ymax()` functions we talked about. They are called by the two first functions. To solve the problem for the triangular grid paths, I just redefined them by coercing the x- and y-coordinates to real values, so that the `max` and `min` functions be well-defined.

I'll upload another patch in a few minutes. Needs review !



---

archive/issue_comments_074484.json:
```json
{
    "body": "Changing assignee from sage-combinat to abmasse.",
    "created_at": "2010-03-01T15:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74484",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing assignee from sage-combinat to abmasse.



---

archive/issue_comments_074485.json:
```json
{
    "body": "New patch -- adds functions xmin(), xmax(), etc.",
    "created_at": "2010-03-01T15:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74485",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

New patch -- adds functions xmin(), xmax(), etc.



---

archive/issue_comments_074486.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-01T15:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74486",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074487.json:
```json
{
    "body": "Attachment [trac_8353_square_grid_word_paths_height_width-abm.patch](tarball://root/attachments/some-uuid/ticket8353/trac_8353_square_grid_word_paths_height_width-abm.patch) by abmasse created at 2010-03-01 15:37:23",
    "created_at": "2010-03-01T15:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74487",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Attachment [trac_8353_square_grid_word_paths_height_width-abm.patch](tarball://root/attachments/some-uuid/ticket8353/trac_8353_square_grid_word_paths_height_width-abm.patch) by abmasse created at 2010-03-01 15:37:23



---

archive/issue_comments_074488.json:
```json
{
    "body": "Attachment [trac_8353_review-sl.patch](tarball://root/attachments/some-uuid/ticket8353/trac_8353_review-sl.patch) by @seblabbe created at 2010-03-03 17:45:05\n\nApplies over the precedent patch",
    "created_at": "2010-03-03T17:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74488",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8353_review-sl.patch](tarball://root/attachments/some-uuid/ticket8353/trac_8353_review-sl.patch) by @seblabbe created at 2010-03-03 17:45:05

Applies over the precedent patch



---

archive/issue_comments_074489.json:
```json
{
    "body": "All tests passed in sage/combinat/words. Documentation builds fine. The issue discussed above is fixed. I am giving a positive review to Alex's changes.\n\nI added a small patch fixing some documentation. If Alexandre agrees with the changes I did, I allow him to change the status of the ticket to positive review.",
    "created_at": "2010-03-03T17:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74489",
    "user": "https://github.com/seblabbe"
}
```

All tests passed in sage/combinat/words. Documentation builds fine. The issue discussed above is fixed. I am giving a positive review to Alex's changes.

I added a small patch fixing some documentation. If Alexandre agrees with the changes I did, I allow him to change the status of the ticket to positive review.



---

archive/issue_comments_074490.json:
```json
{
    "body": "I agree with S\u00e9bastien's changes. I retested it just to make sure, and I looked at the documentation, which is still fine. I'll set this ticket to \"positive review\".",
    "created_at": "2010-03-03T19:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74490",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

I agree with Sébastien's changes. I retested it just to make sure, and I looked at the documentation, which is still fine. I'll set this ticket to "positive review".



---

archive/issue_comments_074491.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T19:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74491",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074492.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T09:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8353#issuecomment-74492",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_008543.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-03-06T09:16:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8353",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8353#event-8543"
}
```
