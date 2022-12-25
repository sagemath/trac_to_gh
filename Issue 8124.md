# Issue 8124: Selmer groups for number fields

archive/issues_008124.json:
```json
{
    "body": "Assignee: @loefflerd\n\nI forgot to include this function in my big S-units and S-class groups patch.\n\nI've tested on my laptop and on sage.math, so I think this passes on 32 and 64 bit systems.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8124\n\n",
    "created_at": "2010-01-29T21:04:44Z",
    "labels": [
        "component: number fields"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Selmer groups for number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8124",
    "user": "https://github.com/rlmill"
}
```
Assignee: @loefflerd

I forgot to include this function in my big S-units and S-class groups patch.

I've tested on my laptop and on sage.math, so I think this passes on 32 and 64 bit systems.

Issue created by migration from https://trac.sagemath.org/ticket/8124





---

archive/issue_comments_071298.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-29T21:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71298",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071299.json:
```json
{
    "body": "Would it be much more work to make this function to give back a finite abelian group ? In the long run, we should make sure that these sort of functions return groups. It may be better to try get the correct type from the beginning as not to break later things that use it.\n\n(Sorry to be criticising this again. I think you are doing a great job implementing all these things.)",
    "created_at": "2010-01-31T01:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71299",
    "user": "https://github.com/categorie"
}
```

Would it be much more work to make this function to give back a finite abelian group ? In the long run, we should make sure that these sort of functions return groups. It may be better to try get the correct type from the beginning as not to break later things that use it.

(Sorry to be criticising this again. I think you are doing a great job implementing all these things.)



---

archive/issue_comments_071300.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T17:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71300",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071301.json:
```json
{
    "body": "Looks good;  tests pass.  Building the docs (reference html) revealed a problem in polynomial_quotient_ring.py, preexisting in the selmer_group function:  the macro \"\\cross\" was not recognised.  I could not get \"\\times\" to work instead (which is what I normally use for this) but * does, so I put that in.\n\nRegarding Chris's comment:  of course I agree, this should be a proper abelian group.  But even making it a semi-functional abelian group of the sort used for unit groups and class groups would require quite a bit of extra work, since this code finds generators but _not_ the group structure.  So I think that should be in another ticket.  (For example, I would like to use this function for m=4 and will try to do so.  In that case there will in general be generators of order 2 as well as some of order 4.)",
    "created_at": "2010-01-31T17:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71301",
    "user": "https://github.com/JohnCremona"
}
```

Looks good;  tests pass.  Building the docs (reference html) revealed a problem in polynomial_quotient_ring.py, preexisting in the selmer_group function:  the macro "\cross" was not recognised.  I could not get "\times" to work instead (which is what I normally use for this) but * does, so I put that in.

Regarding Chris's comment:  of course I agree, this should be a proper abelian group.  But even making it a semi-functional abelian group of the sort used for unit groups and class groups would require quite a bit of extra work, since this code finds generators but _not_ the group structure.  So I think that should be in another ticket.  (For example, I would like to use this function for m=4 and will try to do so.  In that case there will in general be generators of order 2 as well as some of order 4.)



---

archive/issue_comments_071302.json:
```json
{
    "body": "Ok, I see and I also understand that this less costly function should be available even if we had selmer_groups given as abelian groups. Maybe a renaming to selmer_group_gens() would be adequate then we can use it later and add later selmer_group without having to change the type return by a function.\n\nBut I won't oppose the positive review on this ticket, of course.",
    "created_at": "2010-01-31T18:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71302",
    "user": "https://github.com/categorie"
}
```

Ok, I see and I also understand that this less costly function should be available even if we had selmer_groups given as abelian groups. Maybe a renaming to selmer_group_gens() would be adequate then we can use it later and add later selmer_group without having to change the type return by a function.

But I won't oppose the positive review on this ticket, of course.



---

archive/issue_comments_071303.json:
```json
{
    "body": "It looks like someone has already fixed the issue John's patch here fixes, so the release manager should merge the original patch.\n\nIf there are no objections, I will remove the second patch.",
    "created_at": "2010-02-04T19:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71303",
    "user": "https://github.com/rlmill"
}
```

It looks like someone has already fixed the issue John's patch here fixes, so the release manager should merge the original patch.

If there are no objections, I will remove the second patch.



---

archive/issue_comments_071304.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> I could not get \"\\times\" to work instead (which is what I normally use for this) but * does, so I put that in.\n\nActually, it looks like someone changed this to `\\times` in rc0, so I've updated the patch to change `\\times` instead of `\\cross` to `*`.",
    "created_at": "2010-02-04T19:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71304",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:3 cremona]:
> I could not get "\times" to work instead (which is what I normally use for this) but * does, so I put that in.

Actually, it looks like someone changed this to `\times` in rc0, so I've updated the patch to change `\times` instead of `\cross` to `*`.



---

archive/issue_comments_071305.json:
```json
{
    "body": "Replaces previous (fixes latex glitch)",
    "created_at": "2010-02-04T19:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71305",
    "user": "https://github.com/rlmill"
}
```

Replaces previous (fixes latex glitch)



---

archive/issue_comments_071306.json:
```json
{
    "body": "Attachment [trac_8124-selmer-nf.review.patch](tarball://root/attachments/some-uuid/ticket8124/trac_8124-selmer-nf.review.patch) by @JohnCremona created at 2010-02-04 20:00:41\n\nPatch  trac_8124-selmer-nf.review.patch applies fine to 4.3.2.alpha1 and tests pass and doc build ok!\n\nThe tag was already at review, and I'm happy to leave it there.",
    "created_at": "2010-02-04T20:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71306",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8124-selmer-nf.review.patch](tarball://root/attachments/some-uuid/ticket8124/trac_8124-selmer-nf.review.patch) by @JohnCremona created at 2010-02-04 20:00:41

Patch  trac_8124-selmer-nf.review.patch applies fine to 4.3.2.alpha1 and tests pass and doc build ok!

The tag was already at review, and I'm happy to leave it there.



---

archive/issue_comments_071307.json:
```json
{
    "body": "Replying to [comment:7 cremona]:\n> Patch  trac_8124-selmer-nf.review.patch applies fine to 4.3.2.alpha1 and tests pass and doc build ok!\n> \n> The tag was already at review, and I'm happy to leave it there.\n\nThat should have said \"positive review\".\n\nI checked that this applies fine to 4.3.2 + #8184 spkg & patches + #8155 patches;  all tests pass (on 64-bit).",
    "created_at": "2010-02-06T17:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71307",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:7 cremona]:
> Patch  trac_8124-selmer-nf.review.patch applies fine to 4.3.2.alpha1 and tests pass and doc build ok!
> 
> The tag was already at review, and I'm happy to leave it there.

That should have said "positive review".

I checked that this applies fine to 4.3.2 + #8184 spkg & patches + #8155 patches;  all tests pass (on 64-bit).



---

archive/issue_comments_071308.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8124#issuecomment-71308",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019458.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T14:31:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8124",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8124#event-19458"
}
```
