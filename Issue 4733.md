# Issue 4733: matrix exponential for general matrices

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-06 23:35:17

Assignee: was

This adds a generic matrix exponential (convert to SR matrix; use maxima, or use scipy if RDF/CDF matrix)




---

Comment by jason created at 2008-12-06 23:36:03

Changing type from defect to enhancement.


---

Attachment


---

Comment by jason created at 2008-12-06 23:36:56

depends on #4493


---

Comment by jason created at 2008-12-07 04:51:14

This takes care of #2273 (sorry, I didn't find that one before opening this one).


---

Comment by wdj created at 2008-12-07 13:26:45

For my teaching, this is a very useful addition. However, the following behavior seems odd. Maybe it is a quirk and not a bug. Still, I'd like someone to comment on it before reviewing this further. 

(It is based on the facts that exp(A) commutes with A
and the derivative of exp(At) equals Aexp(At)=exp(At)A.)


```
sage: t = var('t')                 
sage: A = matrix([[1,2],[3,4]])
sage: B = (t*A).exp()
sage: Bprime = matrix(map(diff,B.list()))
sage: B(1)*A == Bprime(1)
False                    
sage: B(1)*A == A*B(1)
False                 
sage: B*A == A*B
False           
sage: MS = MatrixSpace(RR,2,2)
sage: MS(A*B(1)) == MS(Bprime(1))
False
sage: MS(A*B(1)); MS(Bprime(1))

[276.178649899715 402.884170665423]
[604.326255998134 880.504905897849]

[276.178649899715 402.884170665423]
[604.326255998134 880.504905897849]
sage: MS(A*B(-1)); MS(Bprime(-1))

[-0.405192443954626  0.196757133983140]
[ 0.295135700974710 -0.110056742979916]

[-0.405192443954626  0.196757133983140]
[ 0.295135700974710 -0.110056742979916]
sage: MS(A*B(-1)); MS(B(-1)*A)

[-0.405192443954626  0.196757133983140]
[ 0.295135700974710 -0.110056742979916]

[-0.405192443954626  0.196757133983140]
[ 0.295135700974711 -0.110056742979916]
sage:
```



---

Comment by jason created at 2008-12-12 21:28:42

Sorry, I only had a minute to look at your code...What exactly is odd?


---

Comment by jason created at 2008-12-12 21:39:44

I think I see what you were saying:


```
sage: t = var('t')     
sage: A = matrix([[1,2],[3,4]])
sage: B = (t*A).exp()
sage: Bprime = matrix(map(diff,B.list())) # This is wrong...
sage: Bprime.nrows()
1
sage: Bprime = B.apply_map(diff) # This is right (and with 3.2.2, we could just do diff(B,x) :).
sage: Bprime.nrows()
2
sage: B(1)*A == Bprime(1)
False
sage: B(1)*A == A*B(1)
False
sage: n(B(1)*A - A*B(1)) # Close to zero, should be equal to zero
[   0.000000000000000 1.42108547152020e-14]
[5.68434188608080e-14    0.000000000000000]
sage: n(B(1)*A - Bprime(1)) # Close to zero, should be equal to zero

[ 2.13162820728030e-14 -1.27897692436818e-13]
[-4.26325641456060e-14  2.84217094304040e-14]
```


Everything is all right, though.  "==" returning false just means that Sage can't prove that they are equal.  Let's simplify instead:


```
sage: (B(1)*A - A*B(1)).apply_map(lambda e: e.full_simplify())

[0 0]
[0 0]
sage: (B(1)*A - Bprime(1)).apply_map(lambda e: e.full_simplify())

[0 0]
[0 0]
```


Does that ease your mind?  Can you review this patch now?


---

Comment by wdj created at 2008-12-12 23:11:20

Yes, thanks. I just wanted to make sure that wasn't a problem.

Applies cleanly and passes sage -t on both modules it modifies. Looks good to me.


---

Comment by mabshoff created at 2008-12-13 02:45:21

This patch does not compile for me:

```
python2.5 `which cython` --embed-positions --incref-local-binop 
-I/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage-main 
-o sage/matrix/matrix_mod2_dense.c sage/matrix/matrix_mod2_dense.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
        a = t.transpose()
        right_mat = right_mat* s.transpose()

    return left_mat, a, right_mat
    
    def exp(self):
   ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage-main/
sage/matrix/matrix2.pyx:4914:4: def statement not allowed here
Parallel build failed with status 256.
sage: There was an error installing modified sage library code.
```

Note that it applied with huge, i.e. 337 line, offset. This patch probably needs a rebase.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 01:50:48

trivial rebase to 3.3.alpha0


---

Attachment


---

Comment by mabshoff created at 2009-01-23 07:30:51

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 07:30:51

Resolution: fixed
