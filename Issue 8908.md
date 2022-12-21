# Issue 8908: Add the Young subgroup method to symmetric groups

Issue created by migration from Trac.

Original creator: jipilab

Original creation time: 2010-05-06 17:58:20

Assignee: joyner

To every composition is associated a Young subgroup. This method returns the Young subgroup associated to the given composition.


---

Comment by jipilab created at 2010-05-06 19:04:45

I uploaded the patch.

attachment:trac_8908-young_subgroup.patch


---

Comment by jipilab created at 2010-05-06 19:04:45

Changing status from new to needs_review.


---

Comment by chapoton created at 2011-07-23 19:03:20

Could you please 

* fold the patches into one patch
* add #8908 to the first description line (instead of trac 8908)

It may then allow to have a green light from the bot.


---

Comment by jipilab created at 2011-08-24 20:36:47

I fixed the description line of the second patch. I hope that the bot will like it.


---

Comment by chapoton created at 2011-10-14 20:13:59

I would give a positive review if you could fold the two patches into one.

The bot is currently not working, so one does not require the green light.


---

Comment by chapoton created at 2011-10-16 20:18:27

Changing status from needs_review to needs_work.


---

Comment by jipilab created at 2011-11-09 11:24:40

I attached a folded patch. This one should work.


---

Comment by jipilab created at 2011-11-09 11:24:40

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2011-11-25 09:21:27

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2011-11-25 09:21:27

This is ok for me, assuming that all tests pass ; I have not checked that.


---

Comment by jipilab created at 2011-11-25 17:15:54

Changing status from positive_review to needs_work.


---

Comment by jipilab created at 2011-11-25 17:15:54

The last patch was tested on 4.7.2 and passed.


---

Comment by jipilab created at 2011-11-25 17:16:32

Changing status from needs_work to needs_review.


---

Comment by jipilab created at 2011-11-25 17:16:32

Changed to needs review: Test passes now.


---

Comment by slabbe created at 2011-11-29 22:25:40

For the patchbot :

Apply trac_8908_young_subgroup_folded.patch


---

Comment by mhansen created at 2011-12-18 13:16:30

Generally, I think this is good, but I changed it so that it works with the symmetric group on an arbitrary domain.  Could you look over my changes?


---

Comment by mhansen created at 2011-12-18 13:17:30

For the patchbot :

Apply 

trac_8908_young_subgroup_folded.patch
trac_8908-young_subgroup-review.patch


---

Comment by mhansen created at 2012-03-29 07:27:06

Apply trac_8908_young_subgroup_folded.patch trac_8908-young_subgroup-review.patch


---

Comment by chapoton created at 2012-06-08 20:33:13

Well, this seems ok to me. I would rather replace


```
gen = self((domain[pos + i], domain[pos + i + 1]))
gens.append(gen) 
```


by the single line

```
gens.append(self((domain[pos + i], domain[pos + i + 1])))
```


I am a bit puzzled by the "PluginFailed" given by the bot. What is the meaning of ValueError("Mercurial queue boilerplate") ?


---

Comment by chapoton created at 2012-06-08 20:33:13

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2012-08-01 06:48:57

I've made that change.

Apply trac_8908_young_subgroup_folded.patch, trac_8908-young_subgroup-review.patch


---

Comment by mhansen created at 2012-08-01 06:48:57

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2012-08-28 08:42:35

Apply: [attachment:trac_8908_young_subgroup_folded-2.patch]


---

Comment by chapoton created at 2012-08-28 08:43:17

Apply only [attachment:trac_8908_young_subgroup_folded-2.patch]


---

Attachment


---

Comment by chapoton created at 2012-09-23 12:58:33

applies on 5.4beta1, all tests pass, doc is ok: positive review


---

Comment by chapoton created at 2012-09-23 12:58:33

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2012-09-23 12:58:33

Changing keywords from "" to "symmetric group".


---

Comment by jdemeyer created at 2012-09-26 07:46:49

Resolution: fixed
