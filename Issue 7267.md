# Issue 7267: Add a compact color picker to SageNB

archive/issues_007267.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jasongrout @williamstein\n\nA compact alternative to [Farbtastic](http://acko.net/dev/farbtastic) would be useful in space-constrained interacts and notebook/user settings pages.\n\nCandidates:\n\n* [Color Picker](http://www.eyecon.ro/colorpicker/)\n* [jPicker](http://www.digitalmagicpro.com/jPicker/)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7267\n\n",
    "created_at": "2009-10-23T07:36:06Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Add a compact color picker to SageNB",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7267",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @jasongrout @williamstein

A compact alternative to [Farbtastic](http://acko.net/dev/farbtastic) would be useful in space-constrained interacts and notebook/user settings pages.

Candidates:

* [Color Picker](http://www.eyecon.ro/colorpicker/)
* [jPicker](http://www.digitalmagicpro.com/jPicker/)



Issue created by migration from https://trac.sagemath.org/ticket/7267





---

archive/issue_comments_060264.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-08T05:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60264",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060265.json:
```json
{
    "body": "There's a patch at\n\n* http://sage.math.washington.edu/home/mpatel/trac/7267/trac_7267_color_choosers.patch\n\nThe patch \n\n* Adds both [ColorPicker](http://www.eyecon.ro/colorpicker/) and [jPicker](http://www.digitalmagicpro.com/jPicker/).\n* Adds a dedicated `color_selector()` `interact` control.  The keyword option\n  * `widget` selects the widget to render.  The choices are `'farbtastic'` (the default), `'jpicker'`, and `'colorpicker'`.\n  * `hide_box` (default: `False`) sets whether the input box is visible.\n\nHere's a compact example:\n\n```python\n@interact\ndef _(color=color_selector((1,0,1), label='', widget='jpicker', hide_box=True)):\n    show(plot(x / (8/7 + sin(x)), (x, -50, 50), fill=True, fillcolor=color))\n```\n\n\nRemarks:\n\n* jPicker adds itself as a (grand)<sup>n</sup>-child of the output cell, so it's confined to that area.  This is a problem, e.g., when `auto_update=False` and a plot disappears.  The smarter ColorPicker appends itself to `document.body`, similarly to jQuery UI's dialogs.\n\n* Continuously or rapidly changing *any* of the widgets sends so many requests to the server that a rendered `interact`'s final color may not match the final selected color.  The server does receive the final color, according to a print statement in `twist.Worksheet_eval`.  I'm not sure what happens to the corresponding output.  Anyway, I think this is an important but separate problem.\n\n* In a future ticket, I'll set up one of the new choosers for user, worksheet, and notebook settings pages.  See `sagenb.notebook.conf.Configuration.html_table()` and `server_conf` for details.",
    "created_at": "2009-11-08T05:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60265",
    "user": "https://github.com/qed777"
}
```

There's a patch at

* http://sage.math.washington.edu/home/mpatel/trac/7267/trac_7267_color_choosers.patch

The patch 

* Adds both [ColorPicker](http://www.eyecon.ro/colorpicker/) and [jPicker](http://www.digitalmagicpro.com/jPicker/).
* Adds a dedicated `color_selector()` `interact` control.  The keyword option
  * `widget` selects the widget to render.  The choices are `'farbtastic'` (the default), `'jpicker'`, and `'colorpicker'`.
  * `hide_box` (default: `False`) sets whether the input box is visible.

Here's a compact example:

```python
@interact
def _(color=color_selector((1,0,1), label='', widget='jpicker', hide_box=True)):
    show(plot(x / (8/7 + sin(x)), (x, -50, 50), fill=True, fillcolor=color))
```


Remarks:

* jPicker adds itself as a (grand)<sup>n</sup>-child of the output cell, so it's confined to that area.  This is a problem, e.g., when `auto_update=False` and a plot disappears.  The smarter ColorPicker appends itself to `document.body`, similarly to jQuery UI's dialogs.

* Continuously or rapidly changing *any* of the widgets sends so many requests to the server that a rendered `interact`'s final color may not match the final selected color.  The server does receive the final color, according to a print statement in `twist.Worksheet_eval`.  I'm not sure what happens to the corresponding output.  Anyway, I think this is an important but separate problem.

* In a future ticket, I'll set up one of the new choosers for user, worksheet, and notebook settings pages.  See `sagenb.notebook.conf.Configuration.html_table()` and `server_conf` for details.



---

archive/issue_comments_060266.json:
```json
{
    "body": "If it helps, this patch is\n\n```\ntrac_7316-sageinspect_defn.patch\ntrac_7318-sphinxify_confdir.patch\ntrac_7309-javascript-sage_v2.patch\ntrac_7310-modals.6.patch\ntrac_7332-css-escape.2.patch\ntrac_sagenb-7341.patch\ntrac_sagenb-7346.patch\ntrac_7339-sagenb_cell_bugs.patch\ntrac_7343-selenium-tests.4.patch\ntrac_7390-sagenb_test_report_A.patch\ntrac_7390-sagenb_test_report_B_v2.patch\ntrac_7267_color_choosers.patch                   # HERE!\ntrac_7404-css_worksheet_title.patch\ntrac_7385-renaming-published-worksheets.patch\ntrac_7384-sphinxify-docstrings.patch\ntrac_7354-jsmath_undo_revision.patch\ntrac_7322-jsmath_upgrade.patch\ntrac_7106-paren_match_doc.patch\n```\n\nin my sagenb patch queue.  But I think the only potential conflict is in `sagenb/data/sage/html/notebook/head.tmpl`.",
    "created_at": "2009-11-08T05:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60266",
    "user": "https://github.com/qed777"
}
```

If it helps, this patch is

```
trac_7316-sageinspect_defn.patch
trac_7318-sphinxify_confdir.patch
trac_7309-javascript-sage_v2.patch
trac_7310-modals.6.patch
trac_7332-css-escape.2.patch
trac_sagenb-7341.patch
trac_sagenb-7346.patch
trac_7339-sagenb_cell_bugs.patch
trac_7343-selenium-tests.4.patch
trac_7390-sagenb_test_report_A.patch
trac_7390-sagenb_test_report_B_v2.patch
trac_7267_color_choosers.patch                   # HERE!
trac_7404-css_worksheet_title.patch
trac_7385-renaming-published-worksheets.patch
trac_7384-sphinxify-docstrings.patch
trac_7354-jsmath_undo_revision.patch
trac_7322-jsmath_upgrade.patch
trac_7106-paren_match_doc.patch
```

in my sagenb patch queue.  But I think the only potential conflict is in `sagenb/data/sage/html/notebook/head.tmpl`.



---

archive/issue_comments_060267.json:
```json
{
    "body": "By the way, should we \"polish\" `interact`'s docstring and move it to the top of its reference manual section?",
    "created_at": "2009-11-08T05:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60267",
    "user": "https://github.com/qed777"
}
```

By the way, should we "polish" `interact`'s docstring and move it to the top of its reference manual section?



---

archive/issue_comments_060268.json:
```json
{
    "body": "Although both of the new jQuery plug-ins are relatively short, we should consider loading them lazily.  [Ajile](http://ajile.net/) may help.  I'll try to investigate.",
    "created_at": "2009-11-08T05:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60268",
    "user": "https://github.com/qed777"
}
```

Although both of the new jQuery plug-ins are relatively short, we should consider loading them lazily.  [Ajile](http://ajile.net/) may help.  I'll try to investigate.



---

archive/issue_comments_060269.json:
```json
{
    "body": "I should add that I have absolutely no problem with not including one or both selectors in `head.tmpl.`  I'll just need to update `interact.py`.  But I think we should have a compact color picker for the settings pages.",
    "created_at": "2009-11-10T03:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60269",
    "user": "https://github.com/qed777"
}
```

I should add that I have absolutely no problem with not including one or both selectors in `head.tmpl.`  I'll just need to update `interact.py`.  But I think we should have a compact color picker for the settings pages.



---

archive/issue_events_017190.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2009-11-12T01:46:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7267#event-17190"
}
```



---

archive/issue_comments_060270.json:
```json
{
    "body": "IMHO, it may be best to have a particular reason to include these packages (i.e., create a patch that makes use of either of them) first, so as to prevent including these and leaving them orphaned in the source tree. I personally favor ColorPicker over jPicker, since it is more customizable, and apparently has better functionality, as you previously remarked.",
    "created_at": "2009-11-15T10:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60270",
    "user": "https://github.com/TimDumol"
}
```

IMHO, it may be best to have a particular reason to include these packages (i.e., create a patch that makes use of either of them) first, so as to prevent including these and leaving them orphaned in the source tree. I personally favor ColorPicker over jPicker, since it is more customizable, and apparently has better functionality, as you previously remarked.



---

archive/issue_comments_060271.json:
```json
{
    "body": "For what it's worth, here's what I have in mind:\n\n* For a [settings page](http://groups.google.com/group/sage-devel/browse_thread/thread/9a5262dfaada469e/764b6f135d926ccd?#764b6f135d926ccd) with many color options (active / inactive cell text, background, etc.), we can use either CP or jP.  For default plot options, e.g., that involve transparency, it's better to use jP.  (It's possible to bind multiple inputs to one instance of F, but I'd like the option to have independent, compact widgets).\n\n* For interacts, CP is a good default compact color selector, since it works better than jP when `auto_update=False`.  But I'm planning to add transparency control with jP, probably in a successor to #260 and the #5601-#5605 sequence that extends Sage's `Color` to matplotlib's RGBA tuples.\n\n* For a [plot options control panel](http://groups.google.com/group/sage-support/msg/ca41dc7496254063) --- double-click on a plot to open the dialog --- I'd like to support transparency (cf. [file:///home/mitesh/sage/doc/output/html/en/reference/sage/plot/plot.html 2D plots] and planned RGBA) so jP is a logical choice.",
    "created_at": "2009-11-16T18:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60271",
    "user": "https://github.com/qed777"
}
```

For what it's worth, here's what I have in mind:

* For a [settings page](http://groups.google.com/group/sage-devel/browse_thread/thread/9a5262dfaada469e/764b6f135d926ccd?#764b6f135d926ccd) with many color options (active / inactive cell text, background, etc.), we can use either CP or jP.  For default plot options, e.g., that involve transparency, it's better to use jP.  (It's possible to bind multiple inputs to one instance of F, but I'd like the option to have independent, compact widgets).

* For interacts, CP is a good default compact color selector, since it works better than jP when `auto_update=False`.  But I'm planning to add transparency control with jP, probably in a successor to #260 and the #5601-#5605 sequence that extends Sage's `Color` to matplotlib's RGBA tuples.

* For a [plot options control panel](http://groups.google.com/group/sage-support/msg/ca41dc7496254063) --- double-click on a plot to open the dialog --- I'd like to support transparency (cf. [file:///home/mitesh/sage/doc/output/html/en/reference/sage/plot/plot.html 2D plots] and planned RGBA) so jP is a logical choice.



---

archive/issue_comments_060272.json:
```json
{
    "body": "Here is a list of files modified by this patch:\n\n\n```\nM sagenb/data/sage/html/notebook/head.tmpl\nM sagenb/notebook/all.py\nM sagenb/notebook/interact.py\n? gosage\n? sagenb/data/jquery/plugins/colorpicker/css/colorpicker.css\n? sagenb/data/jquery/plugins/colorpicker/css/layout.css\n? sagenb/data/jquery/plugins/colorpicker/images/blank.gif\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_background.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hex.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hsb_b.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hsb_h.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hsb_s.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_indic.gif\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_overlay.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_rgb_b.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_rgb_g.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_rgb_r.png\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_select.gif\n? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_submit.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_background.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_hex.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_hsb_b.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_hsb_h.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_hsb_s.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_indic.gif\n? sagenb/data/jquery/plugins/colorpicker/images/custom_rgb_b.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_rgb_g.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_rgb_r.png\n? sagenb/data/jquery/plugins/colorpicker/images/custom_submit.png\n? sagenb/data/jquery/plugins/colorpicker/images/select.png\n? sagenb/data/jquery/plugins/colorpicker/images/select2.png\n? sagenb/data/jquery/plugins/colorpicker/images/slider.png\n? sagenb/data/jquery/plugins/colorpicker/index.html\n? sagenb/data/jquery/plugins/colorpicker/js/colorpicker.js\n? sagenb/data/jquery/plugins/colorpicker/js/colorpicker.min.js\n? sagenb/data/jquery/plugins/colorpicker/js/eye.js\n? sagenb/data/jquery/plugins/colorpicker/js/jquery.js\n? sagenb/data/jquery/plugins/colorpicker/js/layout.js\n? sagenb/data/jquery/plugins/colorpicker/js/utils.js\n? sagenb/data/jquery/plugins/jpicker/css/jPicker-1.0.11.css\n? sagenb/data/jquery/plugins/jpicker/images/Bars.png\n? sagenb/data/jquery/plugins/jpicker/images/Maps.png\n? sagenb/data/jquery/plugins/jpicker/images/bar-opacity.png\n? sagenb/data/jquery/plugins/jpicker/images/map-opacity.png\n? sagenb/data/jquery/plugins/jpicker/images/mappoint.gif\n? sagenb/data/jquery/plugins/jpicker/images/picker.gif\n? sagenb/data/jquery/plugins/jpicker/images/preview-opacity.png\n? sagenb/data/jquery/plugins/jpicker/images/rangearrows.gif\n? sagenb/data/jquery/plugins/jpicker/images/rangearrows2.gif\n? sagenb/data/jquery/plugins/jpicker/jpicker-1.0.11.js\n? sagenb/data/jquery/plugins/jpicker/jpicker-1.0.11.min.js\n```\n",
    "created_at": "2009-12-08T23:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60272",
    "user": "https://github.com/williamstein"
}
```

Here is a list of files modified by this patch:


```
M sagenb/data/sage/html/notebook/head.tmpl
M sagenb/notebook/all.py
M sagenb/notebook/interact.py
? gosage
? sagenb/data/jquery/plugins/colorpicker/css/colorpicker.css
? sagenb/data/jquery/plugins/colorpicker/css/layout.css
? sagenb/data/jquery/plugins/colorpicker/images/blank.gif
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_background.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hex.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hsb_b.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hsb_h.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_hsb_s.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_indic.gif
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_overlay.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_rgb_b.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_rgb_g.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_rgb_r.png
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_select.gif
? sagenb/data/jquery/plugins/colorpicker/images/colorpicker_submit.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_background.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_hex.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_hsb_b.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_hsb_h.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_hsb_s.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_indic.gif
? sagenb/data/jquery/plugins/colorpicker/images/custom_rgb_b.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_rgb_g.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_rgb_r.png
? sagenb/data/jquery/plugins/colorpicker/images/custom_submit.png
? sagenb/data/jquery/plugins/colorpicker/images/select.png
? sagenb/data/jquery/plugins/colorpicker/images/select2.png
? sagenb/data/jquery/plugins/colorpicker/images/slider.png
? sagenb/data/jquery/plugins/colorpicker/index.html
? sagenb/data/jquery/plugins/colorpicker/js/colorpicker.js
? sagenb/data/jquery/plugins/colorpicker/js/colorpicker.min.js
? sagenb/data/jquery/plugins/colorpicker/js/eye.js
? sagenb/data/jquery/plugins/colorpicker/js/jquery.js
? sagenb/data/jquery/plugins/colorpicker/js/layout.js
? sagenb/data/jquery/plugins/colorpicker/js/utils.js
? sagenb/data/jquery/plugins/jpicker/css/jPicker-1.0.11.css
? sagenb/data/jquery/plugins/jpicker/images/Bars.png
? sagenb/data/jquery/plugins/jpicker/images/Maps.png
? sagenb/data/jquery/plugins/jpicker/images/bar-opacity.png
? sagenb/data/jquery/plugins/jpicker/images/map-opacity.png
? sagenb/data/jquery/plugins/jpicker/images/mappoint.gif
? sagenb/data/jquery/plugins/jpicker/images/picker.gif
? sagenb/data/jquery/plugins/jpicker/images/preview-opacity.png
? sagenb/data/jquery/plugins/jpicker/images/rangearrows.gif
? sagenb/data/jquery/plugins/jpicker/images/rangearrows2.gif
? sagenb/data/jquery/plugins/jpicker/jpicker-1.0.11.js
? sagenb/data/jquery/plugins/jpicker/jpicker-1.0.11.min.js
```




---

archive/issue_comments_060273.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T23:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60273",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060274.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. General remark/question.  Is there any way we can get rid of stuff like this, where the exact version number is explicitly given:\n\n```\n+<link rel=\"stylesheet\" href=\"/javascript/jquery/plugins/jpicker/css/jPicker-1.0.11.css\" type=\"text/css\" />\n+<script type=\"text/javascript\" src=\"/javascript/jquery/plugins/jpicker/jpicker-1.0.11.min.js\"></script>\n```\n\nThis is I think happening more and more in the code, and I think it makes it difficult to upgrade the plugins.  Could we use symbolic links or something else that is clever (perhaps in twist.py) to get around this?\n\nI don't think this is specific to this ticket, so I'm not considering this in refereeing this patch. \n\n...\n\nActually, WOW this is a really nice patch!   It must have been quite a lot of work, and really gives the notebook some real added depth.  Thanks!\n\nEverything looks good.  It works fine. \n\nWilliam",
    "created_at": "2009-12-08T23:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60274",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

1. General remark/question.  Is there any way we can get rid of stuff like this, where the exact version number is explicitly given:

```
+<link rel="stylesheet" href="/javascript/jquery/plugins/jpicker/css/jPicker-1.0.11.css" type="text/css" />
+<script type="text/javascript" src="/javascript/jquery/plugins/jpicker/jpicker-1.0.11.min.js"></script>
```

This is I think happening more and more in the code, and I think it makes it difficult to upgrade the plugins.  Could we use symbolic links or something else that is clever (perhaps in twist.py) to get around this?

I don't think this is specific to this ticket, so I'm not considering this in refereeing this patch. 

...

Actually, WOW this is a really nice patch!   It must have been quite a lot of work, and really gives the notebook some real added depth.  Thanks!

Everything looks good.  It works fine. 

William



---

archive/issue_comments_060275.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T01:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60275",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_017191.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-09T01:12:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7267#event-17191"
}
```



---

archive/issue_comments_060276.json:
```json
{
    "body": "I merged this patch into sagenb-0.4.6.",
    "created_at": "2009-12-09T01:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60276",
    "user": "https://github.com/williamstein"
}
```

I merged this patch into sagenb-0.4.6.



---

archive/issue_comments_060277.json:
```json
{
    "body": "Thanks!  On version numbers:  We could use symbolic links, but I don't think they're available on Windows (cf. [os](http://docs.python.org/library/os.html), #6614).",
    "created_at": "2009-12-10T00:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60277",
    "user": "https://github.com/qed777"
}
```

Thanks!  On version numbers:  We could use symbolic links, but I don't think they're available on Windows (cf. [os](http://docs.python.org/library/os.html), #6614).



---

archive/issue_comments_060278.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> Thanks!  On version numbers:  We could use symbolic links, but I don't \n> think they're available on Windows (cf. [os](http://docs.python.org/library/os.html), #6614).\n\nThe sage notebook doesn't work on Windows yet though....  However, another option is just to rename the installed library folder without the version numbers (so no symbolic link is needed).  As long as we include a README things should be clear.",
    "created_at": "2009-12-10T06:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7267#issuecomment-60278",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:12 mpatel]:
> Thanks!  On version numbers:  We could use symbolic links, but I don't 
> think they're available on Windows (cf. [os](http://docs.python.org/library/os.html), #6614).

The sage notebook doesn't work on Windows yet though....  However, another option is just to rename the installed library folder without the version numbers (so no symbolic link is needed).  As long as we include a README things should be clear.
