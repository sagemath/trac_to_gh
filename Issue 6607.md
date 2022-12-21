# Issue 6607: Quadratics in GF(2^m)

Issue created by migration from Trac.

Original creator: wakep

Original creation time: 2009-07-23 22:36:10

Assignee: tbd

Keywords: quadratics, characteristic 2

Added specialized code for factoring quadratic polynomials over GF(2^m).


---

Comment by mvngu created at 2009-08-04 07:13:55

Please follow coding conventions, especially those documented in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions) and [PEP-0008](http://www.python.org/dev/peps/pep-0008/). Don't be afraid to use white spaces in your code. The patch contains codes that are squeezed together; this is difficult to read. For example, this is bad:

```
def gftwosqrt(r): 
    """ 
    Quickly finds the squareroot of an element in GF(2^m) 
    """
    F=r.parent() 
    c=F.cardinality() 
    return r**(c/2)
```

and you should do this instead:

```
def gftwosqrt(r): 
    """ 
    Quickly finds the squareroot of an element in GF(2^m)
    
    INPUT:
    
    <explain any input to this function>
    
    OUTPUT:
    
    <what's the expected output of this function?>
    
    EXAMPLES::
    
        <add-more-doctests-here>
    """
    F = r.parent() 
    c = F.cardinality() 
    return r**(c/2)
```

For more information about writing docstrings, see [this section](http://www.sagemath.org/doc/developer/conventions.html#documentation-strings). Apart from these, there are other reasons to reject the patch, as documented [here](http://www.sagemath.org/doc/developer/trac.html).


---

Comment by wakep created at 2009-08-13 04:30:27

fixed old patch... better documentation etc


---

Attachment

fixed references


---

Comment by wakep created at 2009-08-26 23:26:05

quad.patch should replace 12538.patch


---

Comment by AlexGhitza created at 2009-11-15 10:34:14

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2009-11-15 10:34:14

This has been sitting for a while and got some bitrot.  It doesn't apply cleanly against sage-4.2.

Preston, can you rebase it on sage-4.2?  I'll try to review it quickly after that so you don't have to do this again.

Actually, while you're at it, do you want to just put up a new standalone patch?  As it stands now, quad.patch is dependent on 12538.patch.
