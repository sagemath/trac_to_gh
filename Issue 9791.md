# Issue 9791: kernel and inverse_image of (polynomial) ring maps

Issue created by migration from Trac.

Original creator: vbraun

Original creation time: 2010-08-24 12:04:19

Assignee: AlexGhitza

CC:  dimpase

It would be nice if kernels and inverse images of ring maps were implemented:

```
sage: R.<s,t>=PolynomialRing(QQ);R
Multivariate Polynomial Ring in s, t over Rational Field
sage: S.<x,y,z,w>=PolynomialRing(QQ);S
Multivariate Polynomial Ring in x, y, z, w over Rational Field
sage: f=S.hom([s^4,s^3*t,s*t^3,t^4],R);f
Ring morphism:
  From: Multivariate Polynomial Ring in x, y, z, w over Rational Field
  To:   Multivariate Polynomial Ring in s, t over Rational Field
  Defn: x |--> s^4
        y |--> s^3*t
        z |--> s*t^3
        w |--> t^4
sage: f.inverse_image(0)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.2/devel/sage-main/sage/libs/singular/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/rings/morphism.so in sage.rings.morphism.RingHomomorphism.inverse_image (sage/rings/morphism.c:4168)()

NotImplementedError: 
sage: kernel(f)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.2/devel/sage-main/sage/libs/singular/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/misc/functional.pyc in kernel(x)
    907         ]
    908     """
--> 909     return x.kernel()
    910 
    911 def krull_dimension(x):

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2602)()

AttributeError: 'sage.rings.morphism.RingHomomorphism_im_gens' object has no attribute 'kernel'
```

Here is the corresponding Singular computation:

```
sage: sage: singular.eval('''
....:         ring R=0,(s,t),dp;
....:         ring S=0,(x,y,z,w),dp;
....:         setring R;
....:         map f=S,ideal(s^4,s^3*t,s*t^3,t^4);
....:         setring S;
....:         ideal ker=kernel(R,f)
....:       ''');
sage: sage: singular.get('ker')
'yz-xw,\nz3-yw2,\nxz2-y2w,\ny3-x2z'
sage: sage: print(_)
yz-xw,
z3-yw2,
xz2-y2w,
y3-x2z
```



---

Comment by @mwageringel created at 2020-06-01 16:00:23

Remove assignee AlexGhitza.


---

Comment by @mwageringel created at 2020-06-01 16:00:23

New commits:


---

Comment by @mwageringel created at 2020-06-01 16:00:50

Changing status from new to needs_review.


---

Comment by git created at 2020-06-01 16:44:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2020-06-02 06:23:08

In `RingHomomorphism_cover._inverse_image_element`, you forgot the `EXAMPLES::` (and indentation).

Should we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?


---

Comment by git created at 2020-06-02 19:45:57

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by @mwageringel created at 2020-06-02 19:49:52

Changing status from needs_review to needs_work.


---

Comment by @mwageringel created at 2020-06-02 19:49:52

Replying to [comment:5 tscrim]:
> Should we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?

It would probably be good to wrap the Singular functions `kernel` and `preimage`, yes. I have not compared it in terms of speed yet, mainly because I thought that I needed to implement the graph ideal in Sage anyway in order to compute inverses of elements. However, I have just noticed that the Singular function [algebra_containment](https://www.singular.uni-kl.de/Manual/4-1-3/sing_1215.htm#SEC1296) can be used for that, which I had overlooked before. I will try to figure out how to call it from Sage and then report back.

Possibly this means that this branch can be refactored such that it only wraps Singular functions, instead of constructing the graph ideal in Sage, unless we want to keep it for more control over the Gröbner basis computations.

Here is Singular code for the example from the description:

```
> LIB "algebra.lib";
> ring S = 0, (s,t), dp;
> ideal A = ideal(s^4, s^3*t, s*t^3, t^4);
> poly p = s^3*t^4*(s+t);
> list L = algebra_containment(p, A, 1);
> L[1];
1
> def T = L[2]; setring T; check;
y(1)*y(4)+y(2)*y(4)
```



---

Comment by tscrim created at 2020-06-03 04:06:56

Replying to [comment:7 gh-mwageringel]:
> Replying to [comment:5 tscrim]:
> > Should we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?
> 
> It would probably be good to wrap the Singular functions `kernel` and `preimage`, yes. I have not compared it in terms of speed yet, mainly because I thought that I needed to implement the graph ideal in Sage anyway in order to compute inverses of elements. However, I have just noticed that the Singular function [algebra_containment](https://www.singular.uni-kl.de/Manual/4-1-3/sing_1215.htm#SEC1296) can be used for that, which I had overlooked before. I will try to figure out how to call it from Sage and then report back.
> 
> Possibly this means that this branch can be refactored such that it only wraps Singular functions, instead of constructing the graph ideal in Sage, unless we want to keep it for more control over the Gröbner basis computations.

We will probably want to have both so we can have it for both generic polynomials (over more exotic base fields (integral domains?)) and specialized code for those implemented using Singular (and less back-and-forth between Singular and Sage).


---

Comment by @mwageringel created at 2020-06-13 14:25:22

Implementing this via the libsingular interface is a lot more complicated than I anticipated. It is not currently possible to use Sage's `singular_function` with the Singular type `qring`, and quotient rings in Sage are not even backed by `qring`s in Singular. This means it is not currently possible to use the Singular function `algebra_containment` with quotient rings via libsingular, but only with polynomial rings.

The implementation of [algebra_containment](https://github.com/Singular/Sources/blob/Release-4-1-3p2/Singular/LIB/algebra.lib#L59-L129) is essentially the same as on this branch. The main difference is that `algebra_containment` uses the Singular function `std` for Gröbner basis computations whereas Sage uses the general purpose function `groebner`, which does some preprocessing and then calls a suitable implementation. As such, the computation times can be quite different. The Singular version is often a bit faster, but when computing preimages of many elements, the caching in the Sage version seems to be more effective.

The implementation of the Singular function `preimage` is a bit less transparent to me, so it might be more interesting to wrap this. In this case, by switching to the ambient ring, one can work around the problem that the `qring` type is not supported. However, I still did not manage to call `preimage` via libsingular, as it requires the ideals passed as arguments to have names, which our ideals apparently do not have.

The other option is to use the Singular pexpect interface to wrap `preimage` and `algebra_containment`. Though, as the current branch is functional, I would prefer to not implement that on this ticket here, so I am setting this back to needs_review.


---

Comment by @mwageringel created at 2020-06-13 14:25:22

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2020-06-13 22:28:53

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2020-06-13 22:28:53

That is too bad. Thank you for trying. I agree that we should get this into Sage now, and we can revisit using libsingular later.


---

Comment by @mwageringel created at 2020-06-13 23:02:33

Thank you.


---

Comment by vbraun created at 2020-06-22 22:34:42

Resolution: fixed
