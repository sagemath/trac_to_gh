# Issue 8660: German translation of installation guide

Issue created by migration from https://trac.sagemath.org/ticket/8660

Original creator: mvngu

Original creation time: 2010-04-08 15:12:54

Assignee: mvngu

CC:  bblochl@arcor.de leif schilly minz hedtke

A German translation of the Sage installation guide is complete. See [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/cc2232f6cba3386f) for background information. What needs to be done now is to use Sphinx for the markup so that the translated guide could be included in the Sage standard documentation.


---

Attachment

ODF document of the German translation


---

Comment by mvngu created at 2010-04-08 15:13:47

PDF version of the previous document


---

Attachment


---

Attachment

HTML code for Unicode characters


---

Comment by leif created at 2010-04-11 04:41:51

Sorry to say, but this translation *really* needs (more) work.

There are still lots of typos, inconsistently chosen terms and style, and some errors regarding the content (some information seems not to be up-to-date in the original either, haven't checked that yet). IMHO the translation is too much one-to-one in many places. (I would also add some things, perhaps leaving out other issues, since German documentation is rare if not non-existent anyway.)

The question is which format to edit: convert to ReST and rework that version or change the ODT source?

Bernhard, were you willing to edit/review/maintain a ReST version?

I'd personally prefer typesetting it in LaTeX... ;-)
(and perhaps restructuring the text _before_ it gets converted to .rst)

Unfortunately I currently don't feel having the time to maintain the "whole thing", otherwise I would some time ago have started providing a few translated documents. And -- I'm unfortunately _not_ a mathematician; so I can only offer sporadic and limited help, not continuous collaboration, at least at the moment.

Pardon me,
hope my first impression doesn't embarrass you too much,
and nevertheless thanks for your initiative,

-Leif


---

Comment by mvngu created at 2010-04-13 02:40:05

based on Sage 4.3.5


---

Attachment

I have attached a patch to integrate the German translation into the Sage documentation. The patch needs to be reviewed by someone other than Bernhard and me. My knowledge of the German language is next to nothing. I relied on Google Translate while converting the document from ODT to Sphinx.


---

Comment by mvngu created at 2010-04-13 02:44:04

Changing status from new to needs_review.


---

Comment by schilly created at 2010-04-13 20:25:44

ok, i looked at the rest text and yes, i could proofread it, but i think first of all we have to settle what kind of translation we want. there are some german words i'm not happy with. they sound very artificial and it is from my point of view absolutely ok to keep english words (or near-english words) because more users will know what they mean than a "forced" translation that just sounds funny.

my background is that i did english to german translations for openoffice many years ago and there we had the same problems. i also know that others view that differently, especially from upper and eastern germany. so, we should settle this first.


---

Comment by schilly created at 2010-04-13 20:25:44

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-04-13 20:49:37

First of all, could we _please_ change its title to a _German_ term, which is e.g. _Installationsanleitung_...

There are other flaws like _Polynomiale_ instead of _Polynome_, the meaning of (symbolic) links is "inverted", and much more I don't remember at the moment.

I strongly suggest splitting off a ticket to discuss the contents (or style) _in German_.

-Leif


---

Comment by SimonKing created at 2010-04-17 13:07:13

Can someone please tell me what commands are needed to produce the German documentation (in html or pdf), so that I can do some proof reading?

And how should corrections be suggested/made? Should one state one's suggestions here in trac comments, so that Bernhard can take them into account? Should one post a patch that builds on top of the original patch? Or should one create a "big" patch that could replace the original patch?

Cheers,
Simon


---

Comment by mvngu created at 2010-04-17 13:33:33

Replying to [comment:9 SimonKing]:
> Can someone please tell me what commands are needed to produce the German documentation (in html or pdf), so that I can do some proof reading?

Apply the patch [trac_8660-installation-de.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8660/trac_8660-installation-de.patch), then issue the following command to build the HTML version:


```
./sage -docbuild de/installation html
```


Or do the following to get the PDF version:


```
./sage -docbuild de/installation pdf
```





> Should one post a patch that builds on top of the original patch?

Yes, something like that. In that case, you would be posting a reviewer patch.


---

Comment by SimonKing created at 2010-04-17 18:25:13

Replying to [comment:3 leif]:
> Sorry to say, but this translation *really* needs (more) work.
> 
> There are still lots of typos, inconsistently chosen terms and style, ...

I agree. I read introduction.rst (which describes the components of Sage) and found several mathematical notions that are different in German. Just two examples: 
 * "toric varieties" are not "Torus-Varianten" but "torische Varietäten".
 * "ghmm: Modellbibliothek für versteckte Markov-Prozesse": ghmm is in fact a library that is concerned with hidden Markov models (so, the word "model" refers to Markov and not to the library). 

I hope that Monday I can provide a patch on top of trac_8660-installation-de.patch.

Best regards,
Simon


---

Attachment

Reviewer patch, to apply after ``trac_8660-installation-de.patch``


---

Comment by SimonKing created at 2010-04-18 12:14:07

Earlier than I thought, I can provide a reviewer patch trac_8660-installation-de_reviewer.patch, which is to be applied after trac_8660-installation-de.patch

The changes also concern the parts that are the topic of ticket #8698, so, perhaps the two tickets can be united?

I inserted a lot more back ticks for marking code snippets, as in the English text. I slightly updated some version numbers (for example when the Singular or Gap consoles are demonstrated: Singular is now version 3-1-0, not 3-0-1). And I changed several notions to what I believe is correct in German. However, I am not sure in all cases. 

So, I feel it would be necessary for more native speakers to have a look on it!

Where should my name be inserted: Author(s)? Reviewer(s)?

Some general questions, that also regard the English text: What is the status of Sage on Mac OS-X? I recently had no problems to build Sage in either 32 or 64 bit mode on bsd.math, so, perhaps the problem reports are outdated? And what about gcc versions?

Best regards,

Simon


---

Comment by SimonKing created at 2010-04-18 12:14:07

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-04-18 12:14:07

Changing keywords from "" to "installation guide, German".


---

Comment by SimonKing created at 2010-04-18 12:18:31

Sorry, regarding #8698, I was mistaken: I thought that the text of #8698 is a subset of the text we are discussing here, but in fact they are separated. So, the both tickets should be kept for now.


---

Comment by leif created at 2010-04-19 05:13:49

Replying to [comment:12 SimonKing]:
> Earlier than I thought, I can provide a reviewer patch trac_8660-installation-de_reviewer.patch, which is to be applied after trac_8660-installation-de.patch

Habe den Patch lediglich ueberflogen, sieht aber schon ganz gut aus.

Einige Ungereimtheiten und Fehler sind allerdings noch drin, und wie Harald (schilly) bemerkte, sollte man vielleicht die Uebersetzung einiger Begriffe abklaeren.

(But don't ask for a patch now.)

-Leif


---

Comment by SimonKing created at 2010-04-19 07:48:38

Replying to [comment:14 leif]:
> Einige Ungereimtheiten und Fehler sind allerdings noch drin, und wie Harald (schilly) bemerkte, sollte man vielleicht die Uebersetzung einiger Begriffe abklaeren.

If you can't do a patch for now: Can you make a list of these notions and flaws?


---

Comment by leif created at 2010-04-21 01:15:34

Replying to [comment:15 SimonKing]:
> If you can't do a patch for now: Can you make a list of these notions and flaws?

Sorry, both alternatives require some time (as I'd like to change a lot of things), so be patient...

You're currently focussing on the translation of the tutorial anyway?

-Leif


---

Comment by SimonKing created at 2010-04-21 07:17:52

Replying to [comment:16 leif]:
> ... 
> You're currently focussing on the translation of the tutorial anyway?

Yes.


---

Comment by hedtke created at 2011-07-17 10:10:38

I was not able to apply the patch to my sage 4.7 on my 64bit mac:


```
sage: hg_sage.apply("/Users/hedtke/trac_8660-installation-de.patch")

WARNING:
Make sure to create a ~/.hgrc file:
----------------------------------------------------------------------
[ui]
username = William Stein <wstein@gmail.com>
----------------------------------------------------------------------


cd "/Users/hedtke/sage/devel/sage" && hg status

WARNING:
Make sure to create a ~/.hgrc file:
----------------------------------------------------------------------
[ui]
username = William Stein <wstein@gmail.com>
----------------------------------------------------------------------


cd "/Users/hedtke/sage/devel/sage" && hg status

WARNING:
Make sure to create a ~/.hgrc file:
----------------------------------------------------------------------
[ui]
username = William Stein <wstein@gmail.com>
----------------------------------------------------------------------


cd "/Users/hedtke/sage/devel/sage" && hg import   "/Users/hedtke/trac_8660-installation-de.patch"
applying /Users/hedtke/trac_8660-installation-de.patch
patching file doc/common/builder.py
Hunk #1 FAILED at 13
1 out of 1 hunks FAILED -- saving rejects to file doc/common/builder.py.rej
abort: patch failed to apply
```



---

Comment by hedtke created at 2011-07-17 10:10:38

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2011-07-17 14:49:30

> I was not able to apply the patch to my sage 4.7 on my 64bit mac:

I think that the patch to the file 'builder.py' is no longer necessary, so that part of the patch file can be deleted.


---

Comment by hedtke created at 2011-07-17 18:00:34

Ok. After deletion of the "builder.py" part of the patch I am able to apply both patches. But the docbuild failed:


```
noname:graphs hedtke$ sage -docbuild de/installation pdf
Detected SAGE64 flag
Building Sage on OS X in 64-bit mode
'de/installation' is not a recognized document. Type 'sage -docbuild -D' for a list
of documents, or 'sage -docbuild --help' for more help.
```


What I did:
 1. build a sage clone
 1. hg_sage.apply() with the modified first patch and the original second patch
 1. sage -b
 1. sage -docbuild de/installation pdf

but the files are there:


```
noname:installation hedtke$ pwd
/Users/hedtke/sage/devel/sage-test/doc/de/installation
noname:installation hedtke$ ls
binary.rst		icon.rst		quick-guide.rst
conf.py			index.rst		sagetex.rst
documentation.rst	introduction.rst	source.rst
```



---

Comment by jhpalmieri created at 2011-07-17 18:49:15

I think I see the problem: I was sort of wrong about the patch to builder.py not being necessary.  It's not necessary in the prelease versions of Sage 4.7.1, but a variant of it is necessary in Sage 4.7.  In particular, you need to apply this part of the patch from #9725:

```diff
diff -r 361a4ad7d52c -r aad4d26889c1 doc/common/build_options.py
--- a/doc/common/build_options.py	Fri Feb 25 18:56:01 2011 +0000
+++ b/doc/common/build_options.py	Wed May 11 20:19:52 2011 +0200
@@ -4,7 +4,7 @@
 
 import os
 SAGE_DOC = os.environ['SAGE_DOC']
-LANGUAGES = ['en', 'fr']
+LANGUAGES = ['de', 'en', 'fr']
 SPHINXOPTS = ""
 PAPER = ""
 OMIT = ["introspect"]  # docs/dirs to omit when listing and building 'all'
```

You can certainly just do this by hand if you want.  (Or if you want, you can apply all of the patches from #9725 in order to build the German tutorial.)


---

Comment by hedtke created at 2011-07-17 18:50:46

Thank you.


---

Comment by hedtke created at 2011-07-17 20:05:49

Changing assignee from mvngu to hedtke.


---

Comment by hedtke created at 2011-07-17 20:05:49

I work on a patched patch and I will update the german translation (it is based on a very old version of the english version).


---

Comment by hedtke created at 2011-07-18 21:46:28

Changing status from needs_work to needs_review.


---

Comment by hedtke created at 2011-07-18 21:46:28

I restarted the translation from scratch (because the old patch was broken).
I also updated the translation. I corrected some errors and now it is synced with the english version.
Please proofread it.


---

Comment by jhpalmieri created at 2011-07-18 21:50:36

I don't speak German so I can't help with the real review, but I would say this: rather than including the patch to `doc/common/build_options.py`, you should instead set the dependencies for this ticket to #9725.  (Actually, I just set the dependencies so you don't have to, but you should remove that part of the patch file.)


---

Attachment

restarted the translation. use this instead of all former patches.


---

Comment by hedtke created at 2011-07-18 21:55:41

Thanks I updated the patch. Now it only contains the translation of the installation guide.
Please be sure that you applied the patches from #9725 before proofread the new version.


---

Comment by leif created at 2011-07-19 20:06:21

Also einige Tip[p]fehler sind noch drin, ein paar Formulierungen sind auch etwas merkwürdig oder umständlich. "Eingabezeile" ist allenfalls Microsoft-Deutsch, den "Installationsführer" würde ich entsorgen und stattdessen das deutsche Wort "Installationsanleitung" verwenden.

Habe im Moment leider keine Zeit, alles zu lesen, vielleicht später.

P.S.: Durchaus möglich, dass das englische Original auch noch inhaltliche Fehler sowie Ungereimtheiten enthält; das war zumindest der Fall, als ich Bernhards Übersetzung korrekturgelesen habe.


---

Comment by hedtke created at 2011-07-19 20:45:47

In meinem Dokument kommt "Installationsführer" nicht vor. Welche Version hast Du Dir angesehen?


---

Comment by hedtke created at 2011-07-19 20:47:11

apply after trac_8660_restart.patch


---

Attachment

Die "Eingabezeile" ist jetzt raus ;-)

*BITTE BEACHTEN*: Wegen dem fehlerhaften ersten Patch, habe ich einen kompletten *NEUSTART* gemacht. Bitte zuerst #9725 anwenden (eine *Abhängigkeit*). Dann trac_8660_restart.patch und danach trac_8660_restart_p1.patch. Alle anderen Patches sind in meinem NEUSTART enthalten.


---

Comment by leif created at 2011-07-19 21:10:36

Replying to [comment:30 hedtke]:
> In meinem Dokument kommt "Installationsführer" nicht vor. Welche Version hast Du Dir angesehen?

Ähem, habe nur das komplette Attachment überflogen, der Führer ist noch in `doc/de/installation/index.rst` zu finden.

Bin mir jetzt nicht sicher welche Teile neu oder von Dir überarbeitet sind.


---

Comment by hedtke created at 2011-07-19 21:23:51

apply after trac_8660_restart_p1.patch


---

Attachment

Vielen lieben Dank. Diese Datei produziert keinen Output in der PDF und in der HTML. Daher habe ich das nicht gesehen und leider auch vergessen zu korrigieren. Ist damit geschehen ;-)


---

Comment by leif created at 2011-07-19 21:45:06

John, we really have to get rid of these odd messages:

```
Detected SAGE64 flag
Building Sage on OS X in 64-bit mode
# HG changeset patch
# User Ivo Hedtke <hedtke@me.com>
# Date 1311110488 -7200
# Node ID 3348063a50bb0129e20520811c459b799eca49b9
# Parent  7bf76cfce2b3dabf5aeaf7a47d985b2204ad5cc0
```

(That's from [attachment:trac_8660_restart_p2.patch], the other two patches have it as well.)


---

Comment by jhpalmieri created at 2011-07-19 22:28:00

Replying to [comment:34 leif]:
> John, we really have to get rid of these odd messages:

As far as I can tell, they _are_ gone in the prerelease versions of Sage 4.7.1.  (They are still present in 4.7, though.)


---

Comment by leif created at 2011-07-20 02:44:38

Replying to [comment:36 jhpalmieri]:
> As far as I can tell, they _are_ gone in the prerelease versions of Sage 4.7.1.  (They are still present in 4.7, though.)

Ah, ok. Never was a victim of them.


---

Comment by leif created at 2011-07-20 03:48:17

Also das PDF ist zum K...: 38 Seiten für eine "kurze Anleitung für die Erstinstallation".

Sollte vielleicht erst sammeln, aber hier ist schon mal das Komma falsch gesetzt:

  _Bestimmen Sie den Typ Ihrer CPU (32-bit, 64-bit oder “atom” für Linux und Intel, oder PowerPC für Mac OS X)._

Die Beschreibung ist ohnehin etwas unsinnig, da für die Wahl zwischen 32-Bit- und 64-Bit-Version _das Betriebssystem_ und nicht die vorliegende CPU maßgeblich ist.


---

Comment by hedtke created at 2011-07-20 07:13:31

Dann sollten wir vielleicht einfach "kurz" streichen. Siehst Du Möglichkeiten/Bedarf irgendwo signifikant zu kürzen?


---

Comment by leif created at 2011-07-20 07:26:28

Replying to [comment:39 hedtke]:
> Dann sollten wir vielleicht einfach "kurz" streichen. Siehst Du Möglichkeiten/Bedarf irgendwo signifikant zu kürzen?

Naja das Problem ist vorallem auch die Formatierung. "kurz" zu streichen wäre schon sinnvoll.

Man könnte auch die Reihenfolge ändern, sodass die wichtigen Punkte (baumfreundlich ausdruckbar) am Anfang stehen. Die Paketliste könnte man beispielsweise in einen Anhang verfrachten.

Denke aber eher, eine zusätzliche, _wirklich kurze_ Installationsanleitung (1 bis 2 DIN-A4-Seiten) zum Ausdrucken wäre praktischer. Auf besonderen, für den 08/15-Benutzer eher irrelevanten Kram könnte man dort einfach verweisen.


---

Comment by hedtke created at 2011-07-20 07:35:55

Schöne Idee. Ich wäre auch für so eine zusätzliche Kurzanleitung auf max. 2 Seiten. Allerdings frage ich mich, ob das mit den rst-Dateien zu machen ist. Die jetzige Version produziert schon sehr viel Leerseiten und Co.


---

Comment by davidloeffler created at 2012-03-10 17:38:35

Apply trac_8660_restart.patch, trac_8660_restart_p1.patch, trac_8660_restart_p2.patch

(for the patchbot)


---

Comment by vbraun created at 2013-01-13 11:36:46

Die ersten zwei Zeilen in trac_8660_restart.patch gehoeren da nicht hin:

```
Detected SAGE64 flag
Building Sage on OS X in 64-bit mode
# HG changeset patch
...
```

Der Inhalt sieht OK aus, haetten wir schon laengst mergen sollen. Falls Leif noch etwas an der Formulierung schrauben will dann kann er ja selbst noch einen patch dazufuegen...

The perfect is the enemy of the good


---

Comment by leif created at 2013-01-13 14:53:40

Replying to [comment:43 vbraun]:
> The perfect is the enemy of the good

Der Feind des Guten ist das bessere they say.


---

Comment by kcrisman created at 2013-01-17 13:58:16

> Der Inhalt sieht OK aus, haetten wir schon laengst mergen sollen. Falls Leif noch etwas an der Formulierung schrauben will dann kann er ja selbst noch einen patch dazufuegen...
"mergen sollen" - schon wieder so was eingedeutscht... Ist "Installationsführer" denn so viel schlimmer als Airport BER/FRA/...? ;-)

#9725 ist auch längst "eingemergt", falls man es so formulieren kann...

Ich habe die "patches" "rebasiert", d.h. die zwei überflüssigen Zeilen entfernt.   Volkers Kommentar betrachte ich als Erlaubnis, "positive review" zu "clicken".  Ich sehe keine schlimme Formatierung in die "gebaute" Dokumentation.


---

Comment by kcrisman created at 2013-01-17 13:58:16

Changing status from needs_review to positive_review.


---

Attachment


---

Attachment


---

Comment by kcrisman created at 2013-01-17 14:00:19

Patchbot, apply trac_8660_restart.2.patch, trac_8660_restart_p1.2.patch, and trac_8660_restart_p2.2.patch.


---

Comment by jdemeyer created at 2013-01-19 09:48:50

It's a very nitpicking detail, but you should not use TABs for indentation.  Here is a TAB used:

```
Zur Überprüfung of ``perl`` installiert ist, tippt man

::

   command -v perl

```



---

Comment by jdemeyer created at 2013-01-19 09:48:50

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-01-20 08:09:43

I am afraid this is a translation of an *outdated version* of the installation manual, a lot has changed and is in fact quite wrong, in particular the "installing from source" part.  It even causes:

```
sage -t  --long -force_lib devel/sage/doc/de/installation/source.rst
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/devel/sage-main/doc/de/installation/source.rst", line 166:
    sage: import _tkinter
Exception raised:
    Traceback (most recent call last):
      File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        import _tkinter###line 166:
    sage: import _tkinter
    ImportError: No module named _tkinter
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/devel/sage-main/doc/de/installation/source.rst", line 167:
    sage: import Tkinter
Exception raised:
    Traceback (most recent call last):
      File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        import Tkinter###line 167:
    sage: import Tkinter
      File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.7.beta0/local/lib/python2.7/lib-tk/Tkinter.py", line 39, in <module>
        import _tkinter # If this fails your Python may not be configured for Tk
    ImportError: No module named _tkinter
**********************************************************************
```



---

Comment by kcrisman created at 2014-11-20 16:35:10

Changing component from documentation to translations.


---

Comment by mkoeppe created at 2021-09-01 20:05:40

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2021-09-01 20:05:40

outdated, should close


---

Comment by jhpalmieri created at 2021-09-01 20:21:01

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-09-02 18:48:47

Resolution: invalid
