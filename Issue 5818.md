# Issue 5818: Make it possible to pass a CPU parameter to MPIR (useful for builds in KVM)

Issue created by migration from https://trac.sagemath.org/ticket/5818

Original creator: mabshoff

Original creation time: 2009-04-19 01:00:24

Assignee: mabshoff

See #5516 for the motivation for this. It should be something like SAGE_MPIR_CPU and SAGE_MPIR_ABI to pass either a CPU type or an ABI to MPIR. This allows special configs without the need to change the spkg every time one builds.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 14:29:06

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-05-15 14:29:06

This is also very useful for binaries, i.e. if SAGE_SIMD_MODE is set to SSE2 we should only build for a P4 for example.

Cheers,

Michael


---

Comment by was created at 2009-05-27 19:14:10

From Bill Hart:

```
But you asked a couple of questions. As far as MPIR is concerned, you
can control which optimisations are used by giving it the option
--build.

I presume you are making binaries and whatever machines you want to
support don't have SSE3 or higher. If you build on sage.math or
equivalent it will detect penryn which has every optimisation under
the sun.

All x86_64's support SSE3, i.e. pentium4's, core2's, k8's, etc.

So presumably the problem is for 32 bit machines, perhaps early p4's
before Prescott, which is where SSE3 was introduced, I think. So the
trick would be to force MPIR to build for a netburst without LAHF
support. That is an early p4 without all the bells and whistles.

That option would be --build=netburst-unknown-linux-gnu, which you
should pass to configure when building MPIR.

Note that doing this will build a binary which is 32 bits and
optimised for a pentium 4 with netburst architechture. The resulting
code won't be too bad if you are just making binaries, but it should
not be used for building from source. MPIR should be allowed to detect
the CPU and build with the best possible core in that case, obviously.

If building MPIR from source ever gives invalid instructions for a CPU
then that is a bug in MPIR and we would need to fix that upstream.
Sage should never have to pass options to MPIR to get correct
optimisations for a CPU.

Another thing to be aware of is that sending options like
-build=netburst-unknown-linux-gnu to MPIR when building binaries is
only useful if you plan to build lots of binaries - basically one for
each major type of machine MPIR supports. If not, then the best thing
to do is to let MPIR decide at runtime which core to use, by passing
--enable-fat to MPIR's configure when building on an x86_32 machine it
will build a single 32 bit binary which is "optimal" for each possible
machine. This is suboptimal compared with making lots of binaries and
should never be done when the user is building from source, but is a
reasonable compromise if you want to build a single binary which
supports multiple machines. Unlike GMP, --enable-fat also works on
x86_64 machines, though you have to build a separate binary on a 64
bit machine for this to work, obviously.

What Michael and I had discussed was building 10 or so binaries with
MPIR and then having the correct one linked in when Sage starts
depending on what config.guess returns, i.e. running sage would first
run a script which would run config.guess. That would tell you what
processor one had, then the right MPIR binary would be put in the
LD_LIBRARY_PATH or whatever.

The binaries you would include for x86 and x86_64 are:

atom, netburst, netburstlahf, pentium4, prescott, core2, penryn,
nehalem, k7, k8, k10

I don't see anyone getting Sage to run on an x86 before netburst, so
that should be all the binaries you need.
```



---

Comment by was created at 2009-05-28 06:51:12

This isn't critical for 4.0.


---

Comment by was created at 2009-05-31 23:52:42

Changing priority from blocker to major.


---

Comment by mkoeppe created at 2021-12-02 01:01:44

outdated after mpir removal


---

Comment by mkoeppe created at 2021-12-02 01:01:44

Changing status from new to needs_review.


---

Comment by dimpase created at 2021-12-02 23:38:30

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-12-03 18:41:01

Resolution: invalid
