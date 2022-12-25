# Issue 6614: Remove jsMath from version control in the Sage library.

archive/issues_006614.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @rlmill\n\nAfter the merge of #5799, we have jsMath installed in two places: `$SAGE_ROOT/local/notebook/javascript` **and** `$SAGE_DOC/common/static`.  Moreover, all of jsMath is under version control in the Sage library.  However, the standard practice for Sage development is to keep most upstream spkg code out of Mercurial's reach.\n\nIn particular, we'll need to do unnecessary extra work when we upgrade to new upstream versions of jsMath or keep track of local customizations (cf. #4714).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6614\n\n",
    "created_at": "2009-07-24T14:50:30Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Remove jsMath from version control in the Sage library.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6614",
    "user": "https://github.com/qed777"
}
```
Assignee: tbd

CC:  @rlmill

After the merge of #5799, we have jsMath installed in two places: `$SAGE_ROOT/local/notebook/javascript` **and** `$SAGE_DOC/common/static`.  Moreover, all of jsMath is under version control in the Sage library.  However, the standard practice for Sage development is to keep most upstream spkg code out of Mercurial's reach.

In particular, we'll need to do unnecessary extra work when we upgrade to new upstream versions of jsMath or keep track of local customizations (cf. #4714).


Issue created by migration from https://trac.sagemath.org/ticket/6614





---

archive/issue_comments_054040.json:
```json
{
    "body": "Changing assignee from tbd to tba.",
    "created_at": "2009-07-24T15:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54040",
    "user": "https://github.com/qed777"
}
```

Changing assignee from tbd to tba.



---

archive/issue_comments_054041.json:
```json
{
    "body": "Attachment [trac_6614-distutils_symlinks.patch](tarball://root/attachments/some-uuid/ticket6614/trac_6614-distutils_symlinks.patch) by @qed777 created at 2009-07-24 15:27:39\n\nThis [attachment:trac_6614-distutils_symlinks.patch patch] alters `setup.py` so that distutils includes broken symbolic links as it builds a source distribution of the Sage library.  Is this appropriate?\n\nIf so, I can add another patch that replaces the `jsmath` directory in `$SAGE_DOC/common/static` with a symlink and updates the repository accordingly (i.e., reverses the patch mentioned [here](http://trac.sagemath.org/sage_trac/ticket/5799#comment:11)).\n\nOne caveat is that Python's [os](http://docs.python.org/library/os.html) module supports symbolic links only on Unix systems.  If we need to avoid links altogether, we could instead copy jsMath to multiple locations from its own `spkg-install` script.",
    "created_at": "2009-07-24T15:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54041",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6614-distutils_symlinks.patch](tarball://root/attachments/some-uuid/ticket6614/trac_6614-distutils_symlinks.patch) by @qed777 created at 2009-07-24 15:27:39

This [attachment:trac_6614-distutils_symlinks.patch patch] alters `setup.py` so that distutils includes broken symbolic links as it builds a source distribution of the Sage library.  Is this appropriate?

If so, I can add another patch that replaces the `jsmath` directory in `$SAGE_DOC/common/static` with a symlink and updates the repository accordingly (i.e., reverses the patch mentioned [here](http://trac.sagemath.org/sage_trac/ticket/5799#comment:11)).

One caveat is that Python's [os](http://docs.python.org/library/os.html) module supports symbolic links only on Unix systems.  If we need to avoid links altogether, we could instead copy jsMath to multiple locations from its own `spkg-install` script.



---

archive/issue_comments_054042.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-07-24T15:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54042",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to minor.



---

archive/issue_comments_054043.json:
```json
{
    "body": "Changing component from algebra to documentation.",
    "created_at": "2009-07-24T15:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54043",
    "user": "https://github.com/qed777"
}
```

Changing component from algebra to documentation.



---

archive/issue_comments_054044.json:
```json
{
    "body": "Should we add the jsmath directory to devel/sage/.hgignore?",
    "created_at": "2009-07-24T17:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54044",
    "user": "https://github.com/jhpalmieri"
}
```

Should we add the jsmath directory to devel/sage/.hgignore?



---

archive/issue_comments_054045.json:
```json
{
    "body": "Attachment [trac_6614-jsmath_repo.patch](tarball://root/attachments/some-uuid/ticket6614/trac_6614-jsmath_repo.patch) by @qed777 created at 2009-07-25 12:38:28\n\nDifferent approach.",
    "created_at": "2009-07-25T12:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54045",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6614-jsmath_repo.patch](tarball://root/attachments/some-uuid/ticket6614/trac_6614-jsmath_repo.patch) by @qed777 created at 2009-07-25 12:38:28

Different approach.



---

archive/issue_comments_054046.json:
```json
{
    "body": "This [attachment:trac_6614-jsmath_repo.patch alternative patch] deletes `doc/common/static/jsmath` and adds jsMath to `doc/common/conf.py`'s list of `html_static_path`s.\n\nSince Sphinx recursively copies the only the contents of the static paths, jsMath no longer gets its own directory in `_static`.  I've changed `jsmath_path` to `'easy/load.js'`.\n\nIf we take this approach, then I should update the \"`new_scripts`\" patch at #6187.",
    "created_at": "2009-07-25T12:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54046",
    "user": "https://github.com/qed777"
}
```

This [attachment:trac_6614-jsmath_repo.patch alternative patch] deletes `doc/common/static/jsmath` and adds jsMath to `doc/common/conf.py`'s list of `html_static_path`s.

Since Sphinx recursively copies the only the contents of the static paths, jsMath no longer gets its own directory in `_static`.  I've changed `jsmath_path` to `'easy/load.js'`.

If we take this approach, then I should update the "`new_scripts`" patch at #6187.



---

archive/issue_comments_054047.json:
```json
{
    "body": "New version that puts jsMath path first.",
    "created_at": "2009-08-02T18:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54047",
    "user": "https://github.com/qed777"
}
```

New version that puts jsMath path first.



---

archive/issue_comments_054048.json:
```json
{
    "body": "Attachment [trac_6614-jsmath_repo_v2.patch](tarball://root/attachments/some-uuid/ticket6614/trac_6614-jsmath_repo_v2.patch) by @qed777 created at 2009-08-02 19:00:25\n\nThe new version *prepends* jsMath's path to `html_static_path`, so that custom files copied subsequently from, e.g., `doc/common/static`,  can override certain settings, at our option.\n\nThe same caveats apply.",
    "created_at": "2009-08-02T19:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54048",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6614-jsmath_repo_v2.patch](tarball://root/attachments/some-uuid/ticket6614/trac_6614-jsmath_repo_v2.patch) by @qed777 created at 2009-08-02 19:00:25

The new version *prepends* jsMath's path to `html_static_path`, so that custom files copied subsequently from, e.g., `doc/common/static`,  can override certain settings, at our option.

The same caveats apply.



---

archive/issue_comments_054049.json:
```json
{
    "body": "An aside on Firefox's security policy:\n\n* Build the reference manual with `--jsmath`.\n* Browse to the table of contents in FF 3.5.\n* Open \"The Steenrod algebra\", say, in a new background tab by middle-clicking (or the equivalent).\n* Switch to the new tab.  Did jsMath process the page?  Not for me.\n* Switch back to the ToC tab and browse directly to the same topic.  Did jsMath process the page?  Yes for me.\n\nI've tested this only on Linux.  Opera and Chromium don't behave this way, so I don't think it's [entirely] jsMath's fault.\n\nIn any case, this happens whether or not I apply the patch above.",
    "created_at": "2009-08-02T19:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54049",
    "user": "https://github.com/qed777"
}
```

An aside on Firefox's security policy:

* Build the reference manual with `--jsmath`.
* Browse to the table of contents in FF 3.5.
* Open "The Steenrod algebra", say, in a new background tab by middle-clicking (or the equivalent).
* Switch to the new tab.  Did jsMath process the page?  Not for me.
* Switch back to the ToC tab and browse directly to the same topic.  Did jsMath process the page?  Yes for me.

I've tested this only on Linux.  Opera and Chromium don't behave this way, so I don't think it's [entirely] jsMath's fault.

In any case, this happens whether or not I apply the patch above.



---

archive/issue_comments_054050.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> This [attachment:trac_6614-jsmath_repo.patch alternative patch] deletes `doc/common/static/jsmath` and adds jsMath to `doc/common/conf.py`'s list of `html_static_path`s.\nIt may be necessary to delete `doc/common/static/jsmath` manually, after applying the patch.",
    "created_at": "2009-08-03T18:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54050",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 mpatel]:
> This [attachment:trac_6614-jsmath_repo.patch alternative patch] deletes `doc/common/static/jsmath` and adds jsMath to `doc/common/conf.py`'s list of `html_static_path`s.
It may be necessary to delete `doc/common/static/jsmath` manually, after applying the patch.



---

archive/issue_events_015615.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2009-08-20T21:21:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6614#event-15615"
}
```



---

archive/issue_comments_054051.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Since Sphinx recursively copies the only the contents of the static paths, jsMath no longer gets its own directory in `_static`.  I've changed `jsmath_path` to `'easy/load.js'`.\n\nAlso, since the jsMath files all begin with \"jsMath\", we don't have to worry about name clashes (except, I suppose, the names of the subdirectories of jsMath, but I hope this won't be an issue).\n\nAnyway, it looks good to me.  I did manually delete `doc/common/static/jsmath`, and the documentation build correctly, with or without the \"--jsmath\" switch, and jsMath was active when reading docs off-line and on.  The patch is large, but almost all of it consists of deleting files in `doc/common/static/jsmath`; the only \"interesting\" part is at the very beginning, the changes to `conf.py`.  The changes there look good, both the new stuff and tidying up the old stuff (using `os.path.join` instead of \"+\", for example).\n\nI hope I'm not missing anything, but I think it gets a positive review.  Apply only [trac_6614-jsmath_repo_v2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6614/trac_6614-jsmath_repo_v2.patch).",
    "created_at": "2009-08-20T21:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54051",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:3 mpatel]:
> Since Sphinx recursively copies the only the contents of the static paths, jsMath no longer gets its own directory in `_static`.  I've changed `jsmath_path` to `'easy/load.js'`.

Also, since the jsMath files all begin with "jsMath", we don't have to worry about name clashes (except, I suppose, the names of the subdirectories of jsMath, but I hope this won't be an issue).

Anyway, it looks good to me.  I did manually delete `doc/common/static/jsmath`, and the documentation build correctly, with or without the "--jsmath" switch, and jsMath was active when reading docs off-line and on.  The patch is large, but almost all of it consists of deleting files in `doc/common/static/jsmath`; the only "interesting" part is at the very beginning, the changes to `conf.py`.  The changes there look good, both the new stuff and tidying up the old stuff (using `os.path.join` instead of "+", for example).

I hope I'm not missing anything, but I think it gets a positive review.  Apply only [trac_6614-jsmath_repo_v2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6614/trac_6614-jsmath_repo_v2.patch).



---

archive/issue_comments_054052.json:
```json
{
    "body": "I left alone the following line in `MANIFEST.in`\n\n```\nrecursive-include doc/common/static *\n```\n\nI assume this is OK, although it's somewhat more than we need just now.",
    "created_at": "2009-08-22T13:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54052",
    "user": "https://github.com/qed777"
}
```

I left alone the following line in `MANIFEST.in`

```
recursive-include doc/common/static *
```

I assume this is OK, although it's somewhat more than we need just now.



---

archive/issue_comments_054053.json:
```json
{
    "body": "Yes, I noticed that and decided it was okay to leave it.",
    "created_at": "2009-08-22T14:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54053",
    "user": "https://github.com/jhpalmieri"
}
```

Yes, I noticed that and decided it was okay to leave it.



---

archive/issue_comments_054054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T06:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54054",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015616.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-30T06:35:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6614#event-15616"
}
```



---

archive/issue_comments_054055.json:
```json
{
    "body": "For Sage 4.1.1 with `trac_6614-jsmath_repo_v2.patch`, reference manual built with `./sage -docbuild --jsmath reference html`:\n\n* jsMath can't handle Sage's customized LaTeX macros for common rings such such `\\RR` for the reals, `\\ZZ` for the integers, `\\QQ` for the rationals, `\\CC` for complex numbers, and `\\GF(p)` for the finite field of `p` elements. See this screenshot.\n \n* At least with Firefox 3.5.2, jsMath doesn't render LaTeX-typeset maths expressions very well. See this screenshot.\n\nThese two issues are not specific to the patch. The same things happen without `trac_6614-jsmath_repo_v2.patch` being applied to Sage 4.1.1.\n\n\n\nMerged only `trac_6614-jsmath_repo_v2.patch`.",
    "created_at": "2009-08-30T06:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

For Sage 4.1.1 with `trac_6614-jsmath_repo_v2.patch`, reference manual built with `./sage -docbuild --jsmath reference html`:

* jsMath can't handle Sage's customized LaTeX macros for common rings such such `\RR` for the reals, `\ZZ` for the integers, `\QQ` for the rationals, `\CC` for complex numbers, and `\GF(p)` for the finite field of `p` elements. See this screenshot.
 
* At least with Firefox 3.5.2, jsMath doesn't render LaTeX-typeset maths expressions very well. See this screenshot.

These two issues are not specific to the patch. The same things happen without `trac_6614-jsmath_repo_v2.patch` being applied to Sage 4.1.1.



Merged only `trac_6614-jsmath_repo_v2.patch`.



---

archive/issue_comments_054056.json:
```json
{
    "body": "I also manually deleted the directory `doc/common/static/jsmath`.",
    "created_at": "2009-08-30T06:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54056",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I also manually deleted the directory `doc/common/static/jsmath`.



---

archive/issue_comments_054057.json:
```json
{
    "body": "We're working on Sage-specific jsMath customizations for the documentation at #6673.  \n\nThe screenshots appear to be missing, at least for me.\n\nFrom the [changelog](http://www.math.union.edu/~dpvc/jsMath/changes.html) for jsMath 3.6c:\n\n```\n* Worked around another problem with Firefox 3.5's single-origin policy for\n  local files that would cause jsMath not to be able to load external\n  components.\n```\n\nThis may address the \"aside\" above, unless it's besides the aside's point.",
    "created_at": "2009-08-30T07:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54057",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_054058.json:
```json
{
    "body": "I forgot to add links to the screenshots. See [this](http://sage.math.washington.edu/home/mvngu/patch/screenshots/sage-4.1.1-with-trac-6614-custom-latex.png) for the customized LaTeX macros, and [this](http://sage.math.washington.edu/home/mvngu/patch/screenshots/sage-4.1.1-with-trac-6614-jsmath.png) for jsMath issues with Firefox 3.5.2.",
    "created_at": "2009-08-30T08:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54058",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I forgot to add links to the screenshots. See [this](http://sage.math.washington.edu/home/mvngu/patch/screenshots/sage-4.1.1-with-trac-6614-custom-latex.png) for the customized LaTeX macros, and [this](http://sage.math.washington.edu/home/mvngu/patch/screenshots/sage-4.1.1-with-trac-6614-jsmath.png) for jsMath issues with Firefox 3.5.2.



---

archive/issue_comments_054059.json:
```json
{
    "body": "#6673 should help with the macros, but please let us know if we've missed any.\n\nOn the other problem: If Firefox is running on Linux, are the [updated fonts](http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html) installed?",
    "created_at": "2009-08-30T09:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6614#issuecomment-54059",
    "user": "https://github.com/qed777"
}
```

#6673 should help with the macros, but please let us know if we've missed any.

On the other problem: If Firefox is running on Linux, are the [updated fonts](http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html) installed?
