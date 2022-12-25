# Issue 8118: split off Galois representations and modular parametrization from ell_rational_field.py

archive/issues_008118.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona @williamstein @robertwb @roed314\n\nKeywords: elliptic curve, galois representation, modular parametrization\n\nThe file ell_rational_field.py is huge and should be split up further. This is especially important for the documentation, currently it is not very user-friendy to find a function in the reference.\n\nI propose a first change.\n\n* The modular paratrization class goes into a separate file. (maybe the modular_degree should mover there too ?)\n\n* The functions concerning the Galois representation are moved to a separate field. I changed the functions like `is_surjective` and `is_irreducible` to deprecated. I believe for instance the latter clashes with the irreducibility of the scheme E.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8118\n\n",
    "created_at": "2010-01-29T15:05:17Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "split off Galois representations and modular parametrization from ell_rational_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8118",
    "user": "https://github.com/categorie"
}
```
Assignee: @aghitza

CC:  @JohnCremona @williamstein @robertwb @roed314

Keywords: elliptic curve, galois representation, modular parametrization

The file ell_rational_field.py is huge and should be split up further. This is especially important for the documentation, currently it is not very user-friendy to find a function in the reference.

I propose a first change.

* The modular paratrization class goes into a separate file. (maybe the modular_degree should mover there too ?)

* The functions concerning the Galois representation are moved to a separate field. I changed the functions like `is_surjective` and `is_irreducible` to deprecated. I believe for instance the latter clashes with the irreducibility of the scheme E.

Issue created by migration from https://trac.sagemath.org/ticket/8118





---

archive/issue_comments_071184.json:
```json
{
    "body": "This patch is my first proposal for changes.\n\nIt will also allow me to work more on the Galois representation side. For instance I deleted the second output of non-surjective since it was not used anywhere. I will build this in later in a different way, while also improving the outputs.\n\nLet me know if you think these changes go too far.\n\nWhat was the decision on deprecation policy of sage ? Is my handling here the correct one ?\n\nWhat is a ``TestSuite(s).run()` doctest.` ? Where do I find the information on that ?\n\nI have first to test it myself, before I set it to \"needs review\".",
    "created_at": "2010-01-29T15:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71184",
    "user": "https://github.com/categorie"
}
```

This patch is my first proposal for changes.

It will also allow me to work more on the Galois representation side. For instance I deleted the second output of non-surjective since it was not used anywhere. I will build this in later in a different way, while also improving the outputs.

Let me know if you think these changes go too far.

What was the decision on deprecation policy of sage ? Is my handling here the correct one ?

What is a ``TestSuite(s).run()` doctest.` ? Where do I find the information on that ?

I have first to test it myself, before I set it to "needs review".



---

archive/issue_comments_071185.json:
```json
{
    "body": "Changing assignee from @aghitza to @JohnCremona.",
    "created_at": "2010-01-29T15:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71185",
    "user": "https://github.com/categorie"
}
```

Changing assignee from @aghitza to @JohnCremona.



---

archive/issue_comments_071186.json:
```json
{
    "body": "Changing component from algebra to elliptic curves.",
    "created_at": "2010-01-29T15:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71186",
    "user": "https://github.com/categorie"
}
```

Changing component from algebra to elliptic curves.



---

archive/issue_comments_071187.json:
```json
{
    "body": "I approve of this, though I don't have time to look at the patch right now.",
    "created_at": "2010-01-29T16:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71187",
    "user": "https://github.com/JohnCremona"
}
```

I approve of this, though I don't have time to look at the patch right now.



---

archive/issue_comments_071188.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-01T23:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71188",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071189.json:
```json
{
    "body": "I don't understand this. I exported the patch after adding the two new files to hg. Then I apply it to a new clone.\n\n The patch applies fine and the tests pass. But when I do -docbuild reference html it tells me that it can not find the new files :\n\n\n```\n /usr/local/sage/devel/sage/doc/en/reference/plane_curves.rst:7: (WARNING/2) toctree references unknown document u'sage/schemes/elliptic_curves/modular_parametrization'                                 \n/usr/local/sage/devel/sage/doc/en/reference/plane_curves.rst:7: (WARNING/2) toctree references unknown document u'sage/schemes/elliptic_curves/gal_reps'     \n```\n\n\n I must be doing something stupidly wrong. Help !",
    "created_at": "2010-02-01T23:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71189",
    "user": "https://github.com/categorie"
}
```

I don't understand this. I exported the patch after adding the two new files to hg. Then I apply it to a new clone.

 The patch applies fine and the tests pass. But when I do -docbuild reference html it tells me that it can not find the new files :


```
 /usr/local/sage/devel/sage/doc/en/reference/plane_curves.rst:7: (WARNING/2) toctree references unknown document u'sage/schemes/elliptic_curves/modular_parametrization'                                 
/usr/local/sage/devel/sage/doc/en/reference/plane_curves.rst:7: (WARNING/2) toctree references unknown document u'sage/schemes/elliptic_curves/gal_reps'     
```


 I must be doing something stupidly wrong. Help !



---

archive/issue_comments_071190.json:
```json
{
    "body": "updated.",
    "created_at": "2010-02-01T23:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71190",
    "user": "https://github.com/categorie"
}
```

updated.



---

archive/issue_comments_071191.json:
```json
{
    "body": "Attachment [trac_8118.patch](tarball://root/attachments/some-uuid/ticket8118/trac_8118.patch) by @JohnCremona created at 2010-02-02 09:54:27\n\nI applied the patch to 4.3.2.alpha1:  OK with some fuzz on hunk #7.\n\nTests in sage/schemes/elliptic_curves:  all tests (includng long) pass.\n\nsage -docbuild reference html worked fine for me (it warned about \n\n```\n/home/jec/sage-4.3.2.alpha1/devel/sage/doc/en/reference/sage/geometry/polytope.rst:: WARNING: document isn't included in any toctree\n/home/jec/sage-4.3.2.alpha1/devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree\n```\n\nbut that's not from this patch!)\n\nI have not actually looked at the html docs for the new files yet, but will do so.  Meanwhile: positive review.",
    "created_at": "2010-02-02T09:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71191",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8118.patch](tarball://root/attachments/some-uuid/ticket8118/trac_8118.patch) by @JohnCremona created at 2010-02-02 09:54:27

I applied the patch to 4.3.2.alpha1:  OK with some fuzz on hunk #7.

Tests in sage/schemes/elliptic_curves:  all tests (includng long) pass.

sage -docbuild reference html worked fine for me (it warned about 

```
/home/jec/sage-4.3.2.alpha1/devel/sage/doc/en/reference/sage/geometry/polytope.rst:: WARNING: document isn't included in any toctree
/home/jec/sage-4.3.2.alpha1/devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree
```

but that's not from this patch!)

I have not actually looked at the html docs for the new files yet, but will do so.  Meanwhile: positive review.



---

archive/issue_comments_071192.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-02T09:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71192",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071193.json:
```json
{
    "body": "My queue for 4.3.3.alpha0 is\n\n\n```\ntrac_8219.patch\ntrac_3683-upgrade_moinmoin.patch\ntrac_8183-French_pdf.patch\ntrac_8190-docbuild.patch\ntrac_8184-eclib.patch\ntrac_8184-indentation.patch\ntrac_8155.patch\ntrac_8124-selmer-nf.review.patch\ntrac_7575.patch\ntrac_7575-followup.patch\ntrac_8189-hg.patch\ntrac_7935.patch\ntrac_7935b.2.patch\n```\n\n\nCould you let me know how I should apply #8118 and #4453?  Thanks!",
    "created_at": "2010-02-10T11:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71193",
    "user": "https://github.com/qed777"
}
```

My queue for 4.3.3.alpha0 is


```
trac_8219.patch
trac_3683-upgrade_moinmoin.patch
trac_8183-French_pdf.patch
trac_8190-docbuild.patch
trac_8184-eclib.patch
trac_8184-indentation.patch
trac_8155.patch
trac_8124-selmer-nf.review.patch
trac_7575.patch
trac_7575-followup.patch
trac_8189-hg.patch
trac_7935.patch
trac_7935b.2.patch
```


Could you let me know how I should apply #8118 and #4453?  Thanks!



---

archive/issue_comments_071194.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-13T05:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71194",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071195.json:
```json
{
    "body": "I get hunk failures when applying [trac_8118.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8118/trac_8118.patch) to Sage 4.3.3.alpha0:\n\n```\n[mvngu@sage sage-main]$ pwd\n/dev/shm/mvngu/sage-4.3.3.alpha0/devel/sage-main\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8118/trac_8118.patch && hg qpush\nadding trac_8118.patch to series file\napplying trac_8118.patch\npatching file sage/schemes/elliptic_curves/ell_rational_field.py\nHunk #2 FAILED at 45\nHunk #7 succeeded at 4141 with fuzz 2 (offset 99 lines).\nHunk #16 FAILED at 5294\nHunk #17 FAILED at 5327\nHunk #18 FAILED at 5367\nHunk #19 FAILED at 5381\nHunk #20 FAILED at 5576\nHunk #21 FAILED at 5589\nHunk #22 FAILED at 5610\nHunk #23 FAILED at 5620\nHunk #24 FAILED at 5692\nHunk #25 FAILED at 5702\nHunk #26 FAILED at 5717\nHunk #27 FAILED at 5728\n13 out of 28 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8118.patch\n```\n\nPerhaps the attachment needs a rebase.",
    "created_at": "2010-02-13T05:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71195",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I get hunk failures when applying [trac_8118.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8118/trac_8118.patch) to Sage 4.3.3.alpha0:

```
[mvngu@sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.3.alpha0/devel/sage-main
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8118/trac_8118.patch && hg qpush
adding trac_8118.patch to series file
applying trac_8118.patch
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #2 FAILED at 45
Hunk #7 succeeded at 4141 with fuzz 2 (offset 99 lines).
Hunk #16 FAILED at 5294
Hunk #17 FAILED at 5327
Hunk #18 FAILED at 5367
Hunk #19 FAILED at 5381
Hunk #20 FAILED at 5576
Hunk #21 FAILED at 5589
Hunk #22 FAILED at 5610
Hunk #23 FAILED at 5620
Hunk #24 FAILED at 5692
Hunk #25 FAILED at 5702
Hunk #26 FAILED at 5717
Hunk #27 FAILED at 5728
13 out of 28 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8118.patch
```

Perhaps the attachment needs a rebase.



---

archive/issue_comments_071196.json:
```json
{
    "body": "Attachment [trac_8118_rebased.2.patch](tarball://root/attachments/some-uuid/ticket8118/trac_8118_rebased.2.patch) by @categorie created at 2010-02-13 18:57:31\n\nexported against 4.3.3.alpha0",
    "created_at": "2010-02-13T18:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71196",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_8118_rebased.2.patch](tarball://root/attachments/some-uuid/ticket8118/trac_8118_rebased.2.patch) by @categorie created at 2010-02-13 18:57:31

exported against 4.3.3.alpha0



---

archive/issue_comments_071197.json:
```json
{
    "body": "No, that patch is not good. I will have to modify BSD.py, too.",
    "created_at": "2010-02-13T18:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71197",
    "user": "https://github.com/categorie"
}
```

No, that patch is not good. I will have to modify BSD.py, too.



---

archive/issue_comments_071198.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-13T19:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71198",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071199.json:
```json
{
    "body": "OK. so let's hope I did it correctly this time. The patch trac_8118_rebased.patch can be applied to 4.3.3.alpha0. Please apply it before any other patch for ell_rational_field, since it is likely to break again.",
    "created_at": "2010-02-13T19:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71199",
    "user": "https://github.com/categorie"
}
```

OK. so let's hope I did it correctly this time. The patch trac_8118_rebased.patch can be applied to 4.3.3.alpha0. Please apply it before any other patch for ell_rational_field, since it is likely to break again.



---

archive/issue_comments_071200.json:
```json
{
    "body": "Sorry, I tried to do things too quickly..",
    "created_at": "2010-02-13T21:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71200",
    "user": "https://github.com/categorie"
}
```

Sorry, I tried to do things too quickly..



---

archive/issue_comments_071201.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-13T21:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71201",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071202.json:
```json
{
    "body": "Attachment [trac_8118_rebased.patch](tarball://root/attachments/some-uuid/ticket8118/trac_8118_rebased.patch) by @categorie created at 2010-02-14 17:45:52\n\nexported against 4.3.3.alpha0",
    "created_at": "2010-02-14T17:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71202",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_8118_rebased.patch](tarball://root/attachments/some-uuid/ticket8118/trac_8118_rebased.patch) by @categorie created at 2010-02-14 17:45:52

exported against 4.3.3.alpha0



---

archive/issue_comments_071203.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-14T17:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71203",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071204.json:
```json
{
    "body": "OK. This time, I think I got it right. The patch trac_8118_rebased.patch should apply fine to 4.3.3.alpha0. As said before, it should be applied before any other patch involving ell_rational_field, because I reordered the imports in the beginning of this file.\n\nOn my machine all tests pass. (Except for a problem in heegner.py which is already there on 4.3.3.alpha0.)\n\nI don't know if I am allowed to set this back to positive review, since it is only a rebase. So I put a need_review instead. But it would be good if it gets in 4.3.3.",
    "created_at": "2010-02-14T17:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71204",
    "user": "https://github.com/categorie"
}
```

OK. This time, I think I got it right. The patch trac_8118_rebased.patch should apply fine to 4.3.3.alpha0. As said before, it should be applied before any other patch involving ell_rational_field, because I reordered the imports in the beginning of this file.

On my machine all tests pass. (Except for a problem in heegner.py which is already there on 4.3.3.alpha0.)

I don't know if I am allowed to set this back to positive review, since it is only a rebase. So I put a need_review instead. But it would be good if it gets in 4.3.3.



---

archive/issue_comments_071205.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-18T21:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071206.json:
```json
{
    "body": "The rebase looks good. No drama when doctesting.",
    "created_at": "2010-02-18T21:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The rebase looks good. No drama when doctesting.



---

archive/issue_comments_071207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T21:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071208.json:
```json
{
    "body": "Merged [trac_8118_rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8118/trac_8118_rebased.patch).",
    "created_at": "2010-02-18T21:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8118#issuecomment-71208",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8118_rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8118/trac_8118_rebased.patch).



---

archive/issue_events_008326.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-02-18T21:26:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8118",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8118#event-8326"
}
```
