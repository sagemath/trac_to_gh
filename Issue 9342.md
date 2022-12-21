# Issue 9342: rank method for elliptic curves over number fields

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2010-06-26 00:03:20

Assignee: cremona

CC:  jeremywest

Here is a method to compute the rank of elliptic curves over number fields using Simon 2-descent.

```
def rank(self,verbose=0, lim1=5, lim3=50, limtriv=10, maxprob=20, limbigprime=30):
  r"""

  This computes the rank of elliptic curves over number fields using Simon's algorithm for two-descent. If the upper and lower bounds given are the same, then we return the rank, otherwise we return the upper and lower bounds.

  INPUT: 

  The parameters are those used by simon_two_descent, and are documented there.

  OUTPUT:

  If the upper and lower bounds given by Simon two-descent are the same, then the rank has been uniquely identified and we return this. Otherwise, we return the upper and lower bounds with a warning that these are not the same.

  Note: For non-quadratic number fields, this code does return, but it takes a long time.

  EXAMPLES:

  sage: K.<a> = NumberField(x^2 + 23, 'a')

  sage: E = EllipticCurve(K, '37')

  sage: E == loads(dumps(E))

  True

  sage: E.rank()

  2

  Here is a curve with two-torsion, so here the algorithm gives bounds on the rank:

  sage: Qrt5.<rt5>=NumberField(x^2-5)
  
  sage: E=EllipticCurve([0,5-rt5,0,rt5,0])
  
  sage: E.rank()
  
  Lower and upper bounds differ!
  
  Lower bound being returned

  1

  IMPLEMENTATION:

  Uses Denis Simon's GP/PARI scripts from  \url{http://www.math.unicaen.fr/~simon/}.

  """

  simon_output=self.simon_two_descent(verbose=verbose,lim1=lim1,lim3=lim3,limtriv=limtriv,maxprob=maxprob,limbigprime=limbigprime)
  if simon_output[0]==simon_output[1]:
    return simon_output[0]
  print "Lower and upper bounds differ!"
  print "Lower bound being returned"
  return simon_output[0]
```



---

Comment by cremona created at 2010-06-26 00:40:02

Applies to 4.4.4


---

Attachment

I converted Lloyd's code into a patch.

The ticket description can now be abbreviated!


---

Comment by aly.deines created at 2010-06-29 05:43:23

replaces the previous patch


---

Attachment

This contains rank, rank_bounds, and gens all from simon_two_descent.  We also implemented caching in simon_two_descent.


---

Comment by aly.deines created at 2010-06-29 05:44:49

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-06-29 13:28:39

This is very nice -- good stuff! I have only a few tiny criticisms, mostly to do with docstring formatting.

(1)

```
1347    def rank_bounds(self,verbose=0, lim1=5, lim3=50, limtriv=10, maxprob=20, limbigprime=30): 
1348        r""" 
1349        Returns the lower and upper bounds using simon_two_descent.  The results of simon_two_descent are cached. 
```

There is a ReST syntax for cross-referencing between docstrings, which should be used here:
`... using :meth:`~simon_two_descent`. The results ...`.

(2)

```
1435        .. NOTE:: 
1436 
1437           Note: For non-quadratic number fields, this code does 
1438           return, but it takes a long time.
```

The output is "Note: Note: For ...". The second "Note" should go. This mistake is made in two of the three new docstrings.

(2) If it does terminate for non-quadratic fields, but it takes a long time, then throw in an example and flag it as long:

```
sage: EllipticCurve('11a').base_extend(NumberField(x^3 - 3,'c')).rank() # long time
0
```

This example only takes about 15 seconds on my machine.

(3)

```
1459        IMPLEMENTATION: 
1460 
1461        Uses Denis Simon's GP/PARI scripts from 
1462        \url{http://www.math.unicaen.fr/~simon/}. 
```

This should just be "` from http://www.math.unicaen.fr/~simon/.`" The ReST documentation parser is clever enough to spot URL's without help, and the LaTeX-style syntax you've used just gets copied into the output. This mistake is in all three of the new docstrings.


---

Comment by davidloeffler created at 2010-06-29 13:28:39

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-06-29 14:02:55

apply over trac_9342-rank.2.patch


---

Comment by davidloeffler created at 2010-06-29 14:08:52

Changing status from needs_work to needs_review.


---

Attachment

Perhaps I was being a bit harsh: most of the ReST formatting errors were already present in the docstring of `simon_two_descent`, so they're not your fault. I've done a small patch which fixes these, and also slightly changes the behaviour of `rank` when 2-descent doesn't precisely nail the rank down (in the original version, it didn't report the upper and lower bounds in the error message, although the docstring claimed it did). 

If you're happy with my changes, then feel free to set this to "positive review".


---

Comment by aly.deines created at 2010-06-29 16:39:07

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:18:37

Resolution: fixed
