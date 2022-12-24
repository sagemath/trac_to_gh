# Issue 6939: [with patch, needs review] Make scrollbars appear on cell output when the output is too wide

archive/issues_006939.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777 @kcrisman boothby\n\nCurrently, a scrollbar appears down at the bottom of the entire worksheet, which is only minimally helpful, since you then need to go to the bottom and scroll everything over.\n\nThis patch makes scrollbars appear on output that is too wide, but just on that output.\n\nTo test, do something like:\n\n\n```\nf=cos(x)-x\nshow(f.taylor(x,0,50))\n```\n\n\nin the notebook\n\nIssue created by migration from https://trac.sagemath.org/ticket/6939\n\n",
    "created_at": "2009-09-15T22:08:01Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Make scrollbars appear on cell output when the output is too wide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6939",
    "user": "@jasongrout"
}
```
Assignee: boothby

CC:  @qed777 @kcrisman boothby

Currently, a scrollbar appears down at the bottom of the entire worksheet, which is only minimally helpful, since you then need to go to the bottom and scroll everything over.

This patch makes scrollbars appear on output that is too wide, but just on that output.

To test, do something like:


```
f=cos(x)-x
show(f.taylor(x,0,50))
```


in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/6939





---

archive/issue_comments_057364.json:
```json
{
    "body": "Attachment [trac-6939-notebook-css-overflow.patch](tarball://root/attachments/some-uuid/ticket6939/trac-6939-notebook-css-overflow.patch) by @jasongrout created at 2009-09-15 22:10:13",
    "created_at": "2009-09-15T22:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57364",
    "user": "@jasongrout"
}
```

Attachment [trac-6939-notebook-css-overflow.patch](tarball://root/attachments/some-uuid/ticket6939/trac-6939-notebook-css-overflow.patch) by @jasongrout created at 2009-09-15 22:10:13



---

archive/issue_comments_057365.json:
```json
{
    "body": "Sweet.  I love CSS.  Tested successfully on Safari 4 and Firefox 3.5.  Wish I had access to IE or Linux versions, but this should be okay.\n\nCheck out also:\n\n```\nshow(plot(sin(x),-10,10),figsize=[20,20])\n```\n\nSo you can now generate big pictures in the notebook if you have a reason to do so.  \n\nBut question: why not just overflow, not overflow-x, or also overflow-y?  Those eternally long outputs can be a real pain at times.  Try factorial(10000). Also, how many browsers support CSS3 and not just CSS2?  I can imagine a lot of people on XP having problems with some old version of IE.",
    "created_at": "2009-09-16T13:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57365",
    "user": "@kcrisman"
}
```

Sweet.  I love CSS.  Tested successfully on Safari 4 and Firefox 3.5.  Wish I had access to IE or Linux versions, but this should be okay.

Check out also:

```
show(plot(sin(x),-10,10),figsize=[20,20])
```

So you can now generate big pictures in the notebook if you have a reason to do so.  

But question: why not just overflow, not overflow-x, or also overflow-y?  Those eternally long outputs can be a real pain at times.  Try factorial(10000). Also, how many browsers support CSS3 and not just CSS2?  I can imagine a lot of people on XP having problems with some old version of IE.



---

archive/issue_comments_057366.json:
```json
{
    "body": "Not overflow-y because Sage already handles long vertical outputs by shunting to a file and suppressing text, and besides, who's to say how tall is too tall?  Vertically, we just go by the browser width.  It's a lot harder to guess the magical height that is just right.\n\nIf you think this is good, then you can put a positive review and we can discuss the overflow-y and see if it is needed.",
    "created_at": "2009-09-17T07:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57366",
    "user": "@jasongrout"
}
```

Not overflow-y because Sage already handles long vertical outputs by shunting to a file and suppressing text, and besides, who's to say how tall is too tall?  Vertically, we just go by the browser width.  It's a lot harder to guess the magical height that is just right.

If you think this is good, then you can put a positive review and we can discuss the overflow-y and see if it is needed.



---

archive/issue_comments_057367.json:
```json
{
    "body": "No problem with the vertical, though personally I would prefer a little shorter output, as the screen sometimes jumps rather dramatically and it's hard to scroll back and forth...\n\nWhat about the CSS3 versus CSS2 issue?  On the one hand, I found a quote on css3.info that \"Support for these properties is strong as they were first defined by IE6.\" but on the other hand wikipedia implies that support for this first came in Trident engine 7, which may or may not correspond to IE7...  Maybe the best solution is this one: \"Try specifying the CSS2 overflow property first ... then specify the CSS3 overflow-x/y properties to override it on browsers that can.\"  Of course, that comment was from 2007.\n\nAnyway, as long as it doesn't cause the page to not render at all, I guess this is okay.  If you have time to put in an overflow check first, that would be great.",
    "created_at": "2009-09-17T13:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57367",
    "user": "@kcrisman"
}
```

No problem with the vertical, though personally I would prefer a little shorter output, as the screen sometimes jumps rather dramatically and it's hard to scroll back and forth...

What about the CSS3 versus CSS2 issue?  On the one hand, I found a quote on css3.info that "Support for these properties is strong as they were first defined by IE6." but on the other hand wikipedia implies that support for this first came in Trident engine 7, which may or may not correspond to IE7...  Maybe the best solution is this one: "Try specifying the CSS2 overflow property first ... then specify the CSS3 overflow-x/y properties to override it on browsers that can."  Of course, that comment was from 2007.

Anyway, as long as it doesn't cause the page to not render at all, I guess this is okay.  If you have time to put in an overflow check first, that would be great.



---

archive/issue_comments_057368.json:
```json
{
    "body": "Good point about CSS3 vs. CSS2.  According to http://msdn.microsoft.com/en-us/library/bb250395%28VS.85%29.aspx, IE6 supports overflow-x (search for \"overflow-x\") when in standards-compliant mode.",
    "created_at": "2009-09-17T16:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57368",
    "user": "@jasongrout"
}
```

Good point about CSS3 vs. CSS2.  According to http://msdn.microsoft.com/en-us/library/bb250395%28VS.85%29.aspx, IE6 supports overflow-x (search for "overflow-x") when in standards-compliant mode.



---

archive/issue_comments_057369.json:
```json
{
    "body": "Maybe #6835 should get reviewed and then this should be rebased on that?  #6835 is definitely the larger patch.",
    "created_at": "2009-09-17T19:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57369",
    "user": "@jasongrout"
}
```

Maybe #6835 should get reviewed and then this should be rebased on that?  #6835 is definitely the larger patch.



---

archive/issue_comments_057370.json:
```json
{
    "body": "I meant #6865 in the above comment.",
    "created_at": "2009-09-17T19:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57370",
    "user": "@jasongrout"
}
```

I meant #6865 in the above comment.



---

archive/issue_comments_057371.json:
```json
{
    "body": "I got the following doctest failure:\n\n```\nsage -t -long devel/sage/sage/server/notebook/cell.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/server/notebook/cell.py\", line 2293:\n    sage: C.html_out()\nExpected:\n    '\\n...<table class=\"cell_output_box\">...</table>'\nGot:\n    '\\n               <div class=\"cell_output_div\">\\n               <table class=\"cell_output_box\"><tr>\\n               <td class=\"cell_number\" id=\"cell_number_0\" onClick=\"cycle_cell_output_type(0);\">\\n                 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\n               </td>\\n               <td class=\"output_cell\"><div class=\"cell_div_output_wrap\" id=\"cell_div_output_0\"><div class=\"cell_output_wrap\" id=\"cell_output_0\"><pre class=\"shrunk\">5</pre></div><div class=\"cell_output_nowrap_wrap\" id=\"cell_output_nowrap_0\"><pre class=\"shrunk\">5</pre></div><div class=\"cell_output_html_wrap\" id=\"cell_output_html_0\"> </div></div></td></tr></table></div>'\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_94\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_cell.py\n\t [28.1 s]\n```\n",
    "created_at": "2009-09-18T00:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57371",
    "user": "mvngu"
}
```

I got the following doctest failure:

```
sage -t -long devel/sage/sage/server/notebook/cell.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/server/notebook/cell.py", line 2293:
    sage: C.html_out()
Expected:
    '\n...<table class="cell_output_box">...</table>'
Got:
    '\n               <div class="cell_output_div">\n               <table class="cell_output_box"><tr>\n               <td class="cell_number" id="cell_number_0" onClick="cycle_cell_output_type(0);">\n                 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n               </td>\n               <td class="output_cell"><div class="cell_div_output_wrap" id="cell_div_output_0"><div class="cell_output_wrap" id="cell_output_0"><pre class="shrunk">5</pre></div><div class="cell_output_nowrap_wrap" id="cell_output_nowrap_0"><pre class="shrunk">5</pre></div><div class="cell_output_html_wrap" id="cell_output_html_0"> </div></div></td></tr></table></div>'
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_94
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_cell.py
	 [28.1 s]
```




---

archive/issue_comments_057372.json:
```json
{
    "body": "It looks like #6865 is getting reviewed pretty quickly, so I'll fix the above doctest when I rebase this patch on top of that one.  If this doesn't happen before next Tuesday, I'll just fix the above doctest anyway, since I'd really like to get this into the next version of Sage.",
    "created_at": "2009-09-19T02:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57372",
    "user": "@jasongrout"
}
```

It looks like #6865 is getting reviewed pretty quickly, so I'll fix the above doctest when I rebase this patch on top of that one.  If this doesn't happen before next Tuesday, I'll just fix the above doctest anyway, since I'd really like to get this into the next version of Sage.



---

archive/issue_comments_057373.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2009-09-19T02:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57373",
    "user": "@jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_057374.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-19T02:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57374",
    "user": "@jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057375.json:
```json
{
    "body": "Attachment [trac-6939-notebook-css-overflow.2.patch](tarball://root/attachments/some-uuid/ticket6939/trac-6939-notebook-css-overflow.2.patch) by @qed777 created at 2009-09-21 01:01:48\n\nRebased against #6865.  Apply only this patch.",
    "created_at": "2009-09-21T01:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57375",
    "user": "@qed777"
}
```

Attachment [trac-6939-notebook-css-overflow.2.patch](tarball://root/attachments/some-uuid/ticket6939/trac-6939-notebook-css-overflow.2.patch) by @qed777 created at 2009-09-21 01:01:48

Rebased against #6865.  Apply only this patch.



---

archive/issue_comments_057376.json:
```json
{
    "body": "[attachment:trac-6939-notebook-css-overflow.2.patch Patch v2] is rebased against #6865's [attachment:ticket:6865:trac_6865-templates-css.3.patch patch v3].\n\nI also prepended `#6939` to the commit string.",
    "created_at": "2009-09-21T01:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57376",
    "user": "@qed777"
}
```

[attachment:trac-6939-notebook-css-overflow.2.patch Patch v2] is rebased against #6865's [attachment:ticket:6865:trac_6865-templates-css.3.patch patch v3].

I also prepended `#6939` to the commit string.



---

archive/issue_comments_057377.json:
```json
{
    "body": "I should add that I fixed the doctest failure in `cell.py`.  I've set this ticket to WPNR.",
    "created_at": "2009-09-21T01:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57377",
    "user": "@qed777"
}
```

I should add that I fixed the doctest failure in `cell.py`.  I've set this ticket to WPNR.



---

archive/issue_comments_057378.json:
```json
{
    "body": "mvngu: can you apply the patch now and see if the doctest passes?  If so, then should the positive review above become active again?",
    "created_at": "2009-09-22T17:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57378",
    "user": "@jasongrout"
}
```

mvngu: can you apply the patch now and see if the doctest passes?  If so, then should the positive review above become active again?



---

archive/issue_comments_057379.json:
```json
{
    "body": "positive review on mpatel's rebasing and fixing the doctest (it now works), so I'm putting it back to positive review.\n\nMinh--if there's something wrong with me positive reviewing mpatel's changes, please let me know.",
    "created_at": "2009-09-22T17:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57379",
    "user": "@jasongrout"
}
```

positive review on mpatel's rebasing and fixing the doctest (it now works), so I'm putting it back to positive review.

Minh--if there's something wrong with me positive reviewing mpatel's changes, please let me know.



---

archive/issue_comments_057380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-22T18:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57380",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057381.json:
```json
{
    "body": "Replying to [comment:15 jason]:\n> Minh--if there's something wrong with me positive reviewing mpatel's changes, please let me know.\nI don't see anything wrong, as long as you don't review your own changes and make it positive review. In this case, I see that you reviewed someone else's (mpatel) changes which in this case is a rebase. You never know; rebasing a patch can actually cause unexpected problems. Thank you for your work!\n\n\n\n\nMerged patches in this order:\n\n1. `#6865`\n2. `trac-6939-notebook-css-overflow.2.patch`",
    "created_at": "2009-09-22T18:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57381",
    "user": "mvngu"
}
```

Replying to [comment:15 jason]:
> Minh--if there's something wrong with me positive reviewing mpatel's changes, please let me know.
I don't see anything wrong, as long as you don't review your own changes and make it positive review. In this case, I see that you reviewed someone else's (mpatel) changes which in this case is a rebase. You never know; rebasing a patch can actually cause unexpected problems. Thank you for your work!




Merged patches in this order:

1. `#6865`
2. `trac-6939-notebook-css-overflow.2.patch`



---

archive/issue_comments_057382.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.",
    "created_at": "2009-09-27T09:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6939#issuecomment-57382",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
