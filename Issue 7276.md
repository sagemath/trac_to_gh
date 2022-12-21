# Issue 7276: Fix PPC issues in totallyreal_rel.py

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-10-23 23:40:35

Assignee: davidloeffler

CC:  georgsweber was

Keywords: PPC, powerpc, lattice

From #7112: I don't think this ended up getting officially logged on trac elsewhere.


```
sage -t -long devel/sage/sage/rings/number_field/totallyreal_rel.py
```

will still fail however, there is a deeper problem lurking in that one point of a certain lattice sitting in a certain rectangle is missed in the computations on a PPC platform --- but that would be another ticket. Let the doctest fail for the time being, the enhancements by the patch(es) for this ticket here are needed anyway, I guess.




---

Comment by kcrisman created at 2009-10-28 14:59:14

Here is the code for integral_elements_in_box line by line, up to the first place where PPC differs from Intel:

```
sage: K.<alpha> = NumberField(x^2-2)
sage: d = K.degree()
sage: Z_F = K.maximal_order()
sage: Foo = K.real_embeddings()
sage: B = K.reduced_basis()
sage: import numpy
sage: import numpy.linalg
sage: L = numpy.array([ [v(b) for b in B] for v in Foo])
sage: Linv = numpy.linalg.inv(L)
sage: C = [[0,5],[0,5]]
sage: Vi = [[C[0][0]],[C[0][1]]]
sage: 
sage: Linv

array([[ 0.5       ,  0.5       ],
       [-0.35355339,  0.35355339]])
sage: for i in range(1,d):
....:     Vi = sum([ [v + [C[i][0]], v + [C[i][1]]] for v in Vi], [])
....:     
sage: Vi
[[0, 0], [0, 5], [5, 0], [5, 5]]
sage: V = numpy.matrix(Linv)*(numpy.matrix(Vi).transpose())
sage: V

matrix([[  0.00000000e+00,   2.50000000e+00,   2.50000000e+00,
           5.00000000e+00],
        [  0.00000000e+00,   1.76776695e+00,  -1.76776695e+00,
           5.55111512e-17]])
```

In particular, the matrices Linv and Vi, even in their numpy versions, are still the same.  Essentially, on PPC (at least G4) the computation -0.35355339*5+0.35355339*5 is not (quite) zero, but on Intel it is.  On Intel we get the same stuff but with just 0., 2.5, etc - and the last entry is 0., no hint of the 5.55e-17.  

Anyway, this leads to the following error (since we are depending on the ceil of zero to be zero, but the ceil of 5.55e-17 is 1):

```
sage: while j < 2**d:
    for i in range(d):
        if V[i,j] < V[i,j+1]:
            V[i,j] = math.floor(V[i,j])
            V[i,j+1] = math.ceil(V[i,j+1])
        else:
            V[i,j] = math.ceil(V[i,j])
            V[i,j+1] = math.floor(V[i,j+1])
    j +=2
....:         
sage: V

matrix([[ 0.,  3.,  2.,  5.],
        [ 0.,  2., -2.,  1.]])
```

Where Intel correctly gives 0. in the last entry.

Just so that it's clear that PPC is the issue:

```
sage: matrix(Linv)*matrix(Vi).transpose()

[              0.0               2.5               2.5               5.0]
[              0.0     1.76776695297    -1.76776695297 5.55111512313e-17]
```

Slightly more digits, but same problem.  I can in fact do the computation completely in Sage (which I assume doesn't call numpy for matrix multiplication?) and get the same.  Note however that Sage CAN multiply correctly, as can Numpy:

```
sage: -0.35355339*5+0.35355339*5
0.000000000000000
sage: numpy.int(5)*numpy.float(-0.35355339)+numpy.int(5)*numpy.float(0.35355339)
0.0
```

So somehow it has to do with our matrix multiplication algorithm and how it works on PPC.  Perhaps there are other nasty bugs lurking as yet unseen.  Any thoughts?


---

Comment by GeorgSWeber created at 2009-10-28 22:54:41

The file "devel/sage/sage/rings/number_field/totallyreal_rel.py" has five functions, and only three of these have doctests. The problem in this ticket is with one these, which is an internal function not used elsewhere. From what I guess from the code, it is meant to be called with "inexact" bounds --- see the use of "eps_global".

So we might "heal" this internal function by using some kind of interval technique --- but the price could be high, i.e. slowing down the algorithm where this internal function is intended to be used.

I rather propose to heal the doctest by giving bounds [-0.1, 5.1] ... instead of [0, 5] ..., which most probably is far closer to the actual intended usage than the current doctest.


---

Comment by kcrisman created at 2009-10-29 14:35:09

Just for the record, can you clarify where that is called in integral_elements_in_box?   Especially since Linv and Vi are the same on PPC and Intel, but not the matrix multiplication, which is what integral_elements_in_box uses?   

However, if you can explain that, I agree that (assuming the inexact bounds is correct) fixing the doctest in this way is okay.

Or are you saying that there is more than one problem?  The documentation for one of the other functions does note platform-dependence, so certainly the author knew this.  You might want to email him as well, unfortunately I am not a number field expert so can't identify it further.


---

Comment by was created at 2009-11-06 15:41:44

Changing priority from major to blocker.


---

Comment by was created at 2009-11-06 15:41:44

This is also broken on Itanium.  This *MUST* get fixed -- so I'm promoting this to blocker.  We either remove offending code or fix the bug. 

```
sage -t  "devel/sage/sage/rings/number_field/totallyreal_rel.py"
**********************************************************************
File "/home/wstein/screen/cleo/build/sage-4.2/devel/sage/sage/rings/number_field/totallyreal_rel.py", line 48:
    sage: sorted([str(a) for a in v])
Expected:
    ['-alpha + 2', '-alpha + 3', '0', '1', '2', '3', '4', '5', 'alpha + 2', 'alpha + 3']
Got:
    ['-alpha + 2', '-alpha + 3', '0', '1', '2', '3', '4', 'alpha + 2', 'alpha + 3']
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_1
```



---

Comment by kcrisman created at 2009-11-06 15:49:23

William, can you try 

```
sage: K.<alpha> = NumberField(x^2-2)
sage: d = K.degree()
sage: Z_F = K.maximal_order()
sage: Foo = K.real_embeddings()
sage: B = K.reduced_basis()
sage: import numpy
sage: import numpy.linalg
sage: L = numpy.array([ [v(b) for b in B] for v in Foo])
sage: Linv = numpy.linalg.inv(L)
sage: C = [[0,5],[0,5]]
sage: Vi = [[C[0][0]],[C[0][1]]]
sage: Linv # should be array([[ 0.5       ,  0.5       ],       [-0.35355339,  0.35355339]])
sage: for i in range(1,d):
....:     Vi = sum([ [v + [C[i][0]], v + [C[i][1]]] for v in Vi], [])
....:     
sage: Vi # should be [[0, 0], [0, 5], [5, 0], [5, 5]]
sage: V = numpy.matrix(Linv)*(numpy.matrix(Vi).transpose())
sage: V # should be matrix([[  0.00000000e+00,   2.50000000e+00,   2.50000000e+00,           5.00000000e+00],        [  0.00000000e+00,   1.76776695e+00,  -1.76776695e+00,           0.00000000e+00]]) but isn't on PPC, last element is e-17
sage: matrix(Linv)*matrix(Vi).transpose() # should be [              0.0               2.5               2.5               5.0] [              0.0     1.76776695297    -1.76776695297           0.0] but isn't on PPC
}}} 
on cleo to see if (one of the) problem(s) there is also in matrix multiplication on itanium?   Just to clarify, at least one problem is that ceil(0)=0 but ceil(epsilon)=1.


---

Comment by was created at 2009-11-10 05:54:47

The output on itanium (cleo) is exactly the same as on PPC above.  I.e., I get "last element is e-17".  

So is there a bug somewhere in the algorithm that assumes some floating point number is 0.0, but really it might just be epsilon sometimes, and this is revealed on PPC and Itanium. 

NOTE: Our PPC box is *big endian*.  Our Itanium is *little endian*.  So this is not just an endianess issue.


---

Comment by was created at 2009-11-10 06:27:25

Changing status from new to needs_review.


---

Attachment

I have attached a patch that does what Georg suggested above.  I also added more doctests (i.e., a cubic example) to explain what the mysterius "C" is.   With this patch, doctests pass on ppc, itanium, and x86_64 now. 

I've also emailed John Voight asking him to get the docs of this file up to snuff.


---

Comment by kcrisman created at 2009-11-10 14:24:24

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-11-10 14:24:24

You're gonna love this... on Intel Mac 10.5:

```
number_field/totallyreal_rel.py", line 76:
    sage: sorted(v)
Expected:
    [-1/2*a + 2, 1/4*a^2 + 1/2*a, 0, 1, 2, 3, 4, -1/4*a^2 - 1/2*a + 5, 1/2*a + 3, -1/4*a^2 + 5]
Got:
    [-1/2*a + 2, 1/4*a^2 + 1/2*a, 0, 1, 2, 3, 4, 5, -1/4*a^2 - 1/2*a + 5, 1/2*a + 3, -1/4*a^2 + 5]
```

This is from the cubic field example.

Also, probably it would be good to directly confirm that the original bugbear is fixed, at the end of the first doctest:

```
sage: C = [[0-eps,5+eps],[0-eps,5+eps]] 
sage: v = sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, C) 
sage: sorted(v) [-alpha + 2, -alpha + 3, 0, 1, 2, 3, 4, 5, alpha + 2, alpha + 3]
```


The documentation clarifies things a lot, so +1 on that!


---

Comment by kcrisman created at 2009-11-10 14:28:48

But all tests pass on PPC ;-)


---

Comment by GeorgSWeber created at 2009-11-10 20:10:08

apply instead the first patch from William


---

Attachment

Grmpf.

The new patch version 2 tried to address the issues. In the cubic field example, the "5" should be in, so I enlarged the epsilon. This works "as is" on MacIntel OS X 10.4.11.

However, the patch version 2 does *not* work on MacPPC OS X 10.4.11, so this ticket has to stay "needs work".


---

Comment by was created at 2009-11-11 16:43:08

ignore georg's patch above.  apply trac_7276.patch and this.


---

Attachment


---

Comment by was created at 2009-11-11 16:43:28

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-11-11 17:03:32

Remark from John Voight:
"...what a mess!  I'm so sorry.  (Next time, feel free to contact
me earlier if there are issues with my code that I can be of help
with.)

The algorithm used is described in
 http://www.cems.uvm.edu/~voight/articles/ANTS144.pdf
in Section 3.1 (page 9), "Lattice points in boxes".  There is
absolutely a rounding issue which I can see as failing miserably in
low precision.  Off the top of my head, one might be able to fix the
issue by replacing a ceiling with a floor + 1, or even a ceiling +
1--but even then, this assumes the precision loss is so constrained...

I won't have a chance to work on the doctest until the weekend, but
it's in my queue now.

JV"


---

Comment by GeorgSWeber created at 2009-11-11 20:40:15

Changing status from needs_review to positive_review.


---

Comment by GeorgSWeber created at 2009-11-11 20:40:15

Tested positively on both MacIntel OS X 10.4 and MacPPC OS X 10.4 (apply the original patch and the "part2" patch, both from William; do ignore my "v2" patch).


---

Comment by mhansen created at 2009-11-12 06:09:44

Resolution: fixed


---

Comment by was created at 2009-12-10 01:25:24

See #7649 for a followup ticket.
