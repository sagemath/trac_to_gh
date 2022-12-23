# Issue 8146: building HTML version of French tutorial is broken

archive/issues_008146.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  mpatel\n\nKeywords: French tutorial\n\nTicket #8036 fixes some issues with non-ASCII characters in the reference manual. But it breaks the building of the HTML version of the French tutorial:\n\n```\nsphinx-build -b html -d /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/output/doctrees/fr/tutorial    /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/fr/tutorial /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/output/html/fr/tutorial\nRunning Sphinx v0.6.3\n\nException occurred:\n  File \"/scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/fr/tutorial/conf.py\", line 38, in <module>\n    latex_preamble += '\\\\DeclareUnicodeCharacter{00A0}{\\\\nobreakspace}\\n'\nNameError: name 'latex_preamble' is not defined\nThe full traceback has been saved in /tmp/sphinx-err-6XQBIT.log, if you want to report the issue to the author.\nPlease also report this if it was a user error, so that a better error message can be provided next time.\nSend reports to sphinx-dev@googlegroups.com. Thanks!\nBuild finished.  The built documents can be found in /scratch/mvngu/release/sage-4.3.2.alpha1/devel/sage/doc/output/html/fr/tutorial\n```\n\nThis is due to the deletion of the line\n\n```\nlatex_preamble = '\\usepackage{amsmath}\\n\\usepackage{amsfonts}\\n' \n```\n\nin [trac_8036-docbuild_utf8x.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8036/trac_8036-docbuild_utf8x.patch). I'm making this a blocker against Sage 4.3.2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8146\n\n",
    "created_at": "2010-02-02T02:02:41Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "title": "building HTML version of French tutorial is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8146",
    "user": "mvngu"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/8146





---

archive/issue_comments_071609.json:
```json
{
    "body": "We need to upgrade `SAGE_DOC/fr/tutorial/conf.py` to use `latex_elements['preamble']` instead of `latex_preamble`, which is [deprecated](http://sphinx.pocoo.org/config.html#confval-latex_preamble).  I'll check the other documents.",
    "created_at": "2010-02-02T02:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8146#issuecomment-71609",
    "user": "mpatel"
}
```

We need to upgrade `SAGE_DOC/fr/tutorial/conf.py` to use `latex_elements['preamble']` instead of `latex_preamble`, which is [deprecated](http://sphinx.pocoo.org/config.html#confval-latex_preamble).  I'll check the other documents.



---

archive/issue_comments_071610.json:
```json
{
    "body": "If I either delete the last few lines of `SAGE_DOC/fr/tutorial/conf.py` -- the ones dealing with `latex_preamble` -- or if I replace them with lines using `latex_elements['preamble']` instead, the build seems to go through either way.  I suppose the second option is closer to what we have now, so we should use that?  Here's a patch.",
    "created_at": "2010-02-02T02:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8146#issuecomment-71610",
    "user": "jhpalmieri"
}
```

If I either delete the last few lines of `SAGE_DOC/fr/tutorial/conf.py` -- the ones dealing with `latex_preamble` -- or if I replace them with lines using `latex_elements['preamble']` instead, the build seems to go through either way.  I suppose the second option is closer to what we have now, so we should use that?  Here's a patch.



---

archive/issue_comments_071611.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-02T02:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8146#issuecomment-71611",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071612.json:
```json
{
    "body": "Attachment\n\n(I didn't check `conf.py` for the other documents, but they build with just the usual warnings, so I don't think we need to modify them.)",
    "created_at": "2010-02-02T02:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8146#issuecomment-71612",
    "user": "jhpalmieri"
}
```

Attachment

(I didn't check `conf.py` for the other documents, but they build with just the usual warnings, so I don't think we need to modify them.)



---

archive/issue_comments_071613.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-02T03:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8146#issuecomment-71613",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071614.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T04:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8146#issuecomment-71614",
    "user": "mvngu"
}
```

Resolution: fixed
