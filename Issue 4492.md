# Issue 4492: block_matrix reacts inconsistently with 0

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-11-11 15:17:25

Assignee: tbd

CC:  craigcitro jason davidloeffler

Using ZZ(0) as an element of the list passed to block_matrix appears to be a special case somehow and throws an exception rather than creating the matrix seems reasonable to me.


```
sage: i=MatrixSpace(ZZ,2,2)(1)
sage: i

[1 0]
[0 1]
sage: block_matrix([1,i,1,1])  # this works as I expect

[1 0|1 0]
[0 1|0 1]
[---+---]
[1 0|1 0]
[0 1|0 1]
sage: block_matrix([0,i,1,1])  # this doesn't ... why is 0 special
...
ValueError: Insufficient information to determine dimensions.
```

This feels to me like a hazardous inconsistency.

Perhaps I should also add that I don't really like that it just blithely assumes I want a square matrix (although I did in my actual usage).  Ticket #2429 addresses that issue more wholeheartedly.


---

Comment by jason created at 2008-11-14 06:02:47

Changing assignee from tbd to was.


---

Comment by jason created at 2008-11-14 06:02:47

Changing component from algebra to linear algebra.


---

Comment by sdietzel created at 2010-01-18 05:37:22

So I figured out what is going wrong here. Patch to come shortly.


---

Comment by sdietzel created at 2010-01-18 19:17:12

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-19 04:13:24

I think that in the doctest you give there actually is insufficient information, because you can't deduce the width of the left blocks, so an exception is in my opinion the right thing to do there.

In the example in this ticket, it seems to break because it tries to deduce the block dimensions in a single pass through the cells. In this pass, it only determines the size of column 2 and rows 1 and 2. It might need multiple passes to find all information.


---

Comment by wjp created at 2010-01-19 04:13:24

Changing status from needs_review to needs_work.


---

Attachment

Robert Bradshaw suggested adding an example that explicitly shows zero blocks may be non-square. I added a patch that adds that to the docstring of `block_matrix`.


---

Comment by was created at 2010-01-26 18:38:49

Changing status from needs_work to needs_review.


---

Attachment

apply *only* this patch (don't apply wjp's)


---

Comment by wjp created at 2010-01-26 19:38:13

Changing status from needs_review to needs_work.


---

Comment by wjp created at 2010-01-26 19:38:13

This breaks the following example:

sage: B = Matrix(ZZ,3,2,[1,2,3,4,5,6])
sage: block_matrix([0,1,B,1])

The problem is that it turns the 0 at the top into a 2x2 zero matrix while
it should be a 3x2 zero matrix, but that can only be deduced after processing the ones further on.


---

Comment by wjp created at 2010-01-26 19:41:36

Oops, sorry for the broken formatting. Clean version:


```
sage: B = Matrix(ZZ,3,2,[1,2,3,4,5,6])
sage: block_matrix([0,1,B,1]) 
```



---

Comment by wjp created at 2010-01-29 10:05:53

I tried to write a patch for this, but ran into some trouble with the last doctest:


```
        sage: B = matrix(QQ, 2, 3, range(6))
        sage: block_matrix([~A, B, B, ~A], subdivide=False)
        [-5/12   3/8     0     1     2]
        [  1/4  -1/8     3     4     5]
        [    0     1     2 -5/12   3/8]
        [    3     4     5   1/4  -1/8]
```


In this case there are no real columns as such, and I'm not sure how we should behave if there were an extra row with `'1 0'` below the `'~A B'` and `'B ~A'` rows. Should that give a 3x3 identity matrix and a 3x2 zero matrix, or a 2x2 identity matrix and a 2x2 identity matrix? Maybe undefined behaviour, or an exception?

My current attempt raises an exception for this doctest that the column widths are inconsistent.


---

Comment by wjp created at 2010-01-29 15:15:13

For those interested, my current work-in-progress patch is at

http://www.math.leidenuniv.nl/~wpalenst/sage/sage_WIP_block_matrix.patch


---

Comment by wjp created at 2011-01-11 20:14:47

Further work in progress (replacing the previous patch). This also addresses #2429.

http://www.math.leidenuniv.nl/~wpalenst/sage/block_matrix_2.patch


---

Comment by wjp created at 2011-01-12 01:47:31

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2011-01-12 21:17:39

Changing status from needs_review to needs_work.


---

Comment by aly.deines created at 2011-01-12 21:17:39

The following tests failed:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  devel/sage/sage/matrix/matrix2.pyx # 2 doctests failed
	sage -t  devel/sage/sage/combinat/designs/incidence_structures.py # 1 doctests failed
	sage -t  devel/sage/sage/crypto/lattice.py # 9 doctests failed
	sage -t  devel/sage/sage/combinat/matrices/hadamard_matrix.py # 1 doctests failed
----------------------------------------------------------------------

```



---

Attachment

block_matrix rewrite. Replaces all previous patches.


---

Comment by wjp created at 2011-01-12 21:56:01

Changing status from needs_work to needs_review.


---

Comment by wjp created at 2011-01-12 21:56:01

Oops, sorry about that. New patch up that fixes those.


---

Attachment

Looks real nice.  I've added some edits in a reviewer patch.

I'll run full tests overnight (with reviewer patch), and then will be ready to give this a positive review (subject to acceptance of my reviewer edits).


---

Comment by rbeezer created at 2011-01-13 18:47:15

All tests in `sage/devel` pass with reviewer patch applied.  So I am all clear on a positive review.  Once the reviewer patch gets a review, this can be flipped to "positive review".

Nice contribution - this will be very useful.

Rob


---

Attachment


---

Comment by aly.deines created at 2011-01-13 18:58:24

How should the patches be applied?  If I try either of the last two by themselves, they don't apply.


---

Comment by wjp created at 2011-01-13 19:01:34

The last three, in order:

Apply 4492_block_matrix.patch, trac_4492-block-matrix-reviewer.patch, 4492_typo.patch


---

Comment by wjp created at 2011-01-13 19:09:52

The reviewer patch looks good, and passes all tests for me too. The doctests and documentation it adds are really clarifying. (I did add a very minor patch on top of it fixing two small typos.)


---

Comment by aly.deines created at 2011-01-13 19:54:23

It looks good and all tests pass for me too.


---

Comment by aly.deines created at 2011-01-13 19:54:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-25 08:38:59

This needs to be rebased to sage-4.6.2.alpha1


---

Comment by jdemeyer created at 2011-01-25 08:38:59

Changing status from positive_review to needs_work.


---

Comment by wjp created at 2011-01-25 09:23:10

rebased to 4.6.2.alpha1


---

Attachment


---

Comment by wjp created at 2011-01-25 09:23:47

Changing status from needs_work to needs_review.


---

Comment by wjp created at 2011-01-25 09:26:18

Rebased patch attached. (No actual changes, just the context of one of the hunks had changed.)


---

Attachment

Rebased patches apply fine and Sage builds.

However 3 doctests fail.  These can be traced to #10433 that snuck into 4.6.2.alpha1 while this was in-progress.  ;-)  Specifically one 2x2 block matrix built at line 2366 of `sage/rings/number_field/number_field_ideal.py`

Latest patch rearranges the block matrix construction to meet new requirements for more explicit lists for the block matrix.  I've cc'ed David Loeffler if he wants to check off on just that one change.  Passes all tests now in sage/rings.  All work here is on 4.6.2.alpha1.

Would somebody like to retest the whole package now?


---

Comment by davidloeffler created at 2011-01-26 08:47:18

(The change to number field code looks fine to me.)


---

Comment by jdemeyer created at 2011-01-26 10:18:16

I will test the patches.


---

Comment by wjp created at 2011-01-26 11:25:00

I've also run tests with 4.6.2-alpha2 + this ticket, and all tests passed.


---

Comment by jdemeyer created at 2011-01-26 22:17:00

Yep, tests are okay.


---

Comment by rbeezer created at 2011-01-27 05:35:00

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2011-01-27 05:35:00

David - thanks for the quick check.

Jeroen, Willem - thanks for the testing.

Sounds like the latest patch has been tested and everybody is OK with all of this, so I'm going to switch this back to positive review.


---

Comment by jdemeyer created at 2011-01-27 09:56:32

Resolution: fixed
