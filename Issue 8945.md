# Issue 8945: Cremona labels messed up

Issue created by migration from https://trac.sagemath.org/ticket/8945

Original creator: davidloeffler

Original creation time: 2010-05-10 17:01:33

Assignee: craigcitro

CC:  was cremona

It's possible to create elliptic curves over QQ by giving a Cremona label, e.g. `EllipticCurve('225a1')`, or a short form which gives you the optimal curve, `EllipticCurve('225a')`. It's also possible to create weight 2 newforms using a similar constructor, `Newform('225a')` etc.

The problem is that they don't match! For instance:

```
sage: EllipticCurve('225c').aplist(50)                              
[-1, 0, 0, 0, 4, 2, 2, 4, 0, 2, 0, 10, -10, -4, 8]
sage: f = Newform('225c', names='a'); [f[p] for p in prime_range(50)]
[0, 0, 0, -5, 0, -5, 0, -1, 0, 0, -7, 10, 0, -5, 0]
```


This is pretty embarrasing, particularly because abelian varieties go with newforms rather than with elliptic curves, meaning that `AbelianVariety('225c')` should be the same object as `EllipticCurve('225c')` but it isn't!


---

Comment by cremona created at 2010-05-10 17:51:08

I can explain how this arises.  The labelling in the e.c. tables corresponds with the order the newforms were found --once.  (There's more about this in my Berlin ANTS account).  That order changed over time, particularly for conductors up to 450, since I was developing the algorithm as I went along, and it was just too expensive in those days (late 1980s!) to rerun everything when I changed strategy.

So, if it is important to have the labels match (which it surely is), and if the so-called Cremona labels are set in stone according to the 1992 book, then the only way out is to have hard-coded into the current newforms code the order in the tables (for rational newforms only).  Yes, that is ugly.  But the alternative is to cause confusion in all the literature which has referred to curves by their Cremona label for 18 tears now...

I already have such hard-coding in my own code so that when I recompute all the curves of conductor up to 500 they get reordered into the order in which I first found them, so that the labels are right.  Sage could use this permutation data (which would save anyone having to do it again, which is a real boon, believe me).  See the file curvesort.cc in eclib*/src/g0n.  This contains the following functions:

    1. booknumber(int level, int form_number) -->  book's form number (counting form 1)
    1. booknumber0(level, form_number)  same with numbers starting at 0

The good news is that the permutation is he identity for level <56 or > 450.  But that is true for comparing two version of my own program;  I don't know the Sage order of newforms.


---

Comment by davidloeffler created at 2010-05-12 13:20:44

It looks like eclib supports two different sorting conventions: the "old" convention where curves are sorted first by their local root numbers at the bad primes, and then by their a_p's in the order 0,1,-1,2,-2,..., and the "new" convention which is a straight numerical sort on the a_p's. 

The "old" eclib order (with ad-hoc modifications for 46 <= N <= 450) seems to be what's used in the tables supplied with Sage, and hence it's what the `EllipticCurve('225a1')` constructor picks up. The "new" eclib order seems to be what Sage is using. So the two really are different for infinitely many N (the permutation for N = 9999 seems to be [3, 6, 0, 8, 5, 11, 10, 9, 4, 2, 7, 1, 12]). 

We could change Sage's system to correspond to eclib's old one, but that would only really work for Gamma0(N), since I don't know a good way of calculating the local root numbers in general -- we'd probably have to keep the old sort order for Gamma1 and GammaH spaces and spaces with character.

Maybe it's best to not attempt to fix this issue, and to live with the fact that the conventions don't necessarily agree.


---

Comment by cremona created at 2010-05-12 14:47:38

You are right.  I changed the ordering explicitly at William's request, to agree with what he is using for more general modular forms.  But the rule of the game is that after publishing tables I do not want to change all the labels of all the curves with hindsight.  So the database labelling is "old".

Also in eclib src/g0n/newforms.cc you see

```
  if((n1ds>1)&&(modulus<130000)) // reorder into old order
    {
      if(verbose) 
	{
	  cout<<"Reordering newforms into old order as N<130000"<<endl;
	  //	  cout<<"Before sorting:\n"; display();
	}
      sort(1);
      if(verbose) 
	{
	  //	  cout<<"After sorting:\n"; display();
	}
```

showing that the output of eclib itself uses old ordering for N<130,000 (only).


---

Comment by cremona created at 2010-10-03 17:29:23

One way of dealing with this would be as follows:  for levels up to 130000 and weight 2 newforms for Gamma_0(N), the decomposition function could sort the forms according to the sorting of the curves in the database.  This would be a real pain to do (though only once!) since -- as I pointed out earlier -- there is no simple way to do this for levels < 450 or so.  All one needs is a slave to work out around 400 cases like this:

```
sage: [EllipticCurve('225'+l).aplist(20) for l in 'abcde']
[[0, 0, 0, -5, 0, -5, 0, -1], [0, 0, 0, 5, 0, 5, 0, -1], [-1, 0, 0, 0, 4, 2, 2, 4], [2, 0, 0, 3, -2, -1, 2, -5], [-2, 0, 0, -3, -2, 1, -2, -5]]
sage: [[Newform('225'+l,names='a')[p] for p in prime_range(20)] for l in 'cdbea']
[[0, 0, 0, -5, 0, -5, 0, -1], [0, 0, 0, 5, 0, 5, 0, -1], [-1, 0, 0, 0, 4, 2, 2, 4], [2, 0, 0, 3, -2, -1, 2, -5], [-2, 0, 0, -3, -2, 1, -2, -5]]
```

so as far as level 225 is concerned, 'cdbea' does the trick.

In eclib's src/g0n/curvesort.cc there are lots of lines like this:

```
case 222: return EDACB[form]; break;
```

where

```
int EDACB[] = {4,3,0,2,1};
```

which I tediously worked out by hand around 20 years ago...


---

Comment by cremona created at 2015-08-24 09:54:50

To quote from David L above:

   Maybe it's best to not attempt to fix this issue, and to live with the fact that the conventions  don't necessarily agree.


Personally, I am more concerned with getting the curve/newform labels in the lmfdb to match than to also do the same (but differently) in Sage.  Sorry -- you can write "to do" but that will not make *me* do it!


---

Comment by jakobkroeker created at 2015-08-24 17:16:31

> Sorry -- you can write "to do" but that will not make *me* do it!

I just used the 'todo'-stopgap label to mark tickets which describes issues leading 
to potential silent wrong results. 

Since I checked about one third of open tickets, I estimate
that currently there are about 80-100 known bugs which silently lead to wrong results.
