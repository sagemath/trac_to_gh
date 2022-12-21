# Issue 7512: plot3d variable ranges should respect the named variable, if there is one

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-11-22 03:49:46

Assignee: was

CC:  wcauchois robertwb mjo

This is a somewhat subtle issue if the function is a pure python function (you'd need to analyze the argument names), but maybe a convention is that if variable names are specified, they must match up to argument names in the function, and then they are slotted into the function using a dictionary, so that no matter where in the variable range list the range for x appears, it always is sent to the function as f(x=value).

See http://sagenb.org/home/jason3/302/

I think that each of these should return the same plot:


```
sage: var('x,y')
sage: def f(x,y):
...      return x*sin(y)
...
sage: plot3d(f, (x,0,3),(y,-6,6),viewer='tachyon')
sage: plot3d(f, (y,-6,6),(x,0,3),viewer='tachyon')
sage: g(x,y)= x*sin(y)
sage: plot3d(g, (x,0,3),(y,-6,6),viewer='tachyon')
sage: plot3d(g, (y,-6,6),(x,0,3),viewer='tachyon')
```



---

Comment by jason created at 2010-01-20 11:12:18

Robert and I decided that the fourth plot should be the same as the second, but it is not.  The error is in the fourth plot.  The problem seems to be that in the fourth plot, the g(x,y) is really called as g(x=x_val, y=y_val), but should just be called as g(y_val, x_val) (i.e., not with named variables, but with just positional parameters).


---

Comment by jason created at 2010-01-20 13:21:43

Changing status from new to needs_review.


---

Attachment


---

Comment by jason created at 2010-01-20 13:22:17

We decided that this was just a symptom of a much deeper issue in fast_callable.  The patch fixes the issue in fast_callable.


---

Comment by rossk created at 2010-01-31 05:34:47

Applied patch trac-7512-fast_callable-callable_expressions.patch to sage-4.3.2-alpha0 and tried the exact commands below (in that order). I looked for all 4 plots to be the same (as per the ticket description) but only Plot3d No.1 was the same as Plot3d No.3 - AND - Plot3d No.2 was the same as Plot3d No.4. I tried to see if swapping the ranges of x and y, would give me a clue as to what might be going on (refer plot3d No.5 below) but that caused an exception "ZeroDivisionError: float division" (at line 954: count = (end-start)/step IN sage/misc/misc.pyc)


```
sage: var('x,y')                                                                                                                                         
(x, y)
sage: def f(x,y):
....:     return x*sin(y)
....: 
sage: g(x,y)= x*sin(y)
sage: 
sage: plot3d(f, (x,0,3),(y,-6,6),viewer='tachyon')

sage: plot3d(f, (y,-6,6),(x,0,3),viewer='tachyon')

sage: plot3d(g, (x,0,3),(y,-6,6),viewer='tachyon')

sage: plot3d(g, (y,-6,6),(x,0,3),viewer='tachyon')

sage: plot3d(f, (x,-6,-6),(y,0,3),viewer='tachyon')  
```



---

Comment by jason created at 2010-02-27 10:24:42

rossk: we decided that the four plots shouldn't be equal after all; the first should be the same as the third, and the second should be the same as the fourth.

ping to robertwb: if you have time, it'd be great if you could review this too.


---

Comment by rossk created at 2010-02-28 09:47:00

Played with some examples and can see that the examples below act like lambda functions now (regardless of variable name or variable order or function format - all plots came out the same as expected). Hope that helps speed up the review (someone will still have to do the code review)


```
var('x y v w')

def f(x,y):
    return x*sin(y)

g(x,y)=x*sin(y)

plot3d(f, (x,0,3), (y,-6,6), viewer='tachyon')
plot3d(f, (y,0,3), (x,-6,6), viewer='tachyon')
plot3d(f, (v,0,3), (w,-6,6), viewer='tachyon')

plot3d(g, (x,0,3), (y,-6,6), viewer='tachyon')
plot3d(g, (y,0,3), (x,-6,6), viewer='tachyon')
plot3d(g, (v,0,3), (w,-6,6), viewer='tachyon')
```



---

Comment by kcrisman created at 2010-05-26 18:42:32

I have two dumb questions.  Not putting "needs work" in case someone else decides on the review.

1. Aren't CallableSymbolicExpressions already Expressions?  How does this get into the else? 

```
    if isinstance(x, Expression):
        et = x
        vars = et._etb._vars
    else:
        from sage.symbolic.callable import is_CallableSymbolicExpression
        if is_CallableSymbolicExpression(x):
            vars=x.args()
```


2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).


---

Comment by jason created at 2010-05-26 18:54:19

Replying to [comment:10 kcrisman]:



> 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).




We do allow other variable names in callable expressions:


```
sage: f(x,y)=a*x+y
sage: f(1,2)
a + 2
sage: f(a=2)
2*x + y
```



I'm also looking at your other points...


---

Comment by kcrisman created at 2010-05-26 18:57:27

> 
> > 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).
> 
> 
> We do allow other variable names in callable expressions:
> 
> {{{
> sage: f(x,y)=a*x+y
> sage: f(1,2)
> a + 2
> sage: f(a=2)
> 2*x + y
> }}}
> 

I meant that we aren't allowed to use another variable name to substitute for x and y, but rossk's examples indicate you can do this somehow (?) now since the variables are ignored.


---

Comment by jason created at 2010-05-26 19:07:54

Replying to [comment:10 kcrisman]:


> 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).

I think in retrospect, I agree that this patch does not have the right design decision.  Instead of throwing away the var values, we should make the default be the x.args() (so that someone doesn't need to specify the vars keyword if passing in a CallableSymbolicExpression).


---

Comment by jason created at 2010-05-26 19:09:12

Replying to [comment:10 kcrisman]:
> I have two dumb questions.  Not putting "needs work" in case someone else decides on the review.
> 
> 1. Aren't CallableSymbolicExpressions already Expressions?  How does this get into the else? 

The Expression in the code is different than Symbolic Expressions (instead, they are related to Expression trees, a fast callable construct.


---

Comment by jason created at 2010-05-26 19:11:05

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-05-26 19:35:33

I'm doing quite a bit of work on fast_callable over on #5572.  I think I'll try to take care of this issue (with the different design decision I just mentioned) over there.


---

Comment by jason created at 2010-09-07 02:43:25

Changing to needs info, pending the decisions and work over on #5572 (i.e., the info needed is: is this ticket obsolete and invalid?)


---

Comment by jason created at 2010-09-07 02:43:25

Changing status from needs_work to needs_info.


---

Comment by mkoeppe created at 2021-12-18 19:53:12

Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.
