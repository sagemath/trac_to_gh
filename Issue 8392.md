# Issue 8392: Check when defining a permutation by one-line notation (list of int)

Issue created by migration from https://trac.sagemath.org/ticket/8392

Original creator: nborie

Original creation time: 2010-02-27 21:04:24

Assignee: nborie

CC:  sage-combinat billey

Keywords: permutation, check, assert

Just check the user give a good entry and for that move a method (robinson_schensted)

For now, sage accept that:

```
sage: Permutation([1,1,1,1,1])
[1, 1, 1, 1, 1]
sage: Permutation([-12,1,3])
[-12, 1, 3]
```



---

Attachment


---

Comment by hivert created at 2010-03-02 18:20:48

Changing status from new to needs_work.


---

Comment by hivert created at 2010-03-02 18:20:48

Hi Nicolas,

If you want your patch to be reviewed please check "needs review"...

For your information your patch breaks posets which use permutations starting from 0:

```
    sage: P = Posets.SymmetricGroupBruhatIntervalPoset([0,1,2,3], [2,3,0,1])
Exception raised:
...
    ValueError: [0, 1, 2, 3] is not a Standard permutations
```



---

Comment by nborie created at 2010-03-02 18:35:30

This patch is just a begining. I didn't check the 'needs review'. But really for now, I need the advises from any Veteran of combinatorics software.... 

See http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/c6a39caca9df29dc

Thanks in advance.


---

Comment by nthiery created at 2012-05-09 14:44:55

The current patch breaks integer vectors; it would need to further fix WeightedIntegerVectors to not abuse anymore Permutation with multiple entries.


```
sage: WeightedIntegerVectors(8, [1,1,2]).list()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/categories/finite_enumerated_sets.py", line 308, in list
    self._list = self._list_from_iterator()
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/categories/finite_enumerated_sets.py", line 142, in _list_from_iterator
    return [x for x in self]
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/integer_vector_weighted.py", line 259, in __iter__
    yield perm._left_to_right_multiply_on_right(Permutation_class(x))
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/permutation.py", line 910, in _left_to_right_multiply_on_right
    #Pad the permutations if they are of
  File "/opt/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/combinat/permutation.py", line 286, in Permutation
    if n != len(l) or sorted(l) != range(1,n+1):
ValueError: the list l (=[0, 0, 4]) must contain each integer of {1,...,n} one time
```



---

Comment by tscrim created at 2012-05-10 02:24:40

Changing assignee from nborie to tscrim.


---

Comment by tscrim created at 2012-05-10 02:24:40

Taking over to work on for Sage Days 38.


---

Comment by tscrim created at 2012-05-10 02:24:40

Changing keywords from "permutation, check, assert" to "permutation, check, assert, days38".


---

Comment by tscrim created at 2013-02-01 13:32:24

I'm going to recycle this ticket due to #13742.


---

Comment by tscrim created at 2013-02-01 13:32:24

Changing keywords from "permutation, check, assert, days38" to "permutation, check, days38".


---

Comment by tscrim created at 2013-02-13 21:30:00

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by tscrim created at 2013-02-13 21:30:00

Changing keywords from "permutation, check, days38" to "permutation, check, days38, days45".


---

Comment by tscrim created at 2013-02-13 21:30:00

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-02-15 01:06:01

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by tscrim created at 2013-02-15 16:11:04

Fixed doctests and updated documentation.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by vdelecroix created at 2013-02-15 17:04:20

Hi,

The name of the ticket has nothing to do with what the ticket contains. You must change either one or the other !

Your changes to Word are not valid. Imagine that I am working on the alphabet of tableaux and I want a word of length two (containing two tableaux)...

Two comments, some others will come later
 * sage/combinat/permutation.py, line 2905 you may change the ugly izip(list(range(1, len(self)+1)), self) with izip(xrange(1,len(self)+1), self)
 * sage/combinat/rsk.py, line 114 "an method" -> "a method"

Vincent


---

Comment by tscrim created at 2013-02-16 00:42:38

I've made the changes. Now to construct a word using RSK, one will use the optional argument `RSK_data`.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by tscrim created at 2013-02-16 00:43:12

Changing type from defect to enhancement.


---

Comment by tscrim created at 2013-02-16 04:31:38

Vincent has told me that he is okay with the documentation and current implementation but cannot review the math. I'm cc-ing Sara since she was interested in this patch.


---

Comment by tscrim created at 2013-02-19 15:17:29

Rebased on #6495.


---

Comment by tscrim created at 2013-02-22 19:01:43

Minor documentation tweaks which depend on #13605.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by tscrim created at 2013-02-22 19:02:50

Forgot to refresh...

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by tscrim created at 2013-03-07 17:43:54

Added Edelman-Greene insertion to the patch as well.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by tscrim created at 2013-04-15 15:47:24

Rebased over #8703.


---

Comment by tscrim created at 2013-05-08 15:38:18

Rebased over #14459.


---

Comment by tscrim created at 2013-05-09 14:33:12

Rebased over #14319 due to minor docstring conflicts.


---

Comment by tscrim created at 2013-05-09 14:34:17

For patchbot:

Apply trac_8392-check_permutation-ts.patch


---

Comment by darij created at 2013-05-12 04:55:16

I'm fussing about corner cases as usual, but I think this here might use some fix:

```
sage: Permutation([])  # This is be the identity permutation in S_0.
[]
sage: Permutation([]).cycle_string()    # OK.
'()'
sage: Permutation('()')    # This should give the S_0 identity back -- but it doesn't.
[1]
sage: Permutation('')     # Does this maybe? No.
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-29-3df27d9d4d7a> in <module>()
----> 1 Permutation('')

/home/darij/sage-5.10.beta2/local/lib/python2.7/site-packages/sage/combinat/permutation.pyc in Permutation(l, check_input)
    430         cycle_list = []
    431         for c in cycles:
--> 432             cycle_list.append(map(int, c.split(",")))
    433 
    434         return from_cycles(max([max(c) for c in cycle_list]), cycle_list)

ValueError: invalid literal for int() with base 10: ''
sage: Permutation(())       # What about this?
[1]
```


Travis, why did you replace "standard" by "semi-standard" in ``robinson_schensted``?


---

Comment by darij created at 2013-05-12 06:45:41

apply after trac_8392-check_permutation-ts.patch


---

Attachment

I've just reviewed the math: [attachment:trac_8392-review_patch-dg.patch].

Documentation extended (please check my formatting!), Edelman-Greene insertion fixed (it used to do the same as normal RSK), an is_increasing() method for tableaux added (since we're already doing Edelman-Greene...), and some more doc fixes made (including the changes that were formerly in #14131).

I have not fixed the issues in my previous comment; I don't know our stance on them.


---

Comment by tscrim created at 2013-05-14 22:16:25

Hey Darij,

I've folded your review patch in and made some additional tweaks to the docs. I can't believe how badly I coded the EG insertion. I reverted it back to standard since when I first wrote this patch, permutations could take inputs with repetition.

As for your previous comment, that is outside of the scope of this patch since it deals with input for permutations. I think there already is a ticket about this somewhere (or related to it), but I don't remember the number off hand.

Best,

Travis


---

Comment by tscrim created at 2013-05-14 22:17:20

I also deprecated the `robinson_schensted()` method for permutations.

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by jferreira created at 2013-05-18 22:23:59

Travis -

A couple quick comments on the documentation:

In the docstring for sage.combinat.rsk.RSK:

- In the first paragraph "as known as two-line..." should be "also known as two-line..." ?

-In your description of the algorithm p and q are first referenced as your insertion and recording tableaux and then they become P and Q in the next paragraph and in this paragraph p appears to be a generalized permutation.

In the docstring for sage.combinat.rsk.RSK_inverse:

- I think you forgot a colon at the end of the sentence beginning "Same for Edelman-Greene ..."

Haven't played with the functions yet (except for your examples), but plan to soon.

-Jeff



---

Comment by tscrim created at 2013-05-19 01:12:53

Hey Jeff,

Thanks for catching that. Fixed.

Best,

Travis


---

Comment by jferreira created at 2013-05-22 22:11:45

Travis,

Can you add some more checks for invalid input? For example there is no problem doing this:


```
sage: RSK([1],[1,2])  # Words are different length
sage: RSK([2,1],[1,1])  # Not a generalized permutation

```

I am using the definition of generalized permutation in Stanley EC2 Chapter 7.

- Jeff


---

Comment by tscrim created at 2013-05-24 01:18:51

Hey Jeff,

I added the extra safety checks.

Best,

Travis


---

Comment by jferreira created at 2013-05-24 19:01:23

Looks good. It's going to be nice to have these functions around.


---

Comment by jferreira created at 2013-05-24 19:01:23

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-05-24 19:08:19

Jeff, thanks for doing the final review. Darij thanks for doing the initial review.


---

Comment by tscrim created at 2013-05-25 02:17:29

Rebased to `5.10.beta4` (some fuzz).

For patchbot:

Apply: trac_8392-check_permutation-ts.patch


---

Comment by jdemeyer created at 2013-05-27 13:43:10


```
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:121: WARNING: Duplicate explicit target name: "knu1970".
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:126: WARNING: Duplicate explicit target name: "eg1987".
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:121: WARNING: duplicate citation Knu1970, other instance in /mazur/release/merger/sage-5.10.rc0/devel/sage/doc/en/reference/combinat/sage/combinat/rsk.rst
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.rc0/local/lib/python2.7/site-packages/sage/combinat/rsk.py:docstring of sage.combinat.rsk.RobinsonSchenstedKnuth:126: WARNING: duplicate citation EG1987, other instance in /mazur/release/merger/sage-5.10.rc0/devel/sage/doc/en/reference/combinat/sage/combinat/rsk.rst
```



---

Comment by jdemeyer created at 2013-05-27 13:43:10

Changing status from positive_review to needs_work.


---

Comment by tscrim created at 2013-05-27 20:23:07

Changing status from needs_work to positive_review.


---

Comment by tscrim created at 2013-05-27 20:23:07

Fixed. Errors were due to references being in a function that had an alias.


---

Comment by jdemeyer created at 2013-05-28 12:58:48

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-05-28 12:58:48

This needs to be rebased such that it applies on top of #14302.


---

Comment by tscrim created at 2013-05-28 14:49:08

Rebased


---

Attachment

Rebased over #14302.


---

Comment by tscrim created at 2013-05-28 14:49:30

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-06-06 12:31:11

Resolution: fixed


---

Comment by saliola created at 2013-08-17 17:31:51

Thanks for writing this patch. I support the proposed clean up of the code, but I want to raise an objection to choices in the user interface:

- I don't think that it is useful to deprecate the method `robinson_schensted`:

  {{{
  DeprecationWarning: p.robinson_schensted() is deprecated. Use instead RSK(p)
  }}}

  Telling users to use the RSK function instead of a method is not in the spirit of object-oriented programming. More importantly, it is totally unnecessary to deprecate the method.

- Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.

- Perhaps these names should not be capitalized since they are python functions and not classes. See the [developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).


---

Comment by aschilling created at 2013-08-17 17:35:24

I agree with Franco's comments!

Anne


---

Comment by saliola created at 2013-08-17 18:03:27

- The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is `[3,3,2]` mean with EG insertion? Since it isn't a reduced word, how should this be interpreted? It's not invertible either:

```
sage: P, Q = RSK([3,3,2], insertion='EG')
sage: P
[[2, 3], [3]]
sage: Q
[[1, 2], [3]]
sage: RSK_inverse(P, Q, insertion='EG')
word: 232
```


- I would have expected that the output of `RSK` could be used as input to `RSK_inverse`:

```
sage: RSK_inverse(RSK([1,2]))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-154-cb6c9a6f810d> in <module>()
----> 1 RSK_inverse(RSK([Integer(1),Integer(2)]))

TypeError: RSK_inverse() takes at least 2 arguments (1 given)
```



---

Comment by tscrim created at 2013-08-18 16:02:28

Hey Franco,

Replying to [comment:38 saliola]:
> Thanks for writing this patch. I support the proposed clean up of the code, but I want to raise an objection to choices in the user interface:
> 
> - I don't think that it is useful to deprecate the method `robinson_schensted`:
> 
>   {{{
>   DeprecationWarning: p.robinson_schensted() is deprecated. Use instead RSK(p)
>   }}}
> 
>   Telling users to use the RSK function instead of a method is not in the spirit of object-oriented programming. More importantly, it is totally unnecessary to deprecate the method.

If we wanted to be fully OOP, then there needs to be a class of something like `RSKUsable` which has an abstract method `RSK()` where each type of object implements it's own version of RSK and `RSKUsable` would implement the row-insertion procedure. The problem with this is that we want to be able to handle (pairs of) lists, which we can't modify its class structure and I don't want to have to wrap a list as a word, and I also don't want to clutter up the MRO. Another reason why this is better as a function is most of the operation is independent of the type of object being passed in; all it does is it converts it into a pair of lists of the same size. Thus it provides a uniform interface for objects, and the fact that only permutations has such a method conflicts with this, so I think it is worthwhile to deprecate this.

> - Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.

Then what is your proposed interface? If the input is a pair of tableaux as a list or is given as input 2 tableaux, then run the inverse? Hence we should combine two functions which do completely different behavior into one as I think of RSK as a procedure in 1 direction? What about if someone only thinks of this as the Robinson-Schensted bijection and tries `RobinsonSchestead<tab>`? This is why I setup these aliases and imported them.

> - Perhaps these names should not be capitalized since they are python functions and not classes. See the [developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).

For the full name, probably yes it should be changed. For the shortname `RSK`, it is an acronym, so I think it is better and more likely to be found than `rsk`. See the bottom of [this section of the developers guide](http://www.sagemath.org/doc/developer/conventions.html?highlight=camelcase#python-coding-conventions).

> The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is [3,3,2] mean with EG insertion? Since it isn't a reduced word, how should this be interpreted?

The documentation could use some expansion.

> I would have expected that the output of RSK could be used as input to RSK_inverse:

This is because it's more logical to me for the input to be 2 arguments where we can explicitly specify what they are (as arguments), than a single parameter taking a list and checking to make sure it has length 2 and explaining the (non-standard IMO) input form in the docsting. We could handle both forms of input, but this seems overly complicated, and I imagine python programmers would simply use the `*` to expand the list as inputs as in the EG examples. This could probably use another example (maybe so far as a docstring explanation, but I'm hesitant about that) that's not for EG insertion.

Best,

Travis


---

Comment by aschilling created at 2013-08-19 06:55:19

Hi Travis,

Replying to [comment:41 tscrim]:
> If we wanted to be fully OOP, then there needs to be a class of something like `RSKUsable` which has an abstract method `RSK()` where each type of object implements it's own version of RSK and `RSKUsable` would implement the row-insertion procedure. The problem with this is that we want to be able to handle (pairs of) lists, which we can't modify its class structure and I don't want to have to wrap a list as a word, and I also don't want to clutter up the MRO. Another reason why this is better as a function is most of the operation is independent of the type of object being passed in; all it does is it converts it into a pair of lists of the same size. Thus it provides a uniform interface for objects, and the fact that only permutations has such a method conflicts with this, so I think it is worthwhile to deprecate this.

If a user makes a permutation p, it would be natural to try p.<tab completion> to see all methods. Currently p.robinson_schensted() works and it is the most natural entry point. There is no reason to deprecate this method, it can just be a one-line function returning RSK(p).

> > - Also, I disagree with importing `RSK, RSK_inverse, RobinsonSchenstedKnuth, RobinsonSchenstedKnuth_inverse` into the global namespace when one object could easily handle all of these.
> 
> Then what is your proposed interface? 

Couldn't you just use options for the inverse?

> > The ability of doing RSK and EG is a great feature, but the documentation isn't very clear. What is [3,3,2] mean with EG insertion? Since it isn't a reduced word, how should this be interpreted?
> 
> The documentation could use some expansion.

Right now it is not clear at all that the input to the Edelman-Greene correspondence are reduced words. Also, if you want to put all insertion algorithms in one method, it might be better to call it insertion_algorithms rather than RSK since RSK is just one of them and I as a user would not think that Edelman-Greene would be under RSK. Or you should have Edelman-Greene as a different method. Plus the documentation definitely needs more details! At least you need to explain what the input is with the various options.

Best,

Anne
