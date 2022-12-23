# Issue 6820: [with patch, needs review] browse sage docs

Issue created by migration from https://trac.sagemath.org/ticket/6820

Original creator: jhpalmieri

Original creation time: 2009-08-24 20:05:18

Assignee: tba

CC:  mpatel

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


---

Comment by mpatel created at 2009-08-25 00:14:38

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

Comment by jhpalmieri created at 2009-08-25 02:19:20

On my Mac, I have the same problem with Sphinx 0.5.1, but not with Sphinx 0.6.2.  On an ubuntu box, it works with both 0.5.1 and 0.6.2.


---

Comment by cremona created at 2009-09-02 20:35:16

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

Comment by cremona created at 2009-09-02 20:35:16

Changing keywords from "" to "documentation".


---

Comment by jhpalmieri created at 2009-09-02 21:31:58

Replying to [comment:4 cremona]:
> I think this is a great facility.  Just being able to pop up the 4 main docs so easily is worth including this!
> 
> When I tried  browse_sage_doc(identity_matrix) and the like, I found that the first time I did it I got that error:

On some platforms, this seems to depend on using Sphinx 0.6.2 instead of the version installed with Sage, 0.5.1.  Can you try the spkg at #6586 to see if that helps?  (Use the one listed in [the most recent comment](http://trac.sagemath.org/sage_trac/ticket/6586#comment:33).)

> I'm not sure how useful the output='rst' or the view=False options are though. 

Me neither, but this was in response to [a discussion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/fb5f4b2affb89edc/a5d0cdd440aa83fb?tvc=2&q=6820#), in which the ability to see raw rst or raw html was viewed as potentially useful.


---

Comment by mpatel created at 2009-09-05 23:42:26

What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.

I'm willing to do this, though not immediately.


---

Comment by jhpalmieri created at 2009-09-06 02:12:23

Replying to [comment:6 mpatel]:
> What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.

That sounds good.  This ticket can be accepted as is (if people are happy with it), then the code can be reorganized later.


---

Comment by cremona created at 2009-09-06 19:25:57

I tried this again after installing the new sphinx from #6586, and the problem I reported earlier has gone away.

So I'm giving this s positive review (noting that it should depend on #6586).

Just one thought -- new users might not think of typing "browse_sage_doc", so it might be helpful to include top-level commands tutorial(), manual() [for the reference manual], at least.  Currently help() starts up the python help system which is not so useful in sage, and I would even suggest considering over-writing that with s basic sage help (which would probably just output a brief suggestion to try manual() or tutorial()).


---

Comment by jhpalmieri created at 2009-09-06 19:36:08

depends on #6586


---

Attachment

(I re-attached the same patch so I could add the comment about it depending on #6586.)


---

Comment by mpatel created at 2009-09-25 12:46:00

Replying to [comment:7 jhpalmieri]:
> Replying to [comment:6 mpatel]:
> > What if we moved the Sphinx-ify code to another or its own module?  This might make it easier to develop and use in multiple contexts.
> That sounds good.  This ticket can be accepted as is (if people are happy with it), then the code can be reorganized later.
See #7000.  I may wait until notebook separation is almost complete.  Currently, Sphinx is a prerequisite for [sagenb-0.1.8.tar.gz](http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.1.8.tar.gz).


---

Comment by jhpalmieri created at 2009-10-26 23:25:48

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2009-10-26 23:25:48

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

Comment by jhpalmieri created at 2009-10-26 23:25:54

Changing status from needs_work to needs_review.


---

Attachment

apply only this patch


---

Attachment

Use Sphinx stylesheets and jsMath for docstrings.  Apply only this patch.


---

Comment by mpatel created at 2009-10-27 09:54:08

Version 3:

 * Uses Sphinx's stylesheet and jsMath to format individual docstrings nicely.  Try `browse_sage_doc(identity_matrix)`.
 * _May_ require upgrading [jsMath to version 3.6c](http://www.math.union.edu/~dpvc/jsMath/changes.html), because of Firefox's 3.5's same-origin policy for local files.
 * Guesses the `obj`'s name.  See [this](http://www.daniweb.com/forums/thread229813.html), [this](http://pythonic.pocoo.org/2009/5/30/finding-objects-names), and/or [this](http://bytes.com/topic/python/answers/19521-gathering-variable-names-within-function).

Problems:

 * Math does *not* render properly because backslashes are stripped, somewhere.
 * It may be better to use a HTML template instead of an inline triple-quoted string.


---

Comment by jhpalmieri created at 2009-10-27 22:46:21

Okay, this patch doesn't accidentally strip the backslashes anymore.  This depends on #6673, and indeed, it doesn't seem to work on Firefox.


---

Attachment

depends on #6673.  apply only this patch.


---

Comment by mpatel created at 2009-10-28 19:54:51

Thanks very much for restoring the backslashes --- I didn't think of `EMBEDDED_MODE`.  I'll try to take a closer look at the jsMath problem.  If necessaary, there's #7322.


---

Comment by mpatel created at 2009-10-29 07:38:05

The patch at #7322 upgrades SageNB to jsMath 3.6c.  Please be sure to run

```sh
sage -docbuild website html -j -S -aE
```

before checking that Firefox 3.5.x now typesets `browse_sage_doc(Zmod)`.


---

Comment by mpatel created at 2009-10-29 07:42:24

Should we add a `browse_sage_src()` for parity with the SageNB's `??`.


---

Comment by jhpalmieri created at 2009-10-29 20:13:24

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

Comment by cremona created at 2009-10-29 21:04:56

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 22:03:51

Resolution: fixed
