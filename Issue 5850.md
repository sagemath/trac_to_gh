# Issue 5850: add Creative Commons license to French tutorial

Issue created by migration from https://trac.sagemath.org/ticket/5850

Original creator: ddrake

Original creation time: 2009-04-22 04:18:03

Assignee: tba

The French tutorial doesn't specify a license; to go along with all the other documentation, I think it should have a Creative Commons Attribution-Sharealike license.

I could cut and paste something myself, but I think it would be better if a French-speaking Sage developer got permission from the author and did this, as I would inevitably screw up a breve or grave accent somewhere. :)

Ticket #4809 is the English version of this ticket.


---

Attachment


---

Comment by mmezzarobba created at 2009-04-27 21:06:19

Replying to [ticket:5850 ddrake]:
> The French tutorial doesn't specify a license; to go along with all the other documentation, I think it should have a Creative Commons Attribution-Sharealike license.
> 
> I could cut and paste something myself, but I think it would be better if a French-speaking Sage developer got permission from the author and did this, as I would inevitably screw up a breve or grave accent somewhere. :)
> 
> Ticket #4809 is the English version of this ticket.


---

Comment by mmezzarobba created at 2009-04-27 21:10:20

Hi,

I am one of the translators of the tutorial. I have just noticed that the French translation was added to the Sage repository by Mike Hansen... a few days before we put its proofread version on the wiki!

So I guess the best I can do now is to provide one single patch which updates the translation and fixes all the issues with it I am aware of, namely this ticket, #4318 and #5337. There had been a few changes (limited to the doctests and the build scripts) in the version of the French tutorial in the hg repository in the meantime; I have done my best to merge them with our work.

-- Marc


---

Comment by ddrake created at 2009-04-28 00:32:02

The patch did not quite apply to a 3.4.2.alpha0 (yes, that's a mistake above) tree, so I've uploaded a version which should apply cleanly. One problem was that now you can do ``\QQ`` instead of something like ``\mathbf{Q}``; I fixed all the occurrences I could find.

I'm also assigning this ticket to mmezzarobba, since he did upload a patch.


---

Comment by ddrake created at 2009-04-28 00:32:02

Changing assignee from tba to mmezzarobba.


---

Comment by ddrake created at 2009-04-30 07:41:37

patch rebased against 3.4.2.alpha0; \QQ fixes; doctest fixes


---

Attachment

Oops, I just found that the tutorial doesn't pass doctests...mostly because the doctest framework doesn't speak French, so if you have "`# nécessite le paquet facultatif database_gap`", it doesn't understand that you mean "`optional - database_gap`". :)

You just need the magic (English) words, so you can still include explanation in French. Things like this work fine:

```
some code # sortie plus ou moins aléatoire (random)

more code # nécessite le paquet facultatif database_gap (optional)
```


I added the necessary English words to the doctests, and also added "..." to a Maxima doctest (at the end of tour_algebra.rst) that had random low order bits.


---

Attachment

(some typo fixes)


---

Comment by nborie created at 2009-06-21 23:29:18

I added a very small patch which fix some typo in the sagetutfr-updated.patch

The patch is very good. I have learn some informations by reading it carefully. I give this patch a positive review. (First review for me...)
Being also French, I thank very much the authors.


---

Comment by rlm created at 2009-06-24 09:55:46

Resolution: fixed


---

Comment by mmezzarobba created at 2009-06-24 19:26:21

Nicolas, thank you for your review!

Just one remark: I do not know what the 'author' field is used for, but if it is meant to identify the authors of the change (as opposed to track the authors/submitters of the patches) then Bertrand Meyer should be added. Paul Zimmermann and Ismaël Bouya helped with proofreading and suggestions.
