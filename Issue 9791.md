# Issue 9791: kernel and inverse_image of (polynomial) ring maps

archive/issues_009791.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @dimpase\n\nIt would be nice if kernels and inverse images of ring maps were implemented:\n\n```\nsage: R.<s,t>=PolynomialRing(QQ);R\nMultivariate Polynomial Ring in s, t over Rational Field\nsage: S.<x,y,z,w>=PolynomialRing(QQ);S\nMultivariate Polynomial Ring in x, y, z, w over Rational Field\nsage: f=S.hom([s^4,s^3*t,s*t^3,t^4],R);f\nRing morphism:\n  From: Multivariate Polynomial Ring in x, y, z, w over Rational Field\n  To:   Multivariate Polynomial Ring in s, t over Rational Field\n  Defn: x |--> s^4\n        y |--> s^3*t\n        z |--> s*t^3\n        w |--> t^4\nsage: f.inverse_image(0)\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/vbraun/opt/sage-4.5.2/devel/sage-main/sage/libs/singular/<ipython console> in <module>()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/rings/morphism.so in sage.rings.morphism.RingHomomorphism.inverse_image (sage/rings/morphism.c:4168)()\n\nNotImplementedError: \nsage: kernel(f)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/vbraun/opt/sage-4.5.2/devel/sage-main/sage/libs/singular/<ipython console> in <module>()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/misc/functional.pyc in kernel(x)\n    907         ]\n    908     \"\"\"\n--> 909     return x.kernel()\n    910 \n    911 def krull_dimension(x):\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2602)()\n\nAttributeError: 'sage.rings.morphism.RingHomomorphism_im_gens' object has no attribute 'kernel'\n```\nHere is the corresponding Singular computation:\n\n```\nsage: sage: singular.eval('''\n....:         ring R=0,(s,t),dp;\n....:         ring S=0,(x,y,z,w),dp;\n....:         setring R;\n....:         map f=S,ideal(s^4,s^3*t,s*t^3,t^4);\n....:         setring S;\n....:         ideal ker=kernel(R,f)\n....:       ''');\nsage: sage: singular.get('ker')\n'yz-xw,\\nz3-yw2,\\nxz2-y2w,\\ny3-x2z'\nsage: sage: print(_)\nyz-xw,\nz3-yw2,\nxz2-y2w,\ny3-x2z\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9792\n\n",
    "created_at": "2010-08-24T12:04:19Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.2",
    "title": "kernel and inverse_image of (polynomial) ring maps",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9791",
    "user": "https://github.com/vbraun"
}
```
Assignee: @aghitza

CC:  @dimpase

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

Issue created by migration from https://trac.sagemath.org/ticket/9792





---

archive/issue_events_024559.json:
```json
{
    "actor": "https://github.com/mwageringel",
    "created_at": "2020-06-01T16:00:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "milestone": "sage-9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9791#event-24559"
}
```



---

archive/issue_comments_095988.json:
```json
{
    "body": "Remove assignee @aghitza.",
    "created_at": "2020-06-01T16:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95988",
    "user": "https://github.com/mwageringel"
}
```

Remove assignee @aghitza.



---

archive/issue_comments_095989.json:
```json
{
    "body": "New commits:",
    "created_at": "2020-06-01T16:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95989",
    "user": "https://github.com/mwageringel"
}
```

New commits:



---

archive/issue_comments_095990.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-01T16:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95990",
    "user": "https://github.com/mwageringel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095991.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-06-01T16:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95991",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_095992.json:
```json
{
    "body": "In `RingHomomorphism_cover._inverse_image_element`, you forgot the `EXAMPLES::` (and indentation).\n\nShould we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?",
    "created_at": "2020-06-02T06:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95992",
    "user": "https://github.com/tscrim"
}
```

In `RingHomomorphism_cover._inverse_image_element`, you forgot the `EXAMPLES::` (and indentation).

Should we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?



---

archive/issue_comments_095993.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2020-06-02T19:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95993",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_095994.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2020-06-02T19:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95994",
    "user": "https://github.com/mwageringel"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095995.json:
```json
{
    "body": "Replying to [comment:5 tscrim]:\n> Should we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?\n\n\nIt would probably be good to wrap the Singular functions `kernel` and `preimage`, yes. I have not compared it in terms of speed yet, mainly because I thought that I needed to implement the graph ideal in Sage anyway in order to compute inverses of elements. However, I have just noticed that the Singular function [algebra_containment](https://www.singular.uni-kl.de/Manual/4-1-3/sing_1215.htm#SEC1296) can be used for that, which I had overlooked before. I will try to figure out how to call it from Sage and then report back.\n\nPossibly this means that this branch can be refactored such that it only wraps Singular functions, instead of constructing the graph ideal in Sage, unless we want to keep it for more control over the Gr\u00f6bner basis computations.\n\nHere is Singular code for the example from the description:\n\n```\n> LIB \"algebra.lib\";\n> ring S = 0, (s,t), dp;\n> ideal A = ideal(s^4, s^3*t, s*t^3, t^4);\n> poly p = s^3*t^4*(s+t);\n> list L = algebra_containment(p, A, 1);\n> L[1];\n1\n> def T = L[2]; setring T; check;\ny(1)*y(4)+y(2)*y(4)\n```",
    "created_at": "2020-06-02T19:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95995",
    "user": "https://github.com/mwageringel"
}
```

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

archive/issue_comments_095996.json:
```json
{
    "body": "Replying to [comment:7 gh-mwageringel]:\n> Replying to [comment:5 tscrim]:\n> > Should we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?\n\n> \n> It would probably be good to wrap the Singular functions `kernel` and `preimage`, yes. I have not compared it in terms of speed yet, mainly because I thought that I needed to implement the graph ideal in Sage anyway in order to compute inverses of elements. However, I have just noticed that the Singular function [algebra_containment](https://www.singular.uni-kl.de/Manual/4-1-3/sing_1215.htm#SEC1296) can be used for that, which I had overlooked before. I will try to figure out how to call it from Sage and then report back.\n> \n> Possibly this means that this branch can be refactored such that it only wraps Singular functions, instead of constructing the graph ideal in Sage, unless we want to keep it for more control over the Gr\u00f6bner basis computations.\n\n\nWe will probably want to have both so we can have it for both generic polynomials (over more exotic base fields (integral domains?)) and specialized code for those implemented using Singular (and less back-and-forth between Singular and Sage).",
    "created_at": "2020-06-03T04:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95996",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:7 gh-mwageringel]:
> Replying to [comment:5 tscrim]:
> > Should we also implement a (lib)singular version of the kernel for ideals? Or did you do this already and saw that it was slower?

> 
> It would probably be good to wrap the Singular functions `kernel` and `preimage`, yes. I have not compared it in terms of speed yet, mainly because I thought that I needed to implement the graph ideal in Sage anyway in order to compute inverses of elements. However, I have just noticed that the Singular function [algebra_containment](https://www.singular.uni-kl.de/Manual/4-1-3/sing_1215.htm#SEC1296) can be used for that, which I had overlooked before. I will try to figure out how to call it from Sage and then report back.
> 
> Possibly this means that this branch can be refactored such that it only wraps Singular functions, instead of constructing the graph ideal in Sage, unless we want to keep it for more control over the Gröbner basis computations.


We will probably want to have both so we can have it for both generic polynomials (over more exotic base fields (integral domains?)) and specialized code for those implemented using Singular (and less back-and-forth between Singular and Sage).



---

archive/issue_comments_095997.json:
```json
{
    "body": "Implementing this via the libsingular interface is a lot more complicated than I anticipated. It is not currently possible to use Sage's `singular_function` with the Singular type `qring`, and quotient rings in Sage are not even backed by `qring`s in Singular. This means it is not currently possible to use the Singular function `algebra_containment` with quotient rings via libsingular, but only with polynomial rings.\n\nThe implementation of [algebra_containment](https://github.com/Singular/Sources/blob/Release-4-1-3p2/Singular/LIB/algebra.lib#L59-L129) is essentially the same as on this branch. The main difference is that `algebra_containment` uses the Singular function `std` for Gr\u00f6bner basis computations whereas Sage uses the general purpose function `groebner`, which does some preprocessing and then calls a suitable implementation. As such, the computation times can be quite different. The Singular version is often a bit faster, but when computing preimages of many elements, the caching in the Sage version seems to be more effective.\n\nThe implementation of the Singular function `preimage` is a bit less transparent to me, so it might be more interesting to wrap this. In this case, by switching to the ambient ring, one can work around the problem that the `qring` type is not supported. However, I still did not manage to call `preimage` via libsingular, as it requires the ideals passed as arguments to have names, which our ideals apparently do not have.\n\nThe other option is to use the Singular pexpect interface to wrap `preimage` and `algebra_containment`. Though, as the current branch is functional, I would prefer to not implement that on this ticket here, so I am setting this back to needs_review.",
    "created_at": "2020-06-13T14:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95997",
    "user": "https://github.com/mwageringel"
}
```

Implementing this via the libsingular interface is a lot more complicated than I anticipated. It is not currently possible to use Sage's `singular_function` with the Singular type `qring`, and quotient rings in Sage are not even backed by `qring`s in Singular. This means it is not currently possible to use the Singular function `algebra_containment` with quotient rings via libsingular, but only with polynomial rings.

The implementation of [algebra_containment](https://github.com/Singular/Sources/blob/Release-4-1-3p2/Singular/LIB/algebra.lib#L59-L129) is essentially the same as on this branch. The main difference is that `algebra_containment` uses the Singular function `std` for Gröbner basis computations whereas Sage uses the general purpose function `groebner`, which does some preprocessing and then calls a suitable implementation. As such, the computation times can be quite different. The Singular version is often a bit faster, but when computing preimages of many elements, the caching in the Sage version seems to be more effective.

The implementation of the Singular function `preimage` is a bit less transparent to me, so it might be more interesting to wrap this. In this case, by switching to the ambient ring, one can work around the problem that the `qring` type is not supported. However, I still did not manage to call `preimage` via libsingular, as it requires the ideals passed as arguments to have names, which our ideals apparently do not have.

The other option is to use the Singular pexpect interface to wrap `preimage` and `algebra_containment`. Though, as the current branch is functional, I would prefer to not implement that on this ticket here, so I am setting this back to needs_review.



---

archive/issue_comments_095998.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-06-13T14:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95998",
    "user": "https://github.com/mwageringel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095999.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-06-13T22:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-95999",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096000.json:
```json
{
    "body": "That is too bad. Thank you for trying. I agree that we should get this into Sage now, and we can revisit using libsingular later.",
    "created_at": "2020-06-13T22:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-96000",
    "user": "https://github.com/tscrim"
}
```

That is too bad. Thank you for trying. I agree that we should get this into Sage now, and we can revisit using libsingular later.



---

archive/issue_comments_096001.json:
```json
{
    "body": "Thank you.",
    "created_at": "2020-06-13T23:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-96001",
    "user": "https://github.com/mwageringel"
}
```

Thank you.



---

archive/issue_events_024560.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2020-06-22T22:34:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9791#event-24560"
}
```



---

archive/issue_comments_096002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-06-22T22:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9791#issuecomment-96002",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
