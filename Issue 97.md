# Issue 97: Limitation of number of variables when using the GP interface

Issue created by migration from https://trac.sagemath.org/ticket/97

Original creator: was

Original creation time: 2006-09-29 04:36:25

Assignee: was

From Jon Hanke:


```
There is an indexing overflow with the PARI interface, where if you
pass more than 32769 things then SAGE becomes unhappy. =( I have
attached the last part of the error message below.
							
Also, I would like an login/passwd on your bug tracking page so I
don't have to keep e-mailing these directly to you!   Thanks,
 
								-Jon
								 
 
 
==========================================================================================================
 
/ytmp/sage-1.3.6/local/lib/python2.4/site-packages/sage/interfaces/expect.py in __call__(self, *args)
    594
    595     def __call__(self, *args):
--> 596         return self._parent.function_call(self._name, list(args))
    597
    598
 
/ytmp/sage-1.3.6/local/lib/python2.4/site-packages/sage/interfaces/expect.py in function_call(self, function, args)
    553         for i in range(len(args)):
    554             if not isinstance(args[i], ExpectElement):
--> 555                 args[i] = self.new(args[i])
    556         return self.new("%s(%s)"%(function, ",".join([s.name() for s in args])))
    557
 
/ytmp/sage-1.3.6/local/lib/python2.4/site-packages/sage/interfaces/expect.py in new(self, code)
    456
    457     def new(self, code):
--> 458         return self(code)
    459
    460     ###################################################################
 
/ytmp/sage-1.3.6/local/lib/python2.4/site-packages/sage/interfaces/expect.py in __call__(self, x)
    453             return r
    454
--> 455         return cls(self, x)
    456
    457     def new(self, code):
 
/ytmp/sage-1.3.6/local/lib/python2.4/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    642             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    643                 self._session_number = -1
--> 644                 raise TypeError, x
    645         self._session_number = parent._session_number
    646
 
TypeError: Error executing code in GP/PARI:
CODE:
        sage[32771]=[[;], [;], [;], [;], []~, 0, [x, [1, 0], 1, 1, [Mat(1), Mat(1), 0, Mat(1), Mat(1), Mat(1), [0, Mat(1)]], [0.E-250], [1], Mat(1), Mat(1)], [[1, [], []], 1, 1, [2, -1], []], [[;], [], []], 0];
GP/PARI ERROR:
  ***   array index (32771) out of allowed range [1-32769]: sage[
  ***   32771]=[[;],[;],[;],
        ^--------------------
 ]}}


---

Comment by was created at 2007-01-13 01:51:36

This is not a problem in sage-1.6 anymore. 

William


---

Comment by was created at 2007-01-13 01:51:36

Resolution: fixed
