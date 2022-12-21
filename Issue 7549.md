# Issue 7549: Reference manual: class hierarchy, inherited members, underscore variables

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-11-28 13:42:38

Assignee: mvngu

CC:  hivert jhpalmieri nthiery mvngu jason

In the Sage reference manual, it might be useful to

 * List the base classes for a class.
 * List inherited members but not their docstrings.
 * Include docstrings for "private" variables (e.g., `__init__`, `_foo`).
 * Include inheritance diagrams.

Sphinx extensions of interest: [autodoc](http://sphinx.pocoo.org/ext/autodoc.html), [inheritance_diagram](http://sphinx.pocoo.org/ext/inheritance.html).

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a34a80097ad47805/2e57eb60d7f9881d?#2e57eb60d7f9881d) for some discussions.


---

Attachment

Doc build options for inherited members, private variables.  Inheritance diagrams.  Apply to sage repo.


---

Comment by mpatel created at 2009-11-28 14:20:34

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

Comment by mpatel created at 2009-11-28 14:20:52

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-28 14:30:48

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

Comment by mpatel created at 2009-11-28 16:36:05

Putting

```
# -*- coding: utf-8 -*-                                                         
```

at the beginning of `sage.combinat.lyndon_word` seems to placate Sphinx.

Should we do this with every Sage library .py and .pyx file?


---

Comment by jhpalmieri created at 2009-11-29 05:03:13

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

Comment by jhpalmieri created at 2009-11-29 06:36:56

I have yet to succeed making a pdf version of the reference manual.  On the two machines I've tried, it takes ages and then crashes with "TeX capacity exceeded".  This happened just with the "-i" option on my iMac.  I haven't tried all of the possibilities on all of the machines.

So I wonder if it makes sense, at least until something like #6495 is in place, to disable the "-i" and "-u" flags for the pdf version of the manual.  If not disable them, then at least print a warning saying it's going to take a long time and then might very well crash?


---

Comment by mpatel created at 2009-11-29 07:54:56

Sure, I have no problem with either course.  We could also make `-i` and `-u` "Advanced" options.

Aside:  I can't even build the HTML manual with `-iu` on my local machine.  It requires too much memory.


---

Comment by mpatel created at 2009-11-29 07:59:29

Maybe we can use Sphinx's [intersphinx extension](http://sphinx.pocoo.org/latest/ext/intersphinx.html) to implement a HTML analogue of #6495?


---

Comment by mpatel created at 2009-11-29 08:38:33

For links to [Sage tickets](http://trac.sagemath.org/sage_trac), we could use Sphinx's [extlinks extension](http://sphinx.pocoo.org/latest/ext/extlinks.html).


---

Comment by hivert created at 2009-11-29 08:45:13

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

Comment by mpatel created at 2009-11-29 09:03:37

Set up intersphinx for Python docs.  _Replaces_ previous patch. sage repo.


---

Attachment

Version 2, which replaces the previous patch,

 * Enables `intersphinx` for the Python docs.  This is _easy_ to use, e.g.,

```
For more information, please consult :mod:`subprocess`.  Blah, blah, whatever...
```

 * Adds `# -*- coding: utf-8 -*-` to the top of `sage.combinat.lyndon_word`.
 * Drops a `sage.interfaces.singular.SingularFunctionElement._sage_doc_` doctest.
 * Prepares for `extlinks`.  Sphinx 1.0 will include this new extension.


---

Comment by mpatel created at 2009-11-29 09:29:06

It seems that `:show-inheritance:` shows just the immediate super classes, not the entire hierarchy.  I do not know whether this is easy to change.


---

Comment by mpatel created at 2009-11-29 19:53:39

Please see #6495 for progress on incrementally building the reference manual.


---

Comment by mpatel created at 2009-12-04 08:18:50

Rebased for 4.3.alpha1.  Replaces previous patches.


---

Attachment

I should add that we can also link directly to [matplotlib's docs](http://matplotlib.sourceforge.net/contents.html) from the Sage documentation.  We just need to update `doc.common.conf.intersphinx_mapping` (the object inventory is [here](http://matplotlib.sourceforge.net/objects.inv)).  Perhaps there are others of interest in [this list](http://sphinx.pocoo.org/examples.html)?


---

Comment by mpatel created at 2010-02-01 09:34:33

Against 4.3.2.alpha1:

```
applying trac_7549-doc_inheritance_underscore_v3.patch
patching file doc/common/conf.py
Hunk #5 succeeded at 378 with fuzz 2 (offset 5 lines).
now at: trac_7549-doc_inheritance_underscore_v3.patch
```



---

Comment by jhpalmieri created at 2010-02-09 00:02:25

Replying to [comment:14 mpatel]:
> I should add that we can also link directly to [matplotlib's docs](http://matplotlib.sourceforge.net/contents.html) from the Sage documentation.  We just need to update `doc.common.conf.intersphinx_mapping` (the object inventory is [here](http://matplotlib.sourceforge.net/objects.inv)).  Perhaps there are others of interest in [this list](http://sphinx.pocoo.org/examples.html)?

Cython, mpmath, and Sphinx are possibilities.  Building Sage shouldn't rely on an internet connection, though, and it seems to me that intersphinx does.  So should we also include the object inventories so that we can build the docs without an internet connection?  This would rely on keeping those up to date.  Can we have it check for an internet connection and fail gracefully if there isn't one?

Right now I don't know what I'm doing wrong, but I can't get private methods to be included in the docs.  This is with 4.3.2.  I put in a print statement in `skip_underscore` to make sure it was finding the correct methods, and it was.  But I didn't see them in the documentation afterwards.  I'll try again later.


---

Comment by mpatel created at 2010-02-14 08:22:07

Rebased vs. 4.3.3.alpha0.  See comment.  Apply only this patch.  sage repo.


---

Attachment

V4

 * Rebased vs. 4.3.3.alpha0.
 * Combines the skip member handlers, since Sphinx takes the first answer that's not `None`.  (I suppose we could keep them separate but return `None` when a test is inconclusive).
 * Detects changes in `-u`, too.  Toggling either new option should trigger a rebuild.

Should we move the new options to the "Advanced" section?  Add "may use lots of memory"?

Note: I still haven't done a complete build in each configuration.


---

Comment by mpatel created at 2010-02-14 09:40:03

I should add that I've disabled the intersphinx extension, for now.  It [can cache inventories](http://sphinx.pocoo.org/latest/ext/intersphinx.html), but I don't know whether it fails gracefully if the cache has "expired" but there's no connection.


---

Comment by mpatel created at 2010-02-14 18:23:56

The HTML manual builds with `-i`, `-u`, and `-iu`.

Building the PDF manual with `-u` on sage.math yields


```
[4811] [4812] [4813] [4814] [4815] [4816]
! TeX capacity exceeded, sorry [pool size=1165811].
\Hy`@`pstringdef ...->\edef #1{\pdfescapestring {#2}
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

Comment by jhpalmieri created at 2010-02-17 16:37:21

I get the html manual to build, too, although with 1517 warnings when built with "-u", and more than 28,000 warnings with "-iu": either because the docstrings for underscore methods are sloppily formatted (not a surprise) or messages along the lines of those in #8244.

I noticed that after I built with "-j -iu", edited a few files and ran "sage -b", then when I built the manual again with "-j -iu", in the "reading sources" portion of the build, it only processes the changed files, but in the "writing output" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?

I haven't had the time to try a pdf build yet, but I'll work on that later today.


---

Comment by jhpalmieri created at 2010-02-17 23:20:43

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

Comment by hivert created at 2010-02-18 00:04:18

Hi ! 

Just to make you aware of #7448 (Sphinx rendering of nested classes) which is related. Notice that our patches certainly do not commute but rebasing should be trivial. 

Cheers,

Florent


---

Comment by mpatel created at 2010-02-18 23:38:35

Replying to [comment:20 jhpalmieri]:

> I noticed that after I built with "-j -iu", edited a few files and ran "sage -b", then when I built the manual again with "-j -iu", in the "reading sources" portion of the build, it only processes the changed files, but in the "writing output" phase, it rewrites all of the files.  This could be a little annoying; can it be avoided?

I've also seen this behavior, but I've been unable reproduce it with certainty --- at least, with a version of #6187's ['"testreference" patch'](http://trac.sagemath.org/sage_trac/attachment/ticket/6187/trac_6187_testreference.patch).  Are there particular types of changes that usually trigger the problem?

I don't think Sphinx is especially smart about updating files affected by a change in other files, but this may be irrelevant.


---

Comment by mpatel created at 2010-02-20 21:14:27

To do: Rebase the patch against 4.3.3.alpha1 + #8244 + #7448.


---

Comment by jhpalmieri created at 2010-02-24 22:06:49

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

Comment by mpatel created at 2010-02-25 08:46:21

I've seen this message, too.  It _might_ be a Sphinx bug.

The HTML builder writes a hash of the `html_*` settings to `.buildinfo` in the output directory.  It appears that [StandaloneHTMLBuilder.get_outdated_docs](http://bitbucket.org/birkenfeld/sphinx/src/tip/sphinx/builders/html.py#cl-144) contains nearly all of the relevant code.

If, for some reason, this `get_outdated_docs` doesn't get called, the builder writes empty strings for the hashes.  For example, `sage -docbuild reference html -j -S -a` does this (`-a` tells Sphinx to write all files).  The next build attempt triggers the warning.

But I don't know if this is responsible for what we see.


---

Attachment

Rebase vs. 4.3.4.alpha1 + #8457.  Apply only this patch.


---

Comment by mpatel created at 2010-03-11 06:30:43

V5 is rebased for 4.3.4.alpha1 + #8457.  I'm not sure what we should do about the many `-iu` warnings.  Should we handle them in `sage_getargspec` or in `conf`?


---

Comment by jhpalmieri created at 2010-03-12 23:04:01

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-03-12 23:04:01

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

Comment by jhpalmieri created at 2010-03-12 23:07:43

(You may need to apply #8511 to get rid of one of the "unexpected indentation" warnings.)


---

Comment by jhpalmieri created at 2010-03-12 23:28:58

On second thought, I moved the "unexpected indentation" fix to ticket #8511, so the "small fixes" patch just reinstates the interfaces/singular.py doctest.


---

Comment by jhpalmieri created at 2010-03-12 23:29:33

apply on top of other patch


---

Attachment

Fix recursion problem.  Apply only this combined patch.


---

Comment by mpatel created at 2010-03-13 08:36:09

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-03-13 08:36:09

I broke the module check in #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.4.patch V4] when I made #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.5.patch V5].  I apologize for that.  I've restored Florent's code and folded in the small fixes patch in this ticket's V6.


---

Comment by mpatel created at 2010-03-13 08:37:35

The only change is in `sage_autodoc.py`.


---

Attachment

Help notes.  Replaces V6.


---

Comment by hivert created at 2010-03-13 09:53:46

Replying to [comment:31 mpatel]:
> I broke the module check in #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.4.patch V4] when I made #7448's [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.5.patch V5].  I apologize for that.  I've restored Florent's code and folded in the small fixes patch in this ticket's V6.  

Hi Mitesh ! I don't see any code from me here except a few lines who where already in #7448, and which you decide to improve (thanks by the way). So I don't think I deserve to be in the author.

Also I'm Ok with reviewing this but they are three more tickets in combinatoric which I committed myself to review. So don't rely on me for reviewing this very soon... However, I'd like to see this merged soon, so if you imagine someone who is willing to review, please ask him. Anyway, thanks for this work. I really this sage's doc is going to greatly improve.


---

Comment by jhpalmieri created at 2010-04-05 18:46:51

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-05 18:46:51

Sorry for not getting to this sooner.  Positive review.


---

Comment by jhpalmieri created at 2010-04-15 05:59:07

Merged in 4.4.alpha0:

 - trac_7549-doc_inheritance_underscore_v7.patch


---

Comment by jhpalmieri created at 2010-04-15 05:59:07

Resolution: fixed
