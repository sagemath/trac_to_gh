# Issue 8871: Finding digit sets for dilation matrices

Issue created by migration from https://trac.sagemath.org/ticket/8871

Original creator: ecurry

Original creation time: 2010-05-04 19:07:20

Assignee: Eva Curry

Add to sage a function finddigits that takes as input a dilation matrix A and a method/type of digit set to find (centered canonical "centered", minimum modulus "minimum", or colinear) and outputs a digit set D (or an appropriate error message if the method chosen is colinear and no colinear digit set exists).

I have sage code in a worksheet to do this, but need to tidy it up and test it.


---

Comment by ecurry created at 2010-05-04 21:03:33

Changing status from new to needs_work.


---

Comment by ecurry created at 2010-05-04 21:03:33

Replying to [ticket:8871 ecurry]:
Function with centered canonical digit set method implemented:


```
def finddigits(A,method):
    """
    To Do:
        Implement "minimal" method
        Implement "colinear" method
        Can the algorithm for "centered" method be made more efficient? - It is *slow* already in the 4x4 case!
        How to input method as a name rather than as a string?
    
    Inputs:
        A - a dilation matrix (square, integer entries, all eigenvalues l with |l|>1)
        method - centered (for centered canonical digit set);
                 minimal (for minimum modulus digit set);
                 colinear (for colinear digit set, if exists)
    Outputs:
        a standard digit set for A using the designated method
    
    EXAMPLES:
        A = Matrix(ZZ,[[2,0],[-8,-1]])
        finddigits(A,"centered")
        [(0, 0), (1, -4)]
        
        B = Matrix(ZZ,[[1,2,3],[1,0,2],[1,-2,-1]])
        finddigits(B,"centered")
        [(0, 0, 0), (1, 0, -1), (1, 1, 0), (2, 1, -1)]
        
        C = Matrix(ZZ,[[1,0,1,1],[-1,1,1,1],[1,2,0,-1],[-2,0,0,1]])
        finddigits(C,"centered")
        [(0, -1, 0, -1), (0, 0, 0, 0), (0, 1, 0, 1)]
    """
        from sage.combinat.permutation import Arrangements
    from sage.geometry.polyhedra import Polyhedron
    from sage.matrix.all import matrix
    d = A.ncols()
    
    """
    Method: centered
    F = (-1/2,1/2]^d
    G = AF, considered as a Polyhedron (so closed on all sides)
    find test_points := list of too many integer lattice points that might be in G
    uses the half-plane inequalities defining G to find integer lattice points that are in the interior of G, together with those on just half of the facets of G
    """
    if method=="centered":
        prelist=[]
        for i in range(2**d):
            if i-2**(d-1) >= 0: prelist.append(1)
            if i-2**(d-1) < 0: prelist.append(-1)
        matF = (1/2)*matrix(Arrangements(prelist,d).list()).transpose()
        matG = A*matF
        vertG = matG.columns()
        G = Polyhedron(vertG)
        R = floor(G.radius())
        pretest = [floor(i/d) for i in range(-R*d,(R+1)*d)]
        test_points = matrix(Arrangements(pretest,d).list())
        ieqlist = list(G.inequality_generator())
        excl_ineq = ieqlist[0:d]
        incl_ineq = ieqlist[d:2*d]
        digitslist=[]
        for p in test_points:
            i = 0
            while i < d and excl_ineq[i].interior_contains(p) and incl_ineq[i].contains(p):
                i = i+1
            if i == d:
                digitslist.append(p)
        return digitslist
    
    if method=="minimal":
        return "Minimum modulus digit set not yet implemented."
    
    if method=="colinear":
        return "Colinear digit set not yet implemented."
```



---

Comment by ecurry created at 2010-05-05 15:18:29

A better method for "centered" would be to find the lattice points in the interior of G (already implemented in Polyhedra?), then find the lattice points in the facets of G that I want to include, then take the union of these sets.

To Do: how to list the facets as Polyhedra, and choose the d (=dimension) of them that I want to include?
