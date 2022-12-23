# Issue 7192: Translation of "A Tour Of Sage" to Spanish

Issue created by migration from https://trac.sagemath.org/ticket/7192

Original creator: Loufer

Original creation time: 2009-10-12 03:30:28

Assignee: tba

CC:  mforets kcrisman

================
Un Tour Por SAGE
================

Este es un tour por SAGE que sigue de cerca al Tour Por Mathematica
que está al comienzo de el Libro de Mathematica.


SAGE Como Una Calculadora
=========================

La línea de comandos de SAGE tiene un prompt ``sage:``; no necesitas agregarlo.
Si utilizas el Notebook de SAGE, entonces coloca todo después del 
prompt ``sage:``  en una celda de entrada de datos, y presiona shift-enter para computar la
salida correspondiente.

::

    sage: 3 + 5
    8

El acento circunflejo ``^`` significa "elevar a la potencia".

::

    sage: 57.1 ^ 100
    4.60904368661396e175

Computamos el inverso de una matríz de :math:`2 \times 2` en SAGE.

::

    sage: matrix([[1,2], [3,4]])^(-1)
    [  -2    1]
    [ 3/2 -1/2]

Aquí integramos una función simple.

::

    sage: x = var('x')   # crea una variable simbólica
    sage: integrate(sqrt(x)*sqrt(1+x), x)
    1/4*((x + 1)<sup>(3/2)/x</sup>(3/2) + sqrt(x + 1)/sqrt(x))/((x + 1)<sup>2/x</sup>2 - 2*(x + 1)/x + 1) + 1/8*log(sqrt(x + 1)/sqrt(x) - 1) - 1/8*log(sqrt(x + 1)/sqrt(x) + 1)

Esto le pide a SAGE que resuelva una ecuación cuadrática. El simbolo ``==``
representa igualdad en SAGE.

::

    sage: a = var('a')
    sage: S = solve(x^2 + x == a, x); S
    [x == -1/2*sqrt(4*a + 1) - 1/2, x == 1/2*sqrt(4*a + 1) - 1/2]

El resultado es una lista de igualdades.

.. link

::

    sage: S[0].rhs()
    -1/2*sqrt(4*a + 1) - 1/2
    sage: show(plot(sin(x) + sin(1.6*x), 0, 40))

.. image:: sin_plot.*


Cómputos Poderosos Con SAGE
===========================

Primero creamos una matríz de :math:`500 \times 500` con números
aleatorios.

::

    sage: m = random_matrix(RDF,500)

Le lleva unos cuantos segundos a SAGE para computar los eigenvalores de la
matríz y trazarlos.

.. link

::

    sage: e = m.eigenvalues()  #alrededor de 2 segundos
    sage: w = [(i, abs(e[i])) for i in range(len(e))]
    sage: show(points(w))

.. image:: eigen_plot.*


Grácias a la Biblioteca GNU de Multiprecisión (GMP), SAGE puede manejar 
números muy grandes, hasta números con millones o billones de
dígitos.

::

    sage: factorial(100)
    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    sage: n = factorial(1000000)  #alrededor de 2.5 seconds

Esto calcula al menos 100 digitos de :math:`\pi`.

::

    sage: N(pi, digits=100)
    3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068

Esto le pide a SAGE que factorice un polinomio en dos variables.

::

    sage: R.<x,y> = QQ[]
    sage: F = factor(x^99 + y^99)
    sage: F
    (x + y) * (x^2 - x*y + y^2) * (x^6 - x<sup>3*y</sup>3 + y^6) * 
    (x^10 - x^9*y + x<sup>8*y</sup>2 - x<sup>7*y</sup>3 + x<sup>6*y</sup>4 - x<sup>5*y</sup>5 +
     x<sup>4*y</sup>6 - x<sup>3*y</sup>7 + x<sup>2*y</sup>8 - x*y^9 + y^10) * 
    (x^20 + x^19*y - x<sup>17*y</sup>3 - x<sup>16*y</sup>4 + x<sup>14*y</sup>6 + x<sup>13*y</sup>7 -
     x<sup>11*y</sup>9 - x<sup>10*y</sup>10 - x<sup>9*y</sup>11 + x<sup>7*y</sup>13 + x<sup>6*y</sup>14 - 
     x<sup>4*y</sup>16 - x<sup>3*y</sup>17 + x*y^19 + y^20) * (x^60 + x<sup>57*y</sup>3 -
     x<sup>51*y</sup>9 - x<sup>48*y</sup>12 + x<sup>42*y</sup>18 + x<sup>39*y</sup>21 - x<sup>33*y</sup>27 - 
     x<sup>30*y</sup>30 - x<sup>27*y</sup>33 + x<sup>21*y</sup>39 + x<sup>18*y</sup>42 - x<sup>12*y</sup>48 -
     x<sup>9*y</sup>51 + x<sup>3*y</sup>57 + y^60)
    sage: F.expand()
    x^99 + y^99

A SAGE tan solo le lleva ménos de 5 segundos para computar el número de maneras de
repartir cien milliones como una suma de enteros positivos.

::

    sage: z = Partitions(10^8).cardinality() #alrededor de 4.5 seconds
    sage: str(z)[:40]
    '1760517045946249141360373894679135204009'

Accesando Algoritmos en Sage
============================

Cada vez que usas SAGE, estas accesando una de las más grandes
colecciones de algoritmos computacionales de código abierto de el mundo entero.


---

Comment by jhpalmieri created at 2009-10-12 04:03:46

Replying to [ticket:7192 Loufer]:
> Folder:  .../en/a_tour_of_sage

Should this say ".../es/a_tour_of_sage"?


---

Comment by mvngu created at 2009-10-12 04:10:49

Replying to [comment:2 jhpalmieri]:
> Should this say ".../es/a_tour_of_sage"?

The attachment `index.rst` is a translation of "A Tour of Sage" to Spanish. Based upon this attachment, one needs to create a patch under the directory `SAGE_ROOT/devel/sage-main/doc/es`.


---

Comment by Loufer created at 2009-10-13 01:11:49

Replying to [comment:2 jhpalmieri]:
> Replying to [ticket:7192 Loufer]:
> > Folder:  .../en/a_tour_of_sage
> 
> Should this say ".../es/a_tour_of_sage"?
> 

Well, that's the folder where I grabbed the file from and then transformed it.
If it's in your plans to create a new folder ".../es/...", that would be great.

Sorry for the omission.


---

Comment by Loufer created at 2009-10-13 01:19:29

Also, let me know if my capitalization of the word Sage to SAGE is fine
with you.


---

Comment by mvngu created at 2009-10-13 01:23:18

Replying to [comment:5 Loufer]:
> Also, let me know if my capitalization of the word Sage to SAGE is fine
> with you.

The Sage computer algebra system used to be called "SAGE", which is an acronym for Software for Algebra and Geometry Experimentation. That acronym has been abandoned. You should only use "Sage" to refer to the Sage mathematics software at 

http://www.sagemath.org

Using the capitalization "SAGE" would only confuse people.


---

Comment by Loufer created at 2009-10-13 01:27:56

Replying to [comment:6 mvngu]:

O.K. I'll take care of it right away. Thanks Minh.


---

Comment by Loufer created at 2009-10-15 01:02:46

Acronym "SAGE" replaced by original "Sage"


---

Attachment

What is the status of this ticket? Is it ready for review?


---

Comment by chapoton created at 2014-07-18 12:46:40

Changing status from new to needs_info.


---

Comment by chapoton created at 2014-07-18 12:46:40

Here is a git branch. There are some problems with the accents.
----
New commits:


---

Comment by chapoton created at 2014-07-18 12:48:43

Changing status from needs_info to needs_work.


---

Comment by chapoton created at 2014-07-18 12:48:43

Changing keywords from "" to "spanish".


---

Comment by git created at 2014-07-18 20:32:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-07-18 20:34:07

Solved the problem with accents, needs review !


---

Comment by chapoton created at 2014-07-18 20:34:07

Changing status from needs_work to needs_review.


---

Comment by mmarco created at 2014-07-22 20:23:03

I made some changes to sentences that didn't sound right to me at all. It is still not perfect, but i think now is much better.
----
New commits:


---

Comment by git created at 2014-07-22 20:24:48

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by slelievre created at 2014-07-23 04:21:17

Replying to [comment:18 mmarco]:
> I made some changes to sentences that didn't sound right to me at all.
> New commits:
> ||[89d5285](http://git.sagemath.org/sage.git/commit/?id=89d52850de7945af570070719f8500c097762ae3)||`Corrected some errors, made some changes to unusual expressions.`||

Typo: one of the changes has 'Acceciendo' for 'Accediendo'.


---

Comment by lftabera created at 2014-08-08 13:38:32

It contains several errors "matríz", "grácias". Moreover I am not sure if it is a good idea to include this code. It looks like a copy of the mathematica book, so it could be seen as a copyright infringement.


---

Comment by chapoton created at 2014-08-08 14:24:05

Hello,

if you have found some errors, please do correct them.

And note that we already have en, de and fr versions of the same files.


---

Comment by kcrisman created at 2014-11-13 14:37:23

> It contains several errors "matríz", "grácias". 
Yes, I agree with chapoton - please do even just put a list of typos etc. here!  Thanks.


---

Comment by lftabera created at 2014-11-15 12:00:18

Well, in fact I think that the en, de, fr versions should also be deleted. Moreover, the copy is incomplete and I think that it does not apport anything to the newby with respect to the other documentation.

I will proofread the rest of the Spanish translations.


---

Comment by kcrisman created at 2014-11-20 16:35:22

Changing component from documentation to translations.


---

Comment by kcrisman created at 2014-12-04 03:37:57

Info needed on this issue.


---

Comment by kcrisman created at 2014-12-04 03:37:57

Changing status from needs_review to needs_info.


---

Comment by mforets created at 2017-04-01 10:12:02

Replying to [comment:28 kcrisman]:
> Info needed on this issue.

i'd like to review/wrap-up this ticket. notice there are still typos in the branch u/mmarco/ticket/7192

how to proceed? may i change needs_info -> needs_work and commit the changes? thanks


---

Comment by tscrim created at 2017-04-01 13:56:42

Changing status from needs_info to needs_work.


---

Comment by tscrim created at 2017-04-01 13:56:42

I don't see what the issue with comment:26 is. It is just currently what we have. Also, if it really did result in copyright infringement (see comment:21), I think that would have happened already.

`@`mforets I would just start fixing the typos and finishing the translation.


---

Comment by chapoton created at 2017-08-26 14:22:57

Some Spanish reader should correct any remaining typos.
----
New commits:


---

Comment by chapoton created at 2017-08-26 14:22:57

Changing status from needs_work to needs_info.


---

Comment by tscrim created at 2017-08-27 19:06:58

Changing status from needs_info to needs_review.


---

Comment by tscrim created at 2017-08-27 19:06:58

I'm not a native Spanish speaker, but I do not see any obvious typos. However, perhaps one of the native speakers can double-check. Although if we don't hear anything in a week or so, I will set a positive review so we can get this in.


---

Comment by mforets created at 2017-08-27 19:15:50

hi, thanks for the efforts! yes, there are some typos:


```
de el Libro -> del Libro

matríz -> matriz

milliones -> millones

alrededor de 4.5 seconds -> alrededor de 4.5 segundos

Acceciendo a Distintos -> Accediendo a Distintos

estas accediendo -> estás accediendo 
```



---

Comment by mforets created at 2017-08-27 19:21:47

i'll push the changes myself in a moment


---

Comment by git created at 2017-08-27 19:28:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mforets created at 2017-08-27 19:29:17

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2017-08-28 15:26:52

Changing status from positive_review to needs_work.


---

Comment by chapoton created at 2017-08-28 15:26:52

I am afraid that this now needs technical work, as the patchbot complains.


---

Comment by tscrim created at 2017-08-28 15:37:57

Probably needs this change in `conf.py`:

```diff
-sys.path.append(os.environ['SAGE_DOC'])
+sys.path.append(os.environ['SAGE_DOC_SRC'])
```



---

Comment by git created at 2017-08-28 16:35:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-08-28 16:36:24

let us wait for a patchbot and see


---

Comment by chapoton created at 2017-08-28 16:36:24

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2017-08-28 18:26:32

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2017-08-28 18:26:32

patchbot looks good enough, I think


---

Comment by vbraun created at 2017-09-02 09:34:15

Resolution: fixed
