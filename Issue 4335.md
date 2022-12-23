# Issue 4335: Labelling of newforms

Issue created by migration from https://trac.sagemath.org/ticket/4335

Original creator: ljpk

Original creation time: 2008-10-21 19:15:07

Assignee: craigcitro

Given a space of CuspForms, there is a newforms method which gives a list of newforms associated to that space, with a name specified by the user. However, this does not seem to work correctly at the moment:

```
sage: S=CuspForms(23)
sage: S.newforms('b')
[q + a0*q^2 + (-2*a0 - 1)*q^3 + (-a0 - 1)*q^4 + 2*a0*q^5 + O(q^6)]
```


I think that the newforms code should be changed to something like:

```
def newforms(self, names=None):
        """
        Return all cusp forms in the cuspidal subspace of self.
        
        EXAMPLES:
        
        sage: CuspForms(23).newforms('b')
        [q + b0*q^2 + (-2*b0 - 1)*q^3 + (-b0 - 1)*q^4 + 2*b0*q^5 + O(q^6)]
        """
        M = self.modular_symbols(sign=1)
        factors = M.cuspidal_subspace().new_subspace().decomposition()
        large_dims = [ X.dimension() for X in factors if X.dimension() != 1 ]
        if len(large_dims) > 0 and names is None:            
            names = 'a'
        return [ element.Newform(self, factors[i], names=(names+str(i)) )
                 for i in range(len(factors)) ]
```

(removing the ValueError statement) as this should correctly use the user-specified name if one is given or default to 'a' if one is not.


---

Comment by was created at 2008-10-22 00:40:39

Lloyd,

Thanks for pointing this out!  I guess we only ever tested with 'a'.  This will be good fodder for bug day on Thursday...


---

Attachment

Sorry, I couldn't wait until Thursday. :) I think William's comment is right -- I probably just never tested this with anything except `a`, since that's the letter I usually use. 

However, raising an error if no variable name is provided is, in fact, the intended behavior -- basically obeying the rule of "explicit is better than implicit."


---

Comment by craigcitro created at 2008-10-22 04:13:57

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2008-10-22 06:02:14

Looks good to me.


---

Comment by ljpk created at 2008-10-22 13:47:24

I personally find the fact that one has to manually assign a variable name really annoying, but if that's the design decision you've taken then fair enough (I can see your reasons; I just disagree).


---

Comment by was created at 2008-10-22 20:55:45

> I personally find the fact that one has to manually assign a variable 
> name really annoying, but if that's the design decision you've taken
> then fair enough (I can see your reasons; I just disagree).

We've systematically made that decision throughout all Sage, so we should stick with that here.

That said, we have also talked about making it so one can specify a uniform default throughout sage, e.g., a function f(n) that takes as input an integer n and outputs a variable name.  You could define it to be anything you want and everywhere in Sage that requires variables would call it -- if specified instead of giving an error, when you forget to give a variable name.


---

Comment by craigcitro created at 2008-10-23 07:07:03

Good point. The request for a system-wide variable default is now trac #4345.


---

Comment by mabshoff created at 2008-10-26 02:49:54

Unfortunately other patches mandate a rebase of this patch:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_4335.patch 
patching file sage/modular/modform/space.py
Hunk #1 FAILED at 1571.
1 out of 1 hunk FAILED -- saving rejects to file sage/modular/modform/space.py.rej
```

Please try either my current merge tree on sage.math or alternatively wait for 3.2.alpha1 out in the next 12 hours

Cheers,

Michael


---

Attachment

I rebased the patch, and it *should* work -- I don't have a current alpha, but I was pretty sure it was my patch from another ticket that caused the merge troubles. Let me know if this one doesn't work.


---

Comment by mabshoff created at 2008-10-26 09:50:52

The rebased patch applies fine - now doctesting.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-26 12:05:24

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 12:05:24

Merged in Sage 3.2.alpha1
