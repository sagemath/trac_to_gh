# Issue 7422: New Incidence Structure and Block Design constructions

archive/issues_007422.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @rbeezer @wdjoyner\n\nKeywords: Block Design, Incidence Structure, Residual, Derived, Complement, Supplement, Point Deletion\n\nI have added two references; fixed the points() method to return points in lexicographic order so __eq__ works properly; made is_simple() its own standalone method and call it from block_design_checker and added the following constructions: Derived at a Point, Residual at a Point, Derived at a Block, Residual at a Block, Complementary, Supplementary, Point Deletion and Extraction of Blocks by size.\n\nSome relevant discussion is here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/305158ab5d3181bc\n\nReviewers:\n\n- Please think about my first item on the TODO list; is that a better way to proceed with derived_blck and residual_blck?\n\n-I do not know whether this is \"Minor\" or \"Major\" (I am pretty sure it is not the others) so I have put \"Major\".  Please tell me if I was wrong.\n\n- I have no idea what to put in Milestone so I have left it blank.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7422\n\n",
    "created_at": "2009-11-10T02:09:23Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "New Incidence Structure and Block Design constructions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7422",
    "user": "@brettpim"
}
```
Assignee: @mwhansen

CC:  @rbeezer @wdjoyner

Keywords: Block Design, Incidence Structure, Residual, Derived, Complement, Supplement, Point Deletion

I have added two references; fixed the points() method to return points in lexicographic order so __eq__ works properly; made is_simple() its own standalone method and call it from block_design_checker and added the following constructions: Derived at a Point, Residual at a Point, Derived at a Block, Residual at a Block, Complementary, Supplementary, Point Deletion and Extraction of Blocks by size.

Some relevant discussion is here:

http://groups.google.com/group/sage-devel/browse_thread/thread/305158ab5d3181bc

Reviewers:

- Please think about my first item on the TODO list; is that a better way to proceed with derived_blck and residual_blck?

-I do not know whether this is "Minor" or "Major" (I am pretty sure it is not the others) so I have put "Major".  Please tell me if I was wrong.

- I have no idea what to put in Milestone so I have left it blank.

Issue created by migration from https://trac.sagemath.org/ticket/7422





---

archive/issue_comments_062462.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-10T02:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62462",
    "user": "@brettpim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062463.json:
```json
{
    "body": "Just a python and Sage style note: unless there is a huge significant reason, things in function names should be spelled out.  So, for example, residual_pt should be residual_point, blck should be \"block\", etc.  This makes a huge difference in readability for someone that is using the module, reading code written by others, etc.",
    "created_at": "2009-11-10T15:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62463",
    "user": "@jasongrout"
}
```

Just a python and Sage style note: unless there is a huge significant reason, things in function names should be spelled out.  So, for example, residual_pt should be residual_point, blck should be "block", etc.  This makes a huge difference in readability for someone that is using the module, reading code written by others, etc.



---

archive/issue_comments_062464.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Just a python and Sage style note: unless there is a huge significant reason, things in function names should be spelled out.  So, for example, residual_pt should be residual_point, blck should be \"block\", etc.  This makes a huge difference in readability for someone that is using the module, reading code written by others, etc.\n\n\nOK, I will make this change, thanks.",
    "created_at": "2009-11-10T17:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62464",
    "user": "@brettpim"
}
```

Replying to [comment:2 jason]:
> Just a python and Sage style note: unless there is a huge significant reason, things in function names should be spelled out.  So, for example, residual_pt should be residual_point, blck should be "block", etc.  This makes a huge difference in readability for someone that is using the module, reading code written by others, etc.


OK, I will make this change, thanks.



---

archive/issue_comments_062465.json:
```json
{
    "body": "Attachment [trac_7422_block_design_constructions.patch](tarball://root/attachments/some-uuid/ticket7422/trac_7422_block_design_constructions.patch) by @brettpim created at 2009-11-14 18:42:17\n\nPatch with new constructions",
    "created_at": "2009-11-14T18:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62465",
    "user": "@brettpim"
}
```

Attachment [trac_7422_block_design_constructions.patch](tarball://root/attachments/some-uuid/ticket7422/trac_7422_block_design_constructions.patch) by @brettpim created at 2009-11-14 18:42:17

Patch with new constructions



---

archive/issue_comments_062466.json:
```json
{
    "body": "I have changed the function names so they are all fully descriptive of what they do.\n\nI also have a question.  When I run:\n\nsage -coverage Projects/SAGE/sage-source/devel/sage/sage/combinat/designs/incidence_structures.py\n\nI do get 100% coverage but I also get:\n\nERROR: Please add a `TestSuite(s).run()` doctest.\n\nI have looked in the sage reference manual and the developers guide to see what this is and how I add such a thing, but to no avail.  If someone knows what this is please tell me or send a link to a page that describes it.  When I know what to do, I will add one of these.",
    "created_at": "2009-11-14T18:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62466",
    "user": "@brettpim"
}
```

I have changed the function names so they are all fully descriptive of what they do.

I also have a question.  When I run:

sage -coverage Projects/SAGE/sage-source/devel/sage/sage/combinat/designs/incidence_structures.py

I do get 100% coverage but I also get:

ERROR: Please add a `TestSuite(s).run()` doctest.

I have looked in the sage reference manual and the developers guide to see what this is and how I add such a thing, but to no avail.  If someone knows what this is please tell me or send a link to a page that describes it.  When I know what to do, I will add one of these.



---

archive/issue_comments_062467.json:
```json
{
    "body": "Here is the patch for adding such a thing to matrices in Sage.  You might find the code useful as an example.\n\n#6936\n\nHere is the ticket that introduced the framework:\n\n#6343\n\nI don't know where this is documented, but there probably is a mailing list message or two about it.",
    "created_at": "2009-11-14T19:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62467",
    "user": "@jasongrout"
}
```

Here is the patch for adding such a thing to matrices in Sage.  You might find the code useful as an example.

#6936

Here is the ticket that introduced the framework:

#6343

I don't know where this is documented, but there probably is a mailing list message or two about it.



---

archive/issue_comments_062468.json:
```json
{
    "body": "Remove assignee @mwhansen.",
    "created_at": "2010-02-21T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62468",
    "user": "drkirkby"
}
```

Remove assignee @mwhansen.



---

archive/issue_comments_062469.json:
```json
{
    "body": "Has this been checked on Solaris?\n\nThere's general information about building on Solaris at\n\n http://wiki.sagemath.org/solaris\n\nInformation specifically for 't2' at\n\n http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\nBoth the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html\n\nDave",
    "created_at": "2010-02-21T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62469",
    "user": "drkirkby"
}
```

Has this been checked on Solaris?

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave



---

archive/issue_comments_062470.json:
```json
{
    "body": "I do not know if this patch is still necessary, but if it is it needs to be rebased.\n\n\n```\n12 out of 12 hunks FAILED -- saving rejects to file sage/combinat/designs/incidence_structures.py.rej\n```\n\n\nNathann",
    "created_at": "2010-05-16T16:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62470",
    "user": "@nathanncohen"
}
```

I do not know if this patch is still necessary, but if it is it needs to be rebased.


```
12 out of 12 hunks FAILED -- saving rejects to file sage/combinat/designs/incidence_structures.py.rej
```


Nathann



---

archive/issue_comments_062471.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-16T16:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62471",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062472.json:
```json
{
    "body": "Set assignee to @brettpim.",
    "created_at": "2015-03-10T02:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62472",
    "user": "@brettpim"
}
```

Set assignee to @brettpim.



---

archive/issue_comments_062473.json:
```json
{
    "body": "`@`brett: here is [1] the procedure to follow if you want to close this ticket. Note that while the doc says that you should switch it to 'needs review'first, we usually directly change the status to 'positive review' in this specific case.\n\nNathann\n\n[1] http://www.sagemath.org/doc/developer/trac.html#reviewing-and-closing-tickets",
    "created_at": "2015-03-10T15:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62473",
    "user": "@nathanncohen"
}
```

`@`brett: here is [1] the procedure to follow if you want to close this ticket. Note that while the doc says that you should switch it to 'needs review'first, we usually directly change the status to 'positive review' in this specific case.

Nathann

[1] http://www.sagemath.org/doc/developer/trac.html#reviewing-and-closing-tickets



---

archive/issue_comments_062474.json:
```json
{
    "body": "This ticket should be closed.  It has been superseded by ticket #16534",
    "created_at": "2015-03-10T15:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62474",
    "user": "@brettpim"
}
```

This ticket should be closed.  It has been superseded by ticket #16534



---

archive/issue_comments_062475.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-03-10T15:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62475",
    "user": "@brettpim"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_062476.json:
```json
{
    "body": "you should also set the milestone to duplicate...",
    "created_at": "2015-03-12T23:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62476",
    "user": "@vbraun"
}
```

you should also set the milestone to duplicate...



---

archive/issue_comments_062477.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-03-12T23:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62477",
    "user": "@vbraun"
}
```

Resolution: duplicate



---

archive/issue_comments_062478.json:
```json
{
    "body": "thanks",
    "created_at": "2015-03-13T03:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7422#issuecomment-62478",
    "user": "@brettpim"
}
```

thanks
