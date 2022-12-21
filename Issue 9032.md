# Issue 9032: no method numerical_approx for integers and rationals

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-05-24 09:12:23

Assignee: AlexGhitza

CC:  kcrisman


```
sage: a=8
sage: a.n()
8.00000000000000
sage: a.numerical_approx()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/zimmerma/<ipython console> in <module>()

/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2628)()

/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2828)()

/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2595)()

AttributeError: 'sage.rings.integer.Integer' object has no attribute 'numerical_approx'
```

The same holds for a=17/2 for example.

Since `n` is a shortcut for `numerical_approx`,
it should work with `numerical_approx` too. In addition,
if one uses a variable `n` is a program, it would be more
portable to use `numerical_approx`. 


---

Comment by jason created at 2010-05-26 15:27:11

Changing keywords from "" to "beginner".


---

Comment by ryan created at 2011-01-08 22:56:59

Is there an example when a.numerical_approx() works?

After reading the documentation on numerical_approx(), I don't think it can be used in this manner.  

Note that a.N() does not work either for your example.


---

Comment by gagansekhon created at 2011-01-10 04:23:52

Changing status from new to needs_review.


---

Comment by gagansekhon created at 2011-01-10 04:23:52

a.numerical_approx() needed to be defined in sage.misc.element.pyx. However n() already defined there calls and checks if the element type already has numerical_approx(). So this would cause an infinite loop. 

So instead now it calls to see if it has _numerical_approx()

I changed all the files where a specific type defined numerical_approx to _numerical_approx and defined an "empty method" numerical_approx, which just calls _numerical_approx.

So now every type should automatically have a numerical_approx. If a specific one is defined then that is called or it simply coerces it to be a real or complex approx.


---

Comment by zimmerma created at 2011-01-10 09:40:50

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2011-01-10 09:40:50

hi, with Sage 4.6 I got an error while importing the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 9032
sage: hg_sage.import_patch("/tmp/trac_9032.patch")
cd "/usr/local/sage/devel/sage" && hg status
cd "/usr/local/sage/devel/sage" && hg status
cd "/usr/local/sage/devel/sage" && hg import   "/tmp/trac_9032.patch"
applying /tmp/trac_9032.patch
abort: malformed patch a/sage/structure/element.pyx `@``@` -578,24 +580,26 `@``@`
```

Paul


---

Comment by zimmerma created at 2011-01-10 10:55:12

Changing status from needs_info to needs_work.


---

Comment by zimmerma created at 2011-01-10 10:55:12

sorry, I clicked on the wrong button.


---

Comment by gagansekhon created at 2011-01-10 20:07:35

ok another attempt. But this time, I made the changes much simpler, all elements matrix2, expression, heegner which had a numerical_approx, I just added _numerical_approx=numerical_approx. 

Added numerical_approx and N =n in elements

changed functional line 1252 so it calls x._numerical_approx. So if we call numerical_approx for any element (for example integers) which does not have it explicitly defined it does not go into an infinite loop


---

Comment by gagansekhon created at 2011-01-10 20:07:35

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2011-01-10 20:11:06

This needs a commit message.


---

Comment by aly.deines created at 2011-01-10 20:11:06

Changing status from needs_review to needs_work.


---

Comment by gagansekhon created at 2011-01-10 20:13:07

Changing status from needs_work to needs_review.


---

Comment by wjp created at 2011-01-10 20:44:28

Changing status from needs_review to needs_work.


---

Comment by wjp created at 2011-01-10 20:44:28

A few minor points:

You can just rename `numerical_approx` to `_numerical_approx` in `matrix2.pyx` without keeping `numerical_approx` since `Matrix` is an `element` so it inherits the default implementation of `numerical_approx`. Same for `expression.pyx`.

(On the other hand, `heegner.py` does need both.)

I would change the docstrings in `structure/element.pyx` to something shorter than the full output. Maybe the following?


```
[..., 'is_idempotent', 'is_integral', ...]
```



Is the (capital) `N()` for consistency with something, or is that new?


---

Comment by gagansekhon created at 2011-01-10 23:20:47

If I changed matrix2 and expression to not have numerical_approx then the documentation won't show up. 

changed element.pyx

And yes N() is for consistency, but I did remove them from expression since it is not needed.


---

Comment by gagansekhon created at 2011-01-10 23:22:53

Changing status from needs_work to needs_review.


---

Comment by gagansekhon created at 2011-01-11 18:51:38

This patch won't apply since documentation for misc/functional.py and symbolic/integration/integral.py is changed in rc1. I will update the patch today after I download new version of rc1


---

Comment by gagansekhon created at 2011-01-11 18:51:38

Changing status from needs_review to needs_work.


---

Comment by gagansekhon created at 2011-01-12 18:14:39

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2011-01-12 19:38:12

Changing status from needs_review to needs_work.


---

Comment by aly.deines created at 2011-01-12 19:38:12


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  devel/sage/sage/symbolic/function.pyx # 2 doctests failed
	sage -t  devel/sage/sage/misc/randstate.pyx # Time out
	sage -t  devel/sage/sage/interfaces/sage0.py # Time out
	sage -t  devel/sage/sage/interfaces/psage.py # Time out
	sage -t  devel/sage/sage/plot/plot.py # Time out
	sage -t  devel/sage/sage/symbolic/function_factory.py # 1 doctests failed
	sage -t  devel/sage/sage/functions/min_max.py # 3 doctests failed
	sage -t  devel/sage/sage/modular/modform/test.py # 0 doctests failed
	sage -t  devel/sage/sage/misc/sagedoc.py # Time out
	sage -t  devel/sage/sage/schemes/generic/toric_divisor.py # Time out
	sage -t  devel/sage/sage/tests/cmdline.py # Time out
	sage -t  devel/sage/sage/misc/trace.py # 2 doctests failed
	sage -t  devel/sage/sage/parallel/use_fork.py # 0 doctests failed
	sage -t  devel/sage/sage/symbolic/expression.pyx # Time out
	sage -t  devel/sage/sage/geometry/polyhedra.py # Time out
	sage -t  devel/sage/sage/tests/startup.py # 1 doctests failed
----------------------------------------------------------------------
```



---

Comment by aly.deines created at 2011-01-13 05:18:26

Changing status from needs_work to positive_review.


---

Comment by wjp created at 2011-01-13 05:22:44

mhampton points out there isn't a patch attached.


---

Comment by wjp created at 2011-01-13 05:22:44

Changing status from positive_review to needs_work.


---

Comment by gagansekhon created at 2011-01-13 05:51:08

Let's try this one more time. I promise this one is not empty. I am currently also running testall on rc1


---

Comment by gagansekhon created at 2011-01-13 05:51:08

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2011-01-13 06:50:35

Everything finally passes.


---

Comment by aly.deines created at 2011-01-13 06:50:35

Changing status from needs_review to positive_review.


---

Comment by wjp created at 2011-01-13 08:01:24

Confirmed. (Leaving it as positive review after the patch was updated.)


---

Comment by kcrisman created at 2011-01-13 15:06:48

Replying to [comment:21 wjp]:
> Confirmed. (Leaving it as positive review after the patch was updated.)

Except the commit message of the latest patch is somewhat mystifying.    O bureaucracy!  Maybe a friendly release manager can just update the patch with something like "Ensures everything relevant can be numerically approximated and changes things to an underscore method in a few cases"...


---

Comment by gagansekhon created at 2011-01-13 18:41:05

Added commit message and comments to all changes. Plus added a couple more doctest (just so I don't wake up in the middle of the night afraid something went wrong). I am currently running all doctest to make sure it all still works. And the patch is nonempty, I checked. 

For some reason, I can't change to needs_review.


---

Comment by wjp created at 2011-01-13 18:44:14

Changing status from positive_review to needs_work.


---

Comment by wjp created at 2011-01-13 18:44:21

Changing status from needs_work to needs_review.


---

Comment by jgaski created at 2011-01-14 01:48:15

All tests pass, and I would positively review this patch, except for three
documentation problems.

1) The extraneous, pre-existing example line ("a = 2/3") should be removed 
(in structure/element.pyx). It is neither an example of the use of numerical 
approximation, nor used in the remaining part of the example.


```
sage: a = 8
sage: a.numerical_approx?
...
    
       Return a numerical approximation of x with at least prec bits of
       precision.
    
       EXAMPLES:
    
          sage: (2/3).n()
          0.666666666666667
          sage: a = 2/3
          sage: pi.n(digits=10)
          3.141592654
          sage: pi.n(prec=20)   # 20 bits
          3.1416

```


2) Grammatical error in symbolic/expression.pyx:


```
sage: a = cos(3)
sage: a.numerical_approx?
...
    
       Return a numerical approximation this symbolic expression as either
```


Should be "numerical approximation of this symbolic expression...."
                                   ^^

I know these are trivial and not written by you. However, they're too trivial for their own 
patches, and would fit logically in yours.

3) When I create a symbolic expression, I now get different docstrings for "n" 
(from element) and "numerical_approx" (from expression):


```
sage: a = cos(3)
sage: type(a)
<type 'sage.symbolic.expression.Expression'>
sage: a.n?
...
       Return a numerical approximation of x with at least prec bits of
       precision.
    
       EXAMPLES:
    
          sage: (2/3).n()
          0.666666666666667
...

sage: a.numerical_approx?
...    
       Return a numerical approximation this symbolic expression as either
       a real or complex number with at least the requested number of bits
       or digits of precision.
    
       EXAMPLES:
    
          sage: sin(x).subs(x=5).n()
          -0.958924274663138
...

```


I believe that this happened when you removed the re-definition of method "n" in expression.
However, that is the docstring that you want to be returned for a symbolic expression.


---

Attachment


---

Comment by gagansekhon created at 2011-01-17 00:04:17

I made the changes  jgaski suggested and ran all test. The patch passed.


---

Comment by jgaski created at 2011-01-17 01:00:40

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-17 17:18:28

I think this is the full name of the last reviewer which I put in the reviewer section, but please advise if it's not correct.


---

Comment by jdemeyer created at 2011-01-25 08:14:34

Resolution: fixed


---

Comment by nthiery created at 2011-03-23 21:40:26

Hi!

Is the alias N really needed? It pollutes the namespace of all elements, and broke some code on the Sage-Combinat queue (in that particular case, it was overwriting a field of a gap3 record element). Well, I guess we can find a workaround but still having n and N and numerical_approx seems like a waste.

Cheers,
                        Nicolas


---

Comment by kcrisman created at 2011-03-24 01:17:39

> Is the alias N really needed? It pollutes the namespace of all elements, and broke some code on the Sage-Combinat queue (in that particular case, it was overwriting a field of a gap3 record element). Well, I guess we can find a workaround but still having n and N and numerical_approx seems like a waste.
N has been an alias for this for a long time, so this just making it consistent -  I think this added a method, not a global function.  In a Sage version nearly a year old:

```
sage: N(5)
5.00000000000000
sage: n(5)
5.00000000000000
sage: numerical_approx(5)
5.00000000000000
sage: a=5
sage: a.N?
Object `a.N` not found.
sage: a.n
<built-in method n of sage.rings.integer.Integer object at 0x1091154e0>
```



---

Comment by nthiery created at 2011-03-24 08:00:35

Hi!

Replying to [comment:32 kcrisman]:
> N has been an alias for this for a long time, so this just making it consistent -  I think this added a method, not a global function.

Yes; I am precisely arguing about this method, and the pollution of the method namespace of all elements. We can't use anymore x.N to access an attribute called N in a gap record x (well, we can, but as x.__getattr__("N") which is not very convenient).

Thanks,


---

Comment by kcrisman created at 2011-03-24 12:17:47

I see. Well, it's been merged, so the proper thing to do is to ask on sage-devel or open a ticket. I don't see why it wouldn't be possible to take this behavior away from structure/element and put it only on numerical types, though it would be a little more of a pain.

I could imagine someone wanting numerical approx of e.g. GAP elements, though, and it's true that for consistency n and N should do the same thing as methods as as functions, so maybe this is worth raising on sage-devel. I wouldn't be surprised if no one much cared, though, as long as integers and rationals still had N and n.


---

Comment by nthiery created at 2011-03-24 12:33:03

Replying to [comment:34 kcrisman]:
> I see. Well, it's been merged, so the proper thing to do is to ask on sage-devel or open a ticket. I don't see why it wouldn't be possible to take this behavior away from structure/element and put it only on numerical types, though it would be a little more of a pain.
> 
> I could imagine someone wanting numerical approx of e.g. GAP elements, though, and it's true that for consistency n and N should do the same thing as methods as as functions, so maybe this is worth raising on sage-devel. I wouldn't be surprised if no one much cared, though, as long as integers and rationals still had N and n.

Do you mind running this discussion on sage-devel?

I guess someone wanting a numerical approximation on a gap element (that could well be me :-)) can afford to use g.numerical_approx(), or just g.n().

Thanks!
