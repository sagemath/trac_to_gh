# Issue 8262: developer's guide: document the variable SAGE_CHECK

archive/issues_008262.json:
```json
{
    "body": "Assignee: mvngu\n\nAs the subject says.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8262\n\n",
    "created_at": "2010-02-14T12:19:48Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "developer's guide: document the variable SAGE_CHECK",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8262",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

As the subject says.

Issue created by migration from https://trac.sagemath.org/ticket/8262





---

archive/issue_comments_072996.json:
```json
{
    "body": "Changing assignee from mvngu to drkirkby.",
    "created_at": "2010-02-14T14:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-72996",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from mvngu to drkirkby.



---

archive/issue_comments_072997.json:
```json
{
    "body": "See also #8263, which aims to document all environment variables. SAGE_CHECK is not the only one which is either undocumented, or poorly documented.",
    "created_at": "2010-02-14T14:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-72997",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

See also #8263, which aims to document all environment variables. SAGE_CHECK is not the only one which is either undocumented, or poorly documented.



---

archive/issue_comments_072998.json:
```json
{
    "body": "Some somewhat related data: `SAGE_LOCAL/bin/sage-spkg` contains\n\n```sh\n    cd $BASEDIR\n    if [ \"$SAGE_CHECK\" != \"\" -a -f spkg-check ]; then\n        echo \"Running the test suite.\"\n        chmod +x spkg-check\n        ./spkg-check\n        if [ $? -ne 0 ]; then\n```\n\nbut\n\n\n```sh\n$ \\ls -1 /home/release/latest/sage-4.3.3/spkg/standard/*.spkg | awk '{print \"tar jxvf \"$0}' > zz\n$ . zz\n$ gr -A3 -B2 spkg-check */spkg-install\nflint-1.5.0.p3/spkg-install-\nflint-1.5.0.p3/spkg-install-if [ \"$SAGE_CHECK\" = \"yes\" ]; then\nflint-1.5.0.p3/spkg-install:    cd ..; ./spkg-check\nflint-1.5.0.p3/spkg-install-fi\n--\nmpfr-2.4.1.p1/spkg-install-# Do not bypass the checks, as some MPFR failures\nmpfr-2.4.1.p1/spkg-install-# have been observed, so MPFR should be carefully tested.\nmpfr-2.4.1.p1/spkg-install:cd ..; ./spkg-check\n--\nmpir-1.2.2.p0/spkg-install-\nmpir-1.2.2.p0/spkg-install-if [ \"$SAGE_CHECK\" = \"yes\" ]; then\nmpir-1.2.2.p0/spkg-install:    cd ..; ./spkg-check\nmpir-1.2.2.p0/spkg-install-fi\n```\n\nIn particular, with `SAGE_CHECK=\"yes\"`, the flint's long-running tests are run twice.",
    "created_at": "2010-03-02T23:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-72998",
    "user": "https://github.com/qed777"
}
```

Some somewhat related data: `SAGE_LOCAL/bin/sage-spkg` contains

```sh
    cd $BASEDIR
    if [ "$SAGE_CHECK" != "" -a -f spkg-check ]; then
        echo "Running the test suite."
        chmod +x spkg-check
        ./spkg-check
        if [ $? -ne 0 ]; then
```

but


```sh
$ \ls -1 /home/release/latest/sage-4.3.3/spkg/standard/*.spkg | awk '{print "tar jxvf "$0}' > zz
$ . zz
$ gr -A3 -B2 spkg-check */spkg-install
flint-1.5.0.p3/spkg-install-
flint-1.5.0.p3/spkg-install-if [ "$SAGE_CHECK" = "yes" ]; then
flint-1.5.0.p3/spkg-install:    cd ..; ./spkg-check
flint-1.5.0.p3/spkg-install-fi
--
mpfr-2.4.1.p1/spkg-install-# Do not bypass the checks, as some MPFR failures
mpfr-2.4.1.p1/spkg-install-# have been observed, so MPFR should be carefully tested.
mpfr-2.4.1.p1/spkg-install:cd ..; ./spkg-check
--
mpir-1.2.2.p0/spkg-install-
mpir-1.2.2.p0/spkg-install-if [ "$SAGE_CHECK" = "yes" ]; then
mpir-1.2.2.p0/spkg-install:    cd ..; ./spkg-check
mpir-1.2.2.p0/spkg-install-fi
```

In particular, with `SAGE_CHECK="yes"`, the flint's long-running tests are run twice.



---

archive/issue_comments_072999.json:
```json
{
    "body": "Can this ticket be closed now?",
    "created_at": "2010-07-16T07:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-72999",
    "user": "https://github.com/rlmill"
}
```

Can this ticket be closed now?



---

archive/issue_comments_073000.json:
```json
{
    "body": "Replying to [comment:3 rlm]:\n> Can this ticket be closed now?\n\nYes, this ticket can be closed. The issue of this ticket has been fixed in #8263. I leave it to the release manager to close the current ticket.",
    "created_at": "2010-07-16T07:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-73000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 rlm]:
> Can this ticket be closed now?

Yes, this ticket can be closed. The issue of this ticket has been fixed in #8263. I leave it to the release manager to close the current ticket.



---

archive/issue_comments_073001.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-16T08:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-73001",
    "user": "https://github.com/rlmill"
}
```

Resolution: duplicate



---

archive/issue_events_008461.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-16T08:03:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8262#event-8461"
}
```



---

archive/issue_comments_073002.json:
```json
{
    "body": "Right. Just wanted a second opinion. Thanks!",
    "created_at": "2010-07-16T08:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-73002",
    "user": "https://github.com/rlmill"
}
```

Right. Just wanted a second opinion. Thanks!



---

archive/issue_comments_073003.json:
```json
{
    "body": "Revisiting [comment:2 the comment above] for Sage 4.5, I get\n\n```sh\n$ \\ls -1 /path/to/sage-4.5/spkg/standard/*.spkg | awk '{print \"tar jxvf \"$0}' > unpackem\n$ . unpackem\n$ egrep -A3 -B2 -i SAGE_CHECK\\|spkg-check */spkg-install\ncliquer-1.2.p5/spkg-install-fi\ncliquer-1.2.p5/spkg-install-\ncliquer-1.2.p5/spkg-install:if [ \"$SAGE_CHECK\" = \"yes\" ]; then\ncliquer-1.2.p5/spkg-install-    echo \"Compiling and running the test cases of cliquer...\"\ncliquer-1.2.p5/spkg-install-\ncliquer-1.2.p5/spkg-install-    make testcases\n--\nmpfr-2.4.2/spkg-install-# Do not bypass the checks, as some MPFR failures\nmpfr-2.4.2/spkg-install-# have been observed, so MPFR should be carefully tested.\nmpfr-2.4.2/spkg-install:cd ..; ./spkg-check\n--\nmpir-1.2.2.p1/spkg-install-fi\nmpir-1.2.2.p1/spkg-install-\nmpir-1.2.2.p1/spkg-install:if [ \"$SAGE_CHECK\" = \"yes\" ]; then\nmpir-1.2.2.p1/spkg-install:    cd ..; ./spkg-check\nmpir-1.2.2.p1/spkg-install-fi\n```\n\nIf no one objects, I can open tickets for MPIR and Cliquer.",
    "created_at": "2010-07-16T21:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-73003",
    "user": "https://github.com/qed777"
}
```

Revisiting [comment:2 the comment above] for Sage 4.5, I get

```sh
$ \ls -1 /path/to/sage-4.5/spkg/standard/*.spkg | awk '{print "tar jxvf "$0}' > unpackem
$ . unpackem
$ egrep -A3 -B2 -i SAGE_CHECK\|spkg-check */spkg-install
cliquer-1.2.p5/spkg-install-fi
cliquer-1.2.p5/spkg-install-
cliquer-1.2.p5/spkg-install:if [ "$SAGE_CHECK" = "yes" ]; then
cliquer-1.2.p5/spkg-install-    echo "Compiling and running the test cases of cliquer..."
cliquer-1.2.p5/spkg-install-
cliquer-1.2.p5/spkg-install-    make testcases
--
mpfr-2.4.2/spkg-install-# Do not bypass the checks, as some MPFR failures
mpfr-2.4.2/spkg-install-# have been observed, so MPFR should be carefully tested.
mpfr-2.4.2/spkg-install:cd ..; ./spkg-check
--
mpir-1.2.2.p1/spkg-install-fi
mpir-1.2.2.p1/spkg-install-
mpir-1.2.2.p1/spkg-install:if [ "$SAGE_CHECK" = "yes" ]; then
mpir-1.2.2.p1/spkg-install:    cd ..; ./spkg-check
mpir-1.2.2.p1/spkg-install-fi
```

If no one objects, I can open tickets for MPIR and Cliquer.



---

archive/issue_comments_073004.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> If no one objects, I can open tickets for MPIR and Cliquer.\n\nThese are now #9522 (MPIR) and #9521 (Cliquer).",
    "created_at": "2010-07-17T01:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8262#issuecomment-73004",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:6 mpatel]:
> If no one objects, I can open tickets for MPIR and Cliquer.

These are now #9522 (MPIR) and #9521 (Cliquer).
