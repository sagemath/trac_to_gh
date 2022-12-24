# Issue 7404: Display as much of a worksheet's title for which there's room

archive/issues_007404.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jasongrout @TimDumol @williamstein @kcrisman\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/msg/2973d4d2f3c2406a):\n\n```\nJason Grout wrote:\n> William Stein wrote:\n>> Alex Ghitza wrote:\n>>> 3. long worksheet titles get cut off even if there would be enough\n>>> room to display them in their entirety (in my case, I had \"Victorian\n>>> Algebra Conference 2009\" which appeared as \"Victorian Algebra\n>>> Conference 2...\")\n\n>> True.  It is tricky because fonts are proportionally spaced.\n\n> Why does that make it tricky?  Make the div/table cell the maximum width\n> possible (and expand as the browser window expands), and let the browser\n> worry about when to cut off the text by setting the CSS style to chop\n> off the text.  I suppose we'll miss the \"...\"; is that the tricky part? \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7404\n\n",
    "created_at": "2009-11-06T16:00:29Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Display as much of a worksheet's title for which there's room",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7404",
    "user": "@qed777"
}
```
Assignee: boothby

CC:  @jasongrout @TimDumol @williamstein @kcrisman

From [sage-devel](http://groups.google.com/group/sage-devel/msg/2973d4d2f3c2406a):

```
Jason Grout wrote:
> William Stein wrote:
>> Alex Ghitza wrote:
>>> 3. long worksheet titles get cut off even if there would be enough
>>> room to display them in their entirety (in my case, I had "Victorian
>>> Algebra Conference 2009" which appeared as "Victorian Algebra
>>> Conference 2...")

>> True.  It is tricky because fonts are proportionally spaced.

> Why does that make it tricky?  Make the div/table cell the maximum width
> possible (and expand as the browser window expands), and let the browser
> worry about when to cut off the text by setting the CSS style to chop
> off the text.  I suppose we'll miss the "..."; is that the tricky part? 
```



Issue created by migration from https://trac.sagemath.org/ticket/7404





---

archive/issue_comments_062300.json:
```json
{
    "body": "A first take that probably overdoes it.  Apply to sagenb repo.",
    "created_at": "2009-11-06T16:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62300",
    "user": "@qed777"
}
```

A first take that probably overdoes it.  Apply to sagenb repo.



---

archive/issue_comments_062301.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T16:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62301",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062302.json:
```json
{
    "body": "Attachment [trac_7404-css_worksheet_title.patch](tarball://root/attachments/some-uuid/ticket7404/trac_7404-css_worksheet_title.patch) by @qed777 created at 2009-11-06 16:37:20\n\nThe [attachment:trac_7404-css_worksheet_title.patch first take] appears to work, although a *very* long title is visible under and beyond the \"Save/Discard\" buttons.\n\nI'm sure this is just one way to [attempt to] do it --- I'm not a CSS expert.  Please feel to free to replace it.  Either way, we should check that a candidate works in IE.\n\nBy the way, this patch may depend on other recent sagenb patches.  Here's my current queue (ignore the version numbers):\n\n```\ntrac_7316-sageinspect_defn.patch\ntrac_7318-sphinxify_confdir.patch\ntrac_7309-javascript-sage_v2.patch\ntrac_7310-modals.6.patch\ntrac_7332-css-escape.2.patch\ntrac_sagenb-7341.patch                          # Tab completion.\ntrac_sagenb-7346.patch                          # Vertical scrollbars.\ntrac_7339-sagenb_cell_bugs.patch\ntrac_7343-selenium-tests.4.patch\ntrac_7390-sagenb_test_report_A.patch\ntrac_7390-sagenb_test_report_B.patch\ntrac_7404-css_worksheet_title.patch             # This ticket!\ntrac_7385-renaming-published-worksheets.patch\ntrac_7384-sphinxify-docstrings.patch\ntrac_7354-jsmath_undo_revision.patch\ntrac_7322-jsmath_upgrade.patch\ntrac_7106-paren_match_doc.patch\n```\n\nBut it's likely that several of these commute.",
    "created_at": "2009-11-06T16:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62302",
    "user": "@qed777"
}
```

Attachment [trac_7404-css_worksheet_title.patch](tarball://root/attachments/some-uuid/ticket7404/trac_7404-css_worksheet_title.patch) by @qed777 created at 2009-11-06 16:37:20

The [attachment:trac_7404-css_worksheet_title.patch first take] appears to work, although a *very* long title is visible under and beyond the "Save/Discard" buttons.

I'm sure this is just one way to [attempt to] do it --- I'm not a CSS expert.  Please feel to free to replace it.  Either way, we should check that a candidate works in IE.

By the way, this patch may depend on other recent sagenb patches.  Here's my current queue (ignore the version numbers):

```
trac_7316-sageinspect_defn.patch
trac_7318-sphinxify_confdir.patch
trac_7309-javascript-sage_v2.patch
trac_7310-modals.6.patch
trac_7332-css-escape.2.patch
trac_sagenb-7341.patch                          # Tab completion.
trac_sagenb-7346.patch                          # Vertical scrollbars.
trac_7339-sagenb_cell_bugs.patch
trac_7343-selenium-tests.4.patch
trac_7390-sagenb_test_report_A.patch
trac_7390-sagenb_test_report_B.patch
trac_7404-css_worksheet_title.patch             # This ticket!
trac_7385-renaming-published-worksheets.patch
trac_7384-sphinxify-docstrings.patch
trac_7354-jsmath_undo_revision.patch
trac_7322-jsmath_upgrade.patch
trac_7106-paren_match_doc.patch
```

But it's likely that several of these commute.



---

archive/issue_comments_062303.json:
```json
{
    "body": "Replying to [comment:3:ticket6939 kcrisman]:\n> Sweet.  I love CSS.",
    "created_at": "2009-11-11T17:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62303",
    "user": "@qed777"
}
```

Replying to [comment:3:ticket6939 kcrisman]:
> Sweet.  I love CSS.



---

archive/issue_comments_062304.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> Replying to [comment:3:ticket:6939 kcrisman]:\n> > Sweet.  I love CSS.\nThat's from [comment:3:ticket:6939 this comment], by the way.",
    "created_at": "2009-11-11T17:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62304",
    "user": "@qed777"
}
```

Replying to [comment:2 mpatel]:
> Replying to [comment:3:ticket:6939 kcrisman]:
> > Sweet.  I love CSS.
That's from [comment:3:ticket:6939 this comment], by the way.



---

archive/issue_comments_062305.json:
```json
{
    "body": "I should point out that I only love CSS, but am (also) not by any means an expert in it.  Sorry.",
    "created_at": "2009-11-11T19:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62305",
    "user": "@kcrisman"
}
```

I should point out that I only love CSS, but am (also) not by any means an expert in it.  Sorry.



---

archive/issue_comments_062306.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-11T23:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62306",
    "user": "@williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062307.json:
```json
{
    "body": "REFEREE REPORT:\n\n (1) Looking at and reading the code -- it looks good.\n\n (2) You should always set a milestone for the ticket.  It helps a *lot* in keeping tickets from getting totally lost. \n\n (3) This patch makes all the worksheet titles in the homescreen vanish, so that's a serious bug.  See http://wstein.org/home/wstein/tmp/7404-a.png\n\n (4) This patch also makes the top bar area look ridiculous (in my opinion) when the title is really long.  See http://wstein.org/home/wstein/tmp/7404-b.png",
    "created_at": "2009-11-11T23:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62307",
    "user": "@williamstein"
}
```

REFEREE REPORT:

 (1) Looking at and reading the code -- it looks good.

 (2) You should always set a milestone for the ticket.  It helps a *lot* in keeping tickets from getting totally lost. 

 (3) This patch makes all the worksheet titles in the homescreen vanish, so that's a serious bug.  See http://wstein.org/home/wstein/tmp/7404-a.png

 (4) This patch also makes the top bar area look ridiculous (in my opinion) when the title is really long.  See http://wstein.org/home/wstein/tmp/7404-b.png



---

archive/issue_comments_062308.json:
```json
{
    "body": "A [related] possibility: Use [tablesorter](http://tablesorter.com/docs/) to sort in the browser.",
    "created_at": "2009-11-25T17:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62308",
    "user": "@qed777"
}
```

A [related] possibility: Use [tablesorter](http://tablesorter.com/docs/) to sort in the browser.



---

archive/issue_comments_062309.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62309",
    "user": "boothby"
}
```

Resolution: invalid



---

archive/issue_comments_062310.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7404#issuecomment-62310",
    "user": "boothby"
}
```

Closing deprecated notebook tickets
