# Issue 3889: extend parameter for number field sqrt method

Issue created by migration from https://trac.sagemath.org/ticket/3889

Original creator: jbmohler

Original creation time: 2008-08-18 13:50:47

Assignee: was

CC:  tscrim vdelecroix

Number field element sqrt should support the extend parameter in analogy with other sqrt functions.


```
sage: ZZ(4).sqrt(extend=False)
2
sage: CyclotomicField(4)(4).sqrt(extend=False)
...
TypeError: 'extend' is an invalid keyword argument for this function
```


If it would even have the parameter and raise a NotImplementedError if extend==True, that would aid in writing generic code for the present.


---

Comment by AlexGhitza created at 2009-01-23 07:07:00

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-21 08:04:16

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-21 08:04:16

Changing component from number theory to number fields.


---

Comment by chapoton created at 2020-10-18 08:45:34

New commits:


---

Comment by chapoton created at 2020-10-18 08:45:34

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-10-18 12:20:15

green bot, please review


---

Comment by tscrim created at 2020-10-19 23:37:33

It might be good to allow `extend` to take a string input to set the extension's variable name. Otherwise, LGTM.


---

Comment by chapoton created at 2020-10-20 07:12:31

I can see 2 places where a parameter "name" is used:

```
src/sage/rings/power_series_ring_element.pyx:    def sqrt(self, prec=None, extend=False, all=False, name=None):
src/sage/rings/ring_extension_element.pyx:    def sqrt(self, extend=True, all=False, name=None):
```



---

Comment by git created at 2020-10-20 07:54:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2020-10-20 08:08:29

I have added an optional parameter for the name.


---

Comment by vdelecroix created at 2020-10-20 09:04:28

The specicifications does not match the following behavior

```
sage: CyclotomicField(4)(2).sqrt(extend=False)
sqrt(2)
```

Of course, this is no due to your changes, but this function is just wrong in returning symbolic ring stuff without notice.


---

Comment by chapoton created at 2020-10-20 09:26:27

Et donc ? que faire ?


---

Comment by vdelecroix created at 2020-10-20 09:32:18

Replying to [comment:16 chapoton]:
> Et donc ? que faire ?

Many ways to solve it

1. Do not return symbolic as one can do `SR(my_stuff).sqrt()`

2. Add a `symbolic` argument

3. Make `extend` a three fold alternative
   - `extend=None`: old behavior
   - `extend=False`: return in the current number field or raise an error
   - `extend=True`: return in the current number field or an extended one if needed


---

Comment by git created at 2020-10-20 11:20:08

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2020-10-20 11:23:52

alors, j'ai viré SR (option 1)


---

Comment by vdelecroix created at 2020-10-20 12:19:07

Tu noteras qu'il y a un problème de retrocompatibilité.


---

Comment by chapoton created at 2020-10-20 13:55:20

alors je remets le bloc SR ?


---

Comment by vdelecroix created at 2020-10-21 16:20:13

Oui avec un `DeprecationWarning` disant de faire `SR(my_number_field_element).sqrt()`.


---

Comment by git created at 2020-10-21 18:49:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2020-10-21 18:52:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2020-10-21 18:54:23

Je ne comprends pas pourquoi la deprecation n'est pas déclenchée par le doctest.


---

Comment by vdelecroix created at 2020-10-21 19:28:01

Replying to [comment:25 chapoton]:
> Je ne comprends pas pourquoi la deprecation n'est pas déclenchée par le doctest.

https://trac.sagemath.org/ticket/28500


---

Comment by chapoton created at 2020-10-25 08:22:07

ca pose de gros problemes dans src/sage/geometry/polyhedron/base.py


---

Comment by @kliem created at 2020-10-26 08:57:20

The problem I'm having with `src/sage/geometry/polyhedron.base.py` is the following:

Given a number field `K` with specified embedding into `AA`. How do I obtain a positive square root (i.e. the parent has a specified embedding as well).

It is very unnatural if it isn't well-defined if the volume is positive or negative.


---

Comment by vdelecroix created at 2020-10-26 09:18:16

Replying to [comment:28 gh-kliem]:
> The problem I'm having with `src/sage/geometry/polyhedron.base.py` is the following:
> 
> Given a number field `K` with specified embedding into `AA`. How do I obtain a positive square root (i.e. the parent has a specified embedding as well).
> 
> It is very unnatural if it isn't well-defined if the volume is positive or negative.

Just move the volume answer to `AA`. A number field version can easily be reconstructed

```
sage: K.<sqrt2> = QuadraticField(2, embedding=AA(2).sqrt())                                                                                                                                    
sage: v = AA(12*sqrt2 - 15).sqrt()                                                                                                                                                             
sage: L, vL, phi = v.as_number_field_element(minimal=True, embedded=True)                                                                                                                      
sage: vL                                                                                                                                                                                       
-a^3 + a^2 + 4*a + 3
sage: vL.n()                                                                                                                                                                                   
1.40376734129169
```



---

Comment by @kliem created at 2020-10-26 11:25:59

This works for the volume of polyhedra now.

I did change the behaviour. The new default `None` is deprecated now and `extend=False` raises a `ValueError` to be consistent with other rings. The new default should then be `extend=True` once we remove the deprecation warning.

The `QR` method of method of matrices does not raise correctly a `TypeError`, if the base ring does not support the required roots. (Before it would sometimes implicitly extend even though the documentation tells us that the base ring must support roots.)
----
New commits:


---

Comment by @kliem created at 2020-10-26 11:26:23

The doctest testing the deprecation warning still does not work.


---

Comment by vdelecroix created at 2020-10-26 11:28:45

Having a deprecated default is the worse that can be!


---

Comment by @kliem created at 2020-10-26 11:35:21

How else can you tell users that they should think about what they really want?


---

Comment by git created at 2020-10-26 11:36:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @kliem created at 2020-10-26 11:43:11

`extend=False` should just throw an error (if extension is needed) and don't do something weird like changing to symbolic ring.

To do `elt.sqrt(extend=False)` is correct behaviour and it should just raise and error, like with other rings. Also `extend=False` is a bad default, because it is not the default for `functions.other.sqrt`.

The idea of this default deprecation message is that users code needs to be updated and this is how you notify them, isn't it?


---

Comment by @kliem created at 2020-10-26 12:14:02

Then again we could just not do a deprecation warning at all and change the default to `extend=True`.

This is what it boils down to for `functions.other.sqrt` anyway.


---

Comment by git created at 2020-10-26 12:20:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @kliem created at 2020-10-26 12:24:39

I removed the deprecation warning. The main problem is that `functions.other.sqrt` calls the method `sqrt` without optional arguments and claims that the default is to extend.

In this way it requires:
- that any `sqrt` method must extend by default without deprecation warning etc,
- any `sqrt` method does have an `extend` argument.

If we want to keep the deprecation message we need to alter `functions.other.sqrt`.

Feel free to reject my changes alltogether or change anything you like. I just joined in because there was trouble with polyhedra.


---

Comment by chapoton created at 2020-10-27 17:32:15

There is still one failing doctest, see patchbot report


---

Comment by git created at 2020-10-27 22:50:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2020-10-28 07:52:27

I am not sure what this `sqrt` method is trying to achieve. Giving an answer is not a necessity. Especially if the answer is "the square root of your number". Currently, I find that only the `extend=False` looks reasonable.

I see several problems
- `QQ` is a particular case of number fields, and `ZZ` is a particular case of `QQ`. For both `ZZ` and `QQ` the behavior of `sqrt` should be compatible with what is proposed for number fields.
- The proposal is not compatible with embeddings. Many users would expect `K(2).sqrt() + K(3).sqrt()` to work. Especially with `K=QQ`.


---

Comment by @kliem created at 2020-10-28 08:26:22

I tried to make the behavior consistent, this is why I changed the default to `extend=True`.

But I see the problem that `ZZ` and `QQ` still choose symbolic expressions instead. Should we change them all or just leave it at symbolic expressions? (The polyhedron problem is still solved by this, because by the `extend=False` option, you can stabely raise an error.)

Compatibily of embeddings can be achieved, at least when `all=False`: If `K` has a specified complex embedding, we just use this to specify an ambedding of the extension. In case `K` is `QQ` we just go with `AA`. This way `K(2).sqrt() + K(3).sqrt()` would still work, at least when `K` has a specified complex embedding that contains both `K(2).sqrt()` and `K(3).sqrt()`.


---

Comment by tscrim created at 2020-11-01 23:25:32

So I agree that it should be consistent. However, there will be a backwards incompatibility issue to deal with if we make this change. At least with the current change, there is at least a type distinction that can be employed to justify the difference. If we do make a change for `ZZ` and `QQ`, then we should only do it once as it will likely be a bit painful for users expecting it in `SR`. That is my 2 cents.


---

Comment by git created at 2021-01-11 09:12:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @kliem created at 2021-01-11 09:15:49

Ok. This should now behave consistenly with `ZZ` and `QQ`.
If `self` is a square, just return the root.
If `self` is not a square, raise an error if `extend=False` and use symbolic ring if `extend=True` (default).

Of course one could argue, that this behavior isn't optimal and there are better choices for a square root construction (e.g. extend the number field), but it is really hard to guess what the user wants precisely (e.g. for polytopes volume, if we need to extend anyway, we might as well go to `AA`).


---

Comment by tscrim created at 2021-01-12 00:28:03

I am a little worried about this change:

```diff
diff --git a/src/sage/matrix/matrix2.pyx b/src/sage/matrix/matrix2.pyx
index 5e190ea..7ce4196 100644
--- a/src/sage/matrix/matrix2.pyx
+++ b/src/sage/matrix/matrix2.pyx
@@ -10136,7 +10136,7 @@ cdef class Matrix(Matrix1):
             hip = v.hermitian_inner_product(v)
             if hip != 0:
                 try:
-                    scale = sqrt(hip)
+                    scale = sqrt(hip, extend=False)
                     q = (1/scale)*v
                     Q.append(q)
                     R[row,i] = scale
```

Since this can take in general rings, such as one whose elements could have a `sqrt` that does not take `extend` as a parameter, this could behave differently than before. How would you classify this behavior? A bug in the `sqrt` implementation? Or am I just being paranoid about this?


---

Comment by @kliem created at 2021-01-12 08:06:22

Yes, I agree, there is a number of rings that don't have this keyword.


---

Comment by git created at 2021-01-12 08:16:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @kliem created at 2021-01-12 08:20:06

Reading closely, the documentation of `QR` does not claim that the base ring is preserved. In particular it mentions that it is not preserved, when the base ring is not a field. It just mentions that the base ring must have have roots. In that way, I guess that `QQ` has roots in sage (just not preserving the ring).

The change in `QR` was required, because of some design decision that I reverted already.


---

Comment by tscrim created at 2021-01-14 05:55:25

I am ready to set a positive review. Vincent, any additional comments or things to address before I do so?


---

Comment by vdelecroix created at 2021-01-14 10:13:15

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2021-01-14 10:13:15

Nothing to add. Thanks.


---

Comment by @kliem created at 2021-01-14 10:14:15

Thank you.


---

Comment by vbraun created at 2021-01-24 10:37:53

Resolution: fixed
