# Issue 5516: gmp-mpir-0.9: build failure inside kvm 64 bit virtual machine

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2009-03-14 16:00:04

Assignee: mabshoff

When running a 64 bit virtual cpu in kvm (72+dfsg-4, debian/lenny), the virtual `cpuid` reports the cpu as:

```
vendor_id       : GenuineIntel
cpu family      : 6
model           : 2
model name      : QEMU Virtual CPU version 0.9.1
stepping        : 3
```

AFAICT, from intel's cpuid documentation in http://download.intel.com/design/processor/applnots/24161832.pdf, such a family/model combination doesn't actually exist (pentiumpro is model 1, pentium II is model 3 and 5, celeron is model 6, etc).

On the other hand the `config.guess` script in mpir considers anything models 2 to 6 as being `pentium2`. Misdetection is already bad because core 2 optimizations should be much better than pentium II ones.

The build then fails because for a pentium II, the configure logic forces `ABI=32`, and this is wrong (configure complains about `sizeof(long)` not being `4`, indeed it is `8`).

Of course, this seems to be a bug in kvm; but maybe it should be workarounded? I don't think it is relevant, but just in case the host cpu reports family=6, model=23 (it's a core 2 quad Q9550).

After the fact I discovered that one can use the following command line switch when running kvm:

```
-cpu qemu64,family=6,model=15,+ssse3
```

to set family/model to a core2, and also set `ssse3` cpu flag (disabled by default). Unfortunately, this comand line switch doesn't support models higher than 15, nor the `sse4_1` flag.


---

Comment by mabshoff created at 2009-03-14 17:00:45

Similar misdetection happens when using an AMD CPU where the cpuid reports garbage, too - see #5186.

Cheers,

Michael


---

Comment by tornaria created at 2009-03-14 17:34:26

I proposed a fix upstream which should fix the current issue:
[configure failure inside kvm 64 bit virtual machine](http://groups.google.com/group/mpir-devel/browse_thread/thread/aeb271247ae0eec9/a90654677f9db1d5)

The proposed patch won't fix the issue for AMD cpu in #5186; a similar fix may be possible for that, but I don't have access to AMD cpus and don't know much about their models.


---

Comment by tornaria created at 2009-04-19 00:33:41

The issue is fixed for me in gmp-mpir-1.1.spkg as installed from http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/gmp-mpir-1.1.spkg.

I installed it with `sage -i URL` on top of sage-3.4, inside a kvm with _no_ `-cpu` command line option, and it works fine. The host is set to x86_64-unknown-linux-gnu, which is the proposed workaround.

For the record, note that compiling mpir with x86_64 default is not optimal for a core2, hence it is strongly recommended that one uses a `-cpu` command line option for kvm like

```
-cpu qemu64,family=6,model=15,+ssse3
```

This works with kvm-72 as shipped with debian. For kvm-84, on a penryn (core 2 quad q9550) I'm actually using

```
-cpu core2duo,model=23,+ssse3,+lahf_lm
```

which should be slightly better.


---

Comment by mabshoff created at 2009-04-19 01:00:48

Thanks Gonzalo, I am closing this as fixed. But I am opening a ticket so that one can pass set SAGE_$FOO variable so that MPIR in Sage sets a special CPU type in case someone is capable of optimizing their settings. 

This enhancement ticket is now #5818.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 01:01:22

This issue has been fixed in Sage 3.4.1.rc4 via the spkg at #5788.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 01:01:22

Resolution: fixed
