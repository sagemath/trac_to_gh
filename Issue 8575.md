# Issue 8575: Sphinx should raise warning in case of ill formated enumerated lists

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-03-22 09:50:40

Assignee: mvngu

CC:  jhpalmieri mpatel

Keywords: Sphinx, warning

In some cases, for example when an enumerated list is ill formated, in text mode ouput sphinx returns silently an empty string. It should at least raise some warning. See #8572 for an instance of the problem.
At this point, I don't know if it's a bug of sphinx or the way we call it.


---

Comment by hivert created at 2010-03-22 14:51:33

There is a very good chance that this is a bug of sphinx. I asked it on
sphinx-dev. I'm waiting for their answer.

For the info, here is a ReST file that triggers the problem:

```
**************************
List Bug Triggering Module
**************************

    - list item 1 -- this item is correctly formated. So that there should be
      no problem with it..

    - list item 2 -- this item is ill formated. Sphinx should raise a warning
       when typesetting in in text mode.
```


Florent


---

Comment by hivert created at 2010-04-06 08:32:20

This is indeed a bug of sphinx (see [this Sphinx-dev thread](http://groups.google.com/group/sphinx-dev/t/c65dcb4b8a057d04)). Georg Brandl answered:

   The behavior is clearly a bug, and I've now fixed it in changeset `93ae46825651`
   in the 0.6 branch.  It will be part of the next bugfix release.

I'm not sure what to do now with this ticket... Should we back port the bugfix or wait for the next release ? Should this ticket be left open ? 

Florent


---

Comment by mvngu created at 2010-04-06 21:31:15

Replying to [comment:3 hivert]:
> I'm not sure what to do now with this ticket... Should we back port the bugfix or wait for the next release ? Should this ticket be left open ? 

I would think wait for the next release, as that is (maybe) much easier than backporting. If you can backport, then by all means do so. Until the issue is fixed by upgrading to the new release with the bug fixed, or backporting, this ticket would remain open.


---

Comment by hivert created at 2010-04-07 07:27:38

Changing status from new to needs_info.


---

Comment by hivert created at 2010-04-07 07:27:38

Replying to [comment:4 mvngu]:
> I would think wait for the next release, as that is (maybe) much easier than backporting. If you can backport, then by all means do so. Until the issue is fixed by upgrading to the new release with the bug fixed, or backporting, this ticket would remain open.

According to Georg Brandl, Sphinx should make a new bugfix release "soon"... So I'm in favor of waiting for it.


---

Comment by hivert created at 2011-04-04 16:56:52

This ticket should be closed since sage uses now sphinx 1.0.4


```
(WARNING/2) Bullet list ends without a blank line; unexpected unindent.
```


I set this to positive review.


---

Comment by hivert created at 2011-04-04 16:56:52

Changing status from needs_info to needs_review.


---

Comment by hivert created at 2011-04-04 16:57:02

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-05 16:00:07

Resolution: duplicate
