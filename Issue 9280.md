# Issue 9280: implement an example of a graded algebra with basis

archive/issues_009280.json:
```json
{
    "body": "Assignee: nthiery\n\nThe summary says it all.  Also see the patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9280\n\n",
    "created_at": "2010-06-20T03:39:29Z",
    "labels": [
        "categories",
        "minor",
        "enhancement"
    ],
    "title": "implement an example of a graded algebra with basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9280",
    "user": "jhpalmieri"
}
```
Assignee: nthiery

The summary says it all.  Also see the patch.

Issue created by migration from https://trac.sagemath.org/ticket/9280





---

archive/issue_comments_087399.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-20T03:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87399",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087400.json:
```json
{
    "body": "Attachment\n\nHi John,\n\nFor the record: we went through your patches with Franco and Jason, and discussed quite a bit around it. We will post here shortly an updated patch with some little suggestions.",
    "created_at": "2010-07-21T05:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87400",
    "user": "nthiery"
}
```

Attachment

Hi John,

For the record: we went through your patches with Franco and Jason, and discussed quite a bit around it. We will post here shortly an updated patch with some little suggestions.



---

archive/issue_comments_087401.json:
```json
{
    "body": "Replying to [comment:2 nthiery]:\n> Hi John,\n> \n> For the record: we went through your patches with Franco and Jason, and discussed quite a bit around it. We will post here shortly an updated patch with some little suggestions.\n\nIs it \"shortly\" yet?  :)",
    "created_at": "2010-10-01T22:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87401",
    "user": "jhpalmieri"
}
```

Replying to [comment:2 nthiery]:
> Hi John,
> 
> For the record: we went through your patches with Franco and Jason, and discussed quite a bit around it. We will post here shortly an updated patch with some little suggestions.

Is it "shortly" yet?  :)



---

archive/issue_comments_087402.json:
```json
{
    "body": "In the sage-combinat patch, there are a few typos and some other issues:\n\n- in sage/categories/graded_algebras_with_basis.py, the docstring for \"degree\" says \"The degree of this element in the graded polynomial algebra.\"  Delete \"polynomial\".\n\n- in sage/categories/examples/graded_algebras_with_basis.py, the docstring for \"one_basis\" contains `'(0,...,0`)`, and I think this should be changed to ```(0,...,0)```.\n\n- in sage/categories/examples/graded_algebras_with_basis.py, the docstring for the main class is now outdated: it still refers to \"basis_function\" and \"_basis_fcn\", which don't exist any more, and also to \"homogeneous_component\", which is now part of the default implementation, not something specific to this example.\n\nI'm attaching a referee patch which fixes these. \n\nThere are also some doctests for \"basis\" in sage/categories/graded_algebras_with_basis.py which are marked as \"todo: not implemented\".  Do we need to wait for these to be fixed, or should we consider this ready for review?  It may not be ideal, but we could also change\n\n```\nsage: A.basis(6) # todo: not implemented (output)\nFamily (y^{2}, x^{3}\n```\n\nto\n\n```\nsage: A.basis(6) # todo: not implemented (output)\nFamily (y^{2}, x^{3}\nsage: list(A.basis(6))\n[y^{2}, x^{3}]\n```\n\nBy the way, all tests pass with this patch and with the one from #10193.  So perhaps we could also delete the commented-out part at the beginning of the example, where it says\n\n```\n# TODO: double check that we can now discard this function\n```\n",
    "created_at": "2010-11-08T23:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87402",
    "user": "jhpalmieri"
}
```

In the sage-combinat patch, there are a few typos and some other issues:

- in sage/categories/graded_algebras_with_basis.py, the docstring for "degree" says "The degree of this element in the graded polynomial algebra."  Delete "polynomial".

- in sage/categories/examples/graded_algebras_with_basis.py, the docstring for "one_basis" contains `'(0,...,0`)`, and I think this should be changed to ```(0,...,0)```.

- in sage/categories/examples/graded_algebras_with_basis.py, the docstring for the main class is now outdated: it still refers to "basis_function" and "_basis_fcn", which don't exist any more, and also to "homogeneous_component", which is now part of the default implementation, not something specific to this example.

I'm attaching a referee patch which fixes these. 

There are also some doctests for "basis" in sage/categories/graded_algebras_with_basis.py which are marked as "todo: not implemented".  Do we need to wait for these to be fixed, or should we consider this ready for review?  It may not be ideal, but we could also change

```
sage: A.basis(6) # todo: not implemented (output)
Family (y^{2}, x^{3}
```

to

```
sage: A.basis(6) # todo: not implemented (output)
Family (y^{2}, x^{3}
sage: list(A.basis(6))
[y^{2}, x^{3}]
```

By the way, all tests pass with this patch and with the one from #10193.  So perhaps we could also delete the commented-out part at the beginning of the example, where it says

```
# TODO: double check that we can now discard this function
```




---

archive/issue_comments_087403.json:
```json
{
    "body": "Attachment\n\napply on top of sage-combinat patch",
    "created_at": "2010-11-08T23:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87403",
    "user": "jhpalmieri"
}
```

Attachment

apply on top of sage-combinat patch



---

archive/issue_comments_087404.json:
```json
{
    "body": "There are a couple of patches on the sage-combinat queue experimenting with moving some of the generic methods into the category `GradedAlgebraWithBasis`:\n\n- trac_9280-graded-algebras-example-review-fs.patch\n- trac_9280-graded-algebras-example.patch",
    "created_at": "2012-07-13T14:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87404",
    "user": "saliola"
}
```

There are a couple of patches on the sage-combinat queue experimenting with moving some of the generic methods into the category `GradedAlgebraWithBasis`:

- trac_9280-graded-algebras-example-review-fs.patch
- trac_9280-graded-algebras-example.patch



---

archive/issue_comments_087405.json:
```json
{
    "body": "Sorry for the long delay for the ticket but #10193 is now ready !!",
    "created_at": "2013-02-13T22:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87405",
    "user": "vdelecroix"
}
```

Sorry for the long delay for the ticket but #10193 is now ready !!



---

archive/issue_comments_087406.json:
```json
{
    "body": "Changing keywords from \"\" to \"graded algebra\".",
    "created_at": "2013-08-21T13:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87406",
    "user": "chapoton"
}
```

Changing keywords from "" to "graded algebra".



---

archive/issue_comments_087407.json:
```json
{
    "body": "Franco, Nicolas, what can we do with this ticket ? Should we use the patch from the combinat queue or the patch here ?",
    "created_at": "2013-08-23T08:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87407",
    "user": "chapoton"
}
```

Franco, Nicolas, what can we do with this ticket ? Should we use the patch from the combinat queue or the patch here ?



---

archive/issue_comments_087408.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-30T16:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87408",
    "user": "chapoton"
}
```

Attachment



---

archive/issue_comments_087409.json:
```json
{
    "body": "let me take the patch of sage-combinat as a starting point.\n\nfor the bot: apply only trac_9280-graded-algebras-example-fs.patch",
    "created_at": "2013-08-30T16:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87409",
    "user": "chapoton"
}
```

let me take the patch of sage-combinat as a starting point.

for the bot: apply only trac_9280-graded-algebras-example-fs.patch



---

archive/issue_comments_087410.json:
```json
{
    "body": "I don't know why I'm listed as an author in the file \"sage/categories/examples/graded_modules_with_basis.py\"; I don't think I had anything to do with that.",
    "created_at": "2013-08-30T17:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87410",
    "user": "jhpalmieri"
}
```

I don't know why I'm listed as an author in the file "sage/categories/examples/graded_modules_with_basis.py"; I don't think I had anything to do with that.



---

archive/issue_comments_087411.json:
```json
{
    "body": "The part of this patch concerning modules has been separated into ticket #11688 : the ticket #11688 should go first, then this one will need to be rebased on it. \n\nI upload here the \"algebra only patch\" that will be the new starting point.",
    "created_at": "2013-08-30T18:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87411",
    "user": "chapoton"
}
```

The part of this patch concerning modules has been separated into ticket #11688 : the ticket #11688 should go first, then this one will need to be rebased on it. 

I upload here the "algebra only patch" that will be the new starting point.



---

archive/issue_comments_087412.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-30T18:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87412",
    "user": "chapoton"
}
```

Attachment



---

archive/issue_comments_087413.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-09-15T16:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87413",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087414.json:
```json
{
    "body": "this needs to be rebased",
    "created_at": "2013-09-15T16:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87414",
    "user": "chapoton"
}
```

this needs to be rebased



---

archive/issue_comments_087415.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-12-20T03:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87415",
    "user": "tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087416.json:
```json
{
    "body": "Since the graded algebras with basis example is using (weighted) integer vectors, we need #12453. I'd like to attach the branch \"public/categories/graded_examples-9280\", but trac is giving me an error when I try...",
    "created_at": "2013-12-20T03:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87416",
    "user": "tscrim"
}
```

Since the graded algebras with basis example is using (weighted) integer vectors, we need #12453. I'd like to attach the branch "public/categories/graded_examples-9280", but trac is giving me an error when I try...



---

archive/issue_comments_087417.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-12-21T15:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87417",
    "user": "tscrim"
}
```

New commits:



---

archive/issue_comments_087418.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-25T19:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87418",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087419.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-02-08T17:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87419",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087420.json:
```json
{
    "body": "needs rebase",
    "created_at": "2014-08-10T11:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87420",
    "user": "chapoton"
}
```

needs rebase



---

archive/issue_comments_087421.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-08-10T11:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87421",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087422.json:
```json
{
    "body": "Yet another instance of someone asking a question related to this. Six (!) years ago, when I opened this ticket, I thought it would be good to have an example in the Sage library and in the documentation, and I really can't understand why this hasn't been taken care of yet. I am not interested in working on it myself any more, but I find it incredibly frustrating that this ticket has languished for so long.\n\nhttp://ask.sagemath.org/question/34577/can-sage-compute-a-basis-for-the-graded-parts-of-a-graded-ring/",
    "created_at": "2016-08-25T16:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87422",
    "user": "jhpalmieri"
}
```

Yet another instance of someone asking a question related to this. Six (!) years ago, when I opened this ticket, I thought it would be good to have an example in the Sage library and in the documentation, and I really can't understand why this hasn't been taken care of yet. I am not interested in working on it myself any more, but I find it incredibly frustrating that this ticket has languished for so long.

http://ask.sagemath.org/question/34577/can-sage-compute-a-basis-for-the-graded-parts-of-a-graded-ring/



---

archive/issue_comments_087423.json:
```json
{
    "body": "It is because of the dependency on integer vectors, which led to #12453. We can either give a new example based on another object or we review #12453 (which I just did a [non-trivial] rebase to the latest beta).",
    "created_at": "2016-08-25T19:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9280#issuecomment-87423",
    "user": "tscrim"
}
```

It is because of the dependency on integer vectors, which led to #12453. We can either give a new example based on another object or we review #12453 (which I just did a [non-trivial] rebase to the latest beta).
