# Issue 8146: building HTML version of French tutorial is broken

Issue created by migration from https://trac.sagemath.org/ticket/8146

Original creator: mvngu

Original creation time: 2010-02-02 02:02:41

Assignee: mvngu

CC:  mpatel

Keywords: French tutorial

Ticket #8036 fixes some issues with non-ASCII characters in the reference manual. But it breaks the building of the HTML version of the French tutorial:

```
sphinx-build -b html -d /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/output/doctrees/fr/tutorial    /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/fr/tutorial /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/output/html/fr/tutorial
Running Sphinx v0.6.3

Exception occurred:
  File "/scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/fr/tutorial/conf.py", line 38, in <module>
    latex_preamble += '\\DeclareUnicodeCharacter{00A0}{\\nobreakspace}\n'
NameError: name 'latex_preamble' is not defined
The full traceback has been saved in /tmp/sphinx-err-6XQBIT.log, if you want to report the issue to the author.
Please also report this if it was a user error, so that a better error message can be provided next time.
Send reports to sphinx-dev@googlegroups.com. Thanks!
Build finished.  The built documents can be found in /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/output/html/fr/tutorial
```

This is due to the deletion of the line

```
latex_preamble = '\usepackage{amsmath}\n\usepackage{amsfonts}\n' 
```

in [trac_8036-docbuild_utf8x.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8036/trac_8036-docbuild_utf8x.patch). I'm making this a blocker against Sage 4.3.2.


---

Comment by mpatel created at 2010-02-02 02:10:24

We need to upgrade `SAGE_DOC/fr/tutorial/conf.py` to use `latex_elements['preamble']` instead of `latex_preamble`, which is [deprecated](http://sphinx.pocoo.org/config.html#confval-latex_preamble).  I'll check the other documents.


---

Comment by jhpalmieri created at 2010-02-02 02:44:44

If I either delete the last few lines of `SAGE_DOC/fr/tutorial/conf.py` -- the ones dealing with `latex_preamble` -- or if I replace them with lines using `latex_elements['preamble']` instead, the build seems to go through either way.  I suppose the second option is closer to what we have now, so we should use that?  Here's a patch.


---

Comment by jhpalmieri created at 2010-02-02 02:44:44

Changing status from new to needs_review.


---

Attachment

(I didn't check `conf.py` for the other documents, but they build with just the usual warnings, so I don't think we need to modify them.)


---

Comment by mpatel created at 2010-02-02 03:11:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-02 04:15:02

Resolution: fixed
