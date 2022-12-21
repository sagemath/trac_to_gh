# Issue 4681: General Smith normal form implementation

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2008-12-03 00:01:47

Assignee: davidloeffler

CC:  ncalexan

Keywords: matrix, smith normal form

Smith form is a useful canonical form for matrices over a PID. Sage already has it for ZZ. I've coded up a very basic implementation that should work over any PID Sage knows about (although it is not fast).


---

Comment by davidloeffler created at 2008-12-03 00:05:42

Changing status from new to assigned.


---

Comment by davidloeffler created at 2008-12-03 00:05:42

The above patch is based on sage 3.2.1. It adds the basic algorithm, plus some minor fiddlings needed to get the examples to work :-)


---

Comment by jason created at 2008-12-03 19:28:59

I just glanced at this; could you put in doctests for the additive_order function?


---

Attachment

I've done a new patch (replacing the old one) which includes a doctest; sorry for the omission.


---

Comment by was created at 2008-12-04 22:11:50

THANK YOU!  I've been wanting somebody to do this right (even if slow) forever... and at least two students have tried and failed before, so I'm really glad you did this.


---

Comment by was created at 2008-12-05 07:06:20

I noticed that this docstring is slightly wrong.  The m and y are confused:

```
 	4669	def _smith_augment(x, m): 
 	4670	    r""" For internal use by the smith_form routine. Given scalar x and matrix 
 	4671	    y, construct the block-diagonal matrix [x,0 ; 0, y]. 
```



---

Attachment


---

Comment by davidloeffler created at 2008-12-05 11:40:42

On reflection I realised that my "_smith_augment" function was a waste of space anyway as the same job can be done using the existing "block_sum" method from matrix1.py. I've added a new version of the patch, which replaces the old one (I forgot to tick the replace box in the trac upload page).


---

Comment by was created at 2008-12-07 00:12:49

I read the code, which looks fine.  The doctests pass.  This test passes:

```
for i in range(10):
   print i
   a = random_matrix(ZZ[sqrt(-1)],7)
   d,u,v = a.smith_form()
   assert u*a*v == d
   assert u.det() == 1
   assert v.det() == 1
```


This fails pretty quickly, but it's not the fault of this code:

```
K.<a>=NumberField(x^3-2)
print "h = ", K.class_number()
for i in range(10):
   print i
   a = random_matrix(K,3)
   d,u,v = a.smith_form()
   assert u*a*v == d
   assert u.det() == 1
   assert v.det() == 1
...

Traceback (most recent call last):       d,u,v = a.smith_form()

  File "element.pyx", line 1269, in sage.structure.element.CommutativeRingElement.inverse_mod (sage/structure/element.c:10039)
NotImplementedError
```


It's the fault of other stuff missing in Sage.

Another thing -- in matrices over ZZ there is a smith_form function, and it's inputs, etc., are *not* consistent with the above.  It doesn't have a transformation option - instead it always gives the transformation matrices.  However, it also says to use the function "elementary_divisors" to get the diagonal entries.   I attached a patch that fixes this by making the sage integer matrix snf have the same interface as the generic one. 

The definition of smith_form between your new code and Sage's code (which relies on pari) is inconsistent (see below).  This needs to be somehow resolved.  I haven't done this yet at all.

```
sage: a = matrix(ZZ,3,[1..9]); a

[1 2 3]
[4 5 6]
[7 8 9]
sage: a.smith_form()

([0 0 0]
[0 3 0]
[0 0 1],
 [ 1 -2  1]
[ 0 -1  1]
[ 0  2 -1],
 [ 1  2 -1]
[-2 -1  1]
[ 1  0  0])
sage: a.smith_form(transformation=False)

[0 0 0]
[0 3 0]
[0 0 1]
sage: a = matrix(ZZ[i],3,[1..9]); a

[1 2 3]
[4 5 6]
[7 8 9]
sage: a.smith_form(transformation=False)

[ 1  0  0]
[ 0 -3  0]
[ 0  0  0]
```


To get this into Sage, please:
  * review my matrix_integer_dense patch
  * decide on what to do about the inconsistency between sage/pari/your code.


---

Attachment

Hmm. On reflection, perhaps the way the Sage code was already doing it is the right way: smith_form should always return the transformation matrix, and elementary_divisors should be provided separately.

This seems more logical to me, because one can define analogues of elementary divisors over any Dedekind domain, but the result is a list of ideals rather than of elements and thus there is no analogue of the transformation matrix. PARI/GP has a function that does this over rings of integers of a general number field. Also, even over ZZ where the transformation matrices do make sense there are some fast algorithms for elementary divisors that don't give them.

As for the inconsistency of ordering the results, I've called for a quick straw poll on sage-devel.

The other issue is one of sign. Conventionally elementary divisors are always *nonnegative* integers; one wouldn't want to calculate the invariants of a finitely generated abelian group and be told that it had a direct summand that was cyclic of order -5. But for general PID's there's no canonical choice of sign for the generator of an ideal. I'm sure nobody will actually be all that bothered by this, but I will drop the insistence that U and V have det 1 and replace it with the insistence that the d_i are >= 0, even though this is pretty meaningless.

Incidentally, I just realised the doctests don't pass! I added an is_noetherian method for number field orders, but didn't notice that there is a doctest in sage/rings/ring.pyx that is actually broken by this -- it creates an order, calls is_noetherian() on it and insists that the result should be NotImplementedError. I will fix this.


---

Comment by davidloeffler created at 2008-12-08 16:24:38

New patch, against 3.2.2.alpha0


---

Attachment

(cc'ed to ncalexan as symplectic_basis is his territory)

Nobody's objected violently to the change yet on sage-devel, so the following patch changes SNF over ZZ, to put 1's first and 0's last. (Also, when M is non-square it puts the nonzero entries in the [i,i] diagonal, not on some shifted diagonal ending in the bottom corner like the previous code did -- I found that rather inconvenient.)

As I suggested above, I've changed the call syntax over a general ring to be consistent with the existing code over ZZ, so I got rid of the "transformation=True" argument and added an extra function "elementary_divisors" which returns the diagonal entries of M. This can be overridden later, if anyone feels like implementing a fast algorithm for elementary divisors for more general rings.

I've also fixed up "symplectic_basis" to be consistent with the new "smith_form"; it doesn't explicitly use smith_form, but the conventions for the output are chosen for consistency with smith_form, so I've changed them in tandem. (ncalexan: is this OK with you?)

I didn't actually make it choose ideal representatives that compare as >= 0 -- I decided I couldn't bear to fix such a horrible convention. This means that if R is a general PID, coercing integer matrices from ZZ to R doesn't quite commute with Smith form, but I don't see why one should expect it to.


---

Comment by davidloeffler created at 2008-12-08 18:08:06

fixes broken docstring + handling of empty matrices


---

Attachment


---

Comment by davidloeffler created at 2008-12-08 18:13:10

Just realised that (a) I missed the fact that there is a doctest for symplectic_basis in matrix2.pyx and (b) there is an open ticket #3068 regarding Smith form of empty matrices. I've added a tiny patchlet that fixes both things.


---

Comment by ncalexan created at 2008-12-09 21:25:37

Hi, I can't figure out what patches are supposed to work.

If I apply 4681-smithform-consistent.patch and then 4681-docstringfix.patch, everything works on sage.math but not on my home machine -- there is no inverse_mod for the maximal order elements in question.  Can you clarify?  Do I need some other patches from other tickets?

BTW, I am fine with the changes you made to symplectic_basis.


---

Comment by ncalexan created at 2008-12-09 21:34:32

I see that it requires 4537.  I'll apply that and test again.


---

Comment by ncalexan created at 2008-12-09 21:39:11

Works for me, and the code is fairly straight forward.  It also fixes (and doctests) 3068.  Apply only the final two patches.


---

Attachment

apply after previous two patches


---

Comment by davidloeffler created at 2008-12-09 21:58:16

Actually, after your comments on sage-devel, regarding the lack of doctests over base rings other than number field orders, I have done a third patch adding these. I meant to upload this yesterday but trac was down at the time. It also now raises an error over non-exact base rings, because I tested it with a 2x2 random matrix over CC and it got stuck in an infinite loop; and it always chooses 1 as a generator of the unit ideal so the results look nicer over fields. See the above third patch, to be applied on top of the previous two.

Apologies for the profusion of patches!


---

Comment by ncalexan created at 2008-12-10 02:06:43

Looks good to me.


---

Comment by mabshoff created at 2008-12-10 07:23:15

Unfortunately there is a slight reject for trac_4681_part1_smithform-consistent.patch:

```
sage-3.2.2.alpha1/devel/sage$ patch -p1 < trac_4681_part1_smithform-consistent.patch 
patching file sage/matrix/matrix2.pyx
Hunk #1 FAILED at 4549.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
patching file sage/matrix/matrix_integer_dense.pyx
patching file sage/matrix/symplectic_basis.py
patching file sage/modular/etaproducts.py
patching file sage/rings/number_field/number_field_element.pyx
patching file sage/rings/number_field/number_field_ideal.py
patching file sage/rings/number_field/order.py
patching file sage/rings/polynomial/polynomial_element.pyx
patching file sage/rings/ring.pyx
```


3.2.2.alpha1 should be out in a couple hours, so please rebase. For the record: I want to apply

 * trac_4681_part1_smithform-consistent.patch
 * 4681-docstringfix.patch
 * 4681-more-doctests.patch

Cheers,

Michael


---

Comment by davidloeffler created at 2008-12-10 10:20:32

Looks like it's clashing with trac_4493_matrix-derivative.patch -- nothing else in release-cycles-3.2.2/alpha1 seems to change matrix2.pyx. I'll rebase it around that, and combine the three patches into one at the same time.


---

Comment by mabshoff created at 2008-12-10 10:24:49

Replying to [comment:18 davidloeffler]:

Hi David,

> Looks like it's clashing with trac_4493_matrix-derivative.patch -- nothing else in release-cycles-3.2.2/alpha1 seems to change matrix2.pyx. I'll rebase it around that, and combine the three patches into one at the same time.

Excellent, I can wait a couple hours before doing alpha1 since I can work on some other fixes in the meantime. Note that you can test if your patch applies to my current merge tree at


  /scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage

by running "patch -p1 --dry-run < foo.patch" from inside that directory on sage.math.

Cheers,

Michael


---

Comment by davidloeffler created at 2008-12-10 11:01:48

Replaces all previous patches, rebased to apply over the top of #4493


---

Attachment

Here is the rebased combined patch. I've checked on sage.math as you suggest and it applies OK to the current merge tree.


---

Comment by mabshoff created at 2008-12-10 11:09:29

Thanks David,

it does indeed apply cleanly and I am doctesting it now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 11:25:53

Resolution: fixed


---

Comment by mabshoff created at 2008-12-10 11:25:53

Merged 4681-smithform-all.patch in Sage 3.2.2.alpha1.

All doctest including -long pass

Cheers,

Michael
