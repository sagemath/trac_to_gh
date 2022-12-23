# Issue 5879: [with patch, needs review] Added crystal of letters for type E

archive/issues_005879.json:
```json
{
    "body": "Assignee: aschilling\n\nCC:  sage-combinat-commits\n\nKeywords: combinat, crystals\n\nThis patch adds crystal of letters for type E corresponding to\nthe highest weight crystal B(\\Lambda_1) and its dual B(\\Lambda_6) (in the sage labeling convention of the Dynkin nodes).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5879\n\n",
    "created_at": "2009-04-23T19:27:33Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Added crystal of letters for type E",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5879",
    "user": "aschilling"
}
```
Assignee: aschilling

CC:  sage-combinat-commits

Keywords: combinat, crystals

This patch adds crystal of letters for type E corresponding to
the highest weight crystal B(\Lambda_1) and its dual B(\Lambda_6) (in the sage labeling convention of the Dynkin nodes).

Issue created by migration from https://trac.sagemath.org/ticket/5879





---

archive/issue_comments_046449.json:
```json
{
    "body": "For what it's worth, here's a picture of this crystal:\n\nhttp://sporadic.stanford.edu/bump/xtal/e6.pdf\n\nWhat is the logic of the representations of the elements? That is, why [-5,2,6]?",
    "created_at": "2009-04-24T14:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46449",
    "user": "bump"
}
```

For what it's worth, here's a picture of this crystal:

http://sporadic.stanford.edu/bump/xtal/e6.pdf

What is the logic of the representations of the elements? That is, why [-5,2,6]?



---

archive/issue_comments_046450.json:
```json
{
    "body": "After some testing I am confident that the crystal is correct.\n\nAdding this one crystal (with its dual) actually gives access to\nall E6 crystals (modulo computational complexity) since they can\nbe obtained as subcrystals of tensor products of these two. For\nexample, the second fundamental weight corresponds to a representation\nof degree 351 whose crystal can be obtained thus:\n\n\n```\nsage: C = CrystalOfLetters(\"E6\")\nsage: T = TensorProductOfCrystals(C,C,generators=[[C[0],C[0]]])\nsage: T.cardinality()\n351\n```\n\n\nThe fact that this process (using both crystals) is complete to give all crystals is\nconfirmed here:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/8ef5b6b5b529e51b?hl=en\n\nThis crystal is also interesting because the action of the E6 Weyl group on this \ncrystal of degree 27 must be equivalent to the action of E6 on the 27 lines on a cubic surface.",
    "created_at": "2009-04-25T00:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46450",
    "user": "bump"
}
```

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

archive/issue_comments_046451.json:
```json
{
    "body": "> What is the logic of the representations of the elements? That is, why [-5,2,6]?\n\nThe nodes of this crystal are labeled by their weights. [-5,2,6] indicates that \na 5-arrow is coming in, and a 2-arrow and 6-arrow is leaving the vertex.\n\nI now also added a __repr__ method that allows for concise printing of the nodes by\n+abcdefghijklmnopqrstuvwxyz and -ABCDEFGHIJKLMNOPQRSTUVWXYZ in the dual crystal.",
    "created_at": "2009-04-25T07:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46451",
    "user": "aschilling"
}
```

> What is the logic of the representations of the elements? That is, why [-5,2,6]?

The nodes of this crystal are labeled by their weights. [-5,2,6] indicates that 
a 5-arrow is coming in, and a 2-arrow and 6-arrow is leaving the vertex.

I now also added a __repr__ method that allows for concise printing of the nodes by
+abcdefghijklmnopqrstuvwxyz and -ABCDEFGHIJKLMNOPQRSTUVWXYZ in the dual crystal.



---

archive/issue_comments_046452.json:
```json
{
    "body": "The revision of the patch implementing concise representation is important since\nfor tensor products of crystals the names of elements would be very cumbersome.\nThe crystal at hand has highest weight the first fundamental weight, lambda1 in the\nBourbaki notation. The dual crystal has highest weight lambda6:\n\n```\n        O 2\n        |\n        |\nO---O---O---O---O\n1   3   4   5   6\nE6\n```\n\nThese both have degree 27. The adjoint representation has highest weight lambda2\nhas degree 78 and can be constructed as follows:\n\n```\nsage: C = CrystalOfLetters(['E',6], element_print_style = 'compact')\nsage: D = CrystalOfLetters(['E',6], element_print_style = 'compact', dual=True)\nsage: hwv=TensorProductOfCrystals(C,D).highest_weight_vectors(); hwv\n[[+, -], [j, -], [x, -]]\nsage: T = TensorProductOfCrystals(C,D,generators=[hwv[1]])\nsage: T.cardinality()\n78\nsage: T.latex_file(\"/home/bump/tmp/e6-78.tex\")\n```\n\nThe last step assumes you have dot2tex installed. (Why isn't this\nbundled with SAGE?)\nHere is the resulting crystal of the adjoint representation:\n\nhttp://sporadic.stanford.edu/bump/xtal/e6-78.pdf",
    "created_at": "2009-05-02T17:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46452",
    "user": "bump"
}
```

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

archive/issue_comments_046453.json:
```json
{
    "body": "Mhh, what is the credit situation here? \"Brant Jones\" was added to the list of authors, so is this shared credit for Anne and Brant for authorship?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-07T06:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46453",
    "user": "mabshoff"
}
```

Mhh, what is the credit situation here? "Brant Jones" was added to the list of authors, so is this shared credit for Anne and Brant for authorship?

Cheers,

Michael



---

archive/issue_comments_046454.json:
```json
{
    "body": "Yes, shared authorship please.\n\nAnne",
    "created_at": "2009-05-07T06:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46454",
    "user": "aschilling"
}
```

Yes, shared authorship please.

Anne



---

archive/issue_comments_046455.json:
```json
{
    "body": "This breaks pickling for me (and #5120 by itself did not):\n\n```\n    ** failed:  _class__sage_combinat_crystals_letters_ClassicalCrystalOfLetters__.sobj\n    ** failed:  _class__sage_combinat_crystals_tensor_product_CrystalOfTableauxElement__.sobj\n    ** failed:  _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux__.sobj\n    ** failed:  _class__sage_combinat_crystals_tensor_product_FullTensorProductOfClassicalCrystals__.sobj\n    ** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfClassicalCrystalsWithGenerators__.sobj\n    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Failed:\n    _class__sage_combinat_crystals_letters_ClassicalCrystalOfLetters__.sobj\n    _class__sage_combinat_crystals_tensor_product_CrystalOfTableauxElement__.sobj\n    _class__sage_combinat_crystals_tensor_product_CrystalOfTableaux__.sobj\n    _class__sage_combinat_crystals_tensor_product_FullTensorProductOfClassicalCrystals__.sobj\n    _class__sage_combinat_crystals_tensor_product_TensorProductOfClassicalCrystalsWithGenerators__.sobj\n```\n\nAlso:\n\n```\n\tfrom sage.quadratic_forms.extras import sgn \n```\n\nis going away since it is basically cmp(a,b).\n\nCheers,\n\nMichael",
    "created_at": "2009-05-07T06:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46455",
    "user": "mabshoff"
}
```

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

archive/issue_comments_046456.json:
```json
{
    "body": "Replying to [comment:7 aschilling]:\n> Yes, shared authorship please.\n> \n> Anne\n\nCool. Please specify shared authorship when you post the patch via the comment section during the file upload. That makes it just easier for me to keep track of credit.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-07T07:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46456",
    "user": "mabshoff"
}
```

Replying to [comment:7 aschilling]:
> Yes, shared authorship please.
> 
> Anne

Cool. Please specify shared authorship when you post the patch via the comment section during the file upload. That makes it just easier for me to keep track of credit.

Cheers,

Michael



---

archive/issue_comments_046457.json:
```json
{
    "body": "I just talked to Nicolas about the pickling problem; this is a shortcoming of the current\nunique representation patch and he will try to find a solution to the problem in patch 5120.",
    "created_at": "2009-05-08T00:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46457",
    "user": "aschilling"
}
```

I just talked to Nicolas about the pickling problem; this is a shortcoming of the current
unique representation patch and he will try to find a solution to the problem in patch 5120.



---

archive/issue_comments_046458.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-08T00:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46458",
    "user": "aschilling"
}
```

Attachment



---

archive/issue_comments_046459.json:
```json
{
    "body": "The revised patch fixes the sgn versus comparison issue.\nThe pickling problem will hopefully be fixed by modifications in unique representations!",
    "created_at": "2009-05-08T00:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46459",
    "user": "aschilling"
}
```

The revised patch fixes the sgn versus comparison issue.
The pickling problem will hopefully be fixed by modifications in unique representations!



---

archive/issue_comments_046460.json:
```json
{
    "body": "Nicolas is about to submit a new version of patch #5120 which should fix the pickling problem Michael mentioned above. We checked this by hand, but Michael, could you run your automatic pickling tests again?",
    "created_at": "2009-05-08T21:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46460",
    "user": "aschilling"
}
```

Nicolas is about to submit a new version of patch #5120 which should fix the pickling problem Michael mentioned above. We checked this by hand, but Michael, could you run your automatic pickling tests again?



---

archive/issue_comments_046461.json:
```json
{
    "body": "Pickling seems fine and #5120 got a positive review.  So I reinstate the positive review.",
    "created_at": "2009-05-20T01:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46461",
    "user": "nthiery"
}
```

Pickling seems fine and #5120 got a positive review.  So I reinstate the positive review.



---

archive/issue_comments_046462.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T00:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46462",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_046463.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T00:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5879#issuecomment-46463",
    "user": "mabshoff"
}
```

Resolution: fixed
