# Issue 5564: [with patch, needs review] fix character encoding problems in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/5564

Original creator: mhansen

Original creation time: 2009-03-19 12:06:25

Assignee: boothby

CC:  jason ddrake

Keywords: utf-8 tinymce

This patch when applied on top of #4547 and #5211 will fix the issues people have been having in #2896, #1477, and #4956.

Also, I'm tired of working on Javascript code in triple-quoted strings, so I have moved the code to its own file.  It breaks history but is less crazy.

I will attach two patches -- one for most of the javascript moving and the other for the interesting changes.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-03-19 12:14:17

Note, one thing that may not be obvious from a quick glance at the second patch is the addition of the 'content' function in the addInputType call.


---

Comment by ddrake created at 2009-03-20 02:17:02

Separating the javascript into its own file sounds like a great idea to me. These patches along with #4547 and #5211 seem to fix all the UTF-8 issues I'm aware of.


---

Comment by tornaria created at 2009-03-22 22:07:22

I've tried the patches in #4547 and #5211, and they seem to fix all the UTF-8 issues I had.
I tried #2896, #1477, and #4956, with those applied but with_out_ applying patches in this ticket. The result is:
 - #2896 and #1477 seem to be fixed AFAICT
 - #4956 is partially fixed, but not completely; applying the patches in current ticket doesn't seem to make any difference.

To reproduce the half of #4956 which is not fixed:

 1. enter 

```
print 'Teor&iacute;a de n&uacute;meros'
```

 in a cell, and evaluate. You get back

```
Teor&iacute;a de n&uacute;meros
```

 as expected.
 2. save and quit
 3. open the worksheet again
 4. now the cell reads

```
print 'Teoría de números'
```

 which is incorrect (the output is still the same, but it will change if inserting a cell before the cell in question using "CTRL-ENTER")

I will be applying #4547 + #5211 in a live sage notebook (3.4), and will report back if I find more "incorrect" behaviour (I'm teaching sage in spanish! some accents are needed...). If there are specific issues which the patches in this ticket are supposed to fix which are not fixed by , I can test again.


---

Attachment


---

Comment by mhansen created at 2009-03-23 11:25:06

I've posted a patch which fixes the problems with TinyMCE and jsMath that the earlier ones caused.  TinyMCE, jsMath, and UTF-8 should all be playing nice together.

I also fixed the rest of the issues with #4956.  Since I had to work on the cell output code anyway, I set it up to use templates. I also fixed the small issues at #5324.

The main problem with TinyMCE and UTF-8 is that repr(s) for a string s was being used for define the string in Javascript except this totally breaks when there are "non-standard" characters.  In order to get around this, I used the JSON encoding of the string.  However, this requires the simplejson module ( http://sage.math.washington.edu/home/mhansen/simplejson-2.0.9.spkg); the json module is standard in Python 2.6.  The ticket for simplejson is #1510.  If someone else wants to roll their own Python string -> Javascript string converter to remove the dependency on simplejson, I would have no problem.


---

Comment by mhansen created at 2009-03-23 11:25:06

Changing status from new to assigned.


---

Comment by mhansen created at 2009-03-23 11:25:06

Changing assignee from boothby to mhansen.


---

Comment by ddrake created at 2009-06-01 08:26:55

First, these patches need rebasing against 4.0. Mike, you say that this will break history, but my understanding is that you could just do `hg copy js.py notebook_lib.js` and then delete all the Python stuff from notebook_lib.js. If you use git-style unified diffs, when the patch gets imported into Mercurial, it should follow history.

Second, I did manage to get these patches applied to 4.0, but when I opened an old worksheet that I had had UTF-8 trouble with, I got a server error, since our old code didn't work with UTF-8 correctly and produced invalid UTF-8 files...and the new, 100% UTF-8 code couldn't handle that. I'm guessing there's nothing we can really do about this, since (AFAIK) there's no good way to take an improperly encoded file and translate it into proper UTF-8. I thought I would mention this, though.


---

Comment by ddrake created at 2009-06-03 02:56:49

This ticket is intended to fix [this problem](http://groups.google.com/group/sage-devel/msg/c979d407f5393936): re-editing some UTF-8 text doesn't work. I'm attaching a screenshot that demonstrates the problem.


---

Attachment

screenshot of the save and re-edit problem


---

Comment by boothby created at 2009-06-16 05:45:02

patch_1 bitrotted, so I posted a rebase to #6307.


---

Comment by mvngu created at 2009-07-16 21:24:08

Resolution: fixed


---

Comment by mvngu created at 2009-07-16 21:24:08

Fixed due to #6307.


---

Comment by mhansen created at 2009-07-16 22:34:15

Actually, I don't think #6307 fixes this issue.  I'll apply the patches and double check before re-opening this.


---

Comment by boothby created at 2009-07-18 18:56:30

Changing status from closed to reopened.


---

Comment by boothby created at 2009-07-18 18:56:30

#6307 certainly doesn't fix this ussue.


---

Comment by boothby created at 2009-07-18 18:56:30

Resolution changed from fixed to 


---

Comment by kcrisman created at 2009-08-26 14:04:54

To release manager - recommend closing this ticket, but posting updates to #4956, #5324, and any other relevant tickets to look here for potential code.  The issue ddrake discusses is fixed in #6464 (and also mentioned in #6562), so all issues mentioned here are addressed in other tickets.  That doesn't mean a unified solution isn't possible, but at any rate there is too much going on here.


---

Comment by mvngu created at 2009-08-26 19:57:19

Resolution: wontfix


---

Comment by mvngu created at 2009-08-26 19:57:19

Closing this ticket as per kcrisman's request. Please refer to #4956, #5324, #6464, and #6562 for more specific one-issue focused tickets.
