# Issue 3974: [with patch, needs review] renaming of integral_weierstrass_model to integral_short_weierstrass_model

Issue created by migration from https://trac.sagemath.org/ticket/3974

Original creator: wuthrich

Original creation time: 2008-08-28 12:10:36

Assignee: was

I propose a trivial change in the name of integral_weierstrass_model. According to ell_generic.py the terminology is chosen as

> Elliptic curves are always represented by `Weierstass Models' with
> five coefficients $[a_1,a_2,a_3,a_4,a_6]$ in standard notation.  In
> Magma, `Weierstrass Model' means a model with a1=a2=a3=0, which is
> called `Short Weierstrass Model' in Sage; 

so consequently the integral_weierstrass_model which gives back a Short Weierstrass Model should be called integral_short_weierstrass_model.

That is maybe pedantic and a matter of taste, but I believe it would be better.


---

Attachment


---

Comment by mabshoff created at 2008-08-28 12:16:48

Chris,

integral_weierstrass_model is part of the public API, so the rename requires that the old function is still available, but using it should throw a deprecation warning. One example is:

```
def dynkin_diagram(t):
    """
    Returns the Dynkin diagram of type t.  

    Note that this function is deprecated, and that you should use DynkinDiagram 
    instead as this will be disappearing in the near future.

    EXAMPLES:
        sage: dynkin_diagram(["A", 3])
        doctest:1: DeprecationWarning: dynkin_diagram is deprecated, use DynkinDiagram instead!
        Dynkin diagram of type ['A', 3]

    """
    from sage.misc.misc import deprecation
    deprecation("dynkin_diagram is deprecated, use DynkinDiagram instead!")
    return DynkinDiagram(t)
```

from sage/combinat/root_system/dynkin_diagram.py

Cheers,

Michael


---

Comment by wuthrich created at 2008-08-29 12:09:10

I shall change that. 

Nevertheless, in my 3.1.1, I can't use


```
from sage.misc.misc import deprecation
deprecation("dynkin_diagram is deprecated, use DynkinDiagram instead!")
```


instead looking at dynkin_diagram.py suggests the lines


```
import warnings
warnings.warn("integral_weierstrass_model is deprecated, use integral_short_weierstrass_model instead!", DeprecationWarning, stacklevel=2)
}}}      
Is this the proper way of doing ?
When is the 'near future' coming ? 
and do I have to remove it with another patch later ?

(Thanks for the corrections and sorry for my stupid question, but it seems to me that this is the only way for me to learn these things.)

Chris.


---

Comment by wuthrich created at 2008-08-29 12:11:47

Sorry I just found the ticket 3654 which answers my question. 
Chris.


---

Comment by wuthrich created at 2008-08-29 13:04:17

new patch, erplaces the first patch !


---

Attachment

I changed the patch according to Michael's remark. It replaces the previous patch. This patch only works with the patch from ticket 3654.

 Chris.


---

Comment by cremona created at 2008-09-01 20:26:00

I approve of this, though I'm not familiar with how to do the deprecation thing.  Patch applies cleanly to 3.1.2.alpha3,  doctests in sage.schemes.elliptic_curves all ok.


---

Comment by mabshoff created at 2008-09-02 11:47:50

Resolution: fixed


---

Comment by mabshoff created at 2008-09-02 11:47:50

Merged sage_trac3974_new.patch in Sage 3.1.2.alpha4
