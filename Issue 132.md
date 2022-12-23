# Issue 132: maxima -- implement special arithmetic for MaximaFunction class

Issue created by migration from https://trac.sagemath.org/ticket/132

Original creator: was

Original creation time: 2006-10-15 16:16:39

Assignee: was

CC:  mhansen


```
On Sun, 15 Oct 2006 04:20:55 -0700, Tang Hai Tuan Minh <phohongtuyet@gmail.com> wrote:

> Hello,
>
> I am having a little trouble finding out why the following code segment
> doesn't work as expected
>
> f = maxima.function('x', 'sin(x)')
> g = f.integrate('x')
> h = f*g 				// Here sage return different answers on different executions
>
> If I define h as
>
> def h(n):
> 	return f(n)*g(n)
>
> then everything seems to work fine.
>
> I have attached a hopefully small (42.8 KB) png image showing the above
> mentioned code executed inside a sage notebook.

What's happening is that f and g both wrap maxima objects and
when you multipy you get something that wraps a maxima object.
You can get the names of them and see that multiplying just gives
the name of the product.    The solution is for somebody (e.g., me)
to define arithmetic operations on maxima.function objects, i.e.,
adding to the MaximaFunction class in devel/sage/sage/interfaces/maxima.py.
Your problem is a NotImplementedError. 

The reason the answer is different at different times is that the
variables in maxima that SAGE uses are named consecutively. 

sage: f = maxima.function('x','sin(x)')
sage: g = f.integrate('x')
sage: f.name()
'sage0'
sage: g.name()
'sage2'
sage: f*g
sage0*sage2
sage: f
sin(x)
sage: g
-cos(x)
sage: f(10)
sin(10)
sage: f(10.)
-.5440211108893698
sage: (f*g)(10.0)
(sage0*sage2)[10.0]
sage: h = f*g
sage: h(10.0)
(sage0*sage2)[10.0]
```



---

Comment by SimonKing created at 2008-08-14 16:29:35

Implements basic arithmetic for MaximaFunction


---

Attachment

I am surprised that this old ticket was never closed.

I do not claim that i produced high-performance code. However, the following things are now possible:

```
sage: f=maxima.function('x','sin(x)')
sage: g=f.integrate('x')
sage: h=maxima.function('y','cos(y)')
sage: 2*f
2*sin(x)
sage: f*g
-cos(x)*sin(x)
sage: g*h
-cos(x)*cos(y)
sage: (g*h)(3,4)
-cos(3)*cos(4)
sage: (g-f)
-sin(x)-cos(x)
sage: g^f
(-cos(x))^sin(x)
sage: f^g
1/sin(x)^cos(x)
```


There remains the following problem (if it is a problem):

```
sage: f+x
sin(x)+x  # works
sage: 2+f
sin(x)+2  # works
sage: x+f
x + sage0 # doesn't work!
```

This is -- i guess -- due to automatic coercion: `x+f` is the same as 

```
sage: x+x.parent()(f)
x + sage0
```

while `f+x` is the same as

```
sage: f+f.parent()(x)
sin(x)+x
```



---

Comment by SimonKing created at 2008-08-15 07:48:06

1. I forgot to include doc tests. This is done with the follow-up patch (to be applied after the first).

 2. Also, there was a problem with the order of arguments:

```
sage: a=maxima.function('x,y','cos(y)+sin(x)')
sage: b=maxima.function('x,y','cos(y)-cos(x)')
sage: (a+b)(2,3)
sin(3)-cos(3)+2*cos(2)
```

 Hence, in `(a+b)`, `x` is the second (not the first) argument.

 The methods from the second patch order the arguments lexicographically. I think this is the most natural solution:

```
sage: a=maxima.function('x,y','cos(y)+sin(x)')
sage: b=maxima.function('x,y','cos(y)-cos(x)')
sage: (a+b)(2,3)
2*cos(3)+sin(2)-cos(2)
```


 3. A method `__rpow__` is now also in the second patch.

```
sage: f=maxima.function('x','sin(x)')
sage: g=maxima('-cos(x)') # not a function
sage: g^f
(-cos(x))^sin(x)
sage: _(2)
(-cos(2))^sin(2)
```



---

Attachment

Adding doctests, taking care of argument order, adding __rpow__, correcting misprint


---

Comment by mabshoff created at 2008-08-27 07:57:57

Mike,

can you review this?

Cheers,

Michael


---

Comment by mhansen created at 2008-08-27 22:16:46

Simon's original patches subvert the coercion system.  I posted a new patch instead which uses the coercion system and concentrates all of the actual work into a few places.


---

Attachment

Mike's patch looks good. Positive review. If Mike agrees, one can apply my docstring patch too. However, this is optional and to some extend a question of taste/preference.


---

Comment by malb created at 2008-08-28 10:40:33

optional


---

Attachment

+1 to Martin's patch.


---

Comment by mabshoff created at 2008-08-28 22:18:16

Resolution: fixed


---

Comment by mabshoff created at 2008-08-28 22:18:16

Merged trac_132.patch and trac_132_docstrings.patch in Sage 3.1.2.alpha2
