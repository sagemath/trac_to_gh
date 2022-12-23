# Issue 7192: Translation of "A Tour Of Sage" to Spanish

archive/issues_007192.json:
```json
{
    "body": "Assignee: tba\n\nCC:  mforets kcrisman\n\n================\nUn Tour Por SAGE\n================\n\nEste es un tour por SAGE que sigue de cerca al Tour Por Mathematica\nque est\u00e1 al comienzo de el Libro de Mathematica.\n\n\nSAGE Como Una Calculadora\n=========================\n\nLa l\u00ednea de comandos de SAGE tiene un prompt ``sage:``; no necesitas agregarlo.\nSi utilizas el Notebook de SAGE, entonces coloca todo despu\u00e9s del \nprompt ``sage:``  en una celda de entrada de datos, y presiona shift-enter para computar la\nsalida correspondiente.\n\n::\n\n    sage: 3 + 5\n    8\n\nEl acento circunflejo ``^`` significa \"elevar a la potencia\".\n\n::\n\n    sage: 57.1 ^ 100\n    4.60904368661396e175\n\nComputamos el inverso de una matr\u00edz de :math:`2 \\times 2` en SAGE.\n\n::\n\n    sage: matrix([[1,2], [3,4]])^(-1)\n    [  -2    1]\n    [ 3/2 -1/2]\n\nAqu\u00ed integramos una funci\u00f3n simple.\n\n::\n\n    sage: x = var('x')   # crea una variable simb\u00f3lica\n    sage: integrate(sqrt(x)*sqrt(1+x), x)\n    1/4*((x + 1)<sup>(3/2)/x</sup>(3/2) + sqrt(x + 1)/sqrt(x))/((x + 1)<sup>2/x</sup>2 - 2*(x + 1)/x + 1) + 1/8*log(sqrt(x + 1)/sqrt(x) - 1) - 1/8*log(sqrt(x + 1)/sqrt(x) + 1)\n\nEsto le pide a SAGE que resuelva una ecuaci\u00f3n cuadr\u00e1tica. El simbolo ``==``\nrepresenta igualdad en SAGE.\n\n::\n\n    sage: a = var('a')\n    sage: S = solve(x^2 + x == a, x); S\n    [x == -1/2*sqrt(4*a + 1) - 1/2, x == 1/2*sqrt(4*a + 1) - 1/2]\n\nEl resultado es una lista de igualdades.\n\n.. link\n\n::\n\n    sage: S[0].rhs()\n    -1/2*sqrt(4*a + 1) - 1/2\n    sage: show(plot(sin(x) + sin(1.6*x), 0, 40))\n\n.. image:: sin_plot.*\n\n\nC\u00f3mputos Poderosos Con SAGE\n===========================\n\nPrimero creamos una matr\u00edz de :math:`500 \\times 500` con n\u00fameros\naleatorios.\n\n::\n\n    sage: m = random_matrix(RDF,500)\n\nLe lleva unos cuantos segundos a SAGE para computar los eigenvalores de la\nmatr\u00edz y trazarlos.\n\n.. link\n\n::\n\n    sage: e = m.eigenvalues()  #alrededor de 2 segundos\n    sage: w = [(i, abs(e[i])) for i in range(len(e))]\n    sage: show(points(w))\n\n.. image:: eigen_plot.*\n\n\nGr\u00e1cias a la Biblioteca GNU de Multiprecisi\u00f3n (GMP), SAGE puede manejar \nn\u00fameros muy grandes, hasta n\u00fameros con millones o billones de\nd\u00edgitos.\n\n::\n\n    sage: factorial(100)\n    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000\n    sage: n = factorial(1000000)  #alrededor de 2.5 seconds\n\nEsto calcula al menos 100 digitos de :math:`\\pi`.\n\n::\n\n    sage: N(pi, digits=100)\n    3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068\n\nEsto le pide a SAGE que factorice un polinomio en dos variables.\n\n::\n\n    sage: R.<x,y> = QQ[]\n    sage: F = factor(x^99 + y^99)\n    sage: F\n    (x + y) * (x^2 - x*y + y^2) * (x^6 - x<sup>3*y</sup>3 + y^6) * \n    (x^10 - x^9*y + x<sup>8*y</sup>2 - x<sup>7*y</sup>3 + x<sup>6*y</sup>4 - x<sup>5*y</sup>5 +\n     x<sup>4*y</sup>6 - x<sup>3*y</sup>7 + x<sup>2*y</sup>8 - x*y^9 + y^10) * \n    (x^20 + x^19*y - x<sup>17*y</sup>3 - x<sup>16*y</sup>4 + x<sup>14*y</sup>6 + x<sup>13*y</sup>7 -\n     x<sup>11*y</sup>9 - x<sup>10*y</sup>10 - x<sup>9*y</sup>11 + x<sup>7*y</sup>13 + x<sup>6*y</sup>14 - \n     x<sup>4*y</sup>16 - x<sup>3*y</sup>17 + x*y^19 + y^20) * (x^60 + x<sup>57*y</sup>3 -\n     x<sup>51*y</sup>9 - x<sup>48*y</sup>12 + x<sup>42*y</sup>18 + x<sup>39*y</sup>21 - x<sup>33*y</sup>27 - \n     x<sup>30*y</sup>30 - x<sup>27*y</sup>33 + x<sup>21*y</sup>39 + x<sup>18*y</sup>42 - x<sup>12*y</sup>48 -\n     x<sup>9*y</sup>51 + x<sup>3*y</sup>57 + y^60)\n    sage: F.expand()\n    x^99 + y^99\n\nA SAGE tan solo le lleva m\u00e9nos de 5 segundos para computar el n\u00famero de maneras de\nrepartir cien milliones como una suma de enteros positivos.\n\n::\n\n    sage: z = Partitions(10^8).cardinality() #alrededor de 4.5 seconds\n    sage: str(z)[:40]\n    '1760517045946249141360373894679135204009'\n\nAccesando Algoritmos en Sage\n============================\n\nCada vez que usas SAGE, estas accesando una de las m\u00e1s grandes\ncolecciones de algoritmos computacionales de c\u00f3digo abierto de el mundo entero.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7192\n\n",
    "created_at": "2009-10-12T03:30:28Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "Translation of \"A Tour Of Sage\" to Spanish",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7192",
    "user": "Loufer"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/7192





---

archive/issue_comments_059585.json:
```json
{
    "body": "Replying to [ticket:7192 Loufer]:\n> Folder:  .../en/a_tour_of_sage\n\nShould this say \".../es/a_tour_of_sage\"?",
    "created_at": "2009-10-12T04:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59585",
    "user": "jhpalmieri"
}
```

Replying to [ticket:7192 Loufer]:
> Folder:  .../en/a_tour_of_sage

Should this say ".../es/a_tour_of_sage"?



---

archive/issue_comments_059586.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> Should this say \".../es/a_tour_of_sage\"?\n\nThe attachment `index.rst` is a translation of \"A Tour of Sage\" to Spanish. Based upon this attachment, one needs to create a patch under the directory `SAGE_ROOT/devel/sage-main/doc/es`.",
    "created_at": "2009-10-12T04:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59586",
    "user": "mvngu"
}
```

Replying to [comment:2 jhpalmieri]:
> Should this say ".../es/a_tour_of_sage"?

The attachment `index.rst` is a translation of "A Tour of Sage" to Spanish. Based upon this attachment, one needs to create a patch under the directory `SAGE_ROOT/devel/sage-main/doc/es`.



---

archive/issue_comments_059587.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> Replying to [ticket:7192 Loufer]:\n> > Folder:  .../en/a_tour_of_sage\n> \n> Should this say \".../es/a_tour_of_sage\"?\n> \n\nWell, that's the folder where I grabbed the file from and then transformed it.\nIf it's in your plans to create a new folder \".../es/...\", that would be great.\n\nSorry for the omission.",
    "created_at": "2009-10-13T01:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59587",
    "user": "Loufer"
}
```

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

archive/issue_comments_059588.json:
```json
{
    "body": "Also, let me know if my capitalization of the word Sage to SAGE is fine\nwith you.",
    "created_at": "2009-10-13T01:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59588",
    "user": "Loufer"
}
```

Also, let me know if my capitalization of the word Sage to SAGE is fine
with you.



---

archive/issue_comments_059589.json:
```json
{
    "body": "Replying to [comment:5 Loufer]:\n> Also, let me know if my capitalization of the word Sage to SAGE is fine\n> with you.\n\nThe Sage computer algebra system used to be called \"SAGE\", which is an acronym for Software for Algebra and Geometry Experimentation. That acronym has been abandoned. You should only use \"Sage\" to refer to the Sage mathematics software at \n\nhttp://www.sagemath.org\n\nUsing the capitalization \"SAGE\" would only confuse people.",
    "created_at": "2009-10-13T01:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59589",
    "user": "mvngu"
}
```

Replying to [comment:5 Loufer]:
> Also, let me know if my capitalization of the word Sage to SAGE is fine
> with you.

The Sage computer algebra system used to be called "SAGE", which is an acronym for Software for Algebra and Geometry Experimentation. That acronym has been abandoned. You should only use "Sage" to refer to the Sage mathematics software at 

http://www.sagemath.org

Using the capitalization "SAGE" would only confuse people.



---

archive/issue_comments_059590.json:
```json
{
    "body": "Replying to [comment:6 mvngu]:\n\nO.K. I'll take care of it right away. Thanks Minh.",
    "created_at": "2009-10-13T01:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59590",
    "user": "Loufer"
}
```

Replying to [comment:6 mvngu]:

O.K. I'll take care of it right away. Thanks Minh.



---

archive/issue_comments_059591.json:
```json
{
    "body": "Acronym \"SAGE\" replaced by original \"Sage\"",
    "created_at": "2009-10-15T01:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59591",
    "user": "Loufer"
}
```

Acronym "SAGE" replaced by original "Sage"



---

archive/issue_comments_059592.json:
```json
{
    "body": "Attachment\n\nWhat is the status of this ticket? Is it ready for review?",
    "created_at": "2010-02-01T03:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59592",
    "user": "mvngu"
}
```

Attachment

What is the status of this ticket? Is it ready for review?



---

archive/issue_comments_059593.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2014-07-18T12:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59593",
    "user": "chapoton"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_059594.json:
```json
{
    "body": "Here is a git branch. There are some problems with the accents.\n----\nNew commits:",
    "created_at": "2014-07-18T12:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59594",
    "user": "chapoton"
}
```

Here is a git branch. There are some problems with the accents.
----
New commits:



---

archive/issue_comments_059595.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2014-07-18T12:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59595",
    "user": "chapoton"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_059596.json:
```json
{
    "body": "Changing keywords from \"\" to \"spanish\".",
    "created_at": "2014-07-18T12:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59596",
    "user": "chapoton"
}
```

Changing keywords from "" to "spanish".



---

archive/issue_comments_059597.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-07-18T20:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59597",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_059598.json:
```json
{
    "body": "Solved the problem with accents, needs review !",
    "created_at": "2014-07-18T20:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59598",
    "user": "chapoton"
}
```

Solved the problem with accents, needs review !



---

archive/issue_comments_059599.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-07-18T20:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59599",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059600.json:
```json
{
    "body": "I made some changes to sentences that didn't sound right to me at all. It is still not perfect, but i think now is much better.\n----\nNew commits:",
    "created_at": "2014-07-22T20:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59600",
    "user": "mmarco"
}
```

I made some changes to sentences that didn't sound right to me at all. It is still not perfect, but i think now is much better.
----
New commits:



---

archive/issue_comments_059601.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-07-22T20:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59601",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_059602.json:
```json
{
    "body": "Replying to [comment:18 mmarco]:\n> I made some changes to sentences that didn't sound right to me at all.\n> New commits:\n> ||[89d5285](http://git.sagemath.org/sage.git/commit/?id=89d52850de7945af570070719f8500c097762ae3)||`Corrected some errors, made some changes to unusual expressions.`||\n\nTypo: one of the changes has 'Acceciendo' for 'Accediendo'.",
    "created_at": "2014-07-23T04:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59602",
    "user": "slelievre"
}
```

Replying to [comment:18 mmarco]:
> I made some changes to sentences that didn't sound right to me at all.
> New commits:
> ||[89d5285](http://git.sagemath.org/sage.git/commit/?id=89d52850de7945af570070719f8500c097762ae3)||`Corrected some errors, made some changes to unusual expressions.`||

Typo: one of the changes has 'Acceciendo' for 'Accediendo'.



---

archive/issue_comments_059603.json:
```json
{
    "body": "It contains several errors \"matr\u00edz\", \"gr\u00e1cias\". Moreover I am not sure if it is a good idea to include this code. It looks like a copy of the mathematica book, so it could be seen as a copyright infringement.",
    "created_at": "2014-08-08T13:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59603",
    "user": "lftabera"
}
```

It contains several errors "matríz", "grácias". Moreover I am not sure if it is a good idea to include this code. It looks like a copy of the mathematica book, so it could be seen as a copyright infringement.



---

archive/issue_comments_059604.json:
```json
{
    "body": "Hello,\n\nif you have found some errors, please do correct them.\n\nAnd note that we already have en, de and fr versions of the same files.",
    "created_at": "2014-08-08T14:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59604",
    "user": "chapoton"
}
```

Hello,

if you have found some errors, please do correct them.

And note that we already have en, de and fr versions of the same files.



---

archive/issue_comments_059605.json:
```json
{
    "body": "> It contains several errors \"matr\u00edz\", \"gr\u00e1cias\". \nYes, I agree with chapoton - please do even just put a list of typos etc. here!  Thanks.",
    "created_at": "2014-11-13T14:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59605",
    "user": "kcrisman"
}
```

> It contains several errors "matríz", "grácias". 
Yes, I agree with chapoton - please do even just put a list of typos etc. here!  Thanks.



---

archive/issue_comments_059606.json:
```json
{
    "body": "Well, in fact I think that the en, de, fr versions should also be deleted. Moreover, the copy is incomplete and I think that it does not apport anything to the newby with respect to the other documentation.\n\nI will proofread the rest of the Spanish translations.",
    "created_at": "2014-11-15T12:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59606",
    "user": "lftabera"
}
```

Well, in fact I think that the en, de, fr versions should also be deleted. Moreover, the copy is incomplete and I think that it does not apport anything to the newby with respect to the other documentation.

I will proofread the rest of the Spanish translations.



---

archive/issue_comments_059607.json:
```json
{
    "body": "Changing component from documentation to translations.",
    "created_at": "2014-11-20T16:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59607",
    "user": "kcrisman"
}
```

Changing component from documentation to translations.



---

archive/issue_comments_059608.json:
```json
{
    "body": "Info needed on this issue.",
    "created_at": "2014-12-04T03:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59608",
    "user": "kcrisman"
}
```

Info needed on this issue.



---

archive/issue_comments_059609.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-12-04T03:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59609",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_059610.json:
```json
{
    "body": "Replying to [comment:28 kcrisman]:\n> Info needed on this issue.\n\ni'd like to review/wrap-up this ticket. notice there are still typos in the branch u/mmarco/ticket/7192\n\nhow to proceed? may i change needs_info -> needs_work and commit the changes? thanks",
    "created_at": "2017-04-01T10:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59610",
    "user": "mforets"
}
```

Replying to [comment:28 kcrisman]:
> Info needed on this issue.

i'd like to review/wrap-up this ticket. notice there are still typos in the branch u/mmarco/ticket/7192

how to proceed? may i change needs_info -> needs_work and commit the changes? thanks



---

archive/issue_comments_059611.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2017-04-01T13:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59611",
    "user": "tscrim"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_059612.json:
```json
{
    "body": "I don't see what the issue with comment:26 is. It is just currently what we have. Also, if it really did result in copyright infringement (see comment:21), I think that would have happened already.\n\n`@`mforets I would just start fixing the typos and finishing the translation.",
    "created_at": "2017-04-01T13:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59612",
    "user": "tscrim"
}
```

I don't see what the issue with comment:26 is. It is just currently what we have. Also, if it really did result in copyright infringement (see comment:21), I think that would have happened already.

`@`mforets I would just start fixing the typos and finishing the translation.



---

archive/issue_comments_059613.json:
```json
{
    "body": "Some Spanish reader should correct any remaining typos.\n----\nNew commits:",
    "created_at": "2017-08-26T14:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59613",
    "user": "chapoton"
}
```

Some Spanish reader should correct any remaining typos.
----
New commits:



---

archive/issue_comments_059614.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2017-08-26T14:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59614",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_059615.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2017-08-27T19:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59615",
    "user": "tscrim"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_059616.json:
```json
{
    "body": "I'm not a native Spanish speaker, but I do not see any obvious typos. However, perhaps one of the native speakers can double-check. Although if we don't hear anything in a week or so, I will set a positive review so we can get this in.",
    "created_at": "2017-08-27T19:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59616",
    "user": "tscrim"
}
```

I'm not a native Spanish speaker, but I do not see any obvious typos. However, perhaps one of the native speakers can double-check. Although if we don't hear anything in a week or so, I will set a positive review so we can get this in.



---

archive/issue_comments_059617.json:
```json
{
    "body": "hi, thanks for the efforts! yes, there are some typos:\n\n\n```\nde el Libro -> del Libro\n\nmatr\u00edz -> matriz\n\nmilliones -> millones\n\nalrededor de 4.5 seconds -> alrededor de 4.5 segundos\n\nAcceciendo a Distintos -> Accediendo a Distintos\n\nestas accediendo -> est\u00e1s accediendo \n```\n",
    "created_at": "2017-08-27T19:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59617",
    "user": "mforets"
}
```

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

archive/issue_comments_059618.json:
```json
{
    "body": "i'll push the changes myself in a moment",
    "created_at": "2017-08-27T19:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59618",
    "user": "mforets"
}
```

i'll push the changes myself in a moment



---

archive/issue_comments_059619.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-27T19:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59619",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_059620.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-08-27T19:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59620",
    "user": "mforets"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059621.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2017-08-28T15:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59621",
    "user": "chapoton"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_059622.json:
```json
{
    "body": "I am afraid that this now needs technical work, as the patchbot complains.",
    "created_at": "2017-08-28T15:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59622",
    "user": "chapoton"
}
```

I am afraid that this now needs technical work, as the patchbot complains.



---

archive/issue_comments_059623.json:
```json
{
    "body": "Probably needs this change in `conf.py`:\n\n```diff\n-sys.path.append(os.environ['SAGE_DOC'])\n+sys.path.append(os.environ['SAGE_DOC_SRC'])\n```\n",
    "created_at": "2017-08-28T15:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59623",
    "user": "tscrim"
}
```

Probably needs this change in `conf.py`:

```diff
-sys.path.append(os.environ['SAGE_DOC'])
+sys.path.append(os.environ['SAGE_DOC_SRC'])
```




---

archive/issue_comments_059624.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-28T16:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59624",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_059625.json:
```json
{
    "body": "let us wait for a patchbot and see",
    "created_at": "2017-08-28T16:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59625",
    "user": "chapoton"
}
```

let us wait for a patchbot and see



---

archive/issue_comments_059626.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-08-28T16:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59626",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059627.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-08-28T18:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59627",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059628.json:
```json
{
    "body": "patchbot looks good enough, I think",
    "created_at": "2017-08-28T18:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59628",
    "user": "chapoton"
}
```

patchbot looks good enough, I think



---

archive/issue_comments_059629.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-09-02T09:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7192#issuecomment-59629",
    "user": "vbraun"
}
```

Resolution: fixed
