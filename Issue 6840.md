# Issue 6840: Fix documentation for Sage Notebook

archive/issues_006840.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: notebook documentation\n\nChange documentation of the notebook to a uniform format and complete notebook doctest/documentation coverage.\n\n* Some docstrings are improperly formatted.\n* The formatting of docstrings is inconsistent, e.g.:\n\nSome have:\n\n```\nOutput: footype\n\nDescription\n```\n\n\nWhile others have:\n\n```\nOutput:\n\n- footype -- description\n```\n\n\netc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6840\n\n",
    "created_at": "2009-08-29T07:30:36Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Fix documentation for Sage Notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6840",
    "user": "timdumol"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/6840





---

archive/issue_comments_056410.json:
```json
{
    "body": "Fixes docstrings added by patch #6568 in `notebook.py` and `worksheet.py`. Depends on #6568",
    "created_at": "2009-08-29T07:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56410",
    "user": "timdumol"
}
```

Fixes docstrings added by patch #6568 in `notebook.py` and `worksheet.py`. Depends on #6568



---

archive/issue_comments_056411.json:
```json
{
    "body": "Attachment [trac_6840-notebook-documentation.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation.patch) by mpatel created at 2009-08-30 10:16:59\n\nI think there is some \"overlap\" here with version 2 of the patch at #5360.  But that patch makes only a few changes to `notebook.py`.  To avoid merge conflicts, should I put them in a separate patch or bring them here?",
    "created_at": "2009-08-30T10:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56411",
    "user": "mpatel"
}
```

Attachment [trac_6840-notebook-documentation.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation.patch) by mpatel created at 2009-08-30 10:16:59

I think there is some "overlap" here with version 2 of the patch at #5360.  But that patch makes only a few changes to `notebook.py`.  To avoid merge conflicts, should I put them in a separate patch or bring them here?



---

archive/issue_comments_056412.json:
```json
{
    "body": "If you don't mind, I merged the changes from #5360 to save you the trouble.",
    "created_at": "2009-08-30T16:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56412",
    "user": "timdumol"
}
```

If you don't mind, I merged the changes from #5360 to save you the trouble.



---

archive/issue_comments_056413.json:
```json
{
    "body": "Thanks!  #5360 is now marked for closure.",
    "created_at": "2009-08-30T18:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56413",
    "user": "mpatel"
}
```

Thanks!  #5360 is now marked for closure.



---

archive/issue_comments_056414.json:
```json
{
    "body": "Merged changes from #5360. Apply only this file.",
    "created_at": "2009-08-30T18:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56414",
    "user": "timdumol"
}
```

Merged changes from #5360. Apply only this file.



---

archive/issue_comments_056415.json:
```json
{
    "body": "Attachment [trac_6840-notebook-documentation-v2.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v2.patch) by timdumol created at 2009-08-30 18:13:32\n\nOBSOLETE.",
    "created_at": "2009-08-30T18:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56415",
    "user": "timdumol"
}
```

Attachment [trac_6840-notebook-documentation-v2.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v2.patch) by timdumol created at 2009-08-30 18:13:32

OBSOLETE.



---

archive/issue_comments_056416.json:
```json
{
    "body": "Attachment [trac_6840-notebook-documentation.v2.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation.v2.patch) by mpatel created at 2009-08-30 18:18:08\n\nI think the patch somehow got doubled in size during the merger.",
    "created_at": "2009-08-30T18:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56416",
    "user": "mpatel"
}
```

Attachment [trac_6840-notebook-documentation.v2.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation.v2.patch) by mpatel created at 2009-08-30 18:18:08

I think the patch somehow got doubled in size during the merger.



---

archive/issue_comments_056417.json:
```json
{
    "body": "Yes, it got messed up the first times around, but it seems to be the right size: `trac_6840-notebook-documentation-v2.patch  (112.6 KB)`.",
    "created_at": "2009-08-30T19:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56417",
    "user": "timdumol"
}
```

Yes, it got messed up the first times around, but it seems to be the right size: `trac_6840-notebook-documentation-v2.patch  (112.6 KB)`.



---

archive/issue_comments_056418.json:
```json
{
    "body": "Version 3 adds *lots* of small changes to `introspect.py`, `misc.py`, `docHTMLProcessor.py`, `interact.py`, `notebook.py`, `template.py`, and `support.py`.  \n\nTopics: missing docstrings, directives, blank lines, bullet points, headings; other inconsistencies; Sphinx warnings; etc.  The doctests pass, apart the known problem with randomly ordered tests in `worksheet.py`.\n\nI apologize for stepping on any toes.  There may still be other problems, besides those I just introduced.  Prepping `server/` for the reference manual is tedious, but the docstrings do appear to render somewhat more nicely now, especially those in `interact.py`.\n\nPlease feel free to make more changes.  Or we can just put this up for review and fix the remaining quirks as we find them.",
    "created_at": "2009-08-31T02:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56418",
    "user": "mpatel"
}
```

Version 3 adds *lots* of small changes to `introspect.py`, `misc.py`, `docHTMLProcessor.py`, `interact.py`, `notebook.py`, `template.py`, and `support.py`.  

Topics: missing docstrings, directives, blank lines, bullet points, headings; other inconsistencies; Sphinx warnings; etc.  The doctests pass, apart the known problem with randomly ordered tests in `worksheet.py`.

I apologize for stepping on any toes.  There may still be other problems, besides those I just introduced.  Prepping `server/` for the reference manual is tedious, but the docstrings do appear to render somewhat more nicely now, especially those in `interact.py`.

Please feel free to make more changes.  Or we can just put this up for review and fix the remaining quirks as we find them.



---

archive/issue_comments_056419.json:
```json
{
    "body": "Attachment [trac_6840-notebook-documentation-v3.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v3.patch) by mpatel created at 2009-08-31 03:08:17\n\nVersion 3.  Apply only this patch.",
    "created_at": "2009-08-31T03:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56419",
    "user": "mpatel"
}
```

Attachment [trac_6840-notebook-documentation-v3.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v3.patch) by mpatel created at 2009-08-31 03:08:17

Version 3.  Apply only this patch.



---

archive/issue_comments_056420.json:
```json
{
    "body": "Attachment [trac_6840-notebook-documentation-v4.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v4.patch) by timdumol created at 2009-08-31 10:15:45\n\nVersion 4. Brought up `cell.py` coverage to almost 100%, except for 2 functions.",
    "created_at": "2009-08-31T10:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56420",
    "user": "timdumol"
}
```

Attachment [trac_6840-notebook-documentation-v4.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v4.patch) by timdumol created at 2009-08-31 10:15:45

Version 4. Brought up `cell.py` coverage to almost 100%, except for 2 functions.



---

archive/issue_comments_056421.json:
```json
{
    "body": "Version 4 adds docstrings and doctests for `cell.py` except for 2 functions: one of which is a hack (`doc_html`), and the other I have no idea how to test (`stop_interacting`).\n\nI'll put this up for review, and we can work on the rest of the documentation another time (unless you want to add some more now?).",
    "created_at": "2009-08-31T10:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56421",
    "user": "timdumol"
}
```

Version 4 adds docstrings and doctests for `cell.py` except for 2 functions: one of which is a hack (`doc_html`), and the other I have no idea how to test (`stop_interacting`).

I'll put this up for review, and we can work on the rest of the documentation another time (unless you want to add some more now?).



---

archive/issue_comments_056422.json:
```json
{
    "body": "The patch `trac_6840-notebook-documentation-v4.patch` applies OK against 4.1.1, but with one fuzz:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6840/trac_6840-notebook-documentation-v4.patch && hg qpush\nadding trac_6840-notebook-documentation-v4.patch to series file\napplying trac_6840-notebook-documentation-v4.patch\npatching file sage/server/notebook/config.py\nHunk #1 succeeded at 1 with fuzz 1 (offset -1 lines).\nNow at: trac_6840-notebook-documentation-v4.patch\n```\n\nBuilding the reference manual results in about 10 warnings:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.html:8: (WARNING/2) Inline literal start-string without end-string.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.html_out:6: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.is_interacting:8: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.output_text:10: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.Cell.parse_html:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.html:8: (WARNING/2) Inline literal start-string without end-string.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.html_out:6: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.is_interacting:8: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.output_text:10: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.py:docstring of sage.server.notebook.cell.ComputeCell.parse_html:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```\n\nThe test suite reports one doctest failure:\n\n```\nsage -t -long devel/sage-main/sage/server/notebook/cell.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/notebook/cell.py\", line 1598:\n    sage: C.introspect_html()\nExpected:\n    '<div class=\"docstring\">\\n    \\n  <p><span class=\"math\">foobar</span></p>\\n\\n\\n</div>'\nGot:\n    '<div class=\"docstring\">\\n    \\n  \\n  <p><span class=\"math\">foobar</span></p>\\n\\n\\n</div>'\n**********************************************************************\n1 items had failures:\n   1 of  13 in __main__.example_71\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_cell.py\n\t [26.4 s]\n```\n\nI'm marking this as \"needs work\", since at least the doctest failure must be resolved. The warnings from building the reference manual can be addressed via another ticket. However, it would be nice if both of these issues could be fixed here.",
    "created_at": "2009-08-31T12:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56422",
    "user": "mvngu"
}
```

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

archive/issue_comments_056423.json:
```json
{
    "body": "I've fixed the warnings and the doctest failure.",
    "created_at": "2009-08-31T14:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56423",
    "user": "timdumol"
}
```

I've fixed the warnings and the doctest failure.



---

archive/issue_comments_056424.json:
```json
{
    "body": "Fixed documentation warnings and doctest failure. Apply this patch only.",
    "created_at": "2009-08-31T14:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56424",
    "user": "timdumol"
}
```

Fixed documentation warnings and doctest failure. Apply this patch only.



---

archive/issue_comments_056425.json:
```json
{
    "body": "Attachment [trac_6840-notebook-documentation-v5.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v5.patch) by mpatel created at 2009-08-31 20:43:37\n\nMiscellaneous tiny changes (see comment). Apply only this patch.",
    "created_at": "2009-08-31T20:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56425",
    "user": "mpatel"
}
```

Attachment [trac_6840-notebook-documentation-v5.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v5.patch) by mpatel created at 2009-08-31 20:43:37

Miscellaneous tiny changes (see comment). Apply only this patch.



---

archive/issue_comments_056426.json:
```json
{
    "body": "Attachment [trac_6840-notebook-documentation-v6.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v6.patch) by mpatel created at 2009-08-31 20:54:01\n\nv6 changes:\n\n* Fixed `INPUT::` in `template.py`.\n* Removed the space immediately after `:meth:` in two places in `cell.py`.\n* Removed `config.py` from `notebook.rst`, since there's no significant documentation yet on notebook key bindings.\n\nThat's impressive coverage for `cell.py`!  It seems that `Cell.stop_interacting()` isn't even called in the Sage library.",
    "created_at": "2009-08-31T20:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56426",
    "user": "mpatel"
}
```

Attachment [trac_6840-notebook-documentation-v6.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-notebook-documentation-v6.patch) by mpatel created at 2009-08-31 20:54:01

v6 changes:

* Fixed `INPUT::` in `template.py`.
* Removed the space immediately after `:meth:` in two places in `cell.py`.
* Removed `config.py` from `notebook.rst`, since there's no significant documentation yet on notebook key bindings.

That's impressive coverage for `cell.py`!  It seems that `Cell.stop_interacting()` isn't even called in the Sage library.



---

archive/issue_comments_056427.json:
```json
{
    "body": "One way to placate Sphinx about the unused source file `doc/en/reference/sage/server/notebook/config.rst`:  Delete `doc/output/*/en/reference/` and rebuild from scratch.",
    "created_at": "2009-08-31T21:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56427",
    "user": "mpatel"
}
```

One way to placate Sphinx about the unused source file `doc/en/reference/sage/server/notebook/config.rst`:  Delete `doc/output/*/en/reference/` and rebuild from scratch.



---

archive/issue_comments_056428.json:
```json
{
    "body": "The patch `trac_6840-notebook-documentation-v6.patch` applies OK, but with fuzz:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6840/trac_6840-notebook-documentation-v6.patch && hg qpush\nadding trac_6840-notebook-documentation-v6.patch to series file\napplying trac_6840-notebook-documentation-v6.patch\npatching file sage/server/notebook/config.py\nHunk #1 succeeded at 1 with fuzz 1 (offset -1 lines).\nNow at: trac_6840-notebook-documentation-v6.patch\n```\n\nDon't worry too much about the fuzz. I have attached a reviewer patch that fixes typos introduced by the previous patch. If you're OK with that reviewer patch, then the ticket gets a positive review and patches should be merged in this order:\n\n1. `trac_6840-notebook-documentation-v6.patch`\n2. `trac_6840-reviewer.patch`",
    "created_at": "2009-09-01T04:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56428",
    "user": "mvngu"
}
```

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
2. `trac_6840-reviewer.patch`



---

archive/issue_comments_056429.json:
```json
{
    "body": "Thanks very much for fixing the typos, including `AttributeErrro`.\n\nIs it alright if we treat the \"PLANNING\" section near the top of `interact.py` as \"internal\" documentation, at least for now?  I haven't checked that it's current and Sphinx complains copiously about it.  Either way, just let me know, and I'll attach v2 of the reviewer patch, since I found at least one more minor change to make (`2D` to `2-D`).\n\nBy the way, is there a reST alternative to double back-quotes that puts the enclosed text in a fixed-width font but does not change its background color?",
    "created_at": "2009-09-01T05:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56429",
    "user": "mpatel"
}
```

Thanks very much for fixing the typos, including `AttributeErrro`.

Is it alright if we treat the "PLANNING" section near the top of `interact.py` as "internal" documentation, at least for now?  I haven't checked that it's current and Sphinx complains copiously about it.  Either way, just let me know, and I'll attach v2 of the reviewer patch, since I found at least one more minor change to make (`2D` to `2-D`).

By the way, is there a reST alternative to double back-quotes that puts the enclosed text in a fixed-width font but does not change its background color?



---

archive/issue_comments_056430.json:
```json
{
    "body": "While I'm here I should ask whether we should put both side-effects, including possible exceptions, *and* return values in `OUTPUT` sections.  Mostly, I've mentioned just the return values in `OUTPUT`.  On occasion, I've noted significant effects in the blurb at the top of a docstring.",
    "created_at": "2009-09-01T05:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56430",
    "user": "mpatel"
}
```

While I'm here I should ask whether we should put both side-effects, including possible exceptions, *and* return values in `OUTPUT` sections.  Mostly, I've mentioned just the return values in `OUTPUT`.  On occasion, I've noted significant effects in the blurb at the top of a docstring.



---

archive/issue_comments_056431.json:
```json
{
    "body": "Attachment [trac_6840-reviewer.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-reviewer.patch) by mvngu created at 2009-09-01 05:35:14\n\napply on top of previous patch",
    "created_at": "2009-09-01T05:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56431",
    "user": "mvngu"
}
```

Attachment [trac_6840-reviewer.patch](tarball://root/attachments/some-uuid/ticket6840/trac_6840-reviewer.patch) by mvngu created at 2009-09-01 05:35:14

apply on top of previous patch



---

archive/issue_comments_056432.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Is it alright if we treat the \"PLANNING\" section near the top of `interact.py` as \"internal\" documentation, at least for now?  I haven't checked that it's current and Sphinx complains copiously about it.\nNew reviewer patch attached. Please use that one. That should get rid of the complaints by Sphinx.\n\n\n\n>  Either way, just let me know, and I'll attach v2 of the reviewer patch, since I found at least one more minor change to make (`2D` to `2-D`).\nThe updated reviewer patch also addresses this issue.\n\n\n\n\n> By the way, is there a reST alternative to double back-quotes that puts the enclosed text in a fixed-width font but does not change its background color?\nI don't know.\n\n\n\nReplying to [comment:14 mpatel]:\n> While I'm here I should ask whether we should put both side-effects, including possible exceptions, *and* return values in `OUTPUT` sections.  Mostly, I've mentioned just the return values in `OUTPUT`.  On occasion, I've noted significant effects in the blurb at the top of a docstring.\nThat's a good idea. Document what works and what doesn't. I usually have a \"TESTS:\" section for a method/function/class where I document exceptions that could be raised when using that method/function/class.",
    "created_at": "2009-09-01T05:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56432",
    "user": "mvngu"
}
```

Replying to [comment:13 mpatel]:
> Is it alright if we treat the "PLANNING" section near the top of `interact.py` as "internal" documentation, at least for now?  I haven't checked that it's current and Sphinx complains copiously about it.
New reviewer patch attached. Please use that one. That should get rid of the complaints by Sphinx.



>  Either way, just let me know, and I'll attach v2 of the reviewer patch, since I found at least one more minor change to make (`2D` to `2-D`).
The updated reviewer patch also addresses this issue.




> By the way, is there a reST alternative to double back-quotes that puts the enclosed text in a fixed-width font but does not change its background color?
I don't know.



Replying to [comment:14 mpatel]:
> While I'm here I should ask whether we should put both side-effects, including possible exceptions, *and* return values in `OUTPUT` sections.  Mostly, I've mentioned just the return values in `OUTPUT`.  On occasion, I've noted significant effects in the blurb at the top of a docstring.
That's a good idea. Document what works and what doesn't. I usually have a "TESTS:" section for a method/function/class where I document exceptions that could be raised when using that method/function/class.



---

archive/issue_comments_056433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-01T06:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56433",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056434.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6840-notebook-documentation-v6.patch`\n2. `trac_6840-reviewer.patch`\n\nI take reviewer credit, but not authorship credit :-)",
    "created_at": "2009-09-01T06:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6840#issuecomment-56434",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6840-notebook-documentation-v6.patch`
2. `trac_6840-reviewer.patch`

I take reviewer credit, but not authorship credit :-)
