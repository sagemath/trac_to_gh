# Issue 9787: The coordinates appearing in the output of variety(L) should be easier to access

Issue created by migration from https://trac.sagemath.org/ticket/9788

Original creator: mmezzarobba

Original creation time: 2010-08-23 13:28:40

Assignee: malb

CC:  gagern

When computing the variety over an extension field L of a zero-dimensional ideal of some polynomial ring K[vars], each point of the variety is returned as a dictionary whose keys are generators of L[vars]. It would be more practical to have the keys be either generators of K[vars] or plain strings.


```
sage: R.<x,y> = QQ[]
sage: J = (x+y, x^2+y^2-1)*R
sage: V = J.variety(QQbar); V
[{y: -0.7071067811865475?, x: 0.7071067811865475?}, {y: 0.7071067811865475?, x: -0.7071067811865475?}]
sage: V[0][x]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/data/sage-4.5.1/<ipython console> in <module>()

KeyError: x
sage: V[0]['x']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/data/sage-4.5.1/<ipython console> in <module>()

KeyError: 'x'
sage: V[0][QQbar['x,y'].0]
0.7071067811865475?
```



---

Comment by gagern created at 2015-01-23 13:49:04

As [discussed on sage-devel](https://groups.google.com/forum/#!topic/sage-devel/oAj6Ja-62HA), another alternative would be to use whatever category makes sense for keys, but to coerce keys to that category using a custom class derived from `dict`. Compared to using wither generators of K[vars] or strings this would have the huge advantage of not breaking backwards compatibility, since lookup using generators of L[vars] would work just as well.


---

Comment by mmezzarobba created at 2015-01-23 14:28:07

Replying to [comment:5 gagern]:
> As [discussed on sage-devel](https://groups.google.com/forum/#!topic/sage-devel/oAj6Ja-62HA), another alternative would be to use whatever category makes sense for keys, but to coerce keys to that category using a custom class derived from `dict`. Compared to using wither generators of K[vars] or strings this would have the huge advantage of not breaking backwards compatibility, since lookup using generators of L[vars] would work just as well.

Yes, this is clearly a better solution!


---

Comment by gagern created at 2015-01-31 21:32:43

Changing status from new to needs_review.


---

Comment by gagern created at 2015-01-31 21:32:43

OK, here is an implementation for this.

The object returned from the `variety()` call no longer is a sequence, since converting to sequence will cause some argument misalignment and therefore make all solutions come up as empty dicts. One alternative would be making the key conversion function a named argument, perhaps even guessing it from the type of the keys provided so far. Another alternative would be introducing a category for conversion dicts, one for every possible conversion function. But I doubt either of these is neccessary, since I doubt anyone really relies on receiving a Sequence out of this.

Should `BooleanPolynomialIdeal.variety()` in `pbori.pyx` behave the same? Should other code make use of this as well, e.g. the symbolic `solve` function with `solutions_dict=True`? Should these things be handled in separate tickets?
----
New commits:


---

Comment by git created at 2015-02-01 15:48:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmezzarobba created at 2015-02-02 09:13:28

Replying to [comment:9 gagern]:
> OK, here is an implementation for this.

As you implemented it as a generic programming utility rather than as part of the parent/element/coercion/... infrastructure, perhaps it should go in `sage.misc` rather than `sage.structure`?

> The object returned from the `variety()` call no longer is a sequence, since converting to sequence will cause some argument misalignment and therefore make all solutions come up as empty dicts. One alternative would be making the key conversion function a named argument, perhaps even guessing it from the type of the keys provided so far. Another alternative would be introducing a category for conversion dicts, one for every possible conversion function. But I doubt either of these is neccessary, since I doubt anyone really relies on receiving a Sequence out of this.

I agree, but I'd prefer to get a second opinion.

> Should `BooleanPolynomialIdeal.variety()` in `pbori.pyx` behave the same? Should other code make use of this as well, e.g. the symbolic `solve` function with `solutions_dict=True`?

I'd say yes.

> Should these things be handled in separate tickets?

If that's easy to do, doing at least some of what you suggest here would give `KeyConvertingDict` a bit of field-testing before it is merged...


---

Comment by git created at 2015-02-08 17:53:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by gagern created at 2015-02-08 18:41:52

Replying to [comment:11 mmezzarobba]:
> As you implemented it as a generic programming utility rather than as part of the parent/element/coercion/... infrastructure, perhaps it should go in `sage.misc` rather than `sage.structure`?

Fine with me. Did so.

> I agree, but I'd prefer to get a second opinion.

So this ticket here will remain waiting for review until then? Should I ask someone specific about this?

> > Should `BooleanPolynomialIdeal.variety()` in `pbori.pyx` behave the same?

Did so now.

> > Should other code make use of this as well, e.g. the symbolic `solve` function with `solutions_dict=True`?

I get the feeling that if the result accepts various types to identify variables, the argument which tells `solve` what variable(s) to solve for should be auto-coerced as well. That would be a bigger and possibly more controversial change, and I don't want that in the way of this ticket here.


---

Comment by mmezzarobba created at 2015-02-08 18:51:31

Replying to [comment:13 gagern]:
> > I agree, but I'd prefer to get a second opinion.
> 
> So this ticket here will remain waiting for review until then? Should I ask someone specific about this?

I was hoping that someone would jump in and tell us what they think. At the moment I don't have time to look at your last changes, but if no one has complained when I do... well, no, I don't plan to delay the review forever.


---

Comment by mmezzarobba created at 2015-02-09 09:09:46


```
**********************************************************************
File "src/sage/rings/polynomial/multi_polynomial_sequence.py", line 1348, in sage.rings.polynomial.multi_polynomial_sequence.PolynomialSequence_gf2.solve
Failed example:
    sol = S.solve(); sol                       # random
Exception raised:
    Traceback (most recent call last):
      File "/home/marc/co/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 488, in _run
        self.compile_and_execute(example, compiler, test.globs)
      File "/home/marc/co/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 850, in compile_and_execute
        exec(compiled, globs)
      File "<doctest sage.rings.polynomial.multi_polynomial_sequence.PolynomialSequence_gf2.solve[2]>", line 1, in <module>
        sol = S.solve(); sol                       # random
      File "/home/marc/co/sage/local/lib/python2.7/site-packages/sage/rings/polynomial/multi_polynomial_sequence.py", line 1462, in solve
        sol[ r.lm() ] = r.subs(sol).constant_coefficient()
      File "/home/marc/co/sage/local/lib/python2.7/site-packages/sage/misc/converting_dict.py", line 139, in __setitem__
        key = self.key_conversion_function(key)
      File "sage/structure/parent.pyx", line 1094, in sage.structure.parent.Parent.__call__ (build/cythonized/sage/structure/parent.c:9480)
        return mor._call_(x)
      File "sage/structure/coerce_maps.pyx", line 110, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (build/cythonized/sage/structure/coerce_maps.c:4374)
        raise
      File "sage/structure/coerce_maps.pyx", line 105, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (build/cythonized/sage/structure/coerce_maps.c:4272)
        return C._element_constructor(x)
      File "sage/rings/polynomial/pbori.pyx", line 908, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (build/cythonized/sage/rings/polynomial/pbori.cpp:9793)
        raise TypeError, "cannot convert monomial %s to %s: %s"%(other,self,msg)
    TypeError: cannot convert monomial x to Boolean PolynomialRing in z, y: name x not defined
**********************************************************************
```



---

Comment by mmezzarobba created at 2015-02-09 14:42:09

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-04-20 07:17:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by gagern created at 2015-04-20 07:22:22

Changing status from needs_work to needs_review.


---

Comment by gagern created at 2015-04-20 07:22:22

`PolynomialSequence_gf2.solve` currently uses `lambda x: R_origin(x).lm()` as the key conversion function. Which could lead to strange behavior if used incorrectly:


```
sage: R.<x,y,z> = BooleanPolynomialRing()
sage: sol = Sequence([x*y+z, y*z+x, x+y+z+1]).solve()
sage: sol
[{y: 1, z: 0, x: 0}]
sage: sol[0][y+z]
1
```


Should I have the conversion function verify that converting the resulting monomial back into a polynomial will result in a polynomial equal to the argument? Or should I use the rin instead of its monomials as the key domain of the dict? Or is this glitch acceptable, since it's obvious you should use a single monomial as a key here?


---

Comment by vdelecroix created at 2015-04-20 09:45:24

Patchbot not yet happy (but not that bad, only one failing doctest)

```
File "src/sage/rings/polynomial/multi_polynomial_ideal.py", line 2258,
in sage.rings.polynomial.multi_polynomial_ideal.?.variety
Failed example:
    for V in I.variety(): print V  # long time (6s on sage.math, 2011)
```


Vincent


---

Comment by git created at 2015-04-20 10:21:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-04-20 10:29:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmezzarobba created at 2015-05-25 09:49:52

Changing status from needs_review to needs_info.


---

Comment by mmezzarobba created at 2015-05-25 09:49:52

Rebased to fix minor conflicts.

Just one question: what is `_no_default_provided` for? Wouldn't it be enough to do

```
return super(KeyConvertingDict, self).pop(key, *args)
```

in `KeyConvertingDict.pop()`?

Looks good to me otherwise.
----
New commits:


---

Comment by git created at 2015-06-11 07:21:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmezzarobba created at 2015-09-03 13:09:06

Rebased because of a minor conflict. I guess this ticket should be `needs_review` again, shouldn't it?
----
New commits:


---

Comment by mmezzarobba created at 2015-09-03 13:09:06

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2015-09-03 18:34:38

does not seem to apply


---

Comment by chapoton created at 2015-09-03 18:34:38

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-09-04 05:04:34

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mmezzarobba created at 2015-09-04 05:05:21

Changing status from needs_work to needs_review.


---

Comment by mmezzarobba created at 2015-09-04 05:05:21

Replying to [comment:26 chapoton]:
> does not seem to apply

Sorry, it looks like I pushed the wrong branch!
----
New commits:


---

Comment by git created at 2015-10-15 09:23:00

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mmezzarobba created at 2015-10-15 12:18:50

Changing status from needs_review to positive_review.


---

Comment by mmezzarobba created at 2015-10-15 12:18:50

Since all tests pass and all I did was to rebase Martin's patches and fix trivial conflicts, I'm taking the liberty to set this to positive review myseld.


---

Comment by vbraun created at 2015-10-16 18:42:48

Resolution: fixed


---

Comment by jdemeyer created at 2015-11-27 15:20:56

Breakage:

```
sage -t --warn-long 27.7 src/sage/rings/polynomial/multi_polynomial_sequence.py
**********************************************************************
File "src/sage/rings/polynomial/multi_polynomial_sequence.py", line 1381, in sage.rings.polynomial.multi_polynomial_sequence.PolynomialSequence_gf2.solve
Failed example:
    sol = S.solve(algorithm='sat'); sol  # optional - cryptominisat
Expected nothing
Got:
    [{y: 1, z: 0, x: 0}]
**********************************************************************
```

