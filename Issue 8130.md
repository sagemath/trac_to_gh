# Issue 8130: UnicodeDecodeError (etc.) with view from the command line

Issue created by migration from https://trac.sagemath.org/ticket/8130

Original creator: jhpalmieri

Original creation time: 2010-01-30 04:51:58

Assignee: tbd

Try this:

```
sage: s = u"č"
sage: view(s)
```

It will throw a `UnicodeDecodeError`.  This much can be fixed using the "experimental" patch at #8083; however, after applying that patch,

```
sage: view(s)
```

pops open a dvi/pdf file showing the wrong unicode character.

See #8083 and #8128 for tickets focusing on latex and unicode in the notebook.




---

Comment by mpatel created at 2010-01-30 11:18:09

What if we try just

```python
sage: s ='č'
sage: view(s)
sage: s.decode('utf8')
u'\u010d'
```

?  This opens a PDF file for me that shows the expected character.


---

Comment by jhpalmieri created at 2010-01-30 16:50:48

Should this be closed, or should "view" be able to handle unicode strings?


---

Comment by mpatel created at 2010-01-31 00:02:02

`view(u'\u010d')` works for me, but I may well be misinterpreting your question.  We could use `encoded_str` in place of `str` in some places.

By the way, it seems that [XeTeX / XeLaTeX](http://en.wikipedia.org/wiki/Xelatex) is currently one of the better ways to mix Unicode and LaTeX.  Unfortunately, the example in the article doesn't work for me with TeX Live on Linux --- the font is missing.


---

Comment by jhpalmieri created at 2010-01-31 00:57:22

Resolution: wontfix


---

Comment by jhpalmieri created at 2010-01-31 00:57:22

I don't think you're misinterpreting my question, I think I just don't understand unicode.  Let's close this, and if someone who wants or needs unicode (unlike me -- I was just playing around) has problems with view from the command line, we can open a new ticket.
