# Issue 8036: Sage 4.3.1 reference manual: PDF version failed to build due to non-ASCII characters in docstring

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-01-22 02:31:21

Assignee: mvngu

Keywords: non-ASCII characters

Even after applying #8021, the PDF version of the reference manual for Sage 4.3.1 failed to build. This is due to non-ASCII characters in the docstring of the method `prove_BSD()` of the class `EllipticCurve_rational_field` in

```
sage/schemes/elliptic_curves/ell_rational_field.py
```

Here's a snippet of the error message:

```
! Package inputenc Error: Unicode char \u8:ǎ not set up for use with LaTeX.

See the inputenc package documentation for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.364560 C. Tarniţǎ
                     . Computational verification of the Birch and
?
```



---

Comment by mvngu created at 2010-01-22 02:33:00

based on Sage 4.3.1


---

Attachment


---

Comment by mvngu created at 2010-01-22 02:33:32

Changing status from new to needs_review.


---

Comment by tornaria created at 2010-01-22 03:08:18

Changing status from needs_review to needs_work.


---

Comment by tornaria created at 2010-01-22 03:08:18

`LaTeX` is perfectly fine with utf8 if one uses the inputenc package:

```
\usepackage[utf8x]{inputenc}
```

IOW, it's the latex preamble which needs fixing.


---

Attachment

Latex file which shows usage of utf8


---

Comment by jhpalmieri created at 2010-01-22 05:44:37

Sphinx uses `\usepackage[utf8]{inputenc`}, so if we want to change this to [utf8x], we need to patch Sphinx.  I have no experience with [utf8] or [utf8x], but the documentation for inputenc frowns on utf8x, to some extent.  Another option is to add characters one by one, as needed, using

```
\DeclareUnicodeCharacter{blah}{blah}
```

(See the documentation for inputenc.)  If we knew the details, we could add lines like this to `SAGE_ROOT/devel/sage/doc/common/conf.py` -- add to the `latex_preamble`.  I don't know the details.

A third option is to get rid of all accents, as mvngu's patch does.

A fourth option is to use the attached patch `trac_8036-tex-replacements.patch`, which does some preprocessing, changing the offending character to something latex can handle.

I'll mark this as "needs review", in case option 4 is appealing.


---

Comment by jhpalmieri created at 2010-01-22 05:44:37

Changing status from needs_work to needs_review.


---

Attachment

apply only this patch


---

Comment by jhpalmieri created at 2010-01-22 05:47:54

Note: When I preview my attachment, the "offending character" looks like a capital "C" with a cedilla, but don't be deceived: the actual character (when I download the patch and look at it in emacs, for example), is an "a" with a "vee" accent on top -- the last character in "Tarnita".


---

Comment by jhpalmieri created at 2010-01-22 05:55:36

Replying to [comment:3 jhpalmieri]:
> I have no experience with [utf8] or [utf8x], but the documentation for inputenc frowns on utf8x, to some extent.

In case you're interested in this, the documentation says

   For other languages that do not fit well into LaTeX font selection scheme, ... the outlined inputenc approach will not work. If that is the case one can try using Dominique Unruh’s option utf8x for inputenc which has a somewhat different approach and encodes many more UTF-8 characters than the standard utf8 option. However, we recommend to do so only if you really need such alphabets as there are problems with this extended approach which were precisely the reason that we decided to limit the support to what is properly supported within the boundaries of LaTeX’s font selection.

I don't know what the "problems with this extended approach" are.


---

Comment by tornaria created at 2010-01-22 06:26:44

Replying to [comment:5 jhpalmieri]:
> Replying to [comment:3 jhpalmieri]:
> > I have no experience with [utf8] or [utf8x], but the documentation for inputenc frowns on utf8x, to some extent.
> 
> In case you're interested in this, the documentation says
> 
>    For other languages that do not fit well into LaTeX font selection scheme, ... the outlined inputenc approach will not work. If that is the case one can try using Dominique Unruh’s option utf8x for inputenc which has a somewhat different approach and encodes many more UTF-8 characters than the standard utf8 option. However, we recommend to do so only if you really need such alphabets as there are problems with this extended approach which were precisely the reason that we decided to limit the support to what is properly supported within the boundaries of LaTeX’s font selection.
> 
> I don't know what the "problems with this extended approach" are.

I use [utf8x] on a daily basis, without issues. As you quoted above, it is well known that [utf8] supports a reduced set of characters. Not that utf8x supports arbitrary unicode characters, but I think a proper superset of those supported by utf8.

The option [utf8x] is part of latex package "ucs".

Your proposal (according to the posted patch) would be to special-case any characters not supported by [utf8] option? The patch only handles that particular letter.


---

Comment by jhpalmieri created at 2010-01-22 15:54:28

Replying to [comment:6 tornaria]:

> Your proposal (according to the posted patch) would be to special-case any characters not supported by [utf8] option? The patch only handles that particular letter.

It's either that or patch Sphinx -- not hard, but I'm reluctant to patch external packages if there are other alternatives.  I don't know how often we are likely to come across characters not supported by [utf8], so I don't know which option is better.


---

Comment by rbeezer created at 2010-01-23 22:52:50

There are three non-ascii characters in this file, which prevent me from building the HTML version of the documentation.  The patches here already seem to address the tex processing that builds the PDF.

The patch simply identifies the three characters and replaces them with straight ASCII equivalents.  It might be useful for folks trying to build the docs to test their own fixes/changes elsewhere.  I'm not trying to weigh-in on the long-run solution to this problem.


---

Attachment

#7999 should take care of the HTML reference manual.


---

Comment by mpatel created at 2010-01-31 08:04:57

For now, what if we [set](http://sphinx.pocoo.org/config.html#confval-latex_elements):


```python
latex_elements['inputenc'] = '\\usepackage[utf8x]{inputenc}'
```


in `doc/common/conf.py`?


---

Attachment

Set utf8x in Sphinx option.  Solo patch.


---

Comment by mpatel created at 2010-01-31 09:00:47

Replying to [comment:10 mpatel]:
> For now, what if we [set](http://sphinx.pocoo.org/config.html#confval-latex_elements):

I've attached a [attachment:trac_8036-docbuild_utf8x.patch patch] that does this.  It appears to solve the problem in this ticket's description.

But it fails to handle the unicode tests we've added to SageNB at #7249.


---

Comment by jhpalmieri created at 2010-01-31 16:49:39

I like `trac_8036-docbuild_utf8x.patch`.  I didn't know about the `latex_elements` customization; very nice.

To the release manager: apply only `trac_8036-docbuild_utf8x.patch`.


---

Comment by jhpalmieri created at 2010-01-31 16:49:39

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-01 23:25:10

Resolution: fixed


---

Comment by mvngu created at 2010-02-01 23:25:10

Merged [trac_8036-docbuild_utf8x.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8036/trac_8036-docbuild_utf8x.patch).


---

Comment by mvngu created at 2010-02-02 02:04:04

The attachment [trac_8036-docbuild_utf8x.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8036/trac_8036-docbuild_utf8x.patch) breaks the build of the French tutorial. See #8146 for a follow-up to this issue.
