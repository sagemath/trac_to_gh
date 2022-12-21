# Issue 2877: security risk -- several constructors use eval to parse input

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-04-11 11:39:56

Assignee: cwitty

CC:  tscrim slelievre @kliem klee

There are valid uses for eval() and sage_eval(), it makes it much easier to parse output from  interfaces for example. 

It is difficult (if not impossible) to completely sanitize arbitrary input, but one should be able to be able to (say) write a backend that takes specific data, calls on Sage to process it, and then returns the result. For example, I might want a webpage that uses Sage to compute Julia sets, and takes as input a complex number. That the following work is scary 


```
sage: CC("os.getpid()")
10324.0000000000
sage: CC("os.mkdir('a')")
NaN - NaN*I
sage: CC("os.rmdir('a')")
NaN - NaN*I
sage: CC("os.exec(...)")
```



---

Comment by robertwb created at 2008-04-11 11:40:49

See #2347 which is related.


---

Comment by AlexGhitza created at 2009-01-23 02:46:22

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2014-09-02 09:00:29

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-09-02 09:00:29

Sage is not a secure program and nobody ever claimed it was. Sanitise your input before sending it to Sage!


---

Comment by jdemeyer created at 2014-09-02 09:00:34

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-09 14:52:21

Resolution: invalid


---

Comment by embray created at 2019-07-05 16:41:48

A strange response coming from Jeroen.  The use of `sage_eval` to convert arbitrary string inputs to elements of different fields is, I think, obviously bad on so many levels, and badly mishandled in several cases (e.g. some of them will catch `NameError`s, but not `SyntaxError`s; some will just work, but in weird ways, if you pass some arbitrary string; some are just broken as in https://ask.sagemath.org/question/47068/possible-bug-in-cc-needs-confirmation )

If you want to convert string representations of some elements of a field to actual elements of that field there should be proper parsing, not just arbitrary evals.


---

Comment by embray created at 2019-07-05 16:41:48

Resolution changed from invalid to 


---

Comment by embray created at 2019-07-05 16:41:48

Changing status from closed to new.


---

Comment by vbraun created at 2019-07-06 12:05:39

A simpler fix would be to use a limited eval, e.g. https://newville.github.io/asteval/

The reason for the eval in CC is of course that you want to allow expressions like `2+3*I` that exceed python's `literal_eval` capabilities.


---

Comment by vdelecroix created at 2019-07-11 19:54:37

I fully agree with Erik.

The following does not work (as expected)

```
sage: ZZ('2**3 + 3*g - 2')
Traceback (most recent call last):
...
TypeError: unable to convert '2**3 + 3*g - 2' to an integer
sage: RR('2**2 + 3*5 - 2')
Traceback (most recent call last):
...
TypeError: unable to convert '2**3+5*I-2' to a real number
```

Supporting the following with `CC` is a nonsense

```
sage: CC('2**2 + 3*5 - 2')
17.0000000000000
sage: CC('erf(2)')
0.995322265018953
```

We don't want the element constructor to evaluate a string in hope that it gives a complex number. There should be a clear definition of what is the input format. And the constructor should just stick to specifications. The element constructor of CC is trying to do much more than what it is supposed to.


---

Comment by vdelecroix created at 2019-07-11 19:57:09

And to my mind the main problem is *not* the security risk (I agree with Jeroen on that point). I would advice to open another ticket "fix element constructor of CC".


---

Comment by embray created at 2019-07-12 08:47:05

It's not just CC.  It's all of them.  It's really flaky to allow a general eval to construct instances of some particular type.  Instead, it should really just parse constant-valued expressions for whatever that type is, at the most.  That can either involve custom parsing code, or as Volker suggested a custom AST parser.


---

Comment by embray created at 2019-07-12 08:47:19

Replying to [comment:12 vbraun]:
> A simpler fix would be to use a limited eval, e.g. https://newville.github.io/asteval/
> 
> The reason for the eval in CC is of course that you want to allow expressions like `2+3*I` that exceed python's `literal_eval` capabilities.

+1


---

Comment by embray created at 2019-12-30 14:48:17

Ticket retargeted after milestone closed


---

Comment by mkoeppe created at 2020-04-14 19:41:51

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by chapoton created at 2021-10-19 15:03:00

here is a simple-minded patch. Unless somebody proposes something better, I think it makes sense to merge that now
----
New commits:


---

Comment by chapoton created at 2021-10-19 15:03:00

Changing status from new to needs_review.


---

Comment by git created at 2021-10-19 18:19:59

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2021-10-20 07:18:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2021-10-20 11:22:57

bot is morally green, so please review


---

Comment by tscrim created at 2021-10-20 23:47:56

Do we also want to allow `j` to match Python's convention for complex numbers:

```sage
sage: complex('1+2j')
(1+2j)
sage: complex('1+2i')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-a2113f9c148b> in <module>
----> 1 complex('1+2i')

ValueError: complex() arg is a malformed string
```



---

Comment by git created at 2021-10-21 07:00:51

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by chapoton created at 2021-10-21 07:01:36

ok, done (and squashed the commits)


---

Comment by chapoton created at 2021-10-21 07:02:37

but this will break the doctest in singular.pyx... (sigh)


---

Comment by git created at 2021-10-21 07:03:29

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by chapoton created at 2021-10-21 11:50:59

bot is morally green now


---

Comment by klee created at 2021-10-22 04:34:07

Sorry for late comment, but how about this?

```diff
--- a/src/sage/rings/complex_mpfr.pyx
+++ b/src/sage/rings/complex_mpfr.pyx
`@``@` -504,7 +504,7 `@``@` class ComplexField_class(sage.rings.abc.ComplexField):
             sage: CC('hello')
             Traceback (most recent call last):
             ...
-            ValueError: given string (hello) is not a complex number
+            ValueError: given string 'hello' is not a complex number
         """
         if not isinstance(x, (RealNumber, tuple)):
             if isinstance(x, ComplexDoubleElement):
`@``@` -516,7 +516,7 `@``@` class ComplexField_class(sage.rings.abc.ComplexField):
                 x = x.replace('E', 'e')
                 allowed = '+-.*0123456789Ie'
                 if not all(letter in allowed for letter in x):
-                    raise ValueError(f'given string ({x}) is not a complex number')
+                    raise ValueError(f'given string {x!r} is not a complex number')
                 # This should rather use a proper parser to validate input.
                 # TODO: this is probably not the best and most
                 # efficient way to do this.  -- Martin Albrecht
```


and `does not express a complex number`.


---

Comment by tscrim created at 2021-10-22 05:14:59

Thank you. I am also wondering a bit if we want to document that `CC` also supports `j` as a valid string input. Although I don't hold a strong opinion on this.


---

Comment by git created at 2021-10-22 06:39:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2021-10-22 06:43:36

ok, done.

WARNING: note that CC('1.0+2.0*j') works, but not CC('1.0+2.0j').


---

Comment by git created at 2021-10-24 07:35:07

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by chapoton created at 2021-10-24 07:35:38

I fixed the failing doctest


---

Comment by tscrim created at 2021-10-24 23:42:17

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2021-10-24 23:42:17

Great, thank you. LGTM. Kwankyu, if you do not agree, feel free to revert the positive review.


---

Comment by klee created at 2021-10-25 06:11:15

Replying to [comment:39 tscrim]:
> Great, thank you. LGTM. Kwankyu, if you do not agree, feel free to revert the positive review.

I fully agree. Thanks.


---

Comment by slelievre created at 2021-10-25 09:59:54

Update ticket summary and description
to better describe the changes made here?

(Or just contract "should be able to be able to"
if the rest is still fine?)


---

Comment by chapoton created at 2021-10-25 12:05:44

voilà, voilà.


---

Comment by slelievre created at 2021-10-25 12:23:25

Merci.


---

Comment by vbraun created at 2021-10-28 22:40:01

Resolution: fixed
