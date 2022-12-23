# Issue 4714: use easy/load.js when loading jsmath

Issue created by migration from https://trac.sagemath.org/ticket/4714

Original creator: jason

Original creation time: 2008-12-05 10:10:42

Assignee: boothby

CC:  jhpalmieri timdumol was

From http://groups.google.com/group/sage-support/t/178d0bd277044918


```
Yes, that looks correct.  I'm not sure why people are getting the 
error -7 under these conditions.  It means that something has gone 
wrong when trying to load the fallback method, and that usually means 
it can't read the image font definition files.  There are a couple of 
other possibilities as well:  perhaps the noImageFonts plugin was not 
able to be read (permission issue?) or the unicode fallback file could 
not be read.  Given your use of noImageFonts, I suspect it may be the 
latter.  If the users who are getting error -7 are using Firefox3, 
that may well be it.  There were changes to the same-origin security 
policy in Firefox3 that prevent jsMath from loading local files from 
directories other than the one in which the HTML file is found.  I 
worked around this in jsMath v3.6 (released Sept. 2008), so those 
users should update to the latest version of jsMath to avoid that 
problem. 
> I'm pretty sure we don't use the easy/load.js (and I'm not sure why). 

Probably because it didn't exist when jsMath support was added to 
sage.  The easy/load.js file was a relatively late addition to jsMath, 
but certainly makes things easier for people.  You might consider 
whether you want to use that instead. 

Davide


---

Comment by mpatel created at 2009-05-07 00:26:52

Copied from [comment:ticket:5653:27 jason]:
> Replying to [comment:ticket:5653:24 mpatel]:
> 
> > A related issue:  It would be nice to have just one `<script>` element load jsMath with all of Sage's customizations (extensions, plug-ins, macros, etc.) into regular, published, printed, and docbrowser worksheets, as well as "torn out" introspection windows and offline documentation.  Maybe `easy/load.js` is the right place (see #4714),
> > but I think notebook.py generates the macro list on-the-fly.
> 
> Davide (author of jsmath) sent these comments about the above paragraph:
> 
> Mpatel is right that jsMath/easy/load.js could be used for this.  Rather than putting calls to jsMath.Setup.Script() or jsMath.Extention.Require() in-line in the document itself, these can be be put in the loadFiles array in easy/load.js.  It is also possible to put the jsMath.Macro() calls into a file (say jsMath/local/sage.js), and add that file to the loadFiles array as well rather than put them in-line.  Any sage-specific customization could go in local/sage.js as well.  In the latest version of jsMath, there is even a macros array in easy/load.js for custom macros, so you would not even need an extra file for that.  These features are, in fact, one of the important reasons for easy/load.js, so I hope you are able to take advantage of them.


---

Comment by mpatel created at 2009-06-18 07:51:22

A few *estions:

 * Should we patch the spkg's `jsmath/easy/load.js`?
 * Add `jsmath/local/sage.js` to its `loadFiles` array?
 * Re-generate this `sage.js` from the list in `sage/misc/latex_macros.py` during
   1. `sage -docbuild`, in `doc/common/conf.py`?  
   2. `sage -b`?
   3. notebook startup?


---

Comment by davidloeffler created at 2009-07-13 16:09:02

This is misfiled (should be under "documentation").


---

Comment by davidloeffler created at 2009-07-13 16:09:02

Changing component from notebook to documentation.


---

Comment by davidloeffler created at 2009-07-13 16:09:02

Changing assignee from boothby to tba.


---

Comment by mpatel created at 2009-07-17 10:13:42

After #5799, we have two copies of the `jsmath` tree, one in `doc/common/static` and another in `javascript_local`.  That is, one from `sage-4.1.spkg` and another from `jsmath-3.6b.p1.spkg`.  Can we avoid this?  Or should we maintain separate `load.js` files for the notebook and documentation?


---

Comment by mpatel created at 2009-08-02 21:32:21

Replying to [comment:5 mpatel]:
> After #5799, we have two copies of the `jsmath` tree, one in `doc/common/static` and another in `javascript_local`.  That is, one from `sage-4.1.spkg` and another from `jsmath-3.6b.p1.spkg`.  Can we avoid this?  Or should we maintain separate `load.js` files for the notebook and documentation?
See #6614 for a potential resolution.


---

Comment by mpatel created at 2009-08-02 22:27:47

The latest patch at #6614 tells Sphinx to copy jsMath directly from `javascript_local` to `doc/output/html/en/*/_static`.  In particular, it does this _before_ it copies the files in `doc/common/static`.  How about putting a custom `easy/load.js` there?

If we're not adding new doc macros frequently, we could just paste them from `latex_macros.py`.  Or we might add an option to `sage -docbuild` to regenerate `load.js` on demand (cf. #6187).  If we overwrite the file during _every_ build, we may need to synchronize access from multiple Sphinx processes (cf. #6255).

(Note: Sphinx 0.6.2 supports HTML themes, including [static templates](http://sphinx.pocoo.org/theming.html#static-templates).  It's tempting to create a template `static/easy/load.js_t`.  However, Sphinx does not process user templates in `static`'s _subdirectories_.)

On the notebook:  I believe we can move nearly all jsMath directives from `notebook.py` to a custom `javascript_local/jsmath/easy/load.js` that's overwritten on notebook start-up.  Perhaps in `twist.py`?

I'd really like to get moving on this, provided there's agreement.  Of course, we can split this into two tickets, [at least] one each for the docs and notebook.  Thoughts?


---

Comment by mpatel created at 2009-08-04 04:13:04

Minimal approach for docs.  Depends on #6614.


---

Attachment

This [attachment:trac_4714-minimal_doc.patch p(r)oof of concept], which depends on a [attachment:ticket:6614:trac_6614-jsmath_repo_v2.patch patch] at #6614,

 * Adds `doc/common/static/jsmath_sage.js`.
 * Sets `jsmath_path=jsmath_sage.js` in `doc/common/conf.py`.

The new static file is jsMath's "stock" `easy/load.js` plus all Sage-related customizations I could find, including extensions, macros, and a few other bits from `notebook.py`.  I've also made changes below `DO NOT MAKE CHANGES BELOW THIS` (gasp!) to help the loader find jsMath from its new [relative] location.

I think this means we don't need to patch the spkg.  Later, we may be able to use Sphinx 0.6.2's static templates to insert an updated macro list at build time (cf. #6586).

Perhaps we can do something similar for the notebook, e.g., in `sage/server/notebook/templates`.


---

Comment by mpatel created at 2009-08-04 07:07:56

With major changes in afoot in the notebook at #6568, I've put the doc patch up for review at #6673 and made this ticket specific to the notebook.


---

Comment by mpatel created at 2009-08-04 07:07:56

Changing component from documentation to notebook.


---

Comment by mpatel created at 2009-08-04 07:07:56

Changing assignee from tba to boothby.


---

Comment by mpatel created at 2009-10-16 07:38:55

See [comment:ticket:6673:10 this comment] (and the next one) at #6673 for a suggested path to "unification."


---

Comment by mpatel created at 2009-10-21 19:26:01

In `sagenb.notebook.twist`, we can use a cached `sage.misc.latex_macros.sage_jsmath_macros_easy` (cf. #6673's [attachment:trac_6673-jsmath_macros_docs_v3.patch:ticket:6673 v3]) and `JSMATH_IMAGE_FONTS`, plus a user's own macros, to serve a dynamic `javascript/jsmath.js`.


---

Comment by mpatel created at 2009-10-23 07:02:17

Consolidate jsMath setup.  Apply to sagenb repository.  Apply only this patch.


---

Comment by mpatel created at 2009-10-23 07:10:01

Changing status from new to needs_review.


---

Attachment

The patch [attachment:trac_4714-sagenb_jsmath_init.patch] consolidates jsMath setup in `/javascript/jsmath.js`.  It depends on #6673.

The patch still hard-codes the `sage.misc.latex_macros`'s macros.  Still to do: Generate the macros from server/user settings and `latex_macros`'s helper functions.


---

Comment by mpatel created at 2009-10-24 18:45:46

Hard-code jsMath macros.  Apply to sagenb repository.


---

Attachment

I've reattached [attachment:trac_4714-sagenb_hard_code_macros.patch], since my first try didn't work (server problems?).


---

Comment by mpatel created at 2009-10-24 19:09:46

Note: With Jinja2 (cf. #7269, #7249), we can instead use, e.g.,

```js
    macros: {
       {{ jsmath_macros|join(',\n') }}
    },
```

in `jsmath.js` (cf. #6673).


---

Comment by was created at 2009-10-25 02:22:51

This works: trac_4714-sagenb_hard_code_macros.patc


---

Comment by mpatel created at 2009-10-25 09:42:10

Reminder: Rebase vs. #7269.


---

Comment by mpatel created at 2009-11-26 05:53:18

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2009-11-26 06:33:08

Rebased.  See the comment for the queue.  Apply only this patch.  sagenb repo.


---

Comment by mpatel created at 2009-11-26 06:33:37

Changing status from needs_work to needs_review.


---

Attachment

Rebased against this sequence:

```
trac_7390-sagenb_test_report_A.patch
trac_7390-sagenb_test_report_B_v2.patch
trac_7390-sagenb_test_report_referee.patch
trac_7402-pkg_resources.patch
trac_7428-publish_last_edited_v2.patch
trac_7444-search_after_publish.patch
trac_7376-search_by_username_v2.patch
trac_1321-sagenb_graphed.patch
sagenb_7483.patch
sagenb_7482.patch
sagenb-7495.patch
sagenb_3849.patch
trac_4714-sagenb_jsmath_init_v2.patch
```



---

Comment by mpatel created at 2009-11-26 06:38:34

Changing priority from major to minor.


---

Attachment

Force jsMath to load always.  This patch only.  sagenb repo.


---

Comment by mpatel created at 2009-12-02 23:41:46

Version 3:

 * Disables jsMath's autoload plug-in.  Otherwise, jsMath does not load itself and run in worksheets that _initially_ do not contain expressions to typeset.


---

Comment by was created at 2009-12-08 23:25:49

Looks good to me.


---

Comment by was created at 2009-12-08 23:25:49

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 01:12:41

I merged this patch into sagenb-0.4.6.


---

Comment by was created at 2009-12-09 01:12:41

Resolution: fixed
