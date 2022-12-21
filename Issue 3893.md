# Issue 3893: random_element methods should all accept *args and **kwds

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-18 15:38:23

Assignee: somebody

Because:
 * some more highlevel `random_element` functions pass thru `*args` and `**kwds`
 * it unifies the interface to some extend 
 * it allows the user to pass thru parameters


---

Comment by niles created at 2010-08-23 14:30:23

I've reinterpreted this ticket as "random_element methods which call other random_element methods should pass on *args and **kwds".  This applies mostly to `sage.rings`, but also a few other cases.  The list below shows the output of `sage: search_src("def random_element")`, annotated by the changes this patch makes.

`make ptestlong` passes all tests, and documentation builds without errors or warnings.  Details below.

Note that #9481 fixes `random_element` for univariate power series rings, and I've ignored padics since there is a large revision in process: e.g. #6084 and #5075.

 * algebras/quatalg/quaternion_algebra.py:448:    def random_element(self, *args, **kwds):
   * nothing to fix

 * algebras/quatalg/quaternion_algebra.py:1142:    def random_element(self, *args, **kwds):
   * nothing to fix

 * categories/enumerated_sets.py:472:        def random_element(self):
   * not implemented

 * categories/infinite_enumerated_sets.py:83:        def random_element(self):
   *  not implemented

 * coding/linear_code.py:2022:    def random_element(self):
   *  FIXED

 * combinat/cartesian_product.py:177:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/choose_nk.py:148:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/multichoose_nk.py:90:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/partition.py:3269:    def random_element(self, measure = 'uniform'):
   *  doesn't call other random_element()

 * combinat/partition.py:3297:    def random_element_uniform(self):
   *  doesn't call other random_element()

 * combinat/partition.py:3360:    def random_element_plancherel(self):
   *  doesn't call other random_element()

 * combinat/permutation.py:2792:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/permutation.py:2991:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/permutation.py:3110:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/permutation.py:3334:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/permutation_nk.py:112:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/split_nk.py:113:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/subset.py:238:    def random_element(self):
   *  doesn't call other random_element()

 * combinat/subset.py:485:    def random_element(self):
   *  calls random_element() of ChooseNK from sage.combinat.choose_nk, and that method takes no arguments

 * combinat/tableau.py:2162:    def random_element(self):
   *  doesn't call other random_element()

 * crypto/mq/mpolynomialsystemgenerator.py:184:    def random_element(self):
   *  not implemented

 * crypto/mq/sr.py:1089:    def random_element(self, elem_type = "vector"):
   *  FIXED

 * groups/group.pyx:196:    def random_element(self, bound=None):
   *  not implemented

 * groups/abelian_gps/abelian_group.py:854:    def random_element(self):
   *  doesn't call other random_element()

 * groups/abelian_gps/abelian_group_element.py:312:    def random_element(self):
   *  doesn't call other random_element()

 * groups/abelian_gps/dual_abelian_group.py:221:    def random_element(self):
   *  doesn't call other random_element()

 * groups/matrix_gps/matrix_group.py:643:    def random_element(self):
   *  doesn't call other random_element()

 * groups/perm_gps/permgroup.py:1107:    def random_element(self):
   *  doesn't call other random_element()

 * matrix/matrix_space.py:1221:    def random_element(self, density=None, *args, **kwds):
   *  nothing to fix

 * modular/dirichlet.py:2290:    def random_element(self):
   *  doesn't call other random_element()

 * modular/arithgroup/congroup_sl2z.py:142:    def random_element(self, bound=100):
   *  nothing to fix

 * DONE: modules/free_module.py:1710:    def random_element(self, prob=1.0, *args, **kwds):
   *  FIXED

 * modules/free_module.py:4147:    def random_element(self, prob=1.0, *args, **kwds):
   *  FIXED

 * modules/fg_pid/fgp_module.py:1307:    def random_element(self, *args, **kwds):
   *  FIXED

 * rings/complex_double.pyx:214:    def random_element(self, double xmin=-1, double xmax=1, double ymin=-1, double ymax=1):
   *  doesn't call any other random_element() method

 * rings/complex_field.py:421:    def random_element(self, component_max=1):
   *  FIXED

 * rings/complex_interval_field.py:334:    def random_element(self, *args):
   *  FIXED

 * rings/contfrac.py:331:    def random_element(self, num_bound=2, den_bound=2):
   *  FIXED

 * rings/fraction_field.py:573:    def random_element(self, *args, **kwds):
   *  nothing to fix

 * rings/integer_ring.pyx:511:    def random_element(self, x=None, y=None, distribution=None):
   *  doesn't call any other random_element() method

 * rings/pari_ring.py:58:    def random_element(self, bound=0):
   *  always returns 0

 * rings/power_series_ring.py:622:    def random_element(self, prec=None, *args, **kwds):
   *  fixed by #9481

 * rings/rational_field.py:762:    def random_element(self, num_bound=None, den_bound=None, distribution=None):
   *  FIXED

 * rings/real_double.pyx:406:    def random_element(self, double min=-1, double max=1):
   *  doesn't call any other random_element() method

 * rings/ring.pyx:865:    def random_element(self, bound=2):
   *  uses python's randint instead of ZZ.random_element()
   *  (this has the disadvantage of not allowing one to specify the distribution, but probably no one cares)

 * rings/real_mpfi.pyx:666:    def random_element(self, *args):
   *  FIXED

 * rings/real_mpfr.pyx:884:    def random_element(self, min=-1, max=1, distribution=None):
   *  doesn't call any other random_element() method

 * rings/finite_rings/element_givaro.pyx:352:    def random_element(self, *args, **kwds):
   *  nothing to fix

 * rings/finite_rings/finite_field_base.pyx:569:    def random_element(self, bound=None):
   *  FIXED

 * rings/finite_rings/finite_field_givaro.py:180:    def random_element(self, *args, **kwds):
   *  nothing to fix

 * rings/finite_rings/integer_mod_ring.py:1061:    def random_element(self, bound=None):
   *  calls sage.rings.CommutativeRing.random_element(), whose only allowed argument is 'bound'

 * rings/number_field/number_field.py:1247:    def random_element(self, num_bound=None, den_bound=None,
   *  calls _random_element() method of sage.rings.number_field.number_field_element.NumberFieldElement_absolute, and already includes all possible keyword arguments

 * rings/number_field/number_field_ideal.py:1132:    def random_element(self, *args, **kwds):
   *  nothing to fix

 * rings/number_field/order.py:858:    def random_element(self, *args, **kwds):
   *  nothing to fix

 * rings/padics/generic_nodes.py:265:    def random_element(self, algorithm='default'):
   *  not touching padics (see above)

 * rings/padics/padic_base_leaves.py:508:    def random_element(self, algorithm='default'):
   *  not touching padics (see above)

 * rings/padics/padic_extension_generic.py:286:    def random_element(self):
   *  not touching padics (see above)

 * rings/polynomial/laurent_polynomial_ring.py:707:    def random_element(self, low_degree = -2, high_degree = 2, terms = 5, choose_degree=False,*args, **kwds):
   *  nothing to fix

 * rings/polynomial/multi_polynomial_ring_generic.pyx:585:    def random_element(self, degree=2, terms=None, choose_degree=False,*args, **kwargs):
   *  (added by #1956) nothing to fix

 * rings/polynomial/pbori.pyx:899:    def random_element(self, degree=None, terms=None, choose_degree=True, vars_set=None):
   *  doesn't call any other random_element() method

 * rings/polynomial/polynomial_quotient_ring.py:591:    def random_element(self, *args, **kwds):
   *  nothing to fix

 * rings/polynomial/polynomial_ring.py:883:    def random_element(self, degree=2, *args, **kwds):
   *  nothing to fix


---

Comment by niles created at 2010-08-23 14:30:23

Changing status from new to needs_review.


---

Attachment


---

Attachment

I rebased the patch to 4.5.3.alpha2 and ran long doctests: all passed. The patch also looks good, the only issue I'd have: I'd either move the lines "Trac#3893 ..." to the TESTS:: section or remove that line completely. I understand that people want to point out where something changed, but that docstring is saying nothing to a user since it is developer information.


---

Comment by niles created at 2010-08-24 16:40:14

Thanks for taking a look!

Somewhere I gained the impression that doctests for a ticket should mention the ticket number--is that not necessarily the case?  I don't really have a strong opinion, but since it may be non-obvious functionality I'm in favor of keeping these tests in the EXAMPLES:: section.  How about rewording the description to something like the following?

`Passes extra positional or keyword arguments through (Trac #3893)::`


---

Comment by malb created at 2010-08-24 16:45:08

Replying to [comment:3 niles]:

> Thanks for taking a look! Somewhere I gained the impression that doctests for a ticket should mention the ticket number--is that not necessarily the case?  I don't really have a strong opinion, but since it may be non-obvious functionality I'm in favor of keeping these tests in the EXAMPLES:: section.  How about rewording the description to something like the following? `Passes extra positional or keyword arguments through (Trac #3893)::`

I'm not sure what the official policy is, but I'd say it would be a bit odd when in a few years time the docstring is cluttered with trac ticket numbers, what information do they communicate that is relevant? I am very much in favour of having "`Passes extra positional or keyword arguments through::`". I leave it up to you, so you have a positive review, i.e. toggle it yourself if you don't want to change it.


---

Attachment

clarified docstrings


---

Comment by niles created at 2010-08-24 21:39:09

Replying to [comment:4 malb]:

> 
> I'm not sure what the official policy is, but I'd say it would be a bit odd when in a few years time the docstring is cluttered with trac ticket numbers

fair enough; I also can't find any mention of a policy like this in the developer guide, so I've changed the docstring as you suggested.  Since I don't have 4.5.3a2 installed, will you re-verify that the patch applies cleanly before hitting "positive review"? (Since the changes were easy, I just made them directly to the rebased patch file itself.)


---

Attachment

rebased to 4.5.3


---

Comment by niles created at 2010-09-21 17:47:18

Changing status from needs_review to positive_review.


---

Comment by niles created at 2010-09-21 17:47:18

rebased patch applies cleanly to 4.5.3; switching to positive review, as per Martin's recommendation


---

Comment by mpatel created at 2010-09-30 02:28:25

With the latest patch applied to a trial 4.6.alpha2, I get two doctest failures:

```python
sage -t -long "devel/sage/sage/rings/contfrac.py"           
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/sage/rings/contfrac.py", line 40:
    sage: a
Expected:
    [    [-1, 2] [-1, 1, 94]      [0, 2]       [-12]]
    [       [-1]      [0, 2]  [-1, 1, 3]   [0, 1, 2]]
    [    [-3, 2]   [0, 1, 2]        [-1]         [1]]
    [       [-1]      [0, 3]         [1]        [-1]]
Got:
    [    [-1, 2] [-1, 1, 94]      [0, 2]       [-12]]
    [       [-1]      [0, 2]  [-1, 1, 3]   [0, 1, 2]]
    [    [-3, 2]         [0]   [0, 1, 2]        [-1]]
    [        [1]        [-1]      [0, 3]         [1]]
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1-working/devel/sage/sage/rings/contfrac.py", line 46:
    sage: f
Expected:
    [1]*x^4 + [2]*x^3 + ([-12, 1, 14, 7, 1, 1, 7])*x^2 + ([-40, 2, 32, 2, 1, 1, 2])*x + [8, 1, 5, 2, 14, 1, 1, 3]
Got:
    [1]*x^4 + ([-2, 3])*x^3 + [14, 1, 1, 1, 9, 1, 8]*x^2 + ([-13, 4, 1, 2, 1, 1, 1, 1, 1, 2, 2])*x + [-6, 1, 5, 9, 1, 5]
**********************************************************************
```

Perhaps there's an interaction with one of the [already merged tickets](http://trac.sagemath.org/sage_trac/query?order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&merged=~sage-4.6.alpha2)?


---

Comment by mpatel created at 2010-09-30 02:30:09

Changing status from positive_review to needs_info.


---

Comment by niles created at 2010-09-30 12:24:57

addressed interaction with #8955


---

Comment by niles created at 2010-09-30 12:29:36

Changing keywords from "" to "random_element, args, kwds".


---

Attachment

Indeed; the interaction seems to be with #8955: after applying those patches, I get exactly the same doctest failures, with exactly the same "Got" output.  I just uploaded a fixed patch which passes all doctests after applying #8955.


---

Comment by niles created at 2010-09-30 12:29:36

Changing status from needs_info to needs_review.


---

Comment by mpatel created at 2010-10-03 09:30:12

Martin, could you review the latest patch?  If it's OK, I'll merge it into 4.6.alpha3.


---

Comment by malb created at 2010-10-03 14:56:02

The updated patch applies with some fuzz, but it applies. Doctests pass. I trust only doctest failures were addressed and thus I give this a positive review.


---

Comment by malb created at 2010-10-03 14:56:02

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-04 02:48:24

Resolution: fixed
