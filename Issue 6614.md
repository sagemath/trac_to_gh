# Issue 6614: Remove jsMath from version control in the Sage library.

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-07-24 14:50:30

Assignee: tbd

CC:  rlm

After the merge of #5799, we have jsMath installed in two places: `$SAGE_ROOT/local/notebook/javascript` *and* `$SAGE_DOC/common/static`.  Moreover, all of jsMath is under version control in the Sage library.  However, the standard practice for Sage development is to keep most upstream spkg code out of Mercurial's reach.

In particular, we'll need to do unnecessary extra work when we upgrade to new upstream versions of jsMath or keep track of local customizations (cf. #4714).



---

Comment by mpatel created at 2009-07-24 15:27:39

Changing assignee from tbd to tba.


---

Attachment

This [attachment:trac_6614-distutils_symlinks.patch patch] alters `setup.py` so that distutils includes broken symbolic links as it builds a source distribution of the Sage library.  Is this appropriate?

If so, I can add another patch that replaces the `jsmath` directory in `$SAGE_DOC/common/static` with a symlink and updates the repository accordingly (i.e., reverses the patch mentioned [here](http://trac.sagemath.org/sage_trac/ticket/5799#comment:11)).

One caveat is that Python's [os](http://docs.python.org/library/os.html) module supports symbolic links only on Unix systems.  If we need to avoid links altogether, we could instead copy jsMath to multiple locations from its own `spkg-install` script.


---

Comment by mpatel created at 2009-07-24 15:27:39

Changing priority from major to minor.


---

Comment by mpatel created at 2009-07-24 15:27:39

Changing component from algebra to documentation.


---

Comment by jhpalmieri created at 2009-07-24 17:39:05

Should we add the jsmath directory to devel/sage/.hgignore?


---

Attachment

Different approach.


---

Comment by mpatel created at 2009-07-25 12:55:27

This [attachment:trac_6614-jsmath_repo.patch alternative patch] deletes `doc/common/static/jsmath` and adds jsMath to `doc/common/conf.py`'s list of `html_static_path`s.

Since Sphinx recursively copies the only the contents of the static paths, jsMath no longer gets its own directory in `_static`.  I've changed `jsmath_path` to `'easy/load.js'`.

If we take this approach, then I should update the "`new_scripts`" patch at #6187.


---

Comment by mpatel created at 2009-08-02 18:53:31

New version that puts jsMath path first.


---

Attachment

The new version _prepends_ jsMath's path to `html_static_path`, so that custom files copied subsequently from, e.g., `doc/common/static`,  can override certain settings, at our option.

The same caveats apply.


---

Comment by mpatel created at 2009-08-02 19:18:14

An aside on Firefox's security policy:

 * Build the reference manual with `--jsmath`.
 * Browse to the table of contents in FF 3.5.
 * Open "The Steenrod algebra", say, in a new background tab by middle-clicking (or the equivalent).
 * Switch to the new tab.  Did jsMath process the page?  Not for me.
 * Switch back to the ToC tab and browse directly to the same topic.  Did jsMath process the page?  Yes for me.

I've tested this only on Linux.  Opera and Chromium don't behave this way, so I don't think it's [entirely] jsMath's fault.

In any case, this happens whether or not I apply the patch above.


---

Comment by mpatel created at 2009-08-03 18:40:02

Replying to [comment:3 mpatel]:
> This [attachment:trac_6614-jsmath_repo.patch alternative patch] deletes `doc/common/static/jsmath` and adds jsMath to `doc/common/conf.py`'s list of `html_static_path`s.
It may be necessary to delete `doc/common/static/jsmath` manually, after applying the patch.


---

Comment by jhpalmieri created at 2009-08-20 21:21:21

Replying to [comment:3 mpatel]:
> Since Sphinx recursively copies the only the contents of the static paths, jsMath no longer gets its own directory in `_static`.  I've changed `jsmath_path` to `'easy/load.js'`.

Also, since the jsMath files all begin with "jsMath", we don't have to worry about name clashes (except, I suppose, the names of the subdirectories of jsMath, but I hope this won't be an issue).

Anyway, it looks good to me.  I did manually delete `doc/common/static/jsmath`, and the documentation build correctly, with or without the "--jsmath" switch, and jsMath was active when reading docs off-line and on.  The patch is large, but almost all of it consists of deleting files in `doc/common/static/jsmath`; the only "interesting" part is at the very beginning, the changes to `conf.py`.  The changes there look good, both the new stuff and tidying up the old stuff (using `os.path.join` instead of "+", for example).

I hope I'm not missing anything, but I think it gets a positive review.  Apply only [trac_6614-jsmath_repo_v2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6614/trac_6614-jsmath_repo_v2.patch).


---

Comment by mpatel created at 2009-08-22 13:17:52

I left alone the following line in `MANIFEST.in`

```
recursive-include doc/common/static *
```

I assume this is OK, although it's somewhat more than we need just now.


---

Comment by jhpalmieri created at 2009-08-22 14:47:34

Yes, I noticed that and decided it was okay to leave it.


---

Comment by mvngu created at 2009-08-30 06:35:53

Resolution: fixed


---

Comment by mvngu created at 2009-08-30 06:35:53

For Sage 4.1.1 with `trac_6614-jsmath_repo_v2.patch`, reference manual built with `./sage -docbuild --jsmath reference html`:

 * jsMath can't handle Sage's customized LaTeX macros for common rings such such `\RR` for the reals, `\ZZ` for the integers, `\QQ` for the rationals, `\CC` for complex numbers, and `\GF(p)` for the finite field of `p` elements. See this screenshot.
 
 * At least with Firefox 3.5.2, jsMath doesn't render LaTeX-typeset maths expressions very well. See this screenshot.

These two issues are not specific to the patch. The same things happen without `trac_6614-jsmath_repo_v2.patch` being applied to Sage 4.1.1.



Merged only `trac_6614-jsmath_repo_v2.patch`.


---

Comment by mvngu created at 2009-08-30 06:40:18

I also manually deleted the directory `doc/common/static/jsmath`.


---

Comment by mpatel created at 2009-08-30 07:47:31

We're working on Sage-specific jsMath customizations for the documentation at #6673.  

The screenshots appear to be missing, at least for me.

From the [changelog](http://www.math.union.edu/~dpvc/jsMath/changes.html) for jsMath 3.6c:

```
* Worked around another problem with Firefox 3.5's single-origin policy for
  local files that would cause jsMath not to be able to load external
  components.
```

This may address the "aside" above, unless it's besides the aside's point.


---

Comment by mvngu created at 2009-08-30 08:05:21

I forgot to add links to the screenshots. See [this](http://sage.math.washington.edu/home/mvngu/patch/screenshots/sage-4.1.1-with-trac-6614-custom-latex.png) for the customized LaTeX macros, and [this](http://sage.math.washington.edu/home/mvngu/patch/screenshots/sage-4.1.1-with-trac-6614-jsmath.png) for jsMath issues with Firefox 3.5.2.


---

Comment by mpatel created at 2009-08-30 09:00:18

#6673 should help with the macros, but please let us know if we've missed any.

On the other problem: If Firefox is running on Linux, are the [updated fonts](http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html) installed?
