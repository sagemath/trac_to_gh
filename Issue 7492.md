# Issue 7492: Decomposition of a doubly stochastic matrix as a convex sum of permutations

archive/issues_007492.json:
```json
{
    "body": "Assignee: mhansen\n\nAs the title says, there is a theorem saying that any doubly stochastic matrix ( http://en.wikipedia.org/wiki/Doubly_stochastic_matrix ) can be written as a convex sum of permutations.\n\nA proof and an algorithm can be found in this book : http://www.thi.informatik.uni-frankfurt.de/~jukna/EC_Book/\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7492\n\n",
    "created_at": "2009-11-19T09:50:11Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Decomposition of a doubly stochastic matrix as a convex sum of permutations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7492",
    "user": "ncohen"
}
```
Assignee: mhansen

As the title says, there is a theorem saying that any doubly stochastic matrix ( http://en.wikipedia.org/wiki/Doubly_stochastic_matrix ) can be written as a convex sum of permutations.

A proof and an algorithm can be found in this book : http://www.thi.informatik.uni-frankfurt.de/~jukna/EC_Book/

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7492





---

archive/issue_comments_063276.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-20T09:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63276",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063277.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-27T18:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63277",
    "user": "mhansen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063278.json:
```json
{
    "body": "This patch needs to be updated as there is no max_matching method for graphs.",
    "created_at": "2009-12-27T18:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63278",
    "user": "mhansen"
}
```

This patch needs to be updated as there is no max_matching method for graphs.



---

archive/issue_comments_063279.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-27T19:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63279",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063280.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-17T10:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63280",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063281.json:
```json
{
    "body": "Needs work, I'm afraid.\n\n- Firstly, there are no checks on the input type. It will happily accept non-doubly-stochastic matrices, and return garbage; and it seems to silently replace real numbers with rational approximations to them, which is frankly rather weird. The docstring should state clearly what base rings are allowed (integers? rationals? reals?) and there should be a check to make sure that the input matrix really is a doubly stochastic matrix over one of these base rings.\n\n- The doctests won't work without an optional spkg, so they should be flagged as such.\n\n- Non-ASCII character in the docstring (it reads as \"Birkhoff[a-with-circumflex][empty-square-box][empty-square-box]von Neumann\" on my system)\n\n- There's not a lot of point in adding functions when there's no obvious way of calling them from the command line. Either this should be imported in an all.py somewhere, or (much preferably) there should be a method of one of the matrix classes that calls it.",
    "created_at": "2010-05-17T10:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63281",
    "user": "davidloeffler"
}
```

Needs work, I'm afraid.

- Firstly, there are no checks on the input type. It will happily accept non-doubly-stochastic matrices, and return garbage; and it seems to silently replace real numbers with rational approximations to them, which is frankly rather weird. The docstring should state clearly what base rings are allowed (integers? rationals? reals?) and there should be a check to make sure that the input matrix really is a doubly stochastic matrix over one of these base rings.

- The doctests won't work without an optional spkg, so they should be flagged as such.

- Non-ASCII character in the docstring (it reads as "Birkhoff[a-with-circumflex][empty-square-box][empty-square-box]von Neumann" on my system)

- There's not a lot of point in adding functions when there's no obvious way of calling them from the command line. Either this should be imported in an all.py somewhere, or (much preferably) there should be a method of one of the matrix classes that calls it.



---

archive/issue_comments_063282.json:
```json
{
    "body": "Replying to [comment:7 davidloeffler]:\n> and it seems to silently replace real numbers with rational approximations to them, which is frankly rather weird. \n\nSorry, that was a mistake in my test script, not in your code. But I still think that the code should do some sanity checks on its input.",
    "created_at": "2010-05-17T11:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63282",
    "user": "davidloeffler"
}
```

Replying to [comment:7 davidloeffler]:
> and it seems to silently replace real numbers with rational approximations to them, which is frankly rather weird. 

Sorry, that was a mistake in my test script, not in your code. But I still think that the code should do some sanity checks on its input.



---

archive/issue_comments_063283.json:
```json
{
    "body": "Hello !!\n\nThis patch needed to be updated anyway, as it was veeeeery old and many things changed since. I will gladly add a chechking that the matrix is indeed bistochastic if you think it necessary (though I like to think of functions doing just what they are meant to, and not spend too much time checking the user is not doing anything wrong). It is not very long anyway :-)\n\n* Considering how the algorithm works, it does not really care about the base ring. Anyone will work (well, as long as it is completely ordered !), so Reals, Integers, Rationals are all ok. How would you like this to be mentionned ? I never use these types, and I do not know at all how it is usually done.\n\n* The doctests *needed* an optional package. With #8166, they don't anymore, and I will update the patch in consequence :-)\n\n* Sorry about the non-ASCII character !!\n\n* Another place where I wouldn't know how to do otherwise. There are some graph functions which are not method of the Graph object, just because they are too specific to be, and the users can find out about them by reading the reference manual, or the correct module. If it is not the custom in this part of Sage, where would you like to see it ? I have to admit I have no clue... :-)\n\nThank you for your help !!\n\nNathann",
    "created_at": "2010-05-17T17:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63283",
    "user": "ncohen"
}
```

Hello !!

This patch needed to be updated anyway, as it was veeeeery old and many things changed since. I will gladly add a chechking that the matrix is indeed bistochastic if you think it necessary (though I like to think of functions doing just what they are meant to, and not spend too much time checking the user is not doing anything wrong). It is not very long anyway :-)

* Considering how the algorithm works, it does not really care about the base ring. Anyone will work (well, as long as it is completely ordered !), so Reals, Integers, Rationals are all ok. How would you like this to be mentionned ? I never use these types, and I do not know at all how it is usually done.

* The doctests *needed* an optional package. With #8166, they don't anymore, and I will update the patch in consequence :-)

* Sorry about the non-ASCII character !!

* Another place where I wouldn't know how to do otherwise. There are some graph functions which are not method of the Graph object, just because they are too specific to be, and the users can find out about them by reading the reference manual, or the correct module. If it is not the custom in this part of Sage, where would you like to see it ? I have to admit I have no clue... :-)

Thank you for your help !!

Nathann



---

archive/issue_comments_063284.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-05-17T17:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63284",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_063285.json:
```json
{
    "body": "I think the standard practice is to have an optional argument \"check\", which defaults to True but can be set to False if you know your input is valid and you don't want to waste time checking.\n\nRather than having an explicit list of allowable base rings, I suggest checking that the base ring has a canonical coercion map to RR.\n\nMaybe you could put in a method under (perhaps) sage.matrix.matrix2 that calls this, and cross-reference between the two docstrings.\n\nDavid",
    "created_at": "2010-05-17T18:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63285",
    "user": "davidloeffler"
}
```

I think the standard practice is to have an optional argument "check", which defaults to True but can be set to False if you know your input is valid and you don't want to waste time checking.

Rather than having an explicit list of allowable base rings, I suggest checking that the base ring has a canonical coercion map to RR.

Maybe you could put in a method under (perhaps) sage.matrix.matrix2 that calls this, and cross-reference between the two docstrings.

David



---

archive/issue_comments_063286.json:
```json
{
    "body": "Well, it took me some time but.... Would this patch suit your taste ? :-)\n\nNathann",
    "created_at": "2010-05-17T20:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63286",
    "user": "ncohen"
}
```

Well, it took me some time but.... Would this patch suit your taste ? :-)

Nathann



---

archive/issue_comments_063287.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-17T20:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63287",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063288.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-17T20:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63288",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_063289.json:
```json
{
    "body": "Attachment\n\napply over previous patch",
    "created_at": "2010-05-18T13:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63289",
    "user": "davidloeffler"
}
```

Attachment

apply over previous patch



---

archive/issue_comments_063290.json:
```json
{
    "body": "Excellent! I only have one minor suggestion: I think it's also worth checking that the matrix has nonnegative entries. I've added a reviewer patch that makes this change, and also adds a couple more doctests. I'm happy with the code now, modulo these changes; so if you (or anyone else who happens to be reading this) could double-check my second patch, then we can call this a positive review.",
    "created_at": "2010-05-18T13:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63290",
    "user": "davidloeffler"
}
```

Excellent! I only have one minor suggestion: I think it's also worth checking that the matrix has nonnegative entries. I've added a reviewer patch that makes this change, and also adds a couple more doctests. I'm happy with the code now, modulo these changes; so if you (or anyone else who happens to be reading this) could double-check my second patch, then we can call this a positive review.



---

archive/issue_comments_063291.json:
```json
{
    "body": "Thank you for your corrections ! It introduces no docstring error, is nicely applied, etc... Positive review to your changes, and hence to this whole ticket. It still depends on two other tickets waiting for review, though  (#8364 and #8166) :-)\n\nNathann",
    "created_at": "2010-05-18T21:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63291",
    "user": "ncohen"
}
```

Thank you for your corrections ! It introduces no docstring error, is nicely applied, etc... Positive review to your changes, and hence to this whole ticket. It still depends on two other tickets waiting for review, though  (#8364 and #8166) :-)

Nathann



---

archive/issue_comments_063292.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T21:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63292",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063293.json:
```json
{
    "body": "(if you have a few seconds for them, by the way ^^; ... they are very simple and require absolutely no knowledge of graph theory -- #8364 just adds arguments to graph functions that are immediately forwarded to a sub-function, and #8166 merges two functions which were doing the same thing in different ways ) :-)\n\nNathann",
    "created_at": "2010-05-18T21:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63293",
    "user": "ncohen"
}
```

(if you have a few seconds for them, by the way ^^; ... they are very simple and require absolutely no knowledge of graph theory -- #8364 just adds arguments to graph functions that are immediately forwarded to a sub-function, and #8166 merges two functions which were doing the same thing in different ways ) :-)

Nathann



---

archive/issue_comments_063294.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63294",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_063295.json:
```json
{
    "body": "Some of doctests had to be marked as optional as they required a linear programming solver.",
    "created_at": "2010-06-05T22:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63295",
    "user": "mhansen"
}
```

Some of doctests had to be marked as optional as they required a linear programming solver.



---

archive/issue_comments_063296.json:
```json
{
    "body": "I somehow missed the dependence on #8166.  I've removed the optional markings from the doctests in this patch.",
    "created_at": "2010-06-06T00:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7492#issuecomment-63296",
    "user": "mhansen"
}
```

I somehow missed the dependence on #8166.  I've removed the optional markings from the doctests in this patch.
