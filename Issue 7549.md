# Issue 7549: Reference manual: class hierarchy, inherited members, underscore variables

archive/issues_007549.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @hivert @jhpalmieri @nthiery mvngu @jasongrout\n\nIn the Sage reference manual, it might be useful to\n\n* List the base classes for a class.\n* List inherited members but not their docstrings.\n* Include docstrings for \"private\" variables (e.g., `__init__`, `_foo`).\n* Include inheritance diagrams.\n\nSphinx extensions of interest: [autodoc](http://sphinx.pocoo.org/ext/autodoc.html), [inheritance_diagram](http://sphinx.pocoo.org/ext/inheritance.html).\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a34a80097ad47805/2e57eb60d7f9881d?#2e57eb60d7f9881d) for some discussions.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7549\n\n",
    "created_at": "2009-11-28T13:42:38Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Reference manual: class hierarchy, inherited members, underscore variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7549",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @hivert @jhpalmieri @nthiery mvngu @jasongrout

In the Sage reference manual, it might be useful to

* List the base classes for a class.
* List inherited members but not their docstrings.
* Include docstrings for "private" variables (e.g., `__init__`, `_foo`).
* Include inheritance diagrams.

Sphinx extensions of interest: [autodoc](http://sphinx.pocoo.org/ext/autodoc.html), [inheritance_diagram](http://sphinx.pocoo.org/ext/inheritance.html).

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a34a80097ad47805/2e57eb60d7f9881d?#2e57eb60d7f9881d) for some discussions.

Issue created by migration from https://trac.sagemath.org/ticket/7549





---

archive/issue_comments_064005.json:
```json
{
    "body": "Attachment [trac_7549-doc_inheritance_underscore.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore.patch) by @qed777 created at 2009-11-28 13:55:05\n\nDoc build options for inherited members, private variables.  Inheritance diagrams.  Apply to sage repo.",
    "created_at": "2009-11-28T13:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64005",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7549-doc_inheritance_underscore.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore.patch) by @qed777 created at 2009-11-28 13:55:05

Doc build options for inherited members, private variables.  Inheritance diagrams.  Apply to sage repo.



---

archive/issue_comments_064006.json:
```json
{
    "body": "The patch, which may depend weakly on #7473's \"builder\" patch,\n\n* Adds a `sage -docbuild` option `-i` to include inherited members, mostly without docstrings.\n\n* Adds a `sage -docbuild` option `-u` to include \"private\" variables.\n\n* Uses Sphinx's `:show-inheritance:` [autodoc](http://sphinx.pocoo.org/ext/autodoc.html) option to list the base classes of a class.\n\n* Sets up Sphinx's [inheritance_diagram](http://sphinx.pocoo.org/ext/inheritance.html) extension.  See [attachment:inheritance_example.patch:ticket:6586 this attachment] for an example.  This requires [Graphviz](http://www.graphviz.org/).\n\nIt's likely that the attached patch needs work.  In particular, `sage.doc.common.conf.process_inherited` would benefit from expert intervention.\n\nNote: To force a rebuild when toggling `-u`, add `-S -aE` to the command-line.  For example,\n\n```\nsage -docbuild reference html -juv3 -S -aE\n```\n\nToggling `-i` should automatically trigger a rebuild.",
    "created_at": "2009-11-28T14:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64006",
    "user": "https://github.com/qed777"
}
```

The patch, which may depend weakly on #7473's "builder" patch,

* Adds a `sage -docbuild` option `-i` to include inherited members, mostly without docstrings.

* Adds a `sage -docbuild` option `-u` to include "private" variables.

* Uses Sphinx's `:show-inheritance:` [autodoc](http://sphinx.pocoo.org/ext/autodoc.html) option to list the base classes of a class.

* Sets up Sphinx's [inheritance_diagram](http://sphinx.pocoo.org/ext/inheritance.html) extension.  See [attachment:inheritance_example.patch:ticket:6586 this attachment] for an example.  This requires [Graphviz](http://www.graphviz.org/).

It's likely that the attached patch needs work.  In particular, `sage.doc.common.conf.process_inherited` would benefit from expert intervention.

Note: To force a rebuild when toggling `-u`, add `-S -aE` to the command-line.  For example,

```
sage -docbuild reference html -juv3 -S -aE
```

Toggling `-i` should automatically trigger a rebuild.



---

archive/issue_comments_064007.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-28T14:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64007",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064008.json:
```json
{
    "body": "Running\n\n```\nsage -docbuild reference html -juiv3\n```\n\nI encountered\n\n```\nreading sources... [ 27%] sage/combinat/lyndon_wordtor_weightedturesnssis_basis\nSphinx error:\n'ascii' codec can't decode byte 0xc3 in position 811: ordinal not in range(128)\n```\n\nAre #6674 and #6682 relevant?",
    "created_at": "2009-11-28T14:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64008",
    "user": "https://github.com/qed777"
}
```

Running

```
sage -docbuild reference html -juiv3
```

I encountered

```
reading sources... [ 27%] sage/combinat/lyndon_wordtor_weightedturesnssis_basis
Sphinx error:
'ascii' codec can't decode byte 0xc3 in position 811: ordinal not in range(128)
```

Are #6674 and #6682 relevant?



---

archive/issue_comments_064009.json:
```json
{
    "body": "Putting\n\n```\n# -*- coding: utf-8 -*-                                                         \n```\n\nat the beginning of `sage.combinat.lyndon_word` seems to placate Sphinx.\n\nShould we do this with every Sage library .py and .pyx file?",
    "created_at": "2009-11-28T16:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64009",
    "user": "https://github.com/qed777"
}
```

Putting

```
# -*- coding: utf-8 -*-                                                         
```

at the beginning of `sage.combinat.lyndon_word` seems to placate Sphinx.

Should we do this with every Sage library .py and .pyx file?



---

archive/issue_comments_064010.json:
```json
{
    "body": "After adding the \"utf-8\" line to lyndon_word.py, I got this error:\n\n```\nreading sources... [ 51%] sage/interfaces/singular                 ismsm\nreST markup error:\n/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/singular.py:docstring of sage.interfaces.singular.SingularFunctionElement._sage_doc_:8: (SEVERE/4) Unexpected section title.\n```\n\nAfter fixing this (by ripping out a doctest), things built fine.  The html version of the reference manual looks good, and seems to have all of the methods we want, with the inherited ones having no docstrings.  \n\nHere are some timings on my iMac.  Between each build, I removed the directory doc/output:\n\n```\nsage -docbuild reference html -j        11 minutes\nsage -docbuild reference html -ji       22 minutes\nsage -docbuild reference html -ju      13 minutes\nsage -docbuild reference html -jiu     63 minutes!\n```\n\nAlso\n\n```\nsage -docbuild reference pdf -iu  \n```\n\ntook too long on my iMac.  On sage.math, it took about 2 hours and then bombed when trying to run pdflatex: there was one error (a missing \"r\" before a triple-quoted docstring with backslashes); once this was fixed, it ran for a while and then said\n\n```\n! TeX capacity exceeded, sorry [pool size=1165810].\n```\n\nI don't know if there is a way of fixing this, short of #6495.  (I think that the tex installation on sage.math is somewhat old, which doesn't help.)",
    "created_at": "2009-11-29T05:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64010",
    "user": "https://github.com/jhpalmieri"
}
```

After adding the "utf-8" line to lyndon_word.py, I got this error:

```
reading sources... [ 51%] sage/interfaces/singular                 ismsm
reST markup error:
/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/singular.py:docstring of sage.interfaces.singular.SingularFunctionElement._sage_doc_:8: (SEVERE/4) Unexpected section title.
```

After fixing this (by ripping out a doctest), things built fine.  The html version of the reference manual looks good, and seems to have all of the methods we want, with the inherited ones having no docstrings.  

Here are some timings on my iMac.  Between each build, I removed the directory doc/output:

```
sage -docbuild reference html -j        11 minutes
sage -docbuild reference html -ji       22 minutes
sage -docbuild reference html -ju      13 minutes
sage -docbuild reference html -jiu     63 minutes!
```

Also

```
sage -docbuild reference pdf -iu  
```

took too long on my iMac.  On sage.math, it took about 2 hours and then bombed when trying to run pdflatex: there was one error (a missing "r" before a triple-quoted docstring with backslashes); once this was fixed, it ran for a while and then said

```
! TeX capacity exceeded, sorry [pool size=1165810].
```

I don't know if there is a way of fixing this, short of #6495.  (I think that the tex installation on sage.math is somewhat old, which doesn't help.)



---

archive/issue_comments_064011.json:
```json
{
    "body": "I have yet to succeed making a pdf version of the reference manual.  On the two machines I've tried, it takes ages and then crashes with \"TeX capacity exceeded\".  This happened just with the \"-i\" option on my iMac.  I haven't tried all of the possibilities on all of the machines.\n\nSo I wonder if it makes sense, at least until something like #6495 is in place, to disable the \"-i\" and \"-u\" flags for the pdf version of the manual.  If not disable them, then at least print a warning saying it's going to take a long time and then might very well crash?",
    "created_at": "2009-11-29T06:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64011",
    "user": "https://github.com/jhpalmieri"
}
```

I have yet to succeed making a pdf version of the reference manual.  On the two machines I've tried, it takes ages and then crashes with "TeX capacity exceeded".  This happened just with the "-i" option on my iMac.  I haven't tried all of the possibilities on all of the machines.

So I wonder if it makes sense, at least until something like #6495 is in place, to disable the "-i" and "-u" flags for the pdf version of the manual.  If not disable them, then at least print a warning saying it's going to take a long time and then might very well crash?



---

archive/issue_comments_064012.json:
```json
{
    "body": "Sure, I have no problem with either course.  We could also make `-i` and `-u` \"Advanced\" options.\n\nAside:  I can't even build the HTML manual with `-iu` on my local machine.  It requires too much memory.",
    "created_at": "2009-11-29T07:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64012",
    "user": "https://github.com/qed777"
}
```

Sure, I have no problem with either course.  We could also make `-i` and `-u` "Advanced" options.

Aside:  I can't even build the HTML manual with `-iu` on my local machine.  It requires too much memory.



---

archive/issue_comments_064013.json:
```json
{
    "body": "Maybe we can use Sphinx's [intersphinx extension](http://sphinx.pocoo.org/latest/ext/intersphinx.html) to implement a HTML analogue of #6495?",
    "created_at": "2009-11-29T07:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64013",
    "user": "https://github.com/qed777"
}
```

Maybe we can use Sphinx's [intersphinx extension](http://sphinx.pocoo.org/latest/ext/intersphinx.html) to implement a HTML analogue of #6495?



---

archive/issue_comments_064014.json:
```json
{
    "body": "For links to [Sage tickets](http://trac.sagemath.org/sage_trac), we could use Sphinx's [extlinks extension](http://sphinx.pocoo.org/latest/ext/extlinks.html).",
    "created_at": "2009-11-29T08:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64014",
    "user": "https://github.com/qed777"
}
```

For links to [Sage tickets](http://trac.sagemath.org/sage_trac), we could use Sphinx's [extlinks extension](http://sphinx.pocoo.org/latest/ext/extlinks.html).



---

archive/issue_comments_064015.json:
```json
{
    "body": "> Also\n> {{{\n> sage -docbuild reference pdf -iu  \n> }}}\n> took too long on my iMac.  On sage.math, it took about 2 hours and then bombed when trying to run pdflatex: there was one error (a missing \"r\" before a triple-quoted docstring with backslashes); once this was fixed, it ran for a while and then said\n> {{{\n> ! TeX capacity exceeded, sorry [pool size=1165810].\n> }}}\n> I don't know if there is a way of fixing this, short of #6495.  (I think that the tex installation on sage.math is somewhat old, which doesn't help.)\n> \nDid you try to launch lex with more memory ? I remember doing a \n\n```\nexport extra_mem_bot=8000000; latex ...\n```\n\nin a similar situation.",
    "created_at": "2009-11-29T08:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64015",
    "user": "https://github.com/hivert"
}
```

> Also
> {{{
> sage -docbuild reference pdf -iu  
> }}}
> took too long on my iMac.  On sage.math, it took about 2 hours and then bombed when trying to run pdflatex: there was one error (a missing "r" before a triple-quoted docstring with backslashes); once this was fixed, it ran for a while and then said
> {{{
> ! TeX capacity exceeded, sorry [pool size=1165810].
> }}}
> I don't know if there is a way of fixing this, short of #6495.  (I think that the tex installation on sage.math is somewhat old, which doesn't help.)
> 
Did you try to launch lex with more memory ? I remember doing a 

```
export extra_mem_bot=8000000; latex ...
```

in a similar situation.



---

archive/issue_comments_064016.json:
```json
{
    "body": "Set up intersphinx for Python docs.  *Replaces* previous patch. sage repo.",
    "created_at": "2009-11-29T09:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64016",
    "user": "https://github.com/qed777"
}
```

Set up intersphinx for Python docs.  *Replaces* previous patch. sage repo.



---

archive/issue_comments_064017.json:
```json
{
    "body": "Attachment [trac_7549-doc_inheritance_underscore_v2.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v2.patch) by @qed777 created at 2009-11-29 09:11:42\n\nVersion 2, which replaces the previous patch,\n\n* Enables `intersphinx` for the Python docs.  This is *easy* to use, e.g.,\n\n```\nFor more information, please consult :mod:`subprocess`.  Blah, blah, whatever...\n```\n\n* Adds `# -*- coding: utf-8 -*-` to the top of `sage.combinat.lyndon_word`.\n* Drops a `sage.interfaces.singular.SingularFunctionElement._sage_doc_` doctest.\n* Prepares for `extlinks`.  Sphinx 1.0 will include this new extension.",
    "created_at": "2009-11-29T09:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64017",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7549-doc_inheritance_underscore_v2.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v2.patch) by @qed777 created at 2009-11-29 09:11:42

Version 2, which replaces the previous patch,

* Enables `intersphinx` for the Python docs.  This is *easy* to use, e.g.,

```
For more information, please consult :mod:`subprocess`.  Blah, blah, whatever...
```

* Adds `# -*- coding: utf-8 -*-` to the top of `sage.combinat.lyndon_word`.
* Drops a `sage.interfaces.singular.SingularFunctionElement._sage_doc_` doctest.
* Prepares for `extlinks`.  Sphinx 1.0 will include this new extension.



---

archive/issue_comments_064018.json:
```json
{
    "body": "It seems that `:show-inheritance:` shows just the immediate super classes, not the entire hierarchy.  I do not know whether this is easy to change.",
    "created_at": "2009-11-29T09:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64018",
    "user": "https://github.com/qed777"
}
```

It seems that `:show-inheritance:` shows just the immediate super classes, not the entire hierarchy.  I do not know whether this is easy to change.



---

archive/issue_comments_064019.json:
```json
{
    "body": "Please see #6495 for progress on incrementally building the reference manual.",
    "created_at": "2009-11-29T19:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64019",
    "user": "https://github.com/qed777"
}
```

Please see #6495 for progress on incrementally building the reference manual.



---

archive/issue_comments_064020.json:
```json
{
    "body": "Rebased for 4.3.alpha1.  Replaces previous patches.",
    "created_at": "2009-12-04T08:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64020",
    "user": "https://github.com/qed777"
}
```

Rebased for 4.3.alpha1.  Replaces previous patches.



---

archive/issue_comments_064021.json:
```json
{
    "body": "Attachment [trac_7549-doc_inheritance_underscore_v3.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v3.patch) by @qed777 created at 2009-12-06 00:38:58\n\nI should add that we can also link directly to [matplotlib's docs](http://matplotlib.sourceforge.net/contents.html) from the Sage documentation.  We just need to update `doc.common.conf.intersphinx_mapping` (the object inventory is [here](http://matplotlib.sourceforge.net/objects.inv)).  Perhaps there are others of interest in [this list](http://sphinx.pocoo.org/examples.html)?",
    "created_at": "2009-12-06T00:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64021",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7549-doc_inheritance_underscore_v3.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v3.patch) by @qed777 created at 2009-12-06 00:38:58

I should add that we can also link directly to [matplotlib's docs](http://matplotlib.sourceforge.net/contents.html) from the Sage documentation.  We just need to update `doc.common.conf.intersphinx_mapping` (the object inventory is [here](http://matplotlib.sourceforge.net/objects.inv)).  Perhaps there are others of interest in [this list](http://sphinx.pocoo.org/examples.html)?



---

archive/issue_comments_064022.json:
```json
{
    "body": "Against 4.3.2.alpha1:\n\n```\napplying trac_7549-doc_inheritance_underscore_v3.patch\npatching file doc/common/conf.py\nHunk #5 succeeded at 378 with fuzz 2 (offset 5 lines).\nnow at: trac_7549-doc_inheritance_underscore_v3.patch\n```\n",
    "created_at": "2010-02-01T09:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64022",
    "user": "https://github.com/qed777"
}
```

Against 4.3.2.alpha1:

```
applying trac_7549-doc_inheritance_underscore_v3.patch
patching file doc/common/conf.py
Hunk #5 succeeded at 378 with fuzz 2 (offset 5 lines).
now at: trac_7549-doc_inheritance_underscore_v3.patch
```




---

archive/issue_comments_064023.json:
```json
{
    "body": "Replying to [comment:14 mpatel]:\n> I should add that we can also link directly to [matplotlib's docs](http://matplotlib.sourceforge.net/contents.html) from the Sage documentation.  We just need to update `doc.common.conf.intersphinx_mapping` (the object inventory is [here](http://matplotlib.sourceforge.net/objects.inv)).  Perhaps there are others of interest in [this list](http://sphinx.pocoo.org/examples.html)?\n\nCython, mpmath, and Sphinx are possibilities.  Building Sage shouldn't rely on an internet connection, though, and it seems to me that intersphinx does.  So should we also include the object inventories so that we can build the docs without an internet connection?  This would rely on keeping those up to date.  Can we have it check for an internet connection and fail gracefully if there isn't one?\n\nRight now I don't know what I'm doing wrong, but I can't get private methods to be included in the docs.  This is with 4.3.2.  I put in a print statement in `skip_underscore` to make sure it was finding the correct methods, and it was.  But I didn't see them in the documentation afterwards.  I'll try again later.",
    "created_at": "2010-02-09T00:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64023",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:14 mpatel]:
> I should add that we can also link directly to [matplotlib's docs](http://matplotlib.sourceforge.net/contents.html) from the Sage documentation.  We just need to update `doc.common.conf.intersphinx_mapping` (the object inventory is [here](http://matplotlib.sourceforge.net/objects.inv)).  Perhaps there are others of interest in [this list](http://sphinx.pocoo.org/examples.html)?

Cython, mpmath, and Sphinx are possibilities.  Building Sage shouldn't rely on an internet connection, though, and it seems to me that intersphinx does.  So should we also include the object inventories so that we can build the docs without an internet connection?  This would rely on keeping those up to date.  Can we have it check for an internet connection and fail gracefully if there isn't one?

Right now I don't know what I'm doing wrong, but I can't get private methods to be included in the docs.  This is with 4.3.2.  I put in a print statement in `skip_underscore` to make sure it was finding the correct methods, and it was.  But I didn't see them in the documentation afterwards.  I'll try again later.



---

archive/issue_comments_064024.json:
```json
{
    "body": "Rebased vs. 4.3.3.alpha0.  See comment.  Apply only this patch.  sage repo.",
    "created_at": "2010-02-14T08:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64024",
    "user": "https://github.com/qed777"
}
```

Rebased vs. 4.3.3.alpha0.  See comment.  Apply only this patch.  sage repo.



---

archive/issue_comments_064025.json:
```json
{
    "body": "Attachment [trac_7549-doc_inheritance_underscore_v4.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v4.patch) by @qed777 created at 2010-02-14 08:44:20\n\nV4\n\n* Rebased vs. 4.3.3.alpha0.\n* Combines the skip member handlers, since Sphinx takes the first answer that's not `None`.  (I suppose we could keep them separate but return `None` when a test is inconclusive).\n* Detects changes in `-u`, too.  Toggling either new option should trigger a rebuild.\n\nShould we move the new options to the \"Advanced\" section?  Add \"may use lots of memory\"?\n\nNote: I still haven't done a complete build in each configuration.",
    "created_at": "2010-02-14T08:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64025",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7549-doc_inheritance_underscore_v4.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v4.patch) by @qed777 created at 2010-02-14 08:44:20

V4

* Rebased vs. 4.3.3.alpha0.
* Combines the skip member handlers, since Sphinx takes the first answer that's not `None`.  (I suppose we could keep them separate but return `None` when a test is inconclusive).
* Detects changes in `-u`, too.  Toggling either new option should trigger a rebuild.

Should we move the new options to the "Advanced" section?  Add "may use lots of memory"?

Note: I still haven't done a complete build in each configuration.



---

archive/issue_comments_064026.json:
```json
{
    "body": "I should add that I've disabled the intersphinx extension, for now.  It [can cache inventories](http://sphinx.pocoo.org/latest/ext/intersphinx.html), but I don't know whether it fails gracefully if the cache has \"expired\" but there's no connection.",
    "created_at": "2010-02-14T09:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64026",
    "user": "https://github.com/qed777"
}
```

I should add that I've disabled the intersphinx extension, for now.  It [can cache inventories](http://sphinx.pocoo.org/latest/ext/intersphinx.html), but I don't know whether it fails gracefully if the cache has "expired" but there's no connection.



---

archive/issue_comments_064027.json:
```json
{
    "body": "The HTML manual builds with `-i`, `-u`, and `-iu`.\n\nBuilding the PDF manual with `-u`\u00a0on sage.math yields\n\n\n```\n[4811] [4812] [4813] [4814] [4815] [4816]\n! TeX capacity exceeded, sorry [pool size=1165811].\n\\Hy@pstringdef ...->\\edef #1{\\pdfescapestring {#2}\n                                                  }\nl.392012 ...matrix0.Matrix.multiplicative_order}{}\n                                                  \\begin{methoddesc}{multipl...\n\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on reference.log.\nmake: *** [reference.pdf] Error 1\n```\n\nafter I suppress problems with underscored methods in\n\n* sagenb.notebook.worksheet\n* structure.formal_sum\n* sage.combinat.crystals.tensor_product\n* sage.combinat.species.set_species\n* sage.combinat.words.word_generators\n* sage.rings.number_field.number_field\n* sage.rings.number_field.number_field_ideal\n* sage.rings.polynomial.multi_polynomial_libsingular\n* sage.rings.polynomial.infinite_polynomial_ring\n* sage.rings.polynomial.infinite_polynomial_element\n\nI'll fix the first problem in a separate ticket and leave the others for someone else.",
    "created_at": "2010-02-14T18:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64027",
    "user": "https://github.com/qed777"
}
```

The HTML manual builds with `-i`, `-u`, and `-iu`.

Building the PDF manual with `-u` on sage.math yields


```
[4811] [4812] [4813] [4814] [4815] [4816]
! TeX capacity exceeded, sorry [pool size=1165811].
\Hy@pstringdef ...->\edef #1{\pdfescapestring {#2}
                                                  }
l.392012 ...matrix0.Matrix.multiplicative_order}{}
                                                  \begin{methoddesc}{multipl...

!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on reference.log.
make: *** [reference.pdf] Error 1
```

after I suppress problems with underscored methods in

* sagenb.notebook.worksheet
* structure.formal_sum
* sage.combinat.crystals.tensor_product
* sage.combinat.species.set_species
* sage.combinat.words.word_generators
* sage.rings.number_field.number_field
* sage.rings.number_field.number_field_ideal
* sage.rings.polynomial.multi_polynomial_libsingular
* sage.rings.polynomial.infinite_polynomial_ring
* sage.rings.polynomial.infinite_polynomial_element

I'll fix the first problem in a separate ticket and leave the others for someone else.



---

archive/issue_comments_064028.json:
```json
{
    "body": "I get the html manual to build, too, although with 1517 warnings when built with \"-u\", and more than 28,000 warnings with \"-iu\": either because the docstrings for underscore methods are sloppily formatted (not a surprise) or messages along the lines of those in #8244.\n\nI noticed that after I built with \"-j -iu\", edited a few files and ran \"sage -b\", then when I built the manual again with \"-j -iu\", in the \"reading sources\" portion of the build, it only processes the changed files, but in the \"writing output\" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?\n\nI haven't had the time to try a pdf build yet, but I'll work on that later today.",
    "created_at": "2010-02-17T16:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64028",
    "user": "https://github.com/jhpalmieri"
}
```

I get the html manual to build, too, although with 1517 warnings when built with "-u", and more than 28,000 warnings with "-iu": either because the docstrings for underscore methods are sloppily formatted (not a surprise) or messages along the lines of those in #8244.

I noticed that after I built with "-j -iu", edited a few files and ran "sage -b", then when I built the manual again with "-j -iu", in the "reading sources" portion of the build, it only processes the changed files, but in the "writing output" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?

I haven't had the time to try a pdf build yet, but I'll work on that later today.



---

archive/issue_comments_064029.json:
```json
{
    "body": "Now I've tried building the pdf, and I run into the same \"TeX capacity exceeded\" message.  I've tried altering \"extra_mem_top\" and \"extra_mem_bot\", but it's not helping.  (I may not be doing this right, though.)\n\nI had to fix more problems to get the PDF to build: everywhere there was an email address, pdflatex was crashing on the `@` sign, so I had to enclose the address in double backquotes.  So I ended up changing these files (in addition to sagenb.notebook.worksheet: I applied the patch from #8265 to deal with this one):\n\n* sage/combinat/species/set_species.py\n* sage/combinat/words/word_generators.py\n* sage/misc/hg.py\n* sage/misc/lazy_attribute.py\n* sage/misc/preparser.py\n* sage/rings/number_field/number_field.py\n* sage/rings/number_field/number_field_ideal.py\n* sage/rings/padics/padic_generic.py\n* sage/rings/padics/tutorial.py\n* sage/rings/polynomial/infinite_polynomial_element.py\n* sage/rings/polynomial/infinite_polynomial_ring.py\n* sage/rings/polynomial/multi_polynomial_libsingular.pyx\n* sage/rings/polynomial/pbori.pyx\n* sage/rings/polynomial/symmetric_ideal.py\n* sage/rings/polynomial/symmetric_reduction.pyx\n* sage/structure/formal_sum.py\n* sage/structure/sequence.py\n\nI don't think that fixing these is a high priority, since the PDF manual doesn't build anyway with the \"-u\" option.\n\n--------\n\nAside from my question about why \"-iu\" rewrites all of the output when it shouldn't have to, I'm happy with this.  (I haven't tested this with \"-i\" or \"-u\".)  I agree that there should be a comment about \"-i\" and \"-u\" taking a lot of memory, and perhaps saying that they don't work with the pdf build.  I don't think they need to be in the \"advanced\" options.",
    "created_at": "2010-02-17T23:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64029",
    "user": "https://github.com/jhpalmieri"
}
```

Now I've tried building the pdf, and I run into the same "TeX capacity exceeded" message.  I've tried altering "extra_mem_top" and "extra_mem_bot", but it's not helping.  (I may not be doing this right, though.)

I had to fix more problems to get the PDF to build: everywhere there was an email address, pdflatex was crashing on the `@` sign, so I had to enclose the address in double backquotes.  So I ended up changing these files (in addition to sagenb.notebook.worksheet: I applied the patch from #8265 to deal with this one):

* sage/combinat/species/set_species.py
* sage/combinat/words/word_generators.py
* sage/misc/hg.py
* sage/misc/lazy_attribute.py
* sage/misc/preparser.py
* sage/rings/number_field/number_field.py
* sage/rings/number_field/number_field_ideal.py
* sage/rings/padics/padic_generic.py
* sage/rings/padics/tutorial.py
* sage/rings/polynomial/infinite_polynomial_element.py
* sage/rings/polynomial/infinite_polynomial_ring.py
* sage/rings/polynomial/multi_polynomial_libsingular.pyx
* sage/rings/polynomial/pbori.pyx
* sage/rings/polynomial/symmetric_ideal.py
* sage/rings/polynomial/symmetric_reduction.pyx
* sage/structure/formal_sum.py
* sage/structure/sequence.py

I don't think that fixing these is a high priority, since the PDF manual doesn't build anyway with the "-u" option.

--------

Aside from my question about why "-iu" rewrites all of the output when it shouldn't have to, I'm happy with this.  (I haven't tested this with "-i" or "-u".)  I agree that there should be a comment about "-i" and "-u" taking a lot of memory, and perhaps saying that they don't work with the pdf build.  I don't think they need to be in the "advanced" options.



---

archive/issue_comments_064030.json:
```json
{
    "body": "Hi ! \n\nJust to make you aware of #7448 (Sphinx rendering of nested classes) which is related. Notice that our patches certainly do not commute but rebasing should be trivial. \n\nCheers,\n\nFlorent",
    "created_at": "2010-02-18T00:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64030",
    "user": "https://github.com/hivert"
}
```

Hi ! 

Just to make you aware of #7448 (Sphinx rendering of nested classes) which is related. Notice that our patches certainly do not commute but rebasing should be trivial. 

Cheers,

Florent



---

archive/issue_comments_064031.json:
```json
{
    "body": "Replying to [comment:20 jhpalmieri]:\n\n> I noticed that after I built with \"-j -iu\", edited a few files and ran \"sage -b\", then when I built the manual again with \"-j -iu\", in the \"reading sources\" portion of the build, it only processes the changed files, but in the \"writing output\" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?\n\nI've also seen this behavior, but I've been unable reproduce it with certainty --- at least, with a version of #6187's ['\"testreference\" patch'](http://trac.sagemath.org/sage_trac/attachment/ticket/6187/trac_6187_testreference.patch).  Are there particular types of changes that usually trigger the problem?\n\nI don't think Sphinx is especially smart about updating files affected by a change in other files, but this may be irrelevant.",
    "created_at": "2010-02-18T23:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64031",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:20 jhpalmieri]:

> I noticed that after I built with "-j -iu", edited a few files and ran "sage -b", then when I built the manual again with "-j -iu", in the "reading sources" portion of the build, it only processes the changed files, but in the "writing output" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?

I've also seen this behavior, but I've been unable reproduce it with certainty --- at least, with a version of #6187's ['"testreference" patch'](http://trac.sagemath.org/sage_trac/attachment/ticket/6187/trac_6187_testreference.patch).  Are there particular types of changes that usually trigger the problem?

I don't think Sphinx is especially smart about updating files affected by a change in other files, but this may be irrelevant.



---

archive/issue_comments_064032.json:
```json
{
    "body": "To do: Rebase the patch against 4.3.3.alpha1 + #8244 + #7448.",
    "created_at": "2010-02-20T21:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64032",
    "user": "https://github.com/qed777"
}
```

To do: Rebase the patch against 4.3.3.alpha1 + #8244 + #7448.



---

archive/issue_comments_064033.json:
```json
{
    "body": "Replying to [comment:23 mpatel]:\n> Replying to [comment:20 jhpalmieri]:\n> \n> > I noticed that after I built with \"-j -iu\", edited a few files and ran \"sage -b\", then when I built the manual again with \"-j -iu\", in the \"reading sources\" portion of the build, it only processes the changed files, but in the \"writing output\" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?\n> \n> I've also seen this behavior, but I've been unable reproduce it with certainty --- at least, with a version of #6187's ['\"testreference\" patch'](http://trac.sagemath.org/sage_trac/attachment/ticket/6187/trac_6187_testreference.patch).  Are there particular types of changes that usually trigger the problem?\n\nI'm not sure, but I just saw this message at the beginning of a docbuild:\n\n```\nWARNING: unsupported build info format in '/Applications/sage/devel/sage/doc/output/html/en/reference/.buildinfo', building all\n```\n",
    "created_at": "2010-02-24T22:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64033",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:23 mpatel]:
> Replying to [comment:20 jhpalmieri]:
> 
> > I noticed that after I built with "-j -iu", edited a few files and ran "sage -b", then when I built the manual again with "-j -iu", in the "reading sources" portion of the build, it only processes the changed files, but in the "writing output" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?
> 
> I've also seen this behavior, but I've been unable reproduce it with certainty --- at least, with a version of #6187's ['"testreference" patch'](http://trac.sagemath.org/sage_trac/attachment/ticket/6187/trac_6187_testreference.patch).  Are there particular types of changes that usually trigger the problem?

I'm not sure, but I just saw this message at the beginning of a docbuild:

```
WARNING: unsupported build info format in '/Applications/sage/devel/sage/doc/output/html/en/reference/.buildinfo', building all
```




---

archive/issue_comments_064034.json:
```json
{
    "body": "I've seen this message, too.  It *might* be a Sphinx bug.\n\nThe HTML builder writes a hash of the `html_*` settings to `.buildinfo` in the output directory.  It appears that [StandaloneHTMLBuilder.get_outdated_docs](http://bitbucket.org/birkenfeld/sphinx/src/tip/sphinx/builders/html.py#cl-144) contains nearly all of the relevant code.\n\nIf, for some reason, this `get_outdated_docs` doesn't get called, the builder writes empty strings for the hashes.  For example, `sage -docbuild reference html -j -S -a` does this (`-a` tells Sphinx to write all files).  The next build attempt triggers the warning.\n\nBut I don't know if this is responsible for what we see.",
    "created_at": "2010-02-25T08:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64034",
    "user": "https://github.com/qed777"
}
```

I've seen this message, too.  It *might* be a Sphinx bug.

The HTML builder writes a hash of the `html_*` settings to `.buildinfo` in the output directory.  It appears that [StandaloneHTMLBuilder.get_outdated_docs](http://bitbucket.org/birkenfeld/sphinx/src/tip/sphinx/builders/html.py#cl-144) contains nearly all of the relevant code.

If, for some reason, this `get_outdated_docs` doesn't get called, the builder writes empty strings for the hashes.  For example, `sage -docbuild reference html -j -S -a` does this (`-a` tells Sphinx to write all files).  The next build attempt triggers the warning.

But I don't know if this is responsible for what we see.



---

archive/issue_comments_064035.json:
```json
{
    "body": "Attachment [trac_7549-doc_inheritance_underscore_v5.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v5.patch) by @qed777 created at 2010-03-11 06:21:32\n\nRebase vs. 4.3.4.alpha1 + #8457.  Apply only this patch.",
    "created_at": "2010-03-11T06:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64035",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7549-doc_inheritance_underscore_v5.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v5.patch) by @qed777 created at 2010-03-11 06:21:32

Rebase vs. 4.3.4.alpha1 + #8457.  Apply only this patch.



---

archive/issue_comments_064036.json:
```json
{
    "body": "V5 is rebased for 4.3.4.alpha1 + #8457.  I'm not sure what we should do about the many `-iu` warnings.  Should we handle them in `sage_getargspec` or in `conf`?",
    "created_at": "2010-03-11T06:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64036",
    "user": "https://github.com/qed777"
}
```

V5 is rebased for 4.3.4.alpha1 + #8457.  I'm not sure what we should do about the many `-iu` warnings.  Should we handle them in `sage_getargspec` or in `conf`?



---

archive/issue_comments_064037.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-12T23:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64037",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064038.json:
```json
{
    "body": "If I run `sage -docbuild reference html -i`, I get\n\n```\nreading sources... [  8%] sage/algebras/iwahori_hecke_algebra_element\nException occurred:\n  File \"/Applications/sage/devel/sage/doc/common/conf.py\", line 354, in skip_member\n    if 'SAGE_CHECK_NESTED' in os.environ:\nRuntimeError: maximum recursion depth exceeded\nThe full traceback has been saved in ...\n```\n\nI scanned the traceback but didn't see anything obviously helpful.\n\nBy the way, I think we can put back the doctest from interfaces/singular.py, by changing the triple quotes at the beginning of the docstring to `r\"\"\"`.  The attached patch does this.\n\nAlso, I used all of the extra error messages to figure out where the warnings\n\n```\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n```\n\nwere coming from, and the attached patch fixes the problems.  So now, combined with #8457, I get no error messages when building the reference manual (without the -i or -u switches, of course).\n\nFor the new warnings when building with -i or -u or -iu, I say we deal with them on another ticket.  It's a big job revising all of the docstrings for underscore functions so that they are in proper reST format.  (Also, right now they're useful -- see the previous paragraph. :)\n\nFinally, do we want some sort of warning for the -i switch, and possibly the -u switch?  (\"may be slow, may not be compatible with PDF output\" as part of its help string, for example)?",
    "created_at": "2010-03-12T23:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64038",
    "user": "https://github.com/jhpalmieri"
}
```

If I run `sage -docbuild reference html -i`, I get

```
reading sources... [  8%] sage/algebras/iwahori_hecke_algebra_element
Exception occurred:
  File "/Applications/sage/devel/sage/doc/common/conf.py", line 354, in skip_member
    if 'SAGE_CHECK_NESTED' in os.environ:
RuntimeError: maximum recursion depth exceeded
The full traceback has been saved in ...
```

I scanned the traceback but didn't see anything obviously helpful.

By the way, I think we can put back the doctest from interfaces/singular.py, by changing the triple quotes at the beginning of the docstring to `r"""`.  The attached patch does this.

Also, I used all of the extra error messages to figure out where the warnings

```
<autodoc>:0: (ERROR/3) Unexpected indentation.
```

were coming from, and the attached patch fixes the problems.  So now, combined with #8457, I get no error messages when building the reference manual (without the -i or -u switches, of course).

For the new warnings when building with -i or -u or -iu, I say we deal with them on another ticket.  It's a big job revising all of the docstrings for underscore functions so that they are in proper reST format.  (Also, right now they're useful -- see the previous paragraph. :)

Finally, do we want some sort of warning for the -i switch, and possibly the -u switch?  ("may be slow, may not be compatible with PDF output" as part of its help string, for example)?



---

archive/issue_comments_064039.json:
```json
{
    "body": "(You may need to apply #8511 to get rid of one of the \"unexpected indentation\" warnings.)",
    "created_at": "2010-03-12T23:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64039",
    "user": "https://github.com/jhpalmieri"
}
```

(You may need to apply #8511 to get rid of one of the "unexpected indentation" warnings.)



---

archive/issue_comments_064040.json:
```json
{
    "body": "On second thought, I moved the \"unexpected indentation\" fix to ticket #8511, so the \"small fixes\" patch just reinstates the interfaces/singular.py doctest.",
    "created_at": "2010-03-12T23:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64040",
    "user": "https://github.com/jhpalmieri"
}
```

On second thought, I moved the "unexpected indentation" fix to ticket #8511, so the "small fixes" patch just reinstates the interfaces/singular.py doctest.



---

archive/issue_comments_064041.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2010-03-12T23:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64041",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of other patch



---

archive/issue_comments_064042.json:
```json
{
    "body": "Attachment [trac_7549-doc_inheritance_underscore_v6.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v6.patch) by @qed777 created at 2010-03-13 08:27:04\n\nFix recursion problem.  Apply only this combined patch.",
    "created_at": "2010-03-13T08:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64042",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7549-doc_inheritance_underscore_v6.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v6.patch) by @qed777 created at 2010-03-13 08:27:04

Fix recursion problem.  Apply only this combined patch.



---

archive/issue_comments_064043.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-13T08:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64043",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064044.json:
```json
{
    "body": "I broke the module check in #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.4.patch V4] when I made #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.5.patch V5].  I apologize for that.  I've restored Florent's code and folded in the small fixes patch in this ticket's V6.",
    "created_at": "2010-03-13T08:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64044",
    "user": "https://github.com/qed777"
}
```

I broke the module check in #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.4.patch V4] when I made #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.5.patch V5].  I apologize for that.  I've restored Florent's code and folded in the small fixes patch in this ticket's V6.



---

archive/issue_comments_064045.json:
```json
{
    "body": "The only change is in `sage_autodoc.py`.",
    "created_at": "2010-03-13T08:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64045",
    "user": "https://github.com/qed777"
}
```

The only change is in `sage_autodoc.py`.



---

archive/issue_comments_064046.json:
```json
{
    "body": "Attachment [trac_7549-doc_inheritance_underscore_v7.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v7.patch) by @qed777 created at 2010-03-13 09:01:03\n\nHelp notes.  Replaces V6.",
    "created_at": "2010-03-13T09:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64046",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7549-doc_inheritance_underscore_v7.patch](tarball://root/attachments/some-uuid/ticket7549/trac_7549-doc_inheritance_underscore_v7.patch) by @qed777 created at 2010-03-13 09:01:03

Help notes.  Replaces V6.



---

archive/issue_comments_064047.json:
```json
{
    "body": "Replying to [comment:31 mpatel]:\n> I broke the module check in #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.4.patch V4] when I made #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.5.patch V5].  I apologize for that.  I've restored Florent's code and folded in the small fixes patch in this ticket's V6.  \n\nHi Mitesh ! I don't see any code from me here except a few lines who where already in #7448, and which you decide to improve (thanks by the way). So I don't think I deserve to be in the author.\n\nAlso I'm Ok with reviewing this but they are three more tickets in combinatoric which I committed myself to review. So don't rely on me for reviewing this very soon... However, I'd like to see this merged soon, so if you imagine someone who is willing to review, please ask him. Anyway, thanks for this work. I really this sage's doc is going to greatly improve.",
    "created_at": "2010-03-13T09:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64047",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:31 mpatel]:
> I broke the module check in #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.4.patch V4] when I made #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.5.patch V5].  I apologize for that.  I've restored Florent's code and folded in the small fixes patch in this ticket's V6.  

Hi Mitesh ! I don't see any code from me here except a few lines who where already in #7448, and which you decide to improve (thanks by the way). So I don't think I deserve to be in the author.

Also I'm Ok with reviewing this but they are three more tickets in combinatoric which I committed myself to review. So don't rely on me for reviewing this very soon... However, I'd like to see this merged soon, so if you imagine someone who is willing to review, please ask him. Anyway, thanks for this work. I really this sage's doc is going to greatly improve.



---

archive/issue_comments_064048.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T18:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64048",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064049.json:
```json
{
    "body": "Sorry for not getting to this sooner.  Positive review.",
    "created_at": "2010-04-05T18:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64049",
    "user": "https://github.com/jhpalmieri"
}
```

Sorry for not getting to this sooner.  Positive review.



---

archive/issue_comments_064050.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_7549-doc_inheritance_underscore_v7.patch",
    "created_at": "2010-04-15T05:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64050",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_7549-doc_inheritance_underscore_v7.patch



---

archive/issue_events_007779.json:
```json
{
    "actor": "@jhpalmieri",
    "created_at": "2010-04-15T05:59:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7549#event-7779"
}
```



---

archive/issue_comments_064051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7549#issuecomment-64051",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
