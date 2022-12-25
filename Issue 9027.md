# Issue 9027: Explain Sage and tex interactions in the tutorial

archive/issues_009027.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri mvngu\n\nKeywords: latex\n\nThere are a variety of ways to use latex in Sage, which often leads to some confusion.  This new section of the tutorial will present an overview and the basics of usage from a users perspective.  However, doctests might also help developers understand how to make changes related to various aspects of tex support.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9027\n\n",
    "created_at": "2010-05-24T05:45:32Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Explain Sage and tex interactions in the tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9027",
    "user": "https://github.com/rbeezer"
}
```
Assignee: mvngu

CC:  @jhpalmieri mvngu

Keywords: latex

There are a variety of ways to use latex in Sage, which often leads to some confusion.  This new section of the tutorial will present an overview and the basics of usage from a users perspective.  However, doctests might also help developers understand how to make changes related to various aspects of tex support.

Issue created by migration from https://trac.sagemath.org/ticket/9027





---

archive/issue_comments_083389.json:
```json
{
    "body": "Attachment [trac_9027_tutorial_latex_v1.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v1.patch) by @rbeezer created at 2010-05-24 05:48:10",
    "created_at": "2010-05-24T05:48:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83389",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9027_tutorial_latex_v1.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v1.patch) by @rbeezer created at 2010-05-24 05:48:10



---

archive/issue_comments_083390.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-24T05:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83390",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_083391.json:
```json
{
    "body": "Version 1 patch is incomplete, but should build with just a handful of errors, and contains initial sections followed by a rough outline for contents of subsequent section.",
    "created_at": "2010-05-24T05:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83391",
    "user": "https://github.com/rbeezer"
}
```

Version 1 patch is incomplete, but should build with just a handful of errors, and contains initial sections followed by a rough outline for contents of subsequent section.



---

archive/issue_comments_083392.json:
```json
{
    "body": "Attachment [trac_9027_tutorial_latex_v2.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v2.patch) by @rbeezer created at 2010-05-25 04:33:15\n\nVersion 2 patch has about 80% of the content I'd like to add.  So general comments about direction or scope are welcome.  I'll then be adding the missing sections, filling in doctests, links to methods, etc.",
    "created_at": "2010-05-25T04:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83392",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9027_tutorial_latex_v2.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v2.patch) by @rbeezer created at 2010-05-25 04:33:15

Version 2 patch has about 80% of the content I'd like to add.  So general comments about direction or scope are welcome.  I'll then be adding the missing sections, filling in doctests, links to methods, etc.



---

archive/issue_comments_083393.json:
```json
{
    "body": "Hi Rob,\n\nHere are some comments.  \n\n- Overall, it looks good.  It seems to cover all of the points I would want it to.  I also think it makes sense to include this material in the tutorial.\n\n- In general, make it more clear just how much of this is automatic?  (for example the png conversion discussed at line 237 and nearby)\n\n- how much do we care about consistency between ``\\TeX`` and `tex`, ``\\LaTeX`` and `latex`?\n\ntypos:\n \n- line 7: intensley synergetic --> intensely synergistic\n\n- line 24: constructiing\n\n- line 100: Effecting --> Affecting\n\n- line 173: mathbb?  This might be mathbf unless you use a .. link:: directive to link it to the previous examples.  same issue on lines 183, 188, etc.\n\n- line 235: Typset\n\n- line 240: this class --> This class\n\n- line 240: wwwhat\n\n- line 240: To actual see --> To actually see\n\n- line 262 and following, the sentence starting \"So all of these components need\".  Change to \"So you should make sure that up-to-date versions of these are available\"\n\n- line 311: \"::math\" --> \".. math::\"\n\n- line 318: there is a section in the tutorial on sagetex, so you should refer to that.",
    "created_at": "2010-06-08T04:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83393",
    "user": "https://github.com/jhpalmieri"
}
```

Hi Rob,

Here are some comments.  

- Overall, it looks good.  It seems to cover all of the points I would want it to.  I also think it makes sense to include this material in the tutorial.

- In general, make it more clear just how much of this is automatic?  (for example the png conversion discussed at line 237 and nearby)

- how much do we care about consistency between ``\TeX`` and `tex`, ``\LaTeX`` and `latex`?

typos:
 
- line 7: intensley synergetic --> intensely synergistic

- line 24: constructiing

- line 100: Effecting --> Affecting

- line 173: mathbb?  This might be mathbf unless you use a .. link:: directive to link it to the previous examples.  same issue on lines 183, 188, etc.

- line 235: Typset

- line 240: this class --> This class

- line 240: wwwhat

- line 240: To actual see --> To actually see

- line 262 and following, the sentence starting "So all of these components need".  Change to "So you should make sure that up-to-date versions of these are available"

- line 311: "::math" --> ".. math::"

- line 318: there is a section in the tutorial on sagetex, so you should refer to that.



---

archive/issue_comments_083394.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n\nHi John,\n\nThanks for all the comments, suggestions and fixes.  I'm away doing this Sage workshop this week, but expect to get back to this next week sometime.\n\nRob",
    "created_at": "2010-06-08T12:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83394",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:3 jhpalmieri]:

Hi John,

Thanks for all the comments, suggestions and fixes.  I'm away doing this Sage workshop this week, but expect to get back to this next week sometime.

Rob



---

archive/issue_comments_083395.json:
```json
{
    "body": "Attachment [trac_9027_tutorial_latex_v3.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v3.patch) by @rbeezer created at 2010-06-17 04:49:39",
    "created_at": "2010-06-17T04:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83395",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9027_tutorial_latex_v3.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v3.patch) by @rbeezer created at 2010-06-17 04:49:39



---

archive/issue_comments_083396.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-17T04:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83396",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083397.json:
```json
{
    "body": "Version 3 patch is now ready for review.  This takes into account all of John's comments above, but likely introduces a few new typos (though I'd like to think not).  Two comments:\n\n1.  graphviz otional spkg is broken (#7438) so I can't learn that right now, a section on that could be added later.\n\n2.  I had a tentative section about using TeX in documentation.  I think I might write more for the developer's guide (linking back to this) and I can include the documentation stuff there.  So I dropped that.",
    "created_at": "2010-06-17T04:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83397",
    "user": "https://github.com/rbeezer"
}
```

Version 3 patch is now ready for review.  This takes into account all of John's comments above, but likely introduces a few new typos (though I'd like to think not).  Two comments:

1.  graphviz otional spkg is broken (#7438) so I can't learn that right now, a section on that could be added later.

2.  I had a tentative section about using TeX in documentation.  I think I might write more for the developer's guide (linking back to this) and I can include the documentation stuff there.  So I dropped that.



---

archive/issue_comments_083398.json:
```json
{
    "body": "The most recent patch doesn't apply cleanly, because macros.tex is no longer part of the Sage distribution.\n\nAlso, if you do `sage -docbuild tutorial html -j` to build using jsMath, then jsMath doesn't know about the command `\\LaTeX`, and this causes problems.  I also couldn't get ``\\mbox{\\TeX}`{}shop` to work right, either.  So I'm attaching a reviewer's patch which changes `\\mbox{\\LaTeX}` to the plain-text `LaTeX`, and similarly for `TeX`.  I've also added a few links.",
    "created_at": "2010-06-21T21:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83398",
    "user": "https://github.com/jhpalmieri"
}
```

The most recent patch doesn't apply cleanly, because macros.tex is no longer part of the Sage distribution.

Also, if you do `sage -docbuild tutorial html -j` to build using jsMath, then jsMath doesn't know about the command `\LaTeX`, and this causes problems.  I also couldn't get ``\mbox{\TeX}`{}shop` to work right, either.  So I'm attaching a reviewer's patch which changes `\mbox{\LaTeX}` to the plain-text `LaTeX`, and similarly for `TeX`.  I've also added a few links.



---

archive/issue_comments_083399.json:
```json
{
    "body": "Attachment [trac_9027-reviewer.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027-reviewer.patch) by @jhpalmieri created at 2010-06-21 21:48:09\n\napply on top of v3 patch",
    "created_at": "2010-06-21T21:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83399",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9027-reviewer.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027-reviewer.patch) by @jhpalmieri created at 2010-06-21 21:48:09

apply on top of v3 patch



---

archive/issue_comments_083400.json:
```json
{
    "body": "Oh, there were also a few doctest failures: I think the examples don't get run in order, so the latex preamble was not empty when it was supposed to be, for example.  My patch fixes those (I think).",
    "created_at": "2010-06-21T21:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83400",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, there were also a few doctest failures: I think the examples don't get run in order, so the latex preamble was not empty when it was supposed to be, for example.  My patch fixes those (I think).



---

archive/issue_comments_083401.json:
```json
{
    "body": "See also #9300.  How's your French?",
    "created_at": "2010-06-21T22:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83401",
    "user": "https://github.com/jhpalmieri"
}
```

See also #9300.  How's your French?



---

archive/issue_comments_083402.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> See also #9300.  How's your French?\n\n\nPossibly passable enough to review, but not good enough to create.  ;-)\n\nThanks for the fixes and changes.  I'll look them over soon - busy with out-of-town guests right at the moment.\n\n<joke>\n\nYou know the seasons in the Pacific Northwest, don't you?\n\n10 months of rain and two months of visitors.  ;-)\n\n</joke>",
    "created_at": "2010-06-21T23:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83402",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:8 jhpalmieri]:
> See also #9300.  How's your French?


Possibly passable enough to review, but not good enough to create.  ;-)

Thanks for the fixes and changes.  I'll look them over soon - busy with out-of-town guests right at the moment.

<joke>

You know the seasons in the Pacific Northwest, don't you?

10 months of rain and two months of visitors.  ;-)

</joke>



---

archive/issue_comments_083403.json:
```json
{
    "body": "Stand-alone, apply before reviewer patch",
    "created_at": "2010-07-17T04:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83403",
    "user": "https://github.com/rbeezer"
}
```

Stand-alone, apply before reviewer patch



---

archive/issue_comments_083404.json:
```json
{
    "body": "Attachment [trac_9074-tkz-graph-latex-v4.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9074-tkz-graph-latex-v4.patch) by @rbeezer created at 2010-07-17 05:20:06\n\nApply after reviewer patch",
    "created_at": "2010-07-17T05:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83404",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9074-tkz-graph-latex-v4.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9074-tkz-graph-latex-v4.patch) by @rbeezer created at 2010-07-17 05:20:06

Apply after reviewer patch



---

archive/issue_comments_083405.json:
```json
{
    "body": "Attachment [trac_9027_doctesting.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_doctesting.patch) by @rbeezer created at 2010-07-17 05:40:32\n\nReplying to [comment:7 jhpalmieri]:\n\nv4 patch removes the changes to macros.tex so will now apply cleanly.\n\nreviewer patch looks good to me, so that's a positive review on that.\n\ndoctesting patch makes a few more changes to make random-order doctesting work properly.  The general strategy is to clean-up on finishing a block (rather than always initializing on starting a block).  There are a few report of macros, preamble etc on starting a block, but that is to illustrate, rather than check.\n\nApply three patches in this order:  v4, reviewer, doctesting.  This all applies, builds (documentation) and passes tests (in random order!).  I'll make a mega-patch once final.\n\n> Oh, there were also a few doctest failures: I think the examples don't get run in order, so the latex preamble was not empty when it was supposed to be, for example.  My patch fixes those (I think).",
    "created_at": "2010-07-17T05:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83405",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9027_doctesting.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_doctesting.patch) by @rbeezer created at 2010-07-17 05:40:32

Replying to [comment:7 jhpalmieri]:

v4 patch removes the changes to macros.tex so will now apply cleanly.

reviewer patch looks good to me, so that's a positive review on that.

doctesting patch makes a few more changes to make random-order doctesting work properly.  The general strategy is to clean-up on finishing a block (rather than always initializing on starting a block).  There are a few report of macros, preamble etc on starting a block, but that is to illustrate, rather than check.

Apply three patches in this order:  v4, reviewer, doctesting.  This all applies, builds (documentation) and passes tests (in random order!).  I'll make a mega-patch once final.

> Oh, there were also a few doctest failures: I think the examples don't get run in order, so the latex preamble was not empty when it was supposed to be, for example.  My patch fixes those (I think).



---

archive/issue_comments_083406.json:
```json
{
    "body": "Hi Rob,\n\nIt looks like trac_9074-tkz-graph-latex-v4.patch belongs on #9074 instead of here. Can you move it there?  Is there a new version of the patch for this ticket?",
    "created_at": "2010-07-22T22:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83406",
    "user": "https://github.com/jhpalmieri"
}
```

Hi Rob,

It looks like trac_9074-tkz-graph-latex-v4.patch belongs on #9074 instead of here. Can you move it there?  Is there a new version of the patch for this ticket?



---

archive/issue_comments_083407.json:
```json
{
    "body": "Stand-alone v4 patch, apply before reviewer patch",
    "created_at": "2010-07-22T23:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83407",
    "user": "https://github.com/rbeezer"
}
```

Stand-alone v4 patch, apply before reviewer patch



---

archive/issue_comments_083408.json:
```json
{
    "body": "Attachment [trac_9027_tutorial_latex_v4.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v4.patch) by @rbeezer created at 2010-07-22 23:35:02\n\nReplying to [comment:11 jhpalmieri]:\n> Hi Rob,\n> \n> It looks like trac_9074-tkz-graph-latex-v4.patch belongs on #9074 instead of here. Can you move it there?  Is there a new version of the patch for this ticket?\n\n\nOoh, that's bad.  The #9074 patch is already there where it belongs.  These two v4 patches were next to each other in my local storage, thus......\n\nThe real 9027 v4 patch is here now, sorry for the confusion.  I've never been able to delete files.  Do I need some extra privileges, or can you trash 9074-v4 for me?  Thanks.\n\nRob",
    "created_at": "2010-07-22T23:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83408",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9027_tutorial_latex_v4.patch](tarball://root/attachments/some-uuid/ticket9027/trac_9027_tutorial_latex_v4.patch) by @rbeezer created at 2010-07-22 23:35:02

Replying to [comment:11 jhpalmieri]:
> Hi Rob,
> 
> It looks like trac_9074-tkz-graph-latex-v4.patch belongs on #9074 instead of here. Can you move it there?  Is there a new version of the patch for this ticket?


Ooh, that's bad.  The #9074 patch is already there where it belongs.  These two v4 patches were next to each other in my local storage, thus......

The real 9027 v4 patch is here now, sorry for the confusion.  I've never been able to delete files.  Do I need some extra privileges, or can you trash 9074-v4 for me?  Thanks.

Rob



---

archive/issue_comments_083409.json:
```json
{
    "body": "Looks good to me.\n\nTo the release manager, merge\n\n- trac_9027_tutorial_latex_v4.patch\n- trac_9027-reviewer.patch",
    "created_at": "2010-07-23T03:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83409",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.

To the release manager, merge

- trac_9027_tutorial_latex_v4.patch
- trac_9027-reviewer.patch



---

archive/issue_comments_083410.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T03:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83410",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083411.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83411",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_083412.json:
```json
{
    "body": "Replying to [comment:13 jhpalmieri]:\n> Looks good to me.\n> \n> To the release manager, merge\n> \n> - trac_9027_tutorial_latex_v4.patch\n> - trac_9027-reviewer.patch\n\n\nMerged in 4.5.2.alpha1.",
    "created_at": "2010-07-26T02:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83412",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:13 jhpalmieri]:
> Looks good to me.
> 
> To the release manager, merge
> 
> - trac_9027_tutorial_latex_v4.patch
> - trac_9027-reviewer.patch


Merged in 4.5.2.alpha1.



---

archive/issue_events_022093.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-26T02:17:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9027#event-22093"
}
```



---

archive/issue_comments_083413.json:
```json
{
    "body": "Please see #9607 for a potentially related doctest failure.",
    "created_at": "2010-07-27T07:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9027#issuecomment-83413",
    "user": "https://github.com/qed777"
}
```

Please see #9607 for a potentially related doctest failure.
