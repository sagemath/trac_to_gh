# Issue 2023: dynkin diagram weights

archive/issues_002023.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nI may be misinterpreting something but it seems to me that\nsage: dynkin_diagram(['C',4]).show()\ndoes not display the Dynkin diagram of C_4 correctly.\nThere is a an online generator at http://www-math.mit.edu/~lesha/dynkin-diagrams.html\nwhich indicates the arrow and the long root in that case.\nAlso, there are no examples for that function but the docstring says\n\"Returns a DiGraph corresponding to the Dynkin diagram...\" but the Dynkin \ndiagram is not a digraph, AFAIK.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2023\n\n",
    "created_at": "2008-02-01T04:54:06Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.10",
    "title": "dynkin diagram weights",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2023",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @mwhansen

CC:  sage-combinat

I may be misinterpreting something but it seems to me that
sage: dynkin_diagram(['C',4]).show()
does not display the Dynkin diagram of C_4 correctly.
There is a an online generator at http://www-math.mit.edu/~lesha/dynkin-diagrams.html
which indicates the arrow and the long root in that case.
Also, there are no examples for that function but the docstring says
"Returns a DiGraph corresponding to the Dynkin diagram..." but the Dynkin 
diagram is not a digraph, AFAIK.

Issue created by migration from https://trac.sagemath.org/ticket/2023





---

archive/issue_events_004862.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-01T12:42:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2023#event-4862"
}
```



---

archive/issue_comments_013028.json:
```json
{
    "body": "Mike,\n\nthis has been sitting around for a while. What is the status here?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T07:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13028",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mike,

this has been sitting around for a while. What is the status here?

Cheers,

Michael



---

archive/issue_comments_013029.json:
```json
{
    "body": "It's indeed a bit of an abuse to have Dynkin diagram derive from Digraphs (some edges are not oriented). But they are not Graphs either (some edges are). They don't really deserve a special class graph just for themselves, do they? So, I guess we can live with this abuse.\n\nThat being said, plot should definitely be overriden to get appropriate pictures. Volunteers?\n\nSee also #5502 for ascii art drawing.",
    "created_at": "2009-04-15T16:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13029",
    "user": "https://github.com/nthiery"
}
```

It's indeed a bit of an abuse to have Dynkin diagram derive from Digraphs (some edges are not oriented). But they are not Graphs either (some edges are). They don't really deserve a special class graph just for themselves, do they? So, I guess we can live with this abuse.

That being said, plot should definitely be overriden to get appropriate pictures. Volunteers?

See also #5502 for ascii art drawing.



---

archive/issue_comments_013030.json:
```json
{
    "body": "I've uploaded a patch that gives custom latex printing for Dynkin diagrams for crystallographic types.",
    "created_at": "2013-02-21T17:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13030",
    "user": "https://github.com/tscrim"
}
```

I've uploaded a patch that gives custom latex printing for Dynkin diagrams for crystallographic types.



---

archive/issue_comments_013031.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-21T17:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13031",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013032.json:
```json
{
    "body": "New version which uses the global options framework for notation choices.",
    "created_at": "2013-03-11T15:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13032",
    "user": "https://github.com/tscrim"
}
```

New version which uses the global options framework for notation choices.



---

archive/issue_comments_013033.json:
```json
{
    "body": "Cleaned up some docstrings.",
    "created_at": "2013-03-11T16:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13033",
    "user": "https://github.com/tscrim"
}
```

Cleaned up some docstrings.



---

archive/issue_comments_013034.json:
```json
{
    "body": "Hi Travis,\n\nI pushed a reviewer patch on the queue which makes the logic more concise as we had discussed this morning. Please check my changes and fold them. Due to some changes I undid in my patch, you probably want to have a look at the folded patch, and strip away trivial space changes that could be left due to uncomplete undoes.\n\nI'll then have a final check on the updated patch.\n\nCheers,\n                                     Nicolas",
    "created_at": "2013-04-15T21:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13034",
    "user": "https://github.com/nthiery"
}
```

Hi Travis,

I pushed a reviewer patch on the queue which makes the logic more concise as we had discussed this morning. Please check my changes and fold them. Due to some changes I undid in my patch, you probably want to have a look at the folded patch, and strip away trivial space changes that could be left due to uncomplete undoes.

I'll then have a final check on the updated patch.

Cheers,
                                     Nicolas



---

archive/issue_comments_013035.json:
```json
{
    "body": "Hey Nicolas,\n\nThank you for the review. I had to make some minor tweaks to affine types B,C, and D. However this patch will change depending on what happens in #14248.\n\nThanks,\n\nTravis",
    "created_at": "2013-04-16T13:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13035",
    "user": "https://github.com/tscrim"
}
```

Hey Nicolas,

Thank you for the review. I had to make some minor tweaks to affine types B,C, and D. However this patch will change depending on what happens in #14248.

Thanks,

Travis



---

archive/issue_comments_013036.json:
```json
{
    "body": "Updated with a better note about the conventions used in sage.",
    "created_at": "2013-04-16T17:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13036",
    "user": "https://github.com/tscrim"
}
```

Updated with a better note about the conventions used in sage.



---

archive/issue_comments_013037.json:
```json
{
    "body": "I have just been through the patch, and wrote a little reviewer patch which I just pushed to the Sage-Combinat queue. It sounds good to go assuming all tests pass.\n\nTravis: if you are happy with the reviewer patch, please fold upload and set a positive review on my behalf.",
    "created_at": "2013-05-07T21:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13037",
    "user": "https://github.com/nthiery"
}
```

I have just been through the patch, and wrote a little reviewer patch which I just pushed to the Sage-Combinat queue. It sounds good to go assuming all tests pass.

Travis: if you are happy with the reviewer patch, please fold upload and set a positive review on my behalf.



---

archive/issue_comments_013038.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-07T21:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13038",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013039.json:
```json
{
    "body": "```\ndochtml.log:[combinat ] /mazur/release/merger/sage-5.10.beta3/devel/sage/doc/en/reference/combinat/sage/combinat/root_system/cartan_type.rst:11: WARNING: error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_crystalographic.ascii_art: invalid syntax (<unknown>, line 1)\n```",
    "created_at": "2013-05-08T14:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13039",
    "user": "https://github.com/jdemeyer"
}
```

```
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.beta3/devel/sage/doc/en/reference/combinat/sage/combinat/root_system/cartan_type.rst:11: WARNING: error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_crystalographic.ascii_art: invalid syntax (<unknown>, line 1)
```



---

archive/issue_comments_013040.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-05-08T14:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13040",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_013041.json:
```json
{
    "body": "Sorry, we should have caught that. Worked around in the attached patch. See also #14553.\n\nThe updated patch was checked by Travis. I am running the tests now.",
    "created_at": "2013-05-08T15:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13041",
    "user": "https://github.com/nthiery"
}
```

Sorry, we should have caught that. Worked around in the attached patch. See also #14553.

The updated patch was checked by Travis. I am running the tests now.



---

archive/issue_comments_013042.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-05-08T15:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13042",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013043.json:
```json
{
    "body": "All test passed on sage.math.u-psud.fr and documentation built smoothly:\n\nFor the full logs, see:\n- http://sage.math.washington.edu/home/nthiery/2023-buildlog\n- http://sage.math.washington.edu/home/nthiery/2023-docbuildlog\n- http://sage.math.washington.edu/home/nthiery/2023-testlog",
    "created_at": "2013-05-08T15:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13043",
    "user": "https://github.com/nthiery"
}
```

All test passed on sage.math.u-psud.fr and documentation built smoothly:

For the full logs, see:
- http://sage.math.washington.edu/home/nthiery/2023-buildlog
- http://sage.math.washington.edu/home/nthiery/2023-docbuildlog
- http://sage.math.washington.edu/home/nthiery/2023-testlog



---

archive/issue_comments_013044.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2013-05-08T15:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13044",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_013045.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-08T15:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13045",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013046.json:
```json
{
    "body": "Some doctests are ignored with the new doctest framework, and the framework complains about it with long tests.\n\nSee discussion on:\n\nhttps://groups.google.com/forum/?fromgroups=#!topic/sage-devel/4m1ydGdiGf8",
    "created_at": "2013-05-08T18:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13046",
    "user": "https://github.com/nthiery"
}
```

Some doctests are ignored with the new doctest framework, and the framework complains about it with long tests.

See discussion on:

https://groups.google.com/forum/?fromgroups=#!topic/sage-devel/4m1ydGdiGf8



---

archive/issue_comments_013047.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-05-08T18:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13047",
    "user": "https://github.com/nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_013048.json:
```json
{
    "body": "The new patches contains two little changes we agreed with Travis / on sage-devel:\n\n- Some trailing whitespace in new lines\n- Updating the number of currently ignored tests in doctest/sources\n\nAll long test passed.\n\nBack to positive review!",
    "created_at": "2013-05-09T01:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13048",
    "user": "https://github.com/nthiery"
}
```

The new patches contains two little changes we agreed with Travis / on sage-devel:

- Some trailing whitespace in new lines
- Updating the number of currently ignored tests in doctest/sources

All long test passed.

Back to positive review!



---

archive/issue_comments_013049.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-05-09T01:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13049",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_013050.json:
```json
{
    "body": "Attachment [trac_2023-dynkin_graphs-ts.patch](tarball://root/attachments/some-uuid/ticket2023/trac_2023-dynkin_graphs-ts.patch) by @nthiery created at 2013-05-09 01:41:11\n\nMinor doc tweak",
    "created_at": "2013-05-09T01:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13050",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_2023-dynkin_graphs-ts.patch](tarball://root/attachments/some-uuid/ticket2023/trac_2023-dynkin_graphs-ts.patch) by @nthiery created at 2013-05-09 01:41:11

Minor doc tweak



---

archive/issue_comments_013051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-05-13T13:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2023#issuecomment-13051",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_004863.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-13T13:26:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2023",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2023#event-4863"
}
```
