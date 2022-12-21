# Issue 6855: [with patch, needs work] Enable interacts in published worksheets

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-09-01 12:31:09

Assignee: boothby

CC:  was

Worksheets in the Sage notebook can contain live `interact`-ive cells, which may make it easier to understand how an object's properties depend on a set of parameters.

Please visit the Sage Wiki to view [some examples](http://wiki.sagemath.org/interact).

Currently, `interact` cells do not work in published worksheets.


---

Comment by mpatel created at 2009-09-11 08:46:54

Changing priority from minor to major.


---

Comment by mpatel created at 2009-09-11 16:23:49

Note: See #6897 about The Great Django Migration and for potentially very relevant links.


---

Comment by mpatel created at 2009-09-11 17:36:41

For live cells embedded remotely or in published worksheets, we may need to handle concurrent access, permissions, usage limits, etc.  From this perspective, an asynchronous, event-driven, long-polling, stateless model is quite appealing.  See, e.g.,

 * [Comet](http://en.wikipedia.org/wiki/Comet_%28programming%29Comet)
 * [Django](http://docs.djangoproject.com/en/dev/)
 * [Orbited](http://orbited.org/wiki/Documentation)
 * [Tornado](http://www.tornadoweb.org/documentation) 
 * [Twisted](http://twistedmatrix.com/trac/wiki/Documentation) 
 * [Python / Cython resources](http://wiki.sagemath.org/PythonResources) - Sage wiki.

Note: It's not difficult to make the server respond to a browser's request *only after* it has evaluated the input.  But in the simplest approach, the server *blocks,* unable to answer other clients, while the sage instance ruminates.


---

Comment by mpatel created at 2009-11-26 02:14:52

Non-concurrent first version.  sagenb repo.


---

Attachment

The [attachment:trac_6855-published_interacts.patch patch] enables interacts in published worksheets.  Still to do:

 * Gracefully handle simultaneous access by multiple clients.
 * Find an alternative to `twist.prep_interact` for rendering the interacts upon load.


---

Comment by mpatel created at 2009-11-26 02:38:53

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

Comment by mpatel created at 2009-11-26 02:56:33

Concurrent access possibilities, not necessarily mutex:

 * Use a process pool, with some limit, to evaluate queued cells.
 * Go stateless - always `reset()` after evaluating a cell.
 * Allocate a new cell, with a unique ID, for each evaluation.  Pass this ID back to the browser, so it can poll for updates.  Delete the temporaries, incrementally, and/or all at once when the "idle" check fails.


---

Comment by mpatel created at 2009-11-26 02:59:53

Replying to [comment:6 mpatel]:
> [...] Still to do:
>  * Gracefully handle simultaneous access by multiple clients.

See the previous comment.

>  * Find an alternative to `twist.prep_interact` for rendering the interacts upon load.

Save and serve the rendered HTML.


---

Attachment

Rebased vs. rebased #4714.  Updated commit message.  Only this one.  sagenb repo.


---

Comment by mpatel created at 2009-11-26 07:03:19


```
[...as above...]
sagenb_3849.patch
trac_4714-sagenb_jsmath_init.patch
trac_6855-published_interacts.patch
```



---

Comment by mpatel created at 2009-12-03 11:17:41

Updated patches are available here:

 * [http://sage.math.washington.edu/home/mpatel/trac/6855/](http://sage.math.washington.edu/home/mpatel/trac/6855/)

There's still plenty to do, but I'm making progress.  Version 10:

 * Should allow alphanumeric cell ids.  "Integers" project to integers (e.g., `'0'` is `0`, `"19"` is `19`, etc.).  In particular, we can continue to use non-negative integers for ordinary compute/text cells.  But cells whose ids begin with a non-integer character are [optionally] "special" (e.g., `'tmp123'` is `'tmp123'`).  They should have wider applicability than published and remote embedded interacts.  For example, we could use "g" cells to communicate graph data bidirectionally (cf. #1321), "p" cells for plots, "i" cells for introspection, and so on.

 * Should contain *far less* [JSLint](http://www.jslint.com/).  This was painful, but it was very useful --- it revealed subtle (to me, at least) problems, potential and actual.

 * Subsumes #5644.  This required rewriting most of the introspection functions.  Now each cell has it's own set of introspection variables, but they're all stored in just one global dictionary `introspect`.  Reducing our global footprint (and the probability of library conflicts) is important for embedding worksheets, but I don't plan to take this further just now.

Note: I still need to test browsers other than FF 3.5.5 on Linux.


---

Comment by mpatel created at 2009-12-05 17:25:48

V14 gets (all but one of the) [Selenium](http://seleniumhq.org/) ([Grid](http://selenium-grid.seleniumhq.org/)) test to pass in

 * Linux: FF3.5.
 * Windows XP: FF3.5, IE8, O10.

Several tests fail in Chrome on XP --- `self.logout()` raises the complaint, ["This webpage has a redirect loop."](http://www.google.com/search?q=%22This%20webpage%20has%20a%20redirect%20loop.%22)  I think this is a Chrome bug.

Safari on XP interprets, e.g., `/home/mike/0/` as the local resource `file:///home/mike/0/`, which it refuses to load.  I think this is a Selenium bug.

But both Chrome and Safari sometimes display `Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again.`  Could this be a SageNB bug?

Selenium is far from consistent in its ability to fire "special" keyboard events (e.g., `tab`, `shift-enter`), so I've substituted notebook JS functions, for now.


---

Comment by mpatel created at 2009-12-24 22:02:20

"I love it when a plan comes together." - [Hannibal](http://en.wikipedia.org/wiki/John_%22Hannibal%22_Smith)

Not quite, perhaps, but we're getting close.  The new published interacts patch sequence (`trac_6855-published_interacts_B*.patch`), based on #7666, is at

 * http://sage.math.washington.edu/home/mpatel/trac/6855/

Still to do:

 * Give proxy cells an expiration date.
 * Proxy worksheet process pool.
 * `server_conf` setting.
 * Some of the "TODO" items in `twist.py`.

I'm a bit behind schedule --- I think I underestimated the extent of the changes needed.  But I think it was very important, if not necessary, for me to understand more deeply how the many parts of the Sage Notebook _interact_.  We'll get there soon!

Other changes of interest:

 * Data sent from server to client is [JSON](http://www.json.org/js.html)-encoded.
 * `active_cell_list` is `console.log`ged (or displayed in a floating dialog) _when_ it changes.


---

Comment by mpatel created at 2009-12-25 04:29:03

If there are no objections, I'll delete the older `debug_*` functions and as many of the "legacy" browser-specific workarounds as I can find and estimate are highly likely to be unnecessary today.  Most of the modern browsers --- FF3+, Cr4+, IE7/8+, O10+, S4+ --- now have relatively useful built-in debugging tools and new sets of idiosyncrasies.

In particular, I suggest that we not actively support (and recommend against using) browsers older than FF3, Cr4, IE7/8, O10, S4.  I have access to relatively old (6+ years) 64-bit Fedora Linux and 32-bit Windows XP machines on which I can test most of these.  Combinations I cannot easily test are all browsers on Mac OS X and Windows Vista, IE7 on Windows (apart from IE8 compatibility modes), FF<3.5 on all platforms.  But it seems that browser-to-browser differences on a given platform are typically "greater" than platform-to-platform differences for a given browser.

Of course, it's great to receive useful reports "from the field" on how the notebook performs in these browsers and their contemporaries!


---

Comment by mpatel created at 2009-12-27 01:01:08

B15 enables cell expiration ("garbage collection") for the proxy worksheet process, which can handle multiple concurrent viewers.  Still to do:

 * Security: Make recomputing / updating `interact`s send only _data_ (e.g., arguments), not call the library functions `_interact_.update` and `_interact_.recompute` directly.  Otherwise, a user can execute arbitrary code (on a private server with working published interacts) by prefixing it with `'%__sage_interact__'`.  This should be straightforward to implement, although I'm not sure about replacing the `sage_eval`s in `interact.py`.  Perhaps we can suppress them in "public mode"?

 * Allow a worksheet to use a _pool_ of `sage` processes to evaluate queued cells [1].  Since we `reset()` after each `interact` update, the main difficulty here is passing a cell's global `_interact_.state` to the process assigned to evaluate the cell.  Can we simplify and store this state in a cell attribute?

[1] Related: Share one compute process among multiple worksheets (cf. #7655).

Anyway, with or without these changes, the logical next step is allocate a `W_remote_proxy` worksheet for _remote_ `interact`s analogous to the published `interact`s' `W_pub_proxy`.


---

Comment by mpatel created at 2009-12-27 01:07:56

By the way, in B15, `admin` owns `W_pub_proxy`, but with a few small changes, we can make `pub` the owner, hide the worksheet, and allow it to compute.


---

Comment by mpatel created at 2009-12-30 20:17:19

B19 abandons the `W_pub_proxy` approach, for now, in favor of the "docbrowser pool" approach.  Each has its strengths and weaknesses, I think.  The former is probably better for high-volume/frequency evaluation of self-contained (single-cell) public/remote interacts (e.g., Wikipedia).  But the other approach, since it allocates one process per public/remote page, can handle entire worksheets, with non-trivial state saved between evaluations.

By the way, it seems the `'doc_pool_size'` server setting does nothing in Sage 4.3, but I've made a first attempt at fixing this.

How close are we to being able to suspend (to disk) and resume entire Sage sessions with no loss of [essential] information?  One application: "Shipping" live worksheets to other servers, e.g., to balance loads or to take temporary advantage of extra flops.


---

Comment by mpatel created at 2010-01-03 16:32:12

With V23, `interact` update / recompute requests contain just data.  Still to do: Tame `sage_eval`s for public use.


---

Comment by kcrisman created at 2014-09-17 19:02:11

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-09-17 19:02:11

Published interacts apparently are there (but highly recommended not to be used), while the [Sage cell server](http://sagecell.sagemath.org/) very admirably enables embedding - probably using a lot of the same ideas here, in principle.  There is so much awesome work here, but I just feel like it has gone nowhere in many years so it is probably better to close it, since the main goal is indeed available.


---

Comment by kcrisman created at 2014-09-17 19:02:20

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-18 17:57:44

Resolution: fixed
