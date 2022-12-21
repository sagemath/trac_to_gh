# Issue 5537: [with patch, not ready for review] bug in __cmp__ in permgroup_element.pyx

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-16 23:09:12

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



---

Attachment


---

Comment by robertwb created at 2009-03-17 18:47:58

This will fix the error, but doesn't fix the underlying issue that the coercions should happen *before* cmp gets called. Also, I anticipate it will be a massive speed regression--if the sizes are inequal then the longer one should simply be checked to make sure it fixes the larger elements. 

I'll post a patch.


---

Comment by robertwb created at 2009-03-17 18:47:58

Changing assignee from joyner to robertwb.


---

Comment by rbeezer created at 2009-03-17 22:58:43

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

Comment by mabshoff created at 2009-03-18 00:03:00

There is no such thing as "negative review".

Cheers,

Michael


---

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

Comment by jhpalmieri created at 2009-03-18 06:23:22

I don't like having all of the < and > tests without documentation. I think in the old code, < and > didn't really mean anything, whereas now they do.  I also don't like the examples that were in the old code: things like `G.gen(0) < G.gen(1)`.  This is not very helpful to the user unless they first evaluate G.gen(0) and G.gen(1).  So I've changed the docstring a bit in a referee's patch.

Also, a very minor point, but I think that in

```
    TESTS:: 
	         
    Verify that we fixed bug #5537:: 
```

there should be only one colon after TESTS.  This isn't really important because right now, methods starting with an underscore don't appear in the reference manual, but I hope that some day they might...  I changed this, too.

Meanwhile, the patch fixes the problem in the summary and also the problem that rbeezer reports.  All tests pass.  If my patch is acceptable, positive review.


---

Comment by jhpalmieri created at 2009-03-18 06:24:01

apply 5537-perm-cmp.patch and then this one


---

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

Comment by rbeezer created at 2009-03-18 06:49:51

Replying to [comment:6 jhpalmieri]:

John,

I like the clear explanation of the ordering on permutations.

Do the examples with < and > (or != and == in the referee patch) really need to come from the generators of some group?  This just seems to make it harder for someone to decipher.  Would it be clearer to just make two or three elements using `PermutationGroupElement()`, possibly with different "sizes", and then put them through some of the possible comparisons to exercise as much of the new code as possible?


---

Comment by robertwb created at 2009-03-18 07:15:47

I'm not sure about the second colon on tests, but I thought that was needed for the ReST verbatim blocks. Other than that (which, again, I'm uncertain on) I approve of the referee patch--the explanation of the ordering is especially good. 

The first examples with the generators were there originally. I don't think they're the best, but I figured we'd keep them at least. As for whether or not it make sense to order these things, my choice of ordering was solely to be consistent with what was already there. There is another discussion ongoing at the moment about whether or not it makes sense to try and order everything, or just raise errors for non-obviously comparable things (in the case of permutations, there isn't an obvious ordering to choose), so I'm not sure its worth investing too much time into this until the dust settles there.


---

Comment by jhpalmieri created at 2009-03-18 16:34:19

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

Comment by robertwb created at 2009-03-18 19:09:38

RE ::, good point. I agree about the doctests, the most important point is that they get tested (so comparison of permutation group elements doesn't silently break one of these releases).


---

Comment by mvngu created at 2009-03-19 02:05:34

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

Comment by rbeezer created at 2009-03-19 02:31:24

Replying to [comment:9 robertwb]:

Robert,

If you were agreeable to the cosmetic changes I suggested above for the last bit of the code, then I'd roll up all the patches (your's, John's and mine) into one and John could finish off a review.

Rob


---

Comment by robertwb created at 2009-03-19 02:54:54

Yes, I'm fine with those changes. As for what I ran timings on, OS X 10.4 intel core 2 duo 2.33 Ghz.


---

Attachment

Replying to [comment:14 robertwb]:

OK, final patch (trac_5537_perm_compare) has Robert's "perm-cmp" patch, John's "referee" patch, and my code changes listed above all in one.  So this should be the only file Michael Abshoff will have to deal with.

I think the ball is in your court now, John.

Rob


---

Comment by jhpalmieri created at 2009-03-19 18:16:22

Looks good to me.  Positive review.


---

Comment by mabshoff created at 2009-03-23 22:13:44

Merged trac_5537_perm_compare.patch in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 22:13:44

Resolution: fixed
