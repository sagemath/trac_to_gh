# Issue 8472: add %xelatex to notebook

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-03-07 04:08:15

Assignee: was

In [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/bbb437ab04ff64d), there is a request for something like this to work in the notebook:

```
%xelatex
실수 $x$에 대해서 다음이 성립한다.
\[
    \sqrt{x^2}=|x|
\]
```

[XeTeX](http://en.wikipedia.org/wiki/XeTeX) is an extension of TeX that makes working with arbitrary fonts very easy. In practice, this means that users of non-European languages can simply set a font that supports their writing system, type their document, and everything just works.

Adding support for this would be useful to anyone who uses both Sage and non-European languages.

Note that it will be necessary for most users to use a function corresponding to `latex.add_to_preamble()`, since XeTeX by default uses the Computer Modern fonts and for non-trivial uses, one needs to tell XeTeX what font to use. Also, XeTeX produces PDFs by default, so it will be necessary to use something other than `dvipng` to get something that we can display in the notebook.


---

Comment by robert.marik created at 2010-03-10 10:15:23

duplicate, see #8486


---

Comment by ddrake created at 2010-03-11 01:48:31

Resolution: duplicate
