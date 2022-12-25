# Issue 7976: Extends __classcall__ to control inheritance

archive/issues_007976.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: ClassCall inheritance\n\nThis patch extends `ClasscallMetaclass` so that one can control the call of a class trough two different static methods:\n\n- `__classcall__` which behave as usual and is inherited\n- `__classcall__no_inherits` which is not called by derived classes\n\nIf both exists the latter is used.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7976\n\n",
    "created_at": "2010-01-18T13:03:46Z",
    "labels": [
        "component: categories"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Extends __classcall__ to control inheritance",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7976",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: ClassCall inheritance

This patch extends `ClasscallMetaclass` so that one can control the call of a class trough two different static methods:

- `__classcall__` which behave as usual and is inherited
- `__classcall__no_inherits` which is not called by derived classes

If both exists the latter is used.

Issue created by migration from https://trac.sagemath.org/ticket/7976





---

archive/issue_comments_069460.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T15:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69460",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069461.json:
```json
{
    "body": "Thanks Florent, and thanks for using this occasion to cleanup my code!\n\nCan you fix the copyright dates? Mine should be 2009, and yours 2010\n\nI like the idea of using Python's standard convention for private attributes; on the other hand, I am a bit worried about emulating Python's mechanism. In particular, we could eventually get in trouble with the class name hacking we do for pickling:\n\n```\n   sage: Sets.ParentMethods.__name__\n   'Sets.ParentMethods'\n```\nI haven't found a way to *use* Python mechanism. So instead, what about using ``__classcall_private__``, and doing the test with '__classcall_private__' in cls.__dict__?\n\n(I also prefer ``private`` to ``no_inherit``).\n\nCheers,",
    "created_at": "2010-01-18T22:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69461",
    "user": "https://github.com/nthiery"
}
```

Thanks Florent, and thanks for using this occasion to cleanup my code!

Can you fix the copyright dates? Mine should be 2009, and yours 2010

I like the idea of using Python's standard convention for private attributes; on the other hand, I am a bit worried about emulating Python's mechanism. In particular, we could eventually get in trouble with the class name hacking we do for pickling:

```
   sage: Sets.ParentMethods.__name__
   'Sets.ParentMethods'
```
I haven't found a way to *use* Python mechanism. So instead, what about using ``__classcall_private__``, and doing the test with '__classcall_private__' in cls.__dict__?

(I also prefer ``private`` to ``no_inherit``).

Cheers,



---

archive/issue_comments_069462.json:
```json
{
    "body": "Changing keywords from \"ClassCall inheritance\" to \"ClassCall, inheritance\".",
    "created_at": "2010-01-18T22:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69462",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "ClassCall inheritance" to "ClassCall, inheritance".



---

archive/issue_comments_069463.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-18T22:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69463",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069464.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T05:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69464",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069465.json:
```json
{
    "body": "Replying to [comment:2 nthiery]:\n> Thanks Florent, and thanks for using this occasion to cleanup my code!\n> \n> Can you fix the copyright dates? Mine should be 2009, and yours 2010\n> \n> [...]\n> So instead, what about using ``__classcall_private__``, and doing the test with '__classcall_private__' in cls.__dict__?\n> \n> (I also prefer ``private`` to ``no_inherit``).\n\n\nI just uploaded a new patch which addresses all these remarks... Please re-review.",
    "created_at": "2010-01-19T05:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69465",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:2 nthiery]:
> Thanks Florent, and thanks for using this occasion to cleanup my code!
> 
> Can you fix the copyright dates? Mine should be 2009, and yours 2010
> 
> [...]
> So instead, what about using ``__classcall_private__``, and doing the test with '__classcall_private__' in cls.__dict__?
> 
> (I also prefer ``private`` to ``no_inherit``).


I just uploaded a new patch which addresses all these remarks... Please re-review.



---

archive/issue_comments_069466.json:
```json
{
    "body": "Attachment [trac_7976-classcall_no_inherits-review-nt.patch](tarball://root/attachments/some-uuid/ticket7976/trac_7976-classcall_no_inherits-review-nt.patch) by @nthiery created at 2010-01-19 09:05:06",
    "created_at": "2010-01-19T09:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69466",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7976-classcall_no_inherits-review-nt.patch](tarball://root/attachments/some-uuid/ticket7976/trac_7976-classcall_no_inherits-review-nt.patch) by @nthiery created at 2010-01-19 09:05:06



---

archive/issue_comments_069467.json:
```json
{
    "body": "Please double check the quick review patch, and add '#7976:' in front of the patch description, and it's good to go!",
    "created_at": "2010-01-19T09:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69467",
    "user": "https://github.com/nthiery"
}
```

Please double check the quick review patch, and add '#7976:' in front of the patch description, and it's good to go!



---

archive/issue_events_019084.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2010-01-19T09:07:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7976#event-19084"
}
```



---

archive/issue_comments_069468.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T11:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69468",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069469.json:
```json
{
    "body": "Attachment [trac_7976-classcall_no_inherits-fh.patch](tarball://root/attachments/some-uuid/ticket7976/trac_7976-classcall_no_inherits-fh.patch) by @hivert created at 2010-01-19 11:50:38\n\nReplying to [comment:4 nthiery]:\n> Please double check the quick review patch, and add '#7976:' in front of the patch description, and it's good to go!\n\n\nI added '#7976:' and re-uploaded the patch. Thanks for the improvement of the doc. Your review patch is ok => positive review.",
    "created_at": "2010-01-19T11:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69469",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7976-classcall_no_inherits-fh.patch](tarball://root/attachments/some-uuid/ticket7976/trac_7976-classcall_no_inherits-fh.patch) by @hivert created at 2010-01-19 11:50:38

Replying to [comment:4 nthiery]:
> Please double check the quick review patch, and add '#7976:' in front of the patch description, and it's good to go!


I added '#7976:' and re-uploaded the patch. Thanks for the improvement of the doc. Your review patch is ok => positive review.



---

archive/issue_events_019085.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-22T23:27:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7976#event-19085"
}
```



---

archive/issue_comments_069470.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_7976-classcall_no_inherits-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7976/trac_7976-classcall_no_inherits-fh.patch)\n2. [trac_7976-classcall_no_inherits-review-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7976/trac_7976-classcall_no_inherits-review-nt.patch)",
    "created_at": "2010-01-22T23:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_7976-classcall_no_inherits-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7976/trac_7976-classcall_no_inherits-fh.patch)
2. [trac_7976-classcall_no_inherits-review-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7976/trac_7976-classcall_no_inherits-review-nt.patch)



---

archive/issue_comments_069471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T23:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7976#issuecomment-69471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
