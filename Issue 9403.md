# Issue 9403: preimage method in NumberFieldHomomorphism_im_gens

archive/issues_009403.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  ebeyerstedt fwclarke davidloeffler\n\nKeywords: number field, embedding, homomorphism, preimage\n\nI am adding a preimage method in the NumberFieldHomomorphism_im_gens class. There may be a better or more general place to put this, but we need it for the descend_to method in EllipticCurve so I am putting it there for now.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9403\n\n",
    "created_at": "2010-07-01T23:18:22Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "preimage method in NumberFieldHomomorphism_im_gens",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9403",
    "user": "jeremywest"
}
```
Assignee: AlexGhitza

CC:  ebeyerstedt fwclarke davidloeffler

Keywords: number field, embedding, homomorphism, preimage

I am adding a preimage method in the NumberFieldHomomorphism_im_gens class. There may be a better or more general place to put this, but we need it for the descend_to method in EllipticCurve so I am putting it there for now.



Issue created by migration from https://trac.sagemath.org/ticket/9403





---

archive/issue_comments_089602.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-01T23:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89602",
    "user": "jeremywest"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_089603.json:
```json
{
    "body": "A preimage method for NumberFieldHomomorphism",
    "created_at": "2010-07-02T00:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89603",
    "user": "jeremywest"
}
```

A preimage method for NumberFieldHomomorphism



---

archive/issue_comments_089604.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T00:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89604",
    "user": "jeremywest"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089605.json:
```json
{
    "body": "Attachment\n\nI have implemented the preimage method including documentation and tests. I just need a review now. Let me know if this should go somewhere better.",
    "created_at": "2010-07-02T00:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89605",
    "user": "jeremywest"
}
```

Attachment

I have implemented the preimage method including documentation and tests. I just need a review now. Let me know if this should go somewhere better.



---

archive/issue_comments_089606.json:
```json
{
    "body": "The new patch changes each usage of .vector_space to .absolute_vector_space.\nAlso added a doctest.",
    "created_at": "2010-07-02T04:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89606",
    "user": "ebeyerstedt"
}
```

The new patch changes each usage of .vector_space to .absolute_vector_space.
Also added a doctest.



---

archive/issue_comments_089607.json:
```json
{
    "body": "Replaces previous patch.",
    "created_at": "2010-07-02T05:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89607",
    "user": "ebeyerstedt"
}
```

Replaces previous patch.



---

archive/issue_comments_089608.json:
```json
{
    "body": "Attachment\n\nUpdated documentation.",
    "created_at": "2010-07-02T05:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89608",
    "user": "ebeyerstedt"
}
```

Attachment

Updated documentation.



---

archive/issue_comments_089609.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T17:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89609",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089610.json:
```json
{
    "body": "I changed the error message that is returned when the input is not in the image of the homomorphism so that, rather than a message about solving a matrix equation, it gives a message about the input not being in the image.",
    "created_at": "2010-07-02T19:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89610",
    "user": "jeremywest"
}
```

I changed the error message that is returned when the input is not in the image of the homomorphism so that, rather than a message about solving a matrix equation, it gives a message about the input not being in the image.



---

archive/issue_comments_089611.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-02T19:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89611",
    "user": "davidloeffler"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_089612.json:
```json
{
    "body": "If you really must upload new patches to an already positively reviewed ticket, you *must* put the status back to \"needs review\".",
    "created_at": "2010-07-02T19:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89612",
    "user": "davidloeffler"
}
```

If you really must upload new patches to an already positively reviewed ticket, you *must* put the status back to "needs review".



---

archive/issue_comments_089613.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T19:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89613",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089614.json:
```json
{
    "body": "Attachment\n\nFixes error handling message, replaces all previous patches.",
    "created_at": "2010-07-02T20:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89614",
    "user": "jeremywest"
}
```

Attachment

Fixes error handling message, replaces all previous patches.



---

archive/issue_comments_089615.json:
```json
{
    "body": "David -- can you review the newest patch? If this ticket can get a positive review, then it and #9384 can get into 4.5.2.",
    "created_at": "2010-07-22T23:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89615",
    "user": "ddrake"
}
```

David -- can you review the newest patch? If this ticket can get a positive review, then it and #9384 can get into 4.5.2.



---

archive/issue_comments_089616.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-26T21:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89616",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089617.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-27T00:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89617",
    "user": "ddrake"
}
```

Resolution: fixed



---

archive/issue_comments_089618.json:
```json
{
    "body": "Please include the ticket number in your commit messages! Also, Jeremy, you might want to set your username in your .hgrc file -- your patch has a username of \"jeremy`@`west-imac-8-2007.local\".",
    "created_at": "2010-07-27T00:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89618",
    "user": "ddrake"
}
```

Please include the ticket number in your commit messages! Also, Jeremy, you might want to set your username in your .hgrc file -- your patch has a username of "jeremy`@`west-imac-8-2007.local".



---

archive/issue_comments_089619.json:
```json
{
    "body": "I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.",
    "created_at": "2010-07-27T04:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9403#issuecomment-89619",
    "user": "mpatel"
}
```

I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.
