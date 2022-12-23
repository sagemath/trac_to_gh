# Issue 9342: rank method for elliptic curves over number fields

archive/issues_009342.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  jeremywest\n\nHere is a method to compute the rank of elliptic curves over number fields using Simon 2-descent.\n\n```\ndef rank(self,verbose=0, lim1=5, lim3=50, limtriv=10, maxprob=20, limbigprime=30):\n  r\"\"\"\n\n  This computes the rank of elliptic curves over number fields using Simon's algorithm for two-descent. If the upper and lower bounds given are the same, then we return the rank, otherwise we return the upper and lower bounds.\n\n  INPUT: \n\n  The parameters are those used by simon_two_descent, and are documented there.\n\n  OUTPUT:\n\n  If the upper and lower bounds given by Simon two-descent are the same, then the rank has been uniquely identified and we return this. Otherwise, we return the upper and lower bounds with a warning that these are not the same.\n\n  Note: For non-quadratic number fields, this code does return, but it takes a long time.\n\n  EXAMPLES:\n\n  sage: K.<a> = NumberField(x^2 + 23, 'a')\n\n  sage: E = EllipticCurve(K, '37')\n\n  sage: E == loads(dumps(E))\n\n  True\n\n  sage: E.rank()\n\n  2\n\n  Here is a curve with two-torsion, so here the algorithm gives bounds on the rank:\n\n  sage: Qrt5.<rt5>=NumberField(x^2-5)\n  \n  sage: E=EllipticCurve([0,5-rt5,0,rt5,0])\n  \n  sage: E.rank()\n  \n  Lower and upper bounds differ!\n  \n  Lower bound being returned\n\n  1\n\n  IMPLEMENTATION:\n\n  Uses Denis Simon's GP/PARI scripts from  \\url{http://www.math.unicaen.fr/~simon/}.\n\n  \"\"\"\n\n  simon_output=self.simon_two_descent(verbose=verbose,lim1=lim1,lim3=lim3,limtriv=limtriv,maxprob=maxprob,limbigprime=limbigprime)\n  if simon_output[0]==simon_output[1]:\n    return simon_output[0]\n  print \"Lower and upper bounds differ!\"\n  print \"Lower bound being returned\"\n  return simon_output[0]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9342\n\n",
    "created_at": "2010-06-26T00:03:20Z",
    "labels": [
        "elliptic curves",
        "minor",
        "enhancement"
    ],
    "title": "rank method for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9342",
    "user": "ljpk"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/9342





---

archive/issue_comments_088258.json:
```json
{
    "body": "Applies to 4.4.4",
    "created_at": "2010-06-26T00:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88258",
    "user": "cremona"
}
```

Applies to 4.4.4



---

archive/issue_comments_088259.json:
```json
{
    "body": "Attachment\n\nI converted Lloyd's code into a patch.\n\nThe ticket description can now be abbreviated!",
    "created_at": "2010-06-26T00:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88259",
    "user": "cremona"
}
```

Attachment

I converted Lloyd's code into a patch.

The ticket description can now be abbreviated!



---

archive/issue_comments_088260.json:
```json
{
    "body": "replaces the previous patch",
    "created_at": "2010-06-29T05:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88260",
    "user": "aly.deines"
}
```

replaces the previous patch



---

archive/issue_comments_088261.json:
```json
{
    "body": "Attachment\n\nThis contains rank, rank_bounds, and gens all from simon_two_descent.  We also implemented caching in simon_two_descent.",
    "created_at": "2010-06-29T05:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88261",
    "user": "aly.deines"
}
```

Attachment

This contains rank, rank_bounds, and gens all from simon_two_descent.  We also implemented caching in simon_two_descent.



---

archive/issue_comments_088262.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T05:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88262",
    "user": "aly.deines"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088263.json:
```json
{
    "body": "This is very nice -- good stuff! I have only a few tiny criticisms, mostly to do with docstring formatting.\n\n(1)\n\n```\n1347    def rank_bounds(self,verbose=0, lim1=5, lim3=50, limtriv=10, maxprob=20, limbigprime=30): \n1348        r\"\"\" \n1349        Returns the lower and upper bounds using simon_two_descent.  The results of simon_two_descent are cached. \n```\n\nThere is a ReST syntax for cross-referencing between docstrings, which should be used here:\n`... using :meth:`~simon_two_descent`. The results ...`.\n\n(2)\n\n```\n1435        .. NOTE:: \n1436 \n1437           Note: For non-quadratic number fields, this code does \n1438           return, but it takes a long time.\n```\n\nThe output is \"Note: Note: For ...\". The second \"Note\" should go. This mistake is made in two of the three new docstrings.\n\n(2) If it does terminate for non-quadratic fields, but it takes a long time, then throw in an example and flag it as long:\n\n```\nsage: EllipticCurve('11a').base_extend(NumberField(x^3 - 3,'c')).rank() # long time\n0\n```\n\nThis example only takes about 15 seconds on my machine.\n\n(3)\n\n```\n1459        IMPLEMENTATION: \n1460 \n1461        Uses Denis Simon's GP/PARI scripts from \n1462        \\url{http://www.math.unicaen.fr/~simon/}. \n```\n\nThis should just be \"` from http://www.math.unicaen.fr/~simon/.`\" The ReST documentation parser is clever enough to spot URL's without help, and the LaTeX-style syntax you've used just gets copied into the output. This mistake is in all three of the new docstrings.",
    "created_at": "2010-06-29T13:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88263",
    "user": "davidloeffler"
}
```

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

archive/issue_comments_088264.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-29T13:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88264",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088265.json:
```json
{
    "body": "apply over trac_9342-rank.2.patch",
    "created_at": "2010-06-29T14:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88265",
    "user": "davidloeffler"
}
```

apply over trac_9342-rank.2.patch



---

archive/issue_comments_088266.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-29T14:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88266",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088267.json:
```json
{
    "body": "Attachment\n\nPerhaps I was being a bit harsh: most of the ReST formatting errors were already present in the docstring of `simon_two_descent`, so they're not your fault. I've done a small patch which fixes these, and also slightly changes the behaviour of `rank` when 2-descent doesn't precisely nail the rank down (in the original version, it didn't report the upper and lower bounds in the error message, although the docstring claimed it did). \n\nIf you're happy with my changes, then feel free to set this to \"positive review\".",
    "created_at": "2010-06-29T14:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88267",
    "user": "davidloeffler"
}
```

Attachment

Perhaps I was being a bit harsh: most of the ReST formatting errors were already present in the docstring of `simon_two_descent`, so they're not your fault. I've done a small patch which fixes these, and also slightly changes the behaviour of `rank` when 2-descent doesn't precisely nail the rank down (in the original version, it didn't report the upper and lower bounds in the error message, although the docstring claimed it did). 

If you're happy with my changes, then feel free to set this to "positive review".



---

archive/issue_comments_088268.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T16:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88268",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088269.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9342#issuecomment-88269",
    "user": "mpatel"
}
```

Resolution: fixed
