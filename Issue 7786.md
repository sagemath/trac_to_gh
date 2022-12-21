# Issue 7786: Restructure templates to idiomatic Jinja

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-12-29 09:19:36

Assignee: was

CC:  mpatel was

By idiomatic Jinja, I mean

* Inheritance instead of inclusion

* Arguments required are only the needed models to produce the required view [1]

This will make editing the templates easier, and will allow for a more consistent interface (by specifying base templates for each section).

[1] [Model-View-Controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)


---

Attachment

Preliminary work. Worksheet pages not yet done.


---

Attachment

Converts template structure to an inheritance based tree. Apply this patch alone to sagenb repo.


---

Comment by timdumol created at 2010-01-02 07:38:52

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-02 07:38:52

This is a big patch that makes the template structure more consistent by using inheritance. It also removes a lot of non-semantic markup (<br />, <hr />, etc.). Please note that there are some visual changes (font stack, bar below banner at login.html, headers instead of bold tags at login.html, etc.). I hope they're not too major. Kindly note any changes that are too big and may require consultation at the mailing list.


---

Comment by timdumol created at 2010-01-02 08:54:50

Note: Depends on #7269, #7650, and dependencies.


---

Comment by mpatel created at 2010-01-02 09:52:59

I can only look at the patch right now, but I think these are much-needed and appreciated changes to SageNB.  I think we should make merging this ticket (plus its dependencies) a priority.  I'll try to start reviewing the patch soon.

As the merge nears, I'll rebase #7666 and its descendants, as necessary.


---

Attachment

Rebased on #7650 and its dependencies. Apply this patch alone to sagenb repo.


---

Comment by timdumol created at 2010-01-02 19:08:40

Rebased on #7650 and its dependencies. Apply this patch alone to sagenb repo.


---

Attachment

Updates `source_code.html` and adds styling for it. Also adds a warning to the .css files.


---

Attachment

Adds missing div_wrap argument to template call at `Cell.html()`


---

Comment by mpatel created at 2010-01-05 01:36:36

V4 applies cleanly to 4.3.1.alpha0 + #7650's latest.  With this configuration, I see

 * Se test errors:
   * 4050: `Exception: Timed out after 30000ms`
   * 7433: `Exception: ERROR: Element link=Sign out not found`
   * 3960, 7433, 7428, 7444, searching_for_worksheets: `Exception: ERROR: Element link=Worksheet not found`

 * Doctests:
   * Failures: `challenge.py`, `template.py`, `worksheet.py`.
   * Memory-leak(?): `cell.py`.


---

Comment by mpatel created at 2010-01-05 03:33:31

* "Home" page contains "Toggle" link.
 * Printed/published worksheets: Click bar is visible (on hover).  Clicking adds a cell, which appears to be editable.
 * Upon opening a worksheet: all existing input cells appear to have the same size.
 * Docbrowser worksheets:
   * Extra clickbar at top.
   * Shift-click is not disabled.


---

Comment by mpatel created at 2010-01-05 09:19:14

* Minor: Message at top of `main.sass` should also refer to the `readme.txt` (cf. `test_report.sass`.
 * Just Se test 4050 fails with

```
trac_7843-cell_listdir.patch
trac_7844-notebook_address.patch
trac_7847-empty_trash_ie_ff.patch
trac_7846-no_CODE_PY_symlinks.patch
trac_7650-sagenb_doctesting_v3.patch
trac_7786-template-jinja-idiomatic.4.patch
```


  !


---

Comment by mpatel created at 2010-01-05 10:23:53

* Actually, 4050 gives the same _error_ (i.e., not a failure) as above.
 * `js.py` does not compress `main.js`.
 * `'Error:'` --> `'Error: '` on the Sign in page.
 * Ratings:
   * Unrated worksheets are rated -1.0, it seems.
   * A worksheet's ratings page shows "rating[0]" under User and "rating[1]" under "Rating."
   * Out of curiosity: Is there a maximum comment length?


---

Comment by mpatel created at 2010-01-05 12:38:56

Simple Jinja template dependency graph worksheet.  Not a patch.


---

Attachment

The [attachment:jinja_template_deps.html attached worksheet] (just paste it into an "Edit" window) generates a template dependency graph in Sage.  I'm sure there are many improvements to make, but I hope it's a useful start.  By the way, the last non-empty cell requires [Graphviz's](http://www.graphviz.org/) `dot`.


---

Comment by mpatel created at 2010-01-05 12:51:16

* It seems there are two `account_recovery.html` pages.


---

Comment by mpatel created at 2010-01-05 13:17:51

Actually, [Graph.plot's](http://www.sagemath.org/doc/reference/sage/graphs/graph.html#sage.graphs.graph.GenericGraph.plot) `partition` option may be a better choice for coloring vertices.  Anyway, have fun!


---

Comment by mpatel created at 2010-01-05 17:03:35

Hi Tim -- Do you mind if I make a separate, commuting patch here of just changes under `sagenb/testing`?  If it's OK, I'd like to incorporate some changes I made at #7666, including running a test(s) by name (e.g., `rt.run_any(['4088', 'test_3711'], verbosity=1)`) and making it easier to test other browsers (e.g., first steps toward enabling Selenium Grid).  Actually getting the tests to pass in the other browsers --- I found this very tedious / time-consuming --- we can leave for another ticket.


---

Comment by timdumol created at 2010-01-05 18:04:08

Sure, no problem.


---

Comment by timdumol created at 2010-01-05 19:11:58

By the way, the dependency graph is *awesome*. You may want to put it in the wiki somewhere, for Sage Notebook development tools.


---

Attachment

Fixes the issues pointed out (Se failures, etc.)


---

Comment by timdumol created at 2010-01-05 20:32:15

The doctest failures are not yet fixed. I am having trouble with the Se tests: after a recent kernel upgrade, it seems that `shutil.rmdir()` fails silently, and `os.path.exists` reports the directory as gone, but is actually still there. I can only think of a kludgy fix of sleeping a while and looping until it can be deleted. Any ideas?


---

Attachment

New test options.  Should fix Se + doc tests.  Replaces previous.


---

Comment by mpatel created at 2010-01-06 15:38:39

V6 _might_ help.  I've tested just FF 3.5.6 on Linux, so far.  Examples:

```python
import sagenb.testing.run_tests as rt

# Selenium.
rt.setup_tests(environment='*firefox3 /usr/lib64/firefox-3.5.6/firefox')
rt.run_any()

# Selenium Grid.
envs = [
    '*firefox',
#    '*googlechrome',
    '*iexplore',
    '*opera',
#    '*safari'
    ]

for e in envs:
    rt.setup_tests('192.168.50.99', False, e)
    name = 'report_' + e.split()[0][1:] + '.html'
    rt.run_any(make_report=True, report_filename=name)
```

For other tickets:

 * Parallel testing.
 * Abstract away all `self.selenium` calls from `sagenb/tests/*`, i.e., put them all in a `notebook_test_case.SeleniumTestCase`.  Then we may be able to reuse `test_*` for pure `zope.testbrowser` tests --- "just" write a corresponding `notebook_test_case.ZTTestCase`.


---

Comment by mpatel created at 2010-01-06 15:42:22

Of course, please feel free to make changes!

On the dependency graph:  Thanks!  Maybe we should include parts of the code (wrapped in a `try-except` block) in `template.py`?


---

Attachment

Conditional `main.js` compression.  See `js.py`.  Replaces previous.


---

Comment by mpatel created at 2010-01-06 16:23:35

* It's not possible to delete compute cells from docbrowser worksheets, it seems.


---

Comment by mpatel created at 2010-01-06 16:49:01

Reminder: Use self-closing `<input />` tags in HTML files.  WebKit browsers will complain about extra `</input>`s.


---

Comment by mpatel created at 2010-01-06 19:05:22

Can we delete `twist.Reset_css`?


---

Comment by timdumol created at 2010-01-06 19:15:24

Replying to [comment:16 mpatel]:
> Of course, please feel free to make changes!
> 
> On the dependency graph:  Thanks!  Maybe we should include parts of the code (wrapped in a `try-except` block) in `template.py`?

It doesn't sound like it can be used by a non-developer, so I don't think it's worth including into the package. That's just my opinion though.


---

Comment by mpatel created at 2010-01-06 19:23:45

Should `NotebookSettingsPage.render` return a `HTMLResponse`, instead of a `Response`?


---

Comment by timdumol created at 2010-01-06 19:25:30

Replying to [comment:19 mpatel]:
> Can we delete `twist.Reset_css`?

Yes, we can.

> Should NotebookSettingsPage.render return a HTMLResponse, instead of a Response? 

Yes.

But I think this patch has way too many changes in it as is. The clean up on `twist.py` should probably be spun off to another ticket.


---

Comment by mpatel created at 2010-01-06 19:37:58

Replying to [comment:22 timdumol]:
> But I think this patch has way too many changes in it as is. The clean up on `twist.py` should probably be spun off to another ticket.

Sounds good.  I need to do this anyway for public / remote interacts.


---

Attachment

Further small fixes.  Replaces previous.


---

Comment by mpatel created at 2010-01-07 01:16:10

V8 should cover the problems above, except for deleting docbrowser cells, which is a known "problem" --- we don't save changes to these worksheets.  Anyway, to the extent it counts, my review is positive, except:

 * Is `_topbar.sass` missing?  When compiling, I see

```
Sass::SyntaxError on line 29 of /.../sass/src/main.sass: File to import not found or unreadable: topbar.sass.
```

   If I comment out the ``@`import`, the generated `main.css` seems to be missing topbar directives.

By the way, I removed `template_error.html` and `base_popup.html`, since they don't appear to be used.  I also put `set div_wrap = true` in `cell.html` (when printing).  I apologize for going too far, in case I have.


---

Comment by timdumol created at 2010-01-07 17:30:16

Adds missing file `_topbar.sass`


---

Attachment

Yes, it was missing. This patch fixes that problem.


---

Comment by mpatel created at 2010-01-08 09:19:51

Positive review from me.  If you agree, please update the status.


---

Comment by mpatel created at 2010-01-08 15:06:11

Actually, I just noticed some problems with `$(document).ready()`.  I'm working on V10.


---

Attachment

DOM ready / load event timing fixes.  Replaces previous.


---

Comment by mpatel created at 2010-01-08 16:48:39

In V10, I replaced `$(document).ready()` in a few places with either synchronous evaluation or `$(window).load()` (in particular, `$(document).load()` does not always work).  The main reason is timing --- the "DOM ready" event can fire too early for certain notebook initializations.  For example, evaluate

```
import time
time.sleep(20)
print 'foo'
```

and reload the worksheet.  Published interacts are another, forthcoming example...

I noticed that `Worksheet.html_cell_list` in V9

 * Referred to a non-existent template `published_worksheet.html`.
 * Is really no longer used.  The lone remaining call, in `twist.py` sends refreshed HTML that `notebook_lib.js` ignores.

I've replaced the call with an empty string.  _However,_ the main problem is that HTML for published worksheets is now no longer cached by the server.  Or am I mistaken?

I'll try to fix this in V11...


---

Attachment

Cache HTML for published worksheets.  Replaces previous.


---

Comment by mpatel created at 2010-01-08 17:12:07

V11 is attached.


---

Comment by mpatel created at 2010-01-08 20:17:55

If I save `$\alpha$` in a text cell, then edit the cell again, I see `Ë` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.


---

Comment by mpatel created at 2010-01-08 22:11:12

Fix text cell typesetting.  Replaces previous.


---

Attachment

Replying to [comment:31 mpatel]:
> If I save `$\alpha$` in a text cell, then edit the cell again, I see `Ë` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.
V12 should fix this.


---

Comment by mpatel created at 2010-01-09 00:10:51

I just noticed that Sphinx fails to build the reference manual.  The "problem" may be in `template.py`:

```
Sphinx error:
'utf8' codec can't decode bytes in position 746-749: invalid data
```



---

Comment by mpatel created at 2010-01-09 02:54:49

Fix HTML reference manual build.  Replaces previous.


---

Attachment

Replying to [comment:33 mpatel]:
> I just noticed that Sphinx fails to build the reference manual.  The "problem" may be in `template.py`:
V13 should fix this.


---

Comment by mpatel created at 2010-01-09 14:53:08

It seems the worksheet/cell layout is less compact than before.  It's probably easier to fix this at #7666.


---

Comment by mpatel created at 2010-01-09 23:41:34

Replying to [comment:35 mpatel]:
> It seems the worksheet/cell layout is less compact than before.  It's probably easier to fix this at #7666.
Or the same?  Anyway, possibilities for a completely different ticket:

 * Remove `&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` from `td.cell_number` for cells with no output.
 * Put the green "cell is running" bar adjacent to the red "cell is not evaluated" line.  The latter is actually a border, but we could insert a fixed-width `div` element here.  We could make this a status-area for the whole cell (input + output), add a right-click menu (e.g., for select / insert / move / delete operations, etc.), an on-hover toolbar, etc.


---

Attachment

Rebased on #7650 reviewer patch.


---

Comment by timdumol created at 2010-01-17 19:28:11

My patch series before up to this patch:


```
trac_7650-sagenb_doctesting_v6.patch
trac_7650-reviewer.patch
trac_7648-missing_indent.patch
trac_7663-rstrip_prompt.patch
trac_7847-empty-trash-no-referer.patch
trac_7786-template-jinja-idiomatic.patch
```



---

Comment by mpatel created at 2010-01-18 05:10:38

Tim -- Can you confirm the review (unless you want to get a third opinion)?  At this stage, I suggest we create new tickets to fix problems (if any) discovered later.


---

Comment by timdumol created at 2010-01-18 06:57:06

Alright, signing this off.


---

Comment by timdumol created at 2010-01-18 06:57:06

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-19 03:29:00

Resolution: fixed
