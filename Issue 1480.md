# Issue 1480: [with patch] implement P.show() for mathematica elements -- nice mathematica graphics in the sage notebook!

Issue created by migration from https://trac.sagemath.org/ticket/1480

Original creator: was

Original creation time: 2007-12-12 18:35:05

Assignee: was

As the summary says.  Inspired by this email

```


On Dec 12, 2007 10:07 AM, carlosap <carlosap78@gmail.com> wrote:
> 
> I typed mathematica.NIntegrate[x^2,{x,1,0}]
> 
> And I get
> 
> Syntax Error:
>     mathematica.NIntegrate[x^2,{x,1,0}]
> 
> I know that I can switch to mathematica in the browser and works ok,
> but if I want some result from mathematica and then use Sage, is that
> possible?

Try this:

sage: z = mathematica('NIntegrate[x^2,{x,1,0}]'); z
-0.3333333333333338
sage: z + 3.5
3.166666666666666
sage: sin(float(z))
-0.32719438181048527
 
> I didnt find any docs on how to use mathematica in sage. 


They are here:
   http://sage.math.washington.edu/sage/doc/html/ref/module-sage.interfaces.mathematica.html

> I find really
> cool to use mathematica with the browser so I dont have to buy
> webmathematica.  Is it possible to plot something in mathematica with
> sage browser ?

I've never done this before or seen anybody do it.  I just figured out how.
As an example, paste the following two lines into an input cell and press shift-enter:

mathematica('SetDirectory["%s"]'%os.path.abspath("."))
_ = mathematica('Export["a.png", Plot[Sin[x],{x,-2Pi,4Pi}], ImageSize->600]')

The first complicated line above -- i.e., to set the directory, will not be needed 
in sage >= 2.9 -- I just made it automatic for future versions of sage. 

```



---

Attachment

Timothy Clemans points out that to get graphics to work remotely do:


```
Xvfb 19
export DISPLAY=localhost:19
```

then start the sage notebook server. 

This is discussed at 

 http://witm.sourceforge.net/installation.php

This should definitely somehow be in sage before this ticket is closed!

E.g., on failure a message could be printed out telling the user to do the
above... and something like this could be in the docstring for the new show command.


---

Attachment


---

Comment by mabshoff created at 2007-12-15 14:07:27

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 14:07:27

Merged in 2.9.rc0.
