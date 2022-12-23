# Issue 1997: magma interface -- interrupting restarts magma way way too aggressively

Issue created by migration from https://trac.sagemath.org/ticket/1997

Original creator: was

Original creation time: 2008-01-31 05:00:02

Assignee: was

From the command line

```
teragon:~ was$ magma
Magma V2.13-10    Wed Jan 30 2008 23:54:17 on teragon  [Seed = 166664802]
Type ? for help.  Type <Ctrl>-D to quit.
> j:= 2; for i in [1..10^7] do j +:= i; end for;

[Interrupted]
> 2+2;
4
> 
```


However, exactly the same always results in a complete restart of Magma:

```
sage: magma.eval('j:= 2; for i in [1..10^7] do j +:= i; end for;')
^CInterrupting Magma...
---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in eval(self, x, strip)
    276         if len(x) == 0 or x[len(x) - 1] != ';':
    277             x += ';'
--> 278         ans = Expect.eval(self, x).replace('\\\n','')
    279         if 'Runtime error' in ans or 'User error' in ans:
    280             raise RuntimeError, "Error evaluation Magma code.\nIN:%s\nOUT:%s"%(x, ans)

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)
    705         try:
    706             with gc_disabled():
--> 707                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    708         except KeyboardInterrupt:
    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    646                 out = '\n\r'
    647         except KeyboardInterrupt:
--> 648             self._keyboard_interrupt()
    649             raise KeyboardInterrupt, "Ctrl-c pressed while running %s"%self
    650         i = out.find("\n")

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _keyboard_interrupt(self)
    660                 raise pexcept.ExceptionPexpect( "THIS IS A BUG -- PLEASE REPORT. This should never happen.\n" + msg)
    661             self._start()
--> 662             raise KeyboardInterrupt, "Restarting %s (WARNING: all variables defined in previous session are now invalid)"%self
    663         else:
    664             self._expect.sendline(chr(3))  # send ctrl-c

<type 'exceptions.KeyboardInterrupt'>: Restarting Magma (WARNING: all variables defined in previous session are now invalid)
sage: magma.eval('j')
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in eval(self, x, strip)
    278         ans = Expect.eval(self, x).replace('\\\n','')
    279         if 'Runtime error' in ans or 'User error' in ans:
--> 280             raise RuntimeError, "Error evaluation Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    281         return ans
    282 

<type 'exceptions.RuntimeError'>: Error evaluation Magma code.
IN:j;
OUT:
>> j;
   ^
User error: Identifier 'j' has not been declared or assigned
```


This is ridiculous.  It causes huge trouble for normal users.   Often people spend minutes or hours setting up a magma interface session -- to have it just die any time they hit control-c is ludicrous. 


```
sage: m = magma('Factorial(10^7)')
^CInterrupting Magma...
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)
    332             if isinstance(x, bool):
    333                 return Expect.__call__(self, str(x).lower())
--> 334             return Expect.__call__(self, x)
    335         return self.objgens(x, gens)
    336         

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    736             return x
    737         if isinstance(x, basestring):
--> 738             return cls(self, x)
    739         try:
    740             return self._coerce_from_special_method(x)

/Users/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    987             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    988                 self._session_number = -1
--> 989                 raise TypeError, x
    990         self._session_number = parent._session_number
    991 

<type 'exceptions.TypeError'>: Restarting Magma (WARNING: all variables defined in previous session are now invalid)
```



---

Comment by was created at 2008-10-24 03:40:54

This is completely fixed by changing the restart_on_ctrlc option. see attached 1-line patch.  

It's not possible to doctest this, but easy to test by hand.


---

Attachment

When you apply this to 3.2.alpha0 it may complain

```
Hunk #2 FAILED at 951
1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/magma.py.rej
```


This hunk #2 is a blank line, and is totally safe to ignore this failure.


---

Comment by mabshoff created at 2008-10-24 11:18:22

Looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-26 00:08:13

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 00:08:13

Merged in Sage 3.2.alpha1
