# Issue 420: SAGE's optional axiom package doesn't build on os x

archive/issues_000420.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe title says it all. \n\nIssue created by migration from https://trac.sagemath.org/ticket/420\n\n",
    "created_at": "2007-08-10T20:20:28Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "SAGE's optional axiom package doesn't build on os x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/420",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The title says it all. 

Issue created by migration from https://trac.sagemath.org/ticket/420





---

archive/issue_comments_002103.json:
```json
{
    "body": "gcl hasn't been ported to intel macs yet.\nin short no one has created the file \naxiom4sage-0.1/lsp/gcl-2.6.8pre/h/intel-macosx.defs \n, and the file \naxiom4sage-0.1/lsp/gcl-2.6.8pre/h/powerpc-macosx.defs\nwon't do\n\nwhen trying to build, the problem appears when configure has no type to chose from.",
    "created_at": "2007-08-13T08:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/420#issuecomment-2103",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

gcl hasn't been ported to intel macs yet.
in short no one has created the file 
axiom4sage-0.1/lsp/gcl-2.6.8pre/h/intel-macosx.defs 
, and the file 
axiom4sage-0.1/lsp/gcl-2.6.8pre/h/powerpc-macosx.defs
won't do

when trying to build, the problem appears when configure has no type to chose from.



---

archive/issue_comments_002104.json:
```json
{
    "body": "i fixed this on the plane to san diego.  now it works with the *new* aiom package that builds on CLISP.\n\nWilliam",
    "created_at": "2007-08-18T23:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/420#issuecomment-2104",
    "user": "https://github.com/williamstein"
}
```

i fixed this on the plane to san diego.  now it works with the *new* aiom package that builds on CLISP.

William



---

archive/issue_comments_002105.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T23:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/420#issuecomment-2105",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000447.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-08-18T23:36:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/420",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/420#event-447"
}
```
