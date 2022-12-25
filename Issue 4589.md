# Issue 4589: sage/rings/polynomial/multi_polynomial_ideal.py doctest failure due to #4583

archive/issues_004589.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @malb\n\nWith #4583 applied I am seeing the following issue:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0$ ./sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\nsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 58:\n    sage: S.<a,b> = R.quotient((x^2 + y^2, 17))\nExpected nothing\nGot:\n    End Of File (EOF) in read_nonblocking(). Exception style platform.\n    <pexpect.spawn instance at 0x2b0c44965248>\n    version: 2.0 ($Revision: 1.151 $)\n    command: /usr/local/bin/M2\n    args: ['/usr/local/bin/M2', '--no-debug', '--no-readline', '--silent']\n    patterns:\n        i[0-9]* : \n    buffer (last 100 chars): \n    before (last 100 chars): ine 332: /scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/M2: No such file or directory\n    <BLANKLINE>\n    after: <class 'pexpect.EOF'>\n    match: None\n    match_index: None\n    exitstatus: None\n    flag_eof: 1\n    pid: 19482\n    child_fd: 4\n    timeout: 30\n    delimiter: <class 'pexpect.EOF'>\n    logfile: None\n    maxread: 10000\n    searchwindowsize: None\n    delaybeforesend: 0\n    verbose 0 (1790: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 144:\n    sage: I.groebner_basis()\nExpected:\n    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]\nGot:\n    End Of File (EOF) in read_nonblocking(). Exception style platform.\n    <pexpect.spawn instance at 0x2b0c44b007a0>\n    version: 2.0 ($Revision: 1.151 $)\n    command: /usr/local/bin/M2\n    args: ['/usr/local/bin/M2', '--no-debug', '--no-readline', '--silent']\n    patterns:\n        i[0-9]* : \n    buffer (last 100 chars): \n    before (last 100 chars): ine 332: /scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/M2: No such file or directory\n    <BLANKLINE>\n    after: <class 'pexpect.EOF'>\n    match: None\n    match_index: None\n    exitstatus: None\n    flag_eof: 1\n    pid: 19506\n    child_fd: 4\n    timeout: 30\n    delimiter: <class 'pexpect.EOF'>\n    logfile: None\n    maxread: 10000\n    searchwindowsize: None\n    delaybeforesend: 0\n    verbose 0 (1790: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.\n    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]\n**********************************************************************\n1 items had failures:\n   2 of  49 in __main__.example_0\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/tmp/.doctest_multi_polynomial_ideal.py\n\t [11.0 s]\nexit code: 1024\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4589\n\n",
    "created_at": "2008-11-23T02:52:58Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "sage/rings/polynomial/multi_polynomial_ideal.py doctest failure due to #4583",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4589",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @malb

With #4583 applied I am seeing the following issue:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0$ ./sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 58:
    sage: S.<a,b> = R.quotient((x^2 + y^2, 17))
Expected nothing
Got:
    End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x2b0c44965248>
    version: 2.0 ($Revision: 1.151 $)
    command: /usr/local/bin/M2
    args: ['/usr/local/bin/M2', '--no-debug', '--no-readline', '--silent']
    patterns:
        i[0-9]* : 
    buffer (last 100 chars): 
    before (last 100 chars): ine 332: /scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/M2: No such file or directory
    <BLANKLINE>
    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 1
    pid: 19482
    child_fd: 4
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 10000
    searchwindowsize: None
    delaybeforesend: 0
    verbose 0 (1790: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 144:
    sage: I.groebner_basis()
Expected:
    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]
Got:
    End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0x2b0c44b007a0>
    version: 2.0 ($Revision: 1.151 $)
    command: /usr/local/bin/M2
    args: ['/usr/local/bin/M2', '--no-debug', '--no-readline', '--silent']
    patterns:
        i[0-9]* : 
    buffer (last 100 chars): 
    before (last 100 chars): ine 332: /scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/M2: No such file or directory
    <BLANKLINE>
    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 1
    pid: 19506
    child_fd: 4
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 10000
    searchwindowsize: None
    delaybeforesend: 0
    verbose 0 (1790: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.
    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]
**********************************************************************
1 items had failures:
   2 of  49 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/tmp/.doctest_multi_polynomial_ideal.py
	 [11.0 s]
exit code: 1024
```

Issue created by migration from https://trac.sagemath.org/ticket/4589





---

archive/issue_comments_034351.json:
```json
{
    "body": "Attachment [sage-4589.patch](tarball://root/attachments/some-uuid/ticket4589/sage-4589.patch) by @williamstein created at 2008-11-23 03:58:24",
    "created_at": "2008-11-23T03:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4589#issuecomment-34351",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4589.patch](tarball://root/attachments/some-uuid/ticket4589/sage-4589.patch) by @williamstein created at 2008-11-23 03:58:24



---

archive/issue_comments_034352.json:
```json
{
    "body": "Odd, but the hunk\n\n```\n@@ -164,7 +166,7 @@\n\n         sage: I.change_ring(P.change_ring( IntegerModRing(2*7) )).groebner_basis()\n         verbose 0 (...: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.\n-        [x + y + z, y^2 + y + 8, y*z + y + 2, 2*y + 6, z^2 + 3, 2*z + 10]\n+        [x + y + z^3 + z^2 + 11, y^2 + y + 5*z^3 + 2*z^2 + 3*z + 10, y*z + y + 9*z^3 + 5*z^2 + 9*z + 11, 2*y + 2*z^3 + 4*z^2 + 4*z + 8, z^2 + 3, 2*z + 10]\n\n     Modulo any other prime the Groebner basis is trivial so there are\n     no other solutions. For example:\n```\ncauses a doctest failure for me. Thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T04:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4589#issuecomment-34352",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Odd, but the hunk

```
@@ -164,7 +166,7 @@

         sage: I.change_ring(P.change_ring( IntegerModRing(2*7) )).groebner_basis()
         verbose 0 (...: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.
-        [x + y + z, y^2 + y + 8, y*z + y + 2, 2*y + 6, z^2 + 3, 2*z + 10]
+        [x + y + z^3 + z^2 + 11, y^2 + y + 5*z^3 + 2*z^2 + 3*z + 10, y*z + y + 9*z^3 + 5*z^2 + 9*z + 11, 2*y + 2*z^3 + 4*z^2 + 4*z + 8, z^2 + 3, 2*z + 10]

     Modulo any other prime the Groebner basis is trivial so there are
     no other solutions. For example:
```
causes a doctest failure for me. Thoughts?

Cheers,

Michael



---

archive/issue_comments_034353.json:
```json
{
    "body": "```\n[8:45pm] mabshoff: wstein-4591: I am having some trouble with #4589 ?\n[8:45pm] wstein-4591: what trouble.\n[8:45pm] mabshoff: Commented on the ticket.\n[8:45pm] wstein-4591: yes.\n[8:45pm] wstein-4591: it's because you're testing on a machine with m2 installed.\n[8:46pm] wstein-4591: The output is different if you have m2.\n[8:46pm] mabshoff: I thought that was it.\n[8:46pm] wstein-4591: mark the output random, I guess.\n[8:46pm] wstein-4591: dang.\n[8:46pm] wstein-4591: or put in ... for the whole ideal.\n[8:46pm] wstein-4591: [...]\n[8:46pm] mabshoff: It is on sage.math, no m2 there.\n[8:46pm] mabshoff: At least no in $PATH\n[8:46pm] wstein-4591: was@sage:~$ which M2\n[8:46pm] wstein-4591: /usr/local/bin/M2\n[8:46pm] wstein-4591: It's M2\n[8:46pm] mabshoff: shit\n[8:47pm] mabshoff: Case sensitive executable names are just dumb.\n[8:47pm] mabshoff: Then that test should be #optional - m2\n[8:47pm] wstein-4591: but then you would have to change the output back to m2's output.\n[8:47pm] wstein-4591: stupid design.\n[8:47pm] mabshoff: I will open a ticket for that crap since the doctest result should not change with optional packages installed.\n[8:48pm] wstein-4591: true\n[8:48pm] mabshoff: Yep, I am opening a ticket and make the result optional for now.\n[8:48pm] wstein-4591: pok\n[8:48pm] wstein-4591: ok\n```",
    "created_at": "2008-11-23T04:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4589#issuecomment-34353",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
[8:45pm] mabshoff: wstein-4591: I am having some trouble with #4589 ?
[8:45pm] wstein-4591: what trouble.
[8:45pm] mabshoff: Commented on the ticket.
[8:45pm] wstein-4591: yes.
[8:45pm] wstein-4591: it's because you're testing on a machine with m2 installed.
[8:46pm] wstein-4591: The output is different if you have m2.
[8:46pm] mabshoff: I thought that was it.
[8:46pm] wstein-4591: mark the output random, I guess.
[8:46pm] wstein-4591: dang.
[8:46pm] wstein-4591: or put in ... for the whole ideal.
[8:46pm] wstein-4591: [...]
[8:46pm] mabshoff: It is on sage.math, no m2 there.
[8:46pm] mabshoff: At least no in $PATH
[8:46pm] wstein-4591: was@sage:~$ which M2
[8:46pm] wstein-4591: /usr/local/bin/M2
[8:46pm] wstein-4591: It's M2
[8:46pm] mabshoff: shit
[8:47pm] mabshoff: Case sensitive executable names are just dumb.
[8:47pm] mabshoff: Then that test should be #optional - m2
[8:47pm] wstein-4591: but then you would have to change the output back to m2's output.
[8:47pm] wstein-4591: stupid design.
[8:47pm] mabshoff: I will open a ticket for that crap since the doctest result should not change with optional packages installed.
[8:48pm] wstein-4591: true
[8:48pm] mabshoff: Yep, I am opening a ticket and make the result optional for now.
[8:48pm] wstein-4591: pok
[8:48pm] wstein-4591: ok
```



---

archive/issue_comments_034354.json:
```json
{
    "body": "Positive review. I deleted the last hunk from the patch and made that doctest optional for now. The issue with the doctest changing depending on M2 being installed or not will be dealt with at #4593.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T04:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4589#issuecomment-34354",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. I deleted the last hunk from the patch and made that doctest optional for now. The issue with the doctest changing depending on M2 being installed or not will be dealt with at #4593.

Cheers,

Michael



---

archive/issue_events_010439.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-23T05:01:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4589",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4589#event-10439"
}
```



---

archive/issue_comments_034355.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T05:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4589#issuecomment-34355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_034356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T05:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4589#issuecomment-34356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
