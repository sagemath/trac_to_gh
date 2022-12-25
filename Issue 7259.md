# Issue 7259: Revert Sets().category() from Sets() to Objects()

archive/issues_007259.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: categories, sets\n\nIn Sage 4.1, the category of a category was changed from Objects() to\nSets(). I.e. we used to have:\n\n  \tsage: Groups().category()\n  \tCategory of objects\n\nAnd now we have:\n\n\tsage: Groups().category()\n\tCategory of sets\n\nThe former sounds more natural to me, in particular because the\nobjects of Sets() are exactly the parents.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7259\n\n",
    "created_at": "2009-10-21T08:36:14Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Revert Sets().category() from Sets() to Objects()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7259",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: categories, sets

In Sage 4.1, the category of a category was changed from Objects() to
Sets(). I.e. we used to have:

  	sage: Groups().category()
  	Category of objects

And now we have:

	sage: Groups().category()
	Category of sets

The former sounds more natural to me, in particular because the
objects of Sets() are exactly the parents.

Issue created by migration from https://trac.sagemath.org/ticket/7259





---

archive/issue_comments_060180.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-21T08:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7259#issuecomment-60180",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060181.json:
```json
{
    "body": "Attachment [trac_7259-revert-category-in-sets.patch](tarball://root/attachments/some-uuid/ticket7259/trac_7259-revert-category-in-sets.patch) by @nthiery created at 2009-10-21 08:42:11",
    "created_at": "2009-10-21T08:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7259#issuecomment-60181",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7259-revert-category-in-sets.patch](tarball://root/attachments/some-uuid/ticket7259/trac_7259-revert-category-in-sets.patch) by @nthiery created at 2009-10-21 08:42:11



---

archive/issue_comments_060182.json:
```json
{
    "body": "For the record, all tests pass with this applied.",
    "created_at": "2009-10-21T13:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7259#issuecomment-60182",
    "user": "https://github.com/mwhansen"
}
```

For the record, all tests pass with this applied.



---

archive/issue_comments_060183.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-23T09:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7259#issuecomment-60183",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060184.json:
```json
{
    "body": "I think this can go in now and then we'll switch it over to the \"Category of Categories\" when appropriate.",
    "created_at": "2009-10-23T09:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7259#issuecomment-60184",
    "user": "https://github.com/mwhansen"
}
```

I think this can go in now and then we'll switch it over to the "Category of Categories" when appropriate.



---

archive/issue_comments_060185.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-23T09:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7259#issuecomment-60185",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017179.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-23T09:11:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7259",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7259#event-17179"
}
```
