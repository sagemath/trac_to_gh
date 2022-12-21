# Issue 5879: [with patch, needs review] Added crystal of letters for type E

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2009-04-23 19:27:33

Assignee: aschilling

CC:  sage-combinat-commits

Keywords: combinat, crystals

This patch adds crystal of letters for type E corresponding to
the highest weight crystal B(\Lambda_1) and its dual B(\Lambda_6) (in the sage labeling convention of the Dynkin nodes).


---

Comment by bump created at 2009-04-24 14:20:05

For what it's worth, here's a picture of this crystal:

http://sporadic.stanford.edu/bump/xtal/e6.pdf

What is the logic of the representations of the elements? That is, why [-5,2,6]?


---

Comment by bump created at 2009-04-25 00:21:10

After some testing I am confident that the crystal is correct.

Adding this one crystal (with its dual) actually gives access to
all E6 crystals (modulo computational complexity) since they can
be obtained as subcrystals of tensor products of these two. For
example, the second fundamental weight corresponds to a representation
of degree 351 whose crystal can be obtained thus:


```
sage: C = CrystalOfLetters("E6")
sage: T = TensorProductOfCrystals(C,C,generators=[[C[0],C[0]]])
sage: T.cardinality()
351
```


The fact that this process (using both crystals) is complete to give all crystals is
confirmed here:

http://groups.google.com/group/sage-combinat-devel/msg/8ef5b6b5b529e51b?hl=en

This crystal is also interesting because the action of the E6 Weyl group on this 
crystal of degree 27 must be equivalent to the action of E6 on the 27 lines on a cubic surface.


---

Comment by aschilling created at 2009-04-25 07:05:20

> What is the logic of the representations of the elements? That is, why [-5,2,6]?

The nodes of this crystal are labeled by their weights. [-5,2,6] indicates that 
a 5-arrow is coming in, and a 2-arrow and 6-arrow is leaving the vertex.

I now also added a __repr__ method that allows for concise printing of the nodes by
+abcdefghijklmnopqrstuvwxyz and -ABCDEFGHIJKLMNOPQRSTUVWXYZ in the dual crystal.


---

Comment by bump created at 2009-05-02 17:55:10

The revision of the patch implementing concise representation is important since
for tensor products of crystals the names of elements would be very cumbersome.
The crystal at hand has highest weight the first fundamental weight, lambda1 in the
Bourbaki notation. The dual crystal has highest weight lambda6:

```
        O 2
        |
        |
O---O---O---O---O
1   3   4   5   6
E6
```

These both have degree 27. The adjoint representation has highest weight lambda2
has degree 78 and can be constructed as follows:

```
sage: C = CrystalOfLetters(['E',6], element_print_style = 'compact')
sage: D = CrystalOfLetters(['E',6], element_print_style = 'compact', dual=True)
sage: hwv=TensorProductOfCrystals(C,D).highest_weight_vectors(); hwv
[[+, -], [j, -], [x, -]]
sage: T = TensorProductOfCrystals(C,D,generators=[hwv[1]])
sage: T.cardinality()
78
sage: T.latex_file("/home/bump/tmp/e6-78.tex")
```

The last step assumes you have dot2tex installed. (Why isn't this
bundled with SAGE?)
Here is the resulting crystal of the adjoint representation:

http://sporadic.stanford.edu/bump/xtal/e6-78.pdf


---

Comment by mabshoff created at 2009-05-07 06:37:56

Mhh, what is the credit situation here? "Brant Jones" was added to the list of authors, so is this shared credit for Anne and Brant for authorship?

Cheers,

Michael


---

Comment by aschilling created at 2009-05-07 06:53:56

Yes, shared authorship please.

Anne


---

Comment by mabshoff created at 2009-05-07 06:59:31

This breaks pickling for me (and #5120 by itself did not):

```
    ** failed:  _class__sage_combinat_crystals_letters_ClassicalCrystalOfLetters__.sobj
    ** failed:  _class__sage_combinat_crystals_tensor_product_CrystalOfTableauxElement__.sobj
    ** failed:  _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux__.sobj
    ** failed:  _class__sage_combinat_crystals_tensor_product_FullTensorProductOfClassicalCrystals__.sobj
    ** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfClassicalCrystalsWithGenerators__.sobj
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Failed:
    _class__sage_combinat_crystals_letters_ClassicalCrystalOfLetters__.sobj
    _class__sage_combinat_crystals_tensor_product_CrystalOfTableauxElement__.sobj
    _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux__.sobj
    _class__sage_combinat_crystals_tensor_product_FullTensorProductOfClassicalCrystals__.sobj
    _class__sage_combinat_crystals_tensor_product_TensorProductOfClassicalCrystalsWithGenerators__.sobj
```

Also:

```
	from sage.quadratic_forms.extras import sgn 
```

is going away since it is basically cmp(a,b).

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-07 07:06:11

Replying to [comment:7 aschilling]:
> Yes, shared authorship please.
> 
> Anne

Cool. Please specify shared authorship when you post the patch via the comment section during the file upload. That makes it just easier for me to keep track of credit.

Cheers,

Michael


---

Comment by aschilling created at 2009-05-08 00:31:26

I just talked to Nicolas about the pickling problem; this is a shortcoming of the current
unique representation patch and he will try to find a solution to the problem in patch 5120.


---

Attachment


---

Comment by aschilling created at 2009-05-08 00:59:43

The revised patch fixes the sgn versus comparison issue.
The pickling problem will hopefully be fixed by modifications in unique representations!


---

Comment by aschilling created at 2009-05-08 21:37:06

Nicolas is about to submit a new version of patch #5120 which should fix the pickling problem Michael mentioned above. We checked this by hand, but Michael, could you run your automatic pickling tests again?


---

Comment by nthiery created at 2009-05-20 01:19:35

Pickling seems fine and #5120 got a positive review.  So I reinstate the positive review.


---

Comment by mabshoff created at 2009-05-21 00:59:30

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 00:59:30

Resolution: fixed
