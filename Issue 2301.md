# Issue 2301: Bug in sage_flattened_str_list

Issue created by migration from https://trac.sagemath.org/ticket/2301

Original creator: SimonKing

Original creation time: 2008-02-25 11:19:35

Assignee: malb

CC:  was

Keywords: ringlist, sage_structured_str_list

When playing around with `ringlist`, i found a bug the method `sage_structured_str_list`:


```
sage: R=singular.ring(0,'(x1,x12,x2)','dp')
sage: RL=R.ringlist()
sage: RL

[1]:
   0
[2]:
   [1]:
      x1
   [2]:
      x12
   [3]:
      x2
[3]:
   [1]:
      [1]:
         dp
      [2]:
         1,1,1
   [2]:
      [1]:
         C
      [2]:
         0
[4]:
   _[1]=0
sage: RL.sage_structured_str_list()
[[], [], [], [], [], [], [], [], [], [], [], [], ['0']]
sage: RL.sage_flattened_str_list()
['0', 'x1', 'x12', 'x2', 'dp', '1,1,1', 'C', '0', '_[1]=0']
```




---

Comment by malb created at 2008-02-25 11:25:21

Changing component from commutative algebra to interfaces.


---

Comment by malb created at 2008-02-25 11:25:21

Changing assignee from malb to was.


---

Comment by SimonKing created at 2008-02-26 07:48:49

Sorry, the bug is in sage_*structured*_str_list, rather than in ..._flattened_...


---

Comment by SimonKing created at 2008-02-26 08:30:39

With the attached patch, the following works:

```
sage: R=singular.ring(0,'(x,y)','dp')
sage: R.ringlist().sage_structured_str_list()
['0', ['x', 'y'], [['dp', '1,\n1 '], ['C', '0 ']], '0']
sage: R.ringlist().sage_flattened_str_list()
['0', 'x', 'y', 'dp', '1,1', 'C', '0', '_[1]=0']
```


The suggested algorithm is recursive, and it is easy to see that if `L` is a singular list of (singular lists of (...)) then `L.sage_structured_list()` returns a sage list of lists mimicking `L`'s structure, so that any non-list component of `L` is represented as a string.

The following might be a disadvantage:
 * If `L` is very (i mean: *very*) deeply nested, there might be trouble with the recursion limit.
 * The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.

It may be a matter of taste whether the first or second string representation is preferred, and i think it would not be difficult to achieve the other representation. Opinions?


---

Comment by SimonKing created at 2008-02-26 09:15:46

Replying to [comment:3 SimonKing]:
> It may be a matter of taste whether the first or second string representation is preferred, and i think it would not be difficult to achieve the other representation. 

Here is how to obtain the other representation: In the patch, replace `return str(self)` by `return '\n'.join(x.strip() for x in self.list().__str__().split('\n')[1:])`


---

Comment by malb created at 2008-02-26 09:51:32

> The following might be a disadvantage:
>  * If `L` is very (i mean: *very*) deeply nested, there might be trouble with the recursion limit.

I don't think that this would be an issue in practice.

>  * The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.

I don't like the second representation because it doesn't look like valid Singular outside a list? But if that is the format Singular accepts when we play the list of lists back to it then we should go for this representation.


---

Comment by SimonKing created at 2008-02-26 10:33:29

Replying to [comment:5 malb]:
> >  * The example shows that `sage_flattened_str_list` and my suggestion for `sage_structured_str_list` are based on different string representations of the list components. E.g., in the example, the last component is a 0-ideal. Printing a 0-ideal yields the string `'0'` (see above in `sage_structured_str_list`), but if the 0-ideal is part of a list then printing the list would represent the 0-ideal in the form `'_[0]=0'` (see above in `sage_flattened_str_list`). Similarly, an `intvec` would be represented in two different ways.
> 
> I don't like the second representation because it doesn't look like valid Singular outside a list? But if that is the format Singular accepts when we play the list of lists back to it then we should go for this representation.

*Both* represantations can not be played back. 

Example 1: The first version of representing `intvec(1,1)` is `'1,\n1'` -- but `singular('1,\n1')` results in hanging up. The second version would represent `intvec(1,1)` as `'1,1'` -- but `singular('1,1')` is a list and not an intvec. 

Example 2: `singular.ideal('x','y')` would either be represented by `'x,\ny'` (first version) or by `'_[1]=x\n_[2]=y'` (second version). Both is not valid for `singular(...)`.

So i think it is really just a matter of taste. To return strings that can be used for defining the represented objects would involve much more work, unless there is a simple Singular command that provides such string. Do you know any?


---

Comment by malb created at 2008-02-26 11:27:05

> *Both* represantations can not be played back. 
> 
> Example 1: The first version of representing `intvec(1,1)` is `'1,\n1'` -- but `singular('1,\n1')` results in hanging up. The second version would represent `intvec(1,1)` as `'1,1'` -- but `singular('1,1')` is a list and not an intvec. 
> 
> Example 2: `singular.ideal('x','y')` would either be represented by `'x,\ny'` (first version) or by `'_[1]=x\n_[2]=y'` (second version). Both is not valid for `singular(...)`.
> 
> So i think it is really just a matter of taste. To return strings that can be used for defining the represented objects would involve much more work, unless there is a simple Singular command that provides such string. Do you know any?

Unfortunately I don't know such a function. But I see the point that it is a matter of taste. However, I still prefer the first option because `_[1] = 0` depends on the index of the list ([1]) while just `0` doesn't.


---

Comment by malb created at 2008-02-26 11:31:36

*Referee Report*:
 * Could you add doctests to `sage_structured_str_list` like the examples in the description of the ticket?
 * Does `make test` still pass after the change? In particular does `sage -t schemes/plane_curves/projective_curve.py` still pass? This seems to be the only place this method is called.


---

Attachment

Replying to [comment:8 malb]:
> *Referee Report*:
>  * Could you add doctests to `sage_structured_str_list` like the examples in the description of the ticket?

Done.

>  * Does `make test` still pass after the change? In particular does `sage -t schemes/plane_curves/projective_curve.py` still pass? This seems to be the only place this method is called.

I'm afraid this test fails.

But i believe the function `riemann_roch_basis` only works because it expects a behaviour of `sage_structured_str_list` _that does not fit to its specification_.

To be precise: Taking the example of `riemann_roch_basis`, the function internally computes `LG = G.BrillNoether(X2)`, which is printed as

```
[1]:
   _[1]=x
   _[2]=y
[2]:
   _[1]=1
   _[2]=1
[3]:
   _[1]=z
   _[2]=y
[4]:
   _[1]=z^2
   _[2]=y^2
[5]:
   _[1]=z
   _[2]=x
[6]:
   _[1]=z^2
   _[2]=x*y
```


Then, `sage_structured_str_list` is applied to this thing, and yields

```
[['x', 'y'], ['1', '1'], ['z', 'y'], ['z^2', 'y^2'], ['z', 'x'], ['z^2', 'x*y']]
```


I believe this output is wrong, since `LG[1]` is not a singular list, hence, must be represented as a string and not as a sage list.

I see two ways to resolve it:

1. Change `riemann_roch_basis`, since it relies on getting a _wrong_ answer from `sage_structured_str_list`

2. Change `sage_structured_str_list` so that not only singular lists are turned into a sage list, but also singular ideals and intvecs are turned into lists.

I prefer the first option, since the second option clearly violates the specification of `sage_structured_str_list`.

Anyway, i think we will only be able to fix the bug later.


---

Comment by malb created at 2008-02-27 00:15:08

> 1. Change `riemann_roch_basis`, since it relies on getting a _wrong_ answer from `sage_structured_str_list`
> 
> 2. Change `sage_structured_str_list` so that not only singular lists are turned into a sage list, but also singular ideals and intvecs are turned into lists.
> 
> I prefer the first option, since the second option clearly violates the specification of `sage_structured_str_list`.

This seems reasonable, however we should contact the original author (I don't know this area of the code). I assume it is William whom I hereby CC.
 
> Anyway, i think we will only be able to fix the bug later.

Until we have figured this one out I think we shouldn't merge the patch. However, this seems to be something that can be resolved quickly.


---

Attachment


---

Attachment


---

Comment by SimonKing created at 2008-02-27 09:04:40

Replying to [comment:10 malb]:
> > Anyway, i think we will only be able to fix the bug later.
> 
> Until we have figured this one out I think we shouldn't merge the patch. However, this seems to be something that can be resolved quickly.

I think i did fix it.

First of all, the patch for `sage_structured_str_list` should be replaced by patch number 2, because in the first patch i had a mistake in the doctest.

Then, i attached a patch for `riemann_roch_basis`. The point is that internally `riemann_roch_basis` computes something that apparently is known to be a list of ideals with two generators. We know how these are dealt with by the new version of `sage_structured_str_list`. Hence, changing one line of `riemann_roch_basis` suffices.

Oops, i just see that i attached the patch twice...

Anyway. With the patches `sage_structured_str_list2.patch` and with either patch for `riemann_roch_basis`, all doc tests for `singular.py` and for `projective_curve.py` pass.

Moreover, i can not find any other place where `sage_structured_str_list` or `riemann_roch_basis` are used.


---

Comment by SimonKing created at 2008-02-27 09:14:38

Replying to [comment:7 malb]:
> Unfortunately I don't know such a function. But I see the point that it is a matter of taste. However, I still prefer the first option because `_[1] = 0` depends on the index of the list ([1]) while just `0` doesn't.

And, by the way, i prefer the first option as well, and the patches work accordingly.


---

Comment by malb created at 2008-02-27 11:10:13

Patches look good. Positive review.


---

Comment by mabshoff created at 2008-02-27 11:24:02

No dice:

```
sage$ hg import sage_structured_str_list.2.patch
applying sage_structured_str_list.2.patch
abort: malformed patch sage/interfaces/singular.py @@ -1089,20 +1089,39 @@ class SingularElement(ExpectElement):
```

Can you repost the patches and delete all the old ones?

Cheers,

Michael


---

Comment by SimonKing created at 2008-02-27 11:52:12

Replying to [comment:14 mabshoff]:
> No dice:
> {{{
> sage$ hg import sage_structured_str_list.2.patch
> applying sage_structured_str_list.2.patch
> abort: malformed patch sage/interfaces/singular.py `@``@` -1089,20 +1089,39 `@``@` class SingularElement(ExpectElement):
> }}}

I guess this is since i made the mistake to manually edit the patch.

> Can you repost the patches and delete all the old ones?

I don't know how i can delete an attachment.

Nor do i understand what happens. I did `hg_sage.pull()` followed by `hg_sage.update()`, and i expected to get `singular.py` so that `sage_structured_str_list` is in its old state.

But what i pulled from the official repository did already contain my patch for `sage_structured_str_list`, with the corrected doc test.

Could you verify whether in the official repository the lines 1117-1151 look like that:

```
    def sage_structured_str_list(self):
        """
        If self is a Singular list of lists of Singular elements,
        returns corresponding SAGE list of lists of strings.

        EXAMPLES:
            sage: R=singular.ring(0,'(x,y)','dp')
            sage: RL=R.ringlist()
            sage: RL
            [1]:
               0
            [2]:
               [1]:
                  x
               [2]:
                  y
            [3]:
               [1]:
                  [1]:
                     dp
                  [2]:
                     1,1
               [2]:
                  [1]:
                     C
                  [2]:
                     0
            [4]:
               _[1]=0
            sage: RL.sage_structured_str_list()
            ['0', ['x', 'y'], [['dp', '1,\n1 '], ['C', '0 ']], '0']
        """
        if not (self.type()=='list'):
            return str(self)
        return [X.sage_structured_str_list() for X in self]
```

This is how they should be *after* applying my patch. 

Anyway, i think i need an advice how to make a clean patch.


---

Comment by malb created at 2008-02-27 11:58:56

* I just wrote a new patch, waiting for `make test` to finish, so don't bother with this one Simon
 * to make a new patch you have to remove the patch you already checked in locally. `pull()` will not help since it only adds the patches found upstream but does not remove the ones you already have. 
 * I usually work with branches and if one goes FUBAR I just start with a clean main branche and clone that
 * or you could use the HG queues, don't know how those work though.


---

Comment by wdj created at 2008-02-27 12:12:00

There is a riemann_roch_basis function in both schemes/plane_curves/affine_curve.py
and schemes/plane_curves/projective_curve.py. I think William Stein and I wrote them.
(I need it for AG codes, coding/ag_code.py.) As of a few years ago, riemann_roch_basis
was unreliable in the sense that Singular would not return the same (and consistent)
answers to the same input. I don't remember the counterexamples but could try to dig them
up in old emails. These were reported to the Singular authors. Maybe it's fixed now?
Anyway, I strongly hope that this gets fixed if it hasn't been and thanks *very much* 
for working on this.


---

Comment by malb created at 2008-02-27 13:01:23

replaces all other patches attached to this ticket


---

Attachment

mabshoff, please apply `trac_2301_superpatch.patch` it contains *exactly* the same code as Simon's patches. Credits go to Simon King. `make test` passes.


---

Comment by SimonKing created at 2008-02-27 13:48:12

Replying to [comment:18 malb]:
> mabshoff, please apply `trac_2301_superpatch.patch` it contains *exactly* the same code as Simon's patches. Credits go to Simon King. `make test` passes.

Thank you for your help!


---

Comment by SimonKing created at 2008-02-27 14:23:50

Replying to [comment:17 wdj]:
> As of a few years ago, riemann_roch_basis
> was unreliable in the sense that Singular would not return the same (and consistent)
> answers to the same input. 

Still the second doctest example has random result. Or do you mean something else?

> Maybe it's fixed now?
> Anyway, I strongly hope that this gets fixed if it hasn't been and thanks *very much* 
> for working on this.

I don't know if it is fixed on the Singular side. I can only say: If Singular returns a list of ideals with two generators then I believe my patch for the `riemann_roch_basis` in `projective_curve.py` works.

Could you review the Riemann-Roch part of `trac_2301_superpatch.patch`? The positive review of malb refers to the bug in `sage_structured_str_list`, but a review for the other part is still missing, as far as i understand.


---

Comment by mabshoff created at 2008-02-27 21:28:53

Merged trac_2301_superpatch.patch in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-27 21:28:53

Resolution: fixed


---

Comment by mabshoff created at 2008-02-27 21:30:32

Simon,

please open another ticker for "Follow-up bug in riemann_roch_basis" - if it is a separate issue we prefer to do it that way. Otherwise tickets get too complicated and we can only close them when all issues have been resolved.

Cheers,

Michael


---

Comment by wdj created at 2008-02-28 02:36:27

This appears to cause a failure in another module:

sage -t  devel/sage-rrspace/sage/interfaces/singular.py
**********************************************************************
File "singular.py", line 1117:
   sage: RL.sage_structured_str_list()
Expected:
   ['0', ['x', 'y'], [['dp', '1,\n1 '], ['C', '0 ']], '0']
Got:
   [[], [], [], [], [], [], [], [], [], [], [], ['0']]
**********************************************************************


---

Comment by wdj created at 2008-02-28 11:35:20

Ignore my last comment. (I ran the test incorrectly.)


---

Comment by SimonKing created at 2008-02-28 12:10:13

Replying to [comment:23 mabshoff]:
> please open another ticker for "Follow-up bug in riemann_roch_basis" - if it is a separate issue we prefer to do it that way. 

Next time i will do so. 
I did not open a new ticket because it was the new version of `sage_structured_str_list` that made `riemann_roch_basis` fail, and so i thought that this follow-up still belongs to the same ticket.

Anyway. The doctests for both `singular.py` and `projective_curve.py` pass in `sage-2.10.3.rc0`, so i think it is ok to leave the ticket closed. 

Since the problem seems solved, i also think it is not needed to open a new ticket for `riemann_roch_basis`, or am i mistaken?


---

Comment by mabshoff created at 2008-02-29 16:29:44

Replying to [comment:26 SimonKing]:
 
> Since the problem seems solved, i also think it is not needed to open a new ticket for `riemann_roch_basis`, or am i mistaken?

I am under the impression that malb's patch merged all your patches, but please verify with 2.10.3.rc0. If some code didn't make it in please open another ticket and post the new patch(es) there and mention in the description that it is a merge leftover from this ticket.

Cheers,

Michael


---

Comment by SimonKing created at 2008-02-29 22:29:41

Replying to [comment:27 mabshoff]:
> I am under the impression that malb's patch merged all your patches, but please verify with 2.10.3.rc0. 

Yes, everything is in.
