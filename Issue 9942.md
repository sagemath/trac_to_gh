# Issue 9942: ECL is linkin to two libraries it does not need to (at least on OpenSolaris anyway)

Issue created by migration from https://trac.sagemath.org/ticket/9943

Original creator: drkirkby

Original creation time: 2010-09-18 20:39:23

Assignee: GeorgSWeber

CC:  dimpase

http://blogs.sun.com/rie/entry/tt_dependencies_tt_define_what

shows a way of finding out any libraries that executables link to, where there are no references to what's in the library. 

ECL would appear to have 3 in the current version of Sage, though it is reduced to 2 in the latest `git` snapshot of ECL I downloaded yesterday:


```
drkirkby@hawk:~/ecl$ ldd -u -r ./build/bin/ecl
	libecl.so =>	 (file not found)
	libdl.so.1 =>	 /lib/libdl.so.1
	libm.so.2 =>	 /lib/libm.so.2
	libsocket.so.1 =>	 /lib/libsocket.so.1
	libnsl.so.1 =>	 /lib/libnsl.so.1
	libintl.so.1 =>	 /lib/libintl.so.1
	libc.so.1 =>	 /lib/libc.so.1
	libmp.so.2 =>	 /lib/libmp.so.2
	libmd.so.1 =>	 /lib/libmd.so.1
	libscf.so.1 =>	 /lib/libscf.so.1
	libuutil.so.1 =>	 /lib/libuutil.so.1
	libgen.so.1 =>	 /lib/libgen.so.1
	libsmbios.so.1 =>	 /usr/lib/libsmbios.so.1
	symbol not found: cl_env_p		(build/bin/ecl)
	symbol not found: cl_symbols		(build/bin/ecl)
	symbol not found: cl_boot		(build/bin/ecl)
	symbol not found: _ecl_frs_push		(build/bin/ecl)
	symbol not found: read_VV		(build/bin/ecl)
	symbol not found: make_simple_base_string		(build/bin/ecl)
	symbol not found: si_select_package		(build/bin/ecl)
	symbol not found: si_string_to_object		(build/bin/ecl)
	symbol not found: si_safe_eval		(build/bin/ecl)
	symbol not found: si_exit		(build/bin/ecl)

   unused object=/lib/libsocket.so.1
   unused object=/lib/libintl.so.1
drkirkby@hawk:~/ecl$ 
```


Note there are two unused libraries:

```
   unused object=/lib/libsocket.so.1
   unused object=/lib/libintl.so.1
```


ECL should only link to these libraries if it needs them, which I expect it does with some options. There were no options given to configure here. 

Dave


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by chapoton created at 2020-10-03 07:29:22

Resolution: invalid
