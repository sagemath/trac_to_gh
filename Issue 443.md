# Issue 443: libSingular: Source and destination overlap in strcpy

Issue created by migration from https://trac.sagemath.org/ticket/443

Original creator: mabshoff

Original creation time: 2007-08-18 19:33:29

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


---

Comment by malb created at 2007-08-19 13:56:09

I've reported this upstream (Singular).


---

Comment by malb created at 2007-08-19 13:56:09

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-08-29 21:16:39

Should be resolved with the latest singular.spkg by malb.

Cheers,

Michael


---

Comment by was created at 2007-08-29 23:53:15

Resolution: fixed
