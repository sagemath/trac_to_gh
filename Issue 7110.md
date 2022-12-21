# Issue 7110: [with patch, needs review] SageNB -- Port #4046, #6459, #6694, #6865, #6939

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-10-04 13:52:04

Assignee: boothby

CC:  timdumol was jason mhampton kcrisman mvngu

Keywords: sagenb notebook

Primary authors and reviewers are at listed at

 * #4046
 * #6459
 * #6694
 * #6865
 * #6939

See #6983 for instructions on getting sagenb.


---

Attachment

Port/merge/base #4046, #6459, #6694, #6865, #6939 for sagenb.


---

Comment by mpatel created at 2009-10-04 15:40:33

Apart from rebasing existing patches, I've rearranged some files:

 * Moved `sagenb/data/templates/*_lib.js` to `sagenb/data/javascript/sage/*.js`.
 * Moved TinyMCE initialization code to `sagenb/data/javascript/sage/tinymce.js`.
 * Updated affected HTML templates.
 * On `notebook_lib.js`'s template macros:
   * `SAGE_URL`: "Replaced" with [this URL](http://www.math.union.edu/~dpvc/jsMath/users/welcome.html) for now.  The [existing link](http://sage.math.washington.edu/sage/jsmath) is broken.
   * `KEY_CODES`: "Moved," in `twist.py`, to `javascript/sage/keys.js`.  They're still generated dynamically.

However:

 * `notebook.js` and friends are now static, so they're not sent through `compress.JavaScriptCompressor`.  It may be much better to use the [YUI compressor](http://developer.yahoo.com/yui/compressor/).
 * There are two versions of `sage3d.js`.  Can we move one or both (after renaming) to `javascript/sage3d` or `javascript/sage/`?
 * jsMath initialization is not yet in `javascript/sage/jsmath.js`.  I'll do this at #4714.
 * A rebased jQuery / UI upgrade (cf. #5447) will move `farbtastic` to `jquery/plugins`.
 * Do we use `zorn`?
 * Perhaps we should organize `data/` differently.  By package?  Examples: `highlight` and `sage`, templates and images included.


---

Attachment

v2: converted missed "main.js" in notebook.py.  Apply only this patch.


---

Comment by mpatel created at 2009-10-04 17:30:49

Patch v2 takes care of `"main.js"` in `notebook.list_javascript_window()`, although this function is currently unused, it seems.


---

Comment by mpatel created at 2009-10-04 19:47:11

For #5447, here are the SageNB patches:

 * http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_A.patch
 * http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_B.patch
 * http://sage.math.washington.edu/home/mpatel/trac/7110/trac_5447-sagenb_jquery_upgrade_part_C.patch

Please apply all three patches in lexicographical order *_after*_ the [attachment:trac_7110-sagenb_ports_v2.patch patch above].


---

Attachment

Minimal rebase of #4046, #6694, #6865, #6939 for SageNB.  Apply only this patch.


---

Comment by mpatel created at 2009-10-11 13:43:19

The latest patch is just a minimal rebase of #4046, #6694, #6865, and #6939 for SageNB.


---

Comment by was created at 2009-10-11 19:27:11

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-10-11 19:27:44

Resolution: fixed


---

Comment by was created at 2009-10-11 19:27:44

I merged this into the official sagenb repo and pushed it.  And it works very nicely!
