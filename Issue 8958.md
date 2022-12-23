# Issue 8958: Extend/clarify/normalize the conventions for Python/Cython docstrings

archive/issues_008958.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  mvngu\n\nKeywords: docstring, documentation string, convention, style\n\nThe section of the *Developer's Guide* on conventions for (Python/Cython) docstrings within Sage http://www.sagemath.org/doc/developer/conventions.html#documentation-strings currently lacks some issues; also IMHO the usage of *inline literals* for Python names/types etc., *default-role interpreted text* (i.e. [LaTeX] math mode) and the syntax/style of e.g. parameter and return type descriptions should be normalized (further).\n\n* A description of the `:class:`, `:meth:`, `:func:` etc. roles is completely missing.\n\n* We currently have *at least* both\n\n  ` - ``param`` -- (type, default val) other description...`\n\n  and\n   \n  ` - ``param`` (type, default val) -- other description...`,\n\n  where the latter (without the default) is used by Sphinx.\n\n* `True` and `False` etc. are usually written/typeset as *literals* (```True```), while other Python names and types (e.g. `int`) are not. (Perhaps a bad example, since one could even use `:class:`int``.)\n\n  * True function/return type descriptions use both indicative and imperative mood, sometimes even within the same module/file. (Same for procedures, i.e. \"functions\" doing something but not returning anything.) \n\n  * Some people use *math mode* also for isolated numbers (``1``) and/or numbers within words (e.g. ``2`-descent` instead of `2-descent`), but not necessarily consistently.\n   The *HTML output* of that looks very ugly, as does e.g. that of ``L`-functions`.\n   (There are at least four variants of how *simple* constraints or case distinctions like \"n < 42\" are written, namely without mark-up, entirely literal, partially or completely typeset in math mode, and as mixtures of plain, literal/verbatim and math mode; \"... less than 42\" of course is another option.) \n\n  * IMHO the type descriptions should be specific if a function actually expects (or returns) some particular type.\n  (Once we switch to Python 3, we can use type annotations, too... ;-) )\n\n  * What about documenting potentially raised exceptions?\n\n  * Some frequently used names etc. (even e.g. `int`) could be defined as (global) macros (e.g. `|int|`) to achieve consistent look (this also applies to reST documentation within Sage in general).\n\n(The above list is most probably not exhaustive, nor does it express any importance/priority; additions welcome.)\n\nBesides extending the documentation, we should perhaps discuss some issues and/or hold votes for the preferred/recommended style on *sage-devel*. :)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8958\n\n",
    "created_at": "2010-05-12T23:05:04Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "Extend/clarify/normalize the conventions for Python/Cython docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8958",
    "user": "leif"
}
```
Assignee: mvngu

CC:  mvngu

Keywords: docstring, documentation string, convention, style

The section of the *Developer's Guide* on conventions for (Python/Cython) docstrings within Sage http://www.sagemath.org/doc/developer/conventions.html#documentation-strings currently lacks some issues; also IMHO the usage of *inline literals* for Python names/types etc., *default-role interpreted text* (i.e. [LaTeX] math mode) and the syntax/style of e.g. parameter and return type descriptions should be normalized (further).

* A description of the `:class:`, `:meth:`, `:func:` etc. roles is completely missing.

* We currently have *at least* both

  ` - ``param`` -- (type, default val) other description...`

  and
   
  ` - ``param`` (type, default val) -- other description...`,

  where the latter (without the default) is used by Sphinx.

* `True` and `False` etc. are usually written/typeset as *literals* (```True```), while other Python names and types (e.g. `int`) are not. (Perhaps a bad example, since one could even use `:class:`int``.)

  * True function/return type descriptions use both indicative and imperative mood, sometimes even within the same module/file. (Same for procedures, i.e. "functions" doing something but not returning anything.) 

  * Some people use *math mode* also for isolated numbers (``1``) and/or numbers within words (e.g. ``2`-descent` instead of `2-descent`), but not necessarily consistently.
   The *HTML output* of that looks very ugly, as does e.g. that of ``L`-functions`.
   (There are at least four variants of how *simple* constraints or case distinctions like "n < 42" are written, namely without mark-up, entirely literal, partially or completely typeset in math mode, and as mixtures of plain, literal/verbatim and math mode; "... less than 42" of course is another option.) 

  * IMHO the type descriptions should be specific if a function actually expects (or returns) some particular type.
  (Once we switch to Python 3, we can use type annotations, too... ;-) )

  * What about documenting potentially raised exceptions?

  * Some frequently used names etc. (even e.g. `int`) could be defined as (global) macros (e.g. `|int|`) to achieve consistent look (this also applies to reST documentation within Sage in general).

(The above list is most probably not exhaustive, nor does it express any importance/priority; additions welcome.)

Besides extending the documentation, we should perhaps discuss some issues and/or hold votes for the preferred/recommended style on *sage-devel*. :)



Issue created by migration from https://trac.sagemath.org/ticket/8958





---

archive/issue_comments_082572.json:
```json
{
    "body": "I think before opening *one* **giant** thread on sage-devel, we should sort out some things. ;-)",
    "created_at": "2010-05-12T23:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8958#issuecomment-82572",
    "user": "leif"
}
```

I think before opening *one* **giant** thread on sage-devel, we should sort out some things. ;-)



---

archive/issue_comments_082573.json:
```json
{
    "body": "We also have the sphinx-recommended\n\n```\n   :param: ...\n```\n\n\nSee http://sphinx.pocoo.org/markup/desc.html#info-field-lists",
    "created_at": "2010-05-13T00:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8958#issuecomment-82573",
    "user": "jason"
}
```

We also have the sphinx-recommended

```
   :param: ...
```


See http://sphinx.pocoo.org/markup/desc.html#info-field-lists



---

archive/issue_comments_082574.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> We also have the sphinx-recommended\n> {{{\n>    :param: ...\n> }}}\nI know... which is more formal but less readable in the plain text, i.e. if you type \n\n```\nsage: foo?\n```\n\nor\n\n```\nsage: foo??\n```\n",
    "created_at": "2010-05-13T00:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8958#issuecomment-82574",
    "user": "leif"
}
```

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

archive/issue_comments_082575.json:
```json
{
    "body": "Some thoughts on the subject after writing and reading quite a bit of documentation recently. The main one - it would be really great to have strict formatting standard, preferably without variations...\n\n* PEP 257 and Sage conventions do not agree (e.g. how quotes are located), so I don't think that PEP 257 should be cited at all (currently it is on the top of http://sagemath.org/doc/developer/conventions.html#python-coding-conventions\n* There should be a clear statement which one of the following is correct for the first sentence:\n  * Return a numerical approximation of ``self``.\n  * Returns a  numerical approximation of ``self``.\n  * A numerical approximation of  ``self``.\n  * Numerical approximation of ``self``.\n  * This function returns a numerical approximation of ``self``.\n The last variant is given in the example on docstrings an I consider it the worst one, since it is the longest one and the first three words don't really carry any information - for a one-liner it is really bad. The other ones are more or less the same to me and I would be happy with any choice, but it kind of bugs me when they are mixed.\n* I think it is bad to have serveral approved conventions about anything including INPUT/OUTPUT blocks. It should be clear from the guide which ONE of the following lines should I write in the OUTPUT:\n  * An integer.\n  * Integer\n  * - an integer.\n  * - integer.\n I also didn't quite like the code and look of Sphynx-type INPUT/OUTPUT block, so I would vote for not approving it (or, if we do approve it, I think that it should be the only one...)\n* Precise description of the default value can be quite lengthy and complicated, especially if it is ``None`` in the beginning and then is somehow \"smartly guessed\" based on the combination of other parameters, so I think there should be no requirement to indicate it in any of the forms given in the description. Perhaps, it would be good instead to have a standard way to indicate which parameters are optional.\n* Some functions take as a particular parameter objects of different types, so there should be guidelines on what should one do in this case.\n* There should be guidelines to using hyperlinks, especially in conjunction with type desriptions. E.g., it is OK for me to write\n\n```\nOUTPUT:\n\n- :class:`toric variety <ToricVariety_field>`.\n```\n\n or should I not hide the the actual precise name of the class?",
    "created_at": "2010-07-10T23:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8958#issuecomment-82575",
    "user": "novoselt"
}
```

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

archive/issue_comments_082576.json:
```json
{
    "body": "Replying to [comment:4 novoselt]:\n\n> There should be a clear statement which one of the following is correct for the first sentence: \n\n* Return a numerical approximation of self. \n* Returns a  numerical approximation of self. \n* A numerical approximation of  self. \n* Numerical approximation of self. \n* This function returns a numerical approximation of self. \n \nThe last variant is given in the example on docstrings an I consider it the worst one, since it is the longest one and the first three words don't really carry any information - for a one-liner it is really bad. The other ones are more or less the same to me and I would be happy with any choice, but it kind of bugs me when they are mixed.\n\nAbout this I'd say that the first option is the best.  The imperative mood gives the most direct phrasing and thus the best readable sentence.\u00a0\n\nOptions 2, 3, and 4 aren't even English sentences: number 2 lacks a subject and 3 and 4 lack verbs.  Furthermore, options 3 and 4 aren't accurate: they suggest that the function *is,* rather than *returns,* a numerical approximation.",
    "created_at": "2011-11-15T14:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8958#issuecomment-82576",
    "user": "johanbosman"
}
```

Replying to [comment:4 novoselt]:

> There should be a clear statement which one of the following is correct for the first sentence: 

* Return a numerical approximation of self. 
* Returns a  numerical approximation of self. 
* A numerical approximation of  self. 
* Numerical approximation of self. 
* This function returns a numerical approximation of self. 
 
The last variant is given in the example on docstrings an I consider it the worst one, since it is the longest one and the first three words don't really carry any information - for a one-liner it is really bad. The other ones are more or less the same to me and I would be happy with any choice, but it kind of bugs me when they are mixed.

About this I'd say that the first option is the best.  The imperative mood gives the most direct phrasing and thus the best readable sentence. 

Options 2, 3, and 4 aren't even English sentences: number 2 lacks a subject and 3 and 4 lack verbs.  Furthermore, options 3 and 4 aren't accurate: they suggest that the function *is,* rather than *returns,* a numerical approximation.
