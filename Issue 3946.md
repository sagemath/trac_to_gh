# Issue 3946: Tidier BinaryQF reductions

Issue created by migration from Trac.

Original creator: choldsworth

Original creation time: 2008-08-25 02:35:02

Assignee: was

CC:  cremona

Cremona writes:
>However, there are some things I really do not like about this implementation:

>   1. self.reduce() computes (if necessary) caches and returns the reduced form equivalent to        
>self. I would expect it to change self into the reduced form, and have a different function   
>self.reduced_form() to do what this function does. 

>  2. The function is_reduced() actually reduces self and tests if the result is the same as 
>self. This is potentially very expensive! To test is_reduced() you should just test that the 
>usual inequalities are satisfied. 

I have attached a patch which I believe fixes these issues. I have also altered the reduction methods to throw more enlightening exceptions when given negative definite forms and indefinite forms.

It would be nice to implement the the handling of indefinite and negative definite forms at some point in the future, however I don't think Pari can deal with negative definite forms currently.


---

Attachment


---

Comment by cremona created at 2008-08-25 10:51:10

I am happy that this patch deals with the criticisms I had regarding #3857 (which did in fact have nothing to do with the bug which #3857 fixed, but rather were criticisms of some of the design of this class).

The patch applies fine after the patches for #3857 (and probably independently of those too), and all doctests in sage/quadratic_forms pass.


---

Comment by mabshoff created at 2008-08-25 20:17:28

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 20:17:28

Merged in Sage 3.1.2.alpha1
