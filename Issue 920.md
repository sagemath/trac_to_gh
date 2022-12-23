# Issue 920: integrate doesn't handle divergent case correctly

Issue created by migration from https://trac.sagemath.org/ticket/920

Original creator: jason

Original creation time: 2007-10-18 17:18:07

Assignee: was

The following integral should be divergent, but sage (and maxima?) gives an answer.

sage: integrate(1/x^3,x,-1,3)
4/9
sage: version()
'SAGE Version 2.8.7, Release Date: 2007-10-15'


---

Comment by jason created at 2007-10-18 17:50:53

That's supposed to say:


```
sage: integrate(1/x^3,x,-1,3) 
4/9 
sage: version() 
'SAGE Version 2.8.7, Release Date: 2007-10-15' 
```



---

Comment by mhansen created at 2007-10-18 21:08:08

This is due to Maxima:

```
(%i3) integrate(1/x^3,x,-1,3);
Principal Value                                       4
(%o3)                                  -
                                       9

```


I'm not quite sure what to do about it at the moment.


---

Comment by mhansen created at 2007-10-24 00:44:24

I've attached a patch which makes "Principal Value" output in Maxima raise an error so that sage does not return the wrong answer.  Here is the behavior after the patch.


```
sage: integrate(1/x^3,x,-1,3)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/opt/sage/devel/sage-calc/sage/calculus/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    175         return f.integral(*args, **kwds)
    176     except ValueError, err:
--> 177         raise err
    178     except AttributeError:
    179         pass

<type 'exceptions.ValueError'>: Integral is divergent.
```


This patch should be applied after the patch for #921 is applied.


---

Comment by mhansen created at 2007-10-24 00:44:24

Changing status from new to assigned.


---

Comment by mhansen created at 2007-10-24 00:44:24

Changing assignee from was to mhansen.


---

Comment by was created at 2007-10-24 02:17:42

Looks, good though:

```
19:15 < wstein> re: 920.  I've never seen a line like this before:
19:15 < wstein> if "divergent" in s or 'Principal Value': 
19:16 < wstein> It actually works as claimed.
19:16 < wstein> It's surprising to me that it is equivalent to: if "divergent" in (s + 'Principal Value')
```



---

Attachment

applied to 2.8.9.alpha1


---

Comment by malb created at 2007-10-24 19:24:49

Resolution: fixed
