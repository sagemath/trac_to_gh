# Issue 5918: bring doctest coverage for posets to 100%

archive/issues_005918.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\nI'll post a patch in a few minutes that brings the doctest coverage for posets to 100% (well, except for 2 or 3 nested functions). It also fixes a few bugs that I noticed while adding the doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5918\n\n",
    "created_at": "2009-04-28T14:29:56Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "bring doctest coverage for posets to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5918",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat

I'll post a patch in a few minutes that brings the doctest coverage for posets to 100% (well, except for 2 or 3 nested functions). It also fixes a few bugs that I noticed while adding the doctests.

Issue created by migration from https://trac.sagemath.org/ticket/5918





---

archive/issue_comments_046678.json:
```json
{
    "body": "Attachment [trac_5918.patch](tarball://root/attachments/some-uuid/ticket5918/trac_5918.patch) by @saliola created at 2009-04-28 14:40:24",
    "created_at": "2009-04-28T14:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46678",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_5918.patch](tarball://root/attachments/some-uuid/ticket5918/trac_5918.patch) by @saliola created at 2009-04-28 14:40:24



---

archive/issue_comments_046679.json:
```json
{
    "body": "The patch fails to apply to Sage 3.4.2.alpha0:\n\n```\napplying /Users/palmieri/Downloads/trac_5918.patch\npatching file sage/combinat/posets/poset_examples.py\nHunk #2 FAILED at 164\n1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/posets/poset_examples.py.rej\npatching file sage/combinat/posets/posets.py\nHunk #12 FAILED at 547\n1 out of 48 hunks FAILED -- saving rejects to file sage/combinat/posets/posets.py.rej\nabort: patch failed to apply\n```\n\n(I was hoping that this patch would fix #5280 and/or #5283, but after applying the rejects by hand, I saw that it didn't.  I'll let someone else do a proper review once there is a rebased patch.)",
    "created_at": "2009-04-28T16:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46679",
    "user": "https://github.com/jhpalmieri"
}
```

The patch fails to apply to Sage 3.4.2.alpha0:

```
applying /Users/palmieri/Downloads/trac_5918.patch
patching file sage/combinat/posets/poset_examples.py
Hunk #2 FAILED at 164
1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/posets/poset_examples.py.rej
patching file sage/combinat/posets/posets.py
Hunk #12 FAILED at 547
1 out of 48 hunks FAILED -- saving rejects to file sage/combinat/posets/posets.py.rej
abort: patch failed to apply
```

(I was hoping that this patch would fix #5280 and/or #5283, but after applying the rejects by hand, I saw that it didn't.  I'll let someone else do a proper review once there is a rebased patch.)



---

archive/issue_comments_046680.json:
```json
{
    "body": "Hello John,\n\nThanks for taking a look at this. I'm aware of the other issues, and this patch does not deal with them. (It does deal with the issues in the email you posted to the sage-combinat list some time ago.) I decided to wait to fix those issues using a different patch, so not to put too much into this patch. (I'm planning to have the others fixed soon.)\n\nI'll rebase and post an updated patch in a few hours (I have to upgrade...).",
    "created_at": "2009-04-28T17:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46680",
    "user": "https://github.com/saliola"
}
```

Hello John,

Thanks for taking a look at this. I'm aware of the other issues, and this patch does not deal with them. (It does deal with the issues in the email you posted to the sage-combinat list some time ago.) I decided to wait to fix those issues using a different patch, so not to put too much into this patch. (I'm planning to have the others fixed soon.)

I'll rebase and post an updated patch in a few hours (I have to upgrade...).



---

archive/issue_comments_046681.json:
```json
{
    "body": "rebased to 3.4.2.alpha0 (apply only this patch)",
    "created_at": "2009-04-28T20:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46681",
    "user": "https://github.com/saliola"
}
```

rebased to 3.4.2.alpha0 (apply only this patch)



---

archive/issue_comments_046682.json:
```json
{
    "body": "Attachment [trac_5918-rebased.patch](tarball://root/attachments/some-uuid/ticket5918/trac_5918-rebased.patch) by @saliola created at 2009-04-28 20:13:34",
    "created_at": "2009-04-28T20:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46682",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_5918-rebased.patch](tarball://root/attachments/some-uuid/ticket5918/trac_5918-rebased.patch) by @saliola created at 2009-04-28 20:13:34



---

archive/issue_comments_046683.json:
```json
{
    "body": "I'm going to upload a patch which corrects a bunch of typos and formatting bits. I do have a couple comments:\n\n* before, the definitions for order ideal and filter were both obviously wrong. I corrected the definition and took the liberty of rewriting it; please check those.\n* you need a blank line between `EXAMPLES::}} (or {{{TEST::`) and the first line of the doctest; otherwise, the documentation doesn't get typeset correctly.\n* doing ``M\\\"obius`` doesn't work; it automatically uses LaTeX in math mode, and gets messed up. For now I just removed the backticks. (If we add a utf-8 encoding declaration, you can use the umlaut and everything works, but for now, the official rule is that Sage library code is 7-bit clean.)\n\nAlso. there seems to be a lot of duplication between posets.py and hasse_diagram.py. This makes fixing documentation hard, since you have to fix things in two places. Is it possible to somehow combine this stuff so code and documentation doesn't need to be copied? (I'm asking this of everyone, not necessarily Franco.)\n\nI don't have time for this now, but it would be nice to add cross-references: you can do stuff like \"`...see :func:`coolfunction()` for...`\" and get automatically linked cross-references.\n\nFinally, this does raise coverage to (basically) 100% and passes all doctests. I'm glad to see this!",
    "created_at": "2009-04-29T09:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46683",
    "user": "https://github.com/dandrake"
}
```

I'm going to upload a patch which corrects a bunch of typos and formatting bits. I do have a couple comments:

* before, the definitions for order ideal and filter were both obviously wrong. I corrected the definition and took the liberty of rewriting it; please check those.
* you need a blank line between `EXAMPLES::}} (or {{{TEST::`) and the first line of the doctest; otherwise, the documentation doesn't get typeset correctly.
* doing ``M\"obius`` doesn't work; it automatically uses LaTeX in math mode, and gets messed up. For now I just removed the backticks. (If we add a utf-8 encoding declaration, you can use the umlaut and everything works, but for now, the official rule is that Sage library code is 7-bit clean.)

Also. there seems to be a lot of duplication between posets.py and hasse_diagram.py. This makes fixing documentation hard, since you have to fix things in two places. Is it possible to somehow combine this stuff so code and documentation doesn't need to be copied? (I'm asking this of everyone, not necessarily Franco.)

I don't have time for this now, but it would be nice to add cross-references: you can do stuff like "`...see :func:`coolfunction()` for...`" and get automatically linked cross-references.

Finally, this does raise coverage to (basically) 100% and passes all doctests. I'm glad to see this!



---

archive/issue_comments_046684.json:
```json
{
    "body": "Attachment [trac_5918-typos-docfixes.patch](tarball://root/attachments/some-uuid/ticket5918/trac_5918-typos-docfixes.patch) by @dandrake created at 2009-04-29 09:14:09\n\napply on top of trac_5918-rebased.patch",
    "created_at": "2009-04-29T09:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46684",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_5918-typos-docfixes.patch](tarball://root/attachments/some-uuid/ticket5918/trac_5918-typos-docfixes.patch) by @dandrake created at 2009-04-29 09:14:09

apply on top of trac_5918-rebased.patch



---

archive/issue_comments_046685.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> I'm going to upload a patch which corrects a bunch of typos and formatting bits. I do have a couple comments:\n> \n>   * before, the definitions for order ideal and filter were both obviously wrong. I corrected the definition and took the liberty of rewriting it; please check those.\n\nThanks for catching these. I checked your corrected definitions, and they are correct. (It seems that a bunch of > and < symbols disappeared at some point; most likely during the automatic conversion to ReST).\n\n>   * you need a blank line between `EXAMPLES::}} (or {{{TEST::`) and the first line of the doctest; otherwise, the documentation doesn't get typeset correctly.\n\nThanks for pointing this out. Obviously, I didn't know this.\n\n>   * doing ``M\\\"obius`` doesn't work; it automatically uses LaTeX in math mode, and gets messed up. For now I just removed the backticks. (If we add a utf-8 encoding declaration, you can use the umlaut and everything works, but for now, the official rule is that Sage library code is 7-bit clean.)\n\nIt seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.\n\n> Also. there seems to be a lot of duplication between posets.py and hasse_diagram.py. This makes fixing documentation hard, since you have to fix things in two places. Is it possible to somehow combine this stuff so code and documentation doesn't need to be copied? (I'm asking this of everyone, not necessarily Franco.)\n\nYeah, it is a bit of a pain. The original code was my first Sage/Python coding project, and some of my design decisions were not great. At some point the code needs to be updated to deal with more general posets (like very large/infinite posets), and I imagine at that point the two classes will merge into something like `FinitePosetWithHasseDiagram`.\n\nEven though there are planned changes, I thought it was very much worth the effort to add the doctests and fix the bugs in the current code.\n\nThanks for taking a look at the patch. I agree with all your changes.",
    "created_at": "2009-04-29T09:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46685",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:5 ddrake]:
> I'm going to upload a patch which corrects a bunch of typos and formatting bits. I do have a couple comments:
> 
>   * before, the definitions for order ideal and filter were both obviously wrong. I corrected the definition and took the liberty of rewriting it; please check those.

Thanks for catching these. I checked your corrected definitions, and they are correct. (It seems that a bunch of > and < symbols disappeared at some point; most likely during the automatic conversion to ReST).

>   * you need a blank line between `EXAMPLES::}} (or {{{TEST::`) and the first line of the doctest; otherwise, the documentation doesn't get typeset correctly.

Thanks for pointing this out. Obviously, I didn't know this.

>   * doing ``M\"obius`` doesn't work; it automatically uses LaTeX in math mode, and gets messed up. For now I just removed the backticks. (If we add a utf-8 encoding declaration, you can use the umlaut and everything works, but for now, the official rule is that Sage library code is 7-bit clean.)

It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.

> Also. there seems to be a lot of duplication between posets.py and hasse_diagram.py. This makes fixing documentation hard, since you have to fix things in two places. Is it possible to somehow combine this stuff so code and documentation doesn't need to be copied? (I'm asking this of everyone, not necessarily Franco.)

Yeah, it is a bit of a pain. The original code was my first Sage/Python coding project, and some of my design decisions were not great. At some point the code needs to be updated to deal with more general posets (like very large/infinite posets), and I imagine at that point the two classes will merge into something like `FinitePosetWithHasseDiagram`.

Even though there are planned changes, I thought it was very much worth the effort to add the doctests and fix the bugs in the current code.

Thanks for taking a look at the patch. I agree with all your changes.



---

archive/issue_comments_046686.json:
```json
{
    "body": "Replying to [comment:6 saliola]:\n> It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.\n\nDo `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version. The reference manual pulls in all the docstrings from the Sage library. The output will be in `$SAGE_ROOT/devel/sage/doc/output/` and look in the html or pdf directories. You can also create the developer's guide, installation guide, and a bunch of other stuff by replacing \"reference\" with \"developer\", \"installation\", \"constructions\", and others.\n\n> Even though there are planned changes, I thought it was very much worth the effort to add the doctests and fix the bugs in the current code.\n\nYes! Definitely.",
    "created_at": "2009-04-29T12:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46686",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:6 saliola]:
> It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.

Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version. The reference manual pulls in all the docstrings from the Sage library. The output will be in `$SAGE_ROOT/devel/sage/doc/output/` and look in the html or pdf directories. You can also create the developer's guide, installation guide, and a bunch of other stuff by replacing "reference" with "developer", "installation", "constructions", and others.

> Even though there are planned changes, I thought it was very much worth the effort to add the doctests and fix the bugs in the current code.

Yes! Definitely.



---

archive/issue_comments_046687.json:
```json
{
    "body": "Replying to [comment:7 ddrake]:\n> Replying to [comment:6 saliola]:\n> > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.\n> \n> Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.\n\nThanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.",
    "created_at": "2009-04-29T15:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46687",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:7 ddrake]:
> Replying to [comment:6 saliola]:
> > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.
> 
> Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.

Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.



---

archive/issue_comments_046688.json:
```json
{
    "body": "Replying to [comment:8 saliola]:\n> Replying to [comment:7 ddrake]:\n> > Replying to [comment:6 saliola]:\n> > > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.\n> > \n> > Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.\n> \n> Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.\n\nYes and no.  For the PDF version, there is no way to do this right now, as far as I know.  For the html version, once you've built it once for a particular branch, the next time it will only rebuild the files which have changed.  If you install the patch at #5653, you can also view the html output for individual functions from the notebook by typing `function?`.",
    "created_at": "2009-04-29T16:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46688",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:8 saliola]:
> Replying to [comment:7 ddrake]:
> > Replying to [comment:6 saliola]:
> > > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.
> > 
> > Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.
> 
> Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.

Yes and no.  For the PDF version, there is no way to do this right now, as far as I know.  For the html version, once you've built it once for a particular branch, the next time it will only rebuild the files which have changed.  If you install the patch at #5653, you can also view the html output for individual functions from the notebook by typing `function?`.



---

archive/issue_comments_046689.json:
```json
{
    "body": "Okay, after finding typos, I thought I should go through and actually look at everything: this gets a positive review, although I would like someone to comment on doctesting the nested functions. In this instance, it seems okay but someone who knows better may wish to comment/revert the positive review.",
    "created_at": "2009-04-30T01:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46689",
    "user": "https://github.com/dandrake"
}
```

Okay, after finding typos, I thought I should go through and actually look at everything: this gets a positive review, although I would like someone to comment on doctesting the nested functions. In this instance, it seems okay but someone who knows better may wish to comment/revert the positive review.



---

archive/issue_comments_046690.json:
```json
{
    "body": "I looked over Dan's patch and it looks good to me. Doctests do pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T01:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I looked over Dan's patch and it looks good to me. Doctests do pass.

Cheers,

Michael



---

archive/issue_comments_046691.json:
```json
{
    "body": "Merged  trac_5918-rebased.patch and trac_5918-typos-docfixes.patch in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T01:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged  trac_5918-rebased.patch and trac_5918-typos-docfixes.patch in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046692.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T01:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013879.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T01:40:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5918#event-13879"
}
```



---

archive/issue_comments_046693.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> Replying to [comment:8 saliola]:\n> > Replying to [comment:7 ddrake]:\n> > > Replying to [comment:6 saliola]:\n> > > > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.\n> > > \n> > > Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.\n> > \n> > Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.\n> \n> Yes and no.  For the PDF version, there is no way to do this right now, as far as I know.  For the html version, once you've built it once for a particular branch, the next time it will only rebuild the files which have changed.  If you install the patch at #5653, you can also view the html output for individual functions from the notebook by typing `function?`.\n\nThank you, John and Dan, for you answers. These will be very useful.",
    "created_at": "2009-04-30T07:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5918#issuecomment-46693",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:9 jhpalmieri]:
> Replying to [comment:8 saliola]:
> > Replying to [comment:7 ddrake]:
> > > Replying to [comment:6 saliola]:
> > > > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.
> > > 
> > > Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.
> > 
> > Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.
> 
> Yes and no.  For the PDF version, there is no way to do this right now, as far as I know.  For the html version, once you've built it once for a particular branch, the next time it will only rebuild the files which have changed.  If you install the patch at #5653, you can also view the html output for individual functions from the notebook by typing `function?`.

Thank you, John and Dan, for you answers. These will be very useful.
