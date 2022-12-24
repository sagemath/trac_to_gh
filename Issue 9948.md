# Issue 9948: Add major index (generating polynomial) for the category of finite permutation groups

archive/issues_009948.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat @nthiery\n\nKeywords: major, index, generating, polynomial, permutation\n\nIn the spirit of factorization of the code, add a method major_index for parents/elements inheriting from FinitePrmutationGoups()\n\n\n```\nsage: DihedralGroup(5).major_index()\nq^10 + q^9 + q^8 + q^7 + q^6 + q^4 + q^3 + q^2 + q + 1\nsage: PermutationGroup([[(1,2,3,4,5)]]).major_index()\nq^4 + q^3 + q^2 + q + 1\nsage: SymmetricGroup(3).major_index()\nq^3 + 2*q^2 + 2*q + 1\nsage: TransitiveGroup(5,3).major_index()\nq^10 + q^9 + 2*q^8 + 2*q^7 + 3*q^6 + 2*q^5 + 3*q^4 + 2*q^3 + 2*q^2 + q + 1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9949\n\n",
    "created_at": "2010-09-19T16:49:15Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Add major index (generating polynomial) for the category of finite permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9948",
    "user": "nborie"
}
```
Assignee: nborie

CC:  sage-combinat @nthiery

Keywords: major, index, generating, polynomial, permutation

In the spirit of factorization of the code, add a method major_index for parents/elements inheriting from FinitePrmutationGoups()


```
sage: DihedralGroup(5).major_index()
q^10 + q^9 + q^8 + q^7 + q^6 + q^4 + q^3 + q^2 + q + 1
sage: PermutationGroup([[(1,2,3,4,5)]]).major_index()
q^4 + q^3 + q^2 + q + 1
sage: SymmetricGroup(3).major_index()
q^3 + 2*q^2 + 2*q + 1
sage: TransitiveGroup(5,3).major_index()
q^10 + q^9 + 2*q^8 + 2*q^7 + 3*q^6 + 2*q^5 + 3*q^4 + 2*q^3 + 2*q^2 + q + 1
```


Issue created by migration from https://trac.sagemath.org/ticket/9949





---

archive/issue_comments_099194.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-19T17:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99194",
    "user": "nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099195.json:
```json
{
    "body": "Attachment [trac_9949_major_index_finite_permutation_group-nb.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_finite_permutation_group-nb.patch) by nborie created at 2010-09-19 19:54:10",
    "created_at": "2010-09-19T19:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99195",
    "user": "nborie"
}
```

Attachment [trac_9949_major_index_finite_permutation_group-nb.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_finite_permutation_group-nb.patch) by nborie created at 2010-09-19 19:54:10



---

archive/issue_comments_099196.json:
```json
{
    "body": "Attachment [trac_9949_major_index_finite_permutation_group-review-mh.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_finite_permutation_group-review-mh.patch) by @mwhansen created at 2010-11-26 02:58:52\n\nI've added a review patch which fixes a few minor things.  Other than that, it looks good to me.  Do you want to fold the patches together, put the new one up, and I can give it positive review?",
    "created_at": "2010-11-26T02:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99196",
    "user": "@mwhansen"
}
```

Attachment [trac_9949_major_index_finite_permutation_group-review-mh.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_finite_permutation_group-review-mh.patch) by @mwhansen created at 2010-11-26 02:58:52

I've added a review patch which fixes a few minor things.  Other than that, it looks good to me.  Do you want to fold the patches together, put the new one up, and I can give it positive review?



---

archive/issue_comments_099197.json:
```json
{
    "body": "Yes, I definitely agree with yours corrections. But before finalizing this ticket, we need some informations. Nicolas told me that it is not really reasonable to implement this feature in this category. We don't really know if major index is defined for any Finite Permutation Group. Let's discuss this on sage-combinat-devel.\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/38a0e71e61ca6231\n\nThank you very much Mike for your patch, I also should have open this discussion earlier. Sorry for that...",
    "created_at": "2010-11-28T15:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99197",
    "user": "nborie"
}
```

Yes, I definitely agree with yours corrections. But before finalizing this ticket, we need some informations. Nicolas told me that it is not really reasonable to implement this feature in this category. We don't really know if major index is defined for any Finite Permutation Group. Let's discuss this on sage-combinat-devel.

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/38a0e71e61ca6231

Thank you very much Mike for your patch, I also should have open this discussion earlier. Sorry for that...



---

archive/issue_comments_099198.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-11-28T15:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99198",
    "user": "nborie"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_099199.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-19T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99199",
    "user": "nborie"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_099200.json:
```json
{
    "body": "After discussions, I realized that it is reasonable to define major_index only for the symmetric group. So I moved the method in the proper place. I also integrated all remarks and code corrections from the patch of Mike.\n\nFor Buildbot / reviewer / ... :\n\napply trac_9949_major_index_final-nb.patch\n\nIt is now ready for review.",
    "created_at": "2011-01-19T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99200",
    "user": "nborie"
}
```

After discussions, I realized that it is reasonable to define major_index only for the symmetric group. So I moved the method in the proper place. I also integrated all remarks and code corrections from the patch of Mike.

For Buildbot / reviewer / ... :

apply trac_9949_major_index_final-nb.patch

It is now ready for review.



---

archive/issue_comments_099201.json:
```json
{
    "body": "Hi Nicolas,\n\nIf this only applies to symmetric groups, shouldn't it just return\n\n\n```\nsage.combinat.q_analogues.q_factorial(n)\n```\n\n?\n\nThis would be much more efficient than enumerating over the group.",
    "created_at": "2011-02-02T19:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99201",
    "user": "@jbandlow"
}
```

Hi Nicolas,

If this only applies to symmetric groups, shouldn't it just return


```
sage.combinat.q_analogues.q_factorial(n)
```

?

This would be much more efficient than enumerating over the group.



---

archive/issue_comments_099202.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-02-02T19:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99202",
    "user": "@jbandlow"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_099203.json:
```json
{
    "body": "Hy Jason\n\nYou are definitely right! I didn't know this module about q_analogues. I am going to change it and just make major_cycle point to the right q_analogue. As q_analogues is not imported by default, this ticket will just consist in building a shortcut...\n\nThanks for having regarded this!",
    "created_at": "2011-02-02T20:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99203",
    "user": "nborie"
}
```

Hy Jason

You are definitely right! I didn't know this module about q_analogues. I am going to change it and just make major_cycle point to the right q_analogue. As q_analogues is not imported by default, this ticket will just consist in building a shortcut...

Thanks for having regarded this!



---

archive/issue_comments_099204.json:
```json
{
    "body": "Attachment [trac_9949_major_index_final-nb.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_final-nb.patch) by nborie created at 2011-02-16 17:52:49",
    "created_at": "2011-02-16T17:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99204",
    "user": "nborie"
}
```

Attachment [trac_9949_major_index_final-nb.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_final-nb.patch) by nborie created at 2011-02-16 17:52:49



---

archive/issue_comments_099205.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-02-16T17:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99205",
    "user": "nborie"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_099206.json:
```json
{
    "body": "I update the patch after your last comment Jason. At the end, this method is just a shortcut pointing to the q-analogue of factorial n. As q_analogues are not imported by default and calling SymmetricGroup(n).major_index() seems natural, I think it is good like this.",
    "created_at": "2011-02-16T17:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99206",
    "user": "nborie"
}
```

I update the patch after your last comment Jason. At the end, this method is just a shortcut pointing to the q-analogue of factorial n. As q_analogues are not imported by default and calling SymmetricGroup(n).major_index() seems natural, I think it is good like this.



---

archive/issue_comments_099207.json:
```json
{
    "body": "This looks good.  Thanks, Nicolas.",
    "created_at": "2011-03-14T18:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99207",
    "user": "@jbandlow"
}
```

This looks good.  Thanks, Nicolas.



---

archive/issue_comments_099208.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-14T18:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99208",
    "user": "@jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099209.json:
```json
{
    "body": "Please change the commit message of the patches to something meaningful.  Make sure the ticket number appears on the first line of the commit message.",
    "created_at": "2011-04-07T13:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99209",
    "user": "@jdemeyer"
}
```

Please change the commit message of the patches to something meaningful.  Make sure the ticket number appears on the first line of the commit message.



---

archive/issue_comments_099210.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-07T13:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99210",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_099211.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-04-07T13:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99211",
    "user": "@nthiery"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_099212.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> Please change the commit message of the patches to something meaningful.  Make sure the ticket number appears on the first line of the commit message.\n\nOops, I should have caught this. Fixed!",
    "created_at": "2011-04-07T14:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99212",
    "user": "@nthiery"
}
```

Replying to [comment:10 jdemeyer]:
> Please change the commit message of the patches to something meaningful.  Make sure the ticket number appears on the first line of the commit message.

Oops, I should have caught this. Fixed!



---

archive/issue_comments_099213.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-04-07T14:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99213",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_099214.json:
```json
{
    "body": "May I assume that the description is wrong and that **three** patches need to be applied?",
    "created_at": "2011-04-07T14:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99214",
    "user": "@jdemeyer"
}
```

May I assume that the description is wrong and that **three** patches need to be applied?



---

archive/issue_comments_099215.json:
```json
{
    "body": "Really final version, with ticket number",
    "created_at": "2011-04-07T14:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99215",
    "user": "@nthiery"
}
```

Really final version, with ticket number



---

archive/issue_comments_099216.json:
```json
{
    "body": "Attachment [trac_9949_major_index_really_final-nb.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_really_final-nb.patch) by @nthiery created at 2011-04-07 14:11:52",
    "created_at": "2011-04-07T14:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99216",
    "user": "@nthiery"
}
```

Attachment [trac_9949_major_index_really_final-nb.patch](tarball://root/attachments/some-uuid/ticket9949/trac_9949_major_index_really_final-nb.patch) by @nthiery created at 2011-04-07 14:11:52



---

archive/issue_comments_099217.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-04-07T14:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99217",
    "user": "@nthiery"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_099218.json:
```json
{
    "body": "Replying to [comment:14 jdemeyer]:\n> May I assume that the description is wrong and that **three** patches need to be applied?\n\nSorry, I uploaded the wrong file from the sage-combinat queue, which probably caused the confusion. I confirm that only the advertised patch shall be applied.\n\nThanks!",
    "created_at": "2011-04-07T14:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99218",
    "user": "@nthiery"
}
```

Replying to [comment:14 jdemeyer]:
> May I assume that the description is wrong and that **three** patches need to be applied?

Sorry, I uploaded the wrong file from the sage-combinat queue, which probably caused the confusion. I confirm that only the advertised patch shall be applied.

Thanks!



---

archive/issue_comments_099219.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-07T14:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99219",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099220.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-07T14:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99220",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_099221.json:
```json
{
    "body": "Replying to [comment:16 nthiery]:\n> I confirm that only the advertised patch shall be applied.\n\nThis statement is a non-trivial change to the ticket and needs to be reviewed (since your patch is only a subset of the previous patches).",
    "created_at": "2011-04-07T14:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99221",
    "user": "@jdemeyer"
}
```

Replying to [comment:16 nthiery]:
> I confirm that only the advertised patch shall be applied.

This statement is a non-trivial change to the ticket and needs to be reviewed (since your patch is only a subset of the previous patches).



---

archive/issue_comments_099222.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-07T14:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99222",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099223.json:
```json
{
    "body": "Replying to [comment:18 jdemeyer]:\n> Replying to [comment:16 nthiery]:\n> > I confirm that only the advertised patch shall be applied.\n> \n> This statement is a non-trivial change to the ticket and needs to be reviewed (since your patch is only a subset of the previous patches).\n\nSorry if there is any confusion, but the reduction to a subset dates back from 7 weeks ago, and was already given a positive review by Jason Bandlow. I only changed the patch header from trac_9949_major_index_final-nb.patch. So I think it should be positive review.\n\nDo you mind setting it back if we are now on the same line?",
    "created_at": "2011-04-07T15:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99223",
    "user": "@nthiery"
}
```

Replying to [comment:18 jdemeyer]:
> Replying to [comment:16 nthiery]:
> > I confirm that only the advertised patch shall be applied.
> 
> This statement is a non-trivial change to the ticket and needs to be reviewed (since your patch is only a subset of the previous patches).

Sorry if there is any confusion, but the reduction to a subset dates back from 7 weeks ago, and was already given a positive review by Jason Bandlow. I only changed the patch header from trac_9949_major_index_final-nb.patch. So I think it should be positive review.

Do you mind setting it back if we are now on the same line?



---

archive/issue_comments_099224.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-07T15:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99224",
    "user": "@jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099225.json:
```json
{
    "body": "I confirm that Nicolas Thiery's changes were only to the header of the patch previously given a positive review by me.  I am resetting the status to positive review.  My apologies for missing the incomplete commit message in my first review.",
    "created_at": "2011-04-07T15:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99225",
    "user": "@jbandlow"
}
```

I confirm that Nicolas Thiery's changes were only to the header of the patch previously given a positive review by me.  I am resetting the status to positive review.  My apologies for missing the incomplete commit message in my first review.



---

archive/issue_comments_099226.json:
```json
{
    "body": "To be sure I am clear, the ticket description is correct:\n\nApply only trac_9949_major_index_really_final-nb.patch",
    "created_at": "2011-04-07T15:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99226",
    "user": "@jbandlow"
}
```

To be sure I am clear, the ticket description is correct:

Apply only trac_9949_major_index_really_final-nb.patch



---

archive/issue_comments_099227.json:
```json
{
    "body": "I understand everything now, but bear in mind that it is very important to write in the **ticket description** which patches have to be applied if it's not obvious.  If it weren't for the missing commit message, I would have merged all three patches instead of only the last one (and we would never have known that we did something wrong).",
    "created_at": "2011-04-07T19:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99227",
    "user": "@jdemeyer"
}
```

I understand everything now, but bear in mind that it is very important to write in the **ticket description** which patches have to be applied if it's not obvious.  If it weren't for the missing commit message, I would have merged all three patches instead of only the last one (and we would never have known that we did something wrong).



---

archive/issue_comments_099228.json:
```json
{
    "body": "Sorry for all of that,\n\nIt is a 7 weeks old patch and despite I read sage-devel (and advises in sage-devel like the use of hg qrefresh -e and other patch submitting procedures), I didn't have the reflex of checking all my submitted patch to verify they are conforms. It is not the first time I am making this mistake. Sorry, I will try to be very very conscientious the next time.\n\nAnd I am on the way checking all I already put in trac the last months...\n\nThanks for your help to all of you.",
    "created_at": "2011-04-08T06:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99228",
    "user": "nborie"
}
```

Sorry for all of that,

It is a 7 weeks old patch and despite I read sage-devel (and advises in sage-devel like the use of hg qrefresh -e and other patch submitting procedures), I didn't have the reflex of checking all my submitted patch to verify they are conforms. It is not the first time I am making this mistake. Sorry, I will try to be very very conscientious the next time.

And I am on the way checking all I already put in trac the last months...

Thanks for your help to all of you.



---

archive/issue_comments_099229.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-08T12:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9948#issuecomment-99229",
    "user": "@jdemeyer"
}
```

Resolution: fixed
