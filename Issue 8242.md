# Issue 8242: Fix duplicate citation warnings when building the French-language tutorial

archive/issues_008242.json:
```json
{
    "body": "Assignee: mvngu\n\nTicket #7772 resolves these for the English-language tutorial.\n\n\n```\nbibliography.rst:27: WARNING: duplicate citation Py, other instance in afterword.rst\nbibliography.rst:30: WARNING: duplicate citation PyDev, other instance in afterword.rst\ninteractive_shell.rst:974: WARNING: duplicate citation Py, other instance in bibliography.rst\ninterfaces.rst:357: WARNING: duplicate citation GAPkg, other instance in bibliography.rst\nintroduction.rst:155: WARNING: duplicate citation Dive, other instance in bibliography.rst\nintroduction.rst:158: WARNING: duplicate citation PyT, other instance in bibliography.rst\nprogramming.rst:880: WARNING: duplicate citation PyT, other instance in introduction.rst\ntour_algebra.rst:395: WARNING: duplicate citation GAP, other instance in bibliography.rst\ntour_algebra.rst:397: WARNING: duplicate citation Max, other instance in bibliography.rst\ntour_plotting.rst:187: WARNING: duplicate citation Jmol, other instance in bibliography.rst\ntour_polynomial.rst:340: WARNING: duplicate citation Si, other instance in bibliography.rst\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8242\n\n",
    "created_at": "2010-02-11T21:19:06Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Fix duplicate citation warnings when building the French-language tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8242",
    "user": "https://github.com/qed777"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/8242





---

archive/issue_comments_072749.json:
```json
{
    "body": "Changing assignee from mvngu to @mezzarobba.",
    "created_at": "2010-02-25T16:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72749",
    "user": "https://github.com/mezzarobba"
}
```

Changing assignee from mvngu to @mezzarobba.



---

archive/issue_comments_072750.json:
```json
{
    "body": "Attachment [trac_8242_duplicate_citations.patch](tarball://root/attachments/some-uuid/ticket8242/trac_8242_duplicate_citations.patch) by @mezzarobba created at 2010-02-25 17:10:14",
    "created_at": "2010-02-25T17:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72750",
    "user": "https://github.com/mezzarobba"
}
```

Attachment [trac_8242_duplicate_citations.patch](tarball://root/attachments/some-uuid/ticket8242/trac_8242_duplicate_citations.patch) by @mezzarobba created at 2010-02-25 17:10:14



---

archive/issue_comments_072751.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T17:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72751",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072752.json:
```json
{
    "body": "How can I review that patch (i.e., check the warning are no longer present)?\n\nAlso some typos are still present, for example `Parcourrez` should be `Parcourez`,\n`composantes` should be `composants`.\n\nPaul",
    "created_at": "2010-02-25T21:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72752",
    "user": "https://github.com/zimmermann6"
}
```

How can I review that patch (i.e., check the warning are no longer present)?

Also some typos are still present, for example `Parcourrez` should be `Parcourez`,
`composantes` should be `composants`.

Paul



---

archive/issue_comments_072753.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-25T21:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72753",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072754.json:
```json
{
    "body": "The answer to my question was (thanks Marc):\n\n```\nsage -docbuild fr/tutorial html\n```\n\nHowever some warnings still remain...",
    "created_at": "2010-02-25T22:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72754",
    "user": "https://github.com/zimmermann6"
}
```

The answer to my question was (thanks Marc):

```
sage -docbuild fr/tutorial html
```

However some warnings still remain...



---

archive/issue_comments_072755.json:
```json
{
    "body": "After applying the patch [trac_8242_duplicate_citations.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242_duplicate_citations.patch), I still received two warnings when rebuilding the HTML version of the French tutorial:\n\n```\n/dev/shm/mvngu/sandbox/sage-4.3.3/devel/sage/doc/fr/tutorial/programming.rst:: WARNING: citation not found: Cython\n/dev/shm/mvngu/sandbox/sage-4.3.3/devel/sage/doc/fr/tutorial/programming.rst:: WARNING: citation not found: Pyrex\nwriting additional files... genindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 2 warnings.\n```\n\nThe reviewer patch [trac_8242-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-reviewer.patch) fixes those two warnings and takes care of the typos reported by zimmerma. So only the reviewer patch needs some reviewing from anyone other than me. Once it gets a positive review, the whole ticket gets a positive review.",
    "created_at": "2010-02-25T22:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72755",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_072756.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-25T22:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72756",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072757.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T22:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72757",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072758.json:
```json
{
    "body": "I just checked the reviewer patch and I get no warnings any more.\nThus a positive review.",
    "created_at": "2010-02-25T22:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72758",
    "user": "https://github.com/zimmermann6"
}
```

I just checked the reviewer patch and I get no warnings any more.
Thus a positive review.



---

archive/issue_comments_072759.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-01T21:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072760.json:
```json
{
    "body": "The attachment [trac_8242_duplicate_citations.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242_duplicate_citations.patch) conflicts with ticket #8037, in particular the patch [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch) on that ticket. Here's the hunk failure resulting from first applying #8037, followed by the first patch on #8242:\n\n```\n[mvngu@sage sage-main]$ pwd\n/dev/shm/mvngu/sandbox/sage-4.3.3-8242/devel/sage-main\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch && hg qpush\nadding trac_8037_sagetex_french_tutorial.2.patch to series file\napplying trac_8037_sagetex_french_tutorial.2.patch\nnow at: trac_8037_sagetex_french_tutorial.2.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8242/trac_8242_duplicate_citations.patch && hg qpush\nadding trac_8242_duplicate_citations.patch to series file\napplying trac_8242_duplicate_citations.patch\npatching file doc/fr/tutorial/introduction.rst\nHunk #1 FAILED at 62\n1 out of 2 hunks FAILED -- saving rejects to file doc/fr/tutorial/introduction.rst.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8242_duplicate_citations.patch\n[mvngu@sage sage-main]$ cat doc/fr/tutorial/introduction.rst.rej\n--- introduction.rst\n+++ introduction.rst\n@@ -63,7 +63,7 @@\n \n Des instructions pour installer Sage sur votre ordinateur sont\n disponibles dans le guide d'installation (*Installation Guide*), dans\n-la section documentation de la page web principale de Sage [Sage]_.\n+la section documentation de la page web principale de Sage [SA]_.\n Nous nous limiterons ici \u00e0 deux remarques.\n \n #. La version t\u00e9l\u00e9chargeable de Sage vient avec ses d\u00e9pendances.\n```\n\nOn the one hand, ticket #8037 wants to make the change\n\n```diff\n- la section documentation de la page web principale de Sage [SA]_.\n+ la section documentation de la page web principale de Sage [Sage]_.\n```\n\nBut the current ticket (i.e. #8242) wants to make the change\n\n```diff\n-la section documentation de la page web principale de Sage [Sage]_.\n+la section documentation de la page web principale de Sage [SA]_.\n```\n\nThe patches on this ticket needs to be rebased on top of #8037.",
    "created_at": "2010-03-01T21:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The attachment [trac_8242_duplicate_citations.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242_duplicate_citations.patch) conflicts with ticket #8037, in particular the patch [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch) on that ticket. Here's the hunk failure resulting from first applying #8037, followed by the first patch on #8242:

```
[mvngu@sage sage-main]$ pwd
/dev/shm/mvngu/sandbox/sage-4.3.3-8242/devel/sage-main
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch && hg qpush
adding trac_8037_sagetex_french_tutorial.2.patch to series file
applying trac_8037_sagetex_french_tutorial.2.patch
now at: trac_8037_sagetex_french_tutorial.2.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8242/trac_8242_duplicate_citations.patch && hg qpush
adding trac_8242_duplicate_citations.patch to series file
applying trac_8242_duplicate_citations.patch
patching file doc/fr/tutorial/introduction.rst
Hunk #1 FAILED at 62
1 out of 2 hunks FAILED -- saving rejects to file doc/fr/tutorial/introduction.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8242_duplicate_citations.patch
[mvngu@sage sage-main]$ cat doc/fr/tutorial/introduction.rst.rej
--- introduction.rst
+++ introduction.rst
@@ -63,7 +63,7 @@
 
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

archive/issue_comments_072761.json:
```json
{
    "body": "Attachment [trac_8242-citations-rebased.patch](tarball://root/attachments/some-uuid/ticket8242/trac_8242-citations-rebased.patch) by mvngu created at 2010-03-12 05:48:11\n\nrebased vs. Sage 4.3.4.alpha1",
    "created_at": "2010-03-12T05:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8242-citations-rebased.patch](tarball://root/attachments/some-uuid/ticket8242/trac_8242-citations-rebased.patch) by mvngu created at 2010-03-12 05:48:11

rebased vs. Sage 4.3.4.alpha1



---

archive/issue_comments_072762.json:
```json
{
    "body": "apply on top of previous",
    "created_at": "2010-03-12T05:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72762",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

apply on top of previous



---

archive/issue_comments_072763.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-12T05:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072764.json:
```json
{
    "body": "Attachment [trac_8242-reviewer.patch](tarball://root/attachments/some-uuid/ticket8242/trac_8242-reviewer.patch) by mvngu created at 2010-03-12 05:51:58\n\nI have rebased Marc's patch against Sage 4.3.4.alpha1. Now apply patches in this order:\n\n1. [trac_8242-citations-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-citations-rebased.patch)\n2. [trac_8242-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-reviewer.patch)\n \nBoth the rebased patch and my reviewer patch need reviewing by anyone but me. If they both get a positive review, then the whole ticket is good to go into Sage 4.3.4.rc0.",
    "created_at": "2010-03-12T05:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8242-reviewer.patch](tarball://root/attachments/some-uuid/ticket8242/trac_8242-reviewer.patch) by mvngu created at 2010-03-12 05:51:58

I have rebased Marc's patch against Sage 4.3.4.alpha1. Now apply patches in this order:

1. [trac_8242-citations-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-citations-rebased.patch)
2. [trac_8242-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8242/trac_8242-reviewer.patch)
 
Both the rebased patch and my reviewer patch need reviewing by anyone but me. If they both get a positive review, then the whole ticket is good to go into Sage 4.3.4.rc0.



---

archive/issue_comments_072765.json:
```json
{
    "body": "I tried to apply the new patches but got a failure for the 2nd one:\n\n```\napplying /tmp/trac_8242-reviewer.patch\npatching file doc/fr/tutorial/introduction.rst\nHunk #1 FAILED at 64\n1 out of 1 hunks FAILED -- saving rejects to file doc/fr/tutorial/introduction.rst.rej\nabort: patch failed to apply\n```\n\nMaybe I didn't have a clean 4.3.3. Can somebody else try?\n\nPostfix: sorry, I see the patches should be applied to 4.3.4.alpha1. Sorry, I cannot review\npatches based on alpha releases (not the time to compile them).",
    "created_at": "2010-03-12T07:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72765",
    "user": "https://github.com/zimmermann6"
}
```

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

archive/issue_comments_072766.json:
```json
{
    "body": "The patches apply fine on top of 4.3.4 and there are no more duplicate citations warnings.",
    "created_at": "2010-03-26T20:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72766",
    "user": "https://github.com/mezzarobba"
}
```

The patches apply fine on top of 4.3.4 and there are no more duplicate citations warnings.



---

archive/issue_comments_072767.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-26T20:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72767",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072768.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72768",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_008443.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T20:06:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8242#event-8443"
}
```



---

archive/issue_comments_072769.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_8242-citations-rebased.patch\n- trac_8242-reviewer.patch",
    "created_at": "2010-04-15T20:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8242#issuecomment-72769",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_8242-citations-rebased.patch
- trac_8242-reviewer.patch
