# Issue 7269: SageNB -- Change table layouts to CSS layouts

archive/issues_007269.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was mpatel\n\nKeywords: sagenb notebook\n\nChanging the table layouts to CSS layouts will make it easier to make future edits, and will pave the path to user styling of the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7269\n\n",
    "created_at": "2009-10-23T15:26:53Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "SageNB -- Change table layouts to CSS layouts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7269",
    "user": "timdumol"
}
```
Assignee: boothby

CC:  was mpatel

Keywords: sagenb notebook

Changing the table layouts to CSS layouts will make it easier to make future edits, and will pave the path to user styling of the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/7269





---

archive/issue_comments_060412.json:
```json
{
    "body": "Reduces/replaces table layouts with css layouts. Also cleans up the top bar template to be shared among all the templates.",
    "created_at": "2009-10-23T15:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60412",
    "user": "timdumol"
}
```

Reduces/replaces table layouts with css layouts. Also cleans up the top bar template to be shared among all the templates.



---

archive/issue_comments_060413.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.patch) by timdumol created at 2009-10-23 15:33:18\n\nThis should do the job.",
    "created_at": "2009-10-23T15:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60413",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.patch) by timdumol created at 2009-10-23 15:33:18

This should do the job.



---

archive/issue_comments_060414.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-23T15:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60414",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060415.json:
```json
{
    "body": "Notes from \"functional tests:\"\n\n* \"Report a Problem,\" which now appears on more pages, appears to be broken on some.\n* \"Toggle\" seems to be broken.\n* Should a \"Copy of\" a docbrowser worksheet include `default.css`?  Should we strip the copy of the sidebar, header, footer, etc.?\n\nI try to take a closer look at the patch itself tomorrow.",
    "created_at": "2009-10-23T18:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60415",
    "user": "mpatel"
}
```

Notes from "functional tests:"

* "Report a Problem," which now appears on more pages, appears to be broken on some.
* "Toggle" seems to be broken.
* Should a "Copy of" a docbrowser worksheet include `default.css`?  Should we strip the copy of the sidebar, header, footer, etc.?

I try to take a closer look at the patch itself tomorrow.



---

archive/issue_comments_060416.json:
```json
{
    "body": "Odds and ends:\n\n* Should we mark `notebook/user_controls.tmpl` for deletion?\n* Should we fold in the key parts of #7249's Jinja2 migration patch?\n\nOut of curiousity:\n\n* What is `backwards` for?\n* Has anyone seen a inheritance diagram generator for HTML templates?\n* Could we unify two or more of `accounts_settings.css`, `user_management.css`, and `registration.css` for a common user/admin settings theme?\n\nI'll try to look at `main.css` tomorrow...",
    "created_at": "2009-10-23T19:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60416",
    "user": "mpatel"
}
```

Odds and ends:

* Should we mark `notebook/user_controls.tmpl` for deletion?
* Should we fold in the key parts of #7249's Jinja2 migration patch?

Out of curiousity:

* What is `backwards` for?
* Has anyone seen a inheritance diagram generator for HTML templates?
* Could we unify two or more of `accounts_settings.css`, `user_management.css`, and `registration.css` for a common user/admin settings theme?

I'll try to look at `main.css` tomorrow...



---

archive/issue_comments_060417.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-24T02:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60417",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060418.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Odds and ends:\n> \n>  * Should we mark `notebook/user_controls.tmpl` for deletion?\nYes. I forgot to do so.\n>  * Should we fold in the key parts of #7249's Jinja2 migration patch?\nYes. I'll do that now.\n> \n> Out of curiousity:\n> \n>  * What is `backwards` for?\nI haven't an idea. I just copied that from the old code.\n>  * Has anyone seen a inheritance diagram generator for HTML templates?\nNo, but that would be simply awesome.\n>  * Could we unify two or more of `accounts_settings.css`, `user_management.css`, and `registration.css` for a common user/admin settings theme?\nI actually planned to do a fair bit of changes to the structure (use inheritance instead of includes, etc.), but I think it would be better to put it in another ticket.\n> \n> I'll try to look at `main.css` tomorrow...\nI actually just copied the old main.css and put it through `css2sass` so I could edit it in SASS [1] and Compass [2]. I find it much easier to edit CSS that way -- just ask if you want to see the SASS source files. It's just a pity that SASS is Ruby-based, and the only Python alternative (CleverCSS) lacks many of the features and community support that SASS has.\n\n[1] http://sass-lang.com/\n\n[2] http://wiki.github.com/chriseppstein/compass",
    "created_at": "2009-10-24T02:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60418",
    "user": "timdumol"
}
```

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

archive/issue_comments_060419.json:
```json
{
    "body": "Apparently, `backwards` makes links go to the parent (\"../foo\" instead of \"foo\").",
    "created_at": "2009-10-24T02:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60419",
    "user": "timdumol"
}
```

Apparently, `backwards` makes links go to the parent ("../foo" instead of "foo").



---

archive/issue_comments_060420.json:
```json
{
    "body": "Fixed the \"Report a Problem\" and \"Toggle\" links. Removed `user_controls.tmpl`. Added changes from #7269. Apply this patch only.",
    "created_at": "2009-10-24T02:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60420",
    "user": "timdumol"
}
```

Fixed the "Report a Problem" and "Toggle" links. Removed `user_controls.tmpl`. Added changes from #7269. Apply this patch only.



---

archive/issue_comments_060421.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.2.2.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.2.2.patch) by timdumol created at 2009-10-24 02:38:22\n\nFixed the \"Report a Problem\" and \"Toggle\" links. Removed `user_controls.tmpl`. Added changes from #7249. Apply this patch only.",
    "created_at": "2009-10-24T02:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60421",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.2.2.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.2.2.patch) by timdumol created at 2009-10-24 02:38:22

Fixed the "Report a Problem" and "Toggle" links. Removed `user_controls.tmpl`. Added changes from #7249. Apply this patch only.



---

archive/issue_comments_060422.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-24T02:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60422",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060423.json:
```json
{
    "body": "The Toggle link problem was caused by a changed selector. Report a problem was due to lack of the JS libraries on certain pages. Both are now fixed.",
    "created_at": "2009-10-24T02:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60423",
    "user": "timdumol"
}
```

The Toggle link problem was caused by a changed selector. Report a problem was due to lack of the JS libraries on certain pages. Both are now fixed.



---

archive/issue_comments_060424.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.3.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.3.patch) by timdumol created at 2009-10-24 03:00:37\n\nFixed \"None\" value in search box due to Jinja2 migration.",
    "created_at": "2009-10-24T03:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60424",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.3.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.3.patch) by timdumol created at 2009-10-24 03:00:37

Fixed "None" value in search box due to Jinja2 migration.



---

archive/issue_comments_060425.json:
```json
{
    "body": "Removed an escape that was no longer needed.",
    "created_at": "2009-10-24T04:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60425",
    "user": "timdumol"
}
```

Removed an escape that was no longer needed.



---

archive/issue_comments_060426.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.5.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.5.patch) by timdumol created at 2009-10-24 10:19:13\n\nAdded parentheses to macro `actions` (needed for Jinja2 migration)",
    "created_at": "2009-10-24T10:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60426",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.5.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.5.patch) by timdumol created at 2009-10-24 10:19:13

Added parentheses to macro `actions` (needed for Jinja2 migration)



---

archive/issue_comments_060427.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-25T08:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60427",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060428.json:
```json
{
    "body": "Also:\n\n* \"Log,\" \"Report a Problem,\" and \"Help\" don't work on the main Documentation/Help page.\n* The current Account settings, Error, Sign in, and Sign up pages don't need to load any libraries, I think.\n* The Sage logo on the Sign up page has a border in Firefox.\n* The Upload worksheet and Upload/Create data file pages use `form.submit()` instead of `type=\"submit\"`, but these are probably not important.\n\nThanks for mentioning SASS and Compass!  Should we add the .sass files to the repository, to make it easier update the stylesheets in the future?\n\nReminder to self:  Rebase #4714's \"jsmath_init\" patch.",
    "created_at": "2009-10-25T09:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60428",
    "user": "mpatel"
}
```

Also:

* "Log," "Report a Problem," and "Help" don't work on the main Documentation/Help page.
* The current Account settings, Error, Sign in, and Sign up pages don't need to load any libraries, I think.
* The Sage logo on the Sign up page has a border in Firefox.
* The Upload worksheet and Upload/Create data file pages use `form.submit()` instead of `type="submit"`, but these are probably not important.

Thanks for mentioning SASS and Compass!  Should we add the .sass files to the repository, to make it easier update the stylesheets in the future?

Reminder to self:  Rebase #4714's "jsmath_init" patch.



---

archive/issue_comments_060429.json:
```json
{
    "body": "On the JS functions (this is mainly for future reference):\n\n* Active, Archived, and Deleted Worksheets; Published Worksheets for logged-in users; and Upload Worksheet can work with\n\n```\nhistory_window\nhelp\nbugreport\nsearch_worksheets_enter_pressed\nsearch_worksheets\narchive_button\ndelete_button\nstop_worksheets_button\ndownload_worksheets_button\nset_worksheet_list_checks\nmake_active_button\nempty_trash\n```\n\n\n* Published Worksheets for anonymous users needs just\n\n```\nsearch_worksheets_enter_pressed\nsearch_worksheets\n```\n",
    "created_at": "2009-10-25T09:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60429",
    "user": "mpatel"
}
```

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

archive/issue_comments_060430.json:
```json
{
    "body": "On the JS functions (continued):\n\n* Edit, Text, Undo, Share, Publish, Upload/Create Data File appear to need\n\n```\nserver_ping_while_alive\njmolInitialize\njmolSetCallback\nhistory_window\nhelp\nbugreport\nrename_worksheet\nsave_worksheet - empty\nsave_worksheet_and_close - empty\nworksheet_discard\ngo_option\nupload_worksheet_button\nnew_worksheet\ndownload_worksheet\nprint_worksheet\ncopy_worksheet\ndelete_worksheet\ninterrupt\nrestart_sage\nevaluate_all\nhide_all\nshow_all\ndelete_all_output\nslide_mode\ncell_mode\nhandle_data_menu\ngo_system_select\npretty_print_check\nedit_worksheet\nslide_next\nslide_last\nslide_first\nslide_prev\n```\n\nbut I think we can drop Jmol, jsMath, TinyMCE, sage3d, etc., and any cell-related functions.\n\nThis might seem like too much, but I think it's useful to optimize the JS (and make it modular) just as you've done and are doing for HTML and CSS.  Remote embeds (cf. #6855), in particular, may only need a streamlined library.",
    "created_at": "2009-10-25T09:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60430",
    "user": "mpatel"
}
```

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

archive/issue_comments_060431.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> Also:\n> \n>  * \"Log,\" \"Report a Problem,\" and \"Help\" don't work on the main Documentation/Help page.\n>  * The current Account settings, Error, Sign in, and Sign up pages don't need to load any libraries, I think.\n>  * The Sage logo on the Sign up page has a border in Firefox.\n>  * The Upload worksheet and Upload/Create data file pages use `form.submit()` instead of `type=\"submit\"`, but these are probably not important.\n> \n> Thanks for mentioning SASS and Compass!  Should we add the .sass files to the repository, to make it easier update the stylesheets in the future?\n> \n> Reminder to self:  Rebase #4714's \"jsmath_init\" patch.\n\nI can do so. I'll also put instructions on using SASS + Compass.",
    "created_at": "2009-10-25T15:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60431",
    "user": "timdumol"
}
```

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

archive/issue_comments_060432.json:
```json
{
    "body": "Sphinx generates the CSS directives \"scraped directly from Pygments\" (i.e., `pygments.css`) when the docs are built.  If we use a different HTML theme (via  `pygments_style` in `conf.py` or in `theme.conf`, cf. #6673), we'll need to regenerate the CSS.  I'm not sure about the best way to do this with SASS.",
    "created_at": "2009-10-27T10:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60432",
    "user": "mpatel"
}
```

Sphinx generates the CSS directives "scraped directly from Pygments" (i.e., `pygments.css`) when the docs are built.  If we use a different HTML theme (via  `pygments_style` in `conf.py` or in `theme.conf`, cf. #6673), we'll need to regenerate the CSS.  I'm not sure about the best way to do this with SASS.



---

archive/issue_comments_060433.json:
```json
{
    "body": "How often/when will the HTML theme be changed? Does `main.css` have to be regenerated on the user-end, or during development?\n\nIf it is to be changed on the user-end, ``@`import`ing `pygments.css` on `main.css` would be the best choice. Otherwise, using `css2sass` on `pygments.css` and ``@`import`ing it on `main.sass` would be more efficient.",
    "created_at": "2009-10-27T10:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60433",
    "user": "timdumol"
}
```

How often/when will the HTML theme be changed? Does `main.css` have to be regenerated on the user-end, or during development?

If it is to be changed on the user-end, ``@`import`ing `pygments.css` on `main.css` would be the best choice. Otherwise, using `css2sass` on `pygments.css` and ``@`import`ing it on `main.sass` would be more efficient.



---

archive/issue_comments_060434.json:
```json
{
    "body": "It may be best to ``@`import`, so we can make it possible to customize the introspection and live doc styles.  Sphinx also instantiates a Jinja2 template as `default.css`.",
    "created_at": "2009-10-27T12:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60434",
    "user": "mpatel"
}
```

It may be best to ``@`import`, so we can make it possible to customize the introspection and live doc styles.  Sphinx also instantiates a Jinja2 template as `default.css`.



---

archive/issue_comments_060435.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n> On the JS functions (this is mainly for future reference):\n> \n>  * Active, Archived, and Deleted Worksheets; Published Worksheets for logged-in users; and Upload Worksheet can work with\n\nI've separated out what I think is a minimal `ws_list.js` for these pages.  It depends only on jQuery.  It'll also depend on jQuery UI after I replace the `alert`s.  It might be useful to update the server status on these pages for authenticated users, that is, add a worksheet-independent ping.  I can add that code.",
    "created_at": "2009-10-27T15:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60435",
    "user": "mpatel"
}
```

Replying to [comment:9 mpatel]:
> On the JS functions (this is mainly for future reference):
> 
>  * Active, Archived, and Deleted Worksheets; Published Worksheets for logged-in users; and Upload Worksheet can work with

I've separated out what I think is a minimal `ws_list.js` for these pages.  It depends only on jQuery.  It'll also depend on jQuery UI after I replace the `alert`s.  It might be useful to update the server status on these pages for authenticated users, that is, add a worksheet-independent ping.  I can add that code.



---

archive/issue_comments_060436.json:
```json
{
    "body": "A clarification: I'll definitely make a separate ticket for modularizing the notebook JS.",
    "created_at": "2009-10-27T15:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60436",
    "user": "mpatel"
}
```

A clarification: I'll definitely make a separate ticket for modularizing the notebook JS.



---

archive/issue_comments_060437.json:
```json
{
    "body": "I'm suspending work on this until I finish working on the test suite, now that #7310 is done, albeit not yet accepted.",
    "created_at": "2009-10-27T15:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60437",
    "user": "timdumol"
}
```

I'm suspending work on this until I finish working on the test suite, now that #7310 is done, albeit not yet accepted.



---

archive/issue_comments_060438.json:
```json
{
    "body": "Now that #7343 is mostly done, I'll resume work on this.\n\nReplying to [comment:15 mpatel]:\n> Replying to [comment:9 mpatel]:\n> > On the JS functions (this is mainly for future reference):\n> > \n> >  * Active, Archived, and Deleted Worksheets; Published Worksheets for logged-in users; and Upload Worksheet can work with\n> \n> I've separated out what I think is a minimal `ws_list.js` for these pages.  It depends only on jQuery.  It'll also depend on jQuery UI after I replace the `alert`s.  It might be useful to update the server status on these pages for authenticated users, that is, add a worksheet-independent ping.  I can add that code.\n\nThat would be excellent. Would you mind posting the code?",
    "created_at": "2009-10-29T14:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60438",
    "user": "timdumol"
}
```

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

archive/issue_comments_060439.json:
```json
{
    "body": "Attachment [ws_list.js](tarball://root/attachments/some-uuid/ticket7269/ws_list.js) by mpatel created at 2009-10-31 10:40:58\n\nJust the separated minimal ws_list.js, for experiments.  This is not a patch.",
    "created_at": "2009-10-31T10:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60439",
    "user": "mpatel"
}
```

Attachment [ws_list.js](tarball://root/attachments/some-uuid/ticket7269/ws_list.js) by mpatel created at 2009-10-31 10:40:58

Just the separated minimal ws_list.js, for experiments.  This is not a patch.



---

archive/issue_comments_060440.json:
```json
{
    "body": "Replying to [comment:18 timdumol]:\n> Now that #7343 is mostly done, I'll resume work on this.\n\n> [...]\n\n> That would be excellent. Would you mind posting the code?\n\nI've attached just the separated, minimal `ws_list.js`, which appears to be enough for the intended pages (except for the already broken \"Download\" button).",
    "created_at": "2009-10-31T10:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60440",
    "user": "mpatel"
}
```

Replying to [comment:18 timdumol]:
> Now that #7343 is mostly done, I'll resume work on this.

> [...]

> That would be excellent. Would you mind posting the code?

I've attached just the separated, minimal `ws_list.js`, which appears to be enough for the intended pages (except for the already broken "Download" button).



---

archive/issue_comments_060441.json:
```json
{
    "body": "Replying to [comment:18 timdumol]:\n> Now that #7343 is mostly done, I'll resume work on this.\n\nMay I ask what are your plans for this ticket?  If you need more from me, just let me know.",
    "created_at": "2009-11-11T17:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60441",
    "user": "mpatel"
}
```

Replying to [comment:18 timdumol]:
> Now that #7343 is mostly done, I'll resume work on this.

May I ask what are your plans for this ticket?  If you need more from me, just let me know.



---

archive/issue_comments_060442.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n> Replying to [comment:18 timdumol]:\n> > Now that #7343 is mostly done, I'll resume work on this.\n> \n> May I ask what are your plans for this ticket?  If you need more from me, just let me know.\n\nSorry. I've been a bit caught up with school work, etc. I'll try to resume work on it as soon as my workload lets up.",
    "created_at": "2009-11-12T10:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60442",
    "user": "timdumol"
}
```

Replying to [comment:20 mpatel]:
> Replying to [comment:18 timdumol]:
> > Now that #7343 is mostly done, I'll resume work on this.
> 
> May I ask what are your plans for this ticket?  If you need more from me, just let me know.

Sorry. I've been a bit caught up with school work, etc. I'll try to resume work on it as soon as my workload lets up.



---

archive/issue_comments_060443.json:
```json
{
    "body": "Fixes all given bugs and removes more <table>s. Adds the SASS code with readme file. Apply this patch alone.",
    "created_at": "2009-12-13T06:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60443",
    "user": "timdumol"
}
```

Fixes all given bugs and removes more <table>s. Adds the SASS code with readme file. Apply this patch alone.



---

archive/issue_comments_060444.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-13T06:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60444",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060445.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.6.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.6.patch) by timdumol created at 2009-12-13 06:48:05\n\nThis patch should fix the problems. I have included the SASS source files, with a readme on how to edit them. I hope the patch file size does not daunt anyone -- a large contributor is that both the SASS source files and the generated CSS are included.",
    "created_at": "2009-12-13T06:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60445",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.6.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.6.patch) by timdumol created at 2009-12-13 06:48:05

This patch should fix the problems. I have included the SASS source files, with a readme on how to edit them. I hope the patch file size does not daunt anyone -- a large contributor is that both the SASS source files and the generated CSS are included.



---

archive/issue_comments_060446.json:
```json
{
    "body": "A bit of cleanup to make the Se tests less mercurial.",
    "created_at": "2009-12-13T07:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60446",
    "user": "timdumol"
}
```

A bit of cleanup to make the Se tests less mercurial.



---

archive/issue_comments_060447.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.8.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.8.patch) by timdumol created at 2009-12-13 08:34:39\n\nFixed `ws_list.js` to include the fix from #5100",
    "created_at": "2009-12-13T08:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60447",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.8.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.8.patch) by timdumol created at 2009-12-13 08:34:39

Fixed `ws_list.js` to include the fix from #5100



---

archive/issue_comments_060448.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.9.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.9.patch) by mpatel created at 2009-12-13 12:51:45\n\nVarious fixes.  Rebased vs. #7650.",
    "created_at": "2009-12-13T12:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60448",
    "user": "mpatel"
}
```

Attachment [trac_7269-table-reduction.9.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.9.patch) by mpatel created at 2009-12-13 12:51:45

Various fixes.  Rebased vs. #7650.



---

archive/issue_comments_060449.json:
```json
{
    "body": "V9:\n\n* Rebased for #7650.\n* Fixes several failed doctests.\n* Adds `ws_list.js` to the \"Help\" and \"Log\" pages.\n* Re-centers the \"Help\" page.\n\nProblems:\n\n* Live doc worksheets don't render, e.g.,\n\n```python\n        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 1294: ordinal not in range(128)\n```\n\n\n* Minor: The notebook settings page sections are no longer centered(?).\n* Minor: Can we remove `html/notebook/doc.html` and `notebook.html_doc`?  It *appears * to be redundant.\n* Minor: The user name is not aligned with \"Toggle,\" \"Home,\" etc.\n\n\"Heads up\" note: I'm about to\n\n* Revisit #7650 to try to keep `cell.py` doctests from taking too much memory.\n* Rebase my patch for #7666, which will visit many .py, .js, and .html files, against this ticket.  The local queue:\n\n```\nsagenb_7483.patch\nsagenb_7482.patch\nsagenb-7514.patch\ntrac_7648-missing_indent.patch\ntrac_7650-sagenb_doctesting.patch\ntrac_7269-table-reduction.patch\ntrac_7666-alphanumeric_cell_ids.patch\n```\n",
    "created_at": "2009-12-13T13:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60449",
    "user": "mpatel"
}
```

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
* Minor: Can we remove `html/notebook/doc.html` and `notebook.html_doc`?  It *appears * to be redundant.
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

archive/issue_comments_060450.json:
```json
{
    "body": "Jinja2 disables automatic conversion from byte strings to unicode strings. This causes problems with unicode titles/cells. To fix this cleanly (without too much cruft) will require a clean MVP/MVC (Model-View-Presenter/Controller) separation. I'm removing the jinja2 conversion from this patch, in the meantime.\n\nTo note, `ws_list.js` is the default js include, and so was already included in the Help and Log pages.\n\nI have not noticed that the settings page was centered. IMHO though, I think flush left is cleaner looking (nice straight left edge).\n\nThis patch update deletes the obsolete files, aligns the username and removes the Jinja2 migration.",
    "created_at": "2009-12-19T11:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60450",
    "user": "timdumol"
}
```

Jinja2 disables automatic conversion from byte strings to unicode strings. This causes problems with unicode titles/cells. To fix this cleanly (without too much cruft) will require a clean MVP/MVC (Model-View-Presenter/Controller) separation. I'm removing the jinja2 conversion from this patch, in the meantime.

To note, `ws_list.js` is the default js include, and so was already included in the Help and Log pages.

I have not noticed that the settings page was centered. IMHO though, I think flush left is cleaner looking (nice straight left edge).

This patch update deletes the obsolete files, aligns the username and removes the Jinja2 migration.



---

archive/issue_comments_060451.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.10.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.10.patch) by timdumol created at 2009-12-19 11:45:08\n\nAligns the username, removes the Jinja2 migration, deletes some obsolete files.",
    "created_at": "2009-12-19T11:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60451",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.10.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.10.patch) by timdumol created at 2009-12-19 11:45:08

Aligns the username, removes the Jinja2 migration, deletes some obsolete files.



---

archive/issue_comments_060452.json:
```json
{
    "body": "> To note, ws_list.js is the default js include, and so was already included in the Help and Log pages.\n\nOops.  I apologize for this.  I'm about to attach V11, which\n\n   * May make the top bar display better in narrow windows or those with large fonts.\n   * `ttile` --> `title` in `top_bar.html`.\n   * Adds a `tr` to `worksheet_listing.html` (WebKit error).\n   * Fixes failed doctests in `template.py`:\n   * Restores the previous `template.py` doctests.\n   * Adds `'# not tested'` to the Jinja2 tests.\n   * Fixes a failed doctest in `notebook.py`.",
    "created_at": "2009-12-20T14:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60452",
    "user": "mpatel"
}
```

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

archive/issue_comments_060453.json:
```json
{
    "body": "Top bar tweaks and doctest fixes.  Replaces previous.",
    "created_at": "2009-12-20T14:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60453",
    "user": "mpatel"
}
```

Top bar tweaks and doctest fixes.  Replaces previous.



---

archive/issue_comments_060454.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.12.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.12.patch) by mpatel created at 2009-12-30 07:31:24\n\nInput cell tweaks.  Include jQuery just once.  Replaces previous.",
    "created_at": "2009-12-30T07:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60454",
    "user": "mpatel"
}
```

Attachment [trac_7269-table-reduction.12.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.12.patch) by mpatel created at 2009-12-30 07:31:24

Input cell tweaks.  Include jQuery just once.  Replaces previous.



---

archive/issue_comments_060455.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-30T08:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60455",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060456.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-12-30T08:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60456",
    "user": "mpatel"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_060457.json:
```json
{
    "body": "V12:\n\n* Removes the jQuery include from a few pages, since it's now included in `base.html`.  Including it twice sometimes caused a \"mod-2\" problem in Firefox --- the browser would claim that (and act as if) the resource `jquery-1.3.2.min.js` was missing.\n\n* Tweaks input cell padding so that text does not move by a pixel on focus or blur (I hope).  Text is still very likely to move when a cell is focused for the *first* time after reloading a page, since the sizing algorithms in `cell.py` and `notebook_lib.js` are different.\n\nSomeone should review my changes, of course, and perhaps also comment on the slightly changed layouts.  I think the button/toolbars wrap differently than before, e.g., when the browser width is narrow and/or the font size is large.  Does this cause problems on mobiles or when giving presentations?\n\nPositive review!  This is great work!  I'm still quite new to [SASS](http://sass-lang.com/) and [Compass](http://wiki.github.com/chriseppstein/compass), but it seems that they'll make it much easier to edit and manage SageNB stylesheets.\n\nBy the way, can we use SASS, Compass, and/or another tool to find unused CSS directives?",
    "created_at": "2009-12-30T08:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60457",
    "user": "mpatel"
}
```

V12:

* Removes the jQuery include from a few pages, since it's now included in `base.html`.  Including it twice sometimes caused a "mod-2" problem in Firefox --- the browser would claim that (and act as if) the resource `jquery-1.3.2.min.js` was missing.

* Tweaks input cell padding so that text does not move by a pixel on focus or blur (I hope).  Text is still very likely to move when a cell is focused for the *first* time after reloading a page, since the sizing algorithms in `cell.py` and `notebook_lib.js` are different.

Someone should review my changes, of course, and perhaps also comment on the slightly changed layouts.  I think the button/toolbars wrap differently than before, e.g., when the browser width is narrow and/or the font size is large.  Does this cause problems on mobiles or when giving presentations?

Positive review!  This is great work!  I'm still quite new to [SASS](http://sass-lang.com/) and [Compass](http://wiki.github.com/chriseppstein/compass), but it seems that they'll make it much easier to edit and manage SageNB stylesheets.

By the way, can we use SASS, Compass, and/or another tool to find unused CSS directives?



---

archive/issue_comments_060458.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-12-30T08:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60458",
    "user": "mpatel"
}
```

Changing priority from minor to major.



---

archive/issue_comments_060459.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.13.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.13.patch) by mpatel created at 2010-01-01 23:42:23\n\nApply #7811 to `ws_list.js`.  Replaces previous.",
    "created_at": "2010-01-01T23:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60459",
    "user": "mpatel"
}
```

Attachment [trac_7269-table-reduction.13.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.13.patch) by mpatel created at 2010-01-01 23:42:23

Apply #7811 to `ws_list.js`.  Replaces previous.



---

archive/issue_comments_060460.json:
```json
{
    "body": "V13 just applies #7811 to `ws_list.js`.  I believe we still use `notebook_lib.js` for logged in users, but I've made the change, for the sake of completeness.   If it's OK, I'd like to postpone \"subtracting\" `ws_list.js` from `notebook_lib.js` until after published interacts (cf. #6855) are enabled.",
    "created_at": "2010-01-01T23:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60460",
    "user": "mpatel"
}
```

V13 just applies #7811 to `ws_list.js`.  I believe we still use `notebook_lib.js` for logged in users, but I've made the change, for the sake of completeness.   If it's OK, I'd like to postpone "subtracting" `ws_list.js` from `notebook_lib.js` until after published interacts (cf. #6855) are enabled.



---

archive/issue_comments_060461.json:
```json
{
    "body": "Rebase vs. #7811 v2.  Replaces previous.",
    "created_at": "2010-01-02T09:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60461",
    "user": "mpatel"
}
```

Rebase vs. #7811 v2.  Replaces previous.



---

archive/issue_comments_060462.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.14.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.14.patch) by was created at 2010-01-04 07:00:05\n\nI can't merge this into sagenb-0.4.8 (which I'm about to release).   Please rebase it once sage-4.3.1.alpha0 comes out with this new sagenb.  Thanks!\n\n\n```\napplying trac_7269-table-reduction.14.patch\npatching file sagenb/notebook/notebook.py\nHunk #2 succeeded at 950 with fuzz 2 (offset 3 lines).\nHunk #3 FAILED at 1265\nHunk #4 succeeded at 1334 with fuzz 2 (offset 9 lines).\nHunk #5 succeeded at 1407 with fuzz 1 (offset 9 lines).\nHunk #6 succeeded at 1441 with fuzz 1 (offset 9 lines).\nHunk #7 FAILED at 1467\nHunk #8 succeeded at 1486 with fuzz 1 (offset 9 lines).\nHunk #9 succeeded at 1589 with fuzz 1 (offset 9 lines).\nHunk #10 FAILED at 1608\nHunk #11 succeeded at 1651 with fuzz 1 (offset 9 lines).\nHunk #12 FAILED at 1706\nHunk #13 succeeded at 1748 with fuzz 1 (offset 10 lines).\nHunk #14 FAILED at 1757\n5 out of 14 hunks FAILED -- saving rejects to file sagenb/notebook/notebook.py.rej\npatching file sagenb/notebook/twist.py\nHunk #7 succeeded at 960 with fuzz 2 (offset 2 lines).\npatching file sagenb/notebook/worksheet.py\nHunk #1 FAILED at 1712\nHunk #2 FAILED at 1763\nHunk #3 FAILED at 2300\nHunk #4 succeeded at 2442 with fuzz 1 (offset 87 lines).\nHunk #5 succeeded at 2458 with fuzz 1 (offset 87 lines).\n3 out of 6 hunks FAILED -- saving rejects to file sagenb/notebook/worksheet.py.rej\nabort: patch failed to apply\n\n```\n",
    "created_at": "2010-01-04T07:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60462",
    "user": "was"
}
```

Attachment [trac_7269-table-reduction.14.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.14.patch) by was created at 2010-01-04 07:00:05

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

archive/issue_comments_060463.json:
```json
{
    "body": "rebased vs sagenb-0.4.9",
    "created_at": "2010-01-04T19:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60463",
    "user": "timdumol"
}
```

rebased vs sagenb-0.4.9



---

archive/issue_comments_060464.json:
```json
{
    "body": "Attachment [trac_7269-table-reduction.15.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.15.patch) by timdumol created at 2010-01-04 20:00:08\n\nRebased version posted.",
    "created_at": "2010-01-04T20:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60464",
    "user": "timdumol"
}
```

Attachment [trac_7269-table-reduction.15.patch](tarball://root/attachments/some-uuid/ticket7269/trac_7269-table-reduction.15.patch) by timdumol created at 2010-01-04 20:00:08

Rebased version posted.



---

archive/issue_comments_060465.json:
```json
{
    "body": "Can you try applying #7650 first, then V14?  That should give just one, ignorable failure and much less \"fuzz\".  I apologize for not being more explicit about this dependency.",
    "created_at": "2010-01-04T23:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60465",
    "user": "mpatel"
}
```

Can you try applying #7650 first, then V14?  That should give just one, ignorable failure and much less "fuzz".  I apologize for not being more explicit about this dependency.



---

archive/issue_comments_060466.json:
```json
{
    "body": "Of course, this assumes #7650 is reviewed.",
    "created_at": "2010-01-04T23:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60466",
    "user": "mpatel"
}
```

Of course, this assumes #7650 is reviewed.



---

archive/issue_comments_060467.json:
```json
{
    "body": "Merged into sagenb-0.5.   I was able to apply trac_7269-table-reduction.15.patch  just fine without merging in #7650 first.  Yeah.  So this is in and pushed to the official repo.",
    "created_at": "2010-01-04T23:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60467",
    "user": "was"
}
```

Merged into sagenb-0.5.   I was able to apply trac_7269-table-reduction.15.patch  just fine without merging in #7650 first.  Yeah.  So this is in and pushed to the official repo.



---

archive/issue_comments_060468.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T23:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7269#issuecomment-60468",
    "user": "was"
}
```

Resolution: fixed
