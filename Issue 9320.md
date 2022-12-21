# Issue 9320: Implement root numbers for elliptic curves over number fields

Issue created by migration from Trac.

Original creator: arminstraub

Original creation time: 2010-06-23 22:14:38

Assignee: cremona

CC:  was cturner beankao pbruin cremona

Keywords: root number

Root numbers for elliptic curves are currently only implemented via Pari (pari(E).ellrootno()) and only over the rational numbers.

We (Tim Dokchitser's group at Sage Days 22) intend to add the possibility to compute local and global root numbers for elliptic curves over number fields.  A first patch may not fully implement the case of additive reduction over primes dividing 2 or 3.


---

Comment by arminstraub created at 2010-08-10 11:20:14

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-11 19:50:09

I don't think it is possible to review this until the ticket it depends on (#9334) which needs work has been fixed.


---

Attachment

requires #9334 and #9684


---

Comment by arminstraub created at 2010-08-13 00:33:52

Adapted the patch to reflect the renaming of "tidy" to "reduce" following #9684.


---

Comment by davidloeffler created at 2011-12-30 17:59:19

Rebased to 4.8.alpha5


---

Comment by davidloeffler created at 2011-12-30 18:09:53

Changing status from needs_review to needs_work.


---

Attachment

Ticket #9334 has been merged, so this is now ready for review. Sadly it fails to apply, due to a trivial conflict with #11749. I've uploaded a rebased patch, and checked that all doctests in sage/schemes/elliptic_curves pass with this applied. 

However, some (trivial but tedious) work is needed fixing the ReST formatting of the docstrings -- the indentation is all over the place, and :: should only be used to introduce example code blocks.


---

Attachment

docstrings improved


---

Comment by cturner created at 2012-01-13 14:16:37

I have tried to clean this up, but I'm not very experienced so I may have made some mistakes or missed something - could someone please have a look and help me to get it right?


---

Comment by chapoton created at 2013-08-22 17:37:20

apply only 9320_root_numbers-rebase_docscleaned.patch


---

Comment by chapoton created at 2013-08-22 17:41:11

apply only 9320_root_numbers-rebase_docscleaned.patch


---

Comment by chapoton created at 2013-08-22 17:47:35

seems to apply and pass all tests on 5.12.beta2

needs work to put coverage to 100%


---

Comment by chapoton created at 2013-12-06 20:51:42

this one just needs a little more doc (three functions need doctests)


---

Comment by chapoton created at 2014-03-15 09:39:00

Here is a git branch
----
New commits:


---

Comment by git created at 2014-03-16 13:42:04

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-03-16 13:43:41

It would be good if some expert of elliptic curve could provide correct doctests for the local root numbers at primes 2 and 3. Could you have a look, please ?


---

Comment by cremona created at 2014-03-18 09:58:20

I suggest that a good source of examples would be elliptic curves over number fields where we know the associated modular form, since the root number at a bad prime should match the Atkin-Lehner eigenvalue.  (The alternative would be to compue a whole lot of examples with Magma, but that would make me uncomfortable;  nevertheless we should of course check that our results are compatible with Magma.)

There is no issue when the primes have multiplicative reduction, since then the root number is very easy being minus E.ap, i.e. depends only on whether the number of points on the reduction is p+1 or p-1 (of course "p" means Norm(p) in the number field case).  It's the case of additive reduction at primes dividing 2 or 3 which are harder.

Here is one taken from my thesis (see http://www.numdam.org/numdam-bin/search?h=nc&id=CM_1984__51_3_275_0&format=complete):

```
K.<i>=QuadraticField(-1)
E=EllipticCurve([1+i, 1+i, 0,i,0])
P2=K.ideal(i+i)
E.root_number(P2)
-1
```

which I checked with Magma.  The conductor here is `P2^2 * P41`.

Is this what you want?  How many examples do you need?


Tables of elliptic curves over number fields do exist, and were in fact one of the topics of last week's Curves and Automorphic Forms workshop in Arizona.


---

Comment by chapoton created at 2014-03-18 11:07:36

One example would be enough, I think if it is bad at both 2 and 3. Maybe one can just use the one above as "indirect doctest" ?

Do you really mean `K.ideal(i+i)` ?


---

Comment by cremona created at 2014-03-18 13:26:17

Replying to [comment:14 chapoton]:
> One example would be enough, I think if it is bad at both 2 and 3. Maybe one can just use the one above as "indirect doctest" ?
> 
I'll find another example at 3.  I don't know the code but I expect that it also depends on factors such as the ramification degree of the prime, so I'll give an example over Q(sqrt-3) with additive reduction at 3.  Wait for it...

> Do you really mean `K.ideal(i+i)` ?
Yes


---

Comment by cremona created at 2014-03-18 13:41:03

An example which is additive at 3:

```
sage: K.<r> = NumberField(x^2-x+1)
sage: E = EllipticCurve([r-1,r,1,r-1,-1])
sage: P3 = K.ideal(2*r-1)
sage: assert P3.is_prime() and P3.norm()==3
sage: assert E.has_additive_reduction(P3)
sage: assert P.root_number(P3)==1 ## not implemented
```

Here the value is taken from page 115 of my thesis, and agrees with Magma's value.

For additional testing we could put in an 'algorithm' parameter which could be 'magma' and then (of course) only work when Magma is installed, so you could have optional doctests conditional on Magma of the form

```
assert E.root_number(P) == E.root_number(P, algorithm='magma')
```



---

Comment by git created at 2014-03-18 15:51:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-03-18 15:57:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-03-18 15:58:03

Thanks a lot for the examples. I have done what I could for this code, but there is now a failing doctest for the example you provided which has additive reduction at 2.

And I had to replace `K.ideal(i+i)` by `K.ideal(1+i)` ...

Not being in my field of expertise, I will now leave this ticket in more able hands.


---

Comment by wuthrich created at 2014-03-31 13:44:46

I had a quick look at this and there are indeed major issues with the local root number at places above 2 when the reduction is additive, potentially good. That is in the function `_root_number_local_2` in `ell_number_field.py`.

With the current commit above we get an error for


```
sage: K.<i> = QuadraticField(-1)
sage: E = EllipticCurve([1+i, 1+i, 0, i, 0])
sage: P2 = K.ideal(1+i)
sage: E.root_number(P2)
```


because line 1966 tries to create and extension with a reducible polynomial `K2 = K.extension(t**2+E.a2()*t+E.a4(), 'a2')`. I guess - but it would take me some time to read the sources - that K2 should just be K in this case.

However there are other issues. For instance
  

```
sage: E = EllipticCurve([1+i,0,0,0,i])
sage: E._root_number_local_2(P2)
```


goes "bang".

I would think the code without the very bad case at places above 2 is ok and that could already go in. So I see two possible futures for this ticket:

1. Someone fixes these issues above 2 or

2. We raise an `NotImplementedError` if the reduction is additive and potentially good at a place above 2 and open a new ticket for fixing the problem.

I can help with 2), but I won't have time to do 1). But maybe there is someone out there who would.


---

Comment by cremona created at 2014-03-31 13:50:55

It all started a long time ago, at the Sage Days & summer school at MSRI.  Perhaps we good get Tim Dokchitser, who led the original project (and who developed the background theory, I think) involved?  He works mainly in Magma, but back in 2010 he certainly was involved with this.


---

Comment by git created at 2015-07-09 12:42:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-07-09 13:26:39

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-10-28 20:06:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by wuthrich created at 2015-10-29 09:50:04

Sorry, I reverted that. Tim did not touch much of the code himself as far as I can remember that long long time ago in Berkley. I doubt he would want to vouch for this code by himself...


---

Comment by jdemeyer created at 2015-10-29 09:50:47

Instead of reverting, at least fix it.


---

Comment by wuthrich created at 2015-10-29 09:52:00

What is the issue ? Why can't you leave the original string in there ?


---

Comment by jdemeyer created at 2015-10-29 10:02:35

Because "Tim Dokchitser and group (Sage Days 22)" isn't an actual person.


---

Comment by wuthrich created at 2015-10-29 10:09:13

But it was a collaborative effort. The wiki for the sage days lists the participants in this group as "Armin, Charlie, Hatice, Christ, Lola, Robert Miller, Thilina, M. Tip, Robert Bradshaw " I am not sure who actually did the coding and I don't remember all full names. So the original string was probably the closest to who the author was. Otherwise set it to Armin Straub, who did the original uploading onto this trac ticket.


---

Comment by chapoton created at 2015-10-29 20:26:28

there are some failing doctests..


---

Comment by git created at 2016-03-01 11:03:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-05 17:59:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-05 18:14:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-03-06 13:06:29

Could some expert in elliptic curves have a look at the last failing doctest, please ?


---

Comment by wuthrich created at 2016-03-07 16:04:55

I can simply repeat my comment:20 above. This is a genuine bug. 

My favourite solution is still to raise non implemented warnings for the cases this code does not do currently.

Before accepting this ticket, the reviewer will have to do lots of comparison with magma. The code in magma will have plenty less bugs than this one as the Dokchitsers have worked a lot on that code.


---

Comment by git created at 2016-03-10 20:53:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-03-10 20:56:28

I tried to fix the problem, but only with partial success. It seems that at some point
the code assumes vanishing of coeff a1 in long Weierstrass equation, and I cannot see why.


---

Comment by git created at 2016-07-29 18:42:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-14 12:13:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-01-04 15:58:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2019-01-05 09:49:40

Merged with 8.6.beta1
----
New commits:


---

Comment by git created at 2019-01-09 09:10:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2019-01-09 09:20:32

After merging with 8.6.beta1 I ran the tests, and there is one failure in line 2294 of ell_number_field where a local root number at a ramified prime above 2 where there is additive reduction is computed incorrectly.

I checked with Magma that -1 is the correct value.  This curve is http://beta.lmfdb.org/EllipticCurve/2.0.4.1/164.2/a/2 and has associated Bianchi newform http://beta.lmfdb.org/ModularForm/GL2/ImaginaryQuadratic/2.0.4.1/164.2/a/ where you can see that the Atkin-Lehner eigenvalue at 1+i is -1, giving a second independent evaluation.
