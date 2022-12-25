# Issue 1750: Sage 2.10.alpha1: leak in readline.so

archive/issues_001750.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following started popping up after merging numpy 1.0.4 and fixing #1091:\n\n```\n==14077== 3,691 (208 direct, 3,483 indirect) bytes in 1 blocks are definitely lost in loss record 5,815 of 7,694\n==14077==    at 0x4A1AE5E: calloc (vg_replace_malloc.c:391)\n==14077==    by 0x88D9C3F: _nc_setupterm (in /lib/libncurses.so.5.5)\n==14077==    by 0x88DA59E: tgetent (in /lib/libncurses.so.5.5)\n==14077==    by 0x87893AA: _rl_init_terminal_io (terminal.c:452)\n==14077==    by 0x877709E: rl_initialize (readline.c:1027)\n==14077==    by 0x86600D9: initreadline (readline.c:730)\n==14077==    by 0x49E17D: _PyImport_LoadDynamicModule (importdl.c:53)\n==14077==    by 0x49C08D: import_submodule (import.c:2394)\n==14077==    by 0x49C58E: load_next (import.c:2218)\n==14077==    by 0x49C773: import_module_level (import.c:1995)\n==14077==    by 0x49CBF4: PyImport_ImportModuleLevel (import.c:2066)\n==14077==    by 0x47BEE8: builtin___import__ (bltinmodule.c:47)\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1750\n\n",
    "created_at": "2008-01-10T19:39:18Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 2.10.alpha1: leak in readline.so",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1750",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The following started popping up after merging numpy 1.0.4 and fixing #1091:

```
==14077== 3,691 (208 direct, 3,483 indirect) bytes in 1 blocks are definitely lost in loss record 5,815 of 7,694
==14077==    at 0x4A1AE5E: calloc (vg_replace_malloc.c:391)
==14077==    by 0x88D9C3F: _nc_setupterm (in /lib/libncurses.so.5.5)
==14077==    by 0x88DA59E: tgetent (in /lib/libncurses.so.5.5)
==14077==    by 0x87893AA: _rl_init_terminal_io (terminal.c:452)
==14077==    by 0x877709E: rl_initialize (readline.c:1027)
==14077==    by 0x86600D9: initreadline (readline.c:730)
==14077==    by 0x49E17D: _PyImport_LoadDynamicModule (importdl.c:53)
==14077==    by 0x49C08D: import_submodule (import.c:2394)
==14077==    by 0x49C58E: load_next (import.c:2218)
==14077==    by 0x49C773: import_module_level (import.c:1995)
==14077==    by 0x49CBF4: PyImport_ImportModuleLevel (import.c:2066)
==14077==    by 0x47BEE8: builtin___import__ (bltinmodule.c:47)
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1750





---

archive/issue_comments_011021.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2008-10-26T16:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1750#issuecomment-11021",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: worksforme



---

archive/issue_comments_011022.json:
```json
{
    "body": "I can no longer reproduce this. We upgraded ipyhton as well as numpy mutliple times, so let's open another ticket if this pops up again.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T16:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1750#issuecomment-11022",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I can no longer reproduce this. We upgraded ipyhton as well as numpy mutliple times, so let's open another ticket if this pops up again.

Cheers,

Michael
