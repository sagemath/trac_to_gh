# Issue 7908: Published interacts

archive/issues_007908.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @jvkersch @kcrisman\n\nWorksheets in the Sage notebook can contain live `interact`-ive cells, which may make it easier to understand how an object's properties depend on a set of parameters.\n\nPlease visit the Sage Wiki to view [some examples](http://wiki.sagemath.org/interact).\n\nCurrently, however, `interact` cells do not work in published worksheets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7908\n\n",
    "created_at": "2010-01-12T13:26:52Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Published interacts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7908",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @williamstein @jvkersch @kcrisman

Worksheets in the Sage notebook can contain live `interact`-ive cells, which may make it easier to understand how an object's properties depend on a set of parameters.

Please visit the Sage Wiki to view [some examples](http://wiki.sagemath.org/interact).

Currently, however, `interact` cells do not work in published worksheets.

Issue created by migration from https://trac.sagemath.org/ticket/7908





---

archive/issue_comments_068635.json:
```json
{
    "body": "The chief leftover tasks, I think, are to\n\n* Allow only *interactive* public cells to be evaluated, e.g., someone `evaluate_cell` in a JS console.\n* Limit the use of `sage_eval` in published `interact`s.\n* Enforce the `'doc_pool_size'` (and a `'pub_pool_size'`) but avoid any wrap-around problems. We could add checks in `*_eval` and `*_cell_update`, return an updated `worksheet_filename`, and/or send the user a message (e.g., to reload the page or wait a few minutes and try evaluating again).",
    "created_at": "2010-01-13T17:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68635",
    "user": "https://github.com/qed777"
}
```

The chief leftover tasks, I think, are to

* Allow only *interactive* public cells to be evaluated, e.g., someone `evaluate_cell` in a JS console.
* Limit the use of `sage_eval` in published `interact`s.
* Enforce the `'doc_pool_size'` (and a `'pub_pool_size'`) but avoid any wrap-around problems. We could add checks in `*_eval` and `*_cell_update`, return an updated `worksheet_filename`, and/or send the user a message (e.g., to reload the page or wait a few minutes and try evaluating again).



---

archive/issue_comments_068636.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-13T17:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68636",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068637.json:
```json
{
    "body": "One more task:\n\n* Avoid creating a new cookie (MD5 sum, etc.) for *every* public request.",
    "created_at": "2010-01-13T17:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68637",
    "user": "https://github.com/qed777"
}
```

One more task:

* Avoid creating a new cookie (MD5 sum, etc.) for *every* public request.



---

archive/issue_comments_068638.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n>  * Avoid creating a new cookie (MD5 sum, etc.) for *every* public request.\nI'm not sure about how to set *globally* just one cookie for anonymous visitors.  Setting it `twist.AnonymousToplevel.render` works only for those who visit the login page.  `twist.PublicWorksheet.render` could be a good place.  But it seems we don't actually *use* anonymous cookies, so we could just not generate them at all (see `guard.MySessionWrapper.requestAnonymousAuthentication`).  The sessions do eventually expire; I don't know how much they affect memory use and performance.",
    "created_at": "2010-01-15T01:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68638",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:2 mpatel]:
>  * Avoid creating a new cookie (MD5 sum, etc.) for *every* public request.
I'm not sure about how to set *globally* just one cookie for anonymous visitors.  Setting it `twist.AnonymousToplevel.render` works only for those who visit the login page.  `twist.PublicWorksheet.render` could be a good place.  But it seems we don't actually *use* anonymous cookies, so we could just not generate them at all (see `guard.MySessionWrapper.requestAnonymousAuthentication`).  The sessions do eventually expire; I don't know how much they affect memory use and performance.



---

archive/issue_comments_068639.json:
```json
{
    "body": "V10 allows only published `interact`s to be evaluated.  It also quits the sage process for doc/pub-browser worksheets on unload.",
    "created_at": "2010-01-15T01:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68639",
    "user": "https://github.com/qed777"
}
```

V10 allows only published `interact`s to be evaluated.  It also quits the sage process for doc/pub-browser worksheets on unload.



---

archive/issue_comments_068640.json:
```json
{
    "body": "V11 includes an attempt to reduce flicker and jumping during `interact` updates.",
    "created_at": "2010-01-15T03:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68640",
    "user": "https://github.com/qed777"
}
```

V11 includes an attempt to reduce flicker and jumping during `interact` updates.



---

archive/issue_comments_068641.json:
```json
{
    "body": "By the way, I've also run a few files through the [pep8 checker](http://pypi.python.org/pypi/pep8/0.4.2) with\n\n```sh\npep8 --repeat --show-source --ignore=E251,E301,E302,E501 foo.py\n```\n",
    "created_at": "2010-01-15T03:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68641",
    "user": "https://github.com/qed777"
}
```

By the way, I've also run a few files through the [pep8 checker](http://pypi.python.org/pypi/pep8/0.4.2) with

```sh
pep8 --repeat --show-source --ignore=E251,E301,E302,E501 foo.py
```




---

archive/issue_comments_068642.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> V11 includes an attempt to reduce flicker and jumping during `interact` updates.\nIn particular, we may need to adjust the timing or make it an option.  A `div`'s 'ready' event fires too early.  `DIV`s don't have 'load' events, unfortunately.",
    "created_at": "2010-01-15T21:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68642",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:5 mpatel]:
> V11 includes an attempt to reduce flicker and jumping during `interact` updates.
In particular, we may need to adjust the timing or make it an option.  A `div`'s 'ready' event fires too early.  `DIV`s don't have 'load' events, unfortunately.



---

archive/issue_comments_068643.json:
```json
{
    "body": "Attachment [trac_7908-pub_interact_c11.patch](tarball://root/attachments/some-uuid/ticket7908/trac_7908-pub_interact_c11.patch) by @TimDumol created at 2010-01-17 23:40:20\n\nRebase on a new patch set.",
    "created_at": "2010-01-17T23:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68643",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7908-pub_interact_c11.patch](tarball://root/attachments/some-uuid/ticket7908/trac_7908-pub_interact_c11.patch) by @TimDumol created at 2010-01-17 23:40:20

Rebase on a new patch set.



---

archive/issue_comments_068644.json:
```json
{
    "body": "This is the patch set this was rebased on,\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\ntrac_7666-reviewer.patch\ntrac_7835-preparsing-unicode_v2.patch\ntrac_7249_jinja2_v5.patch\ntrac_2779-sagenb-error-message.patch\n2779_2_banner.patch\ntrac_3154-spurious-u0027-output.patch\ntrac_7969-escaped-backslash.patch\ntrac_7937-sass_manifest.patch\ntrac_4217-html-system-formatting.patch\ntrac_3083-print-documentation.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_5177-delete-cell-dirs.patch\ntrac_7908-pub_interact_c11.patch\n```\n\n\nPlease check if the rebase went wrong: I can't seem to access worksheet pages.",
    "created_at": "2010-01-17T23:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68644",
    "user": "https://github.com/TimDumol"
}
```

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

archive/issue_comments_068645.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-17T23:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68645",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068646.json:
```json
{
    "body": "Hi Tim, Thanks for piling it on --- in a great way!  I'll try to work through the set...",
    "created_at": "2010-01-18T03:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68646",
    "user": "https://github.com/qed777"
}
```

Hi Tim, Thanks for piling it on --- in a great way!  I'll try to work through the set...



---

archive/issue_comments_068647.json:
```json
{
    "body": "Replying to [comment:9 timdumol]:\n> This is the patch set this was rebased on,\n> [...]\n> Please check if the rebase went wrong: I can't seem to access worksheet pages.\n\nIt probably did, given the changes to the queue --- last time I checked, what I posted did work, at least for me.  I would really like this reviewed, given that it's large, I don't want to keep rebasing it (this was transplanted from #6855), implements some potentially useful changes (e.g., JSON-encoding for server-to-client data), and because it's important for #6855.  I'll try to rebase this later this week, after some dust has settled.  Given the many other (and quite welcome) changes afoot right now and the fact that I'm not in Seattle, it doesn't seem practical to this now.",
    "created_at": "2010-01-19T13:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68647",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:9 timdumol]:
> This is the patch set this was rebased on,
> [...]
> Please check if the rebase went wrong: I can't seem to access worksheet pages.

It probably did, given the changes to the queue --- last time I checked, what I posted did work, at least for me.  I would really like this reviewed, given that it's large, I don't want to keep rebasing it (this was transplanted from #6855), implements some potentially useful changes (e.g., JSON-encoding for server-to-client data), and because it's important for #6855.  I'll try to rebase this later this week, after some dust has settled.  Given the many other (and quite welcome) changes afoot right now and the fact that I'm not in Seattle, it doesn't seem practical to this now.



---

archive/issue_comments_068648.json:
```json
{
    "body": "To clarify: I mean that, e.g., the spkg worked for me with 4.3.1.alpha2.  Of course, much has changed in just a few days.",
    "created_at": "2010-01-19T13:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68648",
    "user": "https://github.com/qed777"
}
```

To clarify: I mean that, e.g., the spkg worked for me with 4.3.1.alpha2.  Of course, much has changed in just a few days.



---

archive/issue_comments_068649.json:
```json
{
    "body": "Attachment [trac_7908-pub_interact_c11(3).patch](tarball://root/attachments/some-uuid/ticket7908/trac_7908-pub_interact_c11(3).patch) by @TimDumol created at 2010-01-20 00:03:33\n\nLatest rebase.",
    "created_at": "2010-01-20T00:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68649",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7908-pub_interact_c11(3).patch](tarball://root/attachments/some-uuid/ticket7908/trac_7908-pub_interact_c11(3).patch) by @TimDumol created at 2010-01-20 00:03:33

Latest rebase.



---

archive/issue_comments_068650.json:
```json
{
    "body": "I'm having trouble rebasing it properly. Can you please try rebasing it on, say, sagenb-0.6 + #7249? That should do with most of the rebasing. Alternatively, you can wait till sagenb-0.7, which should be coming real soon due to the number of patches fixed, before rebasing. I'm real sorry that I can't rebase the patch all too well.",
    "created_at": "2010-01-20T08:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68650",
    "user": "https://github.com/TimDumol"
}
```

I'm having trouble rebasing it properly. Can you please try rebasing it on, say, sagenb-0.6 + #7249? That should do with most of the rebasing. Alternatively, you can wait till sagenb-0.7, which should be coming real soon due to the number of patches fixed, before rebasing. I'm real sorry that I can't rebase the patch all too well.



---

archive/issue_comments_068651.json:
```json
{
    "body": "No worries.  I'll definitely take care of it after the next version of SageNB is ready.  I hope you have/had a safe trip!",
    "created_at": "2010-01-21T00:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68651",
    "user": "https://github.com/qed777"
}
```

No worries.  I'll definitely take care of it after the next version of SageNB is ready.  I hope you have/had a safe trip!



---

archive/issue_comments_068652.json:
```json
{
    "body": "Attachment [trac_7908-pub_interact_c11-rebase.patch](tarball://root/attachments/some-uuid/ticket7908/trac_7908-pub_interact_c11-rebase.patch) by @TimDumol created at 2010-04-09 12:28:32\n\nRebase of patch to patch set given in comment.",
    "created_at": "2010-04-09T12:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68652",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7908-pub_interact_c11-rebase.patch](tarball://root/attachments/some-uuid/ticket7908/trac_7908-pub_interact_c11-rebase.patch) by @TimDumol created at 2010-04-09 12:28:32

Rebase of patch to patch set given in comment.



---

archive/issue_comments_068653.json:
```json
{
    "body": "This is the patch set I rebased this on:\n\nsagenb-0.7.5.3 + \n\n\n```\ntrac_5712-interrupt-notification.6.patch\ntrac_7501-codemirror_partB.patch\ntrac_7501-codemirror_partA.patch\ntrac_6069-missing_pub_ws.3.patch\n3154_escaping_quotes.5.patch\ntrac_8249-notebook_cookies.2.patch\ntrac_8436-no_jsmath_for_wrapped.patch\ntrac_8092-init_sage.2.patch\ntrac_8038-email_plus_addressing_v2.patch\ntrac_693-spawn_notebook.3.patch\ntrac_7997-ast-display-hook.patch\ntrac_7633-nb_settings_buttons.patch\ntrac_7633-nb_settings_buttons-reviewer.patch\ntrac_7908-pub_interact_c11.patch\n```\n\n\nI reverted some of the improvements on twist.py (the part with Toplevel's) because it was causing cookie problems. I also renamed cell.py's private variables to use single underscores instead, because that was causing AttributeError's.\n\nI may have made a mistake in the rebasing, because I could not get interacts to work on published worksheets. The controls showed and seemed to work, but the graphics did not display.",
    "created_at": "2010-04-09T12:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68653",
    "user": "https://github.com/TimDumol"
}
```

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

archive/issue_comments_068654.json:
```json
{
    "body": "Hi, any updates on this?",
    "created_at": "2010-04-21T20:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68654",
    "user": "https://github.com/TimDumol"
}
```

Hi, any updates on this?



---

archive/issue_comments_068655.json:
```json
{
    "body": "Just a comment: Mike Hansen pointed out this ticket after I asked a question about it on [AskSage](http://ask.sagemath.org/question/313/using-interactive-commands-in-notebook-when-not/).",
    "created_at": "2011-01-20T16:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68655",
    "user": "https://github.com/jvkersch"
}
```

Just a comment: Mike Hansen pointed out this ticket after I asked a question about it on [AskSage](http://ask.sagemath.org/question/313/using-interactive-commands-in-notebook-when-not/).



---

archive/issue_events_018913.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18913"
}
```



---

archive/issue_events_018914.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18914"
}
```



---

archive/issue_events_018915.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18915"
}
```



---

archive/issue_events_018916.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18916"
}
```



---

archive/issue_events_018917.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18917"
}
```



---

archive/issue_events_018918.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18918"
}
```



---

archive/issue_events_018919.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18919"
}
```



---

archive/issue_comments_068656.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-12-19T14:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68656",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_018920.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-12-19T14:14:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18920"
}
```



---

archive/issue_events_018921.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-12-19T14:14:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18921"
}
```



---

archive/issue_comments_068657.json:
```json
{
    "body": "[Turns out](https://github.com/sagemath/sagenb/commit/35a0c174c1c9c42aea8a059a612aa3e3ab248365) this has been possible (though a highly experimental feature) for over three years!  (Somewhat scarily, they auto-evaluate... but it's cool, very similar in spirit to the cell server.)",
    "created_at": "2014-12-19T14:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68657",
    "user": "https://github.com/kcrisman"
}
```

[Turns out](https://github.com/sagemath/sagenb/commit/35a0c174c1c9c42aea8a059a612aa3e3ab248365) this has been possible (though a highly experimental feature) for over three years!  (Somewhat scarily, they auto-evaluate... but it's cool, very similar in spirit to the cell server.)



---

archive/issue_events_018922.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-01-13T01:16:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7908#event-18922"
}
```



---

archive/issue_comments_068658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-13T01:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7908#issuecomment-68658",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
