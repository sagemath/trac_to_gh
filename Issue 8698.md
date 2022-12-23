# Issue 8698: German translation of the document "A Tour of Sage"

Issue created by migration from https://trac.sagemath.org/ticket/8698

Original creator: mvngu

Original creation time: 2010-04-17 02:49:06

Assignee: mvngu

CC:  bblochl@arcor.de simon.king@nuigalway.ie leif minz

As the subject says.


---

Comment by mvngu created at 2010-04-17 03:21:41

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-04-17 11:21:54

Updated patch in response to Bernhard's new posting at [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/c14c761ee3dc5203).


---

Comment by SimonKing created at 2010-04-17 12:33:33

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-04-17 12:33:33

I made some proof reading, based on the html version that Minh posted at http://sage.math.washington.edu/home/mvngu/8698-tour-de/

 * `Das ist ein Rundgang durch Sage, der sich eng an der „Tour of Mathematica“ am Beginn des Mathematica-Buchs folgt.`
   ---> _Das ist ein Rundgang durch Sage, der sich eng an die „Tour of Mathematica“ am Beginn des Mathematica-Buchs anlehnt._
   oder freier ---> _Das ist ein Rundgang durch Sage, der sich an der „Tour of Mathematica“ am Beginn des Mathematica-Buchs orientiert._
   bzw. ---> _Das ist ein Rundgang durch Sage, der von der „Tour of Mathematica“ am Beginn des Mathematica-Buchs inspiriert ist._
 
 * `Wenn Sie das Sage in der Notebook-Version (als Notizbuch) benutzen`. Since Sage is a name, it should be _Wenn Sie Sage in der Notebook-Version..._

 * `Die Berechnung und Ausgabe des Wertes erfolgt nach der Eingabe der Tasten shift+return`. Keys are not being entered. So, better
   _Die Berechnung und Ausgabe des Wertes erfolgt nach gleichzeitigem Drücken der Tasten shift+return_

 * `Die Invertierung der Matrix 2 \times 2 in Sage:` should be replaced by `Die Invertierung einer (2 \times 2)-Matrix in Sage:`.

 * `Damit ermittelt Sage eine quadratische Gleichung.` It was not immediately clear to me what "Damit" refers to. Moreover, the equation is not "determined" but "solved". So, perhaps better _Im nächsten Beispiel löst Sage eine quadratische Gleichung._

 * `Sage benötigt weniger als 5 Sekunden um die Anzahl der möglichen Varianten zur Partitionierung von... zu berechnen`: There is a comma missing; I don't think that one would talk about "number of possible *variants* of partitions"; Sage is not only computing the number of partitions, but actually finds the partitions (which is stronger); and I think "partition" is "Partition" in German. So, I suggest _Sage benötigt weniger als 5 Sekunden, um alle Partitionen von... zu ermitteln_.

 * Last phrase of section "Sage-Algorithmen benutzen": I suggest to remove the parentheses. Perhaps one can make a footnote, but I think the phrase is just fine in normal text.

Best regards, and thank you for working on a German translation,

Simon


---

Comment by mvngu created at 2010-04-17 23:47:47

based on Sage 4.3.5


---

Attachment

Thanks, Simon... ;-)

I think what's at all meant by "Notebook" has to be explained, too. A typical German reader would first think of his laptop, not a user interface (which is funny if not annoying in the translation of the user guide when talking about `ssh_keygen`...).

It would be nice if you could supply a patch on top of Minh's.

-Leif


---

Comment by SimonKing created at 2010-04-19 09:15:20

Adding a section on the notebook; adding the missing plots; some proof reading


---

Attachment

Replying to [comment:5 leif]:
> I think what's at all meant by "Notebook" has to be explained, too. 

Good idea (and perhaps it would make sense to have this in English, too).

> It would be nice if you could supply a patch on top of Minh's.

Done. 

My patch adds a section on the notebook (I hope I didn't write too much nonsense, because I hardly ever use the notebook) and the two png-plots that were missing.

Minh: Is it OK to first finish this ticket off before focusing on #8660? Or should the two tickets be united at an earlier stage?

Best regards, Simon


---

Comment by SimonKing created at 2010-04-19 09:20:20

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-04-19 09:23:34

Helas.

I just found one typo. I wrote:
"Die Anzahl der Möglichkeiten ist gigantisch, wir geben hier nur die letzten 40 Ziffern an."

Should be "Die Anzahl der Möglichkeiten ist gigantisch, wir geben hier nur die ersten 40 Ziffern an."

But I think this should be fixed once there are more comments of another reviewer.


---

Comment by mvngu created at 2010-04-19 10:47:16

Replying to [comment:6 SimonKing]:
> Minh: Is it OK to first finish this ticket off before focusing on #8660? Or should the two tickets be united at an earlier stage?

The Sage tour is much shorter than the installation guide. So I think the tour would be the first to get into the Sage standard documentation. Thank you for reviewing the tour.


---

Comment by aapitzsch created at 2010-11-19 16:44:52

in conf.py:
 * add `language = 'de'` (to replace _Chapter_ by _Kapitel_)
 * set `html_short_title` to `Sage Rundgang`

in index.rst:
 * `Computer-Labors` ---> `Computerlabors`
 * `shift-return` ---> `Shift + Return` or use only the German words
 * `Gleichheitszeichen.(Das Zeichen` ---> `Gleichheitszeichen. (Das Zeichen`

Some pictures (_sin_plot.png, eigen_plot.png_) are missing. I think they should be put inside _doc/common_ and not be shipped by every language version itself.

When you fixed everything set status back to _needs review_.


---

Comment by aapitzsch created at 2010-11-19 16:44:52

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2014-07-18 12:56:03

Changing keywords from "" to "german".


---

Comment by chapoton created at 2014-07-19 20:51:57

Here is a git branch, passing tests and with html building correctly. I think it can be considered as needs review.
----
New commits:


---

Comment by chapoton created at 2014-07-19 20:51:57

Changing status from needs_work to needs_review.


---

Comment by aapitzsch created at 2014-07-19 21:30:17

See comments 7 and 9.


---

Comment by aapitzsch created at 2014-07-19 21:30:17

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-07-20 07:34:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-07-20 15:41:10

Done. Needs review now.


---

Comment by chapoton created at 2014-07-20 15:41:10

Changing status from needs_work to needs_review.


---

Comment by aapitzsch created at 2014-07-20 17:39:08

Frédéric, if you are happy with my changes you can set the status to positive review.


---

Comment by chapoton created at 2014-07-20 18:13:47

Danke schön !


---

Comment by chapoton created at 2014-07-20 18:13:47

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-07-21 17:38:07

Resolution: fixed
