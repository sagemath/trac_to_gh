# Issue 5333: pynac.spkg: Delete old pynac libray during spkg-install

archive/issues_005333.json:
```json
{
    "body": "Assignee: mabshoff\n\nLeft over pynac libraries in $SAGE_LOCAL/lib cause upgrade trouble from some releases. William reported some as well as John Cremona in \n\nhttp://groups.google.com/group/sage-devel/t/d1105e1b1cd3d057\n\nThe fix is trivial, but very important to get into 3.4.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5333\n\n",
    "created_at": "2009-02-21T22:54:28Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "pynac.spkg: Delete old pynac libray during spkg-install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Left over pynac libraries in $SAGE_LOCAL/lib cause upgrade trouble from some releases. William reported some as well as John Cremona in 

http://groups.google.com/group/sage-devel/t/d1105e1b1cd3d057

The fix is trivial, but very important to get into 3.4.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5333





---

archive/issue_comments_041000.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-21T22:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041001.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-26T11:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41001",
    "user": "https://github.com/burcin"
}
```

Resolution: fixed



---

archive/issue_events_005586.json:
```json
{
    "actor": "@burcin",
    "created_at": "2009-02-26T11:10:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5333#event-5586"
}
```



---

archive/issue_comments_041002.json:
```json
{
    "body": "The pynac package already deletes the existing libraries before installing new ones. The errors mentioned on the linked threads were seen because the sage library was not updated properly.\n\nHere are the relevant lines from spkg-install in pynac-0.1.2.spkg, which is included in Sage-3.3:\n\n```\ninstall_pynac()\n{\n    rm ${SAGE_LOCAL}/lib/*ginac*\n    rm ${SAGE_LOCAL}/lib/*pynac*\n    rm -rf ${SAGE_LOCAL}/include/ginac\n    rm -rf ${SAGE_LOCAL}/include/pynac\n    cd ${PYNACDIR}\n    $MAKE install\n    if [ $? -ne 0 ]; then\n        echo \"Error installing pynac.\"\n        exit 1\n    fi\n    cd ${WORKDIR} \n}\n```\n\n\nI suggest resolving this as invalid.",
    "created_at": "2009-02-26T11:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41002",
    "user": "https://github.com/burcin"
}
```

The pynac package already deletes the existing libraries before installing new ones. The errors mentioned on the linked threads were seen because the sage library was not updated properly.

Here are the relevant lines from spkg-install in pynac-0.1.2.spkg, which is included in Sage-3.3:

```
install_pynac()
{
    rm ${SAGE_LOCAL}/lib/*ginac*
    rm ${SAGE_LOCAL}/lib/*pynac*
    rm -rf ${SAGE_LOCAL}/include/ginac
    rm -rf ${SAGE_LOCAL}/include/pynac
    cd ${PYNACDIR}
    $MAKE install
    if [ $? -ne 0 ]; then
        echo "Error installing pynac."
        exit 1
    fi
    cd ${WORKDIR} 
}
```


I suggest resolving this as invalid.



---

archive/issue_comments_041003.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-26T11:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41003",
    "user": "https://github.com/burcin"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_041004.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-26T11:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41004",
    "user": "https://github.com/burcin"
}
```

Changing status from closed to reopened.



---

archive/issue_events_005587.json:
```json
{
    "actor": "@burcin",
    "created_at": "2009-02-26T11:10:38Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5333#event-5587"
}
```



---

archive/issue_comments_041005.json:
```json
{
    "body": "I need to learn how to use trac.",
    "created_at": "2009-02-26T11:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41005",
    "user": "https://github.com/burcin"
}
```

I need to learn how to use trac.



---

archive/issue_comments_041006.json:
```json
{
    "body": "Replying to [comment:3 burcin]:\n> I need to learn how to use trac. \n\n:)\n\nBut you are right -> invalid.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T11:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41006",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 burcin]:
> I need to learn how to use trac. 

:)

But you are right -> invalid.

Cheers,

Michael



---

archive/issue_events_005588.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-26T11:50:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5333#event-5588"
}
```



---

archive/issue_comments_041007.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-02-26T11:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5333#issuecomment-41007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid
