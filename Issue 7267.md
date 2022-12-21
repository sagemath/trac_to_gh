# Issue 7267: Add a compact color picker to SageNB

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-10-23 07:36:06

Assignee: boothby

CC:  jason was

A compact alternative to [Farbtastic](http://acko.net/dev/farbtastic) would be useful in space-constrained interacts and notebook/user settings pages.

Candidates:

 * [Color Picker](http://www.eyecon.ro/colorpicker/)
 * [jPicker](http://www.digitalmagicpro.com/jPicker/)




---

Comment by mpatel created at 2009-11-08 05:27:00

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-08 05:27:00

There's a patch at

 * http://sage.math.washington.edu/home/mpatel/trac/7267/trac_7267_color_choosers.patch

The patch 

 * Adds both [ColorPicker](http://www.eyecon.ro/colorpicker/) and [jPicker](http://www.digitalmagicpro.com/jPicker/).
 * Adds a dedicated `color_selector()` `interact` control.  The keyword option
   * `widget` selects the widget to render.  The choices are `'farbtastic'` (the default), `'jpicker'`, and `'colorpicker'`.
   * `hide_box` (default: `False`) sets whether the input box is visible.

Here's a compact example:

```python
`@`interact
def _(color=color_selector((1,0,1), label='', widget='jpicker', hide_box=True)):
    show(plot(x / (8/7 + sin(x)), (x, -50, 50), fill=True, fillcolor=color))
```


Remarks:

 * jPicker adds itself as a (grand)<sup>n</sup>-child of the output cell, so it's confined to that area.  This is a problem, e.g., when `auto_update=False` and a plot disappears.  The smarter ColorPicker appends itself to `document.body`, similarly to jQuery UI's dialogs.

 * Continuously or rapidly changing _any_ of the widgets sends so many requests to the server that a rendered `interact`'s final color may not match the final selected color.  The server does receive the final color, according to a print statement in `twist.Worksheet_eval`.  I'm not sure what happens to the corresponding output.  Anyway, I think this is an important but separate problem.

 * In a future ticket, I'll set up one of the new choosers for user, worksheet, and notebook settings pages.  See `sagenb.notebook.conf.Configuration.html_table()` and `server_conf` for details.


---

Comment by mpatel created at 2009-11-08 05:30:55

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

Comment by mpatel created at 2009-11-08 05:33:38

By the way, should we "polish" `interact`'s docstring and move it to the top of its reference manual section?


---

Comment by mpatel created at 2009-11-08 05:38:19

Although both of the new jQuery plug-ins are relatively short, we should consider loading them lazily.  [Ajile](http://ajile.net/) may help.  I'll try to investigate.


---

Comment by mpatel created at 2009-11-10 03:36:43

I should add that I have absolutely no problem with not including one or both selectors in `head.tmpl.`  I'll just need to update `interact.py`.  But I think we should have a compact color picker for the settings pages.


---

Comment by timdumol created at 2009-11-15 10:25:45

IMHO, it may be best to have a particular reason to include these packages (i.e., create a patch that makes use of either of them) first, so as to prevent including these and leaving them orphaned in the source tree. I personally favor ColorPicker over jPicker, since it is more customizable, and apparently has better functionality, as you previously remarked.


---

Comment by mpatel created at 2009-11-16 18:42:04

For what it's worth, here's what I have in mind:

 * For a [settings page](http://groups.google.com/group/sage-devel/browse_thread/thread/9a5262dfaada469e/764b6f135d926ccd?#764b6f135d926ccd) with many color options (active / inactive cell text, background, etc.), we can use either CP or jP.  For default plot options, e.g., that involve transparency, it's better to use jP.  (It's possible to bind multiple inputs to one instance of F, but I'd like the option to have independent, compact widgets).

 * For interacts, CP is a good default compact color selector, since it works better than jP when `auto_update=False`.  But I'm planning to add transparency control with jP, probably in a successor to #260 and the #5601-#5605 sequence that extends Sage's `Color` to matplotlib's RGBA tuples.

 * For a [plot options control panel](http://groups.google.com/group/sage-support/msg/ca41dc7496254063) --- double-click on a plot to open the dialog --- I'd like to support transparency (cf. [file:///home/mitesh/sage/doc/output/html/en/reference/sage/plot/plot.html 2D plots] and planned RGBA) so jP is a logical choice.


---

Comment by was created at 2009-12-08 23:42:00

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

Comment by was created at 2009-12-08 23:57:16

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-08 23:57:16

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

Comment by was created at 2009-12-09 01:12:17

Resolution: fixed


---

Comment by was created at 2009-12-09 01:12:17

I merged this patch into sagenb-0.4.6.


---

Comment by mpatel created at 2009-12-10 00:58:07

Thanks!  On version numbers:  We could use symbolic links, but I don't think they're available on Windows (cf. [os](http://docs.python.org/library/os.html), #6614).


---

Comment by was created at 2009-12-10 06:58:31

Replying to [comment:12 mpatel]:
> Thanks!  On version numbers:  We could use symbolic links, but I don't 
> think they're available on Windows (cf. [os](http://docs.python.org/library/os.html), #6614).

The sage notebook doesn't work on Windows yet though....  However, another option is just to rename the installed library folder without the version numbers (so no symbolic link is needed).  As long as we include a README things should be clear.
