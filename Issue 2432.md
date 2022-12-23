# Issue 2432: Add support for Macdonald polynomials, LLT polynomials, Jack polynomials, etc.

Issue created by migration from https://trac.sagemath.org/ticket/2432

Original creator: mhansen

Original creation time: 2008-03-09 02:57:53

Assignee: mhansen

CC:  sage-combinat




---

Comment by mhansen created at 2008-03-09 03:53:35

Changing type from defect to enhancement.


---

Comment by mhansen created at 2008-03-09 03:53:35

Changing status from new to assigned.


---

Comment by mhansen created at 2008-03-09 13:06:12

I've put a patch at http://sage.math.washington.edu/home/mhansen/macdonald.patch


---

Comment by mabshoff created at 2008-03-09 15:48:13

Once this patch is applied and reviewd we should also close #2427.

Cheers,

Michael


---

Comment by saliola created at 2008-03-10 01:02:48

I've started reviewing this patch (and plan to finish it over the next few days). So far I've made it up to ribbon_tableau.py. Here are my comments/questions so far.

--

First some general comments.

Almost all functions have good examples, but some lack descriptions.
See, for example, _coerce_impl in the CombinatorialAlgebra class. 

I'd like to see more definitions of the mathematical concepts. (You'll
see a bunch of comments to that effect throughout the review.)

--
File specific comments and questions.

combinat.py

1. CombinatorialObject does no type checking, is available to the
user, but seems to only want to accept lists. But, 

```
C = CombinatorialObject('word')
```

works, except str has no __iter__ attribute.

2. After some operations on CombinatorialObjects, you don't get back a
CombinatorialObject. Example:

```
            sage: c = CombinatorialObject([1,2,3])
            sage: c[0]
            1
            sage: c[1:]
            [2, 3]
            sage: type(_)
            <type 'list'>
```

Is this the desired behaviour?

3. Some classes don't have descriptions: CombinatorialObject,
CombinatorialClass, FilteredCombinatorialClass, ....

4. In FilteredCombinatorialClass, why doesn't list use self.iterator
instead of self.combinatorial_class.iterator? Same code in both.

--

combinatorial_algebra.py

1. I think the definition of __contains__ in the
CombinatorialAlgebraElement class is strange, and doesn't behave the
way I would expect it to.

```
            sage: s = SFASchur(QQ)
            sage: a = s([2,1]) + s([3])
            sage: Partition([2,1]) in a
            True
            sage: Partition([1,1,1]) in a
            False
```

I would have expected

```
            sage: s([2,1]) in a
            True
```

but it's false. 

2. There aren't any examples of constructing CombinatorialAlgebras,
and I think it would be helpful since it seems to be non-trivial.

4. Can the basis of a CombinatorialAlgebra be indexed by any object?
The docstring for _apply_module_morphism(self, x, f) suggests not:

```
            -- f : a function that takes in a partition (basis element)
                   and returns an element of the target domain
```


5. The docstring for _linearize needs to be improved (it mentions only
one of the arguments and not the other). And perhaps it should be
renamed to something like _apply_module_endomorphism. Not sure what
would be best.

--

composition.py

Some functions are not documented adequately in that they are missing
the mathematical definition. For example, the docstring for to_code
only states that the function "Return the composition from its code"
but does not explain what the code of a composition is. 

--

partition.py

1. [1,2,3] is not an integer partition of 6, but Partition([1,2,3])
doesn't complain.

2. So the following is wrong.

```
    sage: Partition([1,2,3]) in Partitions()
    True
```

3. You need to define what you mean by an integer partition,
because I expected this to be False: 

```
    sage: [0] in Partitions()
    True
```

And this too:

```
    sage: [3,1,0] in Partitions()
    True
```

But I can see why this might be useful, so it needs to be well
documented.

4. Partitions_starting is missing Examples.

5. Partitions_starting and Partitions_ending are missing explanations.
And explain which ordering is begin used. Perhaps more descriptive
names?

--

permutations.py

1. More out of curiousity than anything: why do

```
   Permutation([1,2,3])._icondition(2)
   Permutation([3,2,1])._icondition(2)
```

return None as the string?

2. I don't know what i-switch, i-shift, etc. are, and there is no
definition included, so I can't tell if the doctests are doing the
right thing.

3. CyclicPermutations doesn't provide a definition, and the term is
used to mean different things: see
http://en.wikipedia.org/wiki/Cyclic_permutation

--

Made it to ribbon_tableau.py


---

Comment by saliola created at 2008-03-11 02:09:33

Here is the second installment of my review. Most of my comments 
pertain to docstrings, but I did find an error not detected by
the doctests. See the comments for the hall_littlewood.py below.

Expect my next (and last) installment tomorrow.

General comments:

As I mentioned before---but I feel it is important so I'm mentioning
it again---I would like to see more definitions of the mathematical
notions.

Perhaps the fact that you are using caching should be documented.

--

ribbon.py

1. Type-checking missing.

```
sage: r = Ribbon("I am not a ribbon!")
sage: r
I am not a ribbon!
sage: type(r)
<class 'sage.combinat.ribbon.Ribbon_class'>
```


2. A definition of what a ribbon is should be included. And what the
argument of Ribbon can be should be explained.

--

ribbon_tableau.py

1. Type mismatch.

```
sage: RT = RibbonTableux([[8,7,6,5,1,1],[3,3,1]], [2,2,2,1], 3)
sage: r = RT.random()
sage: type(r)
<class 'sage.combinat.combinat.CombinatorialObject'>
sage: type(RT.list()[0])
<type 'list'>
```

I imagine that the type should be RibbonTableau_class.

2. Perhaps a basic __contains__ attribute can be defined using list()?

```
sage: RT = RibbonTableux([[8,7,6,5,1,1],[3,3,1]], [2,2,2,1], 3)
sage: s = [[3,3,1],[[1],[0],[0,2,3,0,0],[0,0,2,0,4],[1,0,0,0],[0,0,3,0,0]]]
sage: s in RT.list()
True
sage: s in RT
<type 'exceptions.NotImplementedError'>
```


--

sf/dual.py

1. Add some examples to expand showing how to use the new alphabet
feature. Add these lines:

```
            sage: a.expand(2,alphabet='y')
            2*y0^3 + 3*y0^2*y1 + 3*y0*y1^2 + 2*y1^3
            sage: a.expand(2,alphabet='x,y')
            2*x^3 + 3*x^2*y + 3*x*y^2 + 2*y^3
```


--

sf/elementary.py

1. dual_basis has been deleted, so some weird things happen in the
documentation.

```
sage: e = SFAElementary(QQ)
sage: e.dual_basis?
Docstring:
           Returns the dual basis of the power-sum basis with ...
```

The examples are for e. 

2. If you use the power sum basis instead of the elementary basis in
the above code, then you get the same docstring (so examples are for
e, not p).

3. Examples for expand should include tests for different alphabets.

```
sage: e([3]).expand(4,alphabet='x,y,z,t')
x*y*z + x*y*t + x*z*t + y*z*t
sage: e([3]).expand(4,alphabet='y')
y0*y1*y2 + y0*y1*y3 + y0*y2*y3 + y1*y2*y3
```


--

sf/hall_littlewood.py

1. The doctests for HallLittlewoodP aren't satisfactory:

```
sage: HLP = HallLittlewoodP(QQ,t=0)
sage: s = SFASchur(HLP.base_ring())
sage: s(HLP([2,1]))
<type 'exceptions.TypeError'>: cannot coerce nonconstant polynomial
```

Also note that the following example---probably due to caching---so
the doctests need to be careful.

```
sage: HLP = HallLittlewoodP(QQ)
sage: s = SFASchur(HLP.base_ring())
sage: s(HLP([2,1]))
(-t^2-t)*s[1, 1, 1] + s[2, 1]

sage: HLP = HallLittlewoodP(QQ,t=0)
sage: s = SFASchur(HLP.base_ring())
sage: s(HLP([2,1]))
s[2, 1]

sage: s(HLP([3,2,1]))
<type 'exceptions.TypeError'>: cannot coerce nonconstant polynomial
```


2. The Hall-Littlewood polynomials P at t = 0 are the Schur functions
and at t = 1 are the monomial symmetric functions, so this should go
into the doctests.

```
sage: HLP = HallLittlewoodP(QQ,t=0)
sage: s = SFASchur(HLP.base_ring())
sage: s(HLP([2,1])) == s([2,1])

sage: HLP = HallLittlewoodP(QQ,t=1)
sage: m = SFAMonomial(HLP.base_ring())
sage: m(HLP([2,2,1])) == m([2,2,1])
```

But these don't work because of the above reason.

3. The Hall-Littlewood polynomials are the Macdonald polynomials at
q=0 (when the root system is of type A), so this should be included as
a doctest for both sets of polynomials.

--

sf/homogeneous.py

1. Include the following examples for expand.

```
sage: h([3]).expand(2,alphabet='y')
y0^3 + y0^2*y1 + y0*y1^2 + y1^3
sage: h([3]).expand(2,alphabet='x,y')
x^3 + x^2*y + x*y^2 + y^3
sage: h([3]).expand(3,alphabet='x,y,z')
x^3 + x^2*y + x*y^2 + y^3 + x^2*z + x*y*z + y^2*z + x*z^2 + y*z^2 + z^3
```


--

sf/jack.py

1. The Jack polynomials J at t = 1 are scalar multiples of Schur
functions, so doctest that:

```
sage: J = JackPolynomialsJ(QQ, t=1)
sage: s = SFASchur(J.base_ring())
sage: p = Partition([3,2,1,1])
sage: s(J(p)) == p.hook_product(1)*s(p)
True
```


2. If the partition has more parts than the number of variables, then
the Jack function is 0:

```
sage: J = JackPolynomialsJ(QQ)
sage: J([3,2,1]).expand(4)
```


3. At t = 2, we get a scalar multiple of a Zonal polynomial.

```
sage: t = 2
sage: J = JackPolynomialsJ(QQ,t=t)
sage: Z = ZonalPolynomials(J.base_ring())
sage: p = Partition([2,2,1])
sage: Z(J(p)) == p.hook_product(t)*Z(p)
True
```


--

sf/macdonald.py

1. The Macdonald polynomials can be expanded in terms of LLT
polynomials.

2. Both c1 and c2 have the same description, but do different things:

```
sage: sage.combinat.sf.macdonald.c1?
Docstring:
        This function returns the qt-Hall scalar product between
        J(part) and P(part).

sage: sage.combinat.sf.macdonald.c2?
Docstring:
        This function returns the qt-Hall scalar product between
        J(part) and P(part).
```


3. MacdonaldPolynomial_*.scalar_qt claims to convert everything to the
power sum basis, but this is not exactly what it does.

4. In the docstring for _to_s (in each function), you mention part2,
but it was confusing at first. So I suggest changing it to "a
partition".

--

sf/monomial.py

1. Add the following to examples of expand.

```
sage: m([2,1]).expand(3,alphabet='z')
z0^2*z1 + z0*z1^2 + z0^2*z2 + z1^2*z2 + z0*z2^2 + z1*z2^2
sage: m([2,1]).expand(3,alphabet='x,y,z')
x^2*y + x*y^2 + x^2*z + y^2*z + x*z^2 + y*z^2
```


--

sf/powersum.py

1. See the comment to sf/elementary.py regarding dual_basis.

2. Add the following to examples of expand.

```
sage: p([7]).expand(4)
x0^7 + x1^7 + x2^7 + x3^7
sage: p([7]).expand(4,alphabet='t')
t0^7 + t1^7 + t2^7 + t3^7
sage: p([7]).expand(4,alphabet='x,y,z,t')
x^7 + y^7 + z^7 + t^7
```


--

sf/sfa.py

1. A bunch of functions are missing docstrings, a few are missing
examples.

2. Change the example for prefix to the following:

```
sage: schur = SFASchur(QQ)
sage: schur([3,2,1])
s([3,2,1])
sage: schur.prefix()
s
```

In the current example, a reader might think that prefix s is the
variable that she chose in the first line.

3. dual_basis: The words "of the power-sum basis" probably should be
removed from the docstring.

--

made it up to sf/skew_tableau.py.


---

Comment by saliola created at 2008-03-11 18:27:12

Here is the final installment of the review.

--

skew_tableau.py

1. The docstring for SkewTableau doesn't explain how to use expr.

2. Personal preference: I don't like that I have to put print in front
of st.pp(). (Same goes for Partition([3,2,1]).ferrers_diagram().)

3. Perhaps the examples for to_word_by_column and to_word_by_row can
include a pp so the user can visually see how the reading is done:

```
sage: st1 = SkewTableau([[None,1],[2,3]])
sage: print st1.pp()
  .  1
  2  3
sage: st1.to_word_by_column()
[1, 3, 2]

sage: st2 = SkewTableau([[None, 2, 4], [None, 3], [1]])
sage: print st2.pp()
  .  2  4
  .  3
  1
sage: st2.to_word_by_column()
[4, 2, 3, 1]
```

And for to_word_by_column and to_word:

```
sage: st1 = SkewTableau([[None,1],[2,3]])
sage: print st1.pp()
  .  1
  2  3
sage: st1.to_word_by_row()
[2, 3, 1]

sage: st2 = SkewTableau([[None, 2, 4], [None, 3], [1]])
sage: print st2.pp()
  .  2  4
  .  3
  1
sage: st2.to_word_by_row()
[1, 3, 2, 4]
```


4. I think it would be nice for every example in this section to have
a pp() statement because people work with SkewTableau and Tableau 
visually. 

5. Future consideration: having __repr__ output the result of pp()
instead, like so:

```
sage: st = SkewTableau([[None, 2, 4], [None, 3], [1]])
sage: st
  .  2  4
  .  3
  1
```

Or at least defining a switch that can be toggled between the two.

--

split_nk.py

1. The docstring for SplitNK is wrong.

--

tableau.py

1. I noticed the following problem with Tableau.shape().

```
sage: t = Tableau([[1],[2,3]]); t
[[1], [2, 3]]
sage: t.shape()
[1, 2]
sage: type(t.shape())
<class 'sage.combinat.partition.Partition_class'>
sage: t.shape() == [1,2]
True
sage: t.shape() in Partitions()
True
sage: [1, 2] in Partitions()
False
```

This can probably by fixed by adding some type checking to Tableau.

2. The documentation should mention whether you are using English or
French style for Tableau. I think that the orientation of the
ferrers_diagram of a partition doesn't match that of pp of a tableau.
(This impression I have is probably related to the missing type 
checking above in Tableau.)


---

Comment by mhansen created at 2008-03-13 19:13:54

## combinat.py

1. I've changed it so that CombinatorialObject only accepts lists.  This required changes (for the better) elsewhere in the code.

2. It is intended for indexing and slicing to not return CombinatorialObjects.  

3. Doctests added

4. I've removed FilteredCombinatorial_class.list


## combinatorial_algebra.py

1.  The definition of contains is intended to be what it is currently.  It is primarily for making some of the underlying implementation cleaner. Also, I don't see how your definition of contains would extend to when s([2,1]) is anything more than a single basis element.  I've added a docstring explaining the behavior.

2. I added an example at the top of the file.

4. Yes, the basis of a CombinatorialAlgebra can be indexed by any combinatorial class.  I've updated the docstring to reflect this.

5. I've changed _linearize to _apply_module_endomorphism, and updated the docstring.


## composition.py

1. I've fixed the docstring for to_code.  Anything else should probably be in a different ticket.


## partition.py

1. Partition() will now check for a valid partition

2. This will now fail.

3. I changed it so that partitions cannot have zeros in them.  However, Partition([3,1,0]) will still give the partition [3, 1].  There was some code in macdonald.py that needed this functionality, but I've changed it.

4 & 5. I've added docstrings fixing these.


## permutation.py

1 & 2.  I've added more documentation for the i-moves.

3. Docstrings changed.


## ribbon.py

1 & 2. Fixed


## ribbon_tableau.py

1. Fixed.

2. Naive __contains__ added.


## sf/dual.py

1. Examples added


## sf/elementary.py

1 & 2.  Docstring fixed in sfa.py

3. Examples added


## sf/hall_littlewood.py

1. I fixed this by making sure all the things stored in the cache are done over the most general ring.

2. Doctests added.

3. Doctests added to macdonald.py


## sf/homogeneous.py

1. Examples added


## sf/jack.py

1. Examples added

2. This is currently the way things are:

```
sage: J = JackPolynomialsJ(QQ)
sage: J([1,1,1,1]).expand(3)
0
sage: J([1,1,1]).expand(2)
0
```


3. I've added this as a doctest.


## sf/macdonald.py

1.  Do you want examples added of this?  I don't have code written that gives the expansion of the Ht's in Haiman, Haglund, and Loehr 2004.

2. Docstrings fixed.

3. Docstrings fixed

4. Docstrings fixed.


## sf/monomial.py

1. Examples added.


## sf/powersum.py

1. Fixed above.

2. Examples added


## sf/sfa.py

1. sfa.py is at 100% now.

2. Example changed.

3. Docstring fixed.


## skew_tableau.py

1. Docstring updated.

2. I've made it so that pp() prints the string now.  I can't remember the last time I used those methods.

```
sage: p = Partition([5,3,1])
sage: p.pp()
*****
***
*
sage: st = SkewTableau([[None, 2, 4], [None, 3], [1]])
sage: st.pp()
  .  2  4
  .  3
  1

```


3. I've added the examples you suggested.

4. I'd make this a separate ticket.

5. This would cause problem with lists of skew tableau among many other things.  I intentionally decided to make the __repr__ what it is because it's a dense representation, reflects the internal data structure, and can by copy and pasted.  Also, changing the repr would break _lots_ of things.


## split_nk.py

1. Docstring fixed.


## tableau.py

1. Tableau([[1],[2,3]]) now gives an invalid tableau error which fixes things.

2. I've added documentation saying that the English convention is used for everything.

```
sage: Tableau([[1,2,4],[3]]).pp()
  1  2  4
  3
sage: Tableau([[1,2,4],[3]]).shape().pp()
***
*
```



---

Comment by saliola created at 2008-03-14 18:55:21

Replying to [comment:8 mhansen]:

> == sf/macdonald.py ==
> 
> 1.  Do you want examples added of this?  I don't have code written that gives the expansion of the Ht's in Haiman, Haglund, and Loehr 2004.

I was mentioning it. I didn't think you had the code written. If you ever do, then it would make for good examples.

> == skew_tableau.py ==
>
> 4. I'd make this a separate ticket. [re: using pp() in examples]

It's something I can do. Perhaps I'll ticket it and add the examples once the patch has been merged.

Some typos:

line 441: +the symmetric group algebra of order n(indexed by permutations n) and

line 729: whererever should be wherever

line 3791: convets should be converts

Great job!


---

Attachment

I've updated the patch to fix the typos.


---

Comment by mabshoff created at 2008-03-14 19:51:59

Merged both patches in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-14 19:51:59

Resolution: fixed
