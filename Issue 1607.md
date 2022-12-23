# Issue 1607: kernel -- A.right_kernel and A.left_kernel

archive/issues_001607.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\nIt would be really useful to have\n\n   sage: A.right_kernel()\n\nto mean the set of vectors v such that A*v = 0, i.e., the vectors on the right.\nThat would have to be clearly documented -- the function itself would\nbe defined in matrix2.pyx and would just transpose A and call kernel\non the resulting transpose.  It would also cache the result.  \n\nWe have A.right_eigenvectors() in some cases (e.g., A an RDF matrix), and\nthe documentation makes the meaning very clear:\n\n------------------------------\n\nsage: A = random_matrix(RDF,3)\nsage: A.right_eigenvectors()\n([1.34856636676, -1.04338481358, -0.208244283695],\n [-0.250271326138  0.846883172518 0.0580964218791]\n[ 0.884959315834  0.223023546117 -0.702413116863]\n[ 0.392697431404   0.48275189278  0.709394543977])\nsage: A.left_eigenvectors()\n([1.34856636676, -1.04338481358, -0.208244283695],\n [ -0.51163197441  0.589230432257  0.625332088145]\n[ 0.967591994779  0.214539369634  0.133186300037]\n[-0.344957735432 -0.460493249193  0.817893714497])\nsage: A.right_eigenvectors?\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in method right_eigenvectors of sage.matrix.matrix_real_double_dense.Matrix_real_double_dense object at 0x2b077b08c3b0>\nNamespace:      Interactive\nDocstring:\n    \n            Computes the eigenvalues and *right* eigenvectors of this\n            matrix m acting *from the left*.  I.e., vectors v such that\n            m * v = lambda*v, where v is viewed as a column vector. \n------------------------------\n\n\n\nIt actually might be possible to define\n\n   sage: A.left_kernel()\n\nand\n\n   sage: A.right_kernel()\n\nand have\n  \n  sage: A.kernel()\n\ndefault to A.right_kernel() without breaking sage into a million pieces.\nOne would first define only A.left_kernel and A.right_kernel.  Then\none would go through all of Sage and make sure every instance of\nA.kernel where A is a matrix is changed to A.left_kernel -- since that\nis what is currently assumed, then doctest everything, and finally\ndefine a function kernel() in matrix2.pyx, which just calls self.right_kernel().\n\nSince x*A and A*x are both defined for x = vector(...), I think this\nwould be reasonable. \n\n -- William \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1607\n\n",
    "created_at": "2007-12-27T04:08:56Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "kernel -- A.right_kernel and A.left_kernel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1607",
    "user": "was"
}
```
Assignee: was


```

It would be really useful to have

   sage: A.right_kernel()

to mean the set of vectors v such that A*v = 0, i.e., the vectors on the right.
That would have to be clearly documented -- the function itself would
be defined in matrix2.pyx and would just transpose A and call kernel
on the resulting transpose.  It would also cache the result.  

We have A.right_eigenvectors() in some cases (e.g., A an RDF matrix), and
the documentation makes the meaning very clear:

------------------------------

sage: A = random_matrix(RDF,3)
sage: A.right_eigenvectors()
([1.34856636676, -1.04338481358, -0.208244283695],
 [-0.250271326138  0.846883172518 0.0580964218791]
[ 0.884959315834  0.223023546117 -0.702413116863]
[ 0.392697431404   0.48275189278  0.709394543977])
sage: A.left_eigenvectors()
([1.34856636676, -1.04338481358, -0.208244283695],
 [ -0.51163197441  0.589230432257  0.625332088145]
[ 0.967591994779  0.214539369634  0.133186300037]
[-0.344957735432 -0.460493249193  0.817893714497])
sage: A.right_eigenvectors?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in method right_eigenvectors of sage.matrix.matrix_real_double_dense.Matrix_real_double_dense object at 0x2b077b08c3b0>
Namespace:      Interactive
Docstring:
    
            Computes the eigenvalues and *right* eigenvectors of this
            matrix m acting *from the left*.  I.e., vectors v such that
            m * v = lambda*v, where v is viewed as a column vector. 
------------------------------



It actually might be possible to define

   sage: A.left_kernel()

and

   sage: A.right_kernel()

and have
  
  sage: A.kernel()

default to A.right_kernel() without breaking sage into a million pieces.
One would first define only A.left_kernel and A.right_kernel.  Then
one would go through all of Sage and make sure every instance of
A.kernel where A is a matrix is changed to A.left_kernel -- since that
is what is currently assumed, then doctest everything, and finally
define a function kernel() in matrix2.pyx, which just calls self.right_kernel().

Since x*A and A*x are both defined for x = vector(...), I think this
would be reasonable. 

 -- William 
```


Issue created by migration from https://trac.sagemath.org/ticket/1607





---

archive/issue_comments_010210.json:
```json
{
    "body": "From  David Joyner:\n\n+1 and\n\n\"An option is to add column_echelon in addition to echelon (ie, row_echelon).\nThis is another left vs right thing.\"",
    "created_at": "2007-12-27T05:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1607#issuecomment-10210",
    "user": "was"
}
```

From  David Joyner:

+1 and

"An option is to add column_echelon in addition to echelon (ie, row_echelon).
This is another left vs right thing."



---

archive/issue_comments_010211.json:
```json
{
    "body": "This was taken care of by #2542.",
    "created_at": "2008-04-15T01:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1607#issuecomment-10211",
    "user": "mhansen"
}
```

This was taken care of by #2542.



---

archive/issue_comments_010212.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-15T01:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1607#issuecomment-10212",
    "user": "mhansen"
}
```

Resolution: duplicate
