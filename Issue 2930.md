# Issue 2930: CDF is slow, fix it.

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-04-15 06:13:29

Assignee: gfurnish

CC:  robertwb

Add a CDF pool, optimize CD creation.  


---

Attachment


---

Comment by gfurnish created at 2008-04-15 06:14:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-15 07:19:59

Not even close:

```
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element_generic.py # 4 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 4 doctests failed
        sage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx # 7 doctests failed
        sage -t -long devel/sage/sage/rings/real_double.pyx # 4 doctests failed
        sage -t -long devel/sage/sage/rings/power_series_ring_element.pyx # 9 doctests failed
        sage -t -long devel/sage/sage/rings/number_field/number_field.py # 3 doctests failed
        sage -t -long devel/sage/sage/rings/complex_double.pyx # 21 doctests failed
        sage -t -long devel/sage/sage/modules/free_module.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/modform/numerical.py # 12 doctests failed
        sage -t -long devel/sage/sage/plot/plot.py # 8 doctests failed
        sage -t -long devel/sage/sage/misc/functional.py # 2 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix_real_double_dense.pyx # 4 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix_complex_double_dense.pyx # 26 doctests failed
        sage -t -long devel/sage/sage/matrix/constructor.py # 1 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix2.pyx # 7 doctests failed
        sage -t -long devel/sage/sage/interfaces/phc.py # 2 doctests failed
        sage -t -long devel/sage/sage/functions/orthogonal_polys.py # 1 doctests failed
        sage -t -long devel/sage/sage/functions/functions.py # 2 doctests failed
        sage -t -long devel/doc/const/const.tex # 1 doctests failed
        sage -t -long devel/sage/sage/calculus/calculus.py # 9 doctests failed
```


Back to the drawing board ;)

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-20 04:48:20

Changing keywords from "" to "editor_gfurnish".


---

Comment by mabshoff created at 2008-11-30 08:16:42

The idea of generic pools is a good one, but I am pretty sure this implementation has rotted. 

Robert: Any take here about doing something generic for pools?

Cheers,

Michael


---

Comment by robertwb created at 2008-12-02 12:54:07

Thanks for pinging me. Yes, I've put some thought into making generic pools, just haven't had the time to actually implement anything. 

The ticket is still valid, but I don't think this patch (if it even passed test) is the way to go. 

- Robert


---

Comment by mabshoff created at 2008-12-02 13:01:00

Replying to [comment:6 robertwb]:

Hi,

> Thanks for pinging me. Yes, I've put some thought into making generic pools, just haven't had the time to actually implement anything. 

:)
 
> The ticket is still valid, but I don't think this patch (if it even passed test) is the way to go. 

I have created a wish list ticket at #4673 so we have a clean start and something more generic, i.e. the ticket is about creating the infrastructure. Once that is there we can add tickets for the classes that have not been converted. 

As a consequence I am invalidating this ticket.

> - Robert

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-02 13:01:00

Resolution: invalid


---

Comment by robertwb created at 2008-12-02 19:48:05

Sounds good to me.
