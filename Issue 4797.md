# Issue 4797: upgrade -- if upgrading Cython run -ba instead of -b

Issue created by migration from https://trac.sagemath.org/ticket/4797

Original creator: mabshoff

Original creation time: 2008-12-14 14:44:14

Assignee: mabshoff

CC:  robertwb

When upgrading Cython like at #4639 we should really run a -ba on upgrade and not just a -b since the new Cython version in this case does fix some fundamental issues the way exceptions are handled. In general I would be sleep much better if we do this in general since many potentially odd Heisenbugs that disappear after either a partial -b or a -ba would be avoided that way.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-26 22:53:30

I can live with this issue being fixed in 3.3 since we will not upgrade Cython in 3.2.2->3.2.3.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-26 22:54:10

Ooops. Reassigned this time :)

Cheers,

Michael


---

Comment by was created at 2008-12-29 06:03:58

Does anybody have any idea how to implement this?   Here is one idea.  We make it so there is a command like "sage -ba" that doesn't actually rebuild the sage library, then we make the cython spkg-install call that command.  It could be called "sage -ba_nobuild" or something.  This is way better, I think, than "sage -ba" trying to detect if cython was upgraded.  

The disadvantage is that it might make testing installing the cython SPKG inconvenient.


---

Comment by robertwb created at 2008-12-29 19:38:01

Yes, this would make testing Cython spkgs a major pain. I think this probably best belongs in the upgrade script--it could touch all .pyx files after upgrading the Cython script.


---

Comment by mabshoff created at 2008-12-29 19:42:26

Yes and no. When I test Cython releases I delete the build tree and then do a -ba anyway since that is the only reliable way to test. Obviously if someone is testing "just" the spkg this ought to be not enforced, so RobertWB's idea seems the way to go.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-29 20:14:07

Yep, when you test a Cython release (assuming I've done my job) it should just work. That's different when I'm hunting down a bug and want to keep re-compiling a certain file (e.g. that last memory leak).


---

Comment by was created at 2009-06-15 23:23:15

Changing priority from blocker to critical.


---

Comment by was created at 2009-06-15 23:23:15

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by jdemeyer created at 2010-11-02 22:30:35

Changing keywords from "" to "upgrade cython".


---

Comment by jdemeyer created at 2010-11-02 22:30:35

Changing priority from critical to blocker.


---

Comment by jdemeyer created at 2010-11-02 22:30:35

Changing component from packages to build.


---

Comment by leif created at 2010-11-03 20:11:44

This is just due to missing dependencies in `module_list.py`, so if everybody updating spkgs carefully checked them and added missing ones, this would be a non-issue. (And I consider it as such. Perhaps worth a work-around hint in the Developer's and / or Installation Guide.)

At least for upgrades to final versions, this should IMHO *never* be necessary.


---

Comment by leif created at 2010-11-03 20:20:31

P.S.: Explicitly touching some files in `spkg-install` that _are_ contained in the extension modules' `include_dirs` can also avoid `sage -ba`, though of course a hack.


---

Comment by jdemeyer created at 2010-11-04 20:38:37

Changing priority from blocker to major.


---

Comment by jdemeyer created at 2010-11-04 20:38:37

Replying to [comment:11 leif]:
> This is just due to missing dependencies in `module_list.py`, so if everybody updating spkgs carefully checked them and added missing ones, this would be a non-issue. (And I consider it as such. Perhaps worth a work-around hint in the Developer's and / or Installation Guide.)

I created ticket #10124 to implement this.


---

Comment by leif created at 2010-11-04 21:53:46

Replying to [comment:13 jdemeyer]:
> I created ticket #10124 to implement this.

#10214


---

Comment by leif created at 2010-11-04 22:11:44

Running `sage -ba` _explicitly_ is not even necessary upon (true) Cython upgrades, though we could implement this in `spkg/install`.

We just have to make any Cython file / extension module depend on a single, distinct file of the Cython distribution (e.g. header) and preferably make sure this is _only_ touched when really necessary.

Therefore it would make sense to use a Sage-specific file for such, which is created and managed by our `spkg-install` for Cython.

People upgrading the Cython package will best know if a complete rebuild will be necessary, depending on the Cython version found in the current installation subject to upgrade.


---

Comment by jdemeyer created at 2012-10-05 08:56:48

Resolution: worksforme


---

Comment by jdemeyer created at 2012-10-05 08:56:48

Closing this since I haven't seen this problem at all recently.
