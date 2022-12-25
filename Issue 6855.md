# Issue 6855: [with patch, needs work] Enable interacts in published worksheets

archive/issues_006855.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein\n\nWorksheets in the Sage notebook can contain live `interact`-ive cells, which may make it easier to understand how an object's properties depend on a set of parameters.\n\nPlease visit the Sage Wiki to view [some examples](http://wiki.sagemath.org/interact).\n\nCurrently, `interact` cells do not work in published worksheets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6855\n\n",
    "created_at": "2009-09-01T12:31:09Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs work] Enable interacts in published worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6855",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @williamstein

Worksheets in the Sage notebook can contain live `interact`-ive cells, which may make it easier to understand how an object's properties depend on a set of parameters.

Please visit the Sage Wiki to view [some examples](http://wiki.sagemath.org/interact).

Currently, `interact` cells do not work in published worksheets.

Issue created by migration from https://trac.sagemath.org/ticket/6855





---

archive/issue_comments_056423.json:
```json
{
    "body": "Note: See #6897 about The Great Django Migration and for potentially very relevant links.",
    "created_at": "2009-09-11T16:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56423",
    "user": "https://github.com/qed777"
}
```

Note: See #6897 about The Great Django Migration and for potentially very relevant links.



---

archive/issue_comments_056424.json:
```json
{
    "body": "For live cells embedded remotely or in published worksheets, we may need to handle concurrent access, permissions, usage limits, etc.  From this perspective, an asynchronous, event-driven, long-polling, stateless model is quite appealing.  See, e.g.,\n\n* [Comet](http://en.wikipedia.org/wiki/Comet_%28programming%29Comet)\n* [Django](http://docs.djangoproject.com/en/dev/)\n* [Orbited](http://orbited.org/wiki/Documentation)\n* [Tornado](http://www.tornadoweb.org/documentation) \n* [Twisted](http://twistedmatrix.com/trac/wiki/Documentation) \n* [Python / Cython resources](http://wiki.sagemath.org/PythonResources) - Sage wiki.\n\nNote: It's not difficult to make the server respond to a browser's request **only after** it has evaluated the input.  But in the simplest approach, the server **blocks,** unable to answer other clients, while the sage instance ruminates.",
    "created_at": "2009-09-11T17:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56424",
    "user": "https://github.com/qed777"
}
```

For live cells embedded remotely or in published worksheets, we may need to handle concurrent access, permissions, usage limits, etc.  From this perspective, an asynchronous, event-driven, long-polling, stateless model is quite appealing.  See, e.g.,

* [Comet](http://en.wikipedia.org/wiki/Comet_%28programming%29Comet)
* [Django](http://docs.djangoproject.com/en/dev/)
* [Orbited](http://orbited.org/wiki/Documentation)
* [Tornado](http://www.tornadoweb.org/documentation) 
* [Twisted](http://twistedmatrix.com/trac/wiki/Documentation) 
* [Python / Cython resources](http://wiki.sagemath.org/PythonResources) - Sage wiki.

Note: It's not difficult to make the server respond to a browser's request **only after** it has evaluated the input.  But in the simplest approach, the server **blocks,** unable to answer other clients, while the sage instance ruminates.



---

archive/issue_comments_056425.json:
```json
{
    "body": "Non-concurrent first version.  sagenb repo.",
    "created_at": "2009-11-26T02:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56425",
    "user": "https://github.com/qed777"
}
```

Non-concurrent first version.  sagenb repo.



---

archive/issue_comments_056426.json:
```json
{
    "body": "Attachment [trac_6855-published_interacts.patch](tarball://root/attachments/some-uuid/ticket6855/trac_6855-published_interacts.patch) by @qed777 created at 2009-11-26 02:36:57\n\nThe [attachment:trac_6855-published_interacts.patch patch] enables interacts in published worksheets.  Still to do:\n\n* Gracefully handle simultaneous access by multiple clients.\n* Find an alternative to `twist.prep_interact` for rendering the interacts upon load.",
    "created_at": "2009-11-26T02:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56426",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6855-published_interacts.patch](tarball://root/attachments/some-uuid/ticket6855/trac_6855-published_interacts.patch) by @qed777 created at 2009-11-26 02:36:57

The [attachment:trac_6855-published_interacts.patch patch] enables interacts in published worksheets.  Still to do:

* Gracefully handle simultaneous access by multiple clients.
* Find an alternative to `twist.prep_interact` for rendering the interacts upon load.



---

archive/issue_comments_056427.json:
```json
{
    "body": "The local sagenb queue, for what it's worth:\n\n```\ntrac_7390-sagenb_test_report_A.patch\ntrac_7390-sagenb_test_report_B_v2.patch\ntrac_7390-sagenb_test_report_referee.patch\ntrac_7402-pkg_resources.patch\ntrac_7428-publish_last_edited_v2.patch\ntrac_7444-search_after_publish.patch\ntrac_7376-search_by_username_v2.patch\ntrac_1321-sagenb_graphed.patch\nsagenb_7483.patch\nsagenb_7482.patch\nsagenb-7495.patch\nsagenb_3849.patch\ntrac_6855-published_interacts.patch\n```\n",
    "created_at": "2009-11-26T02:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56427",
    "user": "https://github.com/qed777"
}
```

The local sagenb queue, for what it's worth:

```
trac_7390-sagenb_test_report_A.patch
trac_7390-sagenb_test_report_B_v2.patch
trac_7390-sagenb_test_report_referee.patch
trac_7402-pkg_resources.patch
trac_7428-publish_last_edited_v2.patch
trac_7444-search_after_publish.patch
trac_7376-search_by_username_v2.patch
trac_1321-sagenb_graphed.patch
sagenb_7483.patch
sagenb_7482.patch
sagenb-7495.patch
sagenb_3849.patch
trac_6855-published_interacts.patch
```




---

archive/issue_comments_056428.json:
```json
{
    "body": "Concurrent access possibilities, not necessarily mutex:\n\n* Use a process pool, with some limit, to evaluate queued cells.\n* Go stateless - always `reset()` after evaluating a cell.\n* Allocate a new cell, with a unique ID, for each evaluation.  Pass this ID back to the browser, so it can poll for updates.  Delete the temporaries, incrementally, and/or all at once when the \"idle\" check fails.",
    "created_at": "2009-11-26T02:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56428",
    "user": "https://github.com/qed777"
}
```

Concurrent access possibilities, not necessarily mutex:

* Use a process pool, with some limit, to evaluate queued cells.
* Go stateless - always `reset()` after evaluating a cell.
* Allocate a new cell, with a unique ID, for each evaluation.  Pass this ID back to the browser, so it can poll for updates.  Delete the temporaries, incrementally, and/or all at once when the "idle" check fails.



---

archive/issue_comments_056429.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> [...] Still to do:\n>  * Gracefully handle simultaneous access by multiple clients.\n\nSee the previous comment.\n\n>  * Find an alternative to `twist.prep_interact` for rendering the interacts upon load.\n\nSave and serve the rendered HTML.",
    "created_at": "2009-11-26T02:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56429",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:6 mpatel]:
> [...] Still to do:
>  * Gracefully handle simultaneous access by multiple clients.

See the previous comment.

>  * Find an alternative to `twist.prep_interact` for rendering the interacts upon load.

Save and serve the rendered HTML.



---

archive/issue_comments_056430.json:
```json
{
    "body": "Attachment [trac_6855-published_interacts_v2.patch](tarball://root/attachments/some-uuid/ticket6855/trac_6855-published_interacts_v2.patch) by @qed777 created at 2009-11-26 07:00:16\n\nRebased vs. rebased #4714.  Updated commit message.  Only this one.  sagenb repo.",
    "created_at": "2009-11-26T07:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56430",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6855-published_interacts_v2.patch](tarball://root/attachments/some-uuid/ticket6855/trac_6855-published_interacts_v2.patch) by @qed777 created at 2009-11-26 07:00:16

Rebased vs. rebased #4714.  Updated commit message.  Only this one.  sagenb repo.



---

archive/issue_comments_056431.json:
```json
{
    "body": "\n```\n[...as above...]\nsagenb_3849.patch\ntrac_4714-sagenb_jsmath_init.patch\ntrac_6855-published_interacts.patch\n```\n",
    "created_at": "2009-11-26T07:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56431",
    "user": "https://github.com/qed777"
}
```


```
[...as above...]
sagenb_3849.patch
trac_4714-sagenb_jsmath_init.patch
trac_6855-published_interacts.patch
```




---

archive/issue_comments_056432.json:
```json
{
    "body": "Updated patches are available here:\n\n* [http://sage.math.washington.edu/home/mpatel/trac/6855/](http://sage.math.washington.edu/home/mpatel/trac/6855/)\n\nThere's still plenty to do, but I'm making progress.  Version 10:\n\n* Should allow alphanumeric cell ids.  \"Integers\" project to integers (e.g., `'0'` is `0`, `\"19\"` is `19`, etc.).  In particular, we can continue to use non-negative integers for ordinary compute/text cells.  But cells whose ids begin with a non-integer character are [optionally] \"special\" (e.g., `'tmp123'` is `'tmp123'`).  They should have wider applicability than published and remote embedded interacts.  For example, we could use \"g\" cells to communicate graph data bidirectionally (cf. #1321), \"p\" cells for plots, \"i\" cells for introspection, and so on.\n\n* Should contain **far less** [JSLint](http://www.jslint.com/).  This was painful, but it was very useful --- it revealed subtle (to me, at least) problems, potential and actual.\n\n* Subsumes #5644.  This required rewriting most of the introspection functions.  Now each cell has it's own set of introspection variables, but they're all stored in just one global dictionary `introspect`.  Reducing our global footprint (and the probability of library conflicts) is important for embedding worksheets, but I don't plan to take this further just now.\n\nNote: I still need to test browsers other than FF 3.5.5 on Linux.",
    "created_at": "2009-12-03T11:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56432",
    "user": "https://github.com/qed777"
}
```

Updated patches are available here:

* [http://sage.math.washington.edu/home/mpatel/trac/6855/](http://sage.math.washington.edu/home/mpatel/trac/6855/)

There's still plenty to do, but I'm making progress.  Version 10:

* Should allow alphanumeric cell ids.  "Integers" project to integers (e.g., `'0'` is `0`, `"19"` is `19`, etc.).  In particular, we can continue to use non-negative integers for ordinary compute/text cells.  But cells whose ids begin with a non-integer character are [optionally] "special" (e.g., `'tmp123'` is `'tmp123'`).  They should have wider applicability than published and remote embedded interacts.  For example, we could use "g" cells to communicate graph data bidirectionally (cf. #1321), "p" cells for plots, "i" cells for introspection, and so on.

* Should contain **far less** [JSLint](http://www.jslint.com/).  This was painful, but it was very useful --- it revealed subtle (to me, at least) problems, potential and actual.

* Subsumes #5644.  This required rewriting most of the introspection functions.  Now each cell has it's own set of introspection variables, but they're all stored in just one global dictionary `introspect`.  Reducing our global footprint (and the probability of library conflicts) is important for embedding worksheets, but I don't plan to take this further just now.

Note: I still need to test browsers other than FF 3.5.5 on Linux.



---

archive/issue_comments_056433.json:
```json
{
    "body": "V14 gets (all but one of the) [Selenium](http://seleniumhq.org/) ([Grid](http://selenium-grid.seleniumhq.org/)) test to pass in\n\n* Linux: FF3.5.\n* Windows XP: FF3.5, IE8, O10.\n\nSeveral tests fail in Chrome on XP --- `self.logout()` raises the complaint, [\"This webpage has a redirect loop.\"](http://www.google.com/search?q=%22This%20webpage%20has%20a%20redirect%20loop.%22)  I think this is a Chrome bug.\n\nSafari on XP interprets, e.g., `/home/mike/0/` as the local resource `file:///home/mike/0/`, which it refuses to load.  I think this is a Selenium bug.\n\nBut both Chrome and Safari sometimes display `Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again.`  Could this be a SageNB bug?\n\nSelenium is far from consistent in its ability to fire \"special\" keyboard events (e.g., `tab`, `shift-enter`), so I've substituted notebook JS functions, for now.",
    "created_at": "2009-12-05T17:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56433",
    "user": "https://github.com/qed777"
}
```

V14 gets (all but one of the) [Selenium](http://seleniumhq.org/) ([Grid](http://selenium-grid.seleniumhq.org/)) test to pass in

* Linux: FF3.5.
* Windows XP: FF3.5, IE8, O10.

Several tests fail in Chrome on XP --- `self.logout()` raises the complaint, ["This webpage has a redirect loop."](http://www.google.com/search?q=%22This%20webpage%20has%20a%20redirect%20loop.%22)  I think this is a Chrome bug.

Safari on XP interprets, e.g., `/home/mike/0/` as the local resource `file:///home/mike/0/`, which it refuses to load.  I think this is a Selenium bug.

But both Chrome and Safari sometimes display `Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again.`  Could this be a SageNB bug?

Selenium is far from consistent in its ability to fire "special" keyboard events (e.g., `tab`, `shift-enter`), so I've substituted notebook JS functions, for now.



---

archive/issue_comments_056434.json:
```json
{
    "body": "\"I love it when a plan comes together.\" - [Hannibal](http://en.wikipedia.org/wiki/John_%22Hannibal%22_Smith)\n\nNot quite, perhaps, but we're getting close.  The new published interacts patch sequence (`trac_6855-published_interacts_B*.patch`), based on #7666, is at\n\n* http://sage.math.washington.edu/home/mpatel/trac/6855/\n\nStill to do:\n\n* Give proxy cells an expiration date.\n* Proxy worksheet process pool.\n* `server_conf` setting.\n* Some of the \"TODO\" items in `twist.py`.\n\nI'm a bit behind schedule --- I think I underestimated the extent of the changes needed.  But I think it was very important, if not necessary, for me to understand more deeply how the many parts of the Sage Notebook *interact*.  We'll get there soon!\n\nOther changes of interest:\n\n* Data sent from server to client is [JSON](http://www.json.org/js.html)-encoded.\n* `active_cell_list` is `console.log`ged (or displayed in a floating dialog) *when* it changes.",
    "created_at": "2009-12-24T22:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56434",
    "user": "https://github.com/qed777"
}
```

"I love it when a plan comes together." - [Hannibal](http://en.wikipedia.org/wiki/John_%22Hannibal%22_Smith)

Not quite, perhaps, but we're getting close.  The new published interacts patch sequence (`trac_6855-published_interacts_B*.patch`), based on #7666, is at

* http://sage.math.washington.edu/home/mpatel/trac/6855/

Still to do:

* Give proxy cells an expiration date.
* Proxy worksheet process pool.
* `server_conf` setting.
* Some of the "TODO" items in `twist.py`.

I'm a bit behind schedule --- I think I underestimated the extent of the changes needed.  But I think it was very important, if not necessary, for me to understand more deeply how the many parts of the Sage Notebook *interact*.  We'll get there soon!

Other changes of interest:

* Data sent from server to client is [JSON](http://www.json.org/js.html)-encoded.
* `active_cell_list` is `console.log`ged (or displayed in a floating dialog) *when* it changes.



---

archive/issue_comments_056435.json:
```json
{
    "body": "If there are no objections, I'll delete the older `debug_*` functions and as many of the \"legacy\" browser-specific workarounds as I can find and estimate are highly likely to be unnecessary today.  Most of the modern browsers --- FF3+, Cr4+, IE7/8+, O10+, S4+ --- now have relatively useful built-in debugging tools and new sets of idiosyncrasies.\n\nIn particular, I suggest that we not actively support (and recommend against using) browsers older than FF3, Cr4, IE7/8, O10, S4.  I have access to relatively old (6+ years) 64-bit Fedora Linux and 32-bit Windows XP machines on which I can test most of these.  Combinations I cannot easily test are all browsers on Mac OS X and Windows Vista, IE7 on Windows (apart from IE8 compatibility modes), FF<3.5 on all platforms.  But it seems that browser-to-browser differences on a given platform are typically \"greater\" than platform-to-platform differences for a given browser.\n\nOf course, it's great to receive useful reports \"from the field\" on how the notebook performs in these browsers and their contemporaries!",
    "created_at": "2009-12-25T04:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56435",
    "user": "https://github.com/qed777"
}
```

If there are no objections, I'll delete the older `debug_*` functions and as many of the "legacy" browser-specific workarounds as I can find and estimate are highly likely to be unnecessary today.  Most of the modern browsers --- FF3+, Cr4+, IE7/8+, O10+, S4+ --- now have relatively useful built-in debugging tools and new sets of idiosyncrasies.

In particular, I suggest that we not actively support (and recommend against using) browsers older than FF3, Cr4, IE7/8, O10, S4.  I have access to relatively old (6+ years) 64-bit Fedora Linux and 32-bit Windows XP machines on which I can test most of these.  Combinations I cannot easily test are all browsers on Mac OS X and Windows Vista, IE7 on Windows (apart from IE8 compatibility modes), FF<3.5 on all platforms.  But it seems that browser-to-browser differences on a given platform are typically "greater" than platform-to-platform differences for a given browser.

Of course, it's great to receive useful reports "from the field" on how the notebook performs in these browsers and their contemporaries!



---

archive/issue_comments_056436.json:
```json
{
    "body": "B15 enables cell expiration (\"garbage collection\") for the proxy worksheet process, which can handle multiple concurrent viewers.  Still to do:\n\n* Security: Make recomputing / updating `interact`s send only *data* (e.g., arguments), not call the library functions `_interact_.update` and `_interact_.recompute` directly.  Otherwise, a user can execute arbitrary code (on a private server with working published interacts) by prefixing it with `'%__sage_interact__'`.  This should be straightforward to implement, although I'm not sure about replacing the `sage_eval`s in `interact.py`.  Perhaps we can suppress them in \"public mode\"?\n\n* Allow a worksheet to use a *pool* of `sage` processes to evaluate queued cells [1].  Since we `reset()` after each `interact` update, the main difficulty here is passing a cell's global `_interact_.state` to the process assigned to evaluate the cell.  Can we simplify and store this state in a cell attribute?\n\n[1] Related: Share one compute process among multiple worksheets (cf. #7655).\n\nAnyway, with or without these changes, the logical next step is allocate a `W_remote_proxy` worksheet for *remote* `interact`s analogous to the published `interact`s' `W_pub_proxy`.",
    "created_at": "2009-12-27T01:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56436",
    "user": "https://github.com/qed777"
}
```

B15 enables cell expiration ("garbage collection") for the proxy worksheet process, which can handle multiple concurrent viewers.  Still to do:

* Security: Make recomputing / updating `interact`s send only *data* (e.g., arguments), not call the library functions `_interact_.update` and `_interact_.recompute` directly.  Otherwise, a user can execute arbitrary code (on a private server with working published interacts) by prefixing it with `'%__sage_interact__'`.  This should be straightforward to implement, although I'm not sure about replacing the `sage_eval`s in `interact.py`.  Perhaps we can suppress them in "public mode"?

* Allow a worksheet to use a *pool* of `sage` processes to evaluate queued cells [1].  Since we `reset()` after each `interact` update, the main difficulty here is passing a cell's global `_interact_.state` to the process assigned to evaluate the cell.  Can we simplify and store this state in a cell attribute?

[1] Related: Share one compute process among multiple worksheets (cf. #7655).

Anyway, with or without these changes, the logical next step is allocate a `W_remote_proxy` worksheet for *remote* `interact`s analogous to the published `interact`s' `W_pub_proxy`.



---

archive/issue_comments_056437.json:
```json
{
    "body": "By the way, in B15, `admin` owns `W_pub_proxy`, but with a few small changes, we can make `pub` the owner, hide the worksheet, and allow it to compute.",
    "created_at": "2009-12-27T01:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56437",
    "user": "https://github.com/qed777"
}
```

By the way, in B15, `admin` owns `W_pub_proxy`, but with a few small changes, we can make `pub` the owner, hide the worksheet, and allow it to compute.



---

archive/issue_comments_056438.json:
```json
{
    "body": "B19 abandons the `W_pub_proxy` approach, for now, in favor of the \"docbrowser pool\" approach.  Each has its strengths and weaknesses, I think.  The former is probably better for high-volume/frequency evaluation of self-contained (single-cell) public/remote interacts (e.g., Wikipedia).  But the other approach, since it allocates one process per public/remote page, can handle entire worksheets, with non-trivial state saved between evaluations.\n\nBy the way, it seems the `'doc_pool_size'` server setting does nothing in Sage 4.3, but I've made a first attempt at fixing this.\n\nHow close are we to being able to suspend (to disk) and resume entire Sage sessions with no loss of [essential] information?  One application: \"Shipping\" live worksheets to other servers, e.g., to balance loads or to take temporary advantage of extra flops.",
    "created_at": "2009-12-30T20:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56438",
    "user": "https://github.com/qed777"
}
```

B19 abandons the `W_pub_proxy` approach, for now, in favor of the "docbrowser pool" approach.  Each has its strengths and weaknesses, I think.  The former is probably better for high-volume/frequency evaluation of self-contained (single-cell) public/remote interacts (e.g., Wikipedia).  But the other approach, since it allocates one process per public/remote page, can handle entire worksheets, with non-trivial state saved between evaluations.

By the way, it seems the `'doc_pool_size'` server setting does nothing in Sage 4.3, but I've made a first attempt at fixing this.

How close are we to being able to suspend (to disk) and resume entire Sage sessions with no loss of [essential] information?  One application: "Shipping" live worksheets to other servers, e.g., to balance loads or to take temporary advantage of extra flops.



---

archive/issue_comments_056439.json:
```json
{
    "body": "With V23, `interact` update / recompute requests contain just data.  Still to do: Tame `sage_eval`s for public use.",
    "created_at": "2010-01-03T16:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56439",
    "user": "https://github.com/qed777"
}
```

With V23, `interact` update / recompute requests contain just data.  Still to do: Tame `sage_eval`s for public use.



---

archive/issue_comments_056440.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-17T19:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56440",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056441.json:
```json
{
    "body": "Published interacts apparently are there (but highly recommended not to be used), while the [Sage cell server](http://sagecell.sagemath.org/) very admirably enables embedding - probably using a lot of the same ideas here, in principle.  There is so much awesome work here, but I just feel like it has gone nowhere in many years so it is probably better to close it, since the main goal is indeed available.",
    "created_at": "2014-09-17T19:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56441",
    "user": "https://github.com/kcrisman"
}
```

Published interacts apparently are there (but highly recommended not to be used), while the [Sage cell server](http://sagecell.sagemath.org/) very admirably enables embedding - probably using a lot of the same ideas here, in principle.  There is so much awesome work here, but I just feel like it has gone nowhere in many years so it is probably better to close it, since the main goal is indeed available.



---

archive/issue_comments_056442.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-17T19:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56442",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056443.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-09-18T17:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6855#issuecomment-56443",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_007088.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-09-18T17:57:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6855",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6855#event-7088"
}
```
