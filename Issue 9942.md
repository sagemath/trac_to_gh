# Issue 9942: ECL is linkin to two libraries it does not need to (at least on OpenSolaris anyway)

archive/issues_009942.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  dimpase\n\nhttp://blogs.sun.com/rie/entry/tt_dependencies_tt_define_what\n\nshows a way of finding out any libraries that executables link to, where there are no references to what's in the library. \n\nECL would appear to have 3 in the current version of Sage, though it is reduced to 2 in the latest `git` snapshot of ECL I downloaded yesterday:\n\n\n```\ndrkirkby@hawk:~/ecl$ ldd -u -r ./build/bin/ecl\n\tlibecl.so =>\t (file not found)\n\tlibdl.so.1 =>\t /lib/libdl.so.1\n\tlibm.so.2 =>\t /lib/libm.so.2\n\tlibsocket.so.1 =>\t /lib/libsocket.so.1\n\tlibnsl.so.1 =>\t /lib/libnsl.so.1\n\tlibintl.so.1 =>\t /lib/libintl.so.1\n\tlibc.so.1 =>\t /lib/libc.so.1\n\tlibmp.so.2 =>\t /lib/libmp.so.2\n\tlibmd.so.1 =>\t /lib/libmd.so.1\n\tlibscf.so.1 =>\t /lib/libscf.so.1\n\tlibuutil.so.1 =>\t /lib/libuutil.so.1\n\tlibgen.so.1 =>\t /lib/libgen.so.1\n\tlibsmbios.so.1 =>\t /usr/lib/libsmbios.so.1\n\tsymbol not found: cl_env_p\t\t(build/bin/ecl)\n\tsymbol not found: cl_symbols\t\t(build/bin/ecl)\n\tsymbol not found: cl_boot\t\t(build/bin/ecl)\n\tsymbol not found: _ecl_frs_push\t\t(build/bin/ecl)\n\tsymbol not found: read_VV\t\t(build/bin/ecl)\n\tsymbol not found: make_simple_base_string\t\t(build/bin/ecl)\n\tsymbol not found: si_select_package\t\t(build/bin/ecl)\n\tsymbol not found: si_string_to_object\t\t(build/bin/ecl)\n\tsymbol not found: si_safe_eval\t\t(build/bin/ecl)\n\tsymbol not found: si_exit\t\t(build/bin/ecl)\n\n   unused object=/lib/libsocket.so.1\n   unused object=/lib/libintl.so.1\ndrkirkby@hawk:~/ecl$ \n```\n\n\nNote there are two unused libraries:\n\n```\n   unused object=/lib/libsocket.so.1\n   unused object=/lib/libintl.so.1\n```\n\n\nECL should only link to these libraries if it needs them, which I expect it does with some options. There were no options given to configure here. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9943\n\n",
    "created_at": "2010-09-18T20:39:23Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "title": "ECL is linkin to two libraries it does not need to (at least on OpenSolaris anyway)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9942",
    "user": "drkirkby"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9943





---

archive/issue_comments_099000.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9942#issuecomment-99000",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099001.json:
```json
{
    "body": "Outdated spkg or build system ticket, should be closed",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9942#issuecomment-99001",
    "user": "mkoeppe"
}
```

Outdated spkg or build system ticket, should be closed



---

archive/issue_comments_099002.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-10-03T07:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9942#issuecomment-99002",
    "user": "chapoton"
}
```

Resolution: invalid
