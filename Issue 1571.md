# Issue 1571: corrections for tut.tex

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-20 04:37:51

Assignee: tba

Minh Nguyen send the following patch

```
--- sage-2.8.15/devel/doc-main/tut/tut.tex      2007-12-14
13:05:11.000000000 +1100
+++ sage-2.8.16/devel/doc-main/tut/tut.tex      2007-12-20
15:17:58.000000000 +1100
`@``@` -191,7 +191,7 `@``@`
 \ref{sec:compile}), and
 \item
 {\bf Scripts:}
-by writing a write stand-alone Python scripts that use the \sage library
+by writing stand-alone Python scripts that use the \sage library
 (see Section~\ref{sec:standalone}).
 \end{itemize}%two are needed for some weird reason

`@``@` -403,7 +403,7 `@``@`

 Semicolons are not needed at the ends of lines; a line is
 in most cases ended by a newline.   However, you can put multiple
-statements on one line separate by semicolons:
+statements on one line separated by semicolons:
 \begin{verbatim}
 sage: a = 5; b = a + 3; c = b^2; c
 64
`@``@` -694,7 +694,7 `@``@`
 integer literals beginning with a 0 as octal numbers.

 The field of $p$-adic numbers is implemented as well:
-Note that once $p$-adic field is created, you can not
+Note that once a $p$-adic field is created, you can not
 change its precision.

 \begin{verbatim}
`@``@` -706,7 +706,7 `@``@`
 10*11^-2 + 5*11^-1 + 4 + 2*11 + O(11^18)
 \end{verbatim}

-Much work has been done implementing rings of integers in p-adic
+Much work has been done implementing rings of integers in $p$-adic
 fields or number fields other than $\Q$. The interested reader is
 invited to ask the experts on the mailing for further details.

`@``@` -761,8 +761,8 `@``@`
 Univariate Polynomial Ring in x over Rational Field
 \end{verbatim}%link

-This creates a polynomial ring and tells \SAGE to use (the string) ``x'' and
-the interderminant when printing to the screen. The symbol $x$ is not yet
+This creates a polynomial ring and tells \SAGE to use (the string) ``x'' as
+the indeterminate when printing to the screen. The symbol $x$ is not yet
 known to \sage, so you cannot use it to enter a polynomial (such as $x^2+1$)
 belonging to $R$.

`@``@` -1486,7 +1486,7 `@``@`
 \langle (1,2,3)(4,5), (3,4) \rangle
 \end{verbatim}

-You can also obtain the character table latex format in \sage:
+You can also obtain the character table \LaTeX format in \sage:

 \begin{verbatim}
 sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3)]])
`@``@` -1789,7 +1789,7 `@``@`
 sage: p = polygon(L, rgbcolor=(1/8,3/4,1/2))
 sage: p.save()
 \end{verbatim}
-Type \code{p.show(axes=false)} to see this without any ases.
+Type \code{p.show(axes=false)} to see this without any axes.

     A blue figure 8:

`@``@` -1899,7 +1899,7 `@``@`
                  2 (x - 1)   2 (x + 1)
 \end{verbatim}

-To compute the laplace transform of $t^2e^t - \sin(t)$:
+To compute the Laplace transform of $t^2e^t - \sin(t)$:

 \begin{verbatim}
 sage: s = var("s")
`@``@` -1916,7 +1916,7 `@``@`
 \index{Laplace transform solution of DEs}

 In this section, we provide a few details which are useful to teaching a lower
-level ordinary differential equatoins course using \SAGE.
+level ordinary differential equations course using \SAGE.

 The displacement from equilibrium (respectively)
 for a coupled spring attached to a wall on the left
`@``@` -2674,7 +2674,7 `@``@`
 a trivial command in the system, in order to start up the
 server for that program.  The most relavant time is the wall time.
 However, if there is a significant difference between the
-wall time and the cpu time then this may indicate
+wall time and the CPU time then this may indicate
 a performance issue worth looking into.

 %skip
`@``@` -2722,7 +2722,7 `@``@`
 \index{error mesaages in SAGE}

 When something goes wrong, you will usually see a Python
-``exception''.  Python even tries to suggest what it is that it that
+``exception''.  Python even tries to suggest what
 raised the exception.  Often you see the name of the exception, e.g.,
 {\tt NameError} or \code{ValueError} (see the Python Reference Manual
 \cite{Py} for a complete list of exceptions).  For example,
`@``@` -2912,7 +2912,7 `@``@`
         return self.ambient_vector_space()(v)
 \end{verbatim}
 The \code{coordinate_vector} function coerces its
-input into the ambient space, which has the affect of
+input into the ambient space, which has the effect of
 computing the vector of coefficients of $v$ in terms
 of $V$.  The space~$V$ is already ambient since it's
 just $\Q^3$.  There is also a \code{coordinate_vector}
`@``@` -3105,7 +3105,7 `@``@`
 you've defined in the current session as a dictionary in the given
 \code{sessionname}.  (In the rare case when a variable does not support saving,
 it is simply not saved to the dictionary.)  The resulting file
-is an \code{.sobj} file and can be loading just like any other
+is an \code{.sobj} file and can be loaded just like any other
 object that was saved.   When you load the objects saved in a session,
 you get a dictionary whose keys are the variables names and whose
 values are the objects.
`@``@` -3176,7 +3176,7 `@``@`
 by William Stein, SAGE seminar, 6-9-2006 (notes by D. Joyner).

-The SAGE notebook is run by typing
+The \SAGE notebook is run by typing

 %skip
 \begin{verbatim}
`@``@` -3237,8 +3237,8 `@``@`
 using the ``add" link in the left-hand panel.

 Your worksheet can be emailed to someone
-else, how can open it up in their copy of
-SAGE. The entire worksheet can now be executed.
+else, who can open it up in their copy of
+\SAGE. The entire worksheet can now be executed.

 How does the notebook interface work?

`@``@` -3266,7 +3266,7 `@``@`
 ----------------------                    .
 \end{verbatim}

-For help on a SAGE command, \code{cmd}, in the notebook
+For help on a \SAGE command, \code{cmd}, in the notebook
 browser box, type \code{cmd?} and now hit \verb+<esc>+ (not
 \verb+<shift-enter>+).

`@``@` -3332,17 +3332,17 `@``@`
 program, since it {\em is} running that program.  In particular, you can
 load complicated PARI programs and run them.
 In contrast, the PARI interface (via the C library) is much more restrictive;
-first not all member functions have been implemented.  Second; a lot of code,
+first not all member functions have been implemented.  Second, a lot of code,
 e.g., involving numerical integration, won't work via the PARI interface.
 That said, the PARI interface can be significantly faster and more robust
-then the GP one.
+than the GP one.

 \note{If the GP interface runs out of memory evaluating a given input
 line, it will silently and automatically double the stack size and
 retry that input line.  Thus your computation won't crash if you didn't
 correctly anticipate the amount of memory that would be needed.  This
 is a nice trick the usual GP interpreter doesn't seem to provide.  Regarding
-the PARI C-library interface, it immediately copies each created
+the PARI C library interface, it immediately copies each created
 object off of the PARI stack, hence the stack never grows.  However,
 each object must not exceed 100MB in size, or the stack will overflow
 when the object is being created.  This extra copying does impose
`@``@` -3709,7 +3709,7 `@``@`
 Note that \sage will recompile \code{factorial.spyx} if you quit and
 restart \sage.  The compiled shared object library is stored under
 \code{\$HOME/.sage/temp/hostname/pid/spyx}.  These files are deleted
-when you exist \sage.
+when you exit \sage.

 {\em NO} \sage preparsing is applied to spyx files, e.g., \code{1/3}
 will result in 0 in a spyx file instead of the rational
`@``@` -3964,7 +3964,7 `@``@`

 \index{sequence!creating a}
 Sequences are a third list-oriented \SAGE type. Unlike lists and tuples,
-Sequence is not built--in Python type. By default, a sequence is
+sequence is not a built-in Python type. By default, a sequence is
 mutable, but using the \code{Sequence} class method
 \code{set_immutable}, it can be set to be immutable, as the following
 example illustrates. All elements of a sequence have a common parent,
`@``@` -4050,7 +4050,7 `@``@`
 sage: d.items()
 [(1, 5), ('sage', 17), (Integer Ring, Finite Field of size 7)]
 \end{verbatim}
-A common idiom is to iterate through the pairs of in a
+A common idiom is to iterate through the pairs in a
 dictionary:
 \begin{verbatim}
 sage: d = {2:4, 3:9, 4:16}
`@``@` -4216,9 +4216,9 `@``@`
 \end{verbatim}
 Of course this is not an efficient implementation
 of the Legendre symbol!  It is meant to illustrate
-various aspects of Python/SAGE programming.
+various aspects of Python/\SAGE programming.
 The function \code{kronecker}, which comes with
-SAGE, computes the Legendre symbol efficiently
+\SAGE, computes the Legendre symbol efficiently
 via a C-library call to PARI.

 \index{<=}\index{>=}
`@``@` -4269,7 +4269,7 `@``@`
 In the following two lines the first equality is \code{False} because
 there is no {\em canonical} morphism $\Q\to \F_5$, hence no canonical
 way to compare the $1$ in $\F_5$ to the $1 \in \Q$.  In contrast,
-there is a canonical map $\Z \to \F_5$, hence the second comparison is True.
+there is a canonical map $\Z \to \F_5$, hence the second comparison
is \code{True}.
 Note also that the order doesn't matter.
 \begin{verbatim}
 sage: GF(5)(1) == QQ(1); QQ(1) == GF(5)(1)
`@``@` -4643,7 +4643,7 `@``@`
 still obey the standard Python rules when writing packages that will
 be imported into \SAGE.

-\note{To install a random Python library that you find on the internet,
+\note{To install a random Python library that you find on the Internet,
 follow the directions, but run \code{sage -python} instead of \code{python}.
 Very often this means typing \code{sage -python setup.py install}.} 
```



---

Attachment


---

Comment by mabshoff created at 2008-01-13 18:46:20

Resolution: fixed


---

Comment by mabshoff created at 2008-01-13 18:46:20

Merged in Sage 2.10.alpha3


---

Comment by was created at 2008-01-14 05:55:48

All the suggested changes in this patch look good to me.
