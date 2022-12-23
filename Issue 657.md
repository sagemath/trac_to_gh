# Issue 657: Strange is_zero behavior for symbolics

Issue created by migration from https://trac.sagemath.org/ticket/657

Original creator: robertwb

Original creation time: 2007-09-14 21:06:10

Assignee: was

This may be due to how cmp is implemented (to produce symbolic expressions).


```
On Aug 14, 2007, at 2:07 AM, PaulOlivierSage@gmail.com wrote:


Hi,
I have some problems with the way is_zero() is implemented (or maybe
it is the documentation...)
Is this behavior really desirable?

sage: k = var('k')
sage: pol = 1/(k-1) - 1/k -1/k/(k-1)
sage: pol
-1/((k - 1)*k) - (1/k) + 1/(k - 1)
sage: pol.partial_fraction()
0
sage: pol.is_zero()
False
sage: pol.is_zero??
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in method is_zero of SymbolicArithmetic object
at 0xc4b6af8>
Namespace:      Interactive
Source:
    def is_zero(self):
        """
        Return True if self equals self.parent()(0). The default
        implementation is to fall back to 'not self.__nonzero__'.

        NOTE: Do not re-implement this method in your subclass but
        implement __nonzero__ instead.
        """
        return not self
sage: pol == pol.parent()(0)
-1/((k - 1)*k) - (1/k) + 1/(k - 1) == 0

Paul
```



---

Comment by mhansen created at 2007-10-24 01:48:46

Changing status from new to assigned.


---

Comment by mhansen created at 2007-10-24 01:48:46

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-10-24 01:48:46

I've made some changes to how equality testing is done with symbolic expressions.

Before patch:

```
sage: k = var('k')
sage: pol = 1/(k-1) - 1/k -1/k/(k-1);
sage: pol
-1/((k - 1)*k) - 1/k + 1/(k - 1)
sage: pol.partial_fraction()
0
sage: pol.is_zero()
False
sage: bool(pol == 0)
False
sage: f = sin(x)^2 + cos(x)^2 - 1
sage: f.is_zero()
False
sage: f.simplify_trig()
0
sage: bool(f == 0)
False
```


After patch:

```
sage: sage: k = var('k')
sage: sage: pol = 1/(k-1) - 1/k -1/k/(k-1);
sage: sage: pol
-1/((k - 1)*k) - 1/k + 1/(k - 1)
sage: sage: pol.partial_fraction()
0
sage: sage: pol.is_zero()
True
sage: sage: bool(pol == 0)
True
sage: sage: f = sin(x)^2 + cos(x)^2 - 1
sage: sage: f.is_zero()
True
sage: sage: f.simplify_trig()
0
sage: sage: bool(f == 0)
True
```



---

Comment by was created at 2007-10-24 02:06:51


```
19:05 < wstein> mhansen -- I personally like 657.
19:06 < wstein> I mean, if there is a simplification that makes it 0, then it better be 0.
19:06 < wstein> The problem is of course that it could take a long time.
19:06 < wstein> But these are symbolic, so speed isn't the main thing.
```



---

Comment by malb created at 2007-10-24 20:24:40

Resolution: fixed


---

Comment by malb created at 2007-10-24 20:24:40

applied to 2.8.9.alpha1


---

Comment by malb created at 2007-10-24 21:49:41

This caused many doctests to fail, please re-apply against 2.8.9 once it is released.


---

Comment by malb created at 2007-10-24 21:49:45

Resolution changed from fixed to 


---

Comment by malb created at 2007-10-24 21:49:45

Changing status from closed to reopened.


---

Attachment

Patch updated.


---

Comment by cwitty created at 2007-10-27 02:42:25

Resolution: fixed
