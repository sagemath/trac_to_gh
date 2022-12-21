# Issue 3912: sage -t foo.tex should also test listings blocks not only verbatim

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-20 14:31:47

Assignee: tba

CC:  mvngu

sage -t can check stuff in 

```
\begin{verbatim}
sage: 2 + 3
5
\end{verbatim}
```


I propose to also support 

```
\begin{lstlisting}
sage: 2 + 3
5
\end{llstisting}
```

which looks so much nicer.


---

Comment by chapoton created at 2014-07-25 09:44:14

Changing keywords from "" to "doctest".


---

Comment by chapoton created at 2014-07-25 10:08:10

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-07-25 10:08:10

Changing keywords from "doctest" to "doctest, latex".


---

Comment by chapoton created at 2014-07-25 10:08:10

New commits:


---

Comment by chapoton created at 2014-07-25 11:48:59

See http://mvngu.wordpress.com/2010/06/27/typesetting-sage-code-listings-in-latex/ for nice parameters for the package `listings`.


---

Comment by aapitzsch created at 2014-07-27 09:10:15

[Line 153](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n153) contains a left parenthesis which is never closed.

Could you also unify [Line 1142](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n1142) and [Line 1219](https://github.com/sagemath/sagetrac-mirror/blob/master/src/sage/doctest/sources.py?id=6767e49fed16e13fb6523e2c896594f01cde6ee7#n1219).


---

Comment by git created at 2014-07-27 09:18:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by aapitzsch created at 2014-07-27 09:19:33

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-07-28 03:55:38

Resolution: fixed
