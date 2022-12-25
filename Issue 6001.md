# Issue 6001: [with patch, needs work] tear out docstrings in the notebook into a new window

archive/issues_006001.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jhpalmieri\n\nAs mentioned in [this message](http://groups.google.com/group/sage-devel/msg/d021522accd00e81), it might be useful to tear/pop/pull/rip out/off/up at least some notebook introspection window(s) into a separate window(s) [1].\n\nThis ticket, which builds on #5653 (see comments [comment:ticket:5653:19 19ff]), is currently a ~~disaster~~ test area for variations on this theme.\n\nIn the near future, I'm hoping to send a message to sage-devel to gauge interest, get more suggestions, etc., about similar potential improvements.\n\nRelated: #4714, #5644, #5653. [2]\n\n[1] Nevertheless, they're all fine docstrings.\n[2] Almost surely, this is far from exhaustive or even representative.  Feel free to add to the list.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6001\n\n",
    "created_at": "2009-05-06T23:14:40Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs work] tear out docstrings in the notebook into a new window",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6001",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @jhpalmieri

As mentioned in [this message](http://groups.google.com/group/sage-devel/msg/d021522accd00e81), it might be useful to tear/pop/pull/rip out/off/up at least some notebook introspection window(s) into a separate window(s) [1].

This ticket, which builds on #5653 (see comments [comment:ticket:5653:19 19ff]), is currently a ~~disaster~~ test area for variations on this theme.

In the near future, I'm hoping to send a message to sage-devel to gauge interest, get more suggestions, etc., about similar potential improvements.

Related: #4714, #5644, #5653. [2]

[1] Nevertheless, they're all fine docstrings.
[2] Almost surely, this is far from exhaustive or even representative.  Feel free to add to the list.

Issue created by migration from https://trac.sagemath.org/ticket/6001





---

archive/issue_comments_047642.json:
```json
{
    "body": "Attachment [trac_6001_tearout_docstring_v1.patch](tarball://root/attachments/some-uuid/ticket6001/trac_6001_tearout_docstring_v1.patch) by @qed777 created at 2009-05-06 23:19:50\n\nNeeds accompanying introspect.js",
    "created_at": "2009-05-06T23:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47642",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6001_tearout_docstring_v1.patch](tarball://root/attachments/some-uuid/ticket6001/trac_6001_tearout_docstring_v1.patch) by @qed777 created at 2009-05-06 23:19:50

Needs accompanying introspect.js



---

archive/issue_comments_047643.json:
```json
{
    "body": "Attachment [introspect_v1.js](tarball://root/attachments/some-uuid/ticket6001/introspect_v1.js) by @qed777 created at 2009-05-06 23:21:10\n\nFor now, this should be javascript_local/introspect.js",
    "created_at": "2009-05-06T23:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47643",
    "user": "https://github.com/qed777"
}
```

Attachment [introspect_v1.js](tarball://root/attachments/some-uuid/ticket6001/introspect_v1.js) by @qed777 created at 2009-05-06 23:21:10

For now, this should be javascript_local/introspect.js



---

archive/issue_comments_047644.json:
```json
{
    "body": "I've attached a first take.  Directions:\n\n* Apply [attachment:ticket:5653:docstring.4.patch docstring.4.patch] from #5653.\n\n* Apply [attachment:ticket:6001:trac_6001_tearout_docstring_v1.patch trac_6001_tearout_docstring_v1.patch].\n\n* Save [attachment:ticket:6001:introspect_v1.js introspect_v1.js] to `javascript_local/introspect.js`, that is,\n\n```\nSAGE_ROOT/local/notebook/javascript/introspect.js\n```\n\n\n* Remove .lock and .html files from the doc cache.  The default location is `DOT_SAGE/sage_notebook/doc/`",
    "created_at": "2009-05-06T23:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47644",
    "user": "https://github.com/qed777"
}
```

I've attached a first take.  Directions:

* Apply [attachment:ticket:5653:docstring.4.patch docstring.4.patch] from #5653.

* Apply [attachment:ticket:6001:trac_6001_tearout_docstring_v1.patch trac_6001_tearout_docstring_v1.patch].

* Save [attachment:ticket:6001:introspect_v1.js introspect_v1.js] to `javascript_local/introspect.js`, that is,

```
SAGE_ROOT/local/notebook/javascript/introspect.js
```


* Remove .lock and .html files from the doc cache.  The default location is `DOT_SAGE/sage_notebook/doc/`



---

archive/issue_comments_047645.json:
```json
{
    "body": "Notes:\n\n* Ultimately, the open tab vs. open window decision comes down to a user's browser settings.  The author can't force this either way, it seems.\n* Opera 9 Linux: Works when \"new window\" links are set to open tabs or to open windows.\n* Firefox 3 Linux: Works when set to open windows, but not necessarily when set to open tabs.  The latter depends on whether `introspect.open()` opens a *sized* window.  Please experiment with the [window.open()](http://www.w3schools.com/HTMLDOM/met_win_open.asp) lines in introspect.js and let me know.  Even with [FireBug's](http://getfirebug.com/) help, I don't know what's wrong.\n* The new window and its children are generated dynamically, somewhat in keeping with the transient nature of Sage's introspection `div`s.  Accordingly, commands like \"view source\" and \"refresh page\" may not work as expected.\n* The font-sizing stuff is just an experiment.\n* I have no strong opinions on cosmetic issues, including default font sizes, layouts, etc.  Actually, I'd rather not make these decisions, so please make suggestions.  Later, we can move CSS directives to `css.py`.\n* Modulo ordering, the 'sagedoc' window should be a fixed point with respect to local tear outs.\n* The unordered list of docstrings should be sortable, thanks to [jQuery UI](http://jqueryui.com/demos/).  To see this, I temporarily disable Firefox's [Grab and Drag](https://addons.mozilla.org/en-US/firefox/addon/1250) extension via ALT+SHIFT+D.  Perhaps there's a workaround.\n* The code in `introspect.js` is a mix of jQuery and DOM methods.  This may not be optimal.\n* Evidently, JavaScript is no Python, as [this video](http://www.youtube.com/watch?v=hQVTIJBZook) demonstrates.\n* For now, `introspect.close()` won't work for \"SHIFT-ENTER\" docstrings, because the notebook treats them differently from \"TAB\" docstrings.  See #5644.\n* See #4714 about making jsMath inclusions and tweaks more manageable.",
    "created_at": "2009-05-07T01:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47645",
    "user": "https://github.com/qed777"
}
```

Notes:

* Ultimately, the open tab vs. open window decision comes down to a user's browser settings.  The author can't force this either way, it seems.
* Opera 9 Linux: Works when "new window" links are set to open tabs or to open windows.
* Firefox 3 Linux: Works when set to open windows, but not necessarily when set to open tabs.  The latter depends on whether `introspect.open()` opens a *sized* window.  Please experiment with the [window.open()](http://www.w3schools.com/HTMLDOM/met_win_open.asp) lines in introspect.js and let me know.  Even with [FireBug's](http://getfirebug.com/) help, I don't know what's wrong.
* The new window and its children are generated dynamically, somewhat in keeping with the transient nature of Sage's introspection `div`s.  Accordingly, commands like "view source" and "refresh page" may not work as expected.
* The font-sizing stuff is just an experiment.
* I have no strong opinions on cosmetic issues, including default font sizes, layouts, etc.  Actually, I'd rather not make these decisions, so please make suggestions.  Later, we can move CSS directives to `css.py`.
* Modulo ordering, the 'sagedoc' window should be a fixed point with respect to local tear outs.
* The unordered list of docstrings should be sortable, thanks to [jQuery UI](http://jqueryui.com/demos/).  To see this, I temporarily disable Firefox's [Grab and Drag](https://addons.mozilla.org/en-US/firefox/addon/1250) extension via ALT+SHIFT+D.  Perhaps there's a workaround.
* The code in `introspect.js` is a mix of jQuery and DOM methods.  This may not be optimal.
* Evidently, JavaScript is no Python, as [this video](http://www.youtube.com/watch?v=hQVTIJBZook) demonstrates.
* For now, `introspect.close()` won't work for "SHIFT-ENTER" docstrings, because the notebook treats them differently from "TAB" docstrings.  See #5644.
* See #4714 about making jsMath inclusions and tweaks more manageable.



---

archive/issue_comments_047646.json:
```json
{
    "body": "Opera 9 Linux snapshot",
    "created_at": "2009-05-07T01:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47646",
    "user": "https://github.com/qed777"
}
```

Opera 9 Linux snapshot



---

archive/issue_comments_047647.json:
```json
{
    "body": "Attachment [tearout_opera.png](tarball://root/attachments/some-uuid/ticket6001/tearout_opera.png) by @qed777 created at 2009-05-07 01:25:46\n\nFirefox 3 Linux snapshot of \"torn out\" docstrings",
    "created_at": "2009-05-07T01:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47647",
    "user": "https://github.com/qed777"
}
```

Attachment [tearout_opera.png](tarball://root/attachments/some-uuid/ticket6001/tearout_opera.png) by @qed777 created at 2009-05-07 01:25:46

Firefox 3 Linux snapshot of "torn out" docstrings



---

archive/issue_comments_047648.json:
```json
{
    "body": "Attachment [tornout_firefox.png](tarball://root/attachments/some-uuid/ticket6001/tornout_firefox.png) by @qed777 created at 2009-05-07 01:49:55\n\nUnexciting inaction shots:\n\n<img src=\"tearout_opera.png\" width=200px, right>\n<img src=\"tornout_firefox.png\" width=200px, left>\n\nThis ticket could *really* use *your* help.\n\nBy the way, to get rounded [docstring] borders in Firefox 3, put something like\n\n```\ndiv.docstring {\n    -moz-border-radius: 0.5em;\n    -webkit-border-radius: 0.5em;\n}\n```\n\nin `DOT_SAGE/notebook.css` .  I haven't tested this in Safari.",
    "created_at": "2009-05-07T01:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47648",
    "user": "https://github.com/qed777"
}
```

Attachment [tornout_firefox.png](tarball://root/attachments/some-uuid/ticket6001/tornout_firefox.png) by @qed777 created at 2009-05-07 01:49:55

Unexciting inaction shots:

<img src="tearout_opera.png" width=200px, right>
<img src="tornout_firefox.png" width=200px, left>

This ticket could *really* use *your* help.

By the way, to get rounded [docstring] borders in Firefox 3, put something like

```
div.docstring {
    -moz-border-radius: 0.5em;
    -webkit-border-radius: 0.5em;
}
```

in `DOT_SAGE/notebook.css` .  I haven't tested this in Safari.



---

archive/issue_comments_047649.json:
```json
{
    "body": "On a Mac, works well with Firefox but not with Safari.  With Safari, clicking the tear-out button opens up a new blank window and leaves the docstring in the original window.\n\nWith Firefox, looks great, and I like font-resizing and toggling.",
    "created_at": "2009-05-09T02:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47649",
    "user": "https://github.com/jhpalmieri"
}
```

On a Mac, works well with Firefox but not with Safari.  With Safari, clicking the tear-out button opens up a new blank window and leaves the docstring in the original window.

With Firefox, looks great, and I like font-resizing and toggling.



---

archive/issue_comments_047650.json:
```json
{
    "body": "Attachment [introspect_v2.js](tarball://root/attachments/some-uuid/ticket6001/introspect_v2.js) by @qed777 created at 2009-05-19 15:50:53\n\nAttempted support for WebKit browsers.  Replaces v1.",
    "created_at": "2009-05-19T15:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47650",
    "user": "https://github.com/qed777"
}
```

Attachment [introspect_v2.js](tarball://root/attachments/some-uuid/ticket6001/introspect_v2.js) by @qed777 created at 2009-05-19 15:50:53

Attempted support for WebKit browsers.  Replaces v1.



---

archive/issue_comments_047651.json:
```json
{
    "body": "I've tested the new, possibly improved [attachment:introspect_v2.js `introspect.js`] on Fedora 9 Linux in Firefox 3.0.10, Opera 9.64, and a Qt 4.5.0 WebKit-based \"browser\" demo.\n\nI'm not sure about how well the latter, which I found in `/usr/lib64/qt4/demos/browser,` approximates Safari.  It returns\n\n```\n\"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)  demobrowser/0.1\"\n```\n\nwhen I enter `navigator.userAgent` in the JavaScript console (check the \"Tools\" menu or right-click on any element, then click on \"Inspect\").  To get \"tab\" introspection working, I just added `'sl':keyboard_saf` near the end of `keyboards.py.`  Perhaps this is related to ticket #4046.\n\nAnyway, it seems all the browsers have their own way of doing just about everything, and no major UI library handles pop-ups seamlessly across browsers.  We may not (cannot?) get identical behavior on all major browsers.\n\nSome possible tests, besides the obvious:\n\n* Check whether multiple tear-outs from a worksheet go to a common window.\n* Ditto, from multiple worksheets.\n* Ditto, after reloading a worksheet(s).\n* Ditto, after navigating to another domain (e.g., `google.com`) in a tear-out window(s) (see [same origin policy](http://en.wikipedia.org/wiki/Same_origin_policy)).\n* Check the behavior when tear-outs go to an *unsized* window and the browser is set to open tabs vs. set to open windows.\n* Ditto for *sized* windows.\n\nFor the latter, see the `window.open()` lines in `introspect.js.`  In Firefox, I still get a blank tab when I force new windows to open in tabs and use unsized pop-ups.  I have got this to work with a somewhat different approach, but I haven't yet reconciled it with what's in v2.\n\nDrag-and-drop sometimes behaves oddly in Firefox, adding copious spurious placeholders to the list.  I've noticed this after I navigate to a different domain in a tear-out window, forcing the script to open a new window.  I think this is a jQuery [UI] bug, since it goes away when I substitute the latest versions.  This and other quirks may be a good reason to upgrade both.  Worst case: Disable some tear-out features for certain browsers.\n\nSome ideas, though my patience with browser \"programming\" has all but vanished:\n\n* Do something server-side instead or in addition.\n* Add a top-level toolbar to the tear-out window, e.g., to toggle, close, resize all docstrings.\n* Add a simple \"cell\" input that calls `window.opener.evaluate_cell_inspection().`\n* Cookies, preferably chocolate.\n\nSome ideas related to #5653:\n\n* Collect anonymous statistics on docstring access: compute correlations, do Bayesian predictions, rank the greatest (and worst) docstring writers of ***all time***.\n* Generate a large graph of all docstrings and their cross-links.  Drive the graph theorists wild.  Actually, I think it's rather sparse at the moment.  Not an [expander](http://en.wikipedia.org/wiki/Expander_graph)?\n* Upgrade Sphinx and test the Qt help builder, though it may [need work](http://groups.google.com/group/sphinx-dev/browse_thread/thread/64dd226d9b4cec36/6fa3e0d251dae768#6fa3e0d251dae768).  Try running Qt's `assistant` (`assistant-qt4` on Fedora 9) for a taste.\n* Add \"PDF\" to the toolbar, with maybe a rude surprise for PDF plug-in users.\n* One-click copy-pasting of examples for the truly lazy.",
    "created_at": "2009-05-19T17:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47651",
    "user": "https://github.com/qed777"
}
```

I've tested the new, possibly improved [attachment:introspect_v2.js `introspect.js`] on Fedora 9 Linux in Firefox 3.0.10, Opera 9.64, and a Qt 4.5.0 WebKit-based "browser" demo.

I'm not sure about how well the latter, which I found in `/usr/lib64/qt4/demos/browser,` approximates Safari.  It returns

```
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)  demobrowser/0.1"
```

when I enter `navigator.userAgent` in the JavaScript console (check the "Tools" menu or right-click on any element, then click on "Inspect").  To get "tab" introspection working, I just added `'sl':keyboard_saf` near the end of `keyboards.py.`  Perhaps this is related to ticket #4046.

Anyway, it seems all the browsers have their own way of doing just about everything, and no major UI library handles pop-ups seamlessly across browsers.  We may not (cannot?) get identical behavior on all major browsers.

Some possible tests, besides the obvious:

* Check whether multiple tear-outs from a worksheet go to a common window.
* Ditto, from multiple worksheets.
* Ditto, after reloading a worksheet(s).
* Ditto, after navigating to another domain (e.g., `google.com`) in a tear-out window(s) (see [same origin policy](http://en.wikipedia.org/wiki/Same_origin_policy)).
* Check the behavior when tear-outs go to an *unsized* window and the browser is set to open tabs vs. set to open windows.
* Ditto for *sized* windows.

For the latter, see the `window.open()` lines in `introspect.js.`  In Firefox, I still get a blank tab when I force new windows to open in tabs and use unsized pop-ups.  I have got this to work with a somewhat different approach, but I haven't yet reconciled it with what's in v2.

Drag-and-drop sometimes behaves oddly in Firefox, adding copious spurious placeholders to the list.  I've noticed this after I navigate to a different domain in a tear-out window, forcing the script to open a new window.  I think this is a jQuery [UI] bug, since it goes away when I substitute the latest versions.  This and other quirks may be a good reason to upgrade both.  Worst case: Disable some tear-out features for certain browsers.

Some ideas, though my patience with browser "programming" has all but vanished:

* Do something server-side instead or in addition.
* Add a top-level toolbar to the tear-out window, e.g., to toggle, close, resize all docstrings.
* Add a simple "cell" input that calls `window.opener.evaluate_cell_inspection().`
* Cookies, preferably chocolate.

Some ideas related to #5653:

* Collect anonymous statistics on docstring access: compute correlations, do Bayesian predictions, rank the greatest (and worst) docstring writers of ***all time***.
* Generate a large graph of all docstrings and their cross-links.  Drive the graph theorists wild.  Actually, I think it's rather sparse at the moment.  Not an [expander](http://en.wikipedia.org/wiki/Expander_graph)?
* Upgrade Sphinx and test the Qt help builder, though it may [need work](http://groups.google.com/group/sphinx-dev/browse_thread/thread/64dd226d9b4cec36/6fa3e0d251dae768#6fa3e0d251dae768).  Try running Qt's `assistant` (`assistant-qt4` on Fedora 9) for a taste.
* Add "PDF" to the toolbar, with maybe a rude surprise for PDF plug-in users.
* One-click copy-pasting of examples for the truly lazy.



---

archive/issue_comments_047652.json:
```json
{
    "body": "Attachment [introspect_v3.js](tarball://root/attachments/some-uuid/ticket6001/introspect_v3.js) by @qed777 created at 2009-05-28 04:02:06\n\nGoes with layout_v3.html.",
    "created_at": "2009-05-28T04:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47652",
    "user": "https://github.com/qed777"
}
```

Attachment [introspect_v3.js](tarball://root/attachments/some-uuid/ticket6001/introspect_v3.js) by @qed777 created at 2009-05-28 04:02:06

Goes with layout_v3.html.



---

archive/issue_comments_047653.json:
```json
{
    "body": "Attachment [layout_v3.html](tarball://root/attachments/some-uuid/ticket6001/layout_v3.html) by @qed777 created at 2009-05-28 04:02:28\n\nGoes with introspect_v3.js.",
    "created_at": "2009-05-28T04:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47653",
    "user": "https://github.com/qed777"
}
```

Attachment [layout_v3.html](tarball://root/attachments/some-uuid/ticket6001/layout_v3.html) by @qed777 created at 2009-05-28 04:02:28

Goes with introspect_v3.js.



---

archive/issue_comments_047654.json:
```json
{
    "body": "Version 3 is up.  Please see the code and comments for details.  In particular, see the new `layout.html` for alternative Unicode \"icons.\"  Perhaps we can use jsMath, here, too.  Anyway, suggestions are welcome.  Note:  I thought up/down arrows for font-sizing might be [more] confusing.  Perhaps someday we can add left/right arrows for browsing consecutive docstrings in a module.\n\nI've tested this, though not exhaustively, in Opera 9, Firefox 3, and the Qt 4.5 demo browser on Linux, as well as IE 8, Opera 9, Firefox 3, Safari 3, and Chrome 2 on Windows XP.",
    "created_at": "2009-05-28T04:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47654",
    "user": "https://github.com/qed777"
}
```

Version 3 is up.  Please see the code and comments for details.  In particular, see the new `layout.html` for alternative Unicode "icons."  Perhaps we can use jsMath, here, too.  Anyway, suggestions are welcome.  Note:  I thought up/down arrows for font-sizing might be [more] confusing.  Perhaps someday we can add left/right arrows for browsing consecutive docstrings in a module.

I've tested this, though not exhaustively, in Opera 9, Firefox 3, and the Qt 4.5 demo browser on Linux, as well as IE 8, Opera 9, Firefox 3, Safari 3, and Chrome 2 on Windows XP.



---

archive/issue_comments_047655.json:
```json
{
    "body": "Goes with layout_v4.html.",
    "created_at": "2009-06-04T09:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47655",
    "user": "https://github.com/qed777"
}
```

Goes with layout_v4.html.



---

archive/issue_comments_047656.json:
```json
{
    "body": "Attachment [layout_v4.html](tarball://root/attachments/some-uuid/ticket6001/layout_v4.html) by @qed777 created at 2009-06-04 09:46:24\n\nGoes with introspect_v4.js.",
    "created_at": "2009-06-04T09:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47656",
    "user": "https://github.com/qed777"
}
```

Attachment [layout_v4.html](tarball://root/attachments/some-uuid/ticket6001/layout_v4.html) by @qed777 created at 2009-06-04 09:46:24

Goes with introspect_v4.js.



---

archive/issue_comments_047657.json:
```json
{
    "body": "Version 4 is available.  New features: multiple columns, height limits.  Tested on Linux in Opera 9 and Firefox 3.  Note: Drag-and-drop in the latter is still problematic, but a jQuery/UI upgrade will fix this.  To do:\n* Add a function to \"balance\" or \"equalize\" columns, either by the number of docstrings or, perhaps, instantaneous total height.\n* Query sage-devel for volunteers to design nice icons?\n* Test on Mac OS X, though I can't do this myself.\n* Re-test on Windows.\n\nBy the way, running\n\n```\nhtml('<script>introspect.test1(10)</script>')\n```\n\nin a cell should open 10 docstrings selected not quite at random.  Alternatively, evaluate `introspect.test1(10)` in [Firebug's](http://getfirebug.com/) console.  See the code for details.",
    "created_at": "2009-06-04T10:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47657",
    "user": "https://github.com/qed777"
}
```

Version 4 is available.  New features: multiple columns, height limits.  Tested on Linux in Opera 9 and Firefox 3.  Note: Drag-and-drop in the latter is still problematic, but a jQuery/UI upgrade will fix this.  To do:
* Add a function to "balance" or "equalize" columns, either by the number of docstrings or, perhaps, instantaneous total height.
* Query sage-devel for volunteers to design nice icons?
* Test on Mac OS X, though I can't do this myself.
* Re-test on Windows.

By the way, running

```
html('<script>introspect.test1(10)</script>')
```

in a cell should open 10 docstrings selected not quite at random.  Alternatively, evaluate `introspect.test1(10)` in [Firebug's](http://getfirebug.com/) console.  See the code for details.



---

archive/issue_comments_047658.json:
```json
{
    "body": "See [sage-devel](http://groups.google.com/group/sage-devel/msg/89996604f6cd9c6f) for thoughts about something almost completely different.  See [also](http://www.smartclient.com/docs/7.0rc2/a/b/c/go.html#search%3Dpython).",
    "created_at": "2009-09-23T00:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47658",
    "user": "https://github.com/qed777"
}
```

See [sage-devel](http://groups.google.com/group/sage-devel/msg/89996604f6cd9c6f) for thoughts about something almost completely different.  See [also](http://www.smartclient.com/docs/7.0rc2/a/b/c/go.html#search%3Dpython).



---

archive/issue_comments_047659.json:
```json
{
    "body": "I think this has been fixed by one of the recent patches (~January). Close?",
    "created_at": "2010-04-21T20:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47659",
    "user": "https://github.com/TimDumol"
}
```

I think this has been fixed by one of the recent patches (~January). Close?



---

archive/issue_comments_047660.json:
```json
{
    "body": "This ticket was originally about [optionally] tearing out documentation into an independent browser tab/window, where one could browse and collect docstrings and source code separately from a worksheet(s).  I'd like to keep the ticket open, for now, to pursue a more general Sage documentation browser, about which I've speculated [here](http://groups.google.com/group/sage-devel/msg/89996604f6cd9c6f).  [Miller Columns](http://en.wikipedia.org/wiki/Miller_Columns) still seem promising, and we could adapt an existing JavaScript widget.  I'll need to do another survey to get an update list of candidates.",
    "created_at": "2010-06-10T07:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47660",
    "user": "https://github.com/qed777"
}
```

This ticket was originally about [optionally] tearing out documentation into an independent browser tab/window, where one could browse and collect docstrings and source code separately from a worksheet(s).  I'd like to keep the ticket open, for now, to pursue a more general Sage documentation browser, about which I've speculated [here](http://groups.google.com/group/sage-devel/msg/89996604f6cd9c6f).  [Miller Columns](http://en.wikipedia.org/wiki/Miller_Columns) still seem promising, and we could adapt an existing JavaScript widget.  I'll need to do another survey to get an update list of candidates.



---

archive/issue_comments_047661.json:
```json
{
    "body": "The original thing mentioned has long since been done, as pointed out, and the other piece is just far too vague to merit a specific ticket.  After five years, probably time to close.",
    "created_at": "2014-12-19T04:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47661",
    "user": "https://github.com/kcrisman"
}
```

The original thing mentioned has long since been done, as pointed out, and the other piece is just far too vague to merit a specific ticket.  After five years, probably time to close.



---

archive/issue_comments_047662.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-12-19T04:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47662",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_006254.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-01-13T01:18:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6001#event-6254"
}
```



---

archive/issue_comments_047663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-13T01:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6001#issuecomment-47663",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
