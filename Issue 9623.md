# Issue 9623: interacts for high school level

archive/issues_009623.json:
```json
{
    "body": "Assignee: itolkov, jason\n\nCC:  @kcrisman mhampton @robert-marik @rbeezer jthurber\n\nInclude the interacts listed [here](http://groups.google.com/group/sage-edu/browse_thread/thread/2322cf17a710d205) in `$SAGE/devel/sage-main/sage/interacts/...`\n\nIssue created by migration from https://trac.sagemath.org/ticket/9623\n\n",
    "created_at": "2010-07-28T10:41:53Z",
    "labels": [
        "component: interact"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "interacts for high school level",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9623",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: itolkov, jason

CC:  @kcrisman mhampton @robert-marik @rbeezer jthurber

Include the interacts listed [here](http://groups.google.com/group/sage-edu/browse_thread/thread/2322cf17a710d205) in `$SAGE/devel/sage-main/sage/interacts/...`

Issue created by migration from https://trac.sagemath.org/ticket/9623





---

archive/issue_comments_093063.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-28T22:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93063",
    "user": "https://github.com/haraldschilly"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_093064.json:
```json
{
    "body": "Finished porting most of the examples to the sage library. There are some remaining issues:\n\n* `practice_differentiating_polynomials` - mixups with the states happen\n* `trigonometric_properties_triangle` and\n* `special_points` - drawing the items doesn't always work as it should. \n\nIf there is somebody who sees the bug, please correct it ;)\n\nApart from that, they are now conveniently accessible via `interacts.calculus.[TAB]`, `interacts.geometry.[TAB]` and `interacts.statistics.[TAB]`. Maybe I implement some additional ones from the wiki, too... (and it probably doesn't hurt to add a h2 header and some introduction text to each example)",
    "created_at": "2010-07-29T18:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93064",
    "user": "https://github.com/haraldschilly"
}
```

Finished porting most of the examples to the sage library. There are some remaining issues:

* `practice_differentiating_polynomials` - mixups with the states happen
* `trigonometric_properties_triangle` and
* `special_points` - drawing the items doesn't always work as it should. 

If there is somebody who sees the bug, please correct it ;)

Apart from that, they are now conveniently accessible via `interacts.calculus.[TAB]`, `interacts.geometry.[TAB]` and `interacts.statistics.[TAB]`. Maybe I implement some additional ones from the wiki, too... (and it probably doesn't hurt to add a h2 header and some introduction text to each example)



---

archive/issue_comments_093065.json:
```json
{
    "body": "the \"from the wiki\" patch is meant to be applied on top of the \"high school\" patch to keep things separate for now.",
    "created_at": "2010-07-29T18:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93065",
    "user": "https://github.com/haraldschilly"
}
```

the "from the wiki" patch is meant to be applied on top of the "high school" patch to keep things separate for now.



---

archive/issue_comments_093066.json:
```json
{
    "body": "Attachment [9623-interacts-high-school.patch](tarball://root/attachments/some-uuid/ticket9623/9623-interacts-high-school.patch) by @haraldschilly created at 2010-07-30 16:29:27",
    "created_at": "2010-07-30T16:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93066",
    "user": "https://github.com/haraldschilly"
}
```

Attachment [9623-interacts-high-school.patch](tarball://root/attachments/some-uuid/ticket9623/9623-interacts-high-school.patch) by @haraldschilly created at 2010-07-30 16:29:27



---

archive/issue_comments_093067.json:
```json
{
    "body": "Attachment [9623-from-the-wiki.patch](tarball://root/attachments/some-uuid/ticket9623/9623-from-the-wiki.patch) by @haraldschilly created at 2010-07-30 16:29:36",
    "created_at": "2010-07-30T16:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93067",
    "user": "https://github.com/haraldschilly"
}
```

Attachment [9623-from-the-wiki.patch](tarball://root/attachments/some-uuid/ticket9623/9623-from-the-wiki.patch) by @haraldschilly created at 2010-07-30 16:29:36



---

archive/issue_comments_093068.json:
```json
{
    "body": "I know that `practice_differentiating_polynomials` is buggy and that a few more comments in the generated output of each example to explain what it is all about won't hurt, but I call it finished for now and I will not add more examples. Maybe a reviewer finds the bug or donates some additional words?",
    "created_at": "2010-07-30T16:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93068",
    "user": "https://github.com/haraldschilly"
}
```

I know that `practice_differentiating_polynomials` is buggy and that a few more comments in the generated output of each example to explain what it is all about won't hurt, but I call it finished for now and I will not add more examples. Maybe a reviewer finds the bug or donates some additional words?



---

archive/issue_comments_093069.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-30T16:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93069",
    "user": "https://github.com/haraldschilly"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093070.json:
```json
{
    "body": "Attachment [9623-interact-examples.patch](tarball://root/attachments/some-uuid/ticket9623/9623-interact-examples.patch) by @haraldschilly created at 2010-07-31 13:21:59",
    "created_at": "2010-07-31T13:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93070",
    "user": "https://github.com/haraldschilly"
}
```

Attachment [9623-interact-examples.patch](tarball://root/attachments/some-uuid/ticket9623/9623-interact-examples.patch) by @haraldschilly created at 2010-07-31 13:21:59



---

archive/issue_comments_093071.json:
```json
{
    "body": "I've added a short introduction and a pointer to these interacts in the reference manual. `9623-interact-examples.patch` combines both patches and the other ones can be removed.",
    "created_at": "2010-07-31T13:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93071",
    "user": "https://github.com/haraldschilly"
}
```

I've added a short introduction and a pointer to these interacts in the reference manual. `9623-interact-examples.patch` combines both patches and the other ones can be removed.



---

archive/issue_comments_093072.json:
```json
{
    "body": "Thanks for nice patch, I'll look at it. First ideas: practice_differentiating_polynomials does not work as expected, so I think that it could be removed. \n\nI think that it is better to enter limits from keyboard for trapezoidal and Simpson integration rather than input from slider. I also think that it is better to use html.table in Newton method and it is worth to include option which puts computation fot trapezoidal and Simposon integration in a table. Also newton_method and secant method should have similar input forms (presicion is negative power of ten in one of the interacts and positive in the other). \n\nIn the integrals, dx should be TeX-ed as \\mathrm{d}x\n\nI am collecting these ideas and include then in a reviewer patch which comes (hope) in few days.",
    "created_at": "2010-08-16T10:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93072",
    "user": "https://github.com/robert-marik"
}
```

Thanks for nice patch, I'll look at it. First ideas: practice_differentiating_polynomials does not work as expected, so I think that it could be removed. 

I think that it is better to enter limits from keyboard for trapezoidal and Simpson integration rather than input from slider. I also think that it is better to use html.table in Newton method and it is worth to include option which puts computation fot trapezoidal and Simposon integration in a table. Also newton_method and secant method should have similar input forms (presicion is negative power of ten in one of the interacts and positive in the other). 

In the integrals, dx should be TeX-ed as \mathrm{d}x

I am collecting these ideas and include then in a reviewer patch which comes (hope) in few days.



---

archive/issue_comments_093073.json:
```json
{
    "body": "Replying to [comment:9 robert.marik]:\n> practice_differentiating_polynomials does not work as expected\n\nI know, it's something odd about the state transitions and I just did not have enough patience ...\n\n> \n> I think that it is better to enter limits from keyboard for trapezoidal and Simpson integration rather than input from slider.\n\nOk, well, I like the range slider better. It's a matter of taste but the reason for that is that I tried to make it as intuitive as possible and that includes using mouse handles than having to type in numbers.\n\nI'm fine with your other comments.",
    "created_at": "2010-08-16T10:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93073",
    "user": "https://github.com/haraldschilly"
}
```

Replying to [comment:9 robert.marik]:
> practice_differentiating_polynomials does not work as expected

I know, it's something odd about the state transitions and I just did not have enough patience ...

> 
> I think that it is better to enter limits from keyboard for trapezoidal and Simpson integration rather than input from slider.

Ok, well, I like the range slider better. It's a matter of taste but the reason for that is that I tried to make it as intuitive as possible and that includes using mouse handles than having to type in numbers.

I'm fine with your other comments.



---

archive/issue_comments_093074.json:
```json
{
    "body": "Replying to [comment:10 schilly]:\n> \n> Ok, well, I like the range slider better. \n\nOn the other hand, with sliders you cannot integrate from 0 to 1. I changed the interacts for trapezoidal and simpson rule and they accept both input from slider and keyboard. I hope, this is intuitive enough. \n\nI tested all interacts and give a positive review (removed practice_differentiating_polynomials which does not work as expected)\n\nAdded interact for bisection, since it is close to secant method and newton method.\n\nAdded interact for definition of Riemann integral, which is close to trapezoidal rule and Simpson formula, removed. \n\nFixed one deprecation warning. Added titles to (most) of the interacts. Added tables for computation related to Simpson and trapezoidal rule.\n\nPositive review for 9623-interact-examples.patch! Thank you for the patch. I wonder if the layout parameter in interact can be used also with library_interact.\n\nI included reviewer patch in 9623-interact-examples2.patch. Could you or someone else review my changes?",
    "created_at": "2010-08-17T14:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93074",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:10 schilly]:
> 
> Ok, well, I like the range slider better. 

On the other hand, with sliders you cannot integrate from 0 to 1. I changed the interacts for trapezoidal and simpson rule and they accept both input from slider and keyboard. I hope, this is intuitive enough. 

I tested all interacts and give a positive review (removed practice_differentiating_polynomials which does not work as expected)

Added interact for bisection, since it is close to secant method and newton method.

Added interact for definition of Riemann integral, which is close to trapezoidal rule and Simpson formula, removed. 

Fixed one deprecation warning. Added titles to (most) of the interacts. Added tables for computation related to Simpson and trapezoidal rule.

Positive review for 9623-interact-examples.patch! Thank you for the patch. I wonder if the layout parameter in interact can be used also with library_interact.

I included reviewer patch in 9623-interact-examples2.patch. Could you or someone else review my changes?



---

archive/issue_comments_093075.json:
```json
{
    "body": "apply after 9623-interact-examples.patch",
    "created_at": "2010-08-17T14:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93075",
    "user": "https://github.com/robert-marik"
}
```

apply after 9623-interact-examples.patch



---

archive/issue_comments_093076.json:
```json
{
    "body": "Attachment [9623-interact-examples2.patch](tarball://root/attachments/some-uuid/ticket9623/9623-interact-examples2.patch) by @robert-marik created at 2010-08-17 14:08:04\n\nBtw: The interact for riemann integral is a part of work which has been supported by the grant 131/2010 of the [FRV\u0160](http://www.frvs.cz/)\n\nKnown problem for trapezoidal and simpson integration: bad rendering of the computation if we integrate negative function: minus sign follows dot or plus sign.",
    "created_at": "2010-08-17T14:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93076",
    "user": "https://github.com/robert-marik"
}
```

Attachment [9623-interact-examples2.patch](tarball://root/attachments/some-uuid/ticket9623/9623-interact-examples2.patch) by @robert-marik created at 2010-08-17 14:08:04

Btw: The interact for riemann integral is a part of work which has been supported by the grant 131/2010 of the [FRVŠ](http://www.frvs.cz/)

Known problem for trapezoidal and simpson integration: bad rendering of the computation if we integrate negative function: minus sign follows dot or plus sign.



---

archive/issue_comments_093077.json:
```json
{
    "body": "Some comments:\n\n* several typos and nicer latex symbols---see patch\n* `interacts.library.cube_hemisphere()` -- the cube corners do not touch the hemisphere, so I'm confused what the picture is supposed to be.\n* `interacts.library.coin()` -- Again, I'm confused about what the picture should be.  The code looks like it is plotting `[(i,k/i) for i in num_points random numbers]`.  I'm not sure what the y-axis is supposed to represent, given that there is no documentation.\n* `function_tool` -- you can have a button selected in each row, which looks really weird.  This is a problem with interacts, and should be another ticket.",
    "created_at": "2010-09-28T14:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93077",
    "user": "https://github.com/jasongrout"
}
```

Some comments:

* several typos and nicer latex symbols---see patch
* `interacts.library.cube_hemisphere()` -- the cube corners do not touch the hemisphere, so I'm confused what the picture is supposed to be.
* `interacts.library.coin()` -- Again, I'm confused about what the picture should be.  The code looks like it is plotting `[(i,k/i) for i in num_points random numbers]`.  I'm not sure what the y-axis is supposed to represent, given that there is no documentation.
* `function_tool` -- you can have a button selected in each row, which looks really weird.  This is a problem with interacts, and should be another ticket.



---

archive/issue_comments_093078.json:
```json
{
    "body": "Try again:\n\n\n\nSome comments:\n\n* several typos and nicer latex symbols---see patch \n\n* `interacts.library.cube_hemisphere()` -- the cube corners do not touch the hemisphere, as the docs indicate that they should\n  \n* `interacts.library.coin()` -- Again, I'm confused about what the picture should be. The code looks like it is plotting `[(i,k/i) for i in num_points random numbers]`. I'm not sure what the y-axis is supposed to represent, given that there is no documentation. I think the fix is to add documentation\n\n* (for another ticket) `function_tool` -- you can have a button selected in each row, which looks really weird. This is a problem with interacts, and should be another ticket.",
    "created_at": "2010-09-28T14:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93078",
    "user": "https://github.com/jasongrout"
}
```

Try again:



Some comments:

* several typos and nicer latex symbols---see patch 

* `interacts.library.cube_hemisphere()` -- the cube corners do not touch the hemisphere, as the docs indicate that they should
  
* `interacts.library.coin()` -- Again, I'm confused about what the picture should be. The code looks like it is plotting `[(i,k/i) for i in num_points random numbers]`. I'm not sure what the y-axis is supposed to represent, given that there is no documentation. I think the fix is to add documentation

* (for another ticket) `function_tool` -- you can have a button selected in each row, which looks really weird. This is a problem with interacts, and should be another ticket.



---

archive/issue_comments_093079.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2010-09-28T14:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93079",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_093080.json:
```json
{
    "body": "Attachment [9623-reviewer2.patch](tarball://root/attachments/some-uuid/ticket9623/9623-reviewer2.patch) by @jasongrout created at 2010-09-28 14:53:38\n\nRobert's changes look good.  Can someone comment on points 2 and 3 in my list above?",
    "created_at": "2010-09-28T14:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93080",
    "user": "https://github.com/jasongrout"
}
```

Attachment [9623-reviewer2.patch](tarball://root/attachments/some-uuid/ticket9623/9623-reviewer2.patch) by @jasongrout created at 2010-09-28 14:53:38

Robert's changes look good.  Can someone comment on points 2 and 3 in my list above?



---

archive/issue_comments_093081.json:
```json
{
    "body": "Rebases all previous patches against 4.6.1 and makes minor import changes",
    "created_at": "2011-01-12T23:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Rebases all previous patches against 4.6.1 and makes minor import changes



---

archive/issue_comments_093082.json:
```json
{
    "body": "Attachment [trac_9623_rebase_and_import_change.patch](tarball://root/attachments/some-uuid/ticket9623/trac_9623_rebase_and_import_change.patch) by mhampton created at 2011-01-12 23:10:26\n\nRather than let this bit-rot I would like to see it go in soon.  There are endless tweaks and improvements that can be made to these but it would be nice to have this much included.\n\nI removed the __init__.py and replaced it with an all.py that avoids importing everything in the library.py file, which leaves the autocompletion options of interacts much less cluttered.",
    "created_at": "2011-01-12T23:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_9623_rebase_and_import_change.patch](tarball://root/attachments/some-uuid/ticket9623/trac_9623_rebase_and_import_change.patch) by mhampton created at 2011-01-12 23:10:26

Rather than let this bit-rot I would like to see it go in soon.  There are endless tweaks and improvements that can be made to these but it would be nice to have this much included.

I removed the __init__.py and replaced it with an all.py that avoids importing everything in the library.py file, which leaves the autocompletion options of interacts much less cluttered.



---

archive/issue_comments_093083.json:
```json
{
    "body": "Adding the *original* author!  It only seems fair, even if she didn't commit a patch.\n\nAlso, did we ever get the issue about how these are doctested figured out?\n\nFinally, there is at least one place where I see the word 'intergral' :)  Though I wouldn't hold up positive review for that, since I am not formally reviewing (yet).",
    "created_at": "2011-01-13T01:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93083",
    "user": "https://github.com/kcrisman"
}
```

Adding the *original* author!  It only seems fair, even if she didn't commit a patch.

Also, did we ever get the issue about how these are doctested figured out?

Finally, there is at least one place where I see the word 'intergral' :)  Though I wouldn't hold up positive review for that, since I am not formally reviewing (yet).



---

archive/issue_comments_093084.json:
```json
{
    "body": "Karl, I did fix that spelling mistake.  I'll continue to improve these until this is reviewed (but I would be happy if that was very soon!).",
    "created_at": "2011-01-13T18:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Karl, I did fix that spelling mistake.  I'll continue to improve these until this is reviewed (but I would be happy if that was very soon!).



---

archive/issue_comments_093085.json:
```json
{
    "body": "Apply only this patch; using Jason's idea from #10622",
    "created_at": "2011-01-13T19:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Apply only this patch; using Jason's idea from #10622



---

archive/issue_comments_093086.json:
```json
{
    "body": "Attachment [trac_9623_rebase_and_import_change_v2.patch](tarball://root/attachments/some-uuid/ticket9623/trac_9623_rebase_and_import_change_v2.patch) by @kcrisman created at 2011-01-13 19:12:48\n\nAgreed on the quick reviewing need.  I wish I weren't looking at these things just for five minutes each time, but I haven't had a stretch of time for proper reviewing yet.\n> Also, did we ever get the issue about how these are doctested figured out?\nI can't remember where this was, and searching for it online proves to be a nightmare of unrelated hits.   I'm going to email Jason about this.",
    "created_at": "2011-01-13T19:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93086",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9623_rebase_and_import_change_v2.patch](tarball://root/attachments/some-uuid/ticket9623/trac_9623_rebase_and_import_change_v2.patch) by @kcrisman created at 2011-01-13 19:12:48

Agreed on the quick reviewing need.  I wish I weren't looking at these things just for five minutes each time, but I haven't had a stretch of time for proper reviewing yet.
> Also, did we ever get the issue about how these are doctested figured out?
I can't remember where this was, and searching for it online proves to be a nightmare of unrelated hits.   I'm going to email Jason about this.



---

archive/issue_comments_093087.json:
```json
{
    "body": "No, I don't think we ever had any conclusion about doctesting them.",
    "created_at": "2011-01-13T21:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93087",
    "user": "https://github.com/jasongrout"
}
```

No, I don't think we ever had any conclusion about doctesting them.



---

archive/issue_comments_093088.json:
```json
{
    "body": "I've done a modest review, applying the patch, running tests on the sage/interacts, and looking at a few of the interacts in the notebook.  So far, all is good.\n\nUnless someone is doing it sooner, I'll run --testall --long tonight.",
    "created_at": "2011-01-13T23:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93088",
    "user": "https://trac.sagemath.org/admin/accounts/users/jthurber"
}
```

I've done a modest review, applying the patch, running tests on the sage/interacts, and looking at a few of the interacts in the notebook.  So far, all is good.

Unless someone is doing it sooner, I'll run --testall --long tonight.



---

archive/issue_events_023981.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/jthurber",
    "created_at": "2011-01-13T23:09:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9623#event-23981"
}
```



---

archive/issue_events_023982.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2011-01-13T23:11:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9623#event-23982"
}
```



---

archive/issue_events_023983.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2011-01-13T23:11:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9623#event-23983"
}
```



---

archive/issue_comments_093089.json:
```json
{
    "body": "Replying to [comment:20 jason]:\n> No, I don't think we ever had any conclusion about doctesting them.\nOkay, then I would say a prerequisite for positive review is opening a ticket for figuring out what to do about that.  Do you (or anyone else) have any objections to incorporating this nonetheless?  I think it's far more useful than whatever bitrot may occur in the interacts themselves over time, to be honest, and at least provides a nice place to put them all.",
    "created_at": "2011-01-14T01:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93089",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:20 jason]:
> No, I don't think we ever had any conclusion about doctesting them.
Okay, then I would say a prerequisite for positive review is opening a ticket for figuring out what to do about that.  Do you (or anyone else) have any objections to incorporating this nonetheless?  I think it's far more useful than whatever bitrot may occur in the interacts themselves over time, to be honest, and at least provides a nice place to put them all.



---

archive/issue_comments_093090.json:
```json
{
    "body": "I've done the standard testing against the new release of 4.6.1, and all pass, but I'm inclined to step back and leave the status change to those of you who have been more involved with this one.  I joined in because Marshall brought it up at bugdays, but some of you may have more vested in it.  \n\nPerhaps new tickets should be opened to address Jason's points about cube.hemisphere() and coin().\nThe hemisphere picture is disconcerting, adding documentation to coin() would be easy.",
    "created_at": "2011-01-15T14:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93090",
    "user": "https://trac.sagemath.org/admin/accounts/users/jthurber"
}
```

I've done the standard testing against the new release of 4.6.1, and all pass, but I'm inclined to step back and leave the status change to those of you who have been more involved with this one.  I joined in because Marshall brought it up at bugdays, but some of you may have more vested in it.  

Perhaps new tickets should be opened to address Jason's points about cube.hemisphere() and coin().
The hemisphere picture is disconcerting, adding documentation to coin() would be easy.



---

archive/issue_comments_093091.json:
```json
{
    "body": "I'm fine with getting this in and opening up other tickets to address the small number of points I raised.",
    "created_at": "2011-01-15T20:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93091",
    "user": "https://github.com/jasongrout"
}
```

I'm fine with getting this in and opening up other tickets to address the small number of points I raised.



---

archive/issue_comments_093092.json:
```json
{
    "body": "Actually, maybe the best thing to do is put the hemisphere and coin interacts on another ticket, and let everything else go in.  That would be better than contributing interacts that clearly need work.",
    "created_at": "2011-01-15T20:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93092",
    "user": "https://github.com/jasongrout"
}
```

Actually, maybe the best thing to do is put the hemisphere and coin interacts on another ticket, and let everything else go in.  That would be better than contributing interacts that clearly need work.



---

archive/issue_comments_093093.json:
```json
{
    "body": "Replying to [comment:26 jason]:\n> Actually, maybe the best thing to do is put the hemisphere and coin interacts on another ticket, and let everything else go in.  That would be better than contributing interacts that clearly need work.\nOkay, if someone else doesn't, I'll try to take care of that tonight.  We certainly want the interacts in the library to be top-notch.",
    "created_at": "2011-01-15T20:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93093",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:26 jason]:
> Actually, maybe the best thing to do is put the hemisphere and coin interacts on another ticket, and let everything else go in.  That would be better than contributing interacts that clearly need work.
Okay, if someone else doesn't, I'll try to take care of that tonight.  We certainly want the interacts in the library to be top-notch.



---

archive/issue_comments_093094.json:
```json
{
    "body": "Getting rid of the hemisphere and coin interacts sounds good to me.  I like the coin one, thought it was totally self-explanatory, but clearly I'm in the minority.",
    "created_at": "2011-01-15T20:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Getting rid of the hemisphere and coin interacts sounds good to me.  I like the coin one, thought it was totally self-explanatory, but clearly I'm in the minority.



---

archive/issue_comments_093095.json:
```json
{
    "body": "Replying to [comment:28 mhampton]:\n> Getting rid of the hemisphere and coin interacts sounds good to me.  I like the coin one, thought it was totally self-explanatory, but clearly I'm in the minority.\n\nI agree in that I can think of only one interpretation for the y-axis.  Explaining what it must be could be a good exercise when using it.",
    "created_at": "2011-01-15T21:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93095",
    "user": "https://trac.sagemath.org/admin/accounts/users/jthurber"
}
```

Replying to [comment:28 mhampton]:
> Getting rid of the hemisphere and coin interacts sounds good to me.  I like the coin one, thought it was totally self-explanatory, but clearly I'm in the minority.

I agree in that I can think of only one interpretation for the y-axis.  Explaining what it must be could be a good exercise when using it.



---

archive/issue_comments_093096.json:
```json
{
    "body": "I am really glad I looked at these.  In general, they are really nice, and ready for prime time - and SO much easier to use than sifting through the wiki!\n\nBut oh my goodness... SO many minor things that still had to be taken care of.  I apologize for not creating a new diff - I had already started making the changes quite a bit when I realized I should have just made a reviewer patch.  I tried to make the commit message maximally informative, though.  There is already too much stuff on here to try to avoid the patch bomb; in retrospect, we should have added these a little more incrementally so as to avoid this situation.\n\nSo, **very** unfortunately, I must still ask for review on this.  There are too many changes.  **BUT** I feel like many of them are ones which would have impacted the professionalism pretty significantly.   Read on.\n\nThings I fixed:\n\n* We needed to import `fast_callable` for the Julia set one, for whatever reason.\n\n* I removed the hemisphere, tried to improve the wording of the coin as well as I could - it's a nice example, in fact.\n\n* Many formatting things, $, ticks in doc, confusing wording, bad parenthesis in label of difference quotient, etc.\n\n* Fixed bad thing in function tool where deprecation warning appeared because of `f(x*a)`-type stuff in the code.\n\n* The two formulas on the Simpson one were on top of each other in Safari (not FF).  Since the author used the equals sign incorrectly in any case, I added some words to clarify it was an approximation, and that fixed it.  I think Safari may not like math without words between math (see below for another possible example).  Same on trapezoid.\n\n*  In fact, the entire \"Area\" line in the trigonometry one was gone on Safari, probably because of `\\text`, which I removed.  Also note the triangle was called `A`, not `ABC` as it should have been.\n\nPS - I love the fact you can sage -b while the notebook is still running.  This would have been impossible otherwise.\n\nThings I did not fix:\n\n* Really annoying thing where using these seems to reset my worksheet every so often - I mean it just stops and returns me to the top.  This could be because I had the worksheet open in FF and Safari at the same time.  (?)\n\n* Annoying thing that I could not access the documentation for an interact in the notebook once I had already viewed that particular interact.   This might be a general interact bug.\n\n* I could not easily figure out how to get this in the reference manual; I think I have to create a new directory and a .rst file that will somehow autogenerate, but I don't know how to do this (though I'm sure it's easy).  The original patch of Harald's did not work for me.\n\n* Polar prime spiral consistently complains about failing to evaluate the function at various points.  I had no idea how to fix this, since there are so many functions I couldn't easily identify which one wasn't evaluating, though perhaps it's one of the parametric plots (makes most sense).\n\n* Trig properties angle and circle and text ALL fail to format properly in Safari (not FF). \n\n* The unit circle one should somehow have formatted `pi`, but I still don't know how to do that.\n\n* Julia set thing doesn't zoom when you zoom, unless you zoom a lot.  Instead it just cuts off the picture for the zoom area.  Maybe it needs a simultaneous plot point uppage?  Incidentally, this one could REALLY use an 'update' button.\n\n* Julia and Mandelbrot ones look kind of sad compared to easy-to-download apps available nowadays, even at max plot points.  I suppose this is the limit of what we can do with an interact of this kind.\n\n* Some of these definitely need a teacher to interpret for someone who is brand new to things.  That's not a bug, but worth pointing out, especially if there is a way to get these in the reference manual.  For instance, the trig on a triangle one is a little weird, because you're putting points on a unit circle labeled by degree.  Okay, but then there are still tick marks labeled on the axes!  So we're sending a mixed - and weird - message with that.  Not a game-stopper, but still somewhat rough.\n \n* Quad. Eq. one stacks a little too close in the formatting even in the opening gambit.\n\n* Some of the graphers need more flexible ranges.  I'm not sure how to do this conceptually, though, since we have to hardcode something in with the interacts, and too big a range will make it too hard to zoom.  I guess my point is these are not universal.\n \n* Trapezoid and simpson didn't always immediately respond to the 'from keyboard' change.  Maybe you have to click that first, before doing any keyboard changes, or it doesn't like it?\n\n* To me, trig isn't calculus, but I'm not arguing that it can show up there, so I left that one in both calculus and geometry.\n\nSo tickets that should be opened after someone (*please*! unless I missed something) gives this positive review:\n\n* Fixing the problem with buttons in multiple rows Jason mentioned.\n \n* Putting the hemisphere plot back in, if we want to.\n\n* Polar prime spiral plot point issue.\n \n* Figure out how to get this in the manual\n\n* Figuring out how to truly doctest them.  For instance, there could at least be a search for deprecation warnings, or even random input typed... but at least more than just checking that an html block is formed.",
    "created_at": "2011-01-16T05:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93096",
    "user": "https://github.com/kcrisman"
}
```

I am really glad I looked at these.  In general, they are really nice, and ready for prime time - and SO much easier to use than sifting through the wiki!

But oh my goodness... SO many minor things that still had to be taken care of.  I apologize for not creating a new diff - I had already started making the changes quite a bit when I realized I should have just made a reviewer patch.  I tried to make the commit message maximally informative, though.  There is already too much stuff on here to try to avoid the patch bomb; in retrospect, we should have added these a little more incrementally so as to avoid this situation.

So, **very** unfortunately, I must still ask for review on this.  There are too many changes.  **BUT** I feel like many of them are ones which would have impacted the professionalism pretty significantly.   Read on.

Things I fixed:

* We needed to import `fast_callable` for the Julia set one, for whatever reason.

* I removed the hemisphere, tried to improve the wording of the coin as well as I could - it's a nice example, in fact.

* Many formatting things, $, ticks in doc, confusing wording, bad parenthesis in label of difference quotient, etc.

* Fixed bad thing in function tool where deprecation warning appeared because of `f(x*a)`-type stuff in the code.

* The two formulas on the Simpson one were on top of each other in Safari (not FF).  Since the author used the equals sign incorrectly in any case, I added some words to clarify it was an approximation, and that fixed it.  I think Safari may not like math without words between math (see below for another possible example).  Same on trapezoid.

*  In fact, the entire "Area" line in the trigonometry one was gone on Safari, probably because of `\text`, which I removed.  Also note the triangle was called `A`, not `ABC` as it should have been.

PS - I love the fact you can sage -b while the notebook is still running.  This would have been impossible otherwise.

Things I did not fix:

* Really annoying thing where using these seems to reset my worksheet every so often - I mean it just stops and returns me to the top.  This could be because I had the worksheet open in FF and Safari at the same time.  (?)

* Annoying thing that I could not access the documentation for an interact in the notebook once I had already viewed that particular interact.   This might be a general interact bug.

* I could not easily figure out how to get this in the reference manual; I think I have to create a new directory and a .rst file that will somehow autogenerate, but I don't know how to do this (though I'm sure it's easy).  The original patch of Harald's did not work for me.

* Polar prime spiral consistently complains about failing to evaluate the function at various points.  I had no idea how to fix this, since there are so many functions I couldn't easily identify which one wasn't evaluating, though perhaps it's one of the parametric plots (makes most sense).

* Trig properties angle and circle and text ALL fail to format properly in Safari (not FF). 

* The unit circle one should somehow have formatted `pi`, but I still don't know how to do that.

* Julia set thing doesn't zoom when you zoom, unless you zoom a lot.  Instead it just cuts off the picture for the zoom area.  Maybe it needs a simultaneous plot point uppage?  Incidentally, this one could REALLY use an 'update' button.

* Julia and Mandelbrot ones look kind of sad compared to easy-to-download apps available nowadays, even at max plot points.  I suppose this is the limit of what we can do with an interact of this kind.

* Some of these definitely need a teacher to interpret for someone who is brand new to things.  That's not a bug, but worth pointing out, especially if there is a way to get these in the reference manual.  For instance, the trig on a triangle one is a little weird, because you're putting points on a unit circle labeled by degree.  Okay, but then there are still tick marks labeled on the axes!  So we're sending a mixed - and weird - message with that.  Not a game-stopper, but still somewhat rough.
 
* Quad. Eq. one stacks a little too close in the formatting even in the opening gambit.

* Some of the graphers need more flexible ranges.  I'm not sure how to do this conceptually, though, since we have to hardcode something in with the interacts, and too big a range will make it too hard to zoom.  I guess my point is these are not universal.
 
* Trapezoid and simpson didn't always immediately respond to the 'from keyboard' change.  Maybe you have to click that first, before doing any keyboard changes, or it doesn't like it?

* To me, trig isn't calculus, but I'm not arguing that it can show up there, so I left that one in both calculus and geometry.

So tickets that should be opened after someone (*please*! unless I missed something) gives this positive review:

* Fixing the problem with buttons in multiple rows Jason mentioned.
 
* Putting the hemisphere plot back in, if we want to.

* Polar prime spiral plot point issue.
 
* Figure out how to get this in the manual

* Figuring out how to truly doctest them.  For instance, there could at least be a search for deprecation warnings, or even random input typed... but at least more than just checking that an html block is formed.



---

archive/issue_comments_093097.json:
```json
{
    "body": "Based to 4.6.2.alpha0, should apply ok",
    "created_at": "2011-01-16T05:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93097",
    "user": "https://github.com/kcrisman"
}
```

Based to 4.6.2.alpha0, should apply ok



---

archive/issue_comments_093098.json:
```json
{
    "body": "Attachment [trac_9623-rebase-v3.patch](tarball://root/attachments/some-uuid/ticket9623/trac_9623-rebase-v3.patch) by @kcrisman created at 2011-01-16 05:19:38\n\nBuildbot may apply only trac_9623-rebase-v3.patch if it so chooses.",
    "created_at": "2011-01-16T05:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93098",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9623-rebase-v3.patch](tarball://root/attachments/some-uuid/ticket9623/trac_9623-rebase-v3.patch) by @kcrisman created at 2011-01-16 05:19:38

Buildbot may apply only trac_9623-rebase-v3.patch if it so chooses.



---

archive/issue_comments_093099.json:
```json
{
    "body": "Still applies to 4.6.2.alpha4.  I'm tempted to give it positive review myself to avoid bitrot; if I wouldn't have had to rebase a fair amount, I would have just made a reviewer patch, but that was hard for me to do.",
    "created_at": "2011-02-14T19:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93099",
    "user": "https://github.com/kcrisman"
}
```

Still applies to 4.6.2.alpha4.  I'm tempted to give it positive review myself to avoid bitrot; if I wouldn't have had to rebase a fair amount, I would have just made a reviewer patch, but that was hard for me to do.



---

archive/issue_comments_093100.json:
```json
{
    "body": "This still applies OK to sage-4.7.alpha2.  My inclination is to let this in, with all its faults, and incrementally improve through more tickets.  From that standpoint, not showing up in the reference manual might be a good thing in the short term.",
    "created_at": "2011-03-29T03:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This still applies OK to sage-4.7.alpha2.  My inclination is to let this in, with all its faults, and incrementally improve through more tickets.  From that standpoint, not showing up in the reference manual might be a good thing in the short term.



---

archive/issue_comments_093101.json:
```json
{
    "body": "Replying to [comment:33 mhampton]:\n> This still applies OK to sage-4.7.alpha2.  My inclination is to let this in, with all its faults, and incrementally improve through more tickets.  From that standpoint, not showing up in the reference manual might be a good thing in the short term.  \n\nI just needed someone to review my changes - I agree totally!  I just had to make the most needed changes, and there were enough that I didn't feel comfortable giving positive review.\n\nSo if you think it's fine, do positive review!  Please feel free to open all these followup tickets too :)",
    "created_at": "2011-03-29T13:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93101",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:33 mhampton]:
> This still applies OK to sage-4.7.alpha2.  My inclination is to let this in, with all its faults, and incrementally improve through more tickets.  From that standpoint, not showing up in the reference manual might be a good thing in the short term.  

I just needed someone to review my changes - I agree totally!  I just had to make the most needed changes, and there were enough that I didn't feel comfortable giving positive review.

So if you think it's fine, do positive review!  Please feel free to open all these followup tickets too :)



---

archive/issue_comments_093102.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-29T13:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093103.json:
```json
{
    "body": "OK.  Lets do it then.",
    "created_at": "2011-03-29T13:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK.  Lets do it then.



---

archive/issue_comments_093104.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-12T08:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93104",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093105.json:
```json
{
    "body": "Additional patch",
    "created_at": "2011-04-12T08:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93105",
    "user": "https://github.com/jdemeyer"
}
```

Additional patch



---

archive/issue_comments_093106.json:
```json
{
    "body": "Attachment [9623_copyright.patch](tarball://root/attachments/some-uuid/ticket9623/9623_copyright.patch) by @jdemeyer created at 2011-04-12 08:29:48",
    "created_at": "2011-04-12T08:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93106",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9623_copyright.patch](tarball://root/attachments/some-uuid/ticket9623/9623_copyright.patch) by @jdemeyer created at 2011-04-12 08:29:48



---

archive/issue_comments_093107.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-12T08:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93107",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093108.json:
```json
{
    "body": "<rant>\n\nThis is an example of the kind of not-really-necessary thing that really delays tickets.  When it was written, it was 2010!\n\n</rant>\n\nBut now that you did it, I will have to say 'needs work'.  Although Harald put it in writing, since Lauri Ruotsalainen is the one who came up with many of these in her thesis, it seems inappropriate to not put her in the author listing at the top where you added Harald.   So at least something like `based on work by ...` should be added there.",
    "created_at": "2011-04-12T12:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93108",
    "user": "https://github.com/kcrisman"
}
```

<rant>

This is an example of the kind of not-really-necessary thing that really delays tickets.  When it was written, it was 2010!

</rant>

But now that you did it, I will have to say 'needs work'.  Although Harald put it in writing, since Lauri Ruotsalainen is the one who came up with many of these in her thesis, it seems inappropriate to not put her in the author listing at the top where you added Harald.   So at least something like `based on work by ...` should be added there.



---

archive/issue_comments_093109.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-12T12:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93109",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093110.json:
```json
{
    "body": "Replying to [comment:40 kcrisman]:\n> This is an example of the kind of not-really-necessary thing that really delays tickets.  When it was written, it was 2010!\n\nNote that changing the year was only a trivial change, I made the headers compliant with the developers manual [http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files)",
    "created_at": "2011-04-12T12:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93110",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:40 kcrisman]:
> This is an example of the kind of not-really-necessary thing that really delays tickets.  When it was written, it was 2010!

Note that changing the year was only a trivial change, I made the headers compliant with the developers manual [http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files)



---

archive/issue_events_023984.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-25T18:17:37Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9623#event-23984"
}
```



---

archive/issue_events_023985.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-25T18:17:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9623#event-23985"
}
```



---

archive/issue_comments_093111.json:
```json
{
    "body": "Anyone wants to fix this????",
    "created_at": "2011-04-25T18:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93111",
    "user": "https://github.com/jdemeyer"
}
```

Anyone wants to fix this????



---

archive/issue_comments_093112.json:
```json
{
    "body": "Yes, but it's just tedious enough (for me, because I'm very non-automated and still am a novice with queues) that it isn't as high a priority.   Is there any way you can just merge the previous material and move the copyright patch, with the request to add Ruotsalainen, on another ticket?  I feel like that would be much more productive, and actually rather easier for me (or someone else) to fix easily.",
    "created_at": "2011-04-25T19:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93112",
    "user": "https://github.com/kcrisman"
}
```

Yes, but it's just tedious enough (for me, because I'm very non-automated and still am a novice with queues) that it isn't as high a priority.   Is there any way you can just merge the previous material and move the copyright patch, with the request to add Ruotsalainen, on another ticket?  I feel like that would be much more productive, and actually rather easier for me (or someone else) to fix easily.



---

archive/issue_comments_093113.json:
```json
{
    "body": "Added \"partially based on work by Lauri Ruotsalainen\"",
    "created_at": "2011-04-26T12:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93113",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Added "partially based on work by Lauri Ruotsalainen"



---

archive/issue_comments_093114.json:
```json
{
    "body": "Attachment [9623_copyright_v2.patch](tarball://root/attachments/some-uuid/ticket9623/9623_copyright_v2.patch) by mhampton created at 2011-04-26 12:11:15\n\nI updated the copyright patch to reflect the contributions of Lauri Ruotsalainen.  I can change it if someone objects.",
    "created_at": "2011-04-26T12:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93114",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [9623_copyright_v2.patch](tarball://root/attachments/some-uuid/ticket9623/9623_copyright_v2.patch) by mhampton created at 2011-04-26 12:11:15

I updated the copyright patch to reflect the contributions of Lauri Ruotsalainen.  I can change it if someone objects.



---

archive/issue_comments_093115.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-26T12:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93115",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093116.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-26T14:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93116",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093117.json:
```json
{
    "body": "This seems reasonable enough; Harald did do the actual turning into a Sage file.  Thanks, Marshall.    \n\nI assume that is positive review of Jeroen's changes, and I don't think such a trivial change (in terms of code) that Marshall just made needs other review.  They aren't in the reference manual yet, so nothing needed there.  Passes tests.  Positive review!",
    "created_at": "2011-04-26T14:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93117",
    "user": "https://github.com/kcrisman"
}
```

This seems reasonable enough; Harald did do the actual turning into a Sage file.  Thanks, Marshall.    

I assume that is positive review of Jeroen's changes, and I don't think such a trivial change (in terms of code) that Marshall just made needs other review.  They aren't in the reference manual yet, so nothing needed there.  Passes tests.  Positive review!



---

archive/issue_events_023986.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-03T12:28:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9623#event-23986"
}
```



---

archive/issue_comments_093118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-03T12:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93118",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_093119.json:
```json
{
    "body": "A question for anyone who contributed to this ticket: the file `library_cython.pyx` has this code in it:\n\n```\ncpdef cellular(rule, int N):\n    '''\n    Cythonized helper function for the callular_automata fractal.\n    Yields a matrix showing the evolution of a Wolfram's cellular automaton.\n    Based on work by Pablo Angulo.\n    http://wiki.sagemath.org/interact/misc#CellularAutomata\n    \n    INPUT:\n\n        - `rule` -- determines how a cell's value is updated, depending on its neighbors\n        - `N` -- number of iterations\n\n    TESTS::\n\n        sage: from sage.interacts.library_cython import cellular\n        sage: rule = [1, 0, 1, 0, 0, 1, 1, 0]\n        sage: N = 3\n        sage: print cellular(rule, 3)\n\n    '''\n```\n\nNote that the output from the last line of the doctest is missing.  Since the docstring is enclosed in triple single quotes instead of triple double quotes, doctesting skipped this altogether.  At #8708, there is a patch which will now run doctests within triple single quotes, in which case this file has one failure.\n\nSo the question is: what is the output supposed to be?  When I run this command, I get\n\n```\n        sage: print cellular(rule, 3)\n        [[0 0 0 1 0 0 0]\n         [0 0 0 1 0 0 0]\n         [0 1 0 1 0 1 0]]\n```\n\nIs this right?  I don't know what the mathematics here is trying to do, so I really have no idea...",
    "created_at": "2011-09-29T05:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93119",
    "user": "https://github.com/jhpalmieri"
}
```

A question for anyone who contributed to this ticket: the file `library_cython.pyx` has this code in it:

```
cpdef cellular(rule, int N):
    '''
    Cythonized helper function for the callular_automata fractal.
    Yields a matrix showing the evolution of a Wolfram's cellular automaton.
    Based on work by Pablo Angulo.
    http://wiki.sagemath.org/interact/misc#CellularAutomata
    
    INPUT:

        - `rule` -- determines how a cell's value is updated, depending on its neighbors
        - `N` -- number of iterations

    TESTS::

        sage: from sage.interacts.library_cython import cellular
        sage: rule = [1, 0, 1, 0, 0, 1, 1, 0]
        sage: N = 3
        sage: print cellular(rule, 3)

    '''
```

Note that the output from the last line of the doctest is missing.  Since the docstring is enclosed in triple single quotes instead of triple double quotes, doctesting skipped this altogether.  At #8708, there is a patch which will now run doctests within triple single quotes, in which case this file has one failure.

So the question is: what is the output supposed to be?  When I run this command, I get

```
        sage: print cellular(rule, 3)
        [[0 0 0 1 0 0 0]
         [0 0 0 1 0 0 0]
         [0 1 0 1 0 1 0]]
```

Is this right?  I don't know what the mathematics here is trying to do, so I really have no idea...



---

archive/issue_comments_093120.json:
```json
{
    "body": "There's also a typo - \"callular\" isn't an adjective I'm familiar with in Wolfram's work :)  And `N` is not actually used in the rule.\n\nSee [this MathWorld site](http://mathworld.wolfram.com/ElementaryCellularAutomaton.html) for the descriptions.  The rule is given by binary, so this rule is `2+4+32+128=166`.  It looks like there is in fact an error; I'm having a lot of trouble getting the rules to do what they should with things like rules 1 or 2.  \n\nHere's the problem:\n\n```\n        for k in range(N-j, N+j+1):\n```\n\ninstead of \n\n```\n for k in range(0,2*N):\n```\n\nas on the wiki.  Someone thought they'd be smart and only update the cells that \"need\" updating... but that totally screws it up, as ALL cells might need updating if e.g. the rule has the final binary digit = 1.  \n\nI'm opening a ticket for this.  Thanks a lot for catching this, John.",
    "created_at": "2011-09-29T13:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93120",
    "user": "https://github.com/kcrisman"
}
```

There's also a typo - "callular" isn't an adjective I'm familiar with in Wolfram's work :)  And `N` is not actually used in the rule.

See [this MathWorld site](http://mathworld.wolfram.com/ElementaryCellularAutomaton.html) for the descriptions.  The rule is given by binary, so this rule is `2+4+32+128=166`.  It looks like there is in fact an error; I'm having a lot of trouble getting the rules to do what they should with things like rules 1 or 2.  

Here's the problem:

```
        for k in range(N-j, N+j+1):
```

instead of 

```
 for k in range(0,2*N):
```

as on the wiki.  Someone thought they'd be smart and only update the cells that "need" updating... but that totally screws it up, as ALL cells might need updating if e.g. the rule has the final binary digit = 1.  

I'm opening a ticket for this.  Thanks a lot for catching this, John.



---

archive/issue_comments_093121.json:
```json
{
    "body": "This is now #11871.  John, if you want that ticket to \"fix\" the quoting issue as well, you can put that there; if it doesn't matter because of #8708, then no matter.",
    "created_at": "2011-09-29T13:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93121",
    "user": "https://github.com/kcrisman"
}
```

This is now #11871.  John, if you want that ticket to "fix" the quoting issue as well, you can put that there; if it doesn't matter because of #8708, then no matter.



---

archive/issue_comments_093122.json:
```json
{
    "body": "Replying to [comment:30 kcrisman]:\n>  * Polar prime spiral plot point issue.\n\nSee #22665 for a follow-up on this.",
    "created_at": "2017-03-21T13:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93122",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:30 kcrisman]:
>  * Polar prime spiral plot point issue.

See #22665 for a follow-up on this.



---

archive/issue_comments_093123.json:
```json
{
    "body": "Replying to [comment:30 kcrisman]:\n>  * Figuring out how to truly doctest them.  For instance, there could at least be a search for deprecation warnings, or even random input typed... but at least more than just checking that an html block is formed.\n\nSee #22644 for some real tests using Jupyter.",
    "created_at": "2017-03-21T13:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9623#issuecomment-93123",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:30 kcrisman]:
>  * Figuring out how to truly doctest them.  For instance, there could at least be a search for deprecation warnings, or even random input typed... but at least more than just checking that an html block is formed.

See #22644 for some real tests using Jupyter.
