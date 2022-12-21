# Issue 6290: Allow latex_name=LaTeX keyword while defining symbolic function

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-06-14 23:29:44

CC:  was

Keywords: latex_name, symbolic function

In new symbolics, underlying "sage.symbolic.SFunction" class allows
one to pass the keyword "latex_name=LaTeX". It would be really good if we expose this feature at the user interface level. Currently,
Sage (4.0.1) raises error if one tries to do so.


Example uses:


```
riemann(x) = function('riemann', x, latex_name="\\mathcal{R}")
latex( riemann(x) )
\mathcal{R}
```



---

Comment by was created at 2009-06-15 17:44:54

Nice.  Could you add more to the docstring for function (at least the one that I get by default when I do function? from the sage prompt) that explains what happens to all kwds arguments?  You do give a nice example (with riemann), but a sentence or two explaining what is going on would be very nice.


---

Attachment


---

Comment by gmhossain created at 2009-06-15 20:12:19

Replying to [comment:3 was]:
> Nice.  Could you add more to the docstring for function (at least the one that I get by default when I do function? from the sage prompt) that explains what happens to all kwds arguments?  

Thanks for your comments! As you suggested, I have updated the patch with expanded docstrings.


---

Comment by ncalexan created at 2009-06-15 20:36:20

Looks good to me.


---

Comment by rlm created at 2009-06-24 09:44:35

Merged in sage-4.1.alpha0.


---

Comment by rlm created at 2009-06-24 09:44:35

Resolution: fixed


---

Comment by schymans created at 2009-06-25 10:15:37

Would something similar be possible whenever a variable is defined?
E.g. if I want to use multiple subscripts, I would like to define
var('A_gs', latex_name="A_{gs}"). 

That would make it really flexible.


---

Comment by gmhossain created at 2009-06-25 10:44:11

Replying to [comment:8 schymans]:
> Would something similar be possible whenever a variable is defined?
> E.g. if I want to use multiple subscripts, I would like to define
> var('A_gs', latex_name="A_{gs}"). 

Hmmm, thats a great suggestion. Could you please post this to sage-devel?
