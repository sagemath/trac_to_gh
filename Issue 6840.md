# Issue 6840: Fix documentation for Sage Notebook

Issue created by migration from https://trac.sagemath.org/ticket/6840

Original creator: timdumol

Original creation time: 2009-08-29 07:30:36

Assignee: boothby

Keywords: notebook documentation

Change documentation of the notebook to a uniform format and complete notebook doctest/documentation coverage.

 * Some docstrings are improperly formatted.
 * The formatting of docstrings is inconsistent, e.g.:

Some have:

```
Output: footype

Description
```


While others have:

```
Output:

- footype -- description
```


etc.


---

Comment by timdumol created at 2009-08-29 07:31:56

Fixes docstrings added by patch #6568 in `notebook.py` and `worksheet.py`. Depends on #6568


---

Attachment

I think there is some "overlap" here with version 2 of the patch at #5360.  But that patch makes only a few changes to `notebook.py`.  To avoid merge conflicts, should I put them in a separate patch or bring them here?


---

Comment by timdumol created at 2009-08-30 16:54:21

If you don't mind, I merged the changes from #5360 to save you the trouble.


---

Comment by mpatel created at 2009-08-30 18:09:44

Thanks!  #5360 is now marked for closure.


---

Comment by timdumol created at 2009-08-30 18:11:38

Merged changes from #5360. Apply only this file.


---

Attachment

OBSOLETE.


---

Attachment

I think the patch somehow got doubled in size during the merger.


---

Comment by timdumol created at 2009-08-30 19:31:30

Yes, it got messed up the first times around, but it seems to be the right size: `trac_6840-notebook-documentation-v2.patch  (112.6 KB)`.


---

Comment by mpatel created at 2009-08-31 02:52:49

Version 3 adds _lots_ of small changes to `introspect.py`, `misc.py`, `docHTMLProcessor.py`, `interact.py`, `notebook.py`, `template.py`, and `support.py`.  

Topics: missing docstrings, directives, blank lines, bullet points, headings; other inconsistencies; Sphinx warnings; etc.  The doctests pass, apart the known problem with randomly ordered tests in `worksheet.py`.

I apologize for stepping on any toes.  There may still be other problems, besides those I just introduced.  Prepping `server/` for the reference manual is tedious, but the docstrings do appear to render somewhat more nicely now, especially those in `interact.py`.

Please feel free to make more changes.  Or we can just put this up for review and fix the remaining quirks as we find them.


---

Attachment

Version 3.  Apply only this patch.


---

Attachment

Version 4. Brought up `cell.py` coverage to almost 100%, except for 2 functions.


---

Comment by timdumol created at 2009-08-31 10:18:46

Version 4 adds docstrings and doctests for `cell.py` except for 2 functions: one of which is a hack (`doc_html`), and the other I have no idea how to test (`stop_interacting`).

I'll put this up for review, and we can work on the rest of the documentation another time (unless you want to add some more now?).


---

Comment by mvngu created at 2009-08-31 12:52:56

The patch `trac_6840-notebook-documentation-v4.patch` applies OK against 4.1.1, but with one fuzz:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6840/trac_6840-notebook-documentation-v4.patch && hg qpush
adding trac_6840-notebook-documentation-v4.patch to series file
applying trac_6840-notebook-documentation-v4.patch
patching file sage/server/notebook/config.py
Hunk #1 succeeded at 1 with fuzz 1 (offset -1 lines).
Now at: trac_6840-notebook-documentation-v4.patch
```

Building the reference manual results in about 10 warnings:

```
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.html:8: (WARNING/2) Inline literal start-string without end-string.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.html_out:6: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.is_interacting:8: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.output_text:10: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.parse_html:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.html:8: (WARNING/2) Inline literal start-string without end-string.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.html_out:6: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.is_interacting:8: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.output_text:10: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.parse_html:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```

The test suite reports one doctest failure:

```
sage -t -long devel/sage-main/sage/server/notebook/cell.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/notebook/cell.py", line 1598:
    sage: C.introspect_html()
Expected:
    '<div class="docstring">\n    \n  <p><span class="math">foobar</span></p>\n\n\n</div>'
Got:
    '<div class="docstring">\n    \n  \n  <p><span class="math">foobar</span></p>\n\n\n</div>'
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_71
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_cell.py
	 [26.4 s]
```

I'm marking this as "needs work", since at least the doctest failure must be resolved. The warnings from building the reference manual can be addressed via another ticket. However, it would be nice if both of these issues could be fixed here.


---

Comment by timdumol created at 2009-08-31 14:32:30

I've fixed the warnings and the doctest failure.


---

Comment by timdumol created at 2009-08-31 14:43:55

Fixed documentation warnings and doctest failure. Apply this patch only.


---

Attachment

Miscellaneous tiny changes (see comment). Apply only this patch.


---

Attachment

v6 changes:

 * Fixed `INPUT::` in `template.py`.
 * Removed the space immediately after `:meth:` in two places in `cell.py`.
 * Removed `config.py` from `notebook.rst`, since there's no significant documentation yet on notebook key bindings.

That's impressive coverage for `cell.py`!  It seems that `Cell.stop_interacting()` isn't even called in the Sage library.


---

Comment by mpatel created at 2009-08-31 21:04:53

One way to placate Sphinx about the unused source file `doc/en/reference/sage/server/notebook/config.rst`:  Delete `doc/output/*/en/reference/` and rebuild from scratch.


---

Comment by mvngu created at 2009-09-01 04:20:04

The patch `trac_6840-notebook-documentation-v6.patch` applies OK, but with fuzz:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6840/trac_6840-notebook-documentation-v6.patch && hg qpush
adding trac_6840-notebook-documentation-v6.patch to series file
applying trac_6840-notebook-documentation-v6.patch
patching file sage/server/notebook/config.py
Hunk #1 succeeded at 1 with fuzz 1 (offset -1 lines).
Now at: trac_6840-notebook-documentation-v6.patch
```

Don't worry too much about the fuzz. I have attached a reviewer patch that fixes typos introduced by the previous patch. If you're OK with that reviewer patch, then the ticket gets a positive review and patches should be merged in this order:

 1. `trac_6840-notebook-documentation-v6.patch`
 1. `trac_6840-reviewer.patch`


---

Comment by mpatel created at 2009-09-01 05:16:36

Thanks very much for fixing the typos, including `AttributeErrro`.

Is it alright if we treat the "PLANNING" section near the top of `interact.py` as "internal" documentation, at least for now?  I haven't checked that it's current and Sphinx complains copiously about it.  Either way, just let me know, and I'll attach v2 of the reviewer patch, since I found at least one more minor change to make (`2D` to `2-D`).

By the way, is there a reST alternative to double back-quotes that puts the enclosed text in a fixed-width font but does not change its background color?


---

Comment by mpatel created at 2009-09-01 05:25:19

While I'm here I should ask whether we should put both side-effects, including possible exceptions, _and_ return values in `OUTPUT` sections.  Mostly, I've mentioned just the return values in `OUTPUT`.  On occasion, I've noted significant effects in the blurb at the top of a docstring.


---

Attachment

apply on top of previous patch


---

Comment by mvngu created at 2009-09-01 05:42:18

Replying to [comment:13 mpatel]:
> Is it alright if we treat the "PLANNING" section near the top of `interact.py` as "internal" documentation, at least for now?  I haven't checked that it's current and Sphinx complains copiously about it.
New reviewer patch attached. Please use that one. That should get rid of the complaints by Sphinx.



>  Either way, just let me know, and I'll attach v2 of the reviewer patch, since I found at least one more minor change to make (`2D` to `2-D`).
The updated reviewer patch also addresses this issue.




> By the way, is there a reST alternative to double back-quotes that puts the enclosed text in a fixed-width font but does not change its background color?
I don't know.



Replying to [comment:14 mpatel]:
> While I'm here I should ask whether we should put both side-effects, including possible exceptions, _and_ return values in `OUTPUT` sections.  Mostly, I've mentioned just the return values in `OUTPUT`.  On occasion, I've noted significant effects in the blurb at the top of a docstring.
That's a good idea. Document what works and what doesn't. I usually have a "TESTS:" section for a method/function/class where I document exceptions that could be raised when using that method/function/class.


---

Comment by mvngu created at 2009-09-01 06:12:17

Resolution: fixed


---

Comment by mvngu created at 2009-09-01 06:12:17

Merged patches in this order:

 1. `trac_6840-notebook-documentation-v6.patch`
 1. `trac_6840-reviewer.patch`

I take reviewer credit, but not authorship credit :-)
