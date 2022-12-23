# Issue 5537: [with patch, not ready for review] bug in __cmp__ in permgroup_element.pyx

archive/issues_005537.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  robertwb\n\nFrom [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/5dcc22b42a7227d4):\n\n```\nsage: h = PermutationGroupElement('(1,3,2)') \nsage: k = PermutationGroupElement('(1,2,3),(4,5)') \nsage: h\n(1,3,2)\nsage: k^2\n(1,3,2)\nsage: k^2 == h, h == k^2 \n(False, True)\n```\n\nClearly these comparisons should return the same thing. robertwb pointed out in the thread that, especially since the parents are not explicitly defined here, they should both return True.\n\nI'll post a patch, but I don't know much about this code, and I don't want to slow things down too much.  If anyone else has a faster way, please produce a new patch.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5537\n\n",
    "created_at": "2009-03-16T23:09:12Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "[with patch, not ready for review] bug in __cmp__ in permgroup_element.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5537",
    "user": "jhpalmieri"
}
```
Assignee: joyner

CC:  robertwb

From [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/5dcc22b42a7227d4):

```
sage: h = PermutationGroupElement('(1,3,2)') 
sage: k = PermutationGroupElement('(1,2,3),(4,5)') 
sage: h
(1,3,2)
sage: k^2
(1,3,2)
sage: k^2 == h, h == k^2 
(False, True)
```

Clearly these comparisons should return the same thing. robertwb pointed out in the thread that, especially since the parents are not explicitly defined here, they should both return True.

I'll post a patch, but I don't know much about this code, and I don't want to slow things down too much.  If anyone else has a faster way, please produce a new patch.


Issue created by migration from https://trac.sagemath.org/ticket/5537





---

archive/issue_comments_043050.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-16T23:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43050",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_043051.json:
```json
{
    "body": "This will fix the error, but doesn't fix the underlying issue that the coercions should happen *before* cmp gets called. Also, I anticipate it will be a massive speed regression--if the sizes are inequal then the longer one should simply be checked to make sure it fixes the larger elements. \n\nI'll post a patch.",
    "created_at": "2009-03-17T18:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43051",
    "user": "robertwb"
}
```

This will fix the error, but doesn't fix the underlying issue that the coercions should happen *before* cmp gets called. Also, I anticipate it will be a massive speed regression--if the sizes are inequal then the longer one should simply be checked to make sure it fixes the larger elements. 

I'll post a patch.



---

archive/issue_comments_043052.json:
```json
{
    "body": "Changing assignee from joyner to robertwb.",
    "created_at": "2009-03-17T18:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43052",
    "user": "robertwb"
}
```

Changing assignee from joyner to robertwb.



---

archive/issue_comments_043053.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n\nI spent some time with this earlier today, and had the same concerns about speed.  I grabbed a random element of S_20 and of S_10 and then compared them repeatedly in a loop.  One trip through the loop took about 0.8 seconds (including starting up Sage).  Then for 2000 iterations the speed was 7.555s in 3.4 and 7.937s with the patch.  Other runs with different number of iterations also indicated about 5-10% longer runtimes.  I was just about to do more careful timings with timeit, but won't bother pending a new patch.\n\nI also added the following to the sage-devel thread, being current behavior under 3.4.  A variant should maybe be added to the docstring.\n\n\n```\nsage: G=SymmetricGroup(8)\nsage: H=SymmetricGroup(2)\nsage: a=H('(1,2)')\nsage: b=G('(1,2)(3,4)')\nsage: a==b\nTrue\n```\n",
    "created_at": "2009-03-17T22:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43053",
    "user": "rbeezer"
}
```

Replying to [comment:2 robertwb]:

I spent some time with this earlier today, and had the same concerns about speed.  I grabbed a random element of S_20 and of S_10 and then compared them repeatedly in a loop.  One trip through the loop took about 0.8 seconds (including starting up Sage).  Then for 2000 iterations the speed was 7.555s in 3.4 and 7.937s with the patch.  Other runs with different number of iterations also indicated about 5-10% longer runtimes.  I was just about to do more careful timings with timeit, but won't bother pending a new patch.

I also added the following to the sage-devel thread, being current behavior under 3.4.  A variant should maybe be added to the docstring.


```
sage: G=SymmetricGroup(8)
sage: H=SymmetricGroup(2)
sage: a=H('(1,2)')
sage: b=G('(1,2)(3,4)')
sage: a==b
True
```




---

archive/issue_comments_043054.json:
```json
{
    "body": "There is no such thing as \"negative review\".\n\nCheers,\n\nMichael",
    "created_at": "2009-03-18T00:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43054",
    "user": "mabshoff"
}
```

There is no such thing as "negative review".

Cheers,

Michael



---

archive/issue_comments_043055.json:
```json
{
    "body": "Attachment\n\n\n```\nsage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()\nsage: time v = [a == b for _ in xrange(2000)]\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: timeit(\"a==b\")\n625 loops, best of 3: 240 ns per loop\n```\n\n\nvs. the old code\n\n\n```\nsage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()\nsage: timeit(\"a==b\")\n625 loops, best of 3: 3.19 \u00b5s per loop\n```\n",
    "created_at": "2009-03-18T05:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43055",
    "user": "robertwb"
}
```

Attachment


```
sage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()
sage: time v = [a == b for _ in xrange(2000)]
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: timeit("a==b")
625 loops, best of 3: 240 ns per loop
```


vs. the old code


```
sage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()
sage: timeit("a==b")
625 loops, best of 3: 3.19 µs per loop
```




---

archive/issue_comments_043056.json:
```json
{
    "body": "I don't like having all of the < and > tests without documentation. I think in the old code, < and > didn't really mean anything, whereas now they do.  I also don't like the examples that were in the old code: things like `G.gen(0) < G.gen(1)`.  This is not very helpful to the user unless they first evaluate G.gen(0) and G.gen(1).  So I've changed the docstring a bit in a referee's patch.\n\nAlso, a very minor point, but I think that in\n\n```\n    TESTS:: \n\t         \n    Verify that we fixed bug #5537:: \n```\n\nthere should be only one colon after TESTS.  This isn't really important because right now, methods starting with an underscore don't appear in the reference manual, but I hope that some day they might...  I changed this, too.\n\nMeanwhile, the patch fixes the problem in the summary and also the problem that rbeezer reports.  All tests pass.  If my patch is acceptable, positive review.",
    "created_at": "2009-03-18T06:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43056",
    "user": "jhpalmieri"
}
```

I don't like having all of the < and > tests without documentation. I think in the old code, < and > didn't really mean anything, whereas now they do.  I also don't like the examples that were in the old code: things like `G.gen(0) < G.gen(1)`.  This is not very helpful to the user unless they first evaluate G.gen(0) and G.gen(1).  So I've changed the docstring a bit in a referee's patch.

Also, a very minor point, but I think that in

```
    TESTS:: 
	         
    Verify that we fixed bug #5537:: 
```

there should be only one colon after TESTS.  This isn't really important because right now, methods starting with an underscore don't appear in the reference manual, but I hope that some day they might...  I changed this, too.

Meanwhile, the patch fixes the problem in the summary and also the problem that rbeezer reports.  All tests pass.  If my patch is acceptable, positive review.



---

archive/issue_comments_043057.json:
```json
{
    "body": "apply 5537-perm-cmp.patch and then this one",
    "created_at": "2009-03-18T06:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43057",
    "user": "jhpalmieri"
}
```

apply 5537-perm-cmp.patch and then this one



---

archive/issue_comments_043058.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:5 robertwb]:\n\nHi Robert,\n\nMuch improved.  Correct and faster.  Passed all tests in sage/groups/perm_gps.\n\nDo you think the code for the second loop checking the fixed elements of the longer permutation would be more readable if it mimicked the first loop?  In other words, view the plain i's in the comparison as self.perm[i] and then have everything else match up exactly with the first loop:\n\n\n```\nfor i from self.n <= i < right.n:\n    if i < right.perm[i]:\n        return -swap\n    elif i > right.perm[i]:\n        return swap\n```\n",
    "created_at": "2009-03-18T06:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43058",
    "user": "rbeezer"
}
```

Attachment

Replying to [comment:5 robertwb]:

Hi Robert,

Much improved.  Correct and faster.  Passed all tests in sage/groups/perm_gps.

Do you think the code for the second loop checking the fixed elements of the longer permutation would be more readable if it mimicked the first loop?  In other words, view the plain i's in the comparison as self.perm[i] and then have everything else match up exactly with the first loop:


```
for i from self.n <= i < right.n:
    if i < right.perm[i]:
        return -swap
    elif i > right.perm[i]:
        return swap
```




---

archive/issue_comments_043059.json:
```json
{
    "body": "Replying to [comment:6 jhpalmieri]:\n\nJohn,\n\nI like the clear explanation of the ordering on permutations.\n\nDo the examples with < and > (or != and == in the referee patch) really need to come from the generators of some group?  This just seems to make it harder for someone to decipher.  Would it be clearer to just make two or three elements using `PermutationGroupElement()`, possibly with different \"sizes\", and then put them through some of the possible comparisons to exercise as much of the new code as possible?",
    "created_at": "2009-03-18T06:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43059",
    "user": "rbeezer"
}
```

Replying to [comment:6 jhpalmieri]:

John,

I like the clear explanation of the ordering on permutations.

Do the examples with < and > (or != and == in the referee patch) really need to come from the generators of some group?  This just seems to make it harder for someone to decipher.  Would it be clearer to just make two or three elements using `PermutationGroupElement()`, possibly with different "sizes", and then put them through some of the possible comparisons to exercise as much of the new code as possible?



---

archive/issue_comments_043060.json:
```json
{
    "body": "I'm not sure about the second colon on tests, but I thought that was needed for the ReST verbatim blocks. Other than that (which, again, I'm uncertain on) I approve of the referee patch--the explanation of the ordering is especially good. \n\nThe first examples with the generators were there originally. I don't think they're the best, but I figured we'd keep them at least. As for whether or not it make sense to order these things, my choice of ordering was solely to be consistent with what was already there. There is another discussion ongoing at the moment about whether or not it makes sense to try and order everything, or just raise errors for non-obviously comparable things (in the case of permutations, there isn't an obvious ordering to choose), so I'm not sure its worth investing too much time into this until the dust settles there.",
    "created_at": "2009-03-18T07:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43060",
    "user": "robertwb"
}
```

I'm not sure about the second colon on tests, but I thought that was needed for the ReST verbatim blocks. Other than that (which, again, I'm uncertain on) I approve of the referee patch--the explanation of the ordering is especially good. 

The first examples with the generators were there originally. I don't think they're the best, but I figured we'd keep them at least. As for whether or not it make sense to order these things, my choice of ordering was solely to be consistent with what was already there. There is another discussion ongoing at the moment about whether or not it makes sense to try and order everything, or just raise errors for non-obviously comparable things (in the case of permutations, there isn't an obvious ordering to choose), so I'm not sure its worth investing too much time into this until the dust settles there.



---

archive/issue_comments_043061.json:
```json
{
    "body": "Replying to [comment:9 robertwb]:\n> I'm not sure about the second colon on tests, but I thought that was needed for the ReST verbatim blocks.\n\nAfter a double colon, ReST expects some indented text, and in fact if you use \n\n```\nTESTS::\n\nanother sentence::\n```\n\nin a docstring for a function not starting with an underscore, you get a warning about that.  If you only use one colon after TESTS, the double colon at the end of the next part still signifies an upcoming verbatim block.\n\nAs far as the original examples, I don't think they're very illuminating.  I don't think it's that important, though, because it's not a docstring which appears in the reference manual or in a method people will be explicitly calling very much (and hence they won't be asking for interactive help about it, either).",
    "created_at": "2009-03-18T16:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43061",
    "user": "jhpalmieri"
}
```

Replying to [comment:9 robertwb]:
> I'm not sure about the second colon on tests, but I thought that was needed for the ReST verbatim blocks.

After a double colon, ReST expects some indented text, and in fact if you use 

```
TESTS::

another sentence::
```

in a docstring for a function not starting with an underscore, you get a warning about that.  If you only use one colon after TESTS, the double colon at the end of the next part still signifies an upcoming verbatim block.

As far as the original examples, I don't think they're very illuminating.  I don't think it's that important, though, because it's not a docstring which appears in the reference manual or in a method people will be explicitly calling very much (and hence they won't be asking for interactive help about it, either).



---

archive/issue_comments_043062.json:
```json
{
    "body": "RE ::, good point. I agree about the doctests, the most important point is that they get tested (so comparison of permutation group elements doesn't silently break one of these releases).",
    "created_at": "2009-03-18T19:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43062",
    "user": "robertwb"
}
```

RE ::, good point. I agree about the doctests, the most important point is that they get tested (so comparison of permutation group elements doesn't silently break one of these releases).



---

archive/issue_comments_043063.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n\n```\n> {{{\n> sage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()\n> sage: time v = [a == b for _ in xrange(2000)]\n> CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\n> Wall time: 0.00 s\n> sage: timeit(\"a==b\")\n> 625 loops, best of 3: 240 ns per loop\n> }}}\n> \n> vs. the old code\n> \n> {{{\n> sage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()\n> sage: timeit(\"a==b\")\n> 625 loops, best of 3: 3.19 \u00b5s per loop\n> }}}\n```\n\nHi Robert. Is it possible for you to give some system info for those particular timing statistics? I think it's good to include both the statistics and some accompanying system/architecture info in a release tour.",
    "created_at": "2009-03-19T02:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43063",
    "user": "mvngu"
}
```

Replying to [comment:5 robertwb]:

```
> {{{
> sage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()
> sage: time v = [a == b for _ in xrange(2000)]
> CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
> Wall time: 0.00 s
> sage: timeit("a==b")
> 625 loops, best of 3: 240 ns per loop
> }}}
> 
> vs. the old code
> 
> {{{
> sage: a = SymmetricGroup(20).random_element(); b = SymmetricGroup(10).random_element()
> sage: timeit("a==b")
> 625 loops, best of 3: 3.19 µs per loop
> }}}
```

Hi Robert. Is it possible for you to give some system info for those particular timing statistics? I think it's good to include both the statistics and some accompanying system/architecture info in a release tour.



---

archive/issue_comments_043064.json:
```json
{
    "body": "Replying to [comment:9 robertwb]:\n\nRobert,\n\nIf you were agreeable to the cosmetic changes I suggested above for the last bit of the code, then I'd roll up all the patches (your's, John's and mine) into one and John could finish off a review.\n\nRob",
    "created_at": "2009-03-19T02:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43064",
    "user": "rbeezer"
}
```

Replying to [comment:9 robertwb]:

Robert,

If you were agreeable to the cosmetic changes I suggested above for the last bit of the code, then I'd roll up all the patches (your's, John's and mine) into one and John could finish off a review.

Rob



---

archive/issue_comments_043065.json:
```json
{
    "body": "Yes, I'm fine with those changes. As for what I ran timings on, OS X 10.4 intel core 2 duo 2.33 Ghz.",
    "created_at": "2009-03-19T02:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43065",
    "user": "robertwb"
}
```

Yes, I'm fine with those changes. As for what I ran timings on, OS X 10.4 intel core 2 duo 2.33 Ghz.



---

archive/issue_comments_043066.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:14 robertwb]:\n\nOK, final patch (trac_5537_perm_compare) has Robert's \"perm-cmp\" patch, John's \"referee\" patch, and my code changes listed above all in one.  So this should be the only file Michael Abshoff will have to deal with.\n\nI think the ball is in your court now, John.\n\nRob",
    "created_at": "2009-03-19T04:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43066",
    "user": "rbeezer"
}
```

Attachment

Replying to [comment:14 robertwb]:

OK, final patch (trac_5537_perm_compare) has Robert's "perm-cmp" patch, John's "referee" patch, and my code changes listed above all in one.  So this should be the only file Michael Abshoff will have to deal with.

I think the ball is in your court now, John.

Rob



---

archive/issue_comments_043067.json:
```json
{
    "body": "Looks good to me.  Positive review.",
    "created_at": "2009-03-19T18:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43067",
    "user": "jhpalmieri"
}
```

Looks good to me.  Positive review.



---

archive/issue_comments_043068.json:
```json
{
    "body": "Merged trac_5537_perm_compare.patch in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T22:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43068",
    "user": "mabshoff"
}
```

Merged trac_5537_perm_compare.patch in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043069.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T22:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5537#issuecomment-43069",
    "user": "mabshoff"
}
```

Resolution: fixed
