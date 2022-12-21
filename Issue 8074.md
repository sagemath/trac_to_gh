# Issue 8074: corner cases in RealField and real numbers

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-01-26 08:37:57

Assignee: jkantor

CC:  robertwb was jkantor zimmerma leif

What should these return?


```

sage: RR('inf').is_real()
True
sage: RR('nan').is_real()
True
sage: RR('inf').is_unit()
True
```



---

Comment by jason created at 2010-01-26 08:39:15

Changing status from new to needs_info.


---

Comment by jason created at 2010-01-26 08:40:15

And this:


```
sage: RR('nan').__nonzero__()
False

```



---

Comment by jason created at 2010-01-26 08:47:57

And another corner case:


```
sage: RR('nan')==RR('nan')
True
```



---

Comment by jason created at 2010-01-26 09:00:26

Another one:


```
sage: RR('nan').__pow(0.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.RuntimeError'> ignored
^CERROR: Internal Python error in the inspect module.
Below is the traceback from this internal error.

Traceback (most recent call last):
  File "/home/grout/sage/local/lib/python2.6/site-packages/IPython/ultraTB.py", line 614, in text
    records = _fixed_getinnerframes(etb, context,self.tb_offset)
  File "/home/grout/sage/local/lib/python2.6/site-packages/IPython/ultraTB.py", line 230, in _fixed_getinnerframes
    records  = fix_frame_records_filenames(inspect.getinnerframes(etb, context))
  File "/home/grout/sage/local/lib/python/inspect.py", line 942, in getinnerframes
    framelist.append((tb.tb_frame,) + getframeinfo(tb, context))
  File "/home/grout/sage/local/lib/python/inspect.py", line 902, in getframeinfo
    filename = getsourcefile(frame) or getfile(frame)
  File "/home/grout/sage/local/lib/python/inspect.py", line 451, in getsourcefile
    if hasattr(getmodule(object, filename), '__loader__'):
  File "/home/grout/sage/local/lib/python/inspect.py", line 485, in getmodule
    if ismodule(module) and hasattr(module, '__file__'):
  File "/home/grout/sage/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.py", line 9, in my_sigint
    raise KeyboardInterrupt
KeyboardInterrupt

Unfortunately, your original traceback can not be constructed.
```



---

Comment by jason created at 2010-01-26 09:21:02


```
sage: RR('-inf').__pow(0.5)
+infinity
sage: sqrt(RR('-inf'))     
+infinity*I
```



---

Comment by jason created at 2010-02-09 17:18:50

Paul,

You are one of the best experts around on floating point issues.  If you have time, could you comment on the corner cases listed in the description---do you agree with the current output of Sage, or should it be changed?

Thanks, Jason

(I put all of the corner cases from #7682 and from the comments on this ticket up in the description.)


---

Comment by zimmerma created at 2010-02-09 20:51:31

> You are one of the best experts around on floating point issues...

thanks, you are putting pressure on me! I'll try to do my best...

One first problem is that `is_real` is not documented, thus I don't know what the intended
semantics is or was. In MPFR there is no such function:

```
 -- Function: int mpfr_nan_p (mpfr_t OP)
 -- Function: int mpfr_inf_p (mpfr_t OP)
 -- Function: int mpfr_number_p (mpfr_t OP)
 -- Function: int mpfr_zero_p (mpfr_t OP)
     Return non-zero if OP is respectively NaN, an infinity, an ordinary
     number (i.e. neither NaN nor an infinity) or zero. Return zero
     otherwise.
```


About `RR('inf').is_unit()`, if one considers that x is a unit if 1/x is in RR, then since
1/inf = 0 is in RR, it should return true.

`RR('nan')==RR('nan')` should return False according to IEEE 754.

`RR('nan').__pow(0.5)` should return NaN (here NaN means "can be any real number").

`RR('-inf').__pow(0.5)` is ok according to the MPFR rules (here I assume that we try to stay
in RR):

```
        * `pow(-Inf, Y)' returns plus infinity for Y positive and not
          an odd integer.
```


For `sqrt(RR('-inf'))` it depends on the semantics of the sqrt function. Apparently it
extends to the complex plane (try `sqrt(RR(-1))`) thus the answer seems ok to me.

`RR('nan').__nonzero__()` is more difficult, since "NaN" means "can be any real", thus in
particular it can be zero, thus the answer should be "maybe". If no ternary answer is possible,
false seems the best one.


---

Comment by jdemeyer created at 2010-09-28 20:52:55

Replying to [comment:5 jason]:

```
sage: RR('nan').__pow(0.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.RuntimeError'> ignored
...
```


Regardless of whatever the output of `RR('nan').__pow(0.5)` should be, it is a bug by itself that we don't get a decent exception here...
