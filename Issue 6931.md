# Issue 6931: implement faster computation of data about intersection of abelian varieties attached to modular symbols spaces

Issue created by migration from https://trac.sagemath.org/ticket/6931

Original creator: was

Original creation time: 2009-09-15 04:59:42

Assignee: craigcitro

Amod *really* wants something like this.  Here's code that I just wrote in a notebook that I think is perhaps the optimal algorithm along these lines:


```
def intersect(A, B, p, integral=True):
    r"""
    Return True if p divides the cardinality of the intersection of the abelian
    varieties corresponding to the modular symbols spaces A and B.
    
    INPUT:
    
        - `A` -- cuspidal modular symbols space
        
        - `B` -- cuspidal modular symbols space
        
        - `p` -- prime number
        
        - ``integral`` -- bool (default: True); if False, just take the 
          `\QQ`-basis for the integral structure, which is much faster, 
          but can give false answers (i.e., at worst, I think `A` and `B` 
          would be declared congruent even when they are not). 
          
    OUTPUT:
        
        - ``bool`` -- True if `p` divides intersection of `A` and `B`
        
    EXAMPLES::
        
        sage: H = ModularSymbols(389,2,sign=1).cuspidal_subspace(); D = H.decomposition()
        sage: intersect(D[0],D[4],5)
        True
        sage: intersect(D[0],D[4],7)
        False
        sage: intersect(D[0],D[4],5,integral=False)
        True

        sage: H = ModularSymbols(54).cuspidal_subspace(); D = H.decomposition()
        sage: intersect(D[0],D[2],2)
        False
        sage: intersect(D[0],D[2],3)
        True
        sage: intersect(D[0],D[2],3, integral=False)
        True
        sage: intersect(D[0],D[2],5)
        False
    """           
    if integral: 
        VA = A.integral_structure()
        VB = B.integral_structure()
    else:       
        VA = A.free_module(); VB = B.free_module() 
    LA, dA = VA.basis_matrix()._clear_denom()
    LB, dB = VB.basis_matrix()._clear_denom()
    LA *= dB; LB *= dA
    n = gcd([ZZ(a) for a in LA.list() + LB.list()])
    if n%p == 0:
        LA = LA/n; LB = LB/n
    return LA.stack(LB).change_ring(GF(p)).nullity() > 0
```

