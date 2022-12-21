# Issue 5294: Pickle Jar documentation

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-02-17 18:08:39

Assignee: tba

Keywords: picklejar, documentation

On sage-combinat-devel Michael wrote:

 "The pickle jar is not in the documentation AFAIK and it definitely should be. So someone who thinks this is a good idea please open a ticket."

I definitely think this is a good idea.


---

Comment by andrew.mathas created at 2012-10-19 00:45:20

The attached patch improves the pickle_jar documentation, with the primary aim of telling developers what to do (and not do) when their code breaks a pickle in the pickle_jar. I've added a version of the manual page produced so that people can comment on this without having to rebuild the manual -- unfortunately it doesn't display as html....


---

Comment by andrew.mathas created at 2012-10-19 12:23:57

Currently one doc test fails, but I don't think that this is an issue with the patch. This seems to have nothing to do with the patch but, rather, is a consequence of the following which looks like a bug to me:


```
sage: from sage.structure.sage_object import unpickle_all
sage: %timeit unpickle_all()
/usr/local/src/sage/sage-5.3/local/lib/python/timeit.py:195: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
See http://trac.sagemath.org/4260 for details.
  timing = self.inner(it, self.timer)

------------------------------------------------------------------------
Unhandled SIGABRT: An abort() occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
/usr/local/src/sage/sage-5.3/spkg/bin/sage: line 335: 73974 Abort trap: 6           sage-ipython "$`@`" -i
```

Can anyone confirm whether this is a bug or known issue? Either way, is there a way around this? 

Alternatively I could just remove this doc test from unpickle_all() as it is now referred to in the section in the developers guide.


---

Comment by roed created at 2012-10-19 16:30:52

* The SIGABRT is certainly a bug, and a quick google search doesn't reveal any tickets related to it.  Opening a new ticket seems reasonable.  What's the doctest that fails?
 * The changes in trac_5294--improving_pickle_jar_documentation-am.patch look great to me.  Here are a few more improvements I would suggest. 
   * Mention that pickling and unpickling is different for Cython classes and give some examples of how to write pickling code in this case.  See http://ask.sagemath.org/question/808/pickling-extension-classes and http://docs.python.org/library/pickle.html#pickling-and-unpickling-extension-types.  If you don't want to do this here we can open another ticket.
   * Refer to sage.misc.explain_pickle as a tool to figure out what's in an old pickle that doesn't work any more.


---

Comment by andrew.mathas created at 2012-10-19 21:19:21

Replying to [comment:3 roed]:
> The SIGABRT is certainly a bug, and a quick google search doesn't reveal any tickets related to it.  Opening a new ticket seems reasonable.  What's the doctest that fails?

The doctest that fails is essentially the problem above. The actual doctest, which appears below, is in unpickle_all() and it ends with the command unpickle_all(). It runs fine from the command line back buts when you run it via the doctest framework. The difference, I think, is that during a doctest the code is running inside of (something like) timeit(). Here is the doctest:


```
sage: from sage.structure.sage_object import unpickle_all, register_unpickle_override
sage: class A(CombinatorialObject,sage.structure.element.Element):
...       pass # to break a pickle
sage: register_unpickle_override('sage.combinat.tableau','Tableau_class',A) # breaking the pickle
sage: unpickle_all()  # long time
```



---

Comment by andrew.mathas created at 2012-10-22 02:27:27

I have added some comments about cython and explain_pickle (and filed the ticket #13636 for the bug). I also added sections to the developers guide at the end of the chapters "Conventions for Coding in Sage" and "Coding in Cython about (un)pickling.


---

Comment by andrew.mathas created at 2012-11-01 23:17:16

I noticed that there were other calls to unpickle_all() in the documentation so after playing around for a little I worked out the register_unpickle_override calls in the doctests were causing the SEGABRT.  (However, the bug reported in #13636 appears to be real as it is independent of this patch.)

I have rewritten the relevant examples in the documentation so all doc tests now pass.


---

Comment by andrew.mathas created at 2012-11-01 23:26:01

Changing status from new to needs_review.


---

Comment by andrew.mathas created at 2012-11-01 23:26:24

Changing assignee from tba to andrew.mathas.


---

Comment by saraedum created at 2012-11-22 15:51:23

A very valuable addition to the documentation!

I think I found two minor issues though:

* In the excerpt from the python docs about `object.__setstate__(state)` you lost some underscores (it should say `__setstate__` and not `setstate__`.)
* You should probably remove the trailing whitespace in the `__reduce__` function that the patchbot complains about

Btw., the patchbot coverage plugin complains that you added one method without a doctest. But this is actually just, the `__reduce___` method in the docstring.

I don't have the time to look at the html version of the documentation now, I'll do that soon, write a review patch with the above two points, and set it to positive review.


---

Comment by andrew.mathas created at 2012-11-23 04:47:47

Thanks for this Julian. I have uploaded a new version of the patch which fixes the setstate  and the whitespace problems. To address the coverage plugin complaint I added in a doctest for dumps(), so now the coverage count is (should be) increased by the patch.

Andrew


---

Comment by andrew.mathas created at 2013-01-07 01:02:15

Changing keywords from "picklejar, documentation" to "picklejar, documentation, beginner".


---

Comment by saraedum created at 2013-01-07 22:30:10

Sorry this took so long to finally have a look at this :(

One minor issues:

* your patch file should start with "Trac #5294: Adds information ..."

I found a few small problems in your patch and wrote a review patch for it. If you're happy with these changes, feel free to set it to positive review.


---

Comment by andrew.mathas created at 2013-01-08 02:19:50

Changing status from needs_review to positive_review.


---

Comment by andrew.mathas created at 2013-01-08 02:19:50

Thanks very much Julian. I have folder in your review patch and set it to a positive review.


---

Comment by jdemeyer created at 2013-01-08 09:31:57

The docbuilder doesn't like all those weird characters on line 218 of `sage/structure/sage_object.pyx`:

```
! Package ucs Error: Unknown Unicode character 156 = U+009C,
(ucs)                possibly declared in uni-0.def.
(ucs)                Type H to see if it is available with options.

See the ucs package documentation for explanation.
Type  H <return>  for immediate help.
 ...

l.111426 ...~TÃ¤^^RÂ®{}` Ã~[^^_Ã~B,dÃ~Tl,dÃ~R\PYGZca{}}

?
! Emergency stop.
 ...

l.111426 ...~TÃ¤^^RÂ®{}` Ã~[^^_Ã~B,dÃ~Tl,dÃ~R\PYGZca{}}

!  ==> Fatal error occurred, no output PDF file produced!
```



---

Comment by jdemeyer created at 2013-01-08 09:31:57

Changing status from positive_review to needs_work.


---

Comment by andrew.mathas created at 2013-01-08 12:09:10

Thanks for tracking down the code block for me. It's embarrassing that you keep on finding all of these errors that I don't...fixed now I think.

Andrew


---

Comment by andrew.mathas created at 2013-01-08 12:09:10

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-01-08 15:22:06

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-01-08 15:22:06

There's an obvious doctest failure:

```
sage -t  -force_lib devel/sage/doc/en/developer/conventions.rst
**********************************************************************
File "/release/merger/sage-5.6.beta3/devel/sage-main/doc/en/developer/conventions.rst", line 1040:
    sage: sage -t structure/sage_object.pyx
Exception raised:
    Traceback (most recent call last):
      File "/release/merger/sage-5.6.beta3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/release/merger/sage-5.6.beta3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/release/merger/sage-5.6.beta3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[2]>", line 1
        sage -t structure/sage_object.pyx###line 1040:
    sage: sage -t structure/sage_object.pyx
                        ^
    SyntaxError: invalid syntax
**********************************************************************
```



---

Comment by jdemeyer created at 2013-01-08 15:25:30

And perhaps this failure is also caused by this ticket:

```
sage -t  --long -force_lib devel/sage/sage/structure/sage_object.pyx
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(print_backtrace+0x2b)[0x2ba301ee166e]
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(sigdie+0x14)[0x2ba301ee169b]
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(sage_signal_handler+0x1d8)[0x2ba301ee1156]
/lib/libpthread.so.0[0x2ba2fff4b7d0]
/lib/libc.so.6(gsignal+0x35)[0x2ba3008140c5]
/lib/libc.so.6(abort+0x110)[0x2ba300815b20]
/release/merger/sage-5.6.beta3/local/lib/libcsage.so(init_csage+0x0)[0x2ba301ee1fc8]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL5ErrorEPKc+0x1f)[0x2ba30255e4cf]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL6InvModEll+0x39)[0x2ba3024ad1a9]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL8PlainRemERNS_5zz_pXERKS0_S3_+0x2a9)[0x2ba3025222a9]
/release/merger/sage-5.6.beta3/local/lib/libntl.so.0(_ZN3NTL3GCDERNS_5zz_pXERKS0_S3_+0x19a)[0x2ba30252f7fa]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so[0x2ba31acb0216]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x605)[0x2ba31acabda5]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z3gcdRK13CanonicalFormS1_+0x257)[0x2ba31acac2e7]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so[0x2ba31acae0fd]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7contentRK13CanonicalFormRK8Variable+0xce)[0x2ba31acae29e]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7contentRK13CanonicalFormRK8Variable+0x62)[0x2ba31acae232]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z7EZGCD_PRK13CanonicalFormS1_+0xde8)[0x2ba31acc5378]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x59f)[0x2ba31acabd3f]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z11chinrem_gcdRK13CanonicalFormS1_+0xbab)[0x2ba31acad13b]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z8gcd_polyRK13CanonicalFormS1_+0x656)[0x2ba31acabdf6]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z3gcdRK13CanonicalFormS1_+0x257)[0x2ba31acac2e7]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z14singclap_gcd_rP8spolyrecS0_P9sip_sring+0xf8)[0x2ba31ab0ba28]
/release/merger/sage-5.6.beta3/local/lib/libsingular.so(_Z12singclap_gcdP8spolyrecS0_+0x56)[0x2ba31ab0eb26]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so[0x2ba31a7851df]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so[0x2ba31a7868ef]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x56)[0x2ba2ffc3eb26]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbbad06]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/element.so[0x2ba3093808c3]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba315661005]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba31565941c]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbfa5a8]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/rings/fraction_field_element.so[0x2ba31564b644]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x56)[0x2ba2ffc3eb26]
/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528381e]
/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528a162]
/release/merger/sage-5.6.beta3/local/lib/python2.7/lib-dynload/cPickle.so[0x2ba30528dc35]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d2bbc4]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d1c693]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/python/site-packages/sage/structure/sage_object.so[0x2ba305d23d06]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5de2)[0x2ba2ffc45662]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x2ba2ffc47472]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x714e)[0x2ba2ffc469ce]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbcb9b9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0[0x2ba2ffbae8bf]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyObject_Call+0x68)[0x2ba2ffb9e308]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x1299)[0x2ba2ffc40b19]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5ae4)[0x2ba2ffc45364]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x852)[0x2ba2ffc47352]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x2ba2ffc47472]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyRun_FileExFlags+0xc1)[0x2ba2ffc6b1f1]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(PyRun_SimpleFileExFlags+0x1f9)[0x2ba2ffc6b4c9]
/release/merger/sage-5.6.beta3/local/lib/libpython2.7.so.1.0(Py_Main+0xb15)[0x2ba2ffc7e115]
/lib/libc.so.6(__libc_start_main+0xf4)[0x2ba3008001f4]
python[0x400679]

------------------------------------------------------------------------
Unhandled SIGABRT: An abort() occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
Aborted
```



---

Comment by andrew.mathas created at 2013-01-09 02:05:37

I'm confused because the first test

```
sage -t -force_lib devel/sage/doc/en/developer/conventions.rst
```

passes on sage 5.5. So I compiled 5.6.beta2 (beta3 has not been released yet) and it works there too. Nonetheless, even though I can't replicate the error I agree that there is a problem here so I've fixed it, but I can't check that it's fixed.

With the second test, 

```
sage -t --long -force_lib devel/sage/sage/structure/sage_object.pyx
```

I get a timeout error rather than a SIGBART. It's caused by a call to 

```
sage: unpickle_all() # long time
```

This test works but it would take longer than the _#long time_ tests are supposed to take so I have replaced this with

```
sage: unpickle_all()  # todo: not tested
```



---

Comment by jdemeyer created at 2013-01-09 07:17:07

Replying to [comment:19 andrew.mathas]:
> I'm confused because the first test
> {{{
> sage -t -force_lib devel/sage/doc/en/developer/conventions.rst
> }}}
> passes on sage 5.5.
Sorry, I know what happened. There are some formatting errors in that file with the consequence that doctests aren't run. This is fixed by #13899.


---

Comment by andrew.mathas created at 2013-01-09 08:47:56

Replying to [comment:20 jdemeyer]:

> Sorry, I know what happened. There are some formatting errors in that file with the consequence that doctests aren't run. This is fixed by #13899.

Thanks for the explanation. Does that mean that the problem with this patch is fixed or should it depend on, and need to be rebased over, #13899?

Andrew


---

Comment by jdemeyer created at 2013-01-09 08:50:41

This patch doesn't depend on #13899, but it should be tested with #13899 applied.


---

Comment by andrew.mathas created at 2013-01-10 09:50:34

Changing status from needs_work to positive_review.


---

Comment by andrew.mathas created at 2013-01-10 09:50:34

I've just tested the patch against 5.6.beta3, which has #13899 applied, and the tests above pass. I'm checking everything else now but given that the patch only touches doctests I don't think that they can possibly fail, so I'll put it back to a positive review.


---

Comment by andrew.mathas created at 2013-01-10 10:22:11

Replying to [comment:23 andrew.mathas]:
> I've just tested the patch against 5.6.beta3, which has #13899 applied, and the tests above pass. I'm checking everything else now but given that the patch only touches doctests I don't think that they can possibly fail, so I'll put it back to a positive review.


Just to confirm: all tests pass on 5.6.beta3


---

Comment by jdemeyer created at 2013-01-12 15:05:42

There is still:

```
sage -t  -force_lib devel/sage/doc/en/developer/conventions.rst
**********************************************************************
File "/release/merger/sage-5.7.alpha0/devel/sage-main/doc/en/developer/conventions.rst", line 1052:
    sage: sage -t devel/sage-main/sage/structure/sage_object.pyx
Exception raised:
    Traceback (most recent call last):
      File "/release/merger/sage-5.7.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/release/merger/sage-5.7.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/release/merger/sage-5.7.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[2]>", line 1
        sage -t devel/sage-main/sage/structure/sage_object.pyx###line 1052:
    sage: sage -t devel/sage-main/sage/structure/sage_object.pyx
                    ^
    SyntaxError: invalid syntax
**********************************************************************
```



---

Comment by jdemeyer created at 2013-01-12 15:05:42

Changing status from positive_review to needs_work.


---

Comment by andrew.mathas created at 2013-01-13 08:48:49

UPdated patch fixing conventions.srt problem


---

Attachment

Sorry in all of the excitement I forgot to update the patch on the ticket.


---

Comment by andrew.mathas created at 2013-01-22 12:14:58

I have tested the patch against 5.6.rc1 and the tests pass. For some reason the patchbot isn't checking the ticket, possibly because it's flagged as needing work? I am going to put it back to a positive review in the hope that the patchbot confirms my tests before Jeronen looks at it.


---

Comment by andrew.mathas created at 2013-01-22 12:14:58

Changing status from needs_work to positive_review.


---

Comment by slabbe created at 2013-01-25 00:22:54

Concerning the pickle jar, I use this opportunity to make some publicity for #10705.


---

Comment by andrew.mathas created at 2013-01-25 00:51:21

Replying to [comment:30 slabbe]:
> Concerning the pickle jar, I use this opportunity to make some publicity for #10705.

See #13636 for another seg fault associated with unpickle_all.


---

Comment by jdemeyer created at 2013-01-26 09:52:13

Resolution: fixed
