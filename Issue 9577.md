# Issue 9577: chinese translation of the tutorial

Issue created by migration from https://trac.sagemath.org/ticket/9577

Original creator: schilly

Original creation time: 2010-07-22 21:34:00

Assignee: mvngu

CC:  mvgnu amao@ai7.org vbraun dimpase

i found this on the internetz over here:
http://ai7.org/wp/html/682.html

i am unable to build the pdf, but html works.


---

Comment by schilly created at 2010-07-22 21:38:15

chinese translation of the tutorial


---

Attachment


---

Comment by schilly created at 2010-07-22 21:38:29

Changing status from new to needs_work.


---

Comment by chapoton created at 2014-07-17 20:16:50

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2014-07-17 20:16:50

New commits:


---

Comment by chapoton created at 2014-07-17 20:16:50

Changing keywords from "" to "tutorial, chinese".


---

Comment by git created at 2014-07-19 20:11:32

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-10 15:17:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-21 07:30:15

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-21 18:25:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-22 10:47:31

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-22 10:54:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-22 11:33:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-22 15:47:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-25 19:19:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-09-03 19:16:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vbraun created at 2014-09-23 13:01:21

Is this traditional or simplified? The buildbot also builds the pdf doc. Since chinese is not TeX'ed using babel we'd have to disable pdf output.


---

Comment by vbraun created at 2014-09-23 13:01:29

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2014-11-20 16:34:56

Changing component from documentation to translations.


---

Comment by kcrisman created at 2014-12-04 19:23:45

> Since chinese is not TeX'ed using babel we'd have to disable pdf output.

Is that fairly easy to do with something analogous to the solution in #12559?   It looks like it might "just work" if this ticket depends on that one (I have not tried this yet, though).


---

Comment by kcrisman created at 2014-12-04 20:47:21

This actually looks quite good (html).  I think that the tour_advanced-zh file should replace the other one, since it is clearly a partial translation - or did I miss something there?

I'm going to move this to the `zh_CN` directory created by #12559, assuming that this is also mainland Mandarin.  I have a colleague who has agreed to proofread some stuff and she can comment on that too, of course.

For pdf we'll at least need a config file change, not sure if the solution at #12559 will fix it once that's done.


---

Comment by kcrisman created at 2014-12-04 20:53:59

Okay, once I do that I get the same error as there,

```

Writing index file SageTutorial.idx
kpathsea: Invalid fontname `AR PL UMing CN', contains ' '

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!
! fontspec error: "font-not-found"
! 
! The font "AR PL UMing CN" cannot be found.
! 
! See the fontspec documentation for further information.
! 
! For immediate help type H <return>.
!...............................................  
```

which is presumably my lack of fontitude.  Good.


---

Comment by kcrisman created at 2014-12-04 20:59:02

In the hopes that the original author might see this and have any comments...


---

Comment by kcrisman created at 2014-12-05 16:17:30

The change in fonts in [comment:51:ticket:12559 this comment] seems to work as well, so whatever solution we get there should work here.  Obviously we could just have two different conf things by messing with that file, but that is not particularly elegant.   There are still a few bugs with the LaTeX macros but on the way to happiness.

Also, the author confirms this is simplified Chinese in private communication.


---

Comment by kcrisman created at 2014-12-05 16:48:36

Okay, the errors I am getting are the same ones as in [comment:22:ticket:12559 this other comment], but for this document we really do need the macros that `\DeclareUnicodeCharacter` provides.  

There is a hack, I think, to just provide the macros this document needs, but it will definitely be just a hack.  If we really want to use more xelatex in the future for our documentation, we will have to find a way to work around this, such as [this one](http://tex.stackexchange.com/a/195460/11532).  (Or Sphinx, or someone, will need to do this.)


---

Comment by dimpase created at 2014-12-05 16:51:13

`\DeclareUnicodeCharacter` for each Chinese character would be fun :-)


---

Comment by kcrisman created at 2014-12-05 17:06:38

> `\DeclareUnicodeCharacter` for each Chinese character would be fun :-)
Yikes!  Luckily, I didn't need any of them, just

```
\newcommand{\Bold}[1]{\mathbf{#1}}
\newcommand{\ZZ}{\Bold{Z}}
\newcommand{\QQ}{\Bold{Q}}
\newcommand{\GF}[1]{\Bold{F}_{#1}}
```

As it turns out, the problem is that `xelatex` doesn't recognize `\DeclareUnicodeCharacter`, and so one never gets to this stuff in the first place.  Of course, I didn't check whether some fairly important math characters for Sage such as

```
\DeclareUnicodeCharacter{0428}{cyrillic Sha}
```

appeared correctly, but from a little browsing I think most of those declarations are just to make things look "nice", e.g.

```
\DeclareUnicodeCharacter{221A}{\sqrt}
```



---

Comment by chapoton created at 2015-11-06 13:09:52

Maybe we can use use here what has worked for japanese in #19188 ?


---

Comment by git created at 2016-01-01 20:44:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2017-06-20 20:39:47

Just as an fyi slight updates are pending in tutorial for sagenb becoming legacy - no need to fix this though.  It would be nice to figure out how to get this to work, or maybe we just give up on pdf?
