# Issue 26: add docs to eigenvectors function.

Issue created by migration from https://trac.sagemath.org/ticket/26

Original creator: was

Original creation time: 2006-09-12 23:24:32

Assignee: somebody




---

Comment by mabshoff created at 2007-08-22 19:42:01

Changing assignee from somebody to tba.


---

Comment by mabshoff created at 2007-08-22 19:42:01

Changing component from basic arithmetic to documentation.


---

Comment by mabshoff created at 2007-08-23 12:58:23

This is still a problem with Sage 2.8.2:

```
sage: search_doc(Eigenvector)
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<ipython console> in <module>()

<type 'exceptions.NameError'>: name 'Eigenvector' is not defined
sage: search_doc(eigenvector)
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<ipython console> in <module>()

<type 'exceptions.NameError'>: name 'eigenvector' is not defined
sage: search_doc(eigenvectors)
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<ipython console> in <module>()

<type 'exceptions.NameError'>: name 'eigenvectors' is not defined
```


Cheers,

Michael


---

Comment by mhansen created at 2007-12-06 21:17:27

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-06 21:17:27

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2007-12-07 03:17:28

I think this is invalid.



```
sage: search_doc('eigenvector')
const/node32.html:5.4 Eigenvectors and eigenvalues
const/node32.html:How do you compute eigenvalues and eigenvectors using <I CLASS="sans">SAGE</I>?
const/node32.html:sage: eig = A.eigenvectors()
const/node32.html: is an eigenvector of <!-- MATH
const/node32.html: is an eigenvector of <!-- MATH
const/node32.html:sage: A.eigenvectors()
const/node32.html:sage: A.eigenvectors()
const/node32.html:``rational'' eigenvalues and eigenvectors:
const/node32.html:sage: gap.eval("v := Eigenvectors( Rationals,A)")
const/node33.html:<td class='online-navigation'><a rel="prev" title="5.4 Eigenvectors and eigenvalues"
const/node33.html:<a class="sectref" rel="prev" href="node32.html">5.4 Eigenvectors and eigenvalues</A>
const/node33.html:<td class='online-navigation'><a rel="prev" title="5.4 Eigenvectors and eigenvalues"
const/node33.html:<a class="sectref" rel="prev" href="node32.html">5.4 Eigenvectors and eigenvalues</A>
ref/genindex.html:<dt><a href="module-sage.modular.hecke.module.html#l2h-7427">dual_eigenvector() (in module sage.modular.hecke.module)</a>
ref/module-sage.libs.pari.all.html:sage: A.eigenvectors()
ref/module-sage.matrix.matrix2.html:        algorithm that is in dual_eigenvector in sage/modular/hecke/module.py.
ref/module-sage.matrix.matrix-complex-double-dense.html:    of eigenvalues and the e is a matrix whose columns are the eigenvectors.
ref/module-sage.matrix.matrix-complex-double-dense.html:<EM>Computes the eigenvalues and eigenvectors of this matrix acting
ref/module-sage.matrix.matrix-complex-double-dense.html:             corresponding eigenvectors - as a matrix whose ** ROWS ** are the eigenvectors of
ref/module-sage.matrix.matrix-complex-double-dense.html:<EM>Computes the eigenvalues and eigenvectors of this matrix acting
ref/module-sage.matrix.matrix-complex-double-dense.html:             corresponding eigenvectors - as a matrix whose ** COLUMNS ** are the eigenvectors of
ref/module-sage.matrix.matrix-complex-double-dense.html:<EM>Computes the eigenvalues and eigenvectors of this matrix acting
ref/module-sage.matrix.matrix-real-double-dense.html:<EM>Computes the eigenvalues and *right* eigenvectors of this
ref/module-sage.matrix.matrix-real-double-dense.html:             corresponding eigenvectors - as an RDF matrix whose columns
ref/module-sage.matrix.matrix-real-double-dense.html:                           are the eigenvectors.
ref/module-sage.modular.hecke.module.html: <tt class="method">dual_eigenvector</tt>,<SPAN CLASS="MATH"><IMG
ref/module-sage.modular.hecke.module.html:  <td><nobr><b><tt id='l2h-7427' xml:id='l2h-7427' class="function">dual_eigenvector</tt></b>(</nobr></td>
ref/module-sage.modular.hecke.module.html:Return an eigenvector for the Hecke operators acting on the
ref/module-sage.modular.hecke.module.html:        linear dual of this space.  This eigenvector will have entries
ref/module-sage.modular.hecke.module.html:    ring.  This vector is an eigenvector for all Hecke operators
ref/module-sage.modular.hecke.module.html:            eigenvector.  This function is used mainly for computing
ref/module-sage.modular.hecke.module.html:<EM>(2) One can also view a dual eigenvector as defining (via
ref/module-sage.modular.hecke.module.html:            eigenvector for the dual action of Hecke operators on
ref/module-sage.modular.modform.numerical.html: <tt class="method">_eigenvectors</tt>,<SPAN CLASS="MATH"><IMG
ref/module-sage.modular.modform.numerical.html:Return a very sparse vector v such that v times the eigenvector matrix
ref/module-sage.modular.modsym.space.html:            'eigen' -- compute basis using eigenvectors for the Hecke
tut/node17.html:<I CLASS="sans">SAGE</I> can compute eigenvalues and eigenvectors:
tut/node17.html:Eigenvalues and eigenvectors over <!-- MATH
tut/node44.html:matrices (such as row reduction, eigenvalues and eigenvectors), and
tut/node44.html:sage: A.eigenvectors()
tut/node44.html:sage: eigA = A.eigenvectors()
```



---

Comment by rlm created at 2007-12-22 18:35:41

Resolution: invalid
