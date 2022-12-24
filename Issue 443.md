# Issue 443: libSingular: Source and destination overlap in strcpy

archive/issues_000443.json:
```json
{
    "body": "Assignee: malb\n\nThe following was picked up by valgrind on a x86-64 running Linux (via the new sage -valgrind option - see Ticket #441)\n\n--999-- DWARF2 CFI reader: unhandled CFI instruction 0:10\n--999-- DWARF2 CFI reader: unhandled CFI instruction 0:10\n==999== Source and destination overlap in strcpy(0x7FEFEE210, 0x7FEFEE210)\n==999==    at 0x4A06E47: strcpy (mc_replace_strmem.c:106)\n==999==    by 0x1C4ACEAF: feCleanUpPath(char*) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)\n==999==    by 0x1C4AD8CB: feInitResource(feResourceConfig_s*, int) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)\n==999==    by 0x1C4AE021: feInitResources(char*) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)\n==999==    by 0x1C421768: siInit(char*) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)\n==999==    by 0x1C122AAF: initmulti_polynomial_libsingular (multi_polynomial_libsingular.cpp:1103)\n==999==    by 0x49F3F2: _PyImport_LoadDynamicModule (importdl.c:53)\n==999==    by 0x49D2CE: import_submodule (import.c:2394)\n==999==    by 0x49D7A1: load_next (import.c:2214)\n==999==    by 0x49D9C3: import_module_level (import.c:1995)\n==999==    by 0x49DE34: PyImport_ImportModuleLevel (import.c:2066)\n==999==    by 0x47D268: builtin___import__ (bltinmodule.c:47)\n\nIssue created by migration from https://trac.sagemath.org/ticket/443\n\n",
    "created_at": "2007-08-18T19:33:29Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "libSingular: Source and destination overlap in strcpy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/443",
    "user": "mabshoff"
}
```
Assignee: malb

The following was picked up by valgrind on a x86-64 running Linux (via the new sage -valgrind option - see Ticket #441)

--999-- DWARF2 CFI reader: unhandled CFI instruction 0:10
--999-- DWARF2 CFI reader: unhandled CFI instruction 0:10
==999== Source and destination overlap in strcpy(0x7FEFEE210, 0x7FEFEE210)
==999==    at 0x4A06E47: strcpy (mc_replace_strmem.c:106)
==999==    by 0x1C4ACEAF: feCleanUpPath(char*) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)
==999==    by 0x1C4AD8CB: feInitResource(feResourceConfig_s*, int) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)
==999==    by 0x1C4AE021: feInitResources(char*) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)
==999==    by 0x1C421768: siInit(char*) (in /tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/libsingular.so)
==999==    by 0x1C122AAF: initmulti_polynomial_libsingular (multi_polynomial_libsingular.cpp:1103)
==999==    by 0x49F3F2: _PyImport_LoadDynamicModule (importdl.c:53)
==999==    by 0x49D2CE: import_submodule (import.c:2394)
==999==    by 0x49D7A1: load_next (import.c:2214)
==999==    by 0x49D9C3: import_module_level (import.c:1995)
==999==    by 0x49DE34: PyImport_ImportModuleLevel (import.c:2066)
==999==    by 0x47D268: builtin___import__ (bltinmodule.c:47)

Issue created by migration from https://trac.sagemath.org/ticket/443





---

archive/issue_comments_002213.json:
```json
{
    "body": "I've reported this upstream (Singular).",
    "created_at": "2007-08-19T13:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/443#issuecomment-2213",
    "user": "malb"
}
```

I've reported this upstream (Singular).



---

archive/issue_comments_002214.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-19T13:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/443#issuecomment-2214",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002215.json:
```json
{
    "body": "Should be resolved with the latest singular.spkg by malb.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-29T21:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/443#issuecomment-2215",
    "user": "mabshoff"
}
```

Should be resolved with the latest singular.spkg by malb.

Cheers,

Michael



---

archive/issue_comments_002216.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T23:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/443#issuecomment-2216",
    "user": "was"
}
```

Resolution: fixed
