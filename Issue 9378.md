# Issue 9378: Russian translation of the Sage tutorial

Issue created by migration from https://trac.sagemath.org/ticket/9378

Original creator: mvngu

Original creation time: 2010-06-29 18:36:33

Assignee: mvngu

CC:  freetonik@gmail.com schilly kcrisman novoselt

As the subject says. Get a Russian translation of the [Sage tutorial](http://www.sagemath.org/doc/tutorial/) into the Sage standard documentation.


---

Attachment


---

Comment by mvngu created at 2010-06-29 18:41:15

The attachment [Sage-russian-tutorial-rst.tar.bz2](http://trac.sagemath.org/sage_trac/attachment/ticket/9378/Sage-russian-tutorial-rst.tar.bz2) contains a Russian translation of the Sage tutorial. Thanks to Rakhim Davletkaliyev and Vladimir <v_2e`@`ukr.net> for the translation. We need to create a patch out of the translated .rst files.


---

Comment by mvngu created at 2010-06-29 18:41:15

Changing status from new to needs_work.


---

Comment by schilly created at 2010-06-29 18:49:05

Note from Rakhim: Authors of translation are Temirlan Kumargazhin and Rakhim Davletkaliyev, Vladimir was more an editor.


---

Comment by schilly created at 2010-07-20 14:18:01

Changing status from needs_work to needs_review.


---

Comment by schilly created at 2010-07-20 14:18:01

I've created a patch that includes the modifications to Sage 4.5 to include the russian tutorial. HTML builds fine, to get PDF working I had to install the cyrillic lang package for my livetex, too. It stopped once during latex compilation but worked fine when I just hit return.


---

Comment by schilly created at 2010-07-20 14:18:46

4.5 patch to include the russian translation of the tutorial


---

Attachment


---

Attachment

Rebased to apply on 4.7.1.alpha2


---

Comment by kcrisman created at 2011-06-14 04:50:31

The html looks nice, at least.  A few comments.
 * `tour_assignment` has some comments behind `#` in English still.  It should be pretty easy to make them be Russian, like `means exponent` becoming `значит` exponent (all the translation tools online I am suspicious of, but don't have any Russian math books on me)  
 * in the linear algebra one there is also `# checking our answer...` which could easily be translated
 * on `tour_algebra` there is an extra comma after the system of springs at `, где  - это масса` - extra because the comma is in the system that is LaTeXed.
 * on the plotting page is `Лист Мебиуса:` really a cross-cap?  This seems somewhat misleading as one doesn't get the usual representation of the Moebius strip, which a reader would expect.  
 * The index is empty.  To be fair, the English index has exactly one entry. 
 * In sagetex.html, "The text below will have several errors about unknown control sequences if you are viewing this in the “live” help. Use the static version to see the correct text." should be Russian, I think.  Especially since the warning is a `Предупреждение`!

But these are all very minor.  This looks good, and the parts of it I feel qualified to review the content of seem natural as well, not necessarily woodenly translated.  

Andrey, if you just rebased, then you should be able to just finish the review.  If you can at least fix a couple of the remaining English things that shouldn't be, and the crosscap/Moebius strip thing, that would be nice.


---

Comment by novoselt created at 2011-06-14 05:15:36

I want to make some changes to the "short description of Sage" and will also look over issues that you have raised. I wouldn't be too concerned about empty back-matter like index and it can be left to future tickets. Once the first version is in Sage, I hope it will be easier to get some more people to start working on improvements...

Лист Мёбиуса does seem to be a correct translation for the cross-cap, but I will add a clarification. The alternative seems to be скрещеный колпак:
http://lingvo.yandex.ru/cross-cap/%D1%81%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE/


---

Comment by novoselt created at 2011-06-14 05:52:41

Changing keywords from "" to "sd31".


---

Comment by novoselt created at 2011-06-14 05:52:41

Here are my first corrections, there are also some obvious typos in section names which I am going to fix.


---

Comment by novoselt created at 2011-06-14 05:52:41

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2011-06-14 07:31:05

I'll go through all examples to translate comments, here is an updated version of the patch. I have removed the makefile as it is not present in the French version and seems to be unnecessary, correct me if I am wrong.


---

Comment by novoselt created at 2011-06-14 22:10:57

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2011-06-14 22:10:57

I have removed index. In PDF there are two Bibliographies, as well as in English variant. In Russian these two copies even have different names... But it seems that it is a bug in Sphinx, since HTML looks fine and in the source file there is only one bibliography line (if it is removed, both copies are gone). PDF also does not use monospaced font for examples, but again it looks like Sphinx bug as all mark-up seems to be OK and is obviously looking fine for HTML.

There are some typos/mistakes in the translation which I didn't fix as I didn't read carefully through the whole text. Ideally someone should go through the whole tutorial without looking at the English original and rewrite everything that "does not quite sound Russian" but overall it is pretty good and usable, those who plan to use Sage heavily will be forced to read detailed English documentation anyway.

Karl, if you think my changes are OK, let's switch it to positive review and merge.


---

Comment by kcrisman created at 2011-06-14 22:42:09

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-06-14 22:42:09

Replying to [comment:10 novoselt]:
> I have removed index. In PDF there are two Bibliographies, as well as in English variant. In Russian these two copies even have different names... But it seems that it is a bug in Sphinx, since HTML looks fine and in the source file there is only one bibliography line (if it is removed, both copies are gone). PDF also does not use monospaced font for examples, but again it looks like Sphinx bug as all mark-up seems to be OK and is obviously looking fine for HTML.
> 
> There are some typos/mistakes in the translation which I didn't fix as I didn't read carefully through the whole text. Ideally someone should go through the whole tutorial without looking at the English original and rewrite everything that "does not quite sound Russian" but overall it is pretty good and usable, those who plan to use Sage heavily will be forced to read detailed English documentation anyway.

I agree.  There is not the manpower to do 'real' translations at this point, but as long as it doesn't look auto-generated and is correct enough this is good.  

> Karl, if you think my changes are OK, let's switch it to positive review and merge.

Okay.  Here are a few comments.  The last one will require "needs work", I am pretty sure, but is easy to fix in your patch, I think.

 * One thing

```

-    sage: cputime(t)                       # somewhat random output
+    sage: cputime(t)                       # random output
```

   Was that supposed to turn into Russian?  I think not, based on other stuff, but just checking.

 * A few places you did

```

-Это учебное пособие — лучший способ познакомиться с Sage за несколько 
-часов. Вы можете читать HTML или PDF версию документа, или напрямую из 
-Sage notebook (нажмите Help, потом Tutorial для интерактивной работы по 
-пособию внутри Sage).
 
```

   but didn't replace it. Fine - but then in `introduction.rst` you did replace it.  I assume this was intentional, so it was only in one place, but just making sure.

 * I like the changes you made, too.  Very nice in the commented things, especially.  Нижеследующий is my favorite new word, I will have to find a way to use this soon back home.

 * Here is one thing that should be fixed - but I think one just has to add a few `=` symbols.

```
reading sources... [100%] tour_rings                                            
/Users/karl-dietercrisman/Downloads/sage-4.7.1.alpha2/devel/sage/doc/ru/tutorial/interactive_shell.rst:155: (WARNING/2) Title underline too short.
```

 * Here is something else that needs work.

```

sage -t  "devel/sage/doc/ru/tutorial/introduction.rst"      

    sage: latex(k)
Expected:
    \frac{1}{I \, \sqrt{3} + \frac{5}{9} \, \sqrt{73} + \frac{3}{4}}
Got:
    \frac{1}{i \, \sqrt{3} + \frac{5}{9} \, \sqrt{73} + \frac{3}{4}}

sage -t  "devel/sage/doc/ru/tutorial/programming.rst"       
**********************************************************************
File "/Users/karl-dietercrisman/Downloads/sage-4.7.1.alpha2/devel/sage/doc/ru/tutorial/programming.rst", line 393:
    sage: type(v)
Expected:
    <class 'sage.structure.sequence.Sequence'>
Got:
    <class 'sage.structure.sequence.Sequence_generic'>
**********************************************************************
File "/Users/karl-dietercrisman/Downloads/sage-4.7.1.alpha2/devel/sage/doc/ru/tutorial/programming.rst", line 430:
    sage: type(B)
Expected:
    <class 'sage.structure.sequence.Sequence'>
Got:
    <class 'sage.structure.sequence.Sequence_generic'>
**********************************************************************
File "/Users/karl-dietercrisman/Downloads/sage-4.7.1.alpha2/devel/sage/doc/ru/tutorial/programming.rst", line 343:
    sage: type(L[12])
Expected:
    <class 'sage.structure.factorization.Factorization'>
Got:
    <class 'sage.structure.factorization_integer.IntegerFactorization'>
**********************************************************************
   There are a couple other errors as well in testing the tutorial.  Probably because it's based on an old version of Sage.  They are all probably easy to fix, too.  

Sorry :( but almost there :)


---

Comment by novoselt created at 2011-06-14 22:56:36

Things like "random output" and "long time" were supposed to stay in English, as Volker has pointed out to me, otherwise we will get doctest errors. The reason why I have changed some of them is that in Russian version they are just service tags and so it is better if they are as short as possible. Also, I have studies English in Russia for over 10 years, but I would not quite understand the meaning the meaning of "random-ish" and I doubt this word is in any English-Russian dictionary.

The paragraph which I have removed completely in one place makes sense mostly for the PDF version where it is repeated almost immediately and it looks a bit weird, especially since I have expanded it compared to the English variant. So I think it is better this way.

Thanks for catching errors, I didn't notice the docbuild warning (probably the file didn't change at the time I was looking for them). And I forgot to doctest it completely! Will post fixes shortly.


---

Comment by novoselt created at 2011-06-14 23:05:30

Adjustments and comment translation


---

Attachment


---

Comment by novoselt created at 2011-06-14 23:06:29

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-06-15 17:42:39


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 182.0 seconds
```


Looks good, great work.  С удовольствием!


---

Comment by kcrisman created at 2011-06-15 17:42:39

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-15 20:22:03

Add devel/sage/doc/ru to TESTDIRS


---

Attachment


---

Comment by jdemeyer created at 2011-06-16 11:54:09

Resolution: fixed
