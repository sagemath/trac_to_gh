# Issue 1912: Displaying a list of graphic objects prints what appears to be an empty list

Issue created by migration from https://trac.sagemath.org/ticket/1912

Original creator: jason

Original creation time: 2008-01-24 16:08:14

Assignee: was

CC:  kcrisman


```

> As a final comment, I'll note that the following behavior with objects
> which automatically display is interesting:
> 
> sage: C=circle((0,0),1);P=plot(sin,0,1)
> sage: [C,P]
> [, ]
> 
> and then a display of circle above a plot of sin (in the notebook) or
> two separate pictures (in the command line).  I have no idea what, if
> any, connection should be made with this work, though.

I think it is just printing out the list for you to see and the "print" function for a graphics object displays the object, so you see each object "printed" out.

It would be nice if the text display indicated this, instead of "[, ]".  Maybe something like "[<Graphic object>, <Graphic object>]", since the objects actually are there.  It misleadingly looks like you have an empty list.
```




---

Comment by was created at 2008-01-24 16:25:20

> It would be nice if the text display indicated this, instead of "[, ]".  Maybe 
> something like "[<Graphic object>, <Graphic object>]", since the objects 
> actually are there.  It misleadingly looks like you have an empty list.

I agree.  However, I have *absolutely no clue* how or even if this is possible to implement in Python.  I almost think it isn't.   More precisely, we could easily
make it so we have
 
 sage: plot(sin, 0,1)
 <Graphic object>
 [an actual image]

but that would be really ugly. 

William


---

Comment by was created at 2008-01-24 16:27:13

Actually, I vaguely recall there is a "displayhook" in Python that is called
when one types

```
 sage: <arbitrary object>
```

Maybe we could overload that so if <arbitrary object> is a list or tuple then
instead of calling _repr_ on each graphics object, we call __str__.


William

It's weird.  Every time I think something is impossible I immediately seem to think of a solution...


---

Comment by cwitty created at 2008-01-24 18:38:39

Another idea: make it return <Graphic object> whenever it creates an object; but in IPython/the notebook, check to see if it's about to print "<Graphic object>", and if so print nothing instead.


---

Comment by jason created at 2008-01-24 18:48:58

> It's weird. Every time I think something is impossible I immediately seem to think of a solution...

We ought to put you in charge of more hard problems!  So...do you think it's impossible to prove the Riemann hypothesis? :)


---

Comment by jason created at 2008-01-24 18:55:10

I think either of these solutions works okay, but I prefer the first since it clearly tells the user that they just constructed a list of graphic objects.


```
sage: [graphic1, graphic2]
# Displays each graphic, as well as:
[<graphic object>, <graphic object>]
```



```
sage: [graphic1, graphic2]
# Displays each graphic, but doesn't print anything
```


Just for comparison, Mathematica 6 actually prints out the graphics, surrounded by the delimiters (so the graphics are really inside the list and appear that way) when using the notebook and prints out just a string representation {-Graphics-} when used from the command line.


---

Comment by was created at 2008-01-25 06:01:11

This idea of Jason Grout is the sort of thing we can do to solve this sort of problem:

```
def pretty_print (object):
    if object is None:
        return
    if isinstance(object, (sage.plot.plot.Graphics, sage.plot.plot3d.base.Graphics3d)):
        print repr(object)
        return
    import __builtin__
    __builtin__._=object
    try:
        print html("$$"+latex(object)+"$$")
    except:
        import sys
        sys.__displayhook__(object)

def notebook_pretty(enable=True):
    import sys
    if enable:
        sys.displayhook = pretty_print
    else:
        sys.displayhook = sys.__displayhook__

# To enable the pretty-printing
notebook_pretty(True)
```



---

Comment by jason created at 2008-01-25 08:32:16

See #1922 for the above pretty_print functions.


---

Comment by mmezzarobba created at 2014-02-15 13:29:17

Appears to be fixed, most probably as part of #14469. And there is already a doctest covering this behaviour.


---

Comment by mmezzarobba created at 2014-02-15 13:29:25

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-03-05 09:40:50

Ok, I think this can be closed.


---

Comment by chapoton created at 2014-03-05 09:40:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-05 17:00:35

Resolution: fixed
