# Issue 9440: document more environment variables

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-07-06 18:10:50

Assignee: mvngu

CC:  leif

In ticket #8263, we missed these:

 - SAGE_DOC_JSMATH - should force docs to be built using jsMath

 - SAGE_DOCBUILD_OPTS - passed as an argument to `sage --docbuild` in the main Sage makefile.



---

Comment by leif created at 2010-07-06 18:14:36

I'm quite sure there are more missing... ;-)


---

Comment by leif created at 2010-08-20 13:56:24

TODO:
 * Add `PARI_EXTRA_OPTS`, which is passed to PARI's `Configure` when building Sage / installing the PARI spkg.
 * Add `CPPFLAGS`, `LDFLAGS`, `CXXFLAG64`?, `LDFLAG64`? `LD`?
 * Document that (e.g.) `export CFLAGS=""` has not the same effect as `unset CFLAGS`.
 * Add note on not putting a space between `-j` and `NUM` in the description of `MAKE`, because doing so has a "completely" different meaning...
 * Add warning to (setting) `SAGE_CHECK`, since this currently breaks most builds. This will (or should) be fixed in future releases though; there's afaik a ticket adding more options to the value of this variable...
 * Add a note on / reference to `sage-env`.

Also, the description of some variables is incomplete, not current (in its use in all spkgs, e.g. `SAGE_DEBUG`), misleading, or even wrong (`SAGE_TIMEOUT*`).

I think the various variations of `SAGE_T[E]MP[[_]DIR]` are missing. (I wonder where e.g. `TMP` and `TMPDIR` are / may be used instead, or as a fall-back / default.)

`SHELL` might be relevant, too.

The `*ITER*` variables for (parallel) doctesting are missing.

I'm currently not sure if we have a similar section in the _Developer's Guide_, but some variables like `SAGE_ROOT` and `SAGE_LOCAL` should be documented (there?), too.

I'm still pretty sure even more variables are missing... ;-)


---

Comment by kcrisman created at 2014-11-20 16:01:00

> SAGE_DOC_JSMATH
`SAGE_DOC_MATHJAX` is now in good shape.
>  * SAGE_DOCBUILD_OPTS
if it still exists
>  * Add `PARI_EXTRA_OPTS`, which is passed to PARI's `Configure` when building Sage / installing the PARI spkg.
>  * Add `CPPFLAGS`, `LDFLAGS`, `CXXFLAG64`?, `LDFLAG64`? `LD`?
>  * Document that (e.g.) `export CFLAGS=""` has not the same effect as `unset CFLAGS`.
>  * Add note on not putting a space between `-j` and `NUM` in the description of `MAKE`, because doing so has a "completely" different meaning...
>  * Add warning to (setting) `SAGE_CHECK`, since this currently breaks most builds. This will (or should) be fixed in future releases though; there's afaik a ticket adding more options to the value of this variable...
This is basically fine now
>  * Add a note on / reference to `sage-env`.
> Also, the description of some variables is incomplete, not current (in its use in all spkgs, e.g. `SAGE_DEBUG`), misleading, or even wrong (`SAGE_TIMEOUT*`).
> I think the various variations of `SAGE_T[E]MP[[_]DIR]` are missing. (I wonder where e.g. `TMP` and `TMPDIR` are / may be used instead, or as a fall-back / default.)
> `SHELL` might be relevant, too.
> The `*ITER*` variables for (parallel) doctesting are missing.
> I'm currently not sure if we have a similar section in the _Developer's Guide_, but some variables like `SAGE_ROOT` and `SAGE_LOCAL` should be documented (there?), too.
There is a ticket for the latter to be better, and the former is now in good shape.
> I'm still pretty sure even more variables are missing... ;-)
Indubitably.


---

Comment by jhpalmieri created at 2014-11-20 19:35:53

Replying to [comment:7 kcrisman]:
> >  * SAGE_DOCBUILD_OPTS
> if it still exists

It is actually used for docbuilding in the top-level `Makefile`. So it ought to be documented.


---

Comment by jhpalmieri created at 2014-11-20 19:36:33

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2014-11-20 19:36:33

New commits:


---

Comment by kcrisman created at 2014-11-20 19:43:46

Nice!  Though I misled you by the wiki formatting.  I don't know the status of these, and at least some definitely aren't documented.

>  * Add `PARI_EXTRA_OPTS`, which is passed to PARI's `Configure` when building Sage / installing the PARI spkg.
Needed?
>  * Add `CPPFLAGS`, `LDFLAGS`, `CXXFLAG64`?, `LDFLAG64`? `LD`?
Needed?
>  * Document that (e.g.) `export CFLAGS=""` has not the same effect as `unset CFLAGS`.
Needed?
>  * Add note on not putting a space between `-j` and `NUM` in the description of `MAKE`, because doing so has a "completely" different meaning...
Needed?
>  * Add a note on / reference to `sage-env`.
Needed?
> Also, the description of some variables is incomplete, not current (in its use in all spkgs, e.g. `SAGE_DEBUG`), misleading, or even wrong (`SAGE_TIMEOUT*`).
Needed?
> I think the various variations of `SAGE_T[E]MP[[_]DIR]` are missing. (I wonder where e.g. `TMP` and `TMPDIR` are / may be used instead, or as a fall-back / default.)
Needed?
> `SHELL` might be relevant, too.
Needed?
> The `*ITER*` variables for (parallel) doctesting are missing.
Needed?


---

Comment by kcrisman created at 2014-11-20 19:55:56

Indeed, the output of 

```
sage.env.[tab]
```

is also worth considering.


---

Comment by git created at 2014-11-21 21:56:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jhpalmieri created at 2014-11-21 21:59:34

Replying to [comment:11 kcrisman]:
> Nice!  Though I misled you by the wiki formatting.  I don't know the status of these, and at least some definitely aren't documented.
> 
> >  * Add `PARI_EXTRA_OPTS`, which is passed to PARI's `Configure` when building Sage / installing the PARI spkg.
> Needed?

Doesn't seem to be used, but some other variables are used in Pari's spkg-install file. I've documented those (just copying from spkg-install, basically).

> >  * Add `CPPFLAGS`, `LDFLAGS`, `CXXFLAG64`?, `LDFLAG64`? `LD`?
> Needed?

I added a bit about them.

> >  * Document that (e.g.) `export CFLAGS=""` has not the same effect as `unset CFLAGS`.
> Needed?

Same here.

> >  * Add note on not putting a space between `-j` and `NUM` in the description of `MAKE`, because doing so has a "completely" different meaning...
> Needed?

I don't know, this isn't Sage specific. I think we can skip it.


> >  * Add a note on / reference to `sage-env`.
> Needed?

Done.

> > Also, the description of some variables is incomplete, not current (in its use in all spkgs, e.g. `SAGE_DEBUG`), misleading, or even wrong (`SAGE_TIMEOUT*`).
> Needed?

I noticed that the documented value for SAGE_TIMEOUT was wrong. Beyond that, I don't know what Leif meant by this. If he wants to expand on it at some point, he can open another ticket and clarify.

> > I think the various variations of `SAGE_T[E]MP[[_]DIR]` are missing. (I wonder where e.g. `TMP` and `TMPDIR` are / may be used instead, or as a fall-back / default.)
> Needed?

I don't think there are such variables anymore. There is a variable SAGE_TMP used while running Sage, but it's not user-customizable and it's not an environment variable. So I don't think we need to document it.

> > `SHELL` might be relevant, too.
> Needed?

Why? Let's skip it. What does it have to do with Sage?

> > The `*ITER*` variables for (parallel) doctesting are missing.
> Needed?

I added something about them.


---

Comment by git created at 2014-11-21 22:19:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jhpalmieri created at 2014-11-21 23:59:28

Oh, for what it's worth, I set `SAGE_TUNE_PARI` to yes and rebuilt pari. Without this set, it took 4 minutes. With it set, it took 2 hours. So the comment about being time-consuming is accurate.


---

Comment by kcrisman created at 2014-12-18 04:19:11

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-18 15:51:50

Resolution: fixed
