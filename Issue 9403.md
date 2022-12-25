# Issue 9403: preimage method in NumberFieldHomomorphism_im_gens

archive/issues_009403.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  ebeyerstedt fwclarke @loefflerd\n\nKeywords: number field, embedding, homomorphism, preimage\n\nI am adding a preimage method in the NumberFieldHomomorphism_im_gens class. There may be a better or more general place to put this, but we need it for the descend_to method in EllipticCurve so I am putting it there for now.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9403\n\n",
    "created_at": "2010-07-01T23:18:22Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "preimage method in NumberFieldHomomorphism_im_gens",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9403",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```
Assignee: @aghitza

CC:  ebeyerstedt fwclarke @loefflerd

Keywords: number field, embedding, homomorphism, preimage

I am adding a preimage method in the NumberFieldHomomorphism_im_gens class. There may be a better or more general place to put this, but we need it for the descend_to method in EllipticCurve so I am putting it there for now.



Issue created by migration from https://trac.sagemath.org/ticket/9403





---

archive/issue_comments_089459.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-01T23:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89459",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_089460.json:
```json
{
    "body": "A preimage method for NumberFieldHomomorphism",
    "created_at": "2010-07-02T00:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89460",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

A preimage method for NumberFieldHomomorphism



---

archive/issue_comments_089461.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T00:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89461",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089462.json:
```json
{
    "body": "Attachment [trac_9403-preimage.patch](tarball://root/attachments/some-uuid/ticket9403/trac_9403-preimage.patch) by jeremywest created at 2010-07-02 00:18:23\n\nI have implemented the preimage method including documentation and tests. I just need a review now. Let me know if this should go somewhere better.",
    "created_at": "2010-07-02T00:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89462",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

Attachment [trac_9403-preimage.patch](tarball://root/attachments/some-uuid/ticket9403/trac_9403-preimage.patch) by jeremywest created at 2010-07-02 00:18:23

I have implemented the preimage method including documentation and tests. I just need a review now. Let me know if this should go somewhere better.



---

archive/issue_comments_089463.json:
```json
{
    "body": "The new patch changes each usage of .vector_space to .absolute_vector_space.\nAlso added a doctest.",
    "created_at": "2010-07-02T04:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89463",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

The new patch changes each usage of .vector_space to .absolute_vector_space.
Also added a doctest.



---

archive/issue_comments_089464.json:
```json
{
    "body": "Replaces previous patch.",
    "created_at": "2010-07-02T05:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89464",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

Replaces previous patch.



---

archive/issue_comments_089465.json:
```json
{
    "body": "Attachment [trac_9403-new.patch](tarball://root/attachments/some-uuid/ticket9403/trac_9403-new.patch) by ebeyerstedt created at 2010-07-02 05:44:41\n\nUpdated documentation.",
    "created_at": "2010-07-02T05:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89465",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

Attachment [trac_9403-new.patch](tarball://root/attachments/some-uuid/ticket9403/trac_9403-new.patch) by ebeyerstedt created at 2010-07-02 05:44:41

Updated documentation.



---

archive/issue_comments_089466.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T17:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89466",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089467.json:
```json
{
    "body": "I changed the error message that is returned when the input is not in the image of the homomorphism so that, rather than a message about solving a matrix equation, it gives a message about the input not being in the image.",
    "created_at": "2010-07-02T19:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89467",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

I changed the error message that is returned when the input is not in the image of the homomorphism so that, rather than a message about solving a matrix equation, it gives a message about the input not being in the image.



---

archive/issue_comments_089468.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-02T19:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89468",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_089469.json:
```json
{
    "body": "If you really must upload new patches to an already positively reviewed ticket, you *must* put the status back to \"needs review\".",
    "created_at": "2010-07-02T19:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89469",
    "user": "https://github.com/loefflerd"
}
```

If you really must upload new patches to an already positively reviewed ticket, you *must* put the status back to "needs review".



---

archive/issue_comments_089470.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T19:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89470",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089471.json:
```json
{
    "body": "Attachment [trac_9403-error_handling.patch](tarball://root/attachments/some-uuid/ticket9403/trac_9403-error_handling.patch) by jeremywest created at 2010-07-02 20:27:53\n\nFixes error handling message, replaces all previous patches.",
    "created_at": "2010-07-02T20:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89471",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

Attachment [trac_9403-error_handling.patch](tarball://root/attachments/some-uuid/ticket9403/trac_9403-error_handling.patch) by jeremywest created at 2010-07-02 20:27:53

Fixes error handling message, replaces all previous patches.



---

archive/issue_comments_089472.json:
```json
{
    "body": "David -- can you review the newest patch? If this ticket can get a positive review, then it and #9384 can get into 4.5.2.",
    "created_at": "2010-07-22T23:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89472",
    "user": "https://github.com/dandrake"
}
```

David -- can you review the newest patch? If this ticket can get a positive review, then it and #9384 can get into 4.5.2.



---

archive/issue_comments_089473.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-26T21:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89473",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089474.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-27T00:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89474",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_089475.json:
```json
{
    "body": "Please include the ticket number in your commit messages! Also, Jeremy, you might want to set your username in your .hgrc file -- your patch has a username of \"jeremy`@`west-imac-8-2007.local\".",
    "created_at": "2010-07-27T00:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89475",
    "user": "https://github.com/dandrake"
}
```

Please include the ticket number in your commit messages! Also, Jeremy, you might want to set your username in your .hgrc file -- your patch has a username of "jeremy`@`west-imac-8-2007.local".



---

archive/issue_events_009559.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-27T00:50:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9403#event-9559"
}
```



---

archive/issue_comments_089476.json:
```json
{
    "body": "I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.",
    "created_at": "2010-07-27T04:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89476",
    "user": "https://github.com/qed777"
}
```

I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.
