# Issue 8958: Extend/clarify/normalize the conventions for Python/Cython docstrings

Issue created by migration from Trac.

Original creator: leif

Original creation time: 2010-05-12 23:05:04

Assignee: mvngu

CC:  mvngu

Keywords: docstring, documentation string, convention, style

The section of the _Developer's Guide_ on conventions for (Python/Cython) docstrings within Sage http://www.sagemath.org/doc/developer/conventions.html#documentation-strings currently lacks some issues; also IMHO the usage of _inline literals_ for Python names/types etc., _default-role interpreted text_ (i.e. [LaTeX] math mode) and the syntax/style of e.g. parameter and return type descriptions should be normalized (further).

 * A description of the `:class:`, `:meth:`, `:func:` etc. roles is completely missing.

 * We currently have _at least_ both

   ` - ``param`` -- (type, default val) other description...`

   and
   
   ` - ``param`` (type, default val) -- other description...`,

   where the latter (without the default) is used by Sphinx.

 * `True` and `False` etc. are usually written/typeset as _literals_ (```True```), while other Python names and types (e.g. `int`) are not. (Perhaps a bad example, since one could even use `:class:`int``.)

  * True function/return type descriptions use both indicative and imperative mood, sometimes even within the same module/file. (Same for procedures, i.e. "functions" doing something but not returning anything.) 

  * Some people use _math mode_ also for isolated numbers (``1``) and/or numbers within words (e.g. ``2`-descent` instead of `2-descent`), but not necessarily consistently.
    The _HTML output_ of that looks very ugly, as does e.g. that of ``L`-functions`.
    (There are at least four variants of how _simple_ constraints or case distinctions like "n < 42" are written, namely without mark-up, entirely literal, partially or completely typeset in math mode, and as mixtures of plain, literal/verbatim and math mode; "... less than 42" of course is another option.) 

  * IMHO the type descriptions should be specific if a function actually expects (or returns) some particular type.
  (Once we switch to Python 3, we can use type annotations, too... ;-) )

  * What about documenting potentially raised exceptions?

  * Some frequently used names etc. (even e.g. `int`) could be defined as (global) macros (e.g. `|int|`) to achieve consistent look (this also applies to reST documentation within Sage in general).

(The above list is most probably not exhaustive, nor does it express any importance/priority; additions welcome.)

Besides extending the documentation, we should perhaps discuss some issues and/or hold votes for the preferred/recommended style on _sage-devel_. :)




---

Comment by leif created at 2010-05-12 23:39:31

I think before opening _one_ *giant* thread on sage-devel, we should sort out some things. ;-)


---

Comment by jason created at 2010-05-13 00:41:08

We also have the sphinx-recommended

```
   :param: ...
```


See http://sphinx.pocoo.org/markup/desc.html#info-field-lists


---

Comment by leif created at 2010-05-13 00:49:48

Replying to [comment:2 jason]:
> We also have the sphinx-recommended
> {{{
>    :param: ...
> }}}
I know... which is more formal but less readable in the plain text, i.e. if you type 

```
sage: foo?
```

or

```
sage: foo??
```



---

Comment by novoselt created at 2010-07-10 23:18:25

Some thoughts on the subject after writing and reading quite a bit of documentation recently. The main one - it would be really great to have strict formatting standard, preferably without variations...

 * PEP 257 and Sage conventions do not agree (e.g. how quotes are located), so I don't think that PEP 257 should be cited at all (currently it is on the top of http://sagemath.org/doc/developer/conventions.html#python-coding-conventions
 * There should be a clear statement which one of the following is correct for the first sentence:
  * Return a numerical approximation of ``self``.
  * Returns a  numerical approximation of ``self``.
  * A numerical approximation of  ``self``.
  * Numerical approximation of ``self``.
  * This function returns a numerical approximation of ``self``.
 The last variant is given in the example on docstrings an I consider it the worst one, since it is the longest one and the first three words don't really carry any information - for a one-liner it is really bad. The other ones are more or less the same to me and I would be happy with any choice, but it kind of bugs me when they are mixed.
 * I think it is bad to have serveral approved conventions about anything including INPUT/OUTPUT blocks. It should be clear from the guide which ONE of the following lines should I write in the OUTPUT:
  * An integer.
  * Integer
  * - an integer.
  * - integer.
 I also didn't quite like the code and look of Sphynx-type INPUT/OUTPUT block, so I would vote for not approving it (or, if we do approve it, I think that it should be the only one...)
 * Precise description of the default value can be quite lengthy and complicated, especially if it is ``None`` in the beginning and then is somehow "smartly guessed" based on the combination of other parameters, so I think there should be no requirement to indicate it in any of the forms given in the description. Perhaps, it would be good instead to have a standard way to indicate which parameters are optional.
 * Some functions take as a particular parameter objects of different types, so there should be guidelines on what should one do in this case.
 * There should be guidelines to using hyperlinks, especially in conjunction with type desriptions. E.g., it is OK for me to write

```
OUTPUT:

- :class:`toric variety <ToricVariety_field>`.
```

 or should I not hide the the actual precise name of the class?


---

Comment by johanbosman created at 2011-11-15 14:34:30

Replying to [comment:4 novoselt]:

> There should be a clear statement which one of the following is correct for the first sentence: 

* Return a numerical approximation of self. 
* Returns a  numerical approximation of self. 
* A numerical approximation of  self. 
* Numerical approximation of self. 
* This function returns a numerical approximation of self. 
 
The last variant is given in the example on docstrings an I consider it the worst one, since it is the longest one and the first three words don't really carry any information - for a one-liner it is really bad. The other ones are more or less the same to me and I would be happy with any choice, but it kind of bugs me when they are mixed.

About this I'd say that the first option is the best.  The imperative mood gives the most direct phrasing and thus the best readable sentence. 

Options 2, 3, and 4 aren't even English sentences: number 2 lacks a subject and 3 and 4 lack verbs.  Furthermore, options 3 and 4 aren't accurate: they suggest that the function _is,_ rather than _returns,_ a numerical approximation.
