# Issue 1554: calculus -- issues with calling symbolic expressions

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-17 16:41:42

Assignee: was


```


On Dec 17, 2007 5:32 AM, Joel B. Mohler <joel`@`kiwistrawberry.us> wrote:
> 
> Hi,
> 
> I don't think that the trac 1460 is really fixed.  The bug just got moved
> around.
> http://trac.sagemath.org/sage_trac/ticket/1460
> 
> # sage 2.9
> sage: t=var('t')
> sage: f=t*sin(0)
> sage: float(f(1))
> # goes boom for a different reason than in 2.8.15

This is *not* a bug.  The is by design.  Since f has no variables it is no longer
implicitly callable:

sage: f.variables()
()
sage: f(1)
.ValueError: the number of arguments must be less than or equal to 0

You will have to instead write:
sage: f(t) = t*sin(0)
sage: f(1)
0

or use 

sage: f=t*sin(0)
sage: f(t=0)
0

This change was introduced because people often do the following
by accident:

sage: a = (sqrt(2) + 17)(x+2)
sage: a
sqrt(2) + 17

Of course, that the above doesn't give an error even in 2.9 is a
bug!   At least in most cases it works:

sage: (SR(2) + 3)(x)
<type 'exceptions.ValueError'>: the number of arguments must be less than or equal to 0

Also, this is a bug:

sage: a = (I*17+3*5)(x+2)
AttributeError: 'I_class' object has no attribute 'number_of_arguments'


I want to emphasize that allowing

sage: a = (sqrt(2) + 17)(x+2)

and having it return sqrt(2) + 17 is *very* confusing to
a lot of people.  I witnessed this time after time after time
when teaching a high school workshop using Sage this
summer -- it was really striking how often this happened.


> 
> It seems the originally submitted patch by was has a doc-test testing this very
> thing, but the actual code in my newly upgraded 2.9 just has a bunch of
> doc-strings that look like:
> """
> EXAMPLES:
> """
> with no examples!
> 
> I'm not sure what went on beyond that.
> 
> --
> Joel
> 
> --~--~---------~--~----~------------~-------~--~----~
> To post to this group, send email to sage-devel`@`googlegroups.com
> To unsubscribe from this group, send email to sage-devel-unsubscribe`@`googlegroups.com
> For more options, visit this group at http://groups.google.com/group/sage-devel
> URLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/
> -~----------~----~----~----~------~----~------~--~---
> 
> 



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org

```



---

Comment by mhansen created at 2008-01-27 02:07:45

Changing status from new to assigned.


---

Comment by mhansen created at 2008-01-27 02:07:45

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2008-01-27 20:13:06

This was fixed as a (intended) side-effect of another patch.  The patch posted here adds doctests to cover the cases mentioned in this patch.


---

Comment by was created at 2008-01-27 20:28:48

I give this a positive review.


---

Comment by mabshoff created at 2008-01-29 12:36:13

Resolution: fixed


---

Comment by mabshoff created at 2008-01-29 12:36:13

Merged in Sage 2.10.1.rc3
