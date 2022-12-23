# Issue 6018: Confusing behaviour with Dirichlet characters

Issue created by migration from https://trac.sagemath.org/ticket/6018

Original creator: davidloeffler

Original creation time: 2009-05-11 09:18:29

Assignee: craigcitro

Keywords: Dirichlet characters

Funny things happen if you have two Dirichlet groups with the same modulus and the same base ring, but different roots of unity. This can happen if you use base_extend:


```
sage: G = DirichletGroup(10, QQ).base_extend(CyclotomicField(4))
sage: H = DirichletGroup(10, CyclotomicField(4))
```


Now G and H look pretty similar:

```
sage: G
Group of Dirichlet characters of modulus 10 over Cyclotomic Field of order 4 and degree 2
sage: H
Group of Dirichlet characters of modulus 10 over Cyclotomic Field of order 4 and degree 2
```


But they don't compare as equal and the generators of H don't live in G:

```
sage: G == H
False
sage: H.0 in G
False
```


Here G only actually contains those characters which factor through its original base ring, namely QQ. This is probably going to be a bit mystifying for the end-user.

Similar phenomena can make it next to impossible to do arithmetic with characters obtained by base extension, which somehow are second-class citizens:


```
sage: K5 = CyclotomicField(5); K3 = CyclotomicField(3); K30 = CyclotomicField(30)
sage: (DirichletGroup(31, K5).0).base_extend(K30) * (DirichletGroup(31, K3).0).base_extend(K30)
TypeError: unsupported operand parent(s) for '*': 
'Group of Dirichlet characters of modulus 31 over Cyclotomic Field of order 30 and degree 8' and 
'Group of Dirichlet characters of modulus 31 over Cyclotomic Field of order 30 and degree 8'
```


This is a particularly mystifying error for the uninitiated, since it's asserting that it can't find a common parent, but the string representations of the parents it already has are identical.

I can see a couple of solutions:

- Change base_extend for Dirichlet groups to pick a maximal order root of unity in the new base ring, rather than just base-extending the root of unity it already has. This is nice and transparent, but it could be slow in some cases, and it prevents us constructing Dirichlet characters with values in rings where the unit group isn't cyclic or we can't compute a generator (e.g. we'd lose the ability to base extend elements of `DirichletGroup(N, ZZ)` to `DirichletGroup(N, Integers(15))`).

- Change the `_repr_` method for Dirichlet groups so it explicitly prints the root of unity involved. I don't like this idea much.

- Some combination of the above two, with a special class for Dirichlet groups over domains where a unique root of unity of maximal order dividing `euler_phi(N)` doesn't exist or can't be calculated. This might be fiddly to write and maintain.


---

Comment by was created at 2010-01-19 02:55:04

David, I like your analysis of the situation a lot.  I'm going to do what you suggest first.  Regarding performance issues, I think if the user really is worried about that in some case, they can be explicit about the relevant spaces and zeta's.


---

Attachment


---

Comment by was created at 2010-01-19 03:56:48

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-01-19 05:29:06

This looks like a nice clean fix -- my only worry would be that a few subtle choices cause mayhem with some random modular symbols code. William, did you run doctests on the `modular/` directory? 

Also, one potentially silly comment: your fix assumes that the constructor for `DirichletGroup` always chooses a maximal order and an appropriate zeta if one isn't given. While I can't imagine us ever changing that constructor to do anything different, should we either (1) explicitly choose the maximal order or (2) check and/or document this in some way? I think it's unlikely, but should it ever come up, a comment near that line of code pointing someone in the right direction could be a huge help ...


---

Comment by davidloeffler created at 2010-01-20 18:17:54

I am running sage -testall on this patch at the moment. 

The key question, I think, is what we want to happen in the following situation:

```
sage: f = DirichletGroup(17, ZZ).0
sage: f.base_extend(Integers(15))
```

This worked under the old approach, because the parent of the base-extended thing was the Dirichlet group of modulus 17 and `zeta = ZZ(15)(-1)`, of order 2. But I suspect that with this patch it will fail now, with an error message about not being able to compute roots of unity mod 15.

I suggest a further modification which makes the constructor raise a more intelligent error message if the root of unity isn't specified and the base ring is one where we can't do factorisation. If the tests pass I will write such a patch, and give William's patch a positive review conditional on that.


---

Attachment

apply over previous patch


---

Comment by davidloeffler created at 2010-01-20 19:23:41

As promised, here is a second patch. This takes a compromise approach where base_extend tries to calculate a maximal order root of unity in the new base ring if it's an integral domain, but otherwise uses the base-extension. I've added a couple of doctests, including one to illustrate the perils of the `zeta_order` argument.

If someone else can approve the new patch I think we're sorted.


---

Comment by craigcitro created at 2010-01-20 19:32:45

This looks good -- I just have two questions:

 * In the last example, you show that weirdness ensues when the provided `zeta` doesn't have order `zeta_order`. Couldn't we (optionally, with a `check=...` parameter) check this? Having it on by default definitely seems like it'd stop users from shooting themselves in the foot.

 * Is it possible for the call to `base_ring(zeta)` to raise an exception? If so, do we want to catch that and provide a more direct error message, or just let it go?


---

Comment by davidloeffler created at 2010-01-20 21:47:22

The docs state several times that you don't actually need to supply zeta_order, so nobody's going to use the option in the first place unless they've got a pretty good reason to do so. I'd rather not make the code still more complicated! (Would it actually cause that much harm to get rid of the zeta_order argument entirely?)

If base_ring(zeta) raises an exception, the error message will say something like "Unable to coerce foo into bar", and it should be reasonably clear what the problem is. With these patches, the constructor will almost always be getting called without specifying zeta and zeta_order anyway.

David


---

Comment by craigcitro created at 2010-01-20 22:05:10

I'm a big fan of just removing the `zeta_order` argument -- looking at the code, there's no real reason to specify it, and it'll clean up a few statements in the constructor.


---

Attachment


---

Comment by davidloeffler created at 2010-01-20 22:23:42

Here's a third patch that kills zeta_order. All doctests in modular/ pass, I'm running a full test cycle now.


---

Comment by craigcitro created at 2010-01-20 22:51:22

Changing status from needs_review to positive_review.


---

Comment by craigcitro created at 2010-01-20 22:51:22

Two thumbs up! Apply all three.


---

Comment by davidloeffler created at 2010-01-20 23:17:27

apply only this patch


---

Attachment

Hey, why, wait, what happens if you create a zeta such that zeta.multiplicative_order() doesn't work?!

```
sage: a = CDF(CyclotomicField(5).0)
sage: G = DirichletGroup(11, base_ring=a.parent(), zeta=a, zeta_order=5)
sage: G
Group of Dirichlet characters of modulus 11 over Complex Double Field
sage: G.0
[0.309016994375 + 0.951056516295*I]
sage: G.0(2)
0.309016994375 + 0.951056516295*I
```


Please revert getting rid of zeta_order and make that part of another ticket, keeping in mind that you can't exactly do that, since it is important.  The above doctest should be put in that ticket since this problem wouldn't have happened if I had included the above test.


---

Comment by was created at 2010-01-20 23:57:21

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-01-21 09:22:53

OK, so would you be happy with applying just the first two patches? 

David


---

Comment by davidloeffler created at 2010-01-21 09:39:20

On reflection, the issue is surprisingly subtle.

Consider taking a Dirichlet group with values in the integers of a cyclotomic field K, and base_extending to: (1) the complex double field; (2) the residue field of a prime of K.

In case (1), your example shows that we can't expect the constructor of the new group to calculate the order of a given zeta. But case (2) shows that the order of the base-extended zeta might not be the same as the order of the original zeta, and one can easily get nonsense if one assumes this.

Case (1) is actually OK if we don't pass zeta as an argument at all, because we can factor polynomials in CDF. This is more or less what applying Craig's patch and mine will give: zeta_order is still available as an argument, but it's not used by the base extension code, which relies on the base ring supporting *either* polynomial factoring or `multiplicative_order`.


---

Comment by pbruin created at 2015-06-05 12:24:46

Here is a branch implementing a solution which is somewhat like the third option in the ticket description.  The idea is to introduce two different variants of `DirichletGroup`:
- `DirichletGroup(N, base_ring)`, corresponding to the group Hom((*Z*/_N*_Z*)<sup>*</sup>, _R_<sup>*</sup>);
- `DirichletGroup(N, base_ring, zeta[, zeta_order])` corresponding to the group Hom((*Z*/_N*_Z*)<sup>*</sup>, 〈ζ〉).
If _R_ is a domain, we also allow the user to only specify `zeta_order`, in which case the `DirichletGroup` factory tries to compute a suitable `zeta`.

The difference between the two variants is visible from the string representation:

```
sage: R.<x> = PolynomialRing(QQ)
sage: K.<a> = NumberField(x^4 + 1)
sage: DirichletGroup(5, K)
Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1
sage: DirichletGroup(5, K, a)
Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a
```


Because it is no longer mandatory to have a distinguished `zeta`, Dirichlet characters are by default specified by their values instead of a vector of integers modulo the order of `zeta`.  For efficiency reasons, this vector is still used whenever a `zeta` is known (whether it has been specified as in the second syntax above or has been computed at a later stage).

Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.  This is because `zeta` is only computed when needed, and hence factoring cyclotomic polynomials is avoided.  This factoring will still happen when one asks for things like generators or a list of all elements.

David: part of the branch (including some doctests) is based on your patches; I hope you don't mind me adding you as an author.


---

Comment by pbruin created at 2015-06-05 12:45:56

Changing status from needs_work to needs_review.


---

Comment by git created at 2015-06-05 14:14:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-06-22 19:10:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-07-16 08:21:21

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2015-07-17 20:01:33

This is just a detail, but instead of

```
Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a
```

I would prefer

```
Group of Dirichlet characters of modulus 5 with values in the group of order 8 generated by a over Number Field in a with defining polynomial x^4 + 1
```



---

Comment by jdemeyer created at 2015-07-17 20:11:27

Replying to [comment:18 pbruin]:
> Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.

I assume that this is the main motivation for making `zeta` optional, right? I am not really convinced though that this extra complexity is needed...

It is true that `zeta()` for number fields is slow, but that can easily be improved (#18917).


---

Comment by pbruin created at 2015-07-18 10:45:30

Replying to [comment:24 jdemeyer]:
> Replying to [comment:18 pbruin]:
> > Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.
> 
> I assume that this is the main motivation for making `zeta` optional, right? I am not really convinced though that this extra complexity is needed...
This is not really true; it also makes more sense conceptually if one does not have to make a choice of root of unity.  I think the problems related to base extension do deserve to be solved and are at least as important as the speed-up.
> It is true that `zeta()` for number fields is slow, but that can easily be improved (#18917).
It would be great if it could, but when making a speed improvement to `zeta()` in #15486, I found out that it was necessary to avoid calling PARI's `nfinit()`, because it was too slow for the number fields involved.  This unfortunately precludes using PARI's `nfrootsof1()`...


---

Comment by git created at 2015-07-20 16:47:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2015-07-20 16:51:55

Replying to [comment:23 jdemeyer]:
> This is just a detail, but instead of
> {{{
> Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a
> }}}
> I would prefer
> {{{
> Group of Dirichlet characters of modulus 5 with values in the group of order 8 generated by a over Number Field in a with defining polynomial x^4 + 1
> }}}
I took the opportunity to make a more general improvement to the wording; the format is now

```
Group of Dirichlet characters modulo N with values in [the group of order M generated by Z in ]R


---

Comment by git created at 2016-01-22 00:09:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-01-22 08:13:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-01-22 14:55:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-02-25 23:07:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by aly.deines created at 2016-03-25 00:21:19

Changing status from needs_review to positive_review.


---

Comment by aly.deines created at 2016-03-25 00:21:19

Looks good to me.


---

Comment by aly.deines created at 2016-03-25 00:21:19

Changing keywords from "Dirichlet characters" to "Dirichlet characters, days71".


---

Comment by vbraun created at 2016-03-25 17:34:59

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2016-03-25 17:34:59

Doctests fail


---

Comment by vbraun created at 2016-03-25 17:36:11

http://build.sagedev.org/release/builders/%20%20slow%20AIMS%20%20%28Debian%207%2032%20bit%29%20incremental/builds/439/steps/shell_4/logs/stdio


---

Comment by pbruin created at 2016-03-26 09:12:28

Replying to [comment:34 vbraun]:
> http://build.sagedev.org/release/builders/%20%20slow%20AIMS%20%20%28Debian%207%2032%20bit%29%20incremental/builds/439/steps/shell_4/logs/stdio
From the failing doctest in `cachefunc.pyx`, it seems that #15692 is also merged in that branch; I suspect the failure is actually due to that ticket (cf. comment:48:ticket:15692).


---

Comment by pbruin created at 2016-03-26 09:12:28

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2016-03-27 07:44:21

Resolution: fixed
