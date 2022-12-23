# Issue 7908: Published interacts

Issue created by migration from https://trac.sagemath.org/ticket/7908

Original creator: mpatel

Original creation time: 2010-01-12 13:26:52

Assignee: was

CC:  was jvkersch kcrisman

Worksheets in the Sage notebook can contain live `interact`-ive cells, which may make it easier to understand how an object's properties depend on a set of parameters.

Please visit the Sage Wiki to view [some examples](http://wiki.sagemath.org/interact).

Currently, however, `interact` cells do not work in published worksheets.


---

Comment by mpatel created at 2010-01-13 17:12:31

The chief leftover tasks, I think, are to

 * Allow only _interactive_ public cells to be evaluated, e.g., someone `evaluate_cell` in a JS console.
 * Limit the use of `sage_eval` in published `interact`s.
 * Enforce the `'doc_pool_size'` (and a `'pub_pool_size'`) but avoid any wrap-around problems. We could add checks in `*_eval` and `*_cell_update`, return an updated `worksheet_filename`, and/or send the user a message (e.g., to reload the page or wait a few minutes and try evaluating again).


---

Comment by mpatel created at 2010-01-13 17:12:31

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-13 17:42:19

One more task:

 * Avoid creating a new cookie (MD5 sum, etc.) for _every_ public request.


---

Comment by mpatel created at 2010-01-15 01:26:53

Replying to [comment:2 mpatel]:
>  * Avoid creating a new cookie (MD5 sum, etc.) for _every_ public request.
I'm not sure about how to set _globally_ just one cookie for anonymous visitors.  Setting it `twist.AnonymousToplevel.render` works only for those who visit the login page.  `twist.PublicWorksheet.render` could be a good place.  But it seems we don't actually _use_ anonymous cookies, so we could just not generate them at all (see `guard.MySessionWrapper.requestAnonymousAuthentication`).  The sessions do eventually expire; I don't know how much they affect memory use and performance.


---

Comment by mpatel created at 2010-01-15 01:32:59

V10 allows only published `interact`s to be evaluated.  It also quits the sage process for doc/pub-browser worksheets on unload.


---

Comment by mpatel created at 2010-01-15 03:15:43

V11 includes an attempt to reduce flicker and jumping during `interact` updates.


---

Comment by mpatel created at 2010-01-15 03:34:33

By the way, I've also run a few files through the [pep8 checker](http://pypi.python.org/pypi/pep8/0.4.2) with

```sh
pep8 --repeat --show-source --ignore=E251,E301,E302,E501 foo.py
```



---

Comment by mpatel created at 2010-01-15 21:45:35

Replying to [comment:5 mpatel]:
> V11 includes an attempt to reduce flicker and jumping during `interact` updates.
In particular, we may need to adjust the timing or make it an option.  A `div`'s 'ready' event fires too early.  `DIV`s don't have 'load' events, unfortunately.


---

Attachment

Rebase on a new patch set.


---

Comment by timdumol created at 2010-01-17 23:41:03

This is the patch set this was rebased on,


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
trac_7666-reviewer.patch
trac_7835-preparsing-unicode_v2.patch
trac_7249_jinja2_v5.patch
trac_2779-sagenb-error-message.patch
2779_2_banner.patch
trac_3154-spurious-u0027-output.patch
trac_7969-escaped-backslash.patch
trac_7937-sass_manifest.patch
trac_4217-html-system-formatting.patch
trac_3083-print-documentation.patch
trac_7962-link-worksheets-zip-file.patch
trac_5177-delete-cell-dirs.patch
trac_7908-pub_interact_c11.patch
```


Please check if the rebase went wrong: I can't seem to access worksheet pages.


---

Comment by timdumol created at 2010-01-17 23:41:17

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-01-18 03:51:01

Hi Tim, Thanks for piling it on --- in a great way!  I'll try to work through the set...


---

Comment by mpatel created at 2010-01-19 13:50:28

Replying to [comment:9 timdumol]:
> This is the patch set this was rebased on,
> [...]
> Please check if the rebase went wrong: I can't seem to access worksheet pages.

It probably did, given the changes to the queue --- last time I checked, what I posted did work, at least for me.  I would really like this reviewed, given that it's large, I don't want to keep rebasing it (this was transplanted from #6855), implements some potentially useful changes (e.g., JSON-encoding for server-to-client data), and because it's important for #6855.  I'll try to rebase this later this week, after some dust has settled.  Given the many other (and quite welcome) changes afoot right now and the fact that I'm not in Seattle, it doesn't seem practical to this now.


---

Comment by mpatel created at 2010-01-19 13:52:02

To clarify: I mean that, e.g., the spkg worked for me with 4.3.1.alpha2.  Of course, much has changed in just a few days.


---

Attachment

Latest rebase.


---

Comment by timdumol created at 2010-01-20 08:28:09

I'm having trouble rebasing it properly. Can you please try rebasing it on, say, sagenb-0.6 + #7249? That should do with most of the rebasing. Alternatively, you can wait till sagenb-0.7, which should be coming real soon due to the number of patches fixed, before rebasing. I'm real sorry that I can't rebase the patch all too well.


---

Comment by mpatel created at 2010-01-21 00:52:07

No worries.  I'll definitely take care of it after the next version of SageNB is ready.  I hope you have/had a safe trip!


---

Attachment

Rebase of patch to patch set given in comment.


---

Comment by timdumol created at 2010-04-09 12:33:39

This is the patch set I rebased this on:

sagenb-0.7.5.3 + 


```
trac_5712-interrupt-notification.6.patch
trac_7501-codemirror_partB.patch
trac_7501-codemirror_partA.patch
trac_6069-missing_pub_ws.3.patch
3154_escaping_quotes.5.patch
trac_8249-notebook_cookies.2.patch
trac_8436-no_jsmath_for_wrapped.patch
trac_8092-init_sage.2.patch
trac_8038-email_plus_addressing_v2.patch
trac_693-spawn_notebook.3.patch
trac_7997-ast-display-hook.patch
trac_7633-nb_settings_buttons.patch
trac_7633-nb_settings_buttons-reviewer.patch
trac_7908-pub_interact_c11.patch
```


I reverted some of the improvements on twist.py (the part with Toplevel's) because it was causing cookie problems. I also renamed cell.py's private variables to use single underscores instead, because that was causing AttributeError's.

I may have made a mistake in the rebasing, because I could not get interacts to work on published worksheets. The controls showed and seemed to work, but the graphics did not display.


---

Comment by timdumol created at 2010-04-21 20:13:16

Hi, any updates on this?


---

Comment by jvkersch created at 2011-01-20 16:02:24

Just a comment: Mike Hansen pointed out this ticket after I asked a question about it on [AskSage](http://ask.sagemath.org/question/313/using-interactive-commands-in-notebook-when-not/).


---

Comment by kcrisman created at 2014-12-19 14:14:42

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2014-12-19 14:14:42

[Turns out](https://github.com/sagemath/sagenb/commit/35a0c174c1c9c42aea8a059a612aa3e3ab248365) this has been possible (though a highly experimental feature) for over three years!  (Somewhat scarily, they auto-evaluate... but it's cool, very similar in spirit to the cell server.)


---

Comment by vbraun created at 2015-01-13 01:16:20

Resolution: fixed
