# Issue 8083: fix accents in LaTeX output

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-01-26 20:53:14

Assignee: was

Keywords: latex

Accented letters produced in notebook by command like this

```
%latex
ěščřžýáíéďĎ
```

produce letters composed from two objects - letter and accent - and this does not look good in some cases, especially the letter ď. The solution is to use correct fonts in LaTeX.


---

Attachment


---

Comment by robert.marik created at 2010-01-26 20:57:51

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-01-28 22:10:43

Works as advertised in the notebook.  Note that executing

```
sage: view(s = u"ěščřžýáíéďĎ")
```

from the command line doesn't work at all, and I can't figure out how to fix it.  I can get it not to throw an error -- see the experimental patch.  I think that the command to write the LaTeX file (in the definition of the `view` function) should be something like

```
codecs.open(tex_file, mode='w', encoding='utf_8').write(s)
```

but this garbles the string s.  Anyway, this belongs on another ticket.


---

Comment by jhpalmieri created at 2010-01-28 22:10:43

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-01-28 22:11:07

do not merge: for illustration and testing only


---

Attachment

Out of curiosity: Do other font encodings ever conflict with `T1`?  Other alphabets may require a different one, e.g., for


```
%latex
Теория чисел
```

one can use


```python
sage.misc.latex.latex.extra_preamble('\\usepackage[T2A]{fontenc}')
```



---

Comment by mvngu created at 2010-01-30 23:50:32

Merged [latex_T1_fonts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8083/latex_T1_fonts.patch).


---

Comment by mvngu created at 2010-01-30 23:50:32

Resolution: fixed
