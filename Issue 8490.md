# Issue 8490: Bad behavior of is_square_free for Words

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-03-10 16:38:46

Assignee: vdelecroix

CC:  sage-combinat

Keywords: word

The method is_square_free of sage.combinat.words.word.Word returns the wrong value in special case (including squares !)


```
sage: Word("aa").is_square_free()  # the most funny
True
sage: Word("baa").is_square_free()
True
sage: Word("cbaa").is_square_free()
True
sage: Word("dcbaa").is_square_free()
True
```



---

Comment by vdelecroix created at 2010-03-10 16:46:58

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-03-10 17:16:25

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-10 17:16:25

Looks good to me.


---

Comment by vdelecroix created at 2010-03-10 17:24:34

Oups, intersection with #8429 which refactors the code of sage.combinat.words.

I post soon a new patch that apply only after #8429 and I think it's better.


---

Comment by vdelecroix created at 2010-03-10 17:24:34

Changing status from positive_review to needs_work.


---

Comment by vdelecroix created at 2010-03-10 17:40:25

another one-line correction that applies after #8429


---

Attachment

another one-line correction that applies after #8429


---

Attachment

Apply only this


---

Attachment

The same bug was occuring with `is_cube_free` :


```
sage: Word('111').is_cube_free()
True
sage: Word('2111').is_cube_free()
True
sage: Word('32111').is_cube_free()
True
```


I just applied a patch which fixes this problem. I changed some doctests of both `is_square_free` and `is_cube_free`. I also removed a useless slice in the code of both functions and this gives good improvements in timings :

BEFORE:


```
sage: t = words.ThueMorseWord()
sage: %timeit t[:100].is_cube_free()
5 loops, best of 3: 3.13 s per loop
```


AFTER:


```
sage: t = words.ThueMorseWord()
sage: %timeit t[:100].is_cube_free()
5 loops, best of 3: 1.18 s per loop
```



---

Comment by slabbe created at 2010-04-28 10:18:27

Applies over the precedent patch


---

Attachment


---

Comment by slabbe created at 2010-04-28 10:21:34

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-05-09 17:09:17

Hello !! This patch is finem except for a small unimportant thing which bothered me :


```
for end in xrange(start+3, L+1, 3): 
```


Why go up to L+1 when the last letter is L-1 ? The algorithm is still correct as 


```
Word("abc")[:50000]
```


raises no exception, but as there is no reason to.... So I give a positive review to the patches above, and trac_8490_review-ncohen.patch is left to be reviewed by anyone other than me (quoting Minh) :-)

Thank you for this patch !!

Nathann


---

Comment by ncohen created at 2010-05-09 17:10:26

The patches are to be applied in this order :

  * trac_8490-square_free-vd.patch
  * trac_8490_review-sl.patch
  * trac_8490_review-ncohen.patch

Nathann


---

Comment by slabbe created at 2010-05-13 14:03:24

Replying to [comment:7 ncohen]:
> Hello !! This patch is finem except for a small unimportant thing which bothered me :
> 
> {{{
> for end in xrange(start+3, L+1, 3): 
> }}}
> 
> Why go up to L+1 when the last letter is L-1 ?

First, xrange returns a left-closed and right-open interval. Hence, one needs to write something like `xrange(0,L+1)` if one wants to go up to `L` :


```
sage: list(xrange(0,5))
[0, 1, 2, 3, 4]
```


Second, the variable `end` is not used to get a specific item in self but for slicing self. Hence, if one wants to consider all the slicing possibilities, the variable `end` must take the last possible value `L`:


```
sage: list(xrange(0,5)) [2:5]   #is good
[2, 3, 4]
sage: list(xrange(0,5)) [2:4]   #forgets the last letter
[2, 3]
```


Hence, your patch is strange in the sense that doctests should not pass!

> The algorithm is still correct as 
> 
> {{{
> Word("abc")[:50000]
> }}}
> 
> raises no exception, but as there is no reason to.... 

We made the choice of following the Python behavior for slices that goes too far:


```
sage: L = range(10)
sage: L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sage: L[:100]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


Sébastien


---

Comment by slabbe created at 2010-05-13 14:09:56

Replying to [comment:8 ncohen]:
> The patches are to be applied in this order :
> 
>   * trac_8490-square_free-vd.patch
>   * trac_8490_review-sl.patch
>   * trac_8490_review-ncohen.patch
> 
> Nathann

The patch `trac_8490_review-ncohen.patch` reintroduce the same bug as the current ticket is trying to solve. Hence, I think the patches are to be reviewed in this order again :

 * trac_8490-square_free-vd.patch
 * trac_8490_review-sl.patch

Sébastien


---

Comment by ncohen created at 2010-05-13 14:52:05

Perfectly right !! sorryyyyyyyyyyy !!! :-)

Nathann


---

Comment by ncohen created at 2010-05-16 17:01:10

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-05-16 17:01:10

Well, then short of this, which was my mistake, I noticed nothing wrong with these two patches ! :-)

Nathann


---

Comment by mhansen created at 2010-06-05 22:30:25

Resolution: fixed
