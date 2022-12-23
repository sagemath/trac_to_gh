# Issue 5968: increase doctest coverage of sage/modular/modsym/modular_symbols.py from 0% to 100%

Issue created by migration from https://trac.sagemath.org/ticket/5968

Original creator: was

Original creation time: 2009-05-03 03:18:16

Assignee: was

CC:  cremona




---

Attachment


---

Attachment


---

Comment by davidloeffler created at 2009-05-04 09:15:17

I have one microscopically insignificant quibble: might it not be better to add a couple of minus signs into the `__cmp__` method, changing it to 

```
if not isinstance(other, ModularSymbol):
    return cmp(type(self), type(other))
return cmp((self.__space,-self.__i,self.__alpha,self.__beta),
           (other.__space,-other.__i,other.__alpha,other.__beta))
```

?

This is somehow the sort order that "feels most natural" to me -- so X<sup>2</sup>Y comes before XY<sup>2</sup>. This would then need fewer changes to other files, but of course it means most of the new doctests in your file would need rewriting :-). Also, what is the reasoning behind introducing the space in the `_repr_` method? I would advocate leaving `_repr_` as is unless there is a pressing reason to change it, in order to minimise the likelihood of breaking user code.


---

Comment by davidloeffler created at 2009-05-04 14:36:58

Apply over previous two patches


---

Attachment

The new patch above adds the suggested minus sign to give a more "natural" sort order, and adjusts the doctests accordingly; I've checked that with this modification all doctests still pass on my machine (32-bit Linux). I take back my comment about the `_repr_` method: all the native Python sequence types print with spaces in, so I agree that a space in modular symbols is better for consistency, and it certainly looks nicer.

In the process of fixing this I realised that the file `modular_symbols.py` isn't included in the reference manual, so the new patch does that too (and includes some ReST syntax fixes, so the manual page builds correctly and looks nice-ish). 

William: I'm happy with your changes, so if you're happy with my subsequent ones, I guess we can call this a positive review.


---

Comment by davidloeffler created at 2009-05-10 21:57:06

Changing component from number theory to modular forms.


---

Comment by davidloeffler created at 2009-05-10 21:57:06

William: just in case you've forgotten about this ticket, it would be good if you could take a quick glance at the changes I made in my third patch above.

BTW, I'm moving this ticket to component "modular forms", which seems to be a better fit for it.


---

Comment by davidloeffler created at 2009-05-10 21:57:06

Changing assignee from was to craigcitro.


---

Comment by mabshoff created at 2009-05-15 14:36:13

What is the status here? Let's get it into 4.0 :)

Cheers,

Michael


---

Comment by davidloeffler created at 2009-05-15 14:59:23

I'm waiting for was or somebody else to OK my patch (the third one), which just adds a minus sign and changes doctests to match. I've asked John Cremona (cc'ed) to have a look at it if he gets a chance.


---

Comment by cremona created at 2009-05-15 15:03:32

I am doing it *now*!


---

Comment by cremona created at 2009-05-15 15:29:05

Review: applied all 3 patches to 3.4.2 with no problem.  All tests in sage/modular and doc/en/bordeaux_2008 pass.  This is on a 64-bit machine.

I did not build the documentation (it takes such ages)  but looking at the docstrings could not see anything wrong.

Let's roll!


---

Comment by mabshoff created at 2009-05-16 01:02:34

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-16 01:02:34

Resolution: fixed
