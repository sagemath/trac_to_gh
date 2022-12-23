# Issue 4070: [with spkg, patch: needs review] fix polybori-0.5.rc1 build issues

Issue created by migration from https://trac.sagemath.org/ticket/4070

Original creator: mabshoff

Original creation time: 2008-09-07 17:22:52

Assignee: mabshoff

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc1/polybori-0.5rc.p3.spkg

fixes a couple issues:

 * delete dynamic libs so that the extension is linked statically
 * touch the pbori.pyx extension so that it forces a rebuild

The attached patch also disables m4ri_destroy_all_codes() in pbori.pyx since it causes double frees on OSX. This is maybe related to #1611.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-07 17:22:58

Changing status from new to assigned.


---

Attachment

Builds fine on:
 * x86_64, Core2Duo, Debian GNU/Linux testing (my notebook)
 * x86_64, Opteron, Ubuntu (my desktop)
 * x86_64, Opteron, Debian GNU/Linux testing (my server at RHUL)
 * x86_64, Opteron, Debian GNU/Linux stable (*sage.math*)
 * x86_64, 2xCore2Duo, Fedora 8 (*eno*)

Strictly speaking, `libs/polybori/decl.pxi` should be touched instead of `rings/polynomial/pbori.pyx` but this isn't a show stopper for now, since only one module links against PolyBoRi anyway (i.e. `rings.polynomialpbori`)


---

Comment by malb created at 2008-09-07 18:07:28


```
[18:20] <mabshoff> #4070, patch will be in a second.
[18:20] <mabshoff> There are odd issues in matrix2.pyx on OSX only where there are issues with Matrix inversion.
[18:22] <mabshoff> patch is also up now.
[18:22] <mabshoff> You need that one to fix an issue once the spkg is updated.
[18:39] <mhansen> #4070 fixes the issues for me.
```



---

Comment by malb created at 2008-09-07 18:09:13

The SPKG also passed manual inspection (everything checked in properly, stuff is documented, etc.) Running doctests on the mentioned machines now.


---

Comment by malb created at 2008-09-07 18:53:47

## Doctests
### x86_64, Core2Duo, Debian GNU/Linux testing (my notebook)

```
The following tests failed:

        sage -t  devel/sage/sage/interfaces/sage0.py # 8 doctests failed
```

### x86_64, Opteron, Ubuntu (my desktop)

a lot of segmentation faults, `sage -ba`ing now, might be local problem.

### x86_64, Opteron, Debian GNU/Linux testing (my server at RHUL)

pass

### x86_64, Opteron, Debian GNU/Linux stable (sage.math)

pass

### x86_64, 2xCore2Duo, Fedora 8 (eno)

pass


---

Comment by malb created at 2008-09-07 20:01:02

After a `sage -ba` everything is fine on my Desktop.


---

Comment by mabshoff created at 2008-09-07 23:02:01

Resolution: fixed


---

Comment by mabshoff created at 2008-09-07 23:02:01

Merged in Sage 3.1.2.rc1
