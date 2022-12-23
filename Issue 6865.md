# Issue 6865: Use templates for CSS

Issue created by migration from https://trac.sagemath.org/ticket/6865

Original creator: timdumol

Original creation time: 2009-09-02 15:30:45

Assignee: boothby

Keywords: notebook css stylesheets

CSS is currently served by `css()` in `css.py`, even though it is completely static. Using templates for it should make things easier to customize in the future.


---

Comment by timdumol created at 2009-09-02 16:10:08

Moved CSS in `css.py` to templates, and adjusted `twist.py` to use them.


---

Attachment


---

Comment by jason created at 2009-09-17 19:21:51

This probably needs to be rebased after #6939 to include the CSS fix there (or the rebasing should go the other way, if this gets reviewed before that gets merged...)


---

Comment by jason created at 2009-09-17 19:25:56

#6940 is a dup of this ticket (i.e., close #6940).


---

Comment by mpatel created at 2009-09-17 22:14:07

Does the patch depend on another ticket's patch?  Applying [attachment:trac_6865-templates-css.patch] to 4.1.2.alpha1, I get

```
applying trac_6865-templates-css.patch
patching file sage/server/notebook/css.py
Hunk #1 FAILED at 0
1 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/css.py.rej
patching file sage/server/notebook/twist.py
Hunk #1 FAILED at 133
Hunk #2 succeeded at 1787 with fuzz 1 (offset 37 lines).
Hunk #3 FAILED at 2315
2 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/twist.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6865-templates-css.patch
```

The important one is the last, which doesn't apply because the local `twist.py` contains

```python
        elif self.problem == 'suspended':
            return HTMLResponse(stream = message("Your account is currently suspended."))
```

But I could have altered my configuration.


---

Comment by mpatel created at 2009-09-18 02:20:55

I think we need to add

```
include sage/server/notebook/css/*
```

to `MANIFEST.in,` or we'll definitely hear from the release manager...


---

Comment by jason created at 2009-09-19 02:48:37

What is MANIFEST.in and when do we need to add things to it?


---

Comment by jason created at 2009-09-19 02:49:16

(setting to "needs work", based on mpatel's comment about MANIFEST.in and his comment about applying the patch)


---

Comment by mpatel created at 2009-09-19 05:11:44

Replying to [comment:6 jason]:
> What is MANIFEST.in and when do we need to add things to it?
I believe the `sage -bdist` and `sage -sdist` invoke [distutils](http://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute) to build `sage-*.spkg`.  Distutils uses `SAGE_ROOT/devel/sage/MANIFEST.in` to determine which files to include in the distribution.  If we add files to the local Mercurial repository, we should check that some line(s) in `MANIFEST.in` includes the newly tracked files or add a new line.  Otherwise, the next (pre-)release of Sage will not include them.  As mvngu puts it, this results in ["repository corruption"](http://groups.google.com/group/sage-devel/browse_thread/thread/697693c77e8d7ee8/290f2ec5412b909d?q=repository+corruption+group:sage-devel#290f2ec5412b909d).

Previous sightings: #4460, #5653, #5799, #6568, etc.


---

Comment by timdumol created at 2009-09-20 03:52:52

No, this doesn't depend on other patches. It is based on 4.1.2.alpha1.

I've made the requisite changes to `MANIFEST.in`.


---

Comment by timdumol created at 2009-09-20 03:56:12

Moved CSS in css.py to templates, and adjusted twist.py to use them. Rev 2. Apply this patch only.


---

Attachment

Moved CSS in css.py to templates, and adjusted twist.py to use them. Rev 3. Apply this patch only.


---

Comment by mpatel created at 2009-09-21 00:40:12

Changes in patch v3:

 * `css.py`: `if os.path.exists(user_css):` --> `if os.path.exists(user_css_path):`
 * `css.py`: `+` --> `os.path.join()`
 * `css.py`: html -> HTML in docstring
 * `main.css`: {% ->  {%-

Sorry about the trivial stuff.  I just noticed the [whitespace control](http://jinja.pocoo.org/2/documentation/templates#whitespace-control) part of the Jinja2 docs.

This is a positive review from me, but someone should review my changes.


---

Comment by jason created at 2009-09-22 17:33:17

Your changes look good to me.


---

Comment by jason created at 2009-09-22 17:33:31

Changing priority from minor to major.


---

Comment by mvngu created at 2009-09-22 17:55:59

Resolution: fixed


---

Comment by mvngu created at 2009-09-22 17:55:59

Merged `trac_6865-templates-css.3.patch`.


---

Comment by mvngu created at 2009-09-27 09:25:35

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
