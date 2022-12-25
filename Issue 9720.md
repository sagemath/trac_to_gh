# Issue 9720: Add random echelonizable matrices to matrix/constructor.py

archive/issues_009720.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @rbeezer @jasongrout\n\nAdds two routines.  One creates random matrices in echelon form to be used in other routines to be added later.  The other creates random matrices whose echelon form has desirable properties, with the help of the first routine.  These routines are designed as educational tools, generating exam and homework problems, and problem generating interacts.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9720\n\n",
    "closed_at": "2010-09-15T09:52:32Z",
    "created_at": "2010-08-10T18:51:32Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Add random echelonizable matrices to matrix/constructor.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9720",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```
Assignee: jason, was

CC:  @rbeezer @jasongrout

Adds two routines.  One creates random matrices in echelon form to be used in other routines to be added later.  The other creates random matrices whose echelon form has desirable properties, with the help of the first routine.  These routines are designed as educational tools, generating exam and homework problems, and problem generating interacts.

Issue created by migration from https://trac.sagemath.org/ticket/9720





---

archive/issue_comments_094701.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-10T19:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94701",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094702.json:
```json
{
    "body": "Attachment [trac_9720-random-echelonizable-matrices.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices.patch) by bwonderly created at 2010-08-10 19:11:10",
    "created_at": "2010-08-10T19:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94702",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9720-random-echelonizable-matrices.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices.patch) by bwonderly created at 2010-08-10 19:11:10



---

archive/issue_comments_094703.json:
```json
{
    "body": "Applies fine to 4.5.2.rc0.\n\nTwo extremely minor comments off the top of my head:\n\n1. \"Generate a matrix of a desired size and rank, over a desired field,\n       whose reduced row-echelon form has only whole values.\"\nIMHO, \"integral\" sounds better than \"whole\".\n2. It seems to me that, from the point of view of the functionality,\nusing base_ring = ZZ returns the same result as base_ring = QQ.\n(I understand that over QQ the rref algorithm might be different than over\nZZ, but it seems to me that for the matrices you compute in the \nrandom_echelonizable_matrix function, the rref algorithm(s) yield\nthe same result either way. Correct?",
    "created_at": "2010-08-11T11:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94703",
    "user": "https://github.com/wdjoyner"
}
```

Applies fine to 4.5.2.rc0.

Two extremely minor comments off the top of my head:

1. "Generate a matrix of a desired size and rank, over a desired field,
       whose reduced row-echelon form has only whole values."
IMHO, "integral" sounds better than "whole".
2. It seems to me that, from the point of view of the functionality,
using base_ring = ZZ returns the same result as base_ring = QQ.
(I understand that over QQ the rref algorithm might be different than over
ZZ, but it seems to me that for the matrices you compute in the 
random_echelonizable_matrix function, the rref algorithm(s) yield
the same result either way. Correct?



---

archive/issue_comments_094704.json:
```json
{
    "body": "Attachment [trac_9720-random-echelonizable-matrices-v2.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices-v2.patch) by bwonderly created at 2010-08-11 22:55:31\n\nstand-alone version 2 patch, same patch with one revision",
    "created_at": "2010-08-11T22:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94704",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9720-random-echelonizable-matrices-v2.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices-v2.patch) by bwonderly created at 2010-08-11 22:55:31

stand-alone version 2 patch, same patch with one revision



---

archive/issue_comments_094705.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> Applies fine to 4.5.2.rc0.\n> \n> Two extremely minor comments off the top of my head:\n> \n> 1. \"Generate a matrix of a desired size and rank, over a desired field,\n>        whose reduced row-echelon form has only whole values.\"\n> IMHO, \"integral\" sounds better than \"whole\".\n\n\nI agree completely and have made the change in the v2 patch.\n\n> 2. It seems to me that, from the point of view of the functionality,\n> using base_ring = ZZ returns the same result as base_ring = QQ.\n> (I understand that over QQ the rref algorithm might be different than over\n> ZZ, but it seems to me that for the matrices you compute in the \n> random_echelonizable_matrix function, the rref algorithm(s) yield\n> the same result either way. Correct?\n> \n\n\nYes, the rref algorithm yields the same result with base_ring as ZZ or QQ.  However, as these matrices are going to be used primarily as student example problems I think it would be better to keep the default as QQ.  Although there should be a series of row operations without introducing fractions that achieves rref, a student will likely want to use fractions as they row-reduce an output matrix, and the rescale_row or add_multiple_of_row functions will complain if fractions are introduced working with a matrix over ZZ.  \n> \n\n>",
    "created_at": "2010-08-11T23:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94705",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Replying to [comment:2 wdj]:
> Applies fine to 4.5.2.rc0.
> 
> Two extremely minor comments off the top of my head:
> 
> 1. "Generate a matrix of a desired size and rank, over a desired field,
>        whose reduced row-echelon form has only whole values."
> IMHO, "integral" sounds better than "whole".


I agree completely and have made the change in the v2 patch.

> 2. It seems to me that, from the point of view of the functionality,
> using base_ring = ZZ returns the same result as base_ring = QQ.
> (I understand that over QQ the rref algorithm might be different than over
> ZZ, but it seems to me that for the matrices you compute in the 
> random_echelonizable_matrix function, the rref algorithm(s) yield
> the same result either way. Correct?
> 


Yes, the rref algorithm yields the same result with base_ring as ZZ or QQ.  However, as these matrices are going to be used primarily as student example problems I think it would be better to keep the default as QQ.  Although there should be a series of row operations without introducing fractions that achieves rref, a student will likely want to use fractions as they row-reduce an output matrix, and the rescale_row or add_multiple_of_row functions will complain if fractions are introduced working with a matrix over ZZ.  
> 

>



---

archive/issue_comments_094706.json:
```json
{
    "body": "I am ready to give this patch a positive review. However, although it aplies fine to 4.5.2.rc0, it does not pass sage -testall on a 10.6.4 mac pro. The problems seem to be in some mysterious (to me) failures in \n\n```\nsage -t  \"local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py\"./sage -t  \"local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py\"\n-bash: sage: command not found\nhera:sage-4.5.2.rc0 davidjoyner$ ./sage -t  \"local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py\"sage -t  \"local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py\"\n**********************************************************************\nFile \"/Volumes/Bay2/sagefiles2/sage-4.5.2.rc0/local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py\", line 951:\n    sage: sage_getsourcelines(matrix, True)[1]\nExpected:\n    34\nGot:\n    35\n```\nand a similar failure in\n\n```\nsage -t  \"devel/sage/sage/misc/sageinspect.py\"\n```\nI'll try investigating this using an ubuntu machine, but this seems to possibly be an issue.",
    "created_at": "2010-08-11T23:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94706",
    "user": "https://github.com/wdjoyner"
}
```

I am ready to give this patch a positive review. However, although it aplies fine to 4.5.2.rc0, it does not pass sage -testall on a 10.6.4 mac pro. The problems seem to be in some mysterious (to me) failures in 

```
sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"./sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"
-bash: sage: command not found
hera:sage-4.5.2.rc0 davidjoyner$ ./sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/Volumes/Bay2/sagefiles2/sage-4.5.2.rc0/local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py", line 951:
    sage: sage_getsourcelines(matrix, True)[1]
Expected:
    34
Got:
    35
```
and a similar failure in

```
sage -t  "devel/sage/sage/misc/sageinspect.py"
```
I'll try investigating this using an ubuntu machine, but this seems to possibly be an issue.



---

archive/issue_comments_094707.json:
```json
{
    "body": "Appears to me that the test that fails is testing an actual line number of source code from the file defining the `matrix` constructor.  Billy added an import statement at the top of the module, so the line numbers will increment by one?\n\nRather than patching sagenb, I'm going to do some tests - maybe adding the import of QQ to the same line as the import of ZZ will be a solution.\n\nRob",
    "created_at": "2010-08-11T23:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94707",
    "user": "https://github.com/rbeezer"
}
```

Appears to me that the test that fails is testing an actual line number of source code from the file defining the `matrix` constructor.  Billy added an import statement at the top of the module, so the line numbers will increment by one?

Rather than patching sagenb, I'm going to do some tests - maybe adding the import of QQ to the same line as the import of ZZ will be a solution.

Rob



---

archive/issue_comments_094708.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-12T00:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94708",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094709.json:
```json
{
    "body": "Billy,\n\nMake a v3 patch and replace the two import statements for ZZ and QQ by the statement\n\n```\nfrom sage.rings.all import ZZ, QQ\n```\n\nand subsequent line numbers will return to \"normal\" and this very technical test should pass.  Do the very complete tests\n\n```\n./sage -testall\n```\n\novernight and then post the patch.\n\nI've tested this change on matrix/constructor.py and the two files David has failing.\n\nDavid - nice catch!\n\nRob",
    "created_at": "2010-08-12T00:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94709",
    "user": "https://github.com/rbeezer"
}
```

Billy,

Make a v3 patch and replace the two import statements for ZZ and QQ by the statement

```
from sage.rings.all import ZZ, QQ
```

and subsequent line numbers will return to "normal" and this very technical test should pass.  Do the very complete tests

```
./sage -testall
```

overnight and then post the patch.

I've tested this change on matrix/constructor.py and the two files David has failing.

David - nice catch!

Rob



---

archive/issue_comments_094710.json:
```json
{
    "body": "In the first line of the docstring for the second function, you say:\n\nGenerate a matrix of a desired size and rank, over a desired field,\n\nShould that say \"desired ring\"?",
    "created_at": "2010-08-12T03:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94710",
    "user": "https://github.com/jasongrout"
}
```

In the first line of the docstring for the second function, you say:

Generate a matrix of a desired size and rank, over a desired field,

Should that say "desired ring"?



---

archive/issue_comments_094711.json:
```json
{
    "body": "stand-alone version 3 of the same patch, with import statement change  and documentation revision",
    "created_at": "2010-08-12T07:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94711",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

stand-alone version 3 of the same patch, with import statement change  and documentation revision



---

archive/issue_comments_094712.json:
```json
{
    "body": "Attachment [trac_9720-random-echelonizable-matrices-v3.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices-v3.patch) by bwonderly created at 2010-08-12 07:16:38\n\nReplying to [comment:7 jason]:\n> In the first line of the docstring for the second function, you say:\n> \n> Generate a matrix of a desired size and rank, over a desired field,\n> \n> Should that say \"desired ring\"?\n\n\nAbsolutely, I've made that change and the import statement change, and all tests passed.",
    "created_at": "2010-08-12T07:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94712",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9720-random-echelonizable-matrices-v3.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices-v3.patch) by bwonderly created at 2010-08-12 07:16:38

Replying to [comment:7 jason]:
> In the first line of the docstring for the second function, you say:
> 
> Generate a matrix of a desired size and rank, over a desired field,
> 
> Should that say "desired ring"?


Absolutely, I've made that change and the import statement change, and all tests passed.



---

archive/issue_comments_094713.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-12T17:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94713",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094714.json:
```json
{
    "body": "I think this means you are ready to have the reviewing proceed, so I'll change the status to \"needs review\".",
    "created_at": "2010-08-12T17:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94714",
    "user": "https://github.com/rbeezer"
}
```

I think this means you are ready to have the reviewing proceed, so I'll change the status to "needs review".



---

archive/issue_comments_094715.json:
```json
{
    "body": "The latest patch applies fine to 4.5.2.rc0 and passes sage -testall on a 10.6.4 mac pro.\n\nThis is a well-documented addition and I definitely will use it teaching linear algebra this semester. Thanks for coding this up!",
    "created_at": "2010-08-12T18:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94715",
    "user": "https://github.com/wdjoyner"
}
```

The latest patch applies fine to 4.5.2.rc0 and passes sage -testall on a 10.6.4 mac pro.

This is a well-documented addition and I definitely will use it teaching linear algebra this semester. Thanks for coding this up!



---

archive/issue_comments_094716.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-12T18:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94716",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094717.json:
```json
{
    "body": "Thanks everyone for the suggestions and the expeditious review!\n\nRelease manager:  apply only v3 patch.",
    "created_at": "2010-08-15T19:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94717",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Thanks everyone for the suggestions and the expeditious review!

Release manager:  apply only v3 patch.



---

archive/issue_comments_094718.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-08-25T20:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94718",
    "user": "https://github.com/mwhansen"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_094719.json:
```json
{
    "body": "I think that these should really just be options to the random_matrix function so that we don't have a ton of `random_*_matrix` commands floating around in the global namespace.",
    "created_at": "2010-08-25T20:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94719",
    "user": "https://github.com/mwhansen"
}
```

I think that these should really just be options to the random_matrix function so that we don't have a ton of `random_*_matrix` commands floating around in the global namespace.



---

archive/issue_comments_094720.json:
```json
{
    "body": "Replying to [comment:13 mhansen]:\n> I think that these should really just be options to the random_matrix function so that we don't have a \n> ton of `random_*_matrix` commands floating around in the global namespace.\n\n\nThough this is logical, I personally vote -1 as it will be somewhat harder\nto use for those who need it (teachers not necessarily expert in Sage\nbut needing it for a quick computation for an example or 2 in a lecture note).\n\nIn any case, I hope this will be approved as I am teaching this *right now*:-)",
    "created_at": "2010-08-25T20:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94720",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:13 mhansen]:
> I think that these should really just be options to the random_matrix function so that we don't have a 
> ton of `random_*_matrix` commands floating around in the global namespace.


Though this is logical, I personally vote -1 as it will be somewhat harder
to use for those who need it (teachers not necessarily expert in Sage
but needing it for a quick computation for an example or 2 in a lecture note).

In any case, I hope this will be approved as I am teaching this *right now*:-)



---

archive/issue_comments_094721.json:
```json
{
    "body": "There won't be tons, just four I think.  ;-)  But I agree entirely.\n\nWould you pass some sort of selector in `*args`, then make these methods of some class of matrices?  How would the documentation be immediately or easily accessible?  Is there a model we can follow someplace else in Sage?\n\nIf you'd be able to suggest a course of action, I can work with Billy to make this happen.  He's finished posting all his routines (there aren't any more planned) and classes begin Monday, so it'd be nice to get this going quickly so he can wrap up his summer project.\n\nThanks again, I'd had the same reservations about adding to the global namespace, but hadn't hit on this option.\n\nRob",
    "created_at": "2010-08-25T20:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94721",
    "user": "https://github.com/rbeezer"
}
```

There won't be tons, just four I think.  ;-)  But I agree entirely.

Would you pass some sort of selector in `*args`, then make these methods of some class of matrices?  How would the documentation be immediately or easily accessible?  Is there a model we can follow someplace else in Sage?

If you'd be able to suggest a course of action, I can work with Billy to make this happen.  He's finished posting all his routines (there aren't any more planned) and classes begin Monday, so it'd be nice to get this going quickly so he can wrap up his summer project.

Thanks again, I'd had the same reservations about adding to the global namespace, but hadn't hit on this option.

Rob



---

archive/issue_comments_094722.json:
```json
{
    "body": "I agree with David's comments about documentation - maybe we can make that happen smoothly and logically, but its not coming to me right at the moment.",
    "created_at": "2010-08-25T20:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94722",
    "user": "https://github.com/rbeezer"
}
```

I agree with David's comments about documentation - maybe we can make that happen smoothly and logically, but its not coming to me right at the moment.



---

archive/issue_comments_094723.json:
```json
{
    "body": "Replying to [comment:15 rbeezer]:\n> Would you pass some sort of selector in `*args`, then make these methods of some class of matrices?  How would the documentation be immediately or easily accessible?  Is there a model we can follow someplace else in Sage?\n\n\nYou can leave the functions as they are -- just don't import them into the global namespace.  Then, if you do,\n\n```\nsage: a = random_matrix(QQ, 3, 3, rref=True)\nsage: b = random_matrix(QQ, 3, 3, echelonizable=True)\n```\n\nwhich just delegate to the appropriate function.  You can add a reference to those functions in the docstring of `random_matrix`.\n \nAlso, the documentation is not clear on why there is special casing for ZZ and QQ, and that these methods don't work for inexact rings.  Although, you could argue that if you have one of these matrices over `ZZ` you could just convert all the entries to `RR` and things \"should\" be fine.",
    "created_at": "2010-08-25T20:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94723",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:15 rbeezer]:
> Would you pass some sort of selector in `*args`, then make these methods of some class of matrices?  How would the documentation be immediately or easily accessible?  Is there a model we can follow someplace else in Sage?


You can leave the functions as they are -- just don't import them into the global namespace.  Then, if you do,

```
sage: a = random_matrix(QQ, 3, 3, rref=True)
sage: b = random_matrix(QQ, 3, 3, echelonizable=True)
```

which just delegate to the appropriate function.  You can add a reference to those functions in the docstring of `random_matrix`.
 
Also, the documentation is not clear on why there is special casing for ZZ and QQ, and that these methods don't work for inexact rings.  Although, you could argue that if you have one of these matrices over `ZZ` you could just convert all the entries to `RR` and things "should" be fine.



---

archive/issue_comments_094724.json:
```json
{
    "body": "Mike -\n\nOK, that makes sense - thanks.\n\nWe also have \"diagonalizable\", \"unimodular\" and \"subspaceable\", so I think something like a single keyword type/category/class/method/algorithm (I don't really like any of those too much) that defaults to the current \"randomize\" behavior would be better.  Is \"algorithm\" the policy these days for this type of thing?  Some constructors must be square so we would have to check for that first.  (And we can address the ZZ, QQ, inexact situation.)\n\nThanks for the suggestion and quick help.\n\nDavid - I think I can make the HTML docs work well, and can include the necessary import/qualified statement in the tab-completion documentation to make the notebook/command-line docs relatively easy to access.  We'd include at least one full example in the docs for random_matrix() so it could be discovered that way.  Does that sound OK?\n\nBilly - I'll try to set things up to make current patch work.  It won't be too hard then for you to adjust the other two that are outstanding.  Sound OK?\n\nRob",
    "created_at": "2010-08-25T20:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94724",
    "user": "https://github.com/rbeezer"
}
```

Mike -

OK, that makes sense - thanks.

We also have "diagonalizable", "unimodular" and "subspaceable", so I think something like a single keyword type/category/class/method/algorithm (I don't really like any of those too much) that defaults to the current "randomize" behavior would be better.  Is "algorithm" the policy these days for this type of thing?  Some constructors must be square so we would have to check for that first.  (And we can address the ZZ, QQ, inexact situation.)

Thanks for the suggestion and quick help.

David - I think I can make the HTML docs work well, and can include the necessary import/qualified statement in the tab-completion documentation to make the notebook/command-line docs relatively easy to access.  We'd include at least one full example in the docs for random_matrix() so it could be discovered that way.  Does that sound OK?

Billy - I'll try to set things up to make current patch work.  It won't be too hard then for you to adjust the other two that are outstanding.  Sound OK?

Rob



---

archive/issue_comments_094725.json:
```json
{
    "body": "Replying to [comment:18 rbeezer]:\n> Mike -\n> \n\n\n...\n\n> \n> David - I think I can make the HTML docs work well, and can include the necessary import/qualified \n> statement in the tab-completion documentation to make the notebook/command-line docs relatively \n> easy to access.  We'd include at least one full example in the docs for random_matrix() so it could be \n> discovered that way.  Does that sound OK?\n\n\n\nSounds good - thanks Rob (and Mike)!!\n\n\n> \n> Rob",
    "created_at": "2010-08-25T20:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94725",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:18 rbeezer]:
> Mike -
> 


...

> 
> David - I think I can make the HTML docs work well, and can include the necessary import/qualified 
> statement in the tab-completion documentation to make the notebook/command-line docs relatively 
> easy to access.  We'd include at least one full example in the docs for random_matrix() so it could be 
> discovered that way.  Does that sound OK?



Sounds good - thanks Rob (and Mike)!!


> 
> Rob



---

archive/issue_comments_094726.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-08-25T21:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94726",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_094727.json:
```json
{
    "body": "To take care of the namespace issue, what about making it work like graphs does? In other words, \"random_matrix\" behaves like it always has, and \"random_matrix.echelonizable(...)\", \"random_matrix.unimodular()\", etc., do the specialized functions?\n\nI'm a slight -1 on making random_matrix take a ton of options, a lot of which may be mutually exclusive.  For example, if I ask for a random echelonizable matrix over ZZ, with a specific range of entries, will it work?",
    "created_at": "2010-08-25T21:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94727",
    "user": "https://github.com/jasongrout"
}
```

To take care of the namespace issue, what about making it work like graphs does? In other words, "random_matrix" behaves like it always has, and "random_matrix.echelonizable(...)", "random_matrix.unimodular()", etc., do the specialized functions?

I'm a slight -1 on making random_matrix take a ton of options, a lot of which may be mutually exclusive.  For example, if I ask for a random echelonizable matrix over ZZ, with a specific range of entries, will it work?



---

archive/issue_comments_094728.json:
```json
{
    "body": "Attachment [trac_9720-random-echelonizable-matrices-v4.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices-v4.patch) by @rbeezer created at 2010-08-25 21:33:27\n\nSame as v3, but removed routines from global namespace",
    "created_at": "2010-08-25T21:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94728",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9720-random-echelonizable-matrices-v4.patch](tarball://root/attachments/some-uuid/ticket9720/trac_9720-random-echelonizable-matrices-v4.patch) by @rbeezer created at 2010-08-25 21:33:27

Same as v3, but removed routines from global namespace



---

archive/issue_comments_094729.json:
```json
{
    "body": "v4 patch is identical to v3, except the two new routines are not imported into the global namespace, and therefore two import commands are needed in the doctests.\n\nsage/matrix/constructor.py passes randomized testing (-randorder) with these changes.  Full testing later.  Upcoming patch will have `random_matrix()` delegate to these two routines.\n\nBilly's name should still be on this patch as the author.\n\nRob",
    "created_at": "2010-08-25T21:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94729",
    "user": "https://github.com/rbeezer"
}
```

v4 patch is identical to v3, except the two new routines are not imported into the global namespace, and therefore two import commands are needed in the doctests.

sage/matrix/constructor.py passes randomized testing (-randorder) with these changes.  Full testing later.  Upcoming patch will have `random_matrix()` delegate to these two routines.

Billy's name should still be on this patch as the author.

Rob



---

archive/issue_comments_094730.json:
```json
{
    "body": "Replying to [comment:21 jason]:\n> To take care of the namespace issue, what about making it work like graphs does? In other words, \"random_matrix\" behaves like it always has, and \"random_matrix.echelonizable(...)\", \"random_matrix.unimodular()\", etc., do the specialized functions?\n> \n> I'm a slight -1 on making random_matrix take a ton of options, a lot of which may be mutually exclusive.  For example, if I ask for a random echelonizable matrix over ZZ, with a specific range of entries, will it work?\n\n\nRight now I'm thinking:\n\n```\nrandom_matrix(RR, 6, 4, algorithm='randomize')\n\nrandom_matrix(ZZ, 6, 4, algorithm='echelon_form')\n\nrandom_matrix(ZZ, 3, 4, algorithm='echelonizable')\n\nrandom_matrix(ZZ, 8, 8, algorithm='diagonalizable')\n```\n\netc.  `random_matrix()` would be a big switch on the value of `algorithm`.  Default would be 'randomize' and preserve current behavior.  `random_matrix()` would throw errors for \"wrong\" rings, or \"wrong\" shapes.\n\n`random_matrix()` would have one good example of each type, with link to actual routine's documentation for PDF & HTL version.  For notebook or CL docs, the documentation would say \"use sage.constructor.random_echelonizable_matrix?\" for more detailed documentation right after the example (not tested).\n\n`random_matrix()` already takes lots of options - anything the randomize function of the entry type accepts.  I think the new functions only accept `upper_bound` as an option, as a type of what Billy calls \"size control\".  Currently, the possibilities for arguments is not handled very well:\n\n```\nsage: random_matrix(QQ, 3, 4, num_bound = 4, den_bound = 10)\n[-3/8 -3/5    1 -4/7]\n[ 3/2  2/3   -2 -1/2]\n[-1/8  1/2  1/8 -3/8]\nsage: random_matrix(ZZ, 3, 4, num_bound = 4, den_bound = 10)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/sage/dev/devel/sage-main/<ipython console> in <module>()\n\n/sage/dev/local/lib/python2.6/site-packages/sage/matrix/constructor.pyc in random_matrix(R, nrows, ncols, sparse, density, *args, **kwds)\n    829         A.randomize(density=float(1), nonzero=False, *args, **kwds)\n    830     else:\n--> 831         A.randomize(density=density, nonzero=True, *args, **kwds)\n    832     return A\n    833\n\n/sage/dev/local/lib/python2.6/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense.Matrix_integer_dense.randomize (sage/matrix/matrix_integer_dense.c:23941)()\n\nTypeError: randomize() got an unexpected keyword argument 'num_bound'\n```\n\nI'm -1 to implementing the whole graphs-dot infrastructure for just five or six functions right as Billy is trying to wrap this up.  (And possibly having to deprecate any current behavior.)  I do want to (but have not found the time yet) to implement the dot-syntax for groups.\n\nJust a thought - we could implement a whole random-dot hierarchy: matrices, primes, graphs,....",
    "created_at": "2010-08-25T22:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94730",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:21 jason]:
> To take care of the namespace issue, what about making it work like graphs does? In other words, "random_matrix" behaves like it always has, and "random_matrix.echelonizable(...)", "random_matrix.unimodular()", etc., do the specialized functions?
> 
> I'm a slight -1 on making random_matrix take a ton of options, a lot of which may be mutually exclusive.  For example, if I ask for a random echelonizable matrix over ZZ, with a specific range of entries, will it work?


Right now I'm thinking:

```
random_matrix(RR, 6, 4, algorithm='randomize')

random_matrix(ZZ, 6, 4, algorithm='echelon_form')

random_matrix(ZZ, 3, 4, algorithm='echelonizable')

random_matrix(ZZ, 8, 8, algorithm='diagonalizable')
```

etc.  `random_matrix()` would be a big switch on the value of `algorithm`.  Default would be 'randomize' and preserve current behavior.  `random_matrix()` would throw errors for "wrong" rings, or "wrong" shapes.

`random_matrix()` would have one good example of each type, with link to actual routine's documentation for PDF & HTL version.  For notebook or CL docs, the documentation would say "use sage.constructor.random_echelonizable_matrix?" for more detailed documentation right after the example (not tested).

`random_matrix()` already takes lots of options - anything the randomize function of the entry type accepts.  I think the new functions only accept `upper_bound` as an option, as a type of what Billy calls "size control".  Currently, the possibilities for arguments is not handled very well:

```
sage: random_matrix(QQ, 3, 4, num_bound = 4, den_bound = 10)
[-3/8 -3/5    1 -4/7]
[ 3/2  2/3   -2 -1/2]
[-1/8  1/2  1/8 -3/8]
sage: random_matrix(ZZ, 3, 4, num_bound = 4, den_bound = 10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/sage/dev/devel/sage-main/<ipython console> in <module>()

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/constructor.pyc in random_matrix(R, nrows, ncols, sparse, density, *args, **kwds)
    829         A.randomize(density=float(1), nonzero=False, *args, **kwds)
    830     else:
--> 831         A.randomize(density=density, nonzero=True, *args, **kwds)
    832     return A
    833

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense.Matrix_integer_dense.randomize (sage/matrix/matrix_integer_dense.c:23941)()

TypeError: randomize() got an unexpected keyword argument 'num_bound'
```

I'm -1 to implementing the whole graphs-dot infrastructure for just five or six functions right as Billy is trying to wrap this up.  (And possibly having to deprecate any current behavior.)  I do want to (but have not found the time yet) to implement the dot-syntax for groups.

Just a thought - we could implement a whole random-dot hierarchy: matrices, primes, graphs,....



---

archive/issue_comments_094731.json:
```json
{
    "body": "The algorithm keyword seems natural enough for me.  What I was opposed to was 5 different True/False keyword options, each mutually exclusive for the others.",
    "created_at": "2010-08-25T22:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94731",
    "user": "https://github.com/jasongrout"
}
```

The algorithm keyword seems natural enough for me.  What I was opposed to was 5 different True/False keyword options, each mutually exclusive for the others.



---

archive/issue_comments_094732.json:
```json
{
    "body": "Replying to [comment:24 jason]:\n> The algorithm keyword seems natural enough for me.  What I was opposed to was 5 different True/False keyword options, each mutually exclusive for the others.\n\n\nGood - I didn't want that either.  I'm going to start on the above shortly.",
    "created_at": "2010-08-25T22:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94732",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:24 jason]:
> The algorithm keyword seems natural enough for me.  What I was opposed to was 5 different True/False keyword options, each mutually exclusive for the others.


Good - I didn't want that either.  I'm going to start on the above shortly.



---

archive/issue_comments_094733.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-26T00:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94733",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094734.json:
```json
{
    "body": "Into the `random_matrix` routine and I've never been happy with the documentation, and I may even change the code now that I've dipped into it.  So I'm going to do that work on a new ticket along with allowing for integrating the new constructions.  See #9803.\n\nThat means that the v4 patch makes this ready to go.  It'll be left hidden until #9803 is done, but at least David J can import it as needed until then.\n\nSo if Billy or David want to check-off on my changes from v3 to v4 (undid changes in all.py and added two imports to doctests) then this can go to positive review.  I'll add interested parties to #9803 once I have a patch up, so no need to add yourself yet unless you have more comments.\n\nThis also allows Billy to be sole author on this.",
    "created_at": "2010-08-26T00:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94734",
    "user": "https://github.com/rbeezer"
}
```

Into the `random_matrix` routine and I've never been happy with the documentation, and I may even change the code now that I've dipped into it.  So I'm going to do that work on a new ticket along with allowing for integrating the new constructions.  See #9803.

That means that the v4 patch makes this ready to go.  It'll be left hidden until #9803 is done, but at least David J can import it as needed until then.

So if Billy or David want to check-off on my changes from v3 to v4 (undid changes in all.py and added two imports to doctests) then this can go to positive review.  I'll add interested parties to #9803 once I have a patch up, so no need to add yourself yet unless you have more comments.

This also allows Billy to be sole author on this.



---

archive/issue_comments_094735.json:
```json
{
    "body": "Replying to [comment:26 rbeezer]:\n\n...\n\n> \n> So if Billy or David want to check-off on my changes from v3 to v4 (undid changes in all.py and added two imports to doctests) then this can go to positive review.  I'll add interested parties to #9803 once I have a patch up, so no need to add yourself yet unless you have more comments.\n> \n\n\n\nThis looks good to me (I even tested it again for safety's sake:-).\n\n> This also allows Billy to be sole author on this.",
    "created_at": "2010-08-26T12:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94735",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:26 rbeezer]:

...

> 
> So if Billy or David want to check-off on my changes from v3 to v4 (undid changes in all.py and added two imports to doctests) then this can go to positive review.  I'll add interested parties to #9803 once I have a patch up, so no need to add yourself yet unless you have more comments.
> 



This looks good to me (I even tested it again for safety's sake:-).

> This also allows Billy to be sole author on this.



---

archive/issue_comments_094736.json:
```json
{
    "body": "Thanks, David.  I'm going to move this back to positive review.  Patch up at #9803 to reflect discussion above.\n\n# Release manager\n\nApply only the v4 patch and please merge with #9803 once it is ready - the calling syntax changes, so both tickets should go in together.",
    "created_at": "2010-08-26T22:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94736",
    "user": "https://github.com/rbeezer"
}
```

Thanks, David.  I'm going to move this back to positive review.  Patch up at #9803 to reflect discussion above.

# Release manager

Apply only the v4 patch and please merge with #9803 once it is ready - the calling syntax changes, so both tickets should go in together.



---

archive/issue_comments_094737.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-26T22:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94737",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094738.json:
```json
{
    "body": "## Release Manager\n\n#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this\norder.",
    "created_at": "2010-09-03T06:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94738",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

## Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this
order.



---

archive/issue_comments_094739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9720#issuecomment-94739",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024327.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T09:52:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9720",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9720#event-24327"
}
```
