# Issue 6568: Migrate Notebook to Jinja

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-07-20 13:50:24

Assignee: timdumol

CC:  jason

Keywords: notebook, jinja,templating engine

Jinja is a templating engine based on Django's. It's already included
in Sage due to the inclusion of Sphinx. Migrating from HTML to
templates should make it easier to make future changes to the code,
and make things easier to read.

Additionally, this will give us the option of switching to a web framework such as Django.


---

Comment by timdumol created at 2009-07-20 17:35:51

Changing status from new to assigned.


---

Comment by timdumol created at 2009-07-20 17:40:01

Changing priority from major to minor.


---

Comment by mvngu created at 2009-07-20 19:04:27

timdumol: There should be a proper username on the patch. At the moment I see this

```
# User deadlyx`@`localhost.localdomain
```

The username should not be a leet handle or anything like that. In order to properly credit contributors to Sage, the username should following this format:

```
# User Full Name <email`@`somewhere.com>
```

You can set a proper username in the file `~/.hgrc` with something like

```
[ui]
username = Full Name <email`@`somewhere.com>
```

I say "should", not "must". If you don't want to, then at least fill in the "Author(s):" field with your full name. That way, it makes it easy to credit you.


---

Comment by timdumol created at 2009-07-21 10:10:16

Replying to [comment:3 mvngu]:
> timdumol: There should be a proper username on the patch. At the moment I see this
> {{{
> # User deadlyx`@`localhost.localdomain
> }}}
> The username should not be a leet handle or anything like that. In order to properly credit contributors to Sage, the username should following this format:
> {{{
> # User Full Name <email`@`somewhere.com>
> }}}
> You can set a proper username in the file `~/.hgrc` with something like
> {{{
> [ui]
> username = Full Name <email`@`somewhere.com>
> }}}
> I say "should", not "must". If you don't want to, then at least fill in the "Author(s):" field with your full name. That way, it makes it easy to credit you.

Thank you very much for noticing that. I didn't realize that my local username was included in the patch. I'll fix it asap.


---

Comment by timdumol created at 2009-07-21 12:43:26

Changing keywords from "notebook, jinja,templating engine" to "notebook, jinja, templating engine".


---

Comment by was created at 2009-07-26 19:09:43

Hi,

I get 8 rejects when trying to apply the first patch to a 100% clean build of sage-4.1:


```
wstein`@`sage:~/build/sage-4.1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: ref3
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/6568/12659.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6568/12659.patch
Loading: [.........]
cd "/scratch/wstein/build/sage-4.1/devel/sage" && hg status
/scratch/wstein/build/sage-4.1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/scratch/wstein/build/sage-4.1/devel/sage" && hg status
cd "/scratch/wstein/build/sage-4.1/devel/sage" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/5378/tmp_1.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/5378/tmp_1.patch
patching file sage/server/notebook/notebook.py
Hunk #1 FAILED at 23
Hunk #2 FAILED at 32
Hunk #3 FAILED at 1355
Hunk #4 FAILED at 1402
Hunk #5 FAILED at 1506
Hunk #6 FAILED at 1704
Hunk #7 FAILED at 1903
Hunk #8 FAILED at 2162
8 out of 8 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej
file sage/server/notebook/templates/debug_window.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/debug_window.html.rej
file sage/server/notebook/templates/guest_top_bar_and_worksheet.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/guest_top_bar_and_worksheet.html.rej
file sage/server/notebook/templates/head.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/head.html.rej
file sage/server/notebook/templates/top_bar_and_worksheet.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/top_bar_and_worksheet.html.rej
file sage/server/notebook/templates/user_controls.tmpl already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/user_controls.tmpl.rej
file sage/server/notebook/templates/worksheet_body.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_body.html.rej
file sage/server/notebook/templates/worksheet_topbar.tmpl already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_topbar.tmpl.rej
abort: patch failed to apply
```

| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
What should I do?  What are these patches against exactly?


---

Comment by timdumol created at 2009-07-27 02:43:13

`@`was:
It seems something went wrong with the patch exporting. I cleaned up my hg history and combined a few changesets to make the patches easier to apply. The new patches are _12659.patch and _12660.patch. Sorry for the inconvenience.

The new patches are against r12658. The old ones were as well, but I don't know what happened to them.


---

Comment by mpatel created at 2009-08-04 06:23:59

I can't apply/review this patch immediately, but it seems that each change appears twice in the latest version.  For example, 

```
$ grep "sage/server/notebook/templates/notebook/worksheet.html" _12660.patch
diff -r d3be9e0b1090 -r a60e86f38be7 sage/server/notebook/templates/notebook/worksheet.html
+++ b/sage/server/notebook/templates/notebook/worksheet.html    Sun Jul 26 14:08:17 2009 +0800
diff -r d3be9e0b1090 -r 1335daa5adcd sage/server/notebook/templates/notebook/worksheet.html
+++ b/sage/server/notebook/templates/notebook/worksheet.html    Tue Jul 28 21:33:54 2009 +0800
```

Also, should "reviisons" appear in the patch?  Sorry, if I'm wrong.


---

Comment by mpatel created at 2009-08-04 06:37:42

The transition to templates is much needed and appreciated.  Thanks very much for doing this.  Is it possible to break up the changes into a few separate pieces, possibly logically independent?  This might make it easier to review them and to get feedback on and track down any changes in the behavior of the notebook.  On the other hand, it may be better to do it all at once.  Thoughts?


---

Comment by timdumol created at 2009-08-05 01:35:59

`@`mpatel

Thanks for the feedback. Yeah, that's a typo. Thanks for catching it.

It seems that the patches are messed up. I've fixed them up with `hg histedit`. I don't see any repeated changes in the patches anymore. Please tell me if there are anymore problems.

Breaking them up seems like a good idea. There are quite a lot of functions though, so there'll be a lot of patches. It may be inconvenient to try them all. Anyways, I'll work on them asap.


---

Comment by timdumol created at 2009-08-05 01:38:53

Migrated notebook.py from HTML to Jinja. Base: r12658 (Sage 4.4.1)


---

Attachment

Migrated worksheet.py to Jinja. Added doctests. Removed html_slide_controls. Incremental patch from the first patch.


---

Attachment

OBSOLETE.


---

Comment by timdumol created at 2009-08-05 01:41:09

OBSOLETE.


---

Attachment

OBSOLETE.


---

Attachment

OBSOLETE.


---

Comment by timdumol created at 2009-08-05 01:41:47

OBSOLETE.


---

Attachment

OBSOLETE.


---

Attachment

OBSOLETE.


---

Comment by timdumol created at 2009-08-05 01:42:27

OBSOLETE.


---

Attachment

OBSOLETE.


---

Comment by timdumol created at 2009-08-05 01:42:55

OBSOLETE.


---

Attachment

OBSOLETE.


---

Attachment

#4808 appears to be a duplicate of this ticket.  When one is merged, please consider closing the other.


---

Comment by mpatel created at 2009-08-13 06:36:50

From some testing in Firefox 3.5 on Linux, with both new patches applied:
 * Live doc worksheets do not load their stylesheets.
 * Published worksheets are now [partially] editable.
 * The "re-publish" and "stop publishing" buttons do not work, apparently.
 * The print representation of a worksheet is missing cell boundaries.

Also, a number of doctests in `notebook.py` and `worksheet.py` failed with `sage -t -long -option -verbose -randorder`.  For `worksheet.py`, there are mostly just small changes in expected HTML output.  I think some of the randomized failures are pre-existing:

```
sage -t -long -optional -randorder=87873 "4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py"
**********************************************************************
File "/home/apps/sage-4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py", line 178:
    sage: sage.server.notebook.worksheet.one_prestarted_sage(None,None)
Expected:
    Sage
Got nothing
**********************************************************************
File "/home/apps/sage-4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py", line 148:
    sage: sage.server.notebook.worksheet._a_sage
Expected nothing
Got:
    Sage
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_1270084472
   1 of   5 in __main__.example_1700749147
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/apps/sage/tmp/.doctest_worksheet.py
         [7.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:
        sage -t -long -optional -randorder=87873 "4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py"
Total time for all tests: 7.9 seconds
```

For `notebook.py`, there are other error types.


---

Comment by mpatel created at 2009-08-13 06:40:14

Also,

```
$ grep reviisons sage-trac-6568.*
sage-trac-6568.2.patch:+<a class="listcontrol" href="reviisons?rev={{ rev }}&action=publis">Publish this one</a>&nbsp;&nbsp;
```



---

Comment by timdumol created at 2009-08-13 10:55:23

I've checked the doctests out on a fresh install (r12659). They also fail, so I assume they're pre-existing. I'm not too familiar with the Notebook code, but I'll see if I can fix them up. Meanwhile, perhaps they should be put on a new ticket.

I'm working on the rest of the problems now.


---

Comment by timdumol created at 2009-08-13 11:06:11

Replying to [comment:16 timdumol]:
> I've checked the doctests out on a fresh install (r12659). They also fail, so I assume they're pre-existing. I'm not too familiar with the Notebook code, but I'll see if I can fix them up. Meanwhile, perhaps they should be put on a new ticket.
> 
> I'm working on the rest of the problems now.

I'm sorry, I meant r12658.


---

Comment by timdumol created at 2009-08-13 12:49:18

Fixed several bugs. Incremental patch from sage-trac-6568.2.patch


---

Attachment

Fixed bug in styling of documentation pages.


---

Comment by timdumol created at 2009-08-13 14:00:14

I've fixed all the outlined bugs, and one more. The doctests all seem to pass, except for the pre-existing failures that you pointed out.


---

Comment by mpatel created at 2009-08-13 22:57:07

* I think clicking "No" in reply to "Do you want to publish this worksheet" unpublishes the worksheet, but it does not return the sheet to interactive mode.

 * jsMath is not included in printed worksheets.  The page itself is missing the title.

 * How does the `morecss` block work?  Can we now avoid `twist.py`'s "hack" altogether?

 * Should, e.g., `server/notebook/templates/doc.html` still be there?

If you're not already using the [Mercurial Queues extension](http://wiki.sagemath.org/MercurialQueues), it may be worth trying. `hg qrefresh` can be very helpful.

I've added Jason Grout to the CC: list, since my checks may not cover the range of notebook usage patterns.  Perhaps we can get other volunteers?


---

Comment by mpatel created at 2009-08-13 22:57:07

Changing priority from minor to major.


---

Comment by timdumol created at 2009-08-14 04:40:24

* The `morecss` inserts the code in the block after the first css include. It should be possible to avoid it by creating another template specifically for documentation pages.
* Probably not. I'll work on cleaning up the file tree asap.
* I'll work on the rest of the bugs.

I've actually been using histedit to combine changesets. Although I'm guessing patch queues are more idiomatic.

I'm pretty new to the Sage community, so I don't know.


---

Comment by mvngu created at 2009-08-14 04:52:12

The [official site](http://mercurial.selenic.com/wiki/) of Mercurial contains many tutorials on using Mercurial itself. In particular, I recommend that you go through its [tutorial for beginners](http://mercurial.selenic.com/wiki/Tutorial). After that, you might want to look through a [section](http://hgbook.red-bean.com/read/managing-change-with-mercurial-queues.html) on using Mercurial queues to manage patches. Anyway, please tell me if you have problems with using Mercurial or its queue extension.


---

Comment by jason created at 2009-08-14 05:49:32

Also, you might look at http://wiki.sagemath.org/MercurialQueues for a quick hands-on introduction to queues.


---

Comment by timdumol created at 2009-08-14 08:16:30

Actually, I meant "I don't know." as in I don't know about the possibility of finding other volunteers. I'm familiar with patch queues. Thanks for the help.


---

Attachment

Fixed a few bugs in templating.


---

Attachment

Removed hack in twist.py for documentation page creation. Removed unused files.


---

Attachment

Cumulative patches from sage-trac-6568.2.patch to sage-trac-6568.6.patch. Incremental patch from sage-trac-6568.1.patch.


---

Comment by timdumol created at 2009-08-14 10:00:41

I've fixed all the bugs pointed out, and the kludge/"hack" was removed. I've also cleaned up the templates file tree. Thanks for noting them.


---

Comment by mpatel created at 2009-08-15 03:05:22

All-in-one.  Apply only this patch.


---

Attachment

I've attached a solo patch comprised of Tim Dumol's six recent patches.  (I did not use the cumulative patch.)  I've ignored a few small rejected hunks from the sixth patch --- in `notebook.py`, `twist.py`, and `base.html` --- since it appears that the rejected changes are applied by an earlier patch.  Of course, all credit for the hard work of migrating the notebook to Jinja should go to Tim.

I haven't tested the latest changes extensively, but I've noticed no unwelcome surprises.


---

Comment by mpatel created at 2009-08-16 13:23:26

Fixed introspection, minor clean-ups.  Apply only this patch.


---

Attachment

Version 2 (of the uber-patch) should fix introspection.  It also
 * Simplifies `Notebook.plain_text_worksheet_html()`.
 * Indents `Notebook.html_debug_window()`'s docstring.

There's still some HTML generation in
 * `Notebook.object_list_html()`, `Notebook.list_window_javascript()`, `Notebook.html_settings()`.
 * `Worksheet.html_ratings_into()`
but these methods are unused or minor.  Of course, there's markup in `interact.py`, etc.

Should we make a separate ticket for moving `css.py`'s stylesheets to `templates/`?  Rebasing other tickets against this one may be easier than the opposite.

My review is positive, though someone else should check the most recent changes.  It would be useful to get feedback from other testers.


---

Comment by timdumol created at 2009-08-16 16:18:04

The patch seems quite large enough as is without including the sheets from `css.py`. I think another ticket would be more suitable.

Actually, I hope to clean the HTML up and replace the table layout with CSS once this gets committed, so it may be nice to put those changes into a new ticket as well.


---

Comment by mpatel created at 2009-08-17 06:44:50

Sounds great.  I'll steer clear.  In the near term, I'll try to simplify the jsMath-related code for #4714, along the lines of #6673.

I should add that v2 of the uni-patch also fixes the "User Management" page at, e.g., `http://localhost:8000/users` (for admins).  The problem was a misuse of `template.template()` in `twist.py`.


---

Comment by was created at 2009-08-29 05:40:58

REFEREE REPORT:

The Sphinx docstrings that you added, which are very good, have a formatting problem, namely below there needs to be a newline before each - (i.e., lots of whitespace):

```
 	1315	        INPUT: 
 	1316	        - ``username`` - a string 
 	1317	        - ``worksheet`` - an instance of Worksheet 
 	1318	 
 	1319	        OUTPUT: 
 	1320	        - a string containing the HTML 
```

See this screenshot: http://wstein.org/home/wstein/tmp/jinja1.png which illustrates how the ReST is messed up.  This isn't a big deal, since I don't think this code is even in the reference manual yet...  But it would be good to go through and fix. 

All doctests pass, and *using* the notebook after applying the patches seems to work fine -- I can't find any visible difference. 

I give this a positive review.  Proper Sphinxing of docs can go in a future patch, and be done throughout the notebook server code.


---

Comment by timdumol created at 2009-08-29 07:33:07

I've created a new ticket for notebook documentation at #6840. The docstrings fixes are there.


---

Comment by mpatel created at 2009-08-30 10:01:38

In part, the patch "v2" at #5360 is an attempt to include some `server/` docstrings in the reference manual.


---

Comment by mvngu created at 2009-08-30 11:32:22

Resolution: fixed


---

Comment by mvngu created at 2009-08-30 11:32:22

The patch `trac_6568-jinja_migration_v2.patch` results in over 20 warnings when building the reference manual:

```
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html:20: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_beforepublish_window:14: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_beforepublish_window:19: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_debug_window:8: (WARNING/2) Literal block expected; none found.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.DIR:1: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_debug_window:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_doc:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_doc:17: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_download_or_delete_datafile:17: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_download_or_delete_datafile:25: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_plain_text_window:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_plain_text_window:24: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_share:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_share:24: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_upload_data_window:13: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_upload_data_window:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_revision_list:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_revision_list:23: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_settings:13: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_settings:20: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.worksheet_html:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.worksheet_html:23: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py:docstring of sage.server.notebook.worksheet.Worksheet.html_menu:10: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```

When I ran the test suite with the patch, I received a timed out error:

```
sage -t -long devel/sage-main/sage/interfaces/ecm.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
	 [1800.1 s]
```

This error has nothing to do with the patch. It might be due to sage.math being too busy or its system resources (probably RAM) nearing capacity. Merged `trac_6568-jinja_migration_v2.patch`.


---

Comment by mpatel created at 2009-08-30 18:22:22

Replying to [comment:33 mvngu]:
> The patch `trac_6568-jinja_migration_v2.patch` results in over 20 warnings when building the reference manual:
I think #6840 will take care of these.


---

Attachment

The patch `trac_6568-manifest.patch` prevents repository corruption. A repository corruption can happen because `trac_6568-jinja_migration_v2.patch` adds two new directories:

 1. `sage/server/notebook/templates/notebook/`
 1. `sage/server/notebook/templates/worksheet/`

If the file `SAGE_ROOT/devel/sage-main/MANIFEST.in` is not patched to handle files under these new directories, those files won't be picked up when making a source release with `sage -sdist`.


---

Comment by mpatel created at 2009-09-07 11:36:17

The "manifest" patch should fix #6884.  If so, please close that ticket.


---

Comment by mvngu created at 2009-09-07 16:22:15

Merged patches in this order:

 1. `trac_6568-jinja_migration_v2.patch`
 1. `trac_6568-manifest.patch`
