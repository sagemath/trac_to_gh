# Issue 8495: Regression: Many mathematica doctests fail

Issue created by migration from Trac.

Original creator: flawrence

Original creation time: 2010-03-11 06:33:47

Assignee: was

CC:  burcin jason

Since #3587, which implements a _sage_() method for mathematica elements, many mathematica doctests fail.  E.g:


```
sage: def math_bessel_K(nu,x): 
     ...       return mathematica(nu).BesselK(x).N(20).sage() 
     ... 
     sage: math_bessel_K(2,I) 
NotImplementedError: Unable to parse 
Mathematica output: 
-2.5928861754911969781676606702635284285719718407749199115289`20.1494653502 82203 
+ 
0.1804899720669620266296208808560650432663536549483055754141`18.99213497581 376*i 

```



---

Comment by flawrence created at 2010-03-11 06:42:51

Before #3587, mathematica's output was sent to ExpectElement._sage_repr() in expect.py, which called repr() and tidied up the results (converting {} to [], stripping new line characters etc) then sage_eval() was called on the results.  With this approach, mathematica functions that returned numbers, symbolic variables or arrays could be imported successfully into sage.  The approach had the disadvantage that all symbolic variables had to be passed in manually as locals, and that functions couldn't be translated from mathematica to their equivalents in sage.

#3587 instead calls str() on mathematica's results (which has the alarming option ascii_art = True), then replaces []s by (), changes everything to lower case and sends it to SR.  This works for simple functions but fails for arrays and probably anything affected by ascii_art = True

I'm not familiar with SR, but at a minimum MathematicaElement._sage_() should be patched to call sage_repr() instead of str().  I don't know whether SR has all the functionality of sage_eval(), e.g. supporting arrays.


---

Comment by flawrence created at 2010-03-14 12:59:36

I've uploaded a patch that has a thorough rewrite of MathematicaElement._sage_() to get the functionality from #3587 while keeping the functionality from before it (lists, complex numbers, numbers in scientific notation...).  I still need to write some documentation for the top of the file (i.e. documentation that makes it into the reference manual) but before I do that and submit this for formal review I'd like wise comments about my approach, e.g. "The way you convert function names is really inefficient and problematic, do it this way...", or "You can efficiently get a list of all sage functions recognised by sage_eval() by ...".

Also if someone could check the doctests on a 32-bit computer and let me know the result that they get instead of
[[1.00000000000000, 4], pi, 3.20000000000000*e100, I]
that would be grand.


---

Comment by flawrence created at 2010-03-14 12:59:36

Changing assignee from was to flawrence.


---

Comment by flawrence created at 2010-04-06 05:20:22

I've updated the patch file so that it updates the Mathematica module documentation.  This needs to be doctested on a 32-bit computer at some point.


---

Comment by flawrence created at 2010-04-06 05:20:22

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-07-19 20:05:32

There is dictionary in place from Mathematica to Sage.


```

sage: sage.symbolic.pynac.symbol_table['mathematica']
{'Log[2]': log2, 'Cos': cos, 'DiracDelta': dirac_delta, 'EulerGamma': euler_gamma, 'Glaisher': glaisher, 'Sqrt': <function sqrt at 0x2c20f50>, 'Factorial': factorial, 'Khinchin': khinchin, 'Catalan': catalan, '(1+Sqrt[5])/2': golden_ratio, 'Binomial': binomial, 'PolyGamma': psi, 'HeavisideTheta': heaviside, 'KroneckerDelta': kronecker_delta, 'Pi': pi, 'UnitStep': unit_step, 'Sin': sin, 'Gamma': gamma, 'Sign': sgn}
```


This is constructed at runtime and is filled in by the __init__ methods of the functions and constants.


---

Comment by whuss created at 2010-07-20 13:20:03

Replying to [comment:2 flawrence]:
> I've uploaded a patch that has a thorough rewrite of MathematicaElement._sage_() to get the functionality from #3587 while keeping the functionality from before it (lists, complex numbers, numbers in scientific notation...).  I still need to write some documentation for the top of the file (i.e. documentation that makes it into the reference manual) but before I do that and submit this for formal review I'd like wise comments about my approach, e.g. "The way you convert function names is really inefficient and problematic, do it this way...", or "You can efficiently get a list of all sage functions recognised by sage_eval() by ...".
> 
> Also if someone could check the doctests on a 32-bit computer and let me know the result that they get instead of
> [[1.00000000000000, 4], pi, 3.20000000000000*e100, I]
> that would be grand.

On 32-bit Debian I get the same output. There is only one doctest failure:


```
./sage -t  -only-optional=mathematica "devel/sage/sage/interfaces/mathematica.py"
sage -t -only-optional=mathematica "devel/sage/sage/interfaces/mathematica.py"
**********************************************************************
File "./sage-4.4.4/devel/sage/sage/interfaces/mathematica.py", line 281:
    sage: math_bessel_K(2,I)                      # optional - mathematica
Expected:
    0.180489972066962*I - 2.592886175491197
Got:
    -2.59288617549119697816765132253822887 + 0.180489972066962026629620880838378650*I
**********************************************************************

```


But this is probably unrelated to this patch, since also without this patch applied I get
things like:


```
sage: mathematica('N[Pi, 1]')
3.1415926535897932385
sage: mathematica('N[Pi, 10]')
3.1415926535897932385
sage: mathematica('N[Pi, 11]')
3.1415926535897932384626433836
```



---

Comment by flawrence created at 2010-07-21 08:51:34

Replying to [comment:5 mhansen]:
> There is dictionary in place from Mathematica to Sage.
> 
 {{{
sage: sage.symbolic.pynac.symbol_table['mathematica']
{'Log[2]': log2, 'Cos': cos, 'DiracDelta': dirac_delta, 'EulerGamma': euler_gamma, 'Glaisher': glaisher, 'Sqrt': <function sqrt at 0x2c20f50>, 'Factorial': factorial, 'Khinchin': khinchin, 'Catalan': catalan, '(1+Sqrt[5])/2': golden_ratio, 'Binomial': binomial, 'PolyGamma': psi, 'HeavisideTheta': heaviside, 'KroneckerDelta': kronecker_delta, 'Pi': pi, 'UnitStep': unit_step, 'Sin': sin, 'Gamma': gamma, 'Sign': sgn}
}}}

Excellent! I've updated the patch so that it uses that dictionary.  I also added the ability to pass a locals dictionary to _sage_, which complements and/or overrides the symbol_table['mathematica'] dictionary.

The documentation for this function won't be very visible, since it starts with an underscore, so I was contemplating setting up a mathematica-specific .sage function that accepts a locals dictionary and has a copy of this documentation.  In the end I didn't do this because I don't understand the consequences (or why there are separate _sage_ and sage functions at all).  Opinions?

Replying to [comment:6 whuss]:
>On 32-bit Debian I get the same output. There is only one doctest failure:

>But this is probably unrelated to this patch, since also without this patch applied I get things like:

Yes, I'm not sure it's related to the patch either.  For the record I get the correct behaviour with the patch:

```
sage: mathematica('N[Pi, 1]')
3.1
sage: mathematica('N[Pi, 10]')
3.1415926536
sage: mathematica('N[Pi, 11]')
3.14159265359
```



---

Comment by burcin created at 2010-09-08 14:13:16

This looks great! Many thanks for your work Felix.

Here is my review:
 * Can you change the line lengths to be less than 78 characters? Some of us still edit code using the terminal.
 * There should be an empty line after `::` in the documentation. You can also put the `::` sign right after the text, you don't need to make it a separate line.
 * On line 648 of `interfaces/mathematica.py`, you can change the test `if result.find('"') != -1:` to `if '"' in result:`
 * The dictionary merge in the `_sage_()` method might be expensive. I think it's better to do it only if the locals dictionary is not empty. Perhaps `lsymbols = symbol_table['mathematica'].copy(); lsymbols.update(locals)` would be faster.
 * Using `sage_eval()` has lot's of security implications. Can we replace it with `sage.calculus.calculus.SR_parser` or `sage.calculus.calculus.symbolic_expression_from_string()` in this case?

This is definitely an improvement over what we have currently. I'd really like to see it included in the next release.


---

Comment by burcin created at 2010-09-08 14:13:16

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-09-08 14:18:27

One more:
 * The last two hunks applied to `sage/symbolic/constants.py` should be removed. The `conversions` dictionary defines how the current constant is represented in the given system. The values stored in the dictionary should be in MMA syntax.


---

Comment by flawrence created at 2010-11-03 04:45:38

Changing status from needs_work to needs_review.


---

Comment by flawrence created at 2010-11-03 04:45:38

Thanks for your suggestions Burcin.  I implemented all of them, and made some significant further changes:

Now we actually check whether each function exists, before we try to convert the entire expression.  This allows us to check several variations of mma's function names, such as a downcased version, a down_cased version, and the original name.  In order to do this I needed to add an option to sage.calculus.calculus._find_func() whereby it wouldn't automatically create a symbolic function if none were present in Sage.  We now also try the same downcasing tricks for constants.

In order to convert from [CamelCase](CamelCase) to camel_case I used code from [stack overflow](http://stackoverflow.com/questions/1175208/does-the-python-standard-library-have-function-to-convert-camelcase-to-camel-case).  I presume such code is public domain and doesn't require attribution in the docstring.

I also realised that the documentation for _sage_ won't get into Sage's HTML documentation so I added a short section in the module's documentation that reproduces some of the material in the docstring for _sage_().


---

Attachment

What's changed since burcin's review


---

Comment by drkirkby created at 2011-03-09 06:19:32

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2011-03-09 06:19:32

What patch(s)  is supposed to be applied here? `trac_8495-rewrite-_sage_.patch` applied cleanly to sage-4.6.2.rc1, but `diff_with_previous_review.patch` neither applies cleanly on its own, or after applying `trac_8495-rewrite-_sage_.patch`.


---

Comment by flawrence created at 2011-03-09 08:03:47

`trac_8495-rewrite-_sage_.patch` is the patch to apply.  The other patch is for the eye only: it shows what changed since the patch that burcin originally reviewed (which I perhaps foolishly overwrote with the current version of `trac_8495-rewrite-_sage_.patch`)


---

Comment by flawrence created at 2011-03-09 08:03:47

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2011-03-09 10:14:57

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2011-03-09 10:14:57

For me at least, on OpenSolaris with Mathematica 7.0.1, this is a definite improvement, as it reduced the number of failures in `devel/sage/sage/interfaces/mathematica.py` from 17 to 2. 

 == Prior to adding the patch ==

```

<snip out lots of failures>

4 items had failures:
   5 of  84 in __main__.example_0
   4 of   6 in __main__.example_1
   4 of  19 in __main__.example_12
   4 of   6 in __main__.example_2
***Test Failed*** 17 failures.
For whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_mathematica.py
	 [5.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -optional "devel/sage/sage/interfaces/mathematica.py"
Total time for all tests: 5.4 seconds
```


## After adding the patch
After applying the patch, the number of failures is reduced to 2. 


```
sage-4.6.2.rc1$ ./sage -t -optional devel/sage/sage/interfaces/
sage -t -optional "devel/sage/sage/interfaces/mathematica.py"
**********************************************************************
File "/export/home/drkirkby/3/sage-4.6.2.rc1/devel/sage/sage/interfaces/mathematica.py", line 270:
    sage: print n                   # optional - mathematica
Expected:
                  1.5707963267948966192313216916397514420985846996876
Got:
    1.5707963267949
**********************************************************************
File "/export/home/drkirkby/3/sage-4.6.2.rc1/devel/sage/sage/interfaces/mathematica.py", line 311:
    sage: math_bessel_K(2,I)                      # optional - mathematica
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/3/sage-4.6.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/3/sage-4.6.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/3/sage-4.6.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[75]>", line 1, in <module>
        math_bessel_K(Integer(2),I)                      # optional - mathematica###line 311:
    sage: math_bessel_K(2,I)                      # optional - mathematica
      File "<doctest __main__.example_0[74]>", line 2, in math_bessel_K
        return mathematica(nu).BesselK(x).N(Integer(20))
      File "element.pyx", line 617, in sage.structure.element.Element.numerical_approx (sage/structure/element.c:4658)
      File "/export/home/drkirkby/3/sage-4.6.2.rc1/local/lib/python/site-packages/sage/misc/functional.py", line 1265, in numerical_approx
        return sage.rings.complex_field.ComplexField(prec)(x)
      File "/export/home/drkirkby/3/sage-4.6.2.rc1/local/lib/python/site-packages/sage/rings/complex_field.py", line 279, in __call__
        return Parent.__call__(self, x)
      File "parent.pyx", line 915, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6668)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3119)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3022)
      File "/export/home/drkirkby/3/sage-4.6.2.rc1/local/lib/python/site-packages/sage/rings/complex_field.py", line 310, in _element_constructor_
        return complex_number.ComplexNumber(self, x)
      File "complex_number.pyx", line 162, in sage.rings.complex_number.ComplexNumber.__init__ (sage/rings/complex_number.c:3995)
    TypeError: unable to coerce to a ComplexNumber: <class 'sage.interfaces.mathematica.MathematicaElement'>
**********************************************************************
1 items had failures:
   2 of  84 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_mathematica.py
	 [5.2 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -optional "devel/sage/sage/interfaces/mathematica.py"
Total time for all tests: 5.2 seconds
```



## Mathematica session on the sage machine computing Pi/2


```
drkirkby`@`hawk:~$ math
Mathematica 7.0 for Sun Solaris x86 (64-bit)
Copyright 1988-2009 Wolfram Research, Inc.

In[1]:= n=Pi/2

        Pi
Out[1]= --
        2

In[2]:= N[n,50]

Out[2]= 1.5707963267948966192313216916397514420985846996876
```


## Sage session on the same machine computing pi/2 with the Mathematica interface


```
sage: x = mathematica(pi/2)
sage: print x
        Pi
        --
        2
sage: loads(dumps(x)) == x
True
sage: n = x.N(50)  
sage: print n 
1.5707963267949
```



---

Comment by flawrence created at 2011-03-09 10:56:58

OK, that's quite strange.  On my OS X 10.6 64-bit box with Sage 4.6.1, all tests pass.  But the two doctests that failed on your computer don't even call .sage(), which is the main thing that this ticket modifies!

Can you see whether these doctests pass without my patch applied?

Could you evaluate the following lines for me (with the patch applied) and give me the output from your computer:

```
sage: a = mathematica(2).BesselK(I).N(20)
sage: repr(a)
'-2.59288617549119697817 + 0.18048997206696202663*I'
sage: a._sage_repr()
'-2.59288617549119697817 + 0.18048997206696202663*I'
sage: a.sage()
-2.59288617549 + 0.180489972067*I
```



---

Comment by flawrence created at 2011-03-09 11:06:25

BTW, the use of `sage.calculus.calculus.symbolic_expression_from_string` seems to limit the accuracy of results:


```
sage: from sage.calculus.calculus import symbolic_expression_from_string as sefs 
sage: repr(mathematica(pi/2).N(50))
'1.57079632679489661923132169163975144209858469968755'
sage: sefs('1.57079632679489661923132169163975144209858469968755')
1.57079632679
sage: sage_eval('1.57079632679489661923132169163975144209858469968755')
1.5707963267948966192313216916397514420985846996875
```


`sage_eval` gets it right, but Burcin noted above that using it is a security risk.  I guess my suggestion would be to stick with `symbolic_expression_from_string` and open a ticket on improving its accuracy.  Thoughts?


---

Comment by burcin created at 2011-03-09 14:16:43

Replying to [comment:16 flawrence]:
> BTW, the use of `sage.calculus.calculus.symbolic_expression_from_string` seems to limit the accuracy of results:
> 
 {{{
> sage: from sage.calculus.calculus import symbolic_expression_from_string as sefs 
> sage: repr(mathematica(pi/2).N(50))
> '1.57079632679489661923132169163975144209858469968755'
> sage: sefs('1.57079632679489661923132169163975144209858469968755')
> 1.57079632679
> sage: sage_eval('1.57079632679489661923132169163975144209858469968755')
> 1.5707963267948966192313216916397514420985846996875
 }}}
> 
> `sage_eval` gets it right, but Burcin noted above that using it is a security risk.  I guess my suggestion would be to stick with `symbolic_expression_from_string` and open a ticket on improving its accuracy.  Thoughts?

Sounds good to me. Can you open that ticket? :)


---

Comment by drkirkby created at 2011-03-09 15:56:55

Replying to [comment:15 flawrence]:
> OK, that's quite strange.  On my OS X 10.6 64-bit box with Sage 4.6.1, all tests pass.  But the two doctests that failed on your computer don't even call .sage(), which is the main thing that this ticket modifies!

Em, it is strange. 

I'm a bit tied up now, but will repeat later. 

I'm actually willing to give this a positive review, on the basis that it fixes a very large number of the problems, and no new bugs are introduced. But I'll run the tests later and see what can be done. 

Dave


---

Comment by flawrence created at 2011-03-10 00:58:37

Replying to [comment:17 burcin]:
> Replying to [comment:16 flawrence]:
> > `sage_eval` gets it right, but Burcin noted above that using it is a security risk.  I guess my suggestion would be to stick with `symbolic_expression_from_string` and open a ticket on improving its accuracy.  Thoughts?
> 
> Sounds good to me. Can you open that ticket? :)
Done: #10898


---

Comment by flawrence created at 2011-03-19 12:03:52

Hi Dave,

Have you had a chance to investigate what was happening on Solaris?

Cheers,
Felix


---

Comment by flawrence created at 2011-03-19 12:03:52

Changing status from needs_work to needs_info.


---

Comment by drkirkby created at 2011-03-19 19:11:29

Replying to [comment:20 flawrence]:
> Hi Dave,
> 
> Have you had a chance to investigate what was happening on Solaris?
> 
> Cheers,
> Felix

Can you clarify the exact commands you want tested with and without the patch?


---

Comment by flawrence created at 2011-03-20 00:06:54

Changing status from needs_info to needs_review.


---

Comment by flawrence created at 2011-03-20 00:06:54

ARGH! I upgraded to 4.6.2 (from 4.6.1), ran the tests and get the same errors as Dave.

#9032 modified Sage's .n(), and added (in two files)

```
n = numerical_approx
N = n
```


This means that Mathematica's `N[]` is no longer being called - instead Sage's `numerical_approx()` is being called, and it can't handle certain mma objects.  Furthermore the argument taken by `numerical_approx` is the number of bits (I think?) whereas `N[50]` gives 50 sig figs.

I think that the way to fix this is by adjusting precedences so that on mathematica objects, mathematica functions take priority.  I also think that fixing this is beyond the scope of this ticket (which was a rewrite of `._sage_`).  I have created a new ticket regarding this issue: #10968


---

Comment by drkirkby created at 2011-03-20 01:29:31

Replying to [comment:22 flawrence]:
> ARGH! I upgraded to 4.6.2 (from 4.6.1), ran the tests and get the same errors as Dave.

I'm glad I;m not going mad. 

Since the changes reduces the number of failures from 17 to 2, I believe this should be merged, so positive review. The remaining issues can be sorted out on #10968


---

Comment by drkirkby created at 2011-03-20 01:29:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-23 13:54:44

Problems while building the documentation:

```
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/mathematica.py:docstring of sage.interfaces.mathematica:282: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/mathematica.py:docstring of sage.interfaces.mathematica:284: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/local/lib/python2.6/site-packages/sage/interfaces/mathematica.py:docstring of sage.interfaces.mathematica:277: (ERROR/3) Unexpected indentation.
```



---

Comment by jdemeyer created at 2011-03-23 13:54:44

Changing status from positive_review to needs_work.


---

Attachment


---

Attachment

I made some minor formatting changes to the documentation to avoid the above problems.  The documentation now builds without errors and looks OK on my machine.

I forgot to tick the 'replace attachment' box; please disregard the older (non ".2.") patch.


---

Comment by flawrence created at 2011-03-23 14:27:23

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2011-03-23 17:22:15

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2011-03-23 17:22:15

Yes, the documentation builds ok for me. That was something I did not check before I must admit. 


Dave


---

Comment by jdemeyer created at 2011-03-25 12:31:01

Resolution: fixed
