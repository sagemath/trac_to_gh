# Issue 7938: 'term' and 'monomial' are inconsistently used in some Category and combinat code

archive/issues_007938.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  sage-combinat\n\nI'm including a patch, but will rebase it against 3.4.1 once it is released.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7938\n\n",
    "created_at": "2010-01-15T18:50:38Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "'term' and 'monomial' are inconsistently used in some Category and combinat code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7938",
    "user": "jbandlow"
}
```
Assignee: AlexGhitza

CC:  sage-combinat

I'm including a patch, but will rebase it against 3.4.1 once it is released.

Issue created by migration from https://trac.sagemath.org/ticket/7938





---

archive/issue_comments_069214.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-15T18:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69214",
    "user": "jbandlow"
}
```

Attachment



---

archive/issue_comments_069215.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-15T18:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69215",
    "user": "jbandlow"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069216.json:
```json
{
    "body": "Changing component from algebra to categories.",
    "created_at": "2010-01-15T18:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69216",
    "user": "jbandlow"
}
```

Changing component from algebra to categories.



---

archive/issue_comments_069217.json:
```json
{
    "body": "This change has been discussed and approved on sage-devel and sage-combinat-devel. I went through the current patch and it looks good. This is a conditional positive review, pending a rebase on 4.3.1 (if at all needed), a recheck of all tests passing, and two little details:\n\n- Renaming the patch to trac_7938_swap_term_and_monomial-jb.patch\n- Adding a short description on top of it; say something like: \"#7938: swap term and monomial in category and combinat code for consistency with the rest of sage\"\n\nThanks Jason!",
    "created_at": "2010-01-17T21:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69217",
    "user": "nthiery"
}
```

This change has been discussed and approved on sage-devel and sage-combinat-devel. I went through the current patch and it looks good. This is a conditional positive review, pending a rebase on 4.3.1 (if at all needed), a recheck of all tests passing, and two little details:

- Renaming the patch to trac_7938_swap_term_and_monomial-jb.patch
- Adding a short description on top of it; say something like: "#7938: swap term and monomial in category and combinat code for consistency with the rest of sage"

Thanks Jason!



---

archive/issue_comments_069218.json:
```json
{
    "body": "Replying to [comment:2 nthiery]:\nOops, I forgot the following:\n\n- Removing the spurious change to sage/combinat/crystals/affine.py\n- Adding a default value (the one of the coeff ring) for coeff in the new self.term, to make it backward compatible\n- Only if easy, make the new monomial accept a second optional coeff argument, to make it backward compatible. This could be a bit tricky, since self.monomial is a Map. It is also not as important as for term, since I expect the later to have been used far more more extensively than the former.",
    "created_at": "2010-01-17T21:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69218",
    "user": "nthiery"
}
```

Replying to [comment:2 nthiery]:
Oops, I forgot the following:

- Removing the spurious change to sage/combinat/crystals/affine.py
- Adding a default value (the one of the coeff ring) for coeff in the new self.term, to make it backward compatible
- Only if easy, make the new monomial accept a second optional coeff argument, to make it backward compatible. This could be a bit tricky, since self.monomial is a Map. It is also not as important as for term, since I expect the later to have been used far more more extensively than the former.



---

archive/issue_comments_069219.json:
```json
{
    "body": "Attachment\n\nThe patch called 'trac_7938_...' is all that should be applied.  In response to Nicolas' comments:\n* Rename patch: done\n* Add description: done\n* Remove spurious change to affine.py: done, but see #7978\n* Add default value for coeff in self.term: done\n* Add optional coeff argument to monomial: Not done yet. I'll look more (but maybe not much more) at this later.",
    "created_at": "2010-01-18T14:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69219",
    "user": "jbandlow"
}
```

Attachment

The patch called 'trac_7938_...' is all that should be applied.  In response to Nicolas' comments:
* Rename patch: done
* Add description: done
* Remove spurious change to affine.py: done, but see #7978
* Add default value for coeff in self.term: done
* Add optional coeff argument to monomial: Not done yet. I'll look more (but maybe not much more) at this later.



---

archive/issue_comments_069220.json:
```json
{
    "body": "Replying to [comment:4 jbandlow]:\n> ...\n\nThanks much!\n\n>   * Add description: done\n\nSorry for bothering you again. Please also remove the [mq] line, and put the rest on one line (hg treats the first line specifically).\n\nCheers,",
    "created_at": "2010-01-18T21:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69220",
    "user": "nthiery"
}
```

Replying to [comment:4 jbandlow]:
> ...

Thanks much!

>   * Add description: done

Sorry for bothering you again. Please also remove the [mq] line, and put the rest on one line (hg treats the first line specifically).

Cheers,



---

archive/issue_comments_069221.json:
```json
{
    "body": "It does need a rebase w.r.t. #7729 (iwahori hecke algebra) whose file was renamed.\n\nPlease update the queue accordingly (including the #7729 patch).",
    "created_at": "2010-01-21T18:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69221",
    "user": "nthiery"
}
```

It does need a rebase w.r.t. #7729 (iwahori hecke algebra) whose file was renamed.

Please update the queue accordingly (including the #7729 patch).



---

archive/issue_comments_069222.json:
```json
{
    "body": "Replying to [comment:6 nthiery]:\n> It does need a rebase w.r.t. #7729 (iwahori hecke algebra) whose file was renamed.\n> \n> Please update the queue accordingly (including the #7729 patch).\n\nDone!",
    "created_at": "2010-01-22T22:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69222",
    "user": "nthiery"
}
```

Replying to [comment:6 nthiery]:
> It does need a rebase w.r.t. #7729 (iwahori hecke algebra) whose file was renamed.
> 
> Please update the queue accordingly (including the #7729 patch).

Done!



---

archive/issue_comments_069223.json:
```json
{
    "body": "Rebased for 4.3.1",
    "created_at": "2010-01-23T10:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69223",
    "user": "nthiery"
}
```

Rebased for 4.3.1



---

archive/issue_comments_069224.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-23T10:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69224",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069225.json:
```json
{
    "body": "Attachment\n\n> Sorry for bothering you again. Please also remove the [mq] line, and put the rest on one line (hg treats the first line specifically).\n\nDone. Patch ready for merging into Sage.",
    "created_at": "2010-01-23T10:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69225",
    "user": "nthiery"
}
```

Attachment

> Sorry for bothering you again. Please also remove the [mq] line, and put the rest on one line (hg treats the first line specifically).

Done. Patch ready for merging into Sage.



---

archive/issue_comments_069226.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T10:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69226",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T10:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69227",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_069228.json:
```json
{
    "body": "Merged [trac_7938_swap_term_and_monomial-jb.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7938/trac_7938_swap_term_and_monomial-jb.2.patch).",
    "created_at": "2010-01-23T10:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7938#issuecomment-69228",
    "user": "mvngu"
}
```

Merged [trac_7938_swap_term_and_monomial-jb.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7938/trac_7938_swap_term_and_monomial-jb.2.patch).
