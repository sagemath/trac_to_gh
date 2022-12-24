# Issue 6452: codes over rings

archive/issues_006452.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  cesarnda@gmail.com dlucas jsrn\n\nThis module constructs codes over rings of the form ZZ/mZZ, that is, submodules of FreeModule(IntegerModRing(m), n).\nThe main authors are Cesar Agustin Garcia-Vazquez (who was an undergrad in Mexico when he wrote this) and Carlos A. Lopez-Andrade (his advisor). I made some changes to make it more consistent with LinearCode. (It still has some hidden differences - the basic problem being that FreeModule has no submodule or span method analogous that of VectorSpace.)\n\nIt is in Cython, which I confess I don't really understand well. My role is simply to take Cesar's code (which he emailed to me), tweek it a bit, and create a patch. He has explicitly agreed to distributing it under GPLv2+.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6452\n\n",
    "created_at": "2009-07-01T01:05:53Z",
    "labels": [
        "coding theory",
        "major",
        "enhancement"
    ],
    "title": "codes over rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6452",
    "user": "wdj"
}
```
Assignee: rlm

CC:  cesarnda@gmail.com dlucas jsrn

This module constructs codes over rings of the form ZZ/mZZ, that is, submodules of FreeModule(IntegerModRing(m), n).
The main authors are Cesar Agustin Garcia-Vazquez (who was an undergrad in Mexico when he wrote this) and Carlos A. Lopez-Andrade (his advisor). I made some changes to make it more consistent with LinearCode. (It still has some hidden differences - the basic problem being that FreeModule has no submodule or span method analogous that of VectorSpace.)

It is in Cython, which I confess I don't really understand well. My role is simply to take Cesar's code (which he emailed to me), tweek it a bit, and create a patch. He has explicitly agreed to distributing it under GPLv2+.

Issue created by migration from https://trac.sagemath.org/ticket/6452





---

archive/issue_comments_051896.json:
```json
{
    "body": "applies to 4.1.alpha1",
    "created_at": "2009-07-01T01:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51896",
    "user": "wdj"
}
```

applies to 4.1.alpha1



---

archive/issue_comments_051897.json:
```json
{
    "body": "Attachment [trac_6452-codes-over-rings.patch](tarball://root/attachments/some-uuid/ticket6452/trac_6452-codes-over-rings.patch) by wdj created at 2009-07-01 01:09:02\n\nThis applies to 4.1.alpha1. This passed sage -testall except for\n\n\n```\nThe following tests failed:                                                                             \n\n\n        sage -t  \"devel/sage/doc/fr/tutorial/programming.rst\"\n        sage -t  \"devel/sage/sage/misc/darwin_utilities.pyx\" \nTotal time for all tests: 6017.1 seconds                     \n```\n\nNeither of these failures seem related to this ticket.",
    "created_at": "2009-07-01T01:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51897",
    "user": "wdj"
}
```

Attachment [trac_6452-codes-over-rings.patch](tarball://root/attachments/some-uuid/ticket6452/trac_6452-codes-over-rings.patch) by wdj created at 2009-07-01 01:09:02

This applies to 4.1.alpha1. This passed sage -testall except for


```
The following tests failed:                                                                             


        sage -t  "devel/sage/doc/fr/tutorial/programming.rst"
        sage -t  "devel/sage/sage/misc/darwin_utilities.pyx" 
Total time for all tests: 6017.1 seconds                     
```

Neither of these failures seem related to this ticket.



---

archive/issue_comments_051898.json:
```json
{
    "body": "The patch doesn't contain the crucial file `ring_code.pyx`.  Maybe you forgot to add this file to the hg repository?",
    "created_at": "2009-07-11T09:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51898",
    "user": "AlexGhitza"
}
```

The patch doesn't contain the crucial file `ring_code.pyx`.  Maybe you forgot to add this file to the hg repository?



---

archive/issue_comments_051899.json:
```json
{
    "body": "ignore the previous patch; this applies to 4.1.2.rc2",
    "created_at": "2009-10-18T19:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51899",
    "user": "wdj"
}
```

ignore the previous patch; this applies to 4.1.2.rc2



---

archive/issue_comments_051900.json:
```json
{
    "body": "Attachment [trac_6452-ring-codes.patch](tarball://root/attachments/some-uuid/ticket6452/trac_6452-ring-codes.patch) by wdj created at 2009-10-18 19:52:43\n\nThis latest patch fixes some problems prointed out in private emails from Dan Gordon.",
    "created_at": "2009-10-18T19:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51900",
    "user": "wdj"
}
```

Attachment [trac_6452-ring-codes.patch](tarball://root/attachments/some-uuid/ticket6452/trac_6452-ring-codes.patch) by wdj created at 2009-10-18 19:52:43

This latest patch fixes some problems prointed out in private emails from Dan Gordon.



---

archive/issue_comments_051901.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-18T19:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51901",
    "user": "wdj"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_051902.json:
```json
{
    "body": "I can also say that the module in coding pass sage -t, with this patch applied, in OS 10.6 on an imac. OS10.6 does not pass sage -testall. However, I do have ubuntu 9.04 32bit installed under vmware on this machine and can test it there if desired.",
    "created_at": "2009-10-18T20:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51902",
    "user": "wdj"
}
```

I can also say that the module in coding pass sage -t, with this patch applied, in OS 10.6 on an imac. OS10.6 does not pass sage -testall. However, I do have ubuntu 9.04 32bit installed under vmware on this machine and can test it there if desired.



---

archive/issue_comments_051903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-30T01:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51903",
    "user": "dgordon"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051904.json:
```json
{
    "body": "Is there any way we can get documentation for the cdef methods as well as possibly some more code comments?  I'm just worried that there's no one who is able to maintain this code.\n\nAlso, it's not clear to me that there are not memory leak issues with this code as there are lots of malloc's and only one free.",
    "created_at": "2009-10-31T07:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51904",
    "user": "mhansen"
}
```

Is there any way we can get documentation for the cdef methods as well as possibly some more code comments?  I'm just worried that there's no one who is able to maintain this code.

Also, it's not clear to me that there are not memory leak issues with this code as there are lots of malloc's and only one free.



---

archive/issue_comments_051905.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-10-31T07:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51905",
    "user": "mhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_051906.json:
```json
{
    "body": "If someone can explain to me what those functions will do, I will add comments on them.\nAs I said, I am basically doing a favor by posting a patch of someone else's code. I had to make a lot of additions to make it consistent with other parts of the codes library, but basically it is Cesar's code. Personally, I really don't understand the cython stuff.\n\nDoes this mean that the code will not be accepted?",
    "created_at": "2009-11-17T00:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51906",
    "user": "wdj"
}
```

If someone can explain to me what those functions will do, I will add comments on them.
As I said, I am basically doing a favor by posting a patch of someone else's code. I had to make a lot of additions to make it consistent with other parts of the codes library, but basically it is Cesar's code. Personally, I really don't understand the cython stuff.

Does this mean that the code will not be accepted?



---

archive/issue_comments_051907.json:
```json
{
    "body": "Replying to [comment:7 mhansen]:\n> Is there any way we can get documentation for the cdef methods as well as \n> possibly some more code comments?  I'm just worried that there's no one who is \n> able to maintain this code.\n> \n> Also, it's not clear to me that there are not memory leak issues with this \n> code as there are lots of malloc's and only one free.\n\nAs I said, I could try to add comments to the code, but I really don't know cython\nnearly well enough to deal with malloc issues.\n\nI've emailed Cesar and not gotten any response about the memory leak issues.\n\nGiven that, should the status change to \"resolve as won't fix\"? That would be too bad since Sage could really use \"linear codes\" over rings.",
    "created_at": "2009-12-22T12:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51907",
    "user": "wdj"
}
```

Replying to [comment:7 mhansen]:
> Is there any way we can get documentation for the cdef methods as well as 
> possibly some more code comments?  I'm just worried that there's no one who is 
> able to maintain this code.
> 
> Also, it's not clear to me that there are not memory leak issues with this 
> code as there are lots of malloc's and only one free.

As I said, I could try to add comments to the code, but I really don't know cython
nearly well enough to deal with malloc issues.

I've emailed Cesar and not gotten any response about the memory leak issues.

Given that, should the status change to "resolve as won't fix"? That would be too bad since Sage could really use "linear codes" over rings.



---

archive/issue_comments_051908.json:
```json
{
    "body": "Hello,\n\nI updated a git branch with the patch provided + some corrections. It is not yet in final stage but not far from it!\n\nVincent\n----\nNew commits:",
    "created_at": "2015-09-13T22:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51908",
    "user": "vdelecroix"
}
```

Hello,

I updated a git branch with the patch provided + some corrections. It is not yet in final stage but not far from it!

Vincent
----
New commits:



---

archive/issue_comments_051909.json:
```json
{
    "body": "I'm not particularly fond of this patch, I must admit. It doesn't seem very well thought out. I prefer not putting in code which is weak and not thought through, rather than superficially being able to claim that \"Sage can do codes over rings\". For instance, what can the code actually do right now, besides computing the list of codewords?\n\nSome concrete complaints:\n\n* `gen_mat` should (nowadays) be `generator_matrix`.\n* The class has many non-hidden-but-actually-private-and-stupidly-named fields\n  `self.codeSet`, `self.minimum`, etc. They should be renamed and start with an underscore.\n* `next(self)` is not the way we implement iterators, AFAIK.\n* The name `RingCode` is not sensible, since only `ZZ/mZZ` is supported.\n* The mathematical object of such a code is a free `ZZ/mZZ` module. Shouldn't\n  this be reflected by some parent/category magic in `__init__`?\n* `__latex__` is wrong: it says \"Linear code\".\n* English is bad in some texts, e.g. for `length()`, a \"the\" is missing.\n* What's the point of `spanning_codewords`? The nomenclature is not used in\n  `LinearCode`, and function just returns the rows of the generator matrix\n  anyway.\n\nOn a broader design level: I dislike that tons of computation is done at `__init__`, in particular tabulating all codewords. In coding theory stuff that I have been involved in, we have tried very hard to postpone computation until it becomes necessary. In particular, construction should be cheap.\n\nFor instance, I think that e.g. the cardinality of such a code can be relatively easily computed without tabulating the entire code.\n\nThe design of ring codes should also think the new (well, almost-accepted) `Encoder` and `Decoder` structure into it: #18376, #18813.\n\nNote that I did not run or test the code -- I just looked at it.",
    "created_at": "2015-09-14T14:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51909",
    "user": "jsrn"
}
```

I'm not particularly fond of this patch, I must admit. It doesn't seem very well thought out. I prefer not putting in code which is weak and not thought through, rather than superficially being able to claim that "Sage can do codes over rings". For instance, what can the code actually do right now, besides computing the list of codewords?

Some concrete complaints:

* `gen_mat` should (nowadays) be `generator_matrix`.
* The class has many non-hidden-but-actually-private-and-stupidly-named fields
  `self.codeSet`, `self.minimum`, etc. They should be renamed and start with an underscore.
* `next(self)` is not the way we implement iterators, AFAIK.
* The name `RingCode` is not sensible, since only `ZZ/mZZ` is supported.
* The mathematical object of such a code is a free `ZZ/mZZ` module. Shouldn't
  this be reflected by some parent/category magic in `__init__`?
* `__latex__` is wrong: it says "Linear code".
* English is bad in some texts, e.g. for `length()`, a "the" is missing.
* What's the point of `spanning_codewords`? The nomenclature is not used in
  `LinearCode`, and function just returns the rows of the generator matrix
  anyway.

On a broader design level: I dislike that tons of computation is done at `__init__`, in particular tabulating all codewords. In coding theory stuff that I have been involved in, we have tried very hard to postpone computation until it becomes necessary. In particular, construction should be cheap.

For instance, I think that e.g. the cardinality of such a code can be relatively easily computed without tabulating the entire code.

The design of ring codes should also think the new (well, almost-accepted) `Encoder` and `Decoder` structure into it: #18376, #18813.

Note that I did not run or test the code -- I just looked at it.



---

archive/issue_comments_051910.json:
```json
{
    "body": "Thanks for having a look. (disclaimer: I actually only ended up here because of [this question on ask](http://ask.sagemath.org/question/29424/liner-code-over-integerring/)).\n\nReplying to [comment:17 jsrn]:\n> I'm not particularly fond of this patch, I must admit. It doesn't seem very well thought out. I prefer not putting in code which is weak and not thought through, rather than superficially being able to claim that \"Sage can do codes over rings\". For instance, what can the code actually do right now, besides computing the list of codewords?\n\nNothing I guess. But it is already something and it seems to be done efficiently.\n\n> Some concrete complaints:\n> \n> * The mathematical object of such a code is a free `ZZ/mZZ` module. Shouldn't\n>   this be reflected by some parent/category magic in `__init__`?\n\nNope. It is not necessarily free. The submodule of `(ZZ/4ZZ)` generated by `2` is **not** free.\n\n> On a broader design level: I dislike that tons of computation is done at `__init__`, in particular tabulating all codewords. In coding theory stuff that I have been involved in, we have tried very hard to postpone computation until it becomes necessary. In particular, construction should be cheap.\n\nI guess it would be reasonable to turn it into a function or method.\n\n> For instance, I think that e.g. the cardinality of such a code can be relatively easily computed without tabulating the entire code.\n\nTrue. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a \"pseudo-basis\" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.\n\n> The design of ring codes should also think the new (well, almost-accepted) `Encoder` and `Decoder` structure into it: #18376, #18813.\n\n+1\n \n> Note that I did not run or test the code -- I just looked at it.\n\nThe tests do not pass, but at least some examples run just nicely. Moreover, there was at least one person interested. This is why I thought it would be worse to make it a branch.\n\nVincent",
    "created_at": "2015-09-14T15:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51910",
    "user": "vdelecroix"
}
```

Thanks for having a look. (disclaimer: I actually only ended up here because of [this question on ask](http://ask.sagemath.org/question/29424/liner-code-over-integerring/)).

Replying to [comment:17 jsrn]:
> I'm not particularly fond of this patch, I must admit. It doesn't seem very well thought out. I prefer not putting in code which is weak and not thought through, rather than superficially being able to claim that "Sage can do codes over rings". For instance, what can the code actually do right now, besides computing the list of codewords?

Nothing I guess. But it is already something and it seems to be done efficiently.

> Some concrete complaints:
> 
> * The mathematical object of such a code is a free `ZZ/mZZ` module. Shouldn't
>   this be reflected by some parent/category magic in `__init__`?

Nope. It is not necessarily free. The submodule of `(ZZ/4ZZ)` generated by `2` is **not** free.

> On a broader design level: I dislike that tons of computation is done at `__init__`, in particular tabulating all codewords. In coding theory stuff that I have been involved in, we have tried very hard to postpone computation until it becomes necessary. In particular, construction should be cheap.

I guess it would be reasonable to turn it into a function or method.

> For instance, I think that e.g. the cardinality of such a code can be relatively easily computed without tabulating the entire code.

True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a "pseudo-basis" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.

> The design of ring codes should also think the new (well, almost-accepted) `Encoder` and `Decoder` structure into it: #18376, #18813.

+1
 
> Note that I did not run or test the code -- I just looked at it.

The tests do not pass, but at least some examples run just nicely. Moreover, there was at least one person interested. This is why I thought it would be worse to make it a branch.

Vincent



---

archive/issue_comments_051911.json:
```json
{
    "body": "> Nothing I guess. But it is already something and it seems to be done efficiently.\n\nWell, it's perhaps efficient if what you want is to tabulate the entire code and immediately ask it for various stuff (like minimum distance). It's inefficient if you are only interested in some of the properties.\n\nOn the other hand, the implementation forces Cython on pretty base functionality. I'm not sure what kind of speed-up Cython brings here as opposed to pure Python -- after all, the actual work is done in finite field arithmetic. It would be interesting to compare and see whether Cython is worth it.\n\n> Nope. It is not necessarily free. The submodule of `(ZZ/4ZZ)` generated by `2` is **not** free.\n\nNo of course you're right that it's not -- the word \"free\" slipped in there by mistake. But it *is* a module.\n\n> I guess it would be reasonable to turn it into a function or method.\n\nMinimum distance and minimum codeword computation should also be extracted from the code tabulation. I might want the list of codewords but not care about the minimum distance, and so computing the hamming weight of all the vectors is a huge waste.\n\n> True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a \"pseudo-basis\" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.\n\nIt's interesting: I'll think more on this. For instance, would the Hermite Normal form be sufficient?\n\n> The tests do not pass, but at least some examples run just nicely. Moreover, there was at least one person interested. This is why I thought it would be worse to make it a branch.\n\nYou are right, it would be nice to support codes over `ZZ/mZZ`. I just want to avoid adding stuff that will have to be reformed through a heavy reviewing process just a bit further down the road ;-)",
    "created_at": "2015-09-15T07:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51911",
    "user": "jsrn"
}
```

> Nothing I guess. But it is already something and it seems to be done efficiently.

Well, it's perhaps efficient if what you want is to tabulate the entire code and immediately ask it for various stuff (like minimum distance). It's inefficient if you are only interested in some of the properties.

On the other hand, the implementation forces Cython on pretty base functionality. I'm not sure what kind of speed-up Cython brings here as opposed to pure Python -- after all, the actual work is done in finite field arithmetic. It would be interesting to compare and see whether Cython is worth it.

> Nope. It is not necessarily free. The submodule of `(ZZ/4ZZ)` generated by `2` is **not** free.

No of course you're right that it's not -- the word "free" slipped in there by mistake. But it *is* a module.

> I guess it would be reasonable to turn it into a function or method.

Minimum distance and minimum codeword computation should also be extracted from the code tabulation. I might want the list of codewords but not care about the minimum distance, and so computing the hamming weight of all the vectors is a huge waste.

> True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a "pseudo-basis" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.

It's interesting: I'll think more on this. For instance, would the Hermite Normal form be sufficient?

> The tests do not pass, but at least some examples run just nicely. Moreover, there was at least one person interested. This is why I thought it would be worse to make it a branch.

You are right, it would be nice to support codes over `ZZ/mZZ`. I just want to avoid adding stuff that will have to be reformed through a heavy reviewing process just a bit further down the road ;-)



---

archive/issue_comments_051912.json:
```json
{
    "body": "Replying to [comment:19 jsrn]:\n> > True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a \"pseudo-basis\" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.\n> \n> It's interesting: I'll think more on this. For instance, would the Hermite Normal form be sufficient?\n\nI don't think that it is enough to determine the structure. An example of a problem is if `R=ZZ/4ZZ` and a matrix of the form\n\n```\n2 * *\n0 2 *\n0 0 2\n```\n\nIf you have a vector which is a sum of its row with coefficients `0` or `2` then the leading coefficient vanish... and you lose the nice Hermite form!\n\nBut I guess that the Smith normal form would be of more help. If I intrepret correctly what I read, it tells you that any submodule of `R^r` where `R = ZZ/nZZ` is actually of the form `R / (I1) + R / (I2) + ... + R / (Ik)` for some ideals `I1`, ..., `Ik`. These ideals are basically the product `SAT` (which is diagonal) and the decomposition is explicitly given by `T` (my source and notations from [wikipedia](https://en.wikipedia.org/wiki/Smith_normal_form)).",
    "created_at": "2015-10-02T02:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51912",
    "user": "vdelecroix"
}
```

Replying to [comment:19 jsrn]:
> > True. It would basically be equivalent to implement a generalized echelon form for matrices over `ZZ/nZZ` that give you a "pseudo-basis" of submodules of `(ZZ/nZZ)^r`. I have no idea where to find such algorithm.
> 
> It's interesting: I'll think more on this. For instance, would the Hermite Normal form be sufficient?

I don't think that it is enough to determine the structure. An example of a problem is if `R=ZZ/4ZZ` and a matrix of the form

```
2 * *
0 2 *
0 0 2
```

If you have a vector which is a sum of its row with coefficients `0` or `2` then the leading coefficient vanish... and you lose the nice Hermite form!

But I guess that the Smith normal form would be of more help. If I intrepret correctly what I read, it tells you that any submodule of `R^r` where `R = ZZ/nZZ` is actually of the form `R / (I1) + R / (I2) + ... + R / (Ik)` for some ideals `I1`, ..., `Ik`. These ideals are basically the product `SAT` (which is diagonal) and the decomposition is explicitly given by `T` (my source and notations from [wikipedia](https://en.wikipedia.org/wiki/Smith_normal_form)).



---

archive/issue_comments_051913.json:
```json
{
    "body": "I think you're right that the Smith form is exactly what is needed, for the reasons you mention. Ok, so that would be elegant to have in this patch :-)",
    "created_at": "2015-10-02T22:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51913",
    "user": "jsrn"
}
```

I think you're right that the Smith form is exactly what is needed, for the reasons you mention. Ok, so that would be elegant to have in this patch :-)



---

archive/issue_comments_051914.json:
```json
{
    "body": "All right, I will try to do something. I had a more careful look at the code (and the corresponding master thesis) but I was not able to understand anything. With the Smith form it will also be straightforward to implement a (possibly very efficient) iterator over the elements of the module.\n\nOne non trivial point is to decide equality of sub-modules. The only canonical part of the Smith form is the diagonal matrix (which only gives you a hint about isomorphisms between submodules). But I guess that we can somehow echelonize the part corresponding to a given ideal. I would be much more happy with a clean reference...\n\nSince this is more about submodules of `(ZZ/nZZ)^r` I am not sure it should go at all inside `sage.codings`. I would rather put it in `sage.modules`. And (as I already told you), it would be better to factorize more between `sage.modules` and `sage.codings` when the code is **only** given by a generator matrix. So, for the sake of this ticket, my concrete proposal is:\n- implement submodules of `(ZZ/nZZ)^r` with a canonical form\n- have an efficient iterator\nIf you think it is not too far from the original purpose of this ticket, I will modify the ticket description accordingly.",
    "created_at": "2015-10-02T22:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51914",
    "user": "vdelecroix"
}
```

All right, I will try to do something. I had a more careful look at the code (and the corresponding master thesis) but I was not able to understand anything. With the Smith form it will also be straightforward to implement a (possibly very efficient) iterator over the elements of the module.

One non trivial point is to decide equality of sub-modules. The only canonical part of the Smith form is the diagonal matrix (which only gives you a hint about isomorphisms between submodules). But I guess that we can somehow echelonize the part corresponding to a given ideal. I would be much more happy with a clean reference...

Since this is more about submodules of `(ZZ/nZZ)^r` I am not sure it should go at all inside `sage.codings`. I would rather put it in `sage.modules`. And (as I already told you), it would be better to factorize more between `sage.modules` and `sage.codings` when the code is **only** given by a generator matrix. So, for the sake of this ticket, my concrete proposal is:
- implement submodules of `(ZZ/nZZ)^r` with a canonical form
- have an efficient iterator
If you think it is not too far from the original purpose of this ticket, I will modify the ticket description accordingly.



---

archive/issue_comments_051915.json:
```json
{
    "body": "Replying to [comment:22 vdelecroix]:\n> All right, I will try to do something. I had a more careful look at the code (and the corresponding master thesis) but I was not able to understand anything. With the Smith form it will also be straightforward to implement a (possibly very efficient) iterator over the elements of the module.\n\nNice, I didn't consider that.\n\n> One non trivial point is to decide equality of sub-modules. The only canonical part of the Smith form is the diagonal matrix (which only gives you a hint about isomorphisms between submodules). But I guess that we can somehow echelonize the part corresponding to a given ideal. I would be much more happy with a clean reference...\n> \n> Since this is more about submodules of `(ZZ/nZZ)^r` I am not sure it should go at all inside `sage.codings`. I would rather put it in `sage.modules`. And (as I already told you), it would be better to factorize more between `sage.modules` and `sage.codings` when the code is **only** given by a generator matrix. So, for the sake of this ticket, my concrete proposal is:\n>  - implement submodules of `(ZZ/nZZ)^r` with a canonical form\n>  - have an efficient iterator\n> If you think it is not too far from the original purpose of this ticket, I will modify the ticket description accordingly.\n\nSuch a ticket would definitely make sense. And it seem to cover most of the functionality here (I mean, the minimum distance is right now just exhaustive checking distances...)\n\nThe distinction between vector subspaces and linear codes (given only by their generator matrix) is right now that the latter exposes a list of specialised coding theory functions. Such functions might be interesting for non-coding theorists, but probably won't be. That's an argument for having a special class which basically just wraps vector subspaces. Exactly the same argument could be made for submodules of `(ZZ/nZZ)^r`. But no need to get ahead of ourselves here, though...\n\nA different matter: the current patch is Cython. Do we want that? I remember Jeroen's advice to always try Cython only after you have determined that you really need the performance, and that Cython will give this to you.",
    "created_at": "2015-10-02T23:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51915",
    "user": "jsrn"
}
```

Replying to [comment:22 vdelecroix]:
> All right, I will try to do something. I had a more careful look at the code (and the corresponding master thesis) but I was not able to understand anything. With the Smith form it will also be straightforward to implement a (possibly very efficient) iterator over the elements of the module.

Nice, I didn't consider that.

> One non trivial point is to decide equality of sub-modules. The only canonical part of the Smith form is the diagonal matrix (which only gives you a hint about isomorphisms between submodules). But I guess that we can somehow echelonize the part corresponding to a given ideal. I would be much more happy with a clean reference...
> 
> Since this is more about submodules of `(ZZ/nZZ)^r` I am not sure it should go at all inside `sage.codings`. I would rather put it in `sage.modules`. And (as I already told you), it would be better to factorize more between `sage.modules` and `sage.codings` when the code is **only** given by a generator matrix. So, for the sake of this ticket, my concrete proposal is:
>  - implement submodules of `(ZZ/nZZ)^r` with a canonical form
>  - have an efficient iterator
> If you think it is not too far from the original purpose of this ticket, I will modify the ticket description accordingly.

Such a ticket would definitely make sense. And it seem to cover most of the functionality here (I mean, the minimum distance is right now just exhaustive checking distances...)

The distinction between vector subspaces and linear codes (given only by their generator matrix) is right now that the latter exposes a list of specialised coding theory functions. Such functions might be interesting for non-coding theorists, but probably won't be. That's an argument for having a special class which basically just wraps vector subspaces. Exactly the same argument could be made for submodules of `(ZZ/nZZ)^r`. But no need to get ahead of ourselves here, though...

A different matter: the current patch is Cython. Do we want that? I remember Jeroen's advice to always try Cython only after you have determined that you really need the performance, and that Cython will give this to you.



---

archive/issue_comments_051916.json:
```json
{
    "body": "Replying to [comment:23 jsrn]:\n> Replying to [comment:22 vdelecroix]: \n> A different matter: the current patch is Cython. Do we want that? I remember Jeroen's advice to always try Cython only after you have determined that you really need the performance, and that Cython will give this to you.\n\nMost of it will be in Python. Only the iterator can possibly be in Cython and it should not be more than 20 lines of code. But it makes sense to do it in a second time.",
    "created_at": "2015-10-03T00:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51916",
    "user": "vdelecroix"
}
```

Replying to [comment:23 jsrn]:
> Replying to [comment:22 vdelecroix]: 
> A different matter: the current patch is Cython. Do we want that? I remember Jeroen's advice to always try Cython only after you have determined that you really need the performance, and that Cython will give this to you.

Most of it will be in Python. Only the iterator can possibly be in Cython and it should not be more than 20 lines of code. But it makes sense to do it in a second time.



---

archive/issue_comments_051917.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-10-04T01:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51917",
    "user": "vdelecroix"
}
```

New commits:



---

archive/issue_comments_051918.json:
```json
{
    "body": "Changing component from coding theory to linear algebra.",
    "created_at": "2015-10-04T01:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51918",
    "user": "vdelecroix"
}
```

Changing component from coding theory to linear algebra.



---

archive/issue_comments_051919.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-10-04T01:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51919",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_051920.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-04T18:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51920",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_051921.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-04T18:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51921",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_051922.json:
```json
{
    "body": "For the iterator, see #19345",
    "created_at": "2015-10-04T22:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51922",
    "user": "vdelecroix"
}
```

For the iterator, see #19345



---

archive/issue_comments_051923.json:
```json
{
    "body": "Great work Vincent!\n\nJust to be sure: is this \"In review\"? You made many changes but didn't change the state of \"needs review\".\n\nI will look at it in detail later, and when I'm sure it's ready. But in any case, some preliminary remarks:\n\n- Could you explain to me (reviewer) the reason for the patch in the category\n  files? Something with you using the `Facade` in a previously unthought case.\n  Is this related to the `Free`-thing below?\n\n- `FreeModule_ambient_IntegerModRing.span` never uses its `check` argument.\n\n- Since you compute the smith form at construction, then construction is expensive even when nothing is asked of the object afterwards. Is the argument for this that nothing interesting can be said about the module without computing the smith form anyway? Generally, I like construction to be cheap and postponing computation till the user asks it.\n\nGenerally, it looks pretty good though.",
    "created_at": "2015-10-05T00:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51923",
    "user": "jsrn"
}
```

Great work Vincent!

Just to be sure: is this "In review"? You made many changes but didn't change the state of "needs review".

I will look at it in detail later, and when I'm sure it's ready. But in any case, some preliminary remarks:

- Could you explain to me (reviewer) the reason for the patch in the category
  files? Something with you using the `Facade` in a previously unthought case.
  Is this related to the `Free`-thing below?

- `FreeModule_ambient_IntegerModRing.span` never uses its `check` argument.

- Since you compute the smith form at construction, then construction is expensive even when nothing is asked of the object afterwards. Is the argument for this that nothing interesting can be said about the module without computing the smith form anyway? Generally, I like construction to be cheap and postponing computation till the user asks it.

Generally, it looks pretty good though.



---

archive/issue_comments_051924.json:
```json
{
    "body": "Hi,\n\nReplying to [comment:29 jsrn]:\n> Great work Vincent!\n\nThanks ;-)\n \n> Just to be sure: is this \"In review\"? You made many changes but didn't change the state of \"needs review\".\n\nIt is in needs review. After the first commit, it appears that one doctest failed. And then, I found many typos and some better conventions. This is why there are so much commits afterwards. Shortly: it is ready and in needs review.\n\n> I will look at it in detail later, and when I'm sure it's ready. But in any case, some preliminary remarks:\n> \n> - Could you explain to me (reviewer) the reason for the patch in the category\n>   files? Something with you using the `Facade` in a previously unthought case.\n>   Is this related to the `Free`-thing below?\n\nNope. There is no `TestSuite(U).run()` anywhere for submodules. And this is the reason why.\n\nA facade is a concept from the Sage category. A parent is a facade if its elements do not belong to itself, as for submodules\n\n```\nsage: F = FreeModule(ZZ,2)\nsage: U = F.span([F((3,0))])\nsage: U.an_element().parent() is U\nFalse\nsage: U.an_element().parent() is F\nTrue\n```\n\nSo `U` is a **facade** for `F`. But this is currently not properly done\n\n```\nsage: U in Sets().Facade()\nFalse\n```\n\nI did it for the submodules over `ZZ/nZZ`. I will fix it later on for the other base rings as well and add some `TestSuite`.\n\nThere are many generic tests in category (that are automatically run with the `TestSuite` thing) but some of them do not care about facades. In particulal the `_test_zero` and `_test_one` that I modified.\n\n> - `FreeModule_ambient_IntegerModRing.span` never uses its `check` argument.\n\nTrue. I did it for compatibility with the other `span` functions. Maybe I could remove it.\n\n> - Since you compute the smith form at construction, then construction is expensive even when nothing is asked of the object afterwards. Is the argument for this that nothing interesting can be said about the module without computing the smith form anyway? Generally, I like construction to be cheap and postponing computation till the user asks it.\n\nWithout this nothing can be computed (number of generators, cardinality). Note that I postponed the `_lift` argument computation.",
    "created_at": "2015-10-05T01:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51924",
    "user": "vdelecroix"
}
```

Hi,

Replying to [comment:29 jsrn]:
> Great work Vincent!

Thanks ;-)
 
> Just to be sure: is this "In review"? You made many changes but didn't change the state of "needs review".

It is in needs review. After the first commit, it appears that one doctest failed. And then, I found many typos and some better conventions. This is why there are so much commits afterwards. Shortly: it is ready and in needs review.

> I will look at it in detail later, and when I'm sure it's ready. But in any case, some preliminary remarks:
> 
> - Could you explain to me (reviewer) the reason for the patch in the category
>   files? Something with you using the `Facade` in a previously unthought case.
>   Is this related to the `Free`-thing below?

Nope. There is no `TestSuite(U).run()` anywhere for submodules. And this is the reason why.

A facade is a concept from the Sage category. A parent is a facade if its elements do not belong to itself, as for submodules

```
sage: F = FreeModule(ZZ,2)
sage: U = F.span([F((3,0))])
sage: U.an_element().parent() is U
False
sage: U.an_element().parent() is F
True
```

So `U` is a **facade** for `F`. But this is currently not properly done

```
sage: U in Sets().Facade()
False
```

I did it for the submodules over `ZZ/nZZ`. I will fix it later on for the other base rings as well and add some `TestSuite`.

There are many generic tests in category (that are automatically run with the `TestSuite` thing) but some of them do not care about facades. In particulal the `_test_zero` and `_test_one` that I modified.

> - `FreeModule_ambient_IntegerModRing.span` never uses its `check` argument.

True. I did it for compatibility with the other `span` functions. Maybe I could remove it.

> - Since you compute the smith form at construction, then construction is expensive even when nothing is asked of the object afterwards. Is the argument for this that nothing interesting can be said about the module without computing the smith form anyway? Generally, I like construction to be cheap and postponing computation till the user asks it.

Without this nothing can be computed (number of generators, cardinality). Note that I postponed the `_lift` argument computation.



---

archive/issue_comments_051925.json:
```json
{
    "body": "Note that in the other functions there is a `already_echelonized` function that precisely prevent any computation (assuming that the fed data is in good shape). Perhaps we can add a `already_schmidt_reduced` argument?",
    "created_at": "2015-10-05T01:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51925",
    "user": "vdelecroix"
}
```

Note that in the other functions there is a `already_echelonized` function that precisely prevent any computation (assuming that the fed data is in good shape). Perhaps we can add a `already_schmidt_reduced` argument?



---

archive/issue_comments_051926.json:
```json
{
    "body": "About facade sets, you can read the documentation of `sage.categories.sets_cat.Sets.SubcategoryMethods.Facade`.",
    "created_at": "2015-10-05T01:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51926",
    "user": "vdelecroix"
}
```

About facade sets, you can read the documentation of `sage.categories.sets_cat.Sets.SubcategoryMethods.Facade`.



---

archive/issue_comments_051927.json:
```json
{
    "body": "And I just notice that the other submodules are actually **not** facade sets... I should definitely follow the same convention!",
    "created_at": "2015-10-05T02:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51927",
    "user": "vdelecroix"
}
```

And I just notice that the other submodules are actually **not** facade sets... I should definitely follow the same convention!



---

archive/issue_comments_051928.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-10-05T02:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51928",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_051929.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-10-05T03:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51929",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_051930.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-10-05T03:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51930",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_051931.json:
```json
{
    "body": "Warning: this is a forced push (branch restarted from zero)\n\nDisclaimer: since I had to get rid of facades it did not make sense to just revert all what I did before\n\nNow, no worries about facades... they do not appear anymore. Needs review again.\n\nVincent",
    "created_at": "2015-10-05T03:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51931",
    "user": "vdelecroix"
}
```

Warning: this is a forced push (branch restarted from zero)

Disclaimer: since I had to get rid of facades it did not make sense to just revert all what I did before

Now, no worries about facades... they do not appear anymore. Needs review again.

Vincent



---

archive/issue_comments_051932.json:
```json
{
    "body": "(ping)",
    "created_at": "2015-12-07T21:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51932",
    "user": "vdelecroix"
}
```

(ping)



---

archive/issue_comments_051933.json:
```json
{
    "body": "there is an old-style print somewhere, see bot report",
    "created_at": "2016-07-12T09:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51933",
    "user": "chapoton"
}
```

there is an old-style print somewhere, see bot report



---

archive/issue_comments_051934.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-07-29T06:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51934",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_051935.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2019-03-05T10:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51935",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_051936.json:
```json
{
    "body": "New commits:",
    "created_at": "2019-03-05T10:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51936",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_051937.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2019-03-05T12:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51937",
    "user": "chapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_051938.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2019-03-07T20:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51938",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_051939.json:
```json
{
    "body": "this need a python3 refreshment, to avoid cmp and long",
    "created_at": "2019-03-07T20:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51939",
    "user": "chapoton"
}
```

this need a python3 refreshment, to avoid cmp and long



---

archive/issue_comments_051940.json:
```json
{
    "body": "Tickets still needing working or clarification should be moved to the next release milestone at the soonest (please feel free to revert if you think the ticket is close to being resolved).",
    "created_at": "2019-06-14T14:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51940",
    "user": "embray"
}
```

Tickets still needing working or clarification should be moved to the next release milestone at the soonest (please feel free to revert if you think the ticket is close to being resolved).



---

archive/issue_comments_051941.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2019-12-30T14:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51941",
    "user": "embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_comments_051942.json:
```json
{
    "body": "Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.",
    "created_at": "2020-04-14T19:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51942",
    "user": "mkoeppe"
}
```

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.



---

archive/issue_comments_051943.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51943",
    "user": "mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_comments_051944.json:
```json
{
    "body": "Setting a new milestone for this ticket based on a cursory review.",
    "created_at": "2021-07-19T00:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6452#issuecomment-51944",
    "user": "mkoeppe"
}
```

Setting a new milestone for this ticket based on a cursory review.
