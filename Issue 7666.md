# Issue 7666: Alphanumeric cell IDs

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-12-11 20:25:16

Assignee: was

CC:  was timdumol boothby mhansen

Preparatory work for #6855.


---

Comment by mpatel created at 2009-12-14 17:02:22

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-12-14 17:30:40

Please the commit string for a brief summary.  Other notes:

 * Depends on #7483, #7482, #7514, #7650, #7269.  Negligible dependence on #7648.

 * It seems that auto-indentation was already broken in IE8.  V9 does not fix the problem.

 * Possible CSS problem: The rendered completions menu is just two columns (not characters) wide in IE8 and O10.

 * On introspection:  I think I've reproduced most of the standard behavior.  New: Pressing `TAB` for explicitly requested docstrings or source code toggles between both.

 * We might use [jQuery's data store](http://docs.jquery.com/Internals) to keep cells and their variables together.

 * IE8 CPU problem:  jsMath seems to be involved, somehow.  Try `factor(factorial(100))`, say, and scrolling up and down.


---

Comment by mpatel created at 2009-12-15 21:52:08

A pre-existing bug:

 * "Evaluate All" cells in a worksheet.
 * Evaluate the last cell.
 * A new cell is not automatically inserted in the notebook.
 * Reload to see the new cell.

?  It seems the client and server cell lists are out of sync.  This might explain the "spontaneously appended cell" phenomenon.


---

Comment by mpatel created at 2009-12-17 11:12:56

In v9, "Evaluate All" can delay the updates of freshly rendered interacts.  I can restore their priority (e.g., _prepend_ their IDs to the `active_cell_list`) here or at #6855.


---

Comment by mpatel created at 2009-12-24 22:06:35

Replying to [comment:3 mpatel]:
> A pre-existing bug:
> [...] 
> ?  It seems the client and server cell lists are out of sync.  This might explain the "spontaneously appended cell" phenomenon.

The "B"-series of patches at #6855 should fix this problem.


---

Comment by mpatel created at 2009-12-28 07:37:07

V10 at

 * http://sage.math.washington.edu/home/mpatel/trac/7666/

is rebased vs. Sage 4.3, SageNB 0.4.8, #7483, #7482, #7514, #7650, #7269.


---

Comment by mpatel created at 2010-01-02 00:02:48

The latest, V13, is rebased vs. #7811.


---

Comment by mpatel created at 2010-01-05 01:00:09

I'll stop pre-emptively rebasing this patch, for now.  Just let me know, if/when it's time.


---

Comment by was created at 2010-01-05 04:01:59

mpatel -- fyi, Tom Boothby is going to help get this work into Sage very soon...


---

Comment by mpatel created at 2010-01-05 09:03:29

That's great!  I should still rebase the patch and include a few corrections from #6855's "B" series.  Remarks:

 * I've made many changes, it seems.  Absolutely no offense is intended. 
 * It's likely the introspection rewrite is just a first step.
 * The JS functions are not consistently documented.  I hope to fix this in a future ticket.
 * It's likely that many Selenium tests on non-FF browsers will now fail.  (Selenium is problematic, not everyone is testing them, etc.)  I won't fix them here.
 * I think we can write/use a simple JS _doctesting_ framework for non-{DOM, network} functions, but this should be a separate ticket.


---

Comment by mpatel created at 2010-01-06 13:01:26

Just a quick note:  I'm working on breaking this up into more manageable pieces.


---

Comment by mpatel created at 2010-01-06 15:44:58

Replying to [comment:11 mpatel]:
> Just a quick note:  I'm working on breaking this up into more manageable pieces.
With Tim's permission, I've added the Se test framework changes to #7786.


---

Comment by mpatel created at 2010-01-06 19:43:50

Please see #7858 about setting the `Content-Type` header for dynamic JavaScript files.


---

Comment by mpatel created at 2010-01-07 03:22:56

#7863 applies JSLint to the notebook's auxiliary JS files.


---

Comment by mpatel created at 2010-01-08 20:17:04

If I save `$\alpha$` in a text cell, then edit the cell again, I see `Ë` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.


---

Comment by mpatel created at 2010-01-08 20:17:39

Oops!  Wrong ticket.


---

Comment by mpatel created at 2010-01-08 23:47:28

* Try giving names/labels to cells in the "Edit" window, e.g.,
   {{{
`{{{id=hello|
factor(factorial(37))
///
}}}`
}}}

 * [JSLint](http://www.jslint.com/) is not a compiler, but it can find bugs.  Of course, it helps to start with a reasonably lint-free file!  To do: Look into [Closure Tools](http://code.google.com/closure/).


---

Comment by mpatel created at 2010-01-09 01:25:27

Reminder: Set `proxify` to `false` prior to merge (if we get that far).


---

Comment by rbeezer created at 2010-01-10 06:22:40

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

Comment by mpatel created at 2010-01-10 07:38:05

Replying to [comment:20 rbeezer]:
> mpatel asked if I would test this package.  Some observations follow,  Firefox 3.5.6 on Kubuntu 9.10.
Thanks for your detailed feedback!
> 1.  ESC on introspection seems to be working (a great addition!).  First time I hit 
> 2.  Formatted labels are working in interacts, but now I don't see any output.
I think the JavaScript compressor _may_ be so aggressive that it's changing the semantics of the code.  Could you try this (but don't bother if it's too much trouble):

  * Insert `debug_mode = False` just before `_cache_javascript = None` in `$SAGE_ROOT/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/notebook/js.py`.
  * Restart the server, clear the browser's cache, and test ESC and `interact`s again.

> 3.  Was testing resizing cells on paste:
> (a) paste into a new cell, hit edit key and the pasted text is gone.
This should be easy to fix by also sending the input to the server just after the paste event.
> (b) this one took me a while
I've noticed this, too.  The server code and JS library use different methods to (re)size a cell.  The server does the sizing just before it sends the worksheet to the browser (e.g., on first display, after exiting "Edit" mode, etc.), but the browser resizes in between.  I don't know how easy it is to reconcile the methods, but I'll definitely take a closer look.


---

Comment by mpatel created at 2010-01-10 07:41:15

Oops.  That should be `debug_mode = True`.


---

Comment by mpatel created at 2010-01-10 10:07:19

V4 should make it so a cell is resized and saved about 0.25 seconds after a paste event -- using no delay at all is too fast, apparently.

I think unifying the client and server resize methods should be a separate ticket.  Neither of the current methods is optimal.  The server assumes 80-column-wide input cells.  The browser suffers from the problem described above.

I'm not sure what to do about the compressor.  See #7787 and [sage-notebook](http://groups.google.com/group/sage-notebook/msg/7ad2a17f4e0cc972) for potential options.  For now, how about adding .min.js file(s), generated offline with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/)?


---

Comment by mpatel created at 2010-01-10 15:03:24

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

Comment by mpatel created at 2010-01-10 15:42:07

I've updated the [spkg](http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b5.spkg) to V5, too.


---

Comment by timdumol created at 2010-01-17 21:33:26

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-17 21:33:26

Excellent work. Cleans up the library quite well.

I've rebased the patch on a new patch queue, but since the reject is just some empty lines, I'll mark this with a positive review.


```
--- notebook_lib.js
+++ notebook_lib.js
`@``@` -4376,10 +4676,10 `@``@` function decode64(input) {
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

Comment by timdumol created at 2010-01-17 21:33:56

Rebase on a new patch set.


---

Attachment

A few style tweaks.


---

Comment by timdumol created at 2010-01-17 21:35:04

I've attached a few additional style tweaks to be applied on top of the patch. Feel free to review it or ignore it.


---

Comment by mpatel created at 2010-01-18 05:44:58

Combined patch.  See comment.  Apply only this patch.


---

Attachment

I've attached a combined patch that incorporates most of the reviewer patch.  Thanks for further simplifying `handle_introspection`!  If it's OK, I'd like to adhere to [Crockford's one-var-statement-per-function rule (see Scope)](http://www.jslint.com/lint.html), to minimize false positives from JSLint on its "The Good Parts" setting.


---

Comment by timdumol created at 2010-01-18 07:00:01

I think that the rule is made for functions with less than say, 5, variables. Putting all of those declarations in one line is a tad hard to read.


---

Comment by mpatel created at 2010-01-18 07:41:57

B7 does this

```js
function bar() {
    var foo1, foo2, foo3, foo4, foo5, foo6,
        foo7, foo8, foo9, foo10;
    // ...
}
```



---

Attachment

Combined patch.  Apply only this patch.


---

Comment by timdumol created at 2010-01-19 03:28:41

Resolution: fixed
