# Issue 6820: [with patch, needs review] browse sage docs

archive/issues_006820.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @qed777\n\nThe attached patch introduces the command `browse_sage_doc`.  It lets you do the following from either the command-line or the notebook:\n\n```\nbrowse_sage_doc.tutorial()   # open the tutorial in a browser window\nbrowse_sage_doc.reference()\nbrowse_sage_doc.developer()\nbrowse_sage_doc.constructions()\n```\n\nand also\n\n```\nbrowse_sage_doc(identity_matrix)\n```\n\nopens up the docstring for `identity_matrix` in a browser window.  It doesn't look very pretty, but it's legible.  You can also do\n\n```\nbrowse_sage_doc(identity_matrix, output='rst)\n```\n\nto output (as a string) the reST version of the docstring, and\n\n```\nbrowse_sage_doc(identity_matrix, view=False)\n```\n\nto output (as a string) the html version of the docstring\n\nIssue created by migration from https://trac.sagemath.org/ticket/6820\n\n",
    "created_at": "2009-08-24T20:05:18Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "[with patch, needs review] browse sage docs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6820",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

CC:  @qed777

The attached patch introduces the command `browse_sage_doc`.  It lets you do the following from either the command-line or the notebook:

```
browse_sage_doc.tutorial()   # open the tutorial in a browser window
browse_sage_doc.reference()
browse_sage_doc.developer()
browse_sage_doc.constructions()
```

and also

```
browse_sage_doc(identity_matrix)
```

opens up the docstring for `identity_matrix` in a browser window.  It doesn't look very pretty, but it's legible.  You can also do

```
browse_sage_doc(identity_matrix, output='rst)
```

to output (as a string) the reST version of the docstring, and

```
browse_sage_doc(identity_matrix, view=False)
```

to output (as a string) the html version of the docstring

Issue created by migration from https://trac.sagemath.org/ticket/6820





---

archive/issue_comments_056131.json:
```json
{
    "body": "Sphinx 0.5.1 throws a strange exception in `Cell.set_introspect_html()`.  I set `verbose=True` and replaced `sphinx_app.build(None, [rst_name])` with\n\n```\n                try:\n                    sphinx_app.build(None, [rst_name])\n                except Exception as exc:\n                    print exc\n```\n\nFollowing `sage -br`:\n\n```\nsage: browse_sage_doc(identity_matrix)\nIntrospection cache:  /home/.sage/sage_notebook/doc\nSphinx v0.5.1, building html\nbuilding [html]: 1 source files given on command line\nupdating environment: 1 added, 0 changed, 0 removed\nreading sources... 72cbd366010a4030c528d1f807be048b \npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... 72cbd366010a4030c528d1f807be048b [Errno 2] No such file or directory: '../../../sage/local/lib/python2.6/site-packages/docutils/writers/html4css1/html4css1.css'\nBuilt: /home/.sage/sage_notebook/doc/72cbd366010a4030c528d1f807be048b.html\n---------------------------------------------------------------------------\nIOError                                   Traceback (most recent call last)\n\n/home/.sage/temp/chopin/25868/_home__sage_init_sage_0.py in <module>()\n\n/home/apps/sage/local/lib/python2.6/site-packages/sage/misc/sagedoc.pyc in __call__(self, obj, output, view)\n    842             from sage.server.notebook.cell import Cell\n    843             cell = Cell(0, '0', '0', None)\n--> 844             cell.set_introspect_html(s)\n    845             html = cell._Cell__introspect_html\n    846             if view:\n\n/home/apps/sage/local/lib/python2.6/site-packages/sage/server/notebook/cell.pyc in set_introspect_html(self, html, completing, verbose)\n   1590             finally:\n   1591                 # Contents should be flushed on close().\n-> 1592                 fd_html = open(html_name, 'r')\n   1593                 new_html = fd_html.read()\n   1594                 fd_html.close()\n\nIOError: [Errno 2] No such file or directory: '/home/.sage/sage_notebook/doc/72cbd366010a4030c528d1f807be048b.html'\nsage: \n```\n\nThe lock file remains in the doc cache directory.  This may be peculiar to my current setup, but I can't investigate further right now.\n\nAlso, by default `set_introspect_html()` tries to delete the reST file.\n\nShould we delete leftover .lock files on startup?",
    "created_at": "2009-08-25T00:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56131",
    "user": "https://github.com/qed777"
}
```

Sphinx 0.5.1 throws a strange exception in `Cell.set_introspect_html()`.  I set `verbose=True` and replaced `sphinx_app.build(None, [rst_name])` with

```
                try:
                    sphinx_app.build(None, [rst_name])
                except Exception as exc:
                    print exc
```

Following `sage -br`:

```
sage: browse_sage_doc(identity_matrix)
Introspection cache:  /home/.sage/sage_notebook/doc
Sphinx v0.5.1, building html
building [html]: 1 source files given on command line
updating environment: 1 added, 0 changed, 0 removed
reading sources... 72cbd366010a4030c528d1f807be048b 
pickling environment... done
checking consistency... done
preparing documents... done
writing output... 72cbd366010a4030c528d1f807be048b [Errno 2] No such file or directory: '../../../sage/local/lib/python2.6/site-packages/docutils/writers/html4css1/html4css1.css'
Built: /home/.sage/sage_notebook/doc/72cbd366010a4030c528d1f807be048b.html
---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)

/home/.sage/temp/chopin/25868/_home__sage_init_sage_0.py in <module>()

/home/apps/sage/local/lib/python2.6/site-packages/sage/misc/sagedoc.pyc in __call__(self, obj, output, view)
    842             from sage.server.notebook.cell import Cell
    843             cell = Cell(0, '0', '0', None)
--> 844             cell.set_introspect_html(s)
    845             html = cell._Cell__introspect_html
    846             if view:

/home/apps/sage/local/lib/python2.6/site-packages/sage/server/notebook/cell.pyc in set_introspect_html(self, html, completing, verbose)
   1590             finally:
   1591                 # Contents should be flushed on close().
-> 1592                 fd_html = open(html_name, 'r')
   1593                 new_html = fd_html.read()
   1594                 fd_html.close()

IOError: [Errno 2] No such file or directory: '/home/.sage/sage_notebook/doc/72cbd366010a4030c528d1f807be048b.html'
sage: 
```

The lock file remains in the doc cache directory.  This may be peculiar to my current setup, but I can't investigate further right now.

Also, by default `set_introspect_html()` tries to delete the reST file.

Should we delete leftover .lock files on startup?



---

archive/issue_comments_056132.json:
```json
{
    "body": "On my Mac, I have the same problem with Sphinx 0.5.1, but not with Sphinx 0.6.2.  On an ubuntu box, it works with both 0.5.1 and 0.6.2.",
    "created_at": "2009-08-25T02:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56132",
    "user": "https://github.com/jhpalmieri"
}
```

On my Mac, I have the same problem with Sphinx 0.5.1, but not with Sphinx 0.6.2.  On an ubuntu box, it works with both 0.5.1 and 0.6.2.



---

archive/issue_comments_056133.json:
```json
{
    "body": "I think this is a great facility.  Just being able to pop up the 4 main docs so easily is worth including this!\n\nWhen I tried  browse_sage_doc(identity_matrix) and the like, I found that the first time I did it I got that error:\n\n```\nsage: browse_sage_doc(identity_matrix)\n---------------------------------------------------------------------------\nIOError                                   Traceback (most recent call last)\n\n/home/john/.sage/temp/ubuntu/12456/_home_john__sage_init_sage_0.py in <module>()\n\n/home/john/sage-4.1.1/local/lib/python2.6/site-packages/sage/misc/sagedoc.pyc in __call__(self, obj, output, view)\n    842             from sage.server.notebook.cell import Cell\n    843             cell = Cell(0, '0', '0', None)\n--> 844             cell.set_introspect_html(s)\n    845             html = cell._Cell__introspect_html\n    846             if view:\n\n/home/john/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.pyc in set_introspect_html(self, html, completing, verbose)\n   1587             finally:\n   1588                 # Contents should be flushed on close().\n-> 1589                 fd_html = open(html_name, 'r')\n   1590                 new_html = fd_html.read()\n   1591                 fd_html.close()\n\nIOError: [Errno 2] No such file or directory: '/home/john/.sage/sage_notebook/doc/009e7e626d87d8b9c5ce659c5b01cdb7.html'\n```\n\nbut the second time it worked fine.  Same again with browse_sage_doc(EllipticCurve).\n\nI'm not sure how useful the output='rst' or the view=False options are though.",
    "created_at": "2009-09-02T20:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56133",
    "user": "https://github.com/JohnCremona"
}
```

I think this is a great facility.  Just being able to pop up the 4 main docs so easily is worth including this!

When I tried  browse_sage_doc(identity_matrix) and the like, I found that the first time I did it I got that error:

```
sage: browse_sage_doc(identity_matrix)
---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/12456/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-4.1.1/local/lib/python2.6/site-packages/sage/misc/sagedoc.pyc in __call__(self, obj, output, view)
    842             from sage.server.notebook.cell import Cell
    843             cell = Cell(0, '0', '0', None)
--> 844             cell.set_introspect_html(s)
    845             html = cell._Cell__introspect_html
    846             if view:

/home/john/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/cell.pyc in set_introspect_html(self, html, completing, verbose)
   1587             finally:
   1588                 # Contents should be flushed on close().
-> 1589                 fd_html = open(html_name, 'r')
   1590                 new_html = fd_html.read()
   1591                 fd_html.close()

IOError: [Errno 2] No such file or directory: '/home/john/.sage/sage_notebook/doc/009e7e626d87d8b9c5ce659c5b01cdb7.html'
```

but the second time it worked fine.  Same again with browse_sage_doc(EllipticCurve).

I'm not sure how useful the output='rst' or the view=False options are though.



---

archive/issue_comments_056134.json:
```json
{
    "body": "Changing keywords from \"\" to \"documentation\".",
    "created_at": "2009-09-02T20:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56134",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "documentation".



---

archive/issue_comments_056135.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> I think this is a great facility.  Just being able to pop up the 4 main docs so easily is worth including this!\n> \n> When I tried  browse_sage_doc(identity_matrix) and the like, I found that the first time I did it I got that error:\n\nOn some platforms, this seems to depend on using Sphinx 0.6.2 instead of the version installed with Sage, 0.5.1.  Can you try the spkg at #6586 to see if that helps?  (Use the one listed in [the most recent comment](http://trac.sagemath.org/sage_trac/ticket/6586#comment:33).)\n\n> I'm not sure how useful the output='rst' or the view=False options are though. \n\nMe neither, but this was in response to [a discussion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/fb5f4b2affb89edc/a5d0cdd440aa83fb?tvc=2&q=6820#), in which the ability to see raw rst or raw html was viewed as potentially useful.",
    "created_at": "2009-09-02T21:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56135",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:4 cremona]:
> I think this is a great facility.  Just being able to pop up the 4 main docs so easily is worth including this!
> 
> When I tried  browse_sage_doc(identity_matrix) and the like, I found that the first time I did it I got that error:

On some platforms, this seems to depend on using Sphinx 0.6.2 instead of the version installed with Sage, 0.5.1.  Can you try the spkg at #6586 to see if that helps?  (Use the one listed in [the most recent comment](http://trac.sagemath.org/sage_trac/ticket/6586#comment:33).)

> I'm not sure how useful the output='rst' or the view=False options are though. 

Me neither, but this was in response to [a discussion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/fb5f4b2affb89edc/a5d0cdd440aa83fb?tvc=2&q=6820#), in which the ability to see raw rst or raw html was viewed as potentially useful.



---

archive/issue_comments_056136.json:
```json
{
    "body": "What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.\n\nI'm willing to do this, though not immediately.",
    "created_at": "2009-09-05T23:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56136",
    "user": "https://github.com/qed777"
}
```

What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.

I'm willing to do this, though not immediately.



---

archive/issue_comments_056137.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.\n\nThat sounds good.  This ticket can be accepted as is (if people are happy with it), then the code can be reorganized later.",
    "created_at": "2009-09-06T02:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56137",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:6 mpatel]:
> What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.

That sounds good.  This ticket can be accepted as is (if people are happy with it), then the code can be reorganized later.



---

archive/issue_comments_056138.json:
```json
{
    "body": "I tried this again after installing the new sphinx from #6586, and the problem I reported earlier has gone away.\n\nSo I'm giving this s positive review (noting that it should depend on #6586).\n\nJust one thought -- new users might not think of typing \"browse_sage_doc\", so it might be helpful to include top-level commands tutorial(), manual() [for the reference manual], at least.  Currently help() starts up the python help system which is not so useful in sage, and I would even suggest considering over-writing that with s basic sage help (which would probably just output a brief suggestion to try manual() or tutorial()).",
    "created_at": "2009-09-06T19:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56138",
    "user": "https://github.com/JohnCremona"
}
```

I tried this again after installing the new sphinx from #6586, and the problem I reported earlier has gone away.

So I'm giving this s positive review (noting that it should depend on #6586).

Just one thought -- new users might not think of typing "browse_sage_doc", so it might be helpful to include top-level commands tutorial(), manual() [for the reference manual], at least.  Currently help() starts up the python help system which is not so useful in sage, and I would even suggest considering over-writing that with s basic sage help (which would probably just output a brief suggestion to try manual() or tutorial()).



---

archive/issue_comments_056139.json:
```json
{
    "body": "depends on #6586",
    "created_at": "2009-09-06T19:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56139",
    "user": "https://github.com/jhpalmieri"
}
```

depends on #6586



---

archive/issue_comments_056140.json:
```json
{
    "body": "Attachment [trac_6820-browsedocs.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs.patch) by @jhpalmieri created at 2009-09-06 19:36:54\n\n(I re-attached the same patch so I could add the comment about it depending on #6586.)",
    "created_at": "2009-09-06T19:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56140",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6820-browsedocs.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs.patch) by @jhpalmieri created at 2009-09-06 19:36:54

(I re-attached the same patch so I could add the comment about it depending on #6586.)



---

archive/issue_comments_056141.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> Replying to [comment:6 mpatel]:\n> > What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.\n> That sounds good.  This ticket can be accepted as is (if people are happy with it), then the code can be reorganized later.\nSee #7000.  I may wait until notebook separation is almost complete.  Currently, Sphinx is a prerequisite for [sagenb-0.1.8.tar.gz](http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.1.8.tar.gz).",
    "created_at": "2009-09-25T12:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56141",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:7 jhpalmieri]:
> Replying to [comment:6 mpatel]:
> > What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.
> That sounds good.  This ticket can be accepted as is (if people are happy with it), then the code can be reorganized later.
See #7000.  I may wait until notebook separation is almost complete.  Currently, Sphinx is a prerequisite for [sagenb-0.1.8.tar.gz](http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.1.8.tar.gz).



---

archive/issue_comments_056142.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-10-26T23:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56142",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_056143.json:
```json
{
    "body": "Here's a new patch.  This uses \"sphinxify\" from sagenb, which is good.\n\nFollowing cremona's suggestion above, it also adds top level commands: tutorial, manual, developer, constructions, each of which opens up the named document in a web browser.  Furthermore, it redefines \"help\" so that it prints a short help message:\n\n```\nWelcome to Sage 4.2!  To view the Sage tutorial in your web browser,\ntype 'tutorial()', and to view the (very detailed) Sage reference manual,\ntype 'manual()'.  For help on any function, for example 'matrix_plot', type\n'matrix_plot?' to see display a help message, type 'browse_sage_doc(matrix_plot)'\nto view the same message in a web browser, and type 'matrix_plot??' to look\nat the function's source code.\n\nTo use Python's online help utility, type 'python_help()'.\n```\n\nAs you can see from this message, the old function \"help\" is now called \"python_help\".",
    "created_at": "2009-10-26T23:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56143",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a new patch.  This uses "sphinxify" from sagenb, which is good.

Following cremona's suggestion above, it also adds top level commands: tutorial, manual, developer, constructions, each of which opens up the named document in a web browser.  Furthermore, it redefines "help" so that it prints a short help message:

```
Welcome to Sage 4.2!  To view the Sage tutorial in your web browser,
type 'tutorial()', and to view the (very detailed) Sage reference manual,
type 'manual()'.  For help on any function, for example 'matrix_plot', type
'matrix_plot?' to see display a help message, type 'browse_sage_doc(matrix_plot)'
to view the same message in a web browser, and type 'matrix_plot??' to look
at the function's source code.

To use Python's online help utility, type 'python_help()'.
```

As you can see from this message, the old function "help" is now called "python_help".



---

archive/issue_comments_056144.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-26T23:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56144",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056145.json:
```json
{
    "body": "Attachment [trac_6820-browsedocs-v2.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs-v2.patch) by @jhpalmieri created at 2009-10-27 01:24:41\n\napply only this patch",
    "created_at": "2009-10-27T01:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56145",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6820-browsedocs-v2.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs-v2.patch) by @jhpalmieri created at 2009-10-27 01:24:41

apply only this patch



---

archive/issue_comments_056146.json:
```json
{
    "body": "Attachment [trac_6820-browsedocs-v3.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs-v3.patch) by @qed777 created at 2009-10-27 09:38:42\n\nUse Sphinx stylesheets and jsMath for docstrings.  Apply only this patch.",
    "created_at": "2009-10-27T09:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56146",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6820-browsedocs-v3.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs-v3.patch) by @qed777 created at 2009-10-27 09:38:42

Use Sphinx stylesheets and jsMath for docstrings.  Apply only this patch.



---

archive/issue_comments_056147.json:
```json
{
    "body": "Version 3:\n\n* Uses Sphinx's stylesheet and jsMath to format individual docstrings nicely.  Try `browse_sage_doc(identity_matrix)`.\n* *May* require upgrading [jsMath to version 3.6c](http://www.math.union.edu/~dpvc/jsMath/changes.html), because of Firefox's 3.5's same-origin policy for local files.\n* Guesses the `obj`'s name.  See [this](http://www.daniweb.com/forums/thread229813.html), [this](http://pythonic.pocoo.org/2009/5/30/finding-objects-names), and/or [this](http://bytes.com/topic/python/answers/19521-gathering-variable-names-within-function).\n\nProblems:\n\n* Math does **not** render properly because backslashes are stripped, somewhere.\n* It may be better to use a HTML template instead of an inline triple-quoted string.",
    "created_at": "2009-10-27T09:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56147",
    "user": "https://github.com/qed777"
}
```

Version 3:

* Uses Sphinx's stylesheet and jsMath to format individual docstrings nicely.  Try `browse_sage_doc(identity_matrix)`.
* *May* require upgrading [jsMath to version 3.6c](http://www.math.union.edu/~dpvc/jsMath/changes.html), because of Firefox's 3.5's same-origin policy for local files.
* Guesses the `obj`'s name.  See [this](http://www.daniweb.com/forums/thread229813.html), [this](http://pythonic.pocoo.org/2009/5/30/finding-objects-names), and/or [this](http://bytes.com/topic/python/answers/19521-gathering-variable-names-within-function).

Problems:

* Math does **not** render properly because backslashes are stripped, somewhere.
* It may be better to use a HTML template instead of an inline triple-quoted string.



---

archive/issue_comments_056148.json:
```json
{
    "body": "Okay, this patch doesn't accidentally strip the backslashes anymore.  This depends on #6673, and indeed, it doesn't seem to work on Firefox.",
    "created_at": "2009-10-27T22:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56148",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, this patch doesn't accidentally strip the backslashes anymore.  This depends on #6673, and indeed, it doesn't seem to work on Firefox.



---

archive/issue_comments_056149.json:
```json
{
    "body": "Attachment [trac_6820-browsedocs-v4.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs-v4.patch) by @jhpalmieri created at 2009-10-27 22:46:59\n\ndepends on #6673.  apply only this patch.",
    "created_at": "2009-10-27T22:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56149",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6820-browsedocs-v4.patch](tarball://root/attachments/some-uuid/ticket6820/trac_6820-browsedocs-v4.patch) by @jhpalmieri created at 2009-10-27 22:46:59

depends on #6673.  apply only this patch.



---

archive/issue_comments_056150.json:
```json
{
    "body": "Thanks very much for restoring the backslashes --- I didn't think of `EMBEDDED_MODE`.  I'll try to take a closer look at the jsMath problem.  If necessaary, there's #7322.",
    "created_at": "2009-10-28T19:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56150",
    "user": "https://github.com/qed777"
}
```

Thanks very much for restoring the backslashes --- I didn't think of `EMBEDDED_MODE`.  I'll try to take a closer look at the jsMath problem.  If necessaary, there's #7322.



---

archive/issue_comments_056151.json:
```json
{
    "body": "The patch at #7322 upgrades SageNB to jsMath 3.6c.  Please be sure to run\n\n```sh\nsage -docbuild website html -j -S -aE\n```\n\nbefore checking that Firefox 3.5.x now typesets `browse_sage_doc(Zmod)`.",
    "created_at": "2009-10-29T07:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56151",
    "user": "https://github.com/qed777"
}
```

The patch at #7322 upgrades SageNB to jsMath 3.6c.  Please be sure to run

```sh
sage -docbuild website html -j -S -aE
```

before checking that Firefox 3.5.x now typesets `browse_sage_doc(Zmod)`.



---

archive/issue_comments_056152.json:
```json
{
    "body": "Should we add a `browse_sage_src()` for parity with the SageNB's `??`.",
    "created_at": "2009-10-29T07:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56152",
    "user": "https://github.com/qed777"
}
```

Should we add a `browse_sage_src()` for parity with the SageNB's `??`.



---

archive/issue_comments_056153.json:
```json
{
    "body": "> The patch at #7322 upgrades SageNB to jsMath 3.6c. Please be sure to run\n> \n> sage -docbuild website html -j -S -aE\n>\n> before checking that Firefox 3.5.x now typesets browse_sage_doc(Zmod).\n\nIt works!  (At least on my Mac running OS X 10.5.)\n\n> Should we add a `browse_sage_src()` for parity with the SageNB's `??`.\n\nNot on this ticket.\n\nI'm happy with this.  I'm giving mpatel's contributions a positive review, so if someone can give my contributions a positive review, the patch can be merged.",
    "created_at": "2009-10-29T20:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56153",
    "user": "https://github.com/jhpalmieri"
}
```

> The patch at #7322 upgrades SageNB to jsMath 3.6c. Please be sure to run
> 
> sage -docbuild website html -j -S -aE
>
> before checking that Firefox 3.5.x now typesets browse_sage_doc(Zmod).

It works!  (At least on my Mac running OS X 10.5.)

> Should we add a `browse_sage_src()` for parity with the SageNB's `??`.

Not on this ticket.

I'm happy with this.  I'm giving mpatel's contributions a positive review, so if someone can give my contributions a positive review, the patch can be merged.



---

archive/issue_comments_056154.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T21:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56154",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056155.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6820#issuecomment-56155",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
