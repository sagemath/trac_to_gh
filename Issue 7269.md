# Issue 7269: SageNB -- Change table layouts to CSS layouts

Issue created by migration from https://trac.sagemath.org/ticket/7269

Original creator: timdumol

Original creation time: 2009-10-23 15:26:53

Assignee: boothby

CC:  was mpatel

Keywords: sagenb notebook

Changing the table layouts to CSS layouts will make it easier to make future edits, and will pave the path to user styling of the notebook.


---

Comment by timdumol created at 2009-10-23 15:32:33

Reduces/replaces table layouts with css layouts. Also cleans up the top bar template to be shared among all the templates.


---

Attachment

This should do the job.


---

Comment by timdumol created at 2009-10-23 15:33:18

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-10-23 18:44:22

Notes from "functional tests:"

 * "Report a Problem," which now appears on more pages, appears to be broken on some.
 * "Toggle" seems to be broken.
 * Should a "Copy of" a docbrowser worksheet include `default.css`?  Should we strip the copy of the sidebar, header, footer, etc.?

I try to take a closer look at the patch itself tomorrow.


---

Comment by mpatel created at 2009-10-23 19:42:34

Odds and ends:

 * Should we mark `notebook/user_controls.tmpl` for deletion?
 * Should we fold in the key parts of #7249's Jinja2 migration patch?

Out of curiousity:

 * What is `backwards` for?
 * Has anyone seen a inheritance diagram generator for HTML templates?
 * Could we unify two or more of `accounts_settings.css`, `user_management.css`, and `registration.css` for a common user/admin settings theme?

I'll try to look at `main.css` tomorrow...


---

Comment by timdumol created at 2009-10-24 02:03:08

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2009-10-24 02:03:08

Replying to [comment:3 mpatel]:
> Odds and ends:
> 
>  * Should we mark `notebook/user_controls.tmpl` for deletion?
Yes. I forgot to do so.
>  * Should we fold in the key parts of #7249's Jinja2 migration patch?
Yes. I'll do that now.
> 
> Out of curiousity:
> 
>  * What is `backwards` for?
I haven't an idea. I just copied that from the old code.
>  * Has anyone seen a inheritance diagram generator for HTML templates?
No, but that would be simply awesome.
>  * Could we unify two or more of `accounts_settings.css`, `user_management.css`, and `registration.css` for a common user/admin settings theme?
I actually planned to do a fair bit of changes to the structure (use inheritance instead of includes, etc.), but I think it would be better to put it in another ticket.
> 
> I'll try to look at `main.css` tomorrow...
I actually just copied the old main.css and put it through `css2sass` so I could edit it in SASS [1] and Compass [2]. I find it much easier to edit CSS that way -- just ask if you want to see the SASS source files. It's just a pity that SASS is Ruby-based, and the only Python alternative (CleverCSS) lacks many of the features and community support that SASS has.

[1] http://sass-lang.com/

[2] http://wiki.github.com/chriseppstein/compass


---

Comment by timdumol created at 2009-10-24 02:30:27

Apparently, `backwards` makes links go to the parent ("../foo" instead of "foo").


---

Comment by timdumol created at 2009-10-24 02:37:48

Fixed the "Report a Problem" and "Toggle" links. Removed `user_controls.tmpl`. Added changes from #7269. Apply this patch only.


---

Attachment

Fixed the "Report a Problem" and "Toggle" links. Removed `user_controls.tmpl`. Added changes from #7249. Apply this patch only.


---

Comment by timdumol created at 2009-10-24 02:39:39

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-10-24 02:39:39

The Toggle link problem was caused by a changed selector. Report a problem was due to lack of the JS libraries on certain pages. Both are now fixed.


---

Attachment

Fixed "None" value in search box due to Jinja2 migration.


---

Comment by timdumol created at 2009-10-24 04:08:12

Removed an escape that was no longer needed.


---

Attachment

Added parentheses to macro `actions` (needed for Jinja2 migration)


---

Comment by timdumol created at 2009-10-25 08:44:46

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2009-10-25 09:22:16

Also:

 * "Log," "Report a Problem," and "Help" don't work on the main Documentation/Help page.
 * The current Account settings, Error, Sign in, and Sign up pages don't need to load any libraries, I think.
 * The Sage logo on the Sign up page has a border in Firefox.
 * The Upload worksheet and Upload/Create data file pages use `form.submit()` instead of `type="submit"`, but these are probably not important.

Thanks for mentioning SASS and Compass!  Should we add the .sass files to the repository, to make it easier update the stylesheets in the future?

Reminder to self:  Rebase #4714's "jsmath_init" patch.


---

Comment by mpatel created at 2009-10-25 09:29:51

On the JS functions (this is mainly for future reference):

 * Active, Archived, and Deleted Worksheets; Published Worksheets for logged-in users; and Upload Worksheet can work with

```
history_window
help
bugreport
search_worksheets_enter_pressed
search_worksheets
archive_button
delete_button
stop_worksheets_button
download_worksheets_button
set_worksheet_list_checks
make_active_button
empty_trash
```


 * Published Worksheets for anonymous users needs just

```
search_worksheets_enter_pressed
search_worksheets
```



---

Comment by mpatel created at 2009-10-25 09:40:39

On the JS functions (continued):

 * Edit, Text, Undo, Share, Publish, Upload/Create Data File appear to need

```
server_ping_while_alive
jmolInitialize
jmolSetCallback
history_window
help
bugreport
rename_worksheet
save_worksheet - empty
save_worksheet_and_close - empty
worksheet_discard
go_option
upload_worksheet_button
new_worksheet
download_worksheet
print_worksheet
copy_worksheet
delete_worksheet
interrupt
restart_sage
evaluate_all
hide_all
show_all
delete_all_output
slide_mode
cell_mode
handle_data_menu
go_system_select
pretty_print_check
edit_worksheet
slide_next
slide_last
slide_first
slide_prev
```

but I think we can drop Jmol, jsMath, TinyMCE, sage3d, etc., and any cell-related functions.

This might seem like too much, but I think it's useful to optimize the JS (and make it modular) just as you've done and are doing for HTML and CSS.  Remote embeds (cf. #6855), in particular, may only need a streamlined library.


---

Comment by timdumol created at 2009-10-25 15:32:36

Replying to [comment:8 mpatel]:
> Also:
> 
>  * "Log," "Report a Problem," and "Help" don't work on the main Documentation/Help page.
>  * The current Account settings, Error, Sign in, and Sign up pages don't need to load any libraries, I think.
>  * The Sage logo on the Sign up page has a border in Firefox.
>  * The Upload worksheet and Upload/Create data file pages use `form.submit()` instead of `type="submit"`, but these are probably not important.
> 
> Thanks for mentioning SASS and Compass!  Should we add the .sass files to the repository, to make it easier update the stylesheets in the future?
> 
> Reminder to self:  Rebase #4714's "jsmath_init" patch.

I can do so. I'll also put instructions on using SASS + Compass.


---

Comment by mpatel created at 2009-10-27 10:02:44

Sphinx generates the CSS directives "scraped directly from Pygments" (i.e., `pygments.css`) when the docs are built.  If we use a different HTML theme (via  `pygments_style` in `conf.py` or in `theme.conf`, cf. #6673), we'll need to regenerate the CSS.  I'm not sure about the best way to do this with SASS.


---

Comment by timdumol created at 2009-10-27 10:15:28

How often/when will the HTML theme be changed? Does `main.css` have to be regenerated on the user-end, or during development?

If it is to be changed on the user-end, ``@`import`ing `pygments.css` on `main.css` would be the best choice. Otherwise, using `css2sass` on `pygments.css` and ``@`import`ing it on `main.sass` would be more efficient.


---

Comment by mpatel created at 2009-10-27 12:29:21

It may be best to ``@`import`, so we can make it possible to customize the introspection and live doc styles.  Sphinx also instantiates a Jinja2 template as `default.css`.


---

Comment by mpatel created at 2009-10-27 15:14:17

Replying to [comment:9 mpatel]:
> On the JS functions (this is mainly for future reference):
> 
>  * Active, Archived, and Deleted Worksheets; Published Worksheets for logged-in users; and Upload Worksheet can work with

I've separated out what I think is a minimal `ws_list.js` for these pages.  It depends only on jQuery.  It'll also depend on jQuery UI after I replace the `alert`s.  It might be useful to update the server status on these pages for authenticated users, that is, add a worksheet-independent ping.  I can add that code.


---

Comment by mpatel created at 2009-10-27 15:24:14

A clarification: I'll definitely make a separate ticket for modularizing the notebook JS.


---

Comment by timdumol created at 2009-10-27 15:30:38

I'm suspending work on this until I finish working on the test suite, now that #7310 is done, albeit not yet accepted.


---

Comment by timdumol created at 2009-10-29 14:27:13

Now that #7343 is mostly done, I'll resume work on this.

Replying to [comment:15 mpatel]:
> Replying to [comment:9 mpatel]:
> > On the JS functions (this is mainly for future reference):
> > 
> >  * Active, Archived, and Deleted Worksheets; Published Worksheets for logged-in users; and Upload Worksheet can work with
> 
> I've separated out what I think is a minimal `ws_list.js` for these pages.  It depends only on jQuery.  It'll also depend on jQuery UI after I replace the `alert`s.  It might be useful to update the server status on these pages for authenticated users, that is, add a worksheet-independent ping.  I can add that code.

That would be excellent. Would you mind posting the code?


---

Attachment

Just the separated minimal ws_list.js, for experiments.  This is not a patch.


---

Comment by mpatel created at 2009-10-31 10:53:17

Replying to [comment:18 timdumol]:
> Now that #7343 is mostly done, I'll resume work on this.

> [...]

> That would be excellent. Would you mind posting the code?

I've attached just the separated, minimal `ws_list.js`, which appears to be enough for the intended pages (except for the already broken "Download" button).


---

Comment by mpatel created at 2009-11-11 17:44:40

Replying to [comment:18 timdumol]:
> Now that #7343 is mostly done, I'll resume work on this.

May I ask what are your plans for this ticket?  If you need more from me, just let me know.


---

Comment by timdumol created at 2009-11-12 10:16:23

Replying to [comment:20 mpatel]:
> Replying to [comment:18 timdumol]:
> > Now that #7343 is mostly done, I'll resume work on this.
> 
> May I ask what are your plans for this ticket?  If you need more from me, just let me know.

Sorry. I've been a bit caught up with school work, etc. I'll try to resume work on it as soon as my workload lets up.


---

Comment by timdumol created at 2009-12-13 06:44:29

Fixes all given bugs and removes more <table>s. Adds the SASS code with readme file. Apply this patch alone.


---

Comment by timdumol created at 2009-12-13 06:48:05

Changing status from needs_work to needs_review.


---

Attachment

This patch should fix the problems. I have included the SASS source files, with a readme on how to edit them. I hope the patch file size does not daunt anyone -- a large contributor is that both the SASS source files and the generated CSS are included.


---

Comment by timdumol created at 2009-12-13 07:20:35

A bit of cleanup to make the Se tests less mercurial.


---

Attachment

Fixed `ws_list.js` to include the fix from #5100


---

Attachment

Various fixes.  Rebased vs. #7650.


---

Comment by mpatel created at 2009-12-13 13:18:03

V9:

 * Rebased for #7650.
 * Fixes several failed doctests.
 * Adds `ws_list.js` to the "Help" and "Log" pages.
 * Re-centers the "Help" page.

Problems:

 * Live doc worksheets don't render, e.g.,

```python
        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 1294: ordinal not in range(128)
```


 * Minor: The notebook settings page sections are no longer centered(?).
 * Minor: Can we remove `html/notebook/doc.html` and `notebook.html_doc`?  It _appears _ to be redundant.
 * Minor: The user name is not aligned with "Toggle," "Home," etc.

"Heads up" note: I'm about to

 * Revisit #7650 to try to keep `cell.py` doctests from taking too much memory.
 * Rebase my patch for #7666, which will visit many .py, .js, and .html files, against this ticket.  The local queue:

```
sagenb_7483.patch
sagenb_7482.patch
sagenb-7514.patch
trac_7648-missing_indent.patch
trac_7650-sagenb_doctesting.patch
trac_7269-table-reduction.patch
trac_7666-alphanumeric_cell_ids.patch
```



---

Comment by timdumol created at 2009-12-19 11:42:40

Jinja2 disables automatic conversion from byte strings to unicode strings. This causes problems with unicode titles/cells. To fix this cleanly (without too much cruft) will require a clean MVP/MVC (Model-View-Presenter/Controller) separation. I'm removing the jinja2 conversion from this patch, in the meantime.

To note, `ws_list.js` is the default js include, and so was already included in the Help and Log pages.

I have not noticed that the settings page was centered. IMHO though, I think flush left is cleaner looking (nice straight left edge).

This patch update deletes the obsolete files, aligns the username and removes the Jinja2 migration.


---

Attachment

Aligns the username, removes the Jinja2 migration, deletes some obsolete files.


---

Comment by mpatel created at 2009-12-20 14:04:56

> To note, ws_list.js is the default js include, and so was already included in the Help and Log pages.

Oops.  I apologize for this.  I'm about to attach V11, which

 * May make the top bar display better in narrow windows or those with large fonts.
 * `ttile` --> `title` in `top_bar.html`.
 * Adds a `tr` to `worksheet_listing.html` (WebKit error).
 * Fixes failed doctests in `template.py`:
   * Restores the previous `template.py` doctests.
   * Adds `'# not tested'` to the Jinja2 tests.
 * Fixes a failed doctest in `notebook.py`.


---

Comment by mpatel created at 2009-12-20 14:05:45

Top bar tweaks and doctest fixes.  Replaces previous.


---

Attachment

Input cell tweaks.  Include jQuery just once.  Replaces previous.


---

Comment by mpatel created at 2009-12-30 08:23:48

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-12-30 08:23:48

Changing type from defect to enhancement.


---

Comment by mpatel created at 2009-12-30 08:23:48

V12:

 * Removes the jQuery include from a few pages, since it's now included in `base.html`.  Including it twice sometimes caused a "mod-2" problem in Firefox --- the browser would claim that (and act as if) the resource `jquery-1.3.2.min.js` was missing.

 * Tweaks input cell padding so that text does not move by a pixel on focus or blur (I hope).  Text is still very likely to move when a cell is focused for the _first_ time after reloading a page, since the sizing algorithms in `cell.py` and `notebook_lib.js` are different.

Someone should review my changes, of course, and perhaps also comment on the slightly changed layouts.  I think the button/toolbars wrap differently than before, e.g., when the browser width is narrow and/or the font size is large.  Does this cause problems on mobiles or when giving presentations?

Positive review!  This is great work!  I'm still quite new to [SASS](http://sass-lang.com/) and [Compass](http://wiki.github.com/chriseppstein/compass), but it seems that they'll make it much easier to edit and manage SageNB stylesheets.

By the way, can we use SASS, Compass, and/or another tool to find unused CSS directives?


---

Comment by mpatel created at 2009-12-30 08:23:48

Changing priority from minor to major.


---

Attachment

Apply #7811 to `ws_list.js`.  Replaces previous.


---

Comment by mpatel created at 2010-01-01 23:46:29

V13 just applies #7811 to `ws_list.js`.  I believe we still use `notebook_lib.js` for logged in users, but I've made the change, for the sake of completeness.   If it's OK, I'd like to postpone "subtracting" `ws_list.js` from `notebook_lib.js` until after published interacts (cf. #6855) are enabled.


---

Comment by mpatel created at 2010-01-02 09:07:43

Rebase vs. #7811 v2.  Replaces previous.


---

Attachment

I can't merge this into sagenb-0.4.8 (which I'm about to release).   Please rebase it once sage-4.3.1.alpha0 comes out with this new sagenb.  Thanks!


```
applying trac_7269-table-reduction.14.patch
patching file sagenb/notebook/notebook.py
Hunk #2 succeeded at 950 with fuzz 2 (offset 3 lines).
Hunk #3 FAILED at 1265
Hunk #4 succeeded at 1334 with fuzz 2 (offset 9 lines).
Hunk #5 succeeded at 1407 with fuzz 1 (offset 9 lines).
Hunk #6 succeeded at 1441 with fuzz 1 (offset 9 lines).
Hunk #7 FAILED at 1467
Hunk #8 succeeded at 1486 with fuzz 1 (offset 9 lines).
Hunk #9 succeeded at 1589 with fuzz 1 (offset 9 lines).
Hunk #10 FAILED at 1608
Hunk #11 succeeded at 1651 with fuzz 1 (offset 9 lines).
Hunk #12 FAILED at 1706
Hunk #13 succeeded at 1748 with fuzz 1 (offset 10 lines).
Hunk #14 FAILED at 1757
5 out of 14 hunks FAILED -- saving rejects to file sagenb/notebook/notebook.py.rej
patching file sagenb/notebook/twist.py
Hunk #7 succeeded at 960 with fuzz 2 (offset 2 lines).
patching file sagenb/notebook/worksheet.py
Hunk #1 FAILED at 1712
Hunk #2 FAILED at 1763
Hunk #3 FAILED at 2300
Hunk #4 succeeded at 2442 with fuzz 1 (offset 87 lines).
Hunk #5 succeeded at 2458 with fuzz 1 (offset 87 lines).
3 out of 6 hunks FAILED -- saving rejects to file sagenb/notebook/worksheet.py.rej
abort: patch failed to apply

```



---

Comment by timdumol created at 2010-01-04 19:59:41

rebased vs sagenb-0.4.9


---

Attachment

Rebased version posted.


---

Comment by mpatel created at 2010-01-04 23:06:26

Can you try applying #7650 first, then V14?  That should give just one, ignorable failure and much less "fuzz".  I apologize for not being more explicit about this dependency.


---

Comment by mpatel created at 2010-01-04 23:09:08

Of course, this assumes #7650 is reviewed.


---

Comment by was created at 2010-01-04 23:12:32

Merged into sagenb-0.5.   I was able to apply trac_7269-table-reduction.15.patch  just fine without merging in #7650 first.  Yeah.  So this is in and pushed to the official repo.


---

Comment by was created at 2010-01-04 23:12:32

Resolution: fixed
