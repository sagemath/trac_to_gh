# Issue 8242: Fix duplicate citation warnings when building the French-language tutorial

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-11 21:19:06

Assignee: mvngu

Ticket #7772 resolves these for the English-language tutorial.


```
bibliography.rst:27: WARNING: duplicate citation Py, other instance in afterword.rst
bibliography.rst:30: WARNING: duplicate citation PyDev, other instance in afterword.rst
interactive_shell.rst:974: WARNING: duplicate citation Py, other instance in bibliography.rst
interfaces.rst:357: WARNING: duplicate citation GAPkg, other instance in bibliography.rst
introduction.rst:155: WARNING: duplicate citation Dive, other instance in bibliography.rst
introduction.rst:158: WARNING: duplicate citation PyT, other instance in bibliography.rst
programming.rst:880: WARNING: duplicate citation PyT, other instance in introduction.rst
tour_algebra.rst:395: WARNING: duplicate citation GAP, other instance in bibliography.rst
tour_algebra.rst:397: WARNING: duplicate citation Max, other instance in bibliography.rst
tour_plotting.rst:187: WARNING: duplicate citation Jmol, other instance in bibliography.rst
tour_polynomial.rst:340: WARNING: duplicate citation Si, other instance in bibliography.rst
```



---

Comment by mmezzarobba created at 2010-02-25 16:38:15

Changing assignee from mvngu to mmezzarobba.


---

Attachment


---

Comment by mmezzarobba created at 2010-02-25 17:10:31

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-02-25 21:36:39

How can I review that patch (i.e., check the warning are no longer present)?

Also some typos are still present, for example `Parcourrez` should be `Parcourez`,
`composantes` should be `composants`.

Paul


---

Comment by zimmerma created at 2010-02-25 21:36:39

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-02-25 22:00:08

The answer to my question was (thanks Marc):

```
sage -docbuild fr/tutorial html
```

However some warnings still remain...


---

Comment by mvngu created at 2010-02-25 22:02:45

After applying the patch [trac_8242_duplicate_citations.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242_duplicate_citations.patch), I still received two warnings when rebuilding the HTML version of the French tutorial:

```
/dev/shm/mvngu/sandbox/sage-4.3.3/devel/sage/doc/fr/tutorial/programming.rst:: WARNING: citation not found: Cython
/dev/shm/mvngu/sandbox/sage-4.3.3/devel/sage/doc/fr/tutorial/programming.rst:: WARNING: citation not found: Pyrex
writing additional files... genindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 2 warnings.
```

The reviewer patch [trac_8242-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-reviewer.patch) fixes those two warnings and takes care of the typos reported by zimmerma. So only the reviewer patch needs some reviewing from anyone other than me. Once it gets a positive review, the whole ticket gets a positive review.


---

Comment by mvngu created at 2010-02-25 22:02:45

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-02-25 22:08:30

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-02-25 22:08:30

I just checked the reviewer patch and I get no warnings any more.
Thus a positive review.


---

Comment by mvngu created at 2010-03-01 21:23:43

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-03-01 21:23:43

The attachment [trac_8242_duplicate_citations.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242_duplicate_citations.patch) conflicts with ticket #8037, in particular the patch [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch) on that ticket. Here's the hunk failure resulting from first applying #8037, followed by the first patch on #8242:

```
[mvngu`@`sage sage-main]$ pwd
/dev/shm/mvngu/sandbox/sage-4.3.3-8242/devel/sage-main
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch && hg qpush
adding trac_8037_sagetex_french_tutorial.2.patch to series file
applying trac_8037_sagetex_french_tutorial.2.patch
now at: trac_8037_sagetex_french_tutorial.2.patch
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8242/trac_8242_duplicate_citations.patch && hg qpush
adding trac_8242_duplicate_citations.patch to series file
applying trac_8242_duplicate_citations.patch
patching file doc/fr/tutorial/introduction.rst
Hunk #1 FAILED at 62
1 out of 2 hunks FAILED -- saving rejects to file doc/fr/tutorial/introduction.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8242_duplicate_citations.patch
[mvngu`@`sage sage-main]$ cat doc/fr/tutorial/introduction.rst.rej
--- introduction.rst
+++ introduction.rst
`@``@` -63,7 +63,7 `@``@`
 
 Des instructions pour installer Sage sur votre ordinateur sont
 disponibles dans le guide d'installation (*Installation Guide*), dans
-la section documentation de la page web principale de Sage [Sage]_.
+la section documentation de la page web principale de Sage [SA]_.
 Nous nous limiterons ici à deux remarques.
 
 #. La version téléchargeable de Sage vient avec ses dépendances.
```

On the one hand, ticket #8037 wants to make the change

```diff
- la section documentation de la page web principale de Sage [SA]_.
+ la section documentation de la page web principale de Sage [Sage]_.
```

But the current ticket (i.e. #8242) wants to make the change

```diff
-la section documentation de la page web principale de Sage [Sage]_.
+la section documentation de la page web principale de Sage [SA]_.
```

The patches on this ticket needs to be rebased on top of #8037.


---

Attachment

rebased vs. Sage 4.3.4.alpha1


---

Comment by mvngu created at 2010-03-12 05:48:35

apply on top of previous


---

Comment by mvngu created at 2010-03-12 05:51:58

Changing status from needs_work to needs_review.


---

Attachment

I have rebased Marc's patch against Sage 4.3.4.alpha1. Now apply patches in this order:

 1. [trac_8242-citations-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-citations-rebased.patch)
 1. [trac_8242-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-reviewer.patch)
 
Both the rebased patch and my reviewer patch need reviewing by anyone but me. If they both get a positive review, then the whole ticket is good to go into Sage 4.3.4.rc0.


---

Comment by zimmerma created at 2010-03-12 07:25:52

I tried to apply the new patches but got a failure for the 2nd one:

```
applying /tmp/trac_8242-reviewer.patch
patching file doc/fr/tutorial/introduction.rst
Hunk #1 FAILED at 64
1 out of 1 hunks FAILED -- saving rejects to file doc/fr/tutorial/introduction.rst.rej
abort: patch failed to apply
```

Maybe I didn't have a clean 4.3.3. Can somebody else try?

Postfix: sorry, I see the patches should be applied to 4.3.4.alpha1. Sorry, I cannot review
patches based on alpha releases (not the time to compile them).


---

Comment by mmezzarobba created at 2010-03-26 20:57:28

The patches apply fine on top of 4.3.4 and there are no more duplicate citations warnings.


---

Comment by mmezzarobba created at 2010-03-26 20:57:28

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:06:18

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 20:06:18

Merged in 4.4.alpha0:

 - trac_8242-citations-rebased.patch
 - trac_8242-reviewer.patch
