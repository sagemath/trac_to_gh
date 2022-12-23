# Issue 3350: plot_vector_field error

Issue created by migration from https://trac.sagemath.org/ticket/3350

Original creator: mhampton

Original creation time: 2008-06-02 12:49:28

Assignee: mhampton

Keywords: plot_vector_field, plot

Sometimes functions in plot_vector_field are evaluated on the wrong argument somehow:

Subject: Re: plot directional field differential equations
From: Georg Muntingh <georg.munti...`@`gmail.com>
To: sage-support <sage-support`@`googlegroups.com>

You can use the plot_vector_field command:
# Declare your variables:
var('x t')
# Define you function, for instance:
def f(t,x):
    return t*x
There seems to be something awry, however, compare
plot_vector_field((lambda t, x: 1, x), (-1, 1), (-2, 2))
plot_vector_field((lambda t, x: 1, x + 0.001*t), (-1, 1), (-2, 2))
(the second one is what one expects for the differential equation x' =
x)

Why does the vector field look so different when it depends only on one coordinate?


---

Comment by mhampton created at 2008-10-16 15:17:24

Someone else should take a look at this, I've given it some thought and can't figure it out.

The syntax on the above examples is wrong, I think, but does not account for the problem.  For example, even:

```
plot_vector_field((lambda x,t: 1, lambda x,t: x), (-1, 1), (-2, 2))
```

which seems safer, still gives the wrong result, as does

```
var('x,t')
plot_vector_field((1, x), (-1, 1), (-2, 2))
```



---

Comment by mhampton created at 2008-10-16 15:17:24

Changing assignee from mhampton to somebody.


---

Comment by jason created at 2009-01-22 19:56:59

In your second example, it is impossible to tell which variable is which (i.e., which is the horizontal axis, which is the vertical).  Specify it by doing:


```
var('x,t')
plot_vector_field((1, x), (x,-1, 1), (t,-2, 2))
```


What is wrong about the result?  I get the correct result on my computer.  Of course, to make the slope actually look like a slope of -1, you need to change the aspect_ratio:


```
var('x,t')
plot_vector_field((1, x), (-1, 1), (-2, 2)).show(aspect_ratio=1)
```



---

Comment by jason created at 2009-01-22 20:06:12

You have the same problem of specifying variables in the example in the ticket description.



However, currently the convention for choosing the variables is not very good, and the functions ought to be fast_float functions anyway.  I'll do those two things for this ticket.


---

Comment by jason created at 2009-01-22 22:40:26

I take that back; everything is fine and dandy for this function as far as variable selection and fast_float goes.  At least, it's consistent with all the other plotting functions.

Please, please, please, just like in all of the doc examples for plot_vector_field, specify the variables in the ranges, like (t, -3, 3).


---

Comment by jason created at 2009-01-22 22:43:18

Resolution: invalid
