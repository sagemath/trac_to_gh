# Issue 2696: octave -- implement handling of multiple return values of functions

Issue created by migration from https://trac.sagemath.org/ticket/2696

Original creator: was

Original creation time: 2008-03-28 07:05:59

Assignee: was


```

On Mon, Mar 24, 2008 at 8:26 AM, Michael <michael.delamaza@gmail.com> wrote:
> 
>  What is the recommended way to handle Octave functions with multiple
>  return values in Sage?

I wrote the Sage/Octave interface, but I didn't think of everything.   In particular,
I completely forgot about multiple return values.    The recommend way to handle
them would be to implement something similar to what the Magma interface
currently does, then use that.  :-)

>  Like Magma, Octave functions can return multiple values.  Working with
>  such Magma functions is documented in the Sage documentation (http://
>  modular.math.washington.edu/sage/doc/html/ref/node125.html), but I
>  cannot find similar documentation for Octave.
>  
>  Here is how it works in Octave -- foo is a function that returns two
>  values:
>  
>  octave:4> function [a b] = foo() a=1; b=2; endfunction
>  octave:5> foo()
>  ans = 1
>  octave:6> [c,d] = foo()
>  c = 1
>  d = 2
>  
>  
>  This code transliterated into Sage is shown below.   What is the
>  correct way to do this?
>  
>  ----------------------------------------------------------------------
>  | SAGE Version 2.10.3, Release Date: 2008-03-11                      |
>  | Type notebook() for the GUI, and license() for information.        |
>  ----------------------------------------------------------------------
>  
>  sage: octave.eval("function [a b] = foo() a=1; b=2; endfunction")
>  ''
>  sage: octave.foo()
>   1
>  sage: [c, d] = octave.foo()
>  ---------------------------------------------------------------------------
>  <type 'exceptions.NotImplementedError'>   Traceback (most recent call
>  last)
>  
>  /home/login/<ipython console> in <module>()
>  
>  /usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/
>  expect.py in __iter__(self)
>    1013
>    1014     def __iter__(self):
>  -> 1015         for i in range(1, len(self)+1):
>    1016             yield self[i]
>    1017
>  
>  /usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/
>  expect.py in __len__(self)
>    1017
>    1018     def __len__(self):
>  -> 1019         raise NotImplementedError
>    1020
>    1021     def __reduce__(self):
>  
>  <type 'exceptions.NotImplementedError'>:
>  sage:
>  
```



---

Comment by AlexGhitza created at 2009-01-23 02:42:16

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from interfaces to interfaces: optional.


---

Comment by chapoton created at 2015-09-16 13:45:09

Changing keywords from "" to "octave".


---

Comment by kcrisman created at 2015-10-29 19:30:37

See also #19502 for a possibly related bug (or possibly not).
