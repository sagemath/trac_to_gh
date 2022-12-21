# Issue 8276: The one of MatrixSpace can be changed !

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-02-15 20:49:35

Assignee: hivert

CC:  mraum

Keywords: One mutable.


```
sage: A = MatrixSpace(ZZ, 3)
sage: A.one()
[1 0 0]
[0 1 0]
[0 0 1]
sage: A.one()[1,2] = 1
sage: A.one()
[1 0 0]
[0 1 1]
[0 0 1]
```

Indeed it is mutable an cached !


---

Comment by hivert created at 2010-02-16 23:35:02

Changing status from new to needs_work.


---

Comment by hivert created at 2010-02-16 23:35:02

Correcting MatrixSpace is easy, however there are a lot of places in sage where people create a matrix from the one or zero and modify it after that. I nearly corrected all these occurences. However, I'm stuck with those three files which are very complicated and depend one of each other:

```
    sage/modular/quatalg/brandt.py
    sage/algebras/quatalg/quaternion_algebra.py
    sage/schemes/elliptic_curves/heegner.py
```

There are a lot of error but I can't find where it's coming from. I really
could use the help of a specialist. 

Apply the patch in the following order:

```
    trac_8276-MatrixSpace_one-fh.patch
    trac_8276-fix_sagelib-fh.patch
```

Thanks for any suggestion.


---

Attachment


---

Comment by hivert created at 2010-02-16 23:56:33

I finally manage to get those !!! It should be ready for review. Apply

```
    trac_8276-MatrixSpace_one-fh.patch
    trac_8276-fix_sagelib-fh.2.patch
```


Florent


---

Comment by hivert created at 2010-02-16 23:56:33

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-02-17 10:43:13

I just added a third patch which fixes a non working optimization when creating the zero matrix from `MS(0)` or `MS()`. They are now nearly as fast as calling `copy(MS.zero_matrix())`.

Apply this patch after the two others.


---

Comment by hivert created at 2010-02-17 11:04:59

Changing component from algebra to linear algebra.


---

Comment by hivert created at 2010-02-17 11:17:14

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-02-17 11:17:14

The last improvement patch breaks something...


---

Attachment


---

Comment by hivert created at 2010-02-17 18:09:25

At last thing should be OK ! Please apply in the following order:

```
trac_8276-MatrixSpace_one-fh.patch
trac_8276-fix_sagelib-fh.patch
trac_8276-fix_zero_matrix_creation-fh.patch
```

Depends on #8294

The first patch makes the matrices immutable, the second one fixes Sage's lib accordingly the thirds patch simplifies and optimizes the creation of the zero matrix.


---

Comment by hivert created at 2010-02-17 18:09:25

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by hivert created at 2010-02-20 13:59:49

Oups ! I just realize I forgot to reupload `trac_8276-fix_zero_matrix_creation-fh.patch` after a last minor change. Many apologies if you started to review ! For info here is the changelog between the two last version of the patch

```
    2.31 `@``@` -85,6 +85,8 `@``@`
    2.32               []
    2.33  +            sage: mat.is_mutable()
    2.34  +            False
    2.35 ++            sage: MM.zero().is_mutable()
    2.36 ++            False
    2.37           """
    2.38  -        try:
    2.39  -            z = self.__zero_matrix
    2.40 `@``@` -98,6 +100,8 `@``@`
    2.41  +        res.set_immutable()
    2.42  +        return res
    2.43  +
    2.44 ++    zero = zero_matrix
    2.45 ++
    2.46       def ngens(self):
    2.47           """
    2.48           Return the number of generators of this matrix space,
```

Again, sorry for any inconvenience.

Florent


---

Comment by hivert created at 2010-02-20 14:06:30

Martin Raum: I understand from #8294 that you intend to review this ticket quickly ! I allowed myself to put you in CC of this ticket ! Please make sure that you have the latest version of `trac_8276-fix_zero_matrix_creation-fh.patch`. I forgot to reupload it after a last change (see my previous message). 

Thanks for your help !


---

Comment by rossk created at 2010-02-20 14:18:51

Applied the following patches (in the order below).


trac_8276-MatrixSpace_one-fh.patch


trac_8276-fix_sagelib-fh.patch


trac_8276-fix_zero_matrix_creation-fh.patch


trac_8294-matrix_2x2_copy_mutability_fix-fh.patch


*Almost* everything seems straightforward and correct but... Seems that MM(0) which has a "mutable == True" property/value should be updatable but the example "MM(0)[1,2] = 3" doesnt update MM(0) (see example below) Is that right?



```
# prepatch responses
sage: sage: MM = MatrixSpace(ZZ, 3,3)
sage: sage: MM(0).is_mutable()
True
sage: sage: MM.zero_matrix().is_mutable()
True
sage: sage: MM(1).is_mutable()
True
sage: sage: MM.identity_matrix().is_mutable()
True
sage: sage: timeit("MM(0)")
625 loops, best of 3: 51.1 µs per loop
sage: sage: timeit("copy(MM.zero_matrix())")
625 loops, best of 3: 19.3 µs per loop
sage: sage: timeit("MM(1)")
625 loops, best of 3: 65 µs per loop
sage: sage: timeit("copy(MM.identity_matrix())")
625 loops, best of 3: 60.7 µs per loop

# postpatch responses
sage: MM = MatrixSpace(ZZ, 3,3)
sage: MM(0).is_mutable()
True
sage: MM.zero_matrix().is_mutable()
False
sage: MM(1).is_mutable()
True
sage: MM.identity_matrix().is_mutable()
False
sage: timeit("MM(0)")
625 loops, best of 3: 35.9 µs per loop
sage: timeit("copy(MM.zero_matrix())")
625 loops, best of 3: 29.3 µs per loop
sage: timeit("MM(1)")
625 loops, best of 3: 46.1 µs per loop
sage: timeit("copy(MM.identity_matrix())")
625 loops, best of 3: 29.9 µs per loop

sage: MM(0)
[0 0 0]
[0 0 0]
[0 0 0]

sage: MM(0)[1,2]=3 

# this behavior is the same before and after patches were applied
# is this right? isnt MM(0) mutable and should be = 3 at row/col=[1,2]? 
sage: MM(0)
[0 0 0]
[0 0 0]
[0 0 0]

sage: MM.zero_matrix()[1,2]=3
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5496)()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.check_mutability (sage/matrix/matrix0.c:3686)()
ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

# a copy is mutable
sage: a=copy(MM.zero_matrix())
sage: a[1,2]=3
sage: a
[0 0 0]
[0 0 3]
[0 0 0]

# here, alias_zero is pointing to same object hence it is also immutable and correctly crashes also
sage: alias_zero = MM.zero_matrix()
sage: alias_zero[1,2]=3
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5496)()
/mnt/usb1/scratch/rossk/sage-4.3.3.alpha1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.check_mutability (sage/matrix/matrix0.c:3686)()
ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

```



---

Comment by rossk created at 2010-02-20 14:21:24

Just saw the "updated patch" reference. Will include replace old patch with new tomorrow and re-test


---

Comment by hivert created at 2010-02-20 14:51:51

Replying to [comment:12 rossk]:
> *Almost* everything seems straightforward and correct but... 

Sure ! What wasn't straightforward was to correctly find all the places which needed to be patched and to distinguish them from those who doesn't.

Note that the speed regression when calling `copy(MM.zero_matrix())` is due to a missing optimization in cached_method which should be added soon.

> Seems that MM(0) which has a "mutable == True" property/value should be updatable but the example "MM(0)[1,2] = 3" doesnt update MM(0) (see example below) Is that right?


```
> sage: MM(0)
> [0 0 0]
> [0 0 0]
> [0 0 0]
> 
> sage: MM(0)[1,2]=3 
> 
> # this behavior is the same before and after patches were applied
> # is this right? isnt MM(0) mutable and should be = 3 at row/col=[1,2]? 
> sage: MM(0)
> [0 0 0]
> [0 0 0]
> [0 0 0]
```

This is perfectly normal. `MM(0)` does not design a particular matrix object. It construct a brand new matrix. So that 

```
sage: MM(0)[1,2]=3
}}} 
Construct a matrix, modify it and forget about the result so that the next call to
`MM(0)` gives you a brand new zero matrix. To achieve what you want you should write
{{{
sage: MM = MatrixSpace(ZZ, 3,3)
sage: mat = MM(0); mat[1,2]=3
sage: mat
[0 0 0]
[0 0 3]
[0 0 0]
}}}

Florent


---

Attachment

First reviewed patch


---

Attachment

Seconded reviewed patch.


---

Comment by rossk created at 2010-02-21 00:20:57

Used the new patches (as well as trac_8294-matrix_2x2_copy_mutability_fix-fh.patch). All were applied and compiled with no errors.

```
The following tests failed:
	sage -t  devel/sage/sage/groups/abelian_gps/dual_abelian_group_element.py # Segfault
	sage -t  devel/sage/sage/matrix/matrix_integer_2x2.pyx # 1 doctests failed
	sage -t  devel/sage/doc/fr/tutorial/programming.rst # Segfault
```

Re-tested each and got the following for the first 2 (but the 3rd one passed).

```
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```

I get this "mysterious error" a number of times and have seen many tickets mention it. Can anyone give any advice about it? Given its not always reproduceable, should it block a positive review if the tickets functionality proves good?


---

Comment by rossk created at 2010-02-21 02:46:03

I just have have a query now that Im looking at the ticket that someone may care to answer.
I appreciate there may be implementation issues that differentiate the different constructs i.e.  M().zero() vs M(0) etc. But from a language point of view (i.e. not considering constructions vs coercions), why are the different matrices below treated differently i.e. why arent they all immutable)? Im just thinking that, for example, M().zero() and M().zero_matrix() and M(0) etc each return a zero matrix that cant be changed (either theres an error if its immutable or the assignment is ignored). So shouldnt they all be immutable? And why is there a variation in the mutability between the zero and identity matrices. (Apologies if there's something obvious I missed)


```
sage: MM(0).is_mutable()
True
sage: MM.zero_matrix().is_mutable()
False
sage: MM.zero().is_mutable()
True

sage: MM(1).is_mutable()
True
sage: MM.identity_matrix().is_mutable()
False
sage: MM.one().is_mutable()
False
```



---

Comment by rossk created at 2010-02-21 02:46:03

Changing keywords from "One mutable." to "One Zero mutable.".


---

Comment by mraum created at 2010-02-21 14:26:40

The reason is the categorie framework. MatrixSpaces are vector spaces, so they implement zero(). In my oppinion this should absolutely coinside with MM(0) since everybody will expect it so do so. Hence, it should be mutable.
one() is implemented seperatedly and is just one = identity_matrix. In my oppinion this is a defect, since according to the framework is normally coincides with MM(1). If MatrixSpaces was a ring it would be exactly this.

Could I hear your oppinion? If nobody is opposed I will set this to positive review tomorrow evening and I will open a follow up which sets one = lambda self : self(1) .


---

Comment by hivert created at 2010-02-21 21:08:39


```
sage: MM.zero().is_mutable()
True
```

Is corrected by my last patch. It should be False

Replying to [comment:17 mraum]:
> The reason is the categorie framework. MatrixSpaces are vector spaces, so they implement zero(). In my oppinion this should absolutely coinside with MM(0) since everybody will expect it so do so. Hence, it should be mutable.

No it isn't. See the comment in the doc of `zero` and `one` in their respective category. It has been discussed on sage-devel that `.zero()` and `.one()` should return an *immutable* matrix. The argument of the category framework applies identically to `zero` (vector space) and one (algebra which come actually from monoid).  

> one() is implemented seperatedly and is just one = identity_matrix. In my oppinion this is a defect, since according to the framework is normally coincides with MM(1). If MatrixSpaces was a ring it would be exactly this.

Note that my last version of the patch also implement 

```
zero = zero_matrix
```


> Could I hear your oppinion? If nobody is opposed I will set this to positive review tomorrow evening and I will open a follow up which sets one = lambda self : self(1) .

My opinion which coincide with William's and Robert Bradshaw is that one and zero should be immutable. It was not discussed whether `MM(0)` and `MM(1)` should returns something coherent. 
please see http://groups.google.com/group/sage-devel/browse_frm/thread/1042edd11b3854b2


---

Attachment

Replacing old review; now with zero=zero_matrix


---

Comment by mraum created at 2010-02-22 11:22:59

Changing status from needs_review to positive_review.


---

Comment by mraum created at 2010-02-22 11:22:59

Ok, I didn't read this thread this way, but yes, you're right, a majority seems to want exactly this behaviour.
The review patches now include also your last change.

I'm personally strongly opposed to this, so I am going to open a brief discussion on sage-devel, just to make sure that this is a general policy towards the categories framework. I hope to read your opinion there, too.

rossk: I guess it's fair to say, that you also contributed to this review, so please expand your name in the review field.


---

Comment by mvngu created at 2010-03-03 14:30:36

Merged in this order:

 1. [trac-8276-MatrixSpace_one-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-MatrixSpace_one-review.patch)
 1. [trac-8276-fix_sagelib-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-fix_sagelib-review.patch)
 1. [trac-8276-fix_zero_matrix_creation-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8276/trac-8276-fix_zero_matrix_creation-review.patch)


---

Comment by mvngu created at 2010-03-03 14:30:36

Resolution: fixed
