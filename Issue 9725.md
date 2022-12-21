# Issue 9725: German Translation of the Tutorial

Issue created by migration from Trac.

Original creator: phil

Original creation time: 2010-08-11 16:45:47

Assignee: mvngu

CC:  schilly

Keywords: Documentation Tutorial German

Create a German translation of the Sage Tutorial.


---

Attachment


---

Attachment


---

Attachment


---

Comment by phil created at 2010-08-12 01:12:47

Changing assignee from mvngu to phil.


---

Comment by mardaus created at 2010-08-19 19:16:05

Hallo Phil,
ich hab mal in die erste Datei geschaut, und hätte ein paar typos und Formulierungen anzumerken. Können wir irgendwie zusammen daran arbeiten, ohne das wir dauernd neue Dateien hochladen müssen? Ich denke da an SVN oder dergleichen.
Michael


---

Comment by phil created at 2010-08-20 13:02:32

Changing status from new to needs_work.


---

Comment by phil created at 2010-08-20 13:02:32

If someone would like to help us proofreading, I will keep a current version of the translation published at:
http://wwwcip.informatik.uni-erlangen.de/~snphschn/sage/doc/output/html/de/tutorial/index.html

The current rst Files can be found at:
http://wwwcip.informatik.uni-erlangen.de/~snphschn/sage/doc/de/tutorial/

Philipp


---

Comment by mardaus created at 2010-08-20 15:30:16

FYI: I'm translating interactive_shell.rst at the moment. 

I will send you my file once I'm done translating it, and I will send you a diff or updated/commented version of your files after I proofread them via email.

Michael


---

Attachment

Ein paar Hinweise/Typos:

langfristige >>Zeile<< von Sage -> Ich denke ihr meint >>Ziele<< =)

geführte Tour -> Ich würde guided mit "begleitend", statt mit "geführt" übersetzen macht im Deutschen mehr Sinn...

Ich glaube statt "Hilfe erhalten", würde ich nur "Hilfe" schreiben 

Euler’s Method for Systems of Differential Equations¶ -> warum wurde das nicht übersetzt?

Das sind nur ein paar Sachen die mir beim schnellen durchlesen aufgefallen sind. Aber ansich eine gute Übersetzung. bravo!

greez 
maldun


---

Comment by phil created at 2010-08-23 22:22:22

Thanks for your corrections, I changed everything.
If you would like to translate a section yourself, you are welcome.

Also, I made the pdf version available at
http://wwwcip.informatik.uni-erlangen.de/~snphschn/sage/doc/output/pdf/de/tutorial/SageTutorial.pdf

Phil


---

Attachment


---

Attachment


---

Comment by phil created at 2010-10-04 00:19:17

Changing status from needs_work to needs_review.


---

Attachment

Proofread version of Phil's parts


---

Attachment


---

Comment by mardaus created at 2011-02-12 12:51:28

I found an article in the german computer magazine c't today about sage (c't 5/2011 p. 69) where it says:
"Das Gratis-Paket Sage bringt die wichtigesten Open-Source-Mathematikprogramme schon mit - 'Batteries included', heißt es in der ausführlichen, aber komplett englischen Dokumentation. ..."
(The free package Sage brings the most important open-source math-programs batteries included, as it says in the detailed, but completely english written documentation.)

Maybe we should use that as a reminder that we already have a german version of the tut here.


---

Comment by vbraun created at 2011-05-11 13:58:18

Typo: Whitenys Regenschirm -> Whitneys Regenschirm

Sieht gut aus! Ich gebe dem ticket positive review bis auf den tippfehler. Wenn Du den korrigierst kannst Du das ticket auf "positive review" setzen.


---

Attachment


---

Comment by phil created at 2011-05-11 18:28:12

Hello Volker,

I corrected the typo and made other little changes to make the doctests pass.
Thanks for reviewing! 

Philipp


---

Comment by vbraun created at 2011-05-11 18:44:42

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-17 15:49:40

Resolution: fixed


---

Comment by fbissey created at 2011-05-24 04:52:29

I don't know if it is an interaction with another ticket but I just did a test run of 4.7.1.alpha1 and got

```
sage -t -long -force_lib "devel/sage-main/doc/de/tutorial/programming.rst"
**********************************************************************
File "/Users/frb15/Desktop/sage-4.7.1.alpha1/devel/sage-main/doc/de/tutorial/programming.rst", line 425:
    sage: type(v)
Expected:
    <class 'sage.structure.sequence.Sequence'>
Got:
    <class 'sage.structure.sequence.Sequence_generic'>
**********************************************************************
File "/Users/frb15/Desktop/sage-4.7.1.alpha1/devel/sage-main/doc/de/tutorial/programming.rst", line 463:
    sage: type(B)
Expected:
    <class 'sage.structure.sequence.Sequence'>
Got:
    <class 'sage.structure.sequence.Sequence_generic'>
**********************************************************************
2 items had failures:
```



---

Comment by jdemeyer created at 2011-05-24 08:35:29

Replying to [comment:15 fbissey]:
> I don't know if it is an interaction with another ticket but I just did a test run of 4.7.1.alpha1 and got
> {{{
> sage -t -long -force_lib "devel/sage-main/doc/de/tutorial/programming.rst"
> }}}

Which command did you type to run this test?  When I ran "make ptest" or "make ptestlong", this test simply was not run, so that's where the bug is.


---

Comment by jdemeyer created at 2011-05-24 08:35:29

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-05-24 08:35:29

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-05-24 08:43:28

Note also that the patchbot reports

```
sage -t  -force_lib sage/misc/sagedoc.py
**********************************************************************
File "/levi/scratch/robertwb/buildbot/sage-4.7.rc1/devel/sage-9725/sage/misc/sagedoc.py", line 489:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /levi/scratch/robertwb/buildbot/sage-4.7.rc1/devel/sage/doc/output/html/de/tutorial
    <BLANKLINE>
    You can build this with 'sage -docbuild de/tutorial html'.
    True
**********************************************************************
```

and that the "doc/de" directory is not tested.


---

Comment by jdemeyer created at 2011-05-24 08:43:28

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-05-24 08:43:35

Changing status from needs_review to needs_work.


---

Comment by phil created at 2011-05-24 11:50:46

Hi,
in Sage 4.6.2 all tests passed. (I tested it manually.)
I guess that the type of this sequence has changed in sage 4.7.
I will fix this when sage 4.7 is released.

What i don't know is how to change sage to build and test "de" documentation automatically.


---

Comment by jdemeyer created at 2011-05-24 12:25:50

Apply to SAGE_ROOT repository


---

Attachment


---

Comment by fbissey created at 2011-05-24 19:49:21

Replying to [comment:16 jdemeyer]:
> Replying to [comment:15 fbissey]:
> > I don't know if it is an interaction with another ticket but I just did a test run of 4.7.1.alpha1 and got
> > {{{
> > sage -t -long -force_lib "devel/sage-main/doc/de/tutorial/programming.rst"
> > }}}
> 
> Which command did you type to run this test?  When I ran "make ptest" or "make ptestlong", this test simply was not run, so that's where the bug is.

I just did a build of sage with make and then ran "./sage -tp 3 -long -sagenb devel/" I was checking that gsl-1.15 (#11357) was OK with 4.7.1.alpha1.


---

Comment by fbissey created at 2011-05-25 00:53:52

I don't know why I didn't mention it in my original post but I also have a time out in

```
sage -t -long  -force_lib devel/sage-main/doc/de/tutorial/interfaces.rst
```

Using -verbose it appears to get stuck at

```
Trying:
    maxima.plot3d ("2^(-u^2 + v^2)", "[u, -3, 3]", "[v, -2, 2]",   '[plot_format, openmath]') # nicht getestet###line 323:_sage_    >>> maxima.plot3d ("2^(-u^2 + v^2)", "[u, -3, 3]", "[v, -2, 2]",   '[plot_format, openmath]') # nicht getestet
Expecting nothing
```

I am guessing #7377 is to blame for that one.


---

Comment by vbraun created at 2011-05-25 01:23:00

The magic `# not tested` comment at the end of the doctest means Sage isn't supposed to use the command as a doctest. Its part of the Sage doctest syntax and you shouldn't translate it.


---

Comment by phil created at 2011-05-26 21:14:06

I created a patch to fix the doctest problems.

However, when I try to apply the 9725_TESTDIRS.patch
I get the following error


```
sage: hg_sage.apply("../../9725_TESTDIRS.patch")
cd "/home/phil/Applications/sage-4.7.rc4/devel/sage" && hg status
cd "/home/phil/Applications/sage-4.7.rc4/devel/sage" && hg status
cd "/home/phil/Applications/sage-4.7.rc4/devel/sage" && hg import   "/home/phil/Applications/sage-4.7.rc4/9725_TESTDIRS.patch"
applying /home/phil/Applications/sage-4.7.rc4/9725_TESTDIRS.patch
unable to find 'Makefile' for patching
1 out of 1 hunks FAILED -- saving rejects to file Makefile.rej
abort: patch failed to apply
```



---

Comment by phil created at 2011-05-26 21:15:02

fix the doctest problems


---

Comment by phil created at 2011-05-26 21:16:38

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by phil created at 2011-05-26 23:19:27

Changing status from needs_review to needs_work.


---

Comment by phil created at 2011-05-26 23:23:48

How is it possible to patch the Makefile?

I edited the Makefile to add the directory of the german tutorial to the TESTDIR.
When I tried to commit the change I got:


```
sage: hg_sage.commit()
cd "/home/phil/Applications/sage-4.7.rc4/devel/sage" && hg diff  | less
cd "/home/phil/Applications/sage-4.7.rc4/devel/sage" && hg commit  
nothing changed
```



---

Comment by jdemeyer created at 2011-05-27 07:15:14

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-05-27 07:15:14

Replying to [comment:28 phil]:
> How is it possible to patch the Makefile?
You need to use `hg_root` instead of `hg_sage`:

```
sage: hg_root.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9725/9725_TESTDIRS.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9725/9725_TESTDIRS.patch
Loading: [.]
cd "/usr/local/src/sage-4.7" && hg status
cd "/usr/local/src/sage-4.7" && hg status
cd "/usr/local/src/sage-4.7" && hg import   "/home/jdemeyer/.sage/temp/arcanis/5225/tmp_0.patch"
applying /home/jdemeyer/.sage/temp/arcanis/5225/tmp_0.patch
```



---

Comment by phil created at 2011-05-27 09:31:24

Ok thanks, 

I also ran make ptestlong after adding the directory of the german tutorial the TESTDIRS variable and got


```
phil`@`phil-lt:~/Applications/sage-4.7.rc4$ make ptestlong
...
All tests passed!
Total time for all tests: 3914.3 seconds
```



---

Comment by jdemeyer created at 2011-05-31 08:25:58

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-05-31 08:25:58


```
sage -t  -force_lib devel/sage/doc/de/tutorial/interfaces.rst
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/devel/sage-main/doc/de/tutorial/interfaces.rst", line 163:
    sage: G.IdGroup()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[5]>", line 1, in <module>
        G.IdGroup()###line 163:
    sage: G.IdGroup()
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/lib/python/site-packages/sage/interfaces/interface.py", line 588, in
 __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/lib/python/site-packages/sage/interfaces/gap.py", line 646, in funct
ion_call
        ['%s=%s'%(key,value.name()) for key, value in kwds.items()])))
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/lib/python/site-packages/sage/interfaces/gap.py", line 375, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1026, in e
val
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha2/local/lib/python/site-packages/sage/interfaces/gap.py", line 519, in _eval
_line
        raise RuntimeError, message
    RuntimeError: Gap produced error output
    Error, the Small Groups identification is required but not installed

       executing IdGroup($sage1);
**********************************************************************
```



---

Comment by phil created at 2011-05-31 13:12:31

Well, of course you can only get the required output if you have the GAP group database package installed...


---

Attachment


---

Comment by phil created at 2011-05-31 13:31:36

Changing status from needs_work to needs_review.


---

Comment by phil created at 2011-05-31 13:35:15

I guess the test which depends on the optional package requires a magic string too.
It should work after applying patch C.


---

Comment by vbraun created at 2011-05-31 15:09:41

Works for me on Sage-4.7.1.alpha1


---

Comment by vbraun created at 2011-05-31 15:09:41

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-01 07:10:43

Resolution: fixed


---

Comment by kcrisman created at 2013-01-29 20:21:13

FYI - There is a tiny typo a beginner could fix, wanted to pass it on here though I don't expect anyone here to address it, given that #8660 or #8698 would be more useful...  Anyway, #14035.
