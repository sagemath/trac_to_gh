# Issue 7666: Alphanumeric cell IDs

archive/issues_007666.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @TimDumol boothby @mwhansen\n\nPreparatory work for #6855.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7666\n\n",
    "created_at": "2009-12-11T20:25:16Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Alphanumeric cell IDs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7666",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @williamstein @TimDumol boothby @mwhansen

Preparatory work for #6855.

Issue created by migration from https://trac.sagemath.org/ticket/7666





---

archive/issue_comments_065570.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-14T17:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65570",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065571.json:
```json
{
    "body": "Please the commit string for a brief summary.  Other notes:\n\n* Depends on #7483, #7482, #7514, #7650, #7269.  Negligible dependence on #7648.\n\n* It seems that auto-indentation was already broken in IE8.  V9 does not fix the problem.\n\n* Possible CSS problem: The rendered completions menu is just two columns (not characters) wide in IE8 and O10.\n\n* On introspection:  I think I've reproduced most of the standard behavior.  New: Pressing `TAB` for explicitly requested docstrings or source code toggles between both.\n\n* We might use [jQuery's data store](http://docs.jquery.com/Internals) to keep cells and their variables together.\n\n* IE8 CPU problem:  jsMath seems to be involved, somehow.  Try `factor(factorial(100))`, say, and scrolling up and down.",
    "created_at": "2009-12-14T17:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65571",
    "user": "https://github.com/qed777"
}
```

Please the commit string for a brief summary.  Other notes:

* Depends on #7483, #7482, #7514, #7650, #7269.  Negligible dependence on #7648.

* It seems that auto-indentation was already broken in IE8.  V9 does not fix the problem.

* Possible CSS problem: The rendered completions menu is just two columns (not characters) wide in IE8 and O10.

* On introspection:  I think I've reproduced most of the standard behavior.  New: Pressing `TAB` for explicitly requested docstrings or source code toggles between both.

* We might use [jQuery's data store](http://docs.jquery.com/Internals) to keep cells and their variables together.

* IE8 CPU problem:  jsMath seems to be involved, somehow.  Try `factor(factorial(100))`, say, and scrolling up and down.



---

archive/issue_comments_065572.json:
```json
{
    "body": "A pre-existing bug:\n\n* \"Evaluate All\" cells in a worksheet.\n* Evaluate the last cell.\n* A new cell is not automatically inserted in the notebook.\n* Reload to see the new cell.\n\n?  It seems the client and server cell lists are out of sync.  This might explain the \"spontaneously appended cell\" phenomenon.",
    "created_at": "2009-12-15T21:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65572",
    "user": "https://github.com/qed777"
}
```

A pre-existing bug:

* "Evaluate All" cells in a worksheet.
* Evaluate the last cell.
* A new cell is not automatically inserted in the notebook.
* Reload to see the new cell.

?  It seems the client and server cell lists are out of sync.  This might explain the "spontaneously appended cell" phenomenon.



---

archive/issue_comments_065573.json:
```json
{
    "body": "In v9, \"Evaluate All\" can delay the updates of freshly rendered interacts.  I can restore their priority (e.g., *prepend* their IDs to the `active_cell_list`) here or at #6855.",
    "created_at": "2009-12-17T11:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65573",
    "user": "https://github.com/qed777"
}
```

In v9, "Evaluate All" can delay the updates of freshly rendered interacts.  I can restore their priority (e.g., *prepend* their IDs to the `active_cell_list`) here or at #6855.



---

archive/issue_comments_065574.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> A pre-existing bug:\n> [...] \n> ?  It seems the client and server cell lists are out of sync.  This might explain the \"spontaneously appended cell\" phenomenon.\n\nThe \"B\"-series of patches at #6855 should fix this problem.",
    "created_at": "2009-12-24T22:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65574",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 mpatel]:
> A pre-existing bug:
> [...] 
> ?  It seems the client and server cell lists are out of sync.  This might explain the "spontaneously appended cell" phenomenon.

The "B"-series of patches at #6855 should fix this problem.



---

archive/issue_comments_065575.json:
```json
{
    "body": "V10 at\n\n* http://sage.math.washington.edu/home/mpatel/trac/7666/\n\nis rebased vs. Sage 4.3, SageNB 0.4.8, #7483, #7482, #7514, #7650, #7269.",
    "created_at": "2009-12-28T07:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65575",
    "user": "https://github.com/qed777"
}
```

V10 at

* http://sage.math.washington.edu/home/mpatel/trac/7666/

is rebased vs. Sage 4.3, SageNB 0.4.8, #7483, #7482, #7514, #7650, #7269.



---

archive/issue_comments_065576.json:
```json
{
    "body": "The latest, V13, is rebased vs. #7811.",
    "created_at": "2010-01-02T00:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65576",
    "user": "https://github.com/qed777"
}
```

The latest, V13, is rebased vs. #7811.



---

archive/issue_comments_065577.json:
```json
{
    "body": "I'll stop pre-emptively rebasing this patch, for now.  Just let me know, if/when it's time.",
    "created_at": "2010-01-05T01:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65577",
    "user": "https://github.com/qed777"
}
```

I'll stop pre-emptively rebasing this patch, for now.  Just let me know, if/when it's time.



---

archive/issue_comments_065578.json:
```json
{
    "body": "mpatel -- fyi, Tom Boothby is going to help get this work into Sage very soon...",
    "created_at": "2010-01-05T04:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65578",
    "user": "https://github.com/williamstein"
}
```

mpatel -- fyi, Tom Boothby is going to help get this work into Sage very soon...



---

archive/issue_comments_065579.json:
```json
{
    "body": "That's great!  I should still rebase the patch and include a few corrections from #6855's \"B\" series.  Remarks:\n\n* I've made many changes, it seems.  Absolutely no offense is intended. \n* It's likely the introspection rewrite is just a first step.\n* The JS functions are not consistently documented.  I hope to fix this in a future ticket.\n* It's likely that many Selenium tests on non-FF browsers will now fail.  (Selenium is problematic, not everyone is testing them, etc.)  I won't fix them here.\n* I think we can write/use a simple JS *doctesting* framework for non-{DOM, network} functions, but this should be a separate ticket.",
    "created_at": "2010-01-05T09:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65579",
    "user": "https://github.com/qed777"
}
```

That's great!  I should still rebase the patch and include a few corrections from #6855's "B" series.  Remarks:

* I've made many changes, it seems.  Absolutely no offense is intended. 
* It's likely the introspection rewrite is just a first step.
* The JS functions are not consistently documented.  I hope to fix this in a future ticket.
* It's likely that many Selenium tests on non-FF browsers will now fail.  (Selenium is problematic, not everyone is testing them, etc.)  I won't fix them here.
* I think we can write/use a simple JS *doctesting* framework for non-{DOM, network} functions, but this should be a separate ticket.



---

archive/issue_comments_065580.json:
```json
{
    "body": "Just a quick note:  I'm working on breaking this up into more manageable pieces.",
    "created_at": "2010-01-06T13:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65580",
    "user": "https://github.com/qed777"
}
```

Just a quick note:  I'm working on breaking this up into more manageable pieces.



---

archive/issue_comments_065581.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> Just a quick note:  I'm working on breaking this up into more manageable pieces.\nWith Tim's permission, I've added the Se test framework changes to #7786.",
    "created_at": "2010-01-06T15:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65581",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:11 mpatel]:
> Just a quick note:  I'm working on breaking this up into more manageable pieces.
With Tim's permission, I've added the Se test framework changes to #7786.



---

archive/issue_comments_065582.json:
```json
{
    "body": "Please see #7858 about setting the `Content-Type` header for dynamic JavaScript files.",
    "created_at": "2010-01-06T19:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65582",
    "user": "https://github.com/qed777"
}
```

Please see #7858 about setting the `Content-Type` header for dynamic JavaScript files.



---

archive/issue_comments_065583.json:
```json
{
    "body": "#7863 applies JSLint to the notebook's auxiliary JS files.",
    "created_at": "2010-01-07T03:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65583",
    "user": "https://github.com/qed777"
}
```

#7863 applies JSLint to the notebook's auxiliary JS files.



---

archive/issue_comments_065584.json:
```json
{
    "body": "If I save `$\\alpha$` in a text cell, then edit the cell again, I see `\u00cb` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.",
    "created_at": "2010-01-08T20:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65584",
    "user": "https://github.com/qed777"
}
```

If I save `$\alpha$` in a text cell, then edit the cell again, I see `Ë` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.



---

archive/issue_comments_065585.json:
```json
{
    "body": "Oops!  Wrong ticket.",
    "created_at": "2010-01-08T20:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65585",
    "user": "https://github.com/qed777"
}
```

Oops!  Wrong ticket.



---

archive/issue_comments_065586.json:
```json
{
    "body": "* Try giving names/labels to cells in the \"Edit\" window, e.g.,\n   {{{\n`{{{id=hello|\nfactor(factorial(37))\n///\n}}}`\n}}}\n\n* [JSLint](http://www.jslint.com/) is not a compiler, but it can find bugs.  Of course, it helps to start with a reasonably lint-free file!  To do: Look into [Closure Tools](http://code.google.com/closure/).",
    "created_at": "2010-01-08T23:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65586",
    "user": "https://github.com/qed777"
}
```

* Try giving names/labels to cells in the "Edit" window, e.g.,
   {{{
`{{{id=hello|
factor(factorial(37))
///
}}}`
}}}

* [JSLint](http://www.jslint.com/) is not a compiler, but it can find bugs.  Of course, it helps to start with a reasonably lint-free file!  To do: Look into [Closure Tools](http://code.google.com/closure/).



---

archive/issue_comments_065587.json:
```json
{
    "body": "Reminder: Set `proxify` to `false` prior to merge (if we get that far).",
    "created_at": "2010-01-09T01:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65587",
    "user": "https://github.com/qed777"
}
```

Reminder: Set `proxify` to `false` prior to merge (if we get that far).



---

archive/issue_comments_065588.json:
```json
{
    "body": "mpatel asked if I would test this package.  Some observations follow,  Firefox 3.5.6 on Kubuntu 9.10.\n\n1.  ESC on introspection seems to be working (a great addition!).  First time I hit ESC it didn't seem to have effect, then next tab-completion was weird, then all subsequent uses of ESC worked fine.  Opened a new worksheet, and several uses of ESC worked fine.  So maybe just once per server session?\n\n2.  Formatted labels are working in interacts, but now I don't see any output.  Three different interacts, no output at all.  Controls are functional though, so it is not hung.\n\n3.  Was testing resizing cells on paste:\n\n(a) paste into a new cell, hit edit key and the pasted text is gone.\n\n(b) this one took me a while\n- make a new cell, type a space, then type a sentence almost to the far end of the cell.\n\n- resize browser window by grabbing right edge and dragging left (slowly)\n\n- resize until just the last word of sentence wraps to a new line.\n\n- cell doesn't resize and second line is hidden\n\n- hit edit, cancel changes, see cell is now sized right\n\n- click into cell, it sizes wrong again\n\n\nWithout a space at the start of the line, sometimes there's no problem.  Notice if you keep sliding the window edge, and push two words onto the next line, the sizing comes back to being right.",
    "created_at": "2010-01-10T06:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65588",
    "user": "https://github.com/rbeezer"
}
```

mpatel asked if I would test this package.  Some observations follow,  Firefox 3.5.6 on Kubuntu 9.10.

1.  ESC on introspection seems to be working (a great addition!).  First time I hit ESC it didn't seem to have effect, then next tab-completion was weird, then all subsequent uses of ESC worked fine.  Opened a new worksheet, and several uses of ESC worked fine.  So maybe just once per server session?

2.  Formatted labels are working in interacts, but now I don't see any output.  Three different interacts, no output at all.  Controls are functional though, so it is not hung.

3.  Was testing resizing cells on paste:

(a) paste into a new cell, hit edit key and the pasted text is gone.

(b) this one took me a while
- make a new cell, type a space, then type a sentence almost to the far end of the cell.

- resize browser window by grabbing right edge and dragging left (slowly)

- resize until just the last word of sentence wraps to a new line.

- cell doesn't resize and second line is hidden

- hit edit, cancel changes, see cell is now sized right

- click into cell, it sizes wrong again


Without a space at the start of the line, sometimes there's no problem.  Notice if you keep sliding the window edge, and push two words onto the next line, the sizing comes back to being right.



---

archive/issue_comments_065589.json:
```json
{
    "body": "Replying to [comment:20 rbeezer]:\n> mpatel asked if I would test this package.  Some observations follow,  Firefox 3.5.6 on Kubuntu 9.10.\nThanks for your detailed feedback!\n> 1.  ESC on introspection seems to be working (a great addition!).  First time I hit \n> 2.  Formatted labels are working in interacts, but now I don't see any output.\nI think the JavaScript compressor *may* be so aggressive that it's changing the semantics of the code.  Could you try this (but don't bother if it's too much trouble):\n\n* Insert `debug_mode = False` just before `_cache_javascript = None` in `$SAGE_ROOT/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/notebook/js.py`.\n* Restart the server, clear the browser's cache, and test ESC and `interact`s again.\n\n> 3.  Was testing resizing cells on paste:\n> (a) paste into a new cell, hit edit key and the pasted text is gone.\nThis should be easy to fix by also sending the input to the server just after the paste event.\n> (b) this one took me a while\nI've noticed this, too.  The server code and JS library use different methods to (re)size a cell.  The server does the sizing just before it sends the worksheet to the browser (e.g., on first display, after exiting \"Edit\" mode, etc.), but the browser resizes in between.  I don't know how easy it is to reconcile the methods, but I'll definitely take a closer look.",
    "created_at": "2010-01-10T07:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65589",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:20 rbeezer]:
> mpatel asked if I would test this package.  Some observations follow,  Firefox 3.5.6 on Kubuntu 9.10.
Thanks for your detailed feedback!
> 1.  ESC on introspection seems to be working (a great addition!).  First time I hit 
> 2.  Formatted labels are working in interacts, but now I don't see any output.
I think the JavaScript compressor *may* be so aggressive that it's changing the semantics of the code.  Could you try this (but don't bother if it's too much trouble):

* Insert `debug_mode = False` just before `_cache_javascript = None` in `$SAGE_ROOT/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/notebook/js.py`.
* Restart the server, clear the browser's cache, and test ESC and `interact`s again.

> 3.  Was testing resizing cells on paste:
> (a) paste into a new cell, hit edit key and the pasted text is gone.
This should be easy to fix by also sending the input to the server just after the paste event.
> (b) this one took me a while
I've noticed this, too.  The server code and JS library use different methods to (re)size a cell.  The server does the sizing just before it sends the worksheet to the browser (e.g., on first display, after exiting "Edit" mode, etc.), but the browser resizes in between.  I don't know how easy it is to reconcile the methods, but I'll definitely take a closer look.



---

archive/issue_comments_065590.json:
```json
{
    "body": "Oops.  That should be `debug_mode = True`.",
    "created_at": "2010-01-10T07:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65590",
    "user": "https://github.com/qed777"
}
```

Oops.  That should be `debug_mode = True`.



---

archive/issue_comments_065591.json:
```json
{
    "body": "V4 should make it so a cell is resized and saved about 0.25 seconds after a paste event -- using no delay at all is too fast, apparently.\n\nI think unifying the client and server resize methods should be a separate ticket.  Neither of the current methods is optimal.  The server assumes 80-column-wide input cells.  The browser suffers from the problem described above.\n\nI'm not sure what to do about the compressor.  See #7787 and [sage-notebook](http://groups.google.com/group/sage-notebook/msg/7ad2a17f4e0cc972) for potential options.  For now, how about adding .min.js file(s), generated offline with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/)?",
    "created_at": "2010-01-10T10:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65591",
    "user": "https://github.com/qed777"
}
```

V4 should make it so a cell is resized and saved about 0.25 seconds after a paste event -- using no delay at all is too fast, apparently.

I think unifying the client and server resize methods should be a separate ticket.  Neither of the current methods is optimal.  The server assumes 80-column-wide input cells.  The browser suffers from the problem described above.

I'm not sure what to do about the compressor.  See #7787 and [sage-notebook](http://groups.google.com/group/sage-notebook/msg/7ad2a17f4e0cc972) for potential options.  For now, how about adding .min.js file(s), generated offline with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/)?



---

archive/issue_comments_065592.json:
```json
{
    "body": "Found the problem: The `JavaScriptCompressor` converts, in effect,\n\n```js\nfunction foo() {\n    return 'hello';\n}\n```\n\nto\n\n```js\nfunction foo(){return \n'hello'\n;}\n```\n\nBut\n\n  [In JavaScript, a linefeed can be whitespace or it can act as a semicolon. This replaces one ambiguity with another.](http://www.jslint.com/lint.html)\n\nIn particular, if I execute `foo();`, the former returns `'hello'` and latter returns `undefined`.  I've modified the compressor in V5 so that it does not insert extra `'\\n'`s.  Of course, we should replace this with an free / open source, stable, Pythonic minifier (see above), when we can.  By the way, the YUI Compressor yields\n\n```js\nfunction foo(){return\"hello\"}\n```\n",
    "created_at": "2010-01-10T15:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65592",
    "user": "https://github.com/qed777"
}
```

Found the problem: The `JavaScriptCompressor` converts, in effect,

```js
function foo() {
    return 'hello';
}
```

to

```js
function foo(){return 
'hello'
;}
```

But

  [In JavaScript, a linefeed can be whitespace or it can act as a semicolon. This replaces one ambiguity with another.](http://www.jslint.com/lint.html)

In particular, if I execute `foo();`, the former returns `'hello'` and latter returns `undefined`.  I've modified the compressor in V5 so that it does not insert extra `'\n'`s.  Of course, we should replace this with an free / open source, stable, Pythonic minifier (see above), when we can.  By the way, the YUI Compressor yields

```js
function foo(){return"hello"}
```




---

archive/issue_comments_065593.json:
```json
{
    "body": "I've updated the [spkg](http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b5.spkg) to V5, too.",
    "created_at": "2010-01-10T15:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65593",
    "user": "https://github.com/qed777"
}
```

I've updated the [spkg](http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b5.spkg) to V5, too.



---

archive/issue_comments_065594.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T21:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65594",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065595.json:
```json
{
    "body": "Excellent work. Cleans up the library quite well.\n\nI've rebased the patch on a new patch queue, but since the reject is just some empty lines, I'll mark this with a positive review.\n\n\n```\n--- notebook_lib.js\n+++ notebook_lib.js\n@@ -4376,10 +4676,10 @@ function decode64(input) {\n     return output;\n }\n \n+\n ///////////////////////////////////////////////////////////////////\n // Trash\n ///////////////////////////////////////////////////////////////////\n-\n function empty_trash() {\n     /*\n     Empties the trash folder, after asking for confirmation.\n```\n\n\nThe new patch queue is:\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\n```\n",
    "created_at": "2010-01-17T21:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65595",
    "user": "https://github.com/TimDumol"
}
```

Excellent work. Cleans up the library quite well.

I've rebased the patch on a new patch queue, but since the reject is just some empty lines, I'll mark this with a positive review.


```
--- notebook_lib.js
+++ notebook_lib.js
@@ -4376,10 +4676,10 @@ function decode64(input) {
     return output;
 }
 
+
 ///////////////////////////////////////////////////////////////////
 // Trash
 ///////////////////////////////////////////////////////////////////
-
 function empty_trash() {
     /*
     Empties the trash folder, after asking for confirmation.
```


The new patch queue is:


```
trac_7650-sagenb_doctesting_v6.patch
trac_7650-reviewer.patch
trac_7648-missing_indent.patch
trac_7663-rstrip_prompt.patch
trac_7847-empty-trash-no-referer.patch
trac_7786-template-jinja-idiomatic.patch
trac_7863-declare_vars_aux_js_v2.patch
trac_7874-typeset_interact_labels.patch
trac_7858-key_binding_vars_v2.patch
trac_7666-alphanumeric_cell_ids_B5.patch
```




---

archive/issue_comments_065596.json:
```json
{
    "body": "Rebase on a new patch set.",
    "created_at": "2010-01-17T21:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65596",
    "user": "https://github.com/TimDumol"
}
```

Rebase on a new patch set.



---

archive/issue_comments_065597.json:
```json
{
    "body": "Attachment [trac_7666-reviewer.patch](tarball://root/attachments/some-uuid/ticket7666/trac_7666-reviewer.patch) by @TimDumol created at 2010-01-17 21:34:35\n\nA few style tweaks.",
    "created_at": "2010-01-17T21:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65597",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7666-reviewer.patch](tarball://root/attachments/some-uuid/ticket7666/trac_7666-reviewer.patch) by @TimDumol created at 2010-01-17 21:34:35

A few style tweaks.



---

archive/issue_comments_065598.json:
```json
{
    "body": "I've attached a few additional style tweaks to be applied on top of the patch. Feel free to review it or ignore it.",
    "created_at": "2010-01-17T21:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65598",
    "user": "https://github.com/TimDumol"
}
```

I've attached a few additional style tweaks to be applied on top of the patch. Feel free to review it or ignore it.



---

archive/issue_comments_065599.json:
```json
{
    "body": "Combined patch.  See comment.  Apply only this patch.",
    "created_at": "2010-01-18T05:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65599",
    "user": "https://github.com/qed777"
}
```

Combined patch.  See comment.  Apply only this patch.



---

archive/issue_comments_065600.json:
```json
{
    "body": "Attachment [trac_7666-alphanumeric_cell_ids_B6.patch](tarball://root/attachments/some-uuid/ticket7666/trac_7666-alphanumeric_cell_ids_B6.patch) by @qed777 created at 2010-01-18 06:05:59\n\nI've attached a combined patch that incorporates most of the reviewer patch.  Thanks for further simplifying `handle_introspection`!  If it's OK, I'd like to adhere to [Crockford's one-var-statement-per-function rule (see Scope)](http://www.jslint.com/lint.html), to minimize false positives from JSLint on its \"The Good Parts\" setting.",
    "created_at": "2010-01-18T06:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65600",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7666-alphanumeric_cell_ids_B6.patch](tarball://root/attachments/some-uuid/ticket7666/trac_7666-alphanumeric_cell_ids_B6.patch) by @qed777 created at 2010-01-18 06:05:59

I've attached a combined patch that incorporates most of the reviewer patch.  Thanks for further simplifying `handle_introspection`!  If it's OK, I'd like to adhere to [Crockford's one-var-statement-per-function rule (see Scope)](http://www.jslint.com/lint.html), to minimize false positives from JSLint on its "The Good Parts" setting.



---

archive/issue_comments_065601.json:
```json
{
    "body": "I think that the rule is made for functions with less than say, 5, variables. Putting all of those declarations in one line is a tad hard to read.",
    "created_at": "2010-01-18T07:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65601",
    "user": "https://github.com/TimDumol"
}
```

I think that the rule is made for functions with less than say, 5, variables. Putting all of those declarations in one line is a tad hard to read.



---

archive/issue_comments_065602.json:
```json
{
    "body": "B7 does this\n\n```js\nfunction bar() {\n    var foo1, foo2, foo3, foo4, foo5, foo6,\n        foo7, foo8, foo9, foo10;\n    // ...\n}\n```\n",
    "created_at": "2010-01-18T07:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65602",
    "user": "https://github.com/qed777"
}
```

B7 does this

```js
function bar() {
    var foo1, foo2, foo3, foo4, foo5, foo6,
        foo7, foo8, foo9, foo10;
    // ...
}
```




---

archive/issue_comments_065603.json:
```json
{
    "body": "Attachment [trac_7666-alphanumeric_cell_ids_B7.patch](tarball://root/attachments/some-uuid/ticket7666/trac_7666-alphanumeric_cell_ids_B7.patch) by @qed777 created at 2010-01-18 07:42:43\n\nCombined patch.  Apply only this patch.",
    "created_at": "2010-01-18T07:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65603",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7666-alphanumeric_cell_ids_B7.patch](tarball://root/attachments/some-uuid/ticket7666/trac_7666-alphanumeric_cell_ids_B7.patch) by @qed777 created at 2010-01-18 07:42:43

Combined patch.  Apply only this patch.



---

archive/issue_comments_065604.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7666#issuecomment-65604",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed
