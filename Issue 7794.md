# Issue 7794: PolynomialRing_integral_domain ignores Ctrl-C and segfaults

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-12-30 10:52:47

Assignee: AlexGhitza

Keywords: Polynomial Ring KeyboardInterrupt

The following was reported by Alex P on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/d92efb12f35e758a):

```
sage: F.<a> = FiniteField(3)
sage: P.<T> = PolynomialRing(F)
sage: PP.<z> = PolynomialRing(P)
sage: PP
Univariate Polynomial Ring in z over Univariate Polynomial Ring in T over Finite Field of size 3
sage: type(PP)
<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_integral_domain'>
sage: (z^3 + T*z)^(81*3)
^CException KeyboardInterrupt: KeyboardInterrupt() in 'sage.rings.polynomial.polynomial_zmod_flint.get_cparent' ignored
^C^C

------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


So: First, Ctrl-C is ignored, which is bad IMO. Then, hitting Ctrl-C again (actually twice) results in a segfault, which is a desaster.




---

Comment by SimonKing created at 2011-05-19 18:08:26

Changing status from new to needs_review.


---

Comment by SimonKing created at 2011-05-19 18:08:26

I just verified that the problem seems to be fixed in sage-4.6.2.

Firstly, the original example now works sufficiently quickly, so that there is no need to interrupt the computation:

```
sage: F.<a> = FiniteField(3)
sage: P.<T> = PolynomialRing(F)
sage: PP.<z> = PolynomialRing(P)
sage: PP
Univariate Polynomial Ring in z over Univariate Polynomial Ring in T over Finite Field of size 3
sage: type(PP)
<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_integral_domain'>
sage: (z^3 + T*z)^(81*3)
z^729 + T^243*z^243
```


Secondly, if one tries the same thing with a higher exponent, hitting Ctrl-c works (or at least it does after several attempts):

```
sage: (z^3 + T*z)^(81^3)
^C^C^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/king/<ipython console> in <module>()

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.__pow__ (sage/rings/polynomial/polynomial_element.c:12738)()

/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.generic_power (sage/structure/element.c:20326)()
...
<LONG TRACEBACK>
...
/mnt/local/king/SAGE/broken/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10
     11 def my_sigfpe(x, n):

KeyboardInterrupt:
```


So, I believe this ticket can be closed! If I am not mistaken, I first need to put it as "needs review"...


---

Comment by SimonKing created at 2011-05-19 18:10:34

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2011-05-19 18:10:34

I miss the possibility to change the ticket into the state "worksforme", but that's my review, in one word...


---

Comment by jdemeyer created at 2011-05-19 20:00:10

I'm still able to reproduce the problem on sage-4.7.rc2 (note that interrupt handling was completely rewritten in #9678, merged in sage-4.7.alpha1, so testing this with sage-4.6.2 is pointless).


```
sage: F.<a> = FiniteField(3)
sage: P.<T> = PolynomialRing(F)
sage: PP.<z> = PolynomialRing(P)
sage: (z^3 + T*z)^(81*3)
^C^CException KeyboardInterrupt in 'sage.rings.polynomial.polynomial_zmod_flint.get_cparent' ignored
z^729 + T^243*z^243
sage: (z^3 + T*z)^(81*3)
^C/usr/local/src/sage-4.7/local/lib/libcsage.so(print_backtrace+0x31)[0x7f3398533e02]
/usr/local/src/sage-4.7/local/lib/libcsage.so(sigdie+0x14)[0x7f3398533e34]
/usr/local/src/sage-4.7/local/lib/libcsage.so(sage_signal_handler+0x1e6)[0x7f3398533a5c]
/lib/libpthread.so.0(+0xf400)[0x7f339d78c400]
/usr/local/src/sage-4.7/local/lib/libgmp.so.3(__gmp_exception+0x1e)[0x7f33982c357e]
/usr/local/src/sage-4.7/local/lib/libgmp.so.3(+0xb5ae)[0x7f33982c35ae]
/usr/local/src/sage-4.7/local/lib/libgmp.so.3(__gmpz_fdiv_ui+0x0)[0x7f33982cfed0]
/usr/local/src/sage-4.7/local/lib/libflint.so(zn_mod_init+0x5c)[0x7f33902e109c]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_zmod_flint.so(+0x19ce6)[0x7f336d5ddce6]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(+0x9b85c)[0x7f339da3485c]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyObject_Call+0x53)[0x7f339d9e3cf3]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyEval_CallObjectWithKeywords+0x47)[0x7f339da76617]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(+0x61747)[0x7f339d9fa747]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyObject_Call+0x53)[0x7f339d9e3cf3]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_zmod_flint.so(+0xad24)[0x7f336d5ced24]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(+0xa1098)[0x7f339da3a098]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyObject_Call+0x53)[0x7f339d9e3cf3]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyEval_EvalFrameEx+0x3a79)[0x7f339da7a689]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyEval_EvalCodeEx+0x879)[0x7f339da7d819]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(+0x70b26)[0x7f339da09b26]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyObject_Call+0x53)[0x7f339d9e3cf3]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(+0x5793f)[0x7f339d9f093f]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyObject_Call+0x53)[0x7f339d9e3cf3]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so(+0x12ec1)[0x7f3388decec1]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so(+0x12beb)[0x7f3388decbeb]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/categories/map.so(+0x6be5)[0x7f3394501be5]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/structure/coerce.so(+0x1fb4d)[0x7f339473eb4d]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/structure/coerce.so(+0x179e0)[0x7f33947369e0]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/structure/element.so(+0x108d9)[0x7f339496b8d9]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/structure/element.so(+0x3a681)[0x7f3394995681]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(+0x4621c)[0x7f339d9df21c]
/usr/local/src/sage-4.7/local/lib/libpython2.6.so.1.0(PyNumber_Add+0x20)[0x7f339d9e1640]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so(+0x41f03)[0x7f3388e1bf03]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so(+0x6ff62)[0x7f3388e49f62]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so(+0x6ed99)[0x7f3388e48d99]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so(+0x6ef0c)[0x7f3388e48f0c]
/usr/local/src/sage-4.7/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so(+0x6edcf)[0x7f3388e48dcf]

------------------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
```



---

Comment by jdemeyer created at 2011-05-19 20:00:10

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2011-05-20 05:36:04

Replying to [comment:3 jdemeyer]:
> I'm still able to reproduce the problem on sage-4.7.rc2 (note that interrupt handling was completely rewritten in #9678, merged in sage-4.7.alpha1, so testing this with sage-4.6.2 is pointless).

What a pity!


---

Comment by SimonKing created at 2011-05-20 06:25:39

Since the problem seems to be related with get_cparent, I was first looking into that. There was a bare "except:", where it should be catching an attribute error. But that was not the problem.

Next, I looked into polynomial_template.pxi, where get_cparent is frequently used. Too frequently, actually. In many methods it is called several times. So, it would be better to assign its output to a cdef'd variable -- that would actually boost the speed a lot!

Namely, working on other tickets, I know that the "harmless" method `modulus()` takes the most time when doing arithmetic with polynomials over finite fields. `modulus()` is called in get_cparent (actually, it is called twice!), and get_cparent is called several times in both _pow_ and _mul_ (as in polynomial_template.pxi).

So, one approach would be to remove the redundant calls - which makes sense anyway. If that does not help with the segfault, one could still try to wrap it into sig_on()/sig_off().


---

Comment by SimonKing created at 2011-05-20 06:39:22

It is really surprising how many redundant calls can be found in polynomial_template.pxi. I guess that's why get_cparent is defined as an inline cpdef function -- but that won't help if it internally calls pure Python functions!


---

Comment by jdemeyer created at 2011-05-20 08:41:25

The attached patch seems to fix the problem, but I haven't checked carefully whether it might break other stuff.  I'm putting it to needs_review, but I haven't really thought about it much.


---

Comment by jdemeyer created at 2011-05-20 08:41:25

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-05-20 12:13:35

Hi Jeroen,

Can you give me a pointer to the documentation of the `except? 0` syntax? Sounds useful.

I'll try your patch. I have prepared another patch, with the purpose of reducing the number of calls to get_cparent() (and thus to modulus()). But this will concern performance and should thus be on another ticket.


---

Comment by SimonKing created at 2011-05-20 12:18:01

I think a found a [reference](http://docs.cython.org/src/userguide/language_basics.html#error-return-values) to handling Cython errors.


---

Comment by SimonKing created at 2011-05-20 12:22:38

After reading the documentation, it seems to me that your approach makes very much sense. The original problem seems to be solved.

So, if the long doctests pass then I'll give it a positive review.


---

Comment by SimonKing created at 2011-05-20 12:33:12

Meanwhile I wonder:

In the original version of get_cparent, an attribute error was caught internally, and then zero was returned. Now, you return zero on error, and you do not catch the error internally. Couldn't that result in confusion, if the argument `parent` has no `modulus()` method?

Perhaps it is safer to keep modify the internal try-except clause (namely replace the bare `except:` by `except AttributeError:`) and declare the Cython funtion as `cdef inline cparent get_cparent(parent) except -1:`.

Namely, -1 can not result as a regular return value (the return value is the modulus of a ring, and thus a positive number), and so it would be safe to reserve -1 for errors (then you can also remove the question mark from `except?`).

Will you do this change (if you agree with my arguing), or shall I make the change in a separate patch?


---

Comment by SimonKing created at 2011-05-20 12:49:47

Replying to [comment:11 SimonKing]:
> Perhaps it is safer to keep modify the internal try-except clause (namely replace the bare `except:` by `except AttributeError:`) and declare the Cython funtion as `cdef inline cparent get_cparent(parent) except -1:`.

On the other hand:

 * In polynomial_zmod_flint, get_cparent is supposed to return unsigned int. So, -1 does not make sense.

 * The modulus is positive. So, actually 0 should be a clear sign that something went wrong. I wonder if the function is ever called with `parent=None` (because this is the only situation in which zero is returned).

I will test whether `parent is None` ever occurs. If not, then we could keep 0 as return value on error, but could remove the question mark (which should result in a faster code).


---

Comment by SimonKing created at 2011-05-20 12:52:30

Replying to [comment:12 SimonKing]:
> I will test whether `parent is None` ever occurs. If not, then we could keep 0 as return value on error, but could remove the question mark (which should result in a faster code).

Yes, it _is_ called with `parent=None`, namely when unpickling.


---

Comment by SimonKing created at 2011-05-20 13:11:38

I considered the following version of get_cparent in polynomial_zmod_flint.pyx:

```
cdef inline cparent get_cparent(parent) except 1:
    if parent is None:
        return 0
    try:
        return <unsigned long>(parent.modulus())
    except AttributeError:
        return 0
```


Rationale:

The original code was catching an error that should probably be an attribute error - so, we do the same, and return the same value that was returned by the original version.

But the return value 1 can never occur (which I verified by the doctests of sage/rings/). So, it is safe to reserve 1 as the exceptional value, without question mark after `except`.

However, our two patch versions performed equally when I tried some timings. Hence, unless you say that I convinced you to use 1 as exceptional return value (without question mark), I will give your patch a positive review, provided the doc tests pass.


---

Comment by SimonKing created at 2011-05-20 13:49:33

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2011-05-20 13:49:33

Tests pass. So, let it be a positive review to your patch!


---

Comment by jdemeyer created at 2011-05-20 18:00:37

Replying to [comment:14 SimonKing]:
> But the return value 1 can never occur (which I verified by the doctests of sage/rings/). So, it is safe to reserve 1 as the exceptional value, without question mark after `except`.
Are you *very sure* that 1 cannot occur?  You might be right, but I would not count on it.


---

Comment by jdemeyer created at 2011-05-20 18:05:12

you are probably right about `except AttributeError`. How about

```
cdef inline cparent get_cparent(parent) except? 0:
    try:
        return <unsigned long>(parent.modulus())
    except AttributeError:
        return 0
```

This will also catch the case `parent == None`.


---

Comment by SimonKing created at 2011-05-21 06:17:15

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2011-05-21 06:17:15

Replying to [comment:17 jdemeyer]:
> you are probably right about `except AttributeError`. How about
> {{{
> cdef inline cparent get_cparent(parent) except? 0:
>     try:
>         return <unsigned long>(parent.modulus())
>     except AttributeError:
>         return 0
> }}}
> This will also catch the case `parent == None`.

Yes, that looks a bit better. 

Concerning modulus 1:

It is possible to explicitly construct an instance of `sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint` whose parent has modulus 1:

```
sage: from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_mod_n
sage: P = PolynomialRing_dense_mod_n(Zmod(1),'x')
sage: type(P.0)
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
```


So, in order to be on the safe side, one should not have `get_cparent(parent) except 1:`.

One may argue, however, that it can not occur if one constructs a ring as one is supposed to, namely by calling the polynomial ring constructor:

```
sage: P.<x> = Zmod(1)[]
sage: type(x)
<type 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense'>
```


But better safe than sorry, in particular since your safe solution (`... except? 0:`) should have no serious time penalty.

Namely, as much as I understand, `cdef get_cparent(parent) except? 0:` will slow things down only if the return value is 0, because then it will be tested whether an error has actually occured.

But, to the best of my knowledge, it is _impossible_ to have a parent with modulus zero, even if one works around the polynomial ring constructor:

```
sage: P = PolynomialRing_dense_mod_n(ZZ,'x')
Traceback (most recent call last):
...
ValueError: invalid integer: +Infinity
```


So, if one has return value zero then something exceptional must be happening: Either it is a real error, or it is during pickling, when `parent` is None. So, we can certainly afford to test for an error in that situation.

Can you update your patch, so that the attribute error is caught? Then I'll run the tests again, and will hoppefully be able to renew my positive review.


---

Attachment


---

Comment by jdemeyer created at 2011-05-21 06:24:49

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-05-21 09:04:59

All long tests passed with your new patch.

I tried to add a doc test, as follows:

```
    sage: def test():
    ...    P = GF(3)['T']
    ...    PP = P['z']
    ...    T = P.gen()
    ...    z = PP.gen()
    ...    alarm(1)
    ...    try:
    ...       while(1):
    ...           x = (z**3+T*z)**243
    ...    except KeyboardInterrupt:
    ...       print "First interrupt caught"
    ...    alarm(1)
    ...    try:
    ...        while(1):
    ...            x = (z**3+T*z)**243
    ...    except KeyboardInterrupt:
    ...        print "Second interrupt caught"
    sage: test()
    First interrupt caught
    Second interrupt caught
```


However, it did not work, since there seem to be other places in which errors are not properly caught. Namely, I occasionally got:

```
sage: test()
First interrupt caught
Exception KeyboardInterrupt: KeyboardInterrupt('computation timed out because alarm was set for 1 seconds',) in T^79 + 2*T^78 + 2*T^77 + T^74 ignored
^CSecond interrupt caught
```

So, the first alarm worked, but the second didn't, and only when I pressed <ctrl>-c then the computation was interrupted.

What shall we do now? Clearly, your patch is a progress. So, I tend to give it a positive review (because all tests pass), and deal with the remaining problem on a different ticket.

What do you think?


---

Comment by jdemeyer created at 2011-05-23 10:38:19

Replying to [comment:21 SimonKing]:
> What do you think?

I'll see if I can identify the problem.


---

Comment by jdemeyer created at 2011-05-23 15:09:19

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-23 15:09:19

I cannot easily identify the problem, so let's put it to positive_review (even though I agree the isuue is not 100% solved).


---

Comment by jdemeyer created at 2011-05-24 07:52:00

I have tracked the `Exception KeyboardInterrupt... ignored` problem
down to the following Cython-generated code in `sage/rings/polynomial/polynomial_zmod_flint.c`:


```
static void __pyx_tp_dealloc_4sage_5rings_10polynomial_21polynomial_zmod_flint_Polynomial_template(PyObject *o) {
  {
    PyObject *etype, *eval, *etb;
    PyErr_Fetch(&etype, &eval, &etb);
    ++Py_REFCNT(o);
    __pyx_pf_4sage_5rings_10polynomial_21polynomial_zmod_flint_19Polynomial_template_3__dealloc__(o);
    if (PyErr_Occurred()) PyErr_WriteUnraisable(o);
    --Py_REFCNT(o);
    PyErr_Restore(etype, eval, etb);
  }
  __pyx_ptype_4sage_5rings_10polynomial_18polynomial_element_Polynomial->tp_dealloc(o);
}
```


The problem is the line

```
if (PyErr_Occurred()) PyErr_WriteUnraisable(o);
```

Since this code is generated by Cython, perhaps it is not possible to solve this problem without patching Cython.


---

Comment by jdemeyer created at 2011-05-24 09:06:58

I believe the "Exception ignored" to be harmless, in the sense that it's not going to break anything or cause segmentation faults.  If the exception is ignored, the computation simply continues and the user can press ctrl-C a second time and that should do it.


---

Comment by SimonKing created at 2011-05-24 09:23:16

Replying to [comment:25 jdemeyer]:
> I believe the "Exception ignored" to be harmless, in the sense that it's not going to break anything or cause segmentation faults.  If the exception is ignored, the computation simply continues and the user can press ctrl-C a second time and that should do it.

Yes, but it made it impossible for me to create a doctest for your fix!


---

Comment by jdemeyer created at 2011-05-30 14:52:02

Resolution: fixed
