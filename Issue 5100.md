# Issue 5100: worksheets: can't empty the trash (safari only?)

archive/issues_005100.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jasongrout @mwhansen @williamstein\n\nKeywords: trash, safari\n\nWith Safari on an Intel iMac, sage 3.3.alpha1:\n\nFrom the notebook interface, if I select \"Trash\" to get the list of deleted worksheets, then clicking \"Empty trash\" doesn't actually empty the trash.  It sends me back to the list of active worksheets, but if I click on \"Trash\" again, I see the same list of deleted worksheets.\n\nWith Firefox on the same iMac, emptying the trash works just fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5100\n\n",
    "created_at": "2009-01-25T17:01:45Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "worksheets: can't empty the trash (safari only?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5100",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: boothby

CC:  @jasongrout @mwhansen @williamstein

Keywords: trash, safari

With Safari on an Intel iMac, sage 3.3.alpha1:

From the notebook interface, if I select "Trash" to get the list of deleted worksheets, then clicking "Empty trash" doesn't actually empty the trash.  It sends me back to the list of active worksheets, but if I click on "Trash" again, I see the same list of deleted worksheets.

With Firefox on the same iMac, emptying the trash works just fine.

Issue created by migration from https://trac.sagemath.org/ticket/5100





---

archive/issue_comments_038854.json:
```json
{
    "body": "This sounds similar to #5095. There were also some places where Safari acted differently than Firefox, so this is likely due to the work around TinyMCE.\n\nJason, Mike: Any idea what might be going on?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T20:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This sounds similar to #5095. There were also some places where Safari acted differently than Firefox, so this is likely due to the work around TinyMCE.

Jason, Mike: Any idea what might be going on?

Cheers,

Michael



---

archive/issue_comments_038855.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T20:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38855",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038856.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2009-01-25T20:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38856",
    "user": "https://github.com/mwhansen"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_038857.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-25T20:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38857",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_038858.json:
```json
{
    "body": "This is definitely different than #5095.  I will try to get access to Safari to see what's going on, but nothing leaps out at me at this point.  I guess I'll go through the TinyMCE patches and see what all was changed.",
    "created_at": "2009-01-25T20:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38858",
    "user": "https://github.com/mwhansen"
}
```

This is definitely different than #5095.  I will try to get access to Safari to see what's going on, but nothing leaps out at me at this point.  I guess I'll go through the TinyMCE patches and see what all was changed.



---

archive/issue_comments_038859.json:
```json
{
    "body": "To confirm mhansen's comment, I applied the patch for #5095 (I gave it a positive review, in fact), and it doesn't fix this problem.",
    "created_at": "2009-01-25T21:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38859",
    "user": "https://github.com/jhpalmieri"
}
```

To confirm mhansen's comment, I applied the patch for #5095 (I gave it a positive review, in fact), and it doesn't fix this problem.



---

archive/issue_comments_038860.json:
```json
{
    "body": "I get this behavior on 3.2.1 with Safari, not Firefox (both on a version without TinyMCE and one where I had applied TinyMCE).  So this probably has been around for a bit, and should be unrelated to TinyMCE.",
    "created_at": "2009-01-26T01:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38860",
    "user": "https://github.com/kcrisman"
}
```

I get this behavior on 3.2.1 with Safari, not Firefox (both on a version without TinyMCE and one where I had applied TinyMCE).  So this probably has been around for a bit, and should be unrelated to TinyMCE.



---

archive/issue_comments_038861.json:
```json
{
    "body": "The issue we had with TinyMCE acting different under Safari vs. Firefox had to do with the browser executing javascript code when html was inserted dynamically into the DOM of the browser page.  Apparently Firefox automatically executes code inside of <script> tags that are inserted into the DOM, while Safari doesn't.  To overcome this, we ended up stripping out the <script> tags from any HTML that was inserted into the DOM and running the script code separately.\n\nOf course, the above comment only applies to <script> blocks loaded dynamically; any <script> blocks in the original HTML page should execute just normally.\n\nI don't know if that is the issue, but since mabshoff asked, I thought I'd mention it.",
    "created_at": "2009-01-26T12:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38861",
    "user": "https://github.com/jasongrout"
}
```

The issue we had with TinyMCE acting different under Safari vs. Firefox had to do with the browser executing javascript code when html was inserted dynamically into the DOM of the browser page.  Apparently Firefox automatically executes code inside of <script> tags that are inserted into the DOM, while Safari doesn't.  To overcome this, we ended up stripping out the <script> tags from any HTML that was inserted into the DOM and running the script code separately.

Of course, the above comment only applies to <script> blocks loaded dynamically; any <script> blocks in the original HTML page should execute just normally.

I don't know if that is the issue, but since mabshoff asked, I thought I'd mention it.



---

archive/issue_comments_038862.json:
```json
{
    "body": "For those that can reproduce the problem, could you please give me the specific versions of OS X and Safari that you are using?\n\nI just tried this in Safari 3.2.1 on Mac OS X 10.5.6 and it worked fine.",
    "created_at": "2009-01-26T18:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38862",
    "user": "https://github.com/mwhansen"
}
```

For those that can reproduce the problem, could you please give me the specific versions of OS X and Safari that you are using?

I just tried this in Safari 3.2.1 on Mac OS X 10.5.6 and it worked fine.



---

archive/issue_comments_038863.json:
```json
{
    "body": "Also, one can run (while Safari is not running), \"defaults write com.apple.Safari IncludeDebugMenu 1\" in the terminal to enable the debug menu in Safari.    Choosing Develop -> Show WebInspector before trying to delete the worksheets may yield some useful information.",
    "created_at": "2009-01-26T19:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38863",
    "user": "https://github.com/mwhansen"
}
```

Also, one can run (while Safari is not running), "defaults write com.apple.Safari IncludeDebugMenu 1" in the terminal to enable the debug menu in Safari.    Choosing Develop -> Show WebInspector before trying to delete the worksheets may yield some useful information.



---

archive/issue_comments_038864.json:
```json
{
    "body": "I am on a PPC OSX.4 using Safari 3.2.1.  \n\nI'll try this other debugging thing tonight if I get a chance.",
    "created_at": "2009-01-26T19:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38864",
    "user": "https://github.com/kcrisman"
}
```

I am on a PPC OSX.4 using Safari 3.2.1.  

I'll try this other debugging thing tonight if I get a chance.



---

archive/issue_comments_038865.json:
```json
{
    "body": "Replying to [comment:8 mhansen]:\n> Also, one can run (while Safari is not running), \"defaults write com.apple.Safari IncludeDebugMenu 1\" in the terminal to enable the debug menu in Safari.    Choosing Develop -> Show WebInspector before trying to delete the worksheets may yield some useful information.\n\n\"Unmatched </input> encountered.  Ignoring tag.\"\n\nThis linked to line 38 of my HTML, which was:\n\n```\n<input id=\"search_worksheets\" size=20 onkeypress=\"return search_worksheets_enter_pressed(event, 'trash');\" value\"\"></input>\n```\n\n\nBy the way, this *also* happened pretty much any time I used the Current Folder links in any way, so I'm not sure how this error report actually has anything to do with the onClick=\"empty_trash(); return false;\" (should that be False?), but it did generate an error, so perhaps it will be useful to someone.",
    "created_at": "2009-01-27T03:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38865",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:8 mhansen]:
> Also, one can run (while Safari is not running), "defaults write com.apple.Safari IncludeDebugMenu 1" in the terminal to enable the debug menu in Safari.    Choosing Develop -> Show WebInspector before trying to delete the worksheets may yield some useful information.

"Unmatched </input> encountered.  Ignoring tag."

This linked to line 38 of my HTML, which was:

```
<input id="search_worksheets" size=20 onkeypress="return search_worksheets_enter_pressed(event, 'trash');" value""></input>
```


By the way, this *also* happened pretty much any time I used the Current Folder links in any way, so I'm not sure how this error report actually has anything to do with the onClick="empty_trash(); return false;" (should that be False?), but it did generate an error, so perhaps it will be useful to someone.



---

archive/issue_comments_038866.json:
```json
{
    "body": "I see the same things as kcrisman, including the same error message, but with Safari 3.2.1 (5525.27.1), OS X 10.5.6 on an Intel iMac.",
    "created_at": "2009-01-27T03:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38866",
    "user": "https://github.com/jhpalmieri"
}
```

I see the same things as kcrisman, including the same error message, but with Safari 3.2.1 (5525.27.1), OS X 10.5.6 on an Intel iMac.



---

archive/issue_comments_038867.json:
```json
{
    "body": "That is missing an equals sign between the value and the quotes.  Is that a typo or is that the error?\n\nThe template in server/notebook/templates/search.html doesn't seem to be missing the equals sign.",
    "created_at": "2009-01-27T03:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38867",
    "user": "https://github.com/jasongrout"
}
```

That is missing an equals sign between the value and the quotes.  Is that a typo or is that the error?

The template in server/notebook/templates/search.html doesn't seem to be missing the equals sign.



---

archive/issue_comments_038868.json:
```json
{
    "body": "Replying to [comment:11 jhpalmieri]:\n> I see the same things as kcrisman, including the same error message, but with Safari 3.2.1 (5525.27.1), OS X 10.5.6 on an Intel iMac.\n> \n\nI don't think that error message has anything to do with it.  Are you doing this in Sage 3.3.alpha2 + #5095.",
    "created_at": "2009-01-27T03:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38868",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:11 jhpalmieri]:
> I see the same things as kcrisman, including the same error message, but with Safari 3.2.1 (5525.27.1), OS X 10.5.6 on an Intel iMac.
> 

I don't think that error message has anything to do with it.  Are you doing this in Sage 3.3.alpha2 + #5095.



---

archive/issue_comments_038869.json:
```json
{
    "body": "Replying to [comment:12 jason]:\n> That is missing an equals sign between the value and the quotes.  Is that a typo or is that the error?\n\nTypo, I think.\n\nDon't have 3.3.alpha2+anything, and unfortunately that won't happen for a bit.  Sorry the debugger didn't help.",
    "created_at": "2009-01-27T04:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38869",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:12 jason]:
> That is missing an equals sign between the value and the quotes.  Is that a typo or is that the error?

Typo, I think.

Don't have 3.3.alpha2+anything, and unfortunately that won't happen for a bit.  Sorry the debugger didn't help.



---

archive/issue_comments_038870.json:
```json
{
    "body": "Now this is with 3.3.alpha2 + the 5095 patch.\n\nWhen I click the Trash button to get the list of deleted worksheets, I get this in the error console:\n\n```\nUnmatched </input> encountered.  Ignoring tag.\nhttp://localhost:8000/home/admin/?typ=trash (line 68)\n```\n\n\nThis points to the line\n\n```\n<input id=\"search_worksheets\" size=20 onkeypress=\"return search_worksheets_enter_pressed(event, 'trash');\" \n```\n\n\nClicking \"Empty Trash\" then gives me\n\n```\nUnmatched </input> encountered.  Ignoring tag.\nhttp://localhost:8000/home/admin/ (line 68)\n```\n\nThis points to the line\n\n```\n<input id=\"search_worksheets\" size=20 onkeypress=\"return search_worksheets_enter_pressed(event, 'active');\" \n```\n\n\n(By the way, for what it's worth, you can turn on the Develop menu in Safari from the \"Advanced\" tab in the preferences -- no need to quit and restart.)",
    "created_at": "2009-01-27T05:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38870",
    "user": "https://github.com/jhpalmieri"
}
```

Now this is with 3.3.alpha2 + the 5095 patch.

When I click the Trash button to get the list of deleted worksheets, I get this in the error console:

```
Unmatched </input> encountered.  Ignoring tag.
http://localhost:8000/home/admin/?typ=trash (line 68)
```


This points to the line

```
<input id="search_worksheets" size=20 onkeypress="return search_worksheets_enter_pressed(event, 'trash');" 
```


Clicking "Empty Trash" then gives me

```
Unmatched </input> encountered.  Ignoring tag.
http://localhost:8000/home/admin/ (line 68)
```

This points to the line

```
<input id="search_worksheets" size=20 onkeypress="return search_worksheets_enter_pressed(event, 'active');" 
```


(By the way, for what it's worth, you can turn on the Develop menu in Safari from the "Advanced" tab in the preferences -- no need to quit and restart.)



---

archive/issue_comments_038871.json:
```json
{
    "body": "It would be nice to get this sorted out in 3.3 since we are doing an rc0 in about two days.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T02:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It would be nice to get this sorted out in 3.3 since we are doing an rc0 in about two days.

Cheers,

Michael



---

archive/issue_comments_038872.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-03-01T02:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_038873.json:
```json
{
    "body": "Can someone confirm this as a problem that is still happening?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Can someone confirm this as a problem that is still happening?

Cheers,

Michael



---

archive/issue_comments_038874.json:
```json
{
    "body": "I've never been able to reproduce it, and I've tried on like three different OS X boxes.",
    "created_at": "2009-03-01T02:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38874",
    "user": "https://github.com/mwhansen"
}
```

I've never been able to reproduce it, and I've tried on like three different OS X boxes.



---

archive/issue_comments_038875.json:
```json
{
    "body": "It's still a problem for me: Sage 3.4.alpha0 (both an upgraded version and a version built from scratch), Intel iMac running OS X 10.5.6, and now with Safari 4 beta (build 5528.16), although I was having the problem before with Safari 3.2.1.  Just to test, I created a new .sage directory and I still have the problem, so it's not something weird in my .sage directory.  I'll try it on my MacBookPro, too. What else can I do to help debug this?",
    "created_at": "2009-03-01T17:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38875",
    "user": "https://github.com/jhpalmieri"
}
```

It's still a problem for me: Sage 3.4.alpha0 (both an upgraded version and a version built from scratch), Intel iMac running OS X 10.5.6, and now with Safari 4 beta (build 5528.16), although I was having the problem before with Safari 3.2.1.  Just to test, I created a new .sage directory and I still have the problem, so it's not something weird in my .sage directory.  I'll try it on my MacBookPro, too. What else can I do to help debug this?



---

archive/issue_comments_038876.json:
```json
{
    "body": "Can someone please try this out and see if this is still a problem? Thanks.",
    "created_at": "2009-11-15T12:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38876",
    "user": "https://github.com/TimDumol"
}
```

Can someone please try this out and see if this is still a problem? Thanks.



---

archive/issue_comments_038877.json:
```json
{
    "body": "It's still a problem for me: with Sage 4.2.1 on OS X 10.5, Safari 4.0.4, it still behaves as described in the summary.",
    "created_at": "2009-11-15T16:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38877",
    "user": "https://github.com/jhpalmieri"
}
```

It's still a problem for me: with Sage 4.2.1 on OS X 10.5, Safari 4.0.4, it still behaves as described in the summary.



---

archive/issue_comments_038878.json:
```json
{
    "body": "Attachment [trac_5100-empty-trash.patch](tarball://root/attachments/some-uuid/ticket5100/trac_5100-empty-trash.patch) by @TimDumol created at 2009-12-05 12:04:38\n\nAn attempt at fixing the bug.",
    "created_at": "2009-12-05T12:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38878",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_5100-empty-trash.patch](tarball://root/attachments/some-uuid/ticket5100/trac_5100-empty-trash.patch) by @TimDumol created at 2009-12-05 12:04:38

An attempt at fixing the bug.



---

archive/issue_comments_038879.json:
```json
{
    "body": "I'm not sure if this patch fixes the bug -- I don't own a Mac, but can anyone check if it does? Thanks!",
    "created_at": "2009-12-05T12:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38879",
    "user": "https://github.com/TimDumol"
}
```

I'm not sure if this patch fixes the bug -- I don't own a Mac, but can anyone check if it does? Thanks!



---

archive/issue_comments_038880.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-05T12:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38880",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038881.json:
```json
{
    "body": "This patch fixes it for me on Mac OS X 10.6.\n\nCan people without Macs test that this doesn't break things for them?",
    "created_at": "2009-12-05T18:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38881",
    "user": "https://github.com/jhpalmieri"
}
```

This patch fixes it for me on Mac OS X 10.6.

Can people without Macs test that this doesn't break things for them?



---

archive/issue_comments_038882.json:
```json
{
    "body": "This is very nice, sensible, and well researched patch. It's also the right pattern for how we should do other similar things in the future.  Very nice!",
    "created_at": "2009-12-08T19:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38882",
    "user": "https://github.com/williamstein"
}
```

This is very nice, sensible, and well researched patch. It's also the right pattern for how we should do other similar things in the future.  Very nice!



---

archive/issue_comments_038883.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T19:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38883",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T19:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38884",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_005346.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-08T19:13:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5100#event-5346"
}
```



---

archive/issue_comments_038885.json:
```json
{
    "body": "I merged this into sage-0.4.6.",
    "created_at": "2009-12-08T19:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38885",
    "user": "https://github.com/williamstein"
}
```

I merged this into sage-0.4.6.



---

archive/issue_comments_038886.json:
```json
{
    "body": "I think this breaks emptying the trash in Firefox 3.5.6 on Linux and IE 8 on Windows XP.  Please see #7847 for a possible workaround.",
    "created_at": "2010-01-05T03:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5100#issuecomment-38886",
    "user": "https://github.com/qed777"
}
```

I think this breaks emptying the trash in Firefox 3.5.6 on Linux and IE 8 on Windows XP.  Please see #7847 for a possible workaround.
