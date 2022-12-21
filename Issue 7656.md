# Issue 7656: Bitset tricks

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-12-11 04:03:16

Assignee: tbd

There are some extra tricks in here: http://www.jjj.de/fxt/#fxtbook

in the first chapter for doing bitset operations that ought to be applied to our Bitset class.  For example, there is a trick that allows you to count the number of bits in log time instead of linear time.


---

Comment by jason created at 2010-05-11 20:49:23

Changing priority from major to minor.


---

Comment by ncohen created at 2011-05-02 16:19:41

This FXTBook is the best book in the universe. I'm *EAGER* to read it.

About the counting trick : there is a builtin gcc command called __builtin_popcount which may do wonders. It does count the bits in general (though I haven't found the corresponding code) -- it may well be the logarithmic way (+very nice trick btw), and in case the popcnt instruction is available on the processor, it is directly called.

And I assure you for having compared the two that it does.... WONDERS :-D

Nathann


---

Comment by jason created at 2011-05-02 18:41:41

If we can guarantee that gcc is used to compile the file, then great!  I think we can assume that for now, but it may not be true in the future.  Is there a preprocessor check we can put in or something?


---

Comment by ncohen created at 2011-05-03 12:40:03

I'd say "test for ``__GNUC__`` with the preprocessor". Though on these aspects I'd ask David first `:-D`

http://gcc.gnu.org/onlinedocs/cpp/Common-Predefined-Macros.html

Nathann


---

Comment by ncohen created at 2011-05-03 12:45:40

Oh. Actually I already did and he advised to use this very piece of code 

```
#ifdef __GNUC__
 /* Make use of GCC extensions here. */
#else
/* Add portable version here */
#endif
```


Give to Caesar [..] `:-)`

Nathann


---

Comment by jdemeyer created at 2013-12-10 13:12:49

This ticket is very vague. It should either be made more concrete (like, *what* do you want to do with bitsets) or closed as "invalid".


---

Comment by jdemeyer created at 2014-09-11 09:12:03

...and it's probably superseded by #16937 also.


---

Comment by jdemeyer created at 2014-09-11 09:12:03

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-09-11 09:12:09

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-15 14:56:06

Resolution: duplicate
