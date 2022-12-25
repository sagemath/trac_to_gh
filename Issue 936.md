# Issue 936: doctest optional doctests

archive/issues_000936.json:
```json
{
    "body": "Assignee: failure\n\nDo \n\n   sage -t --optional SAGE_ROOT/devel/sage\n\nand fix the numerous problems.  This requires a Sage install with all optional packages installed,\nand maple,mathematica,matlab,reduce,etc., all installed.  (I.e., sage.math.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/936\n\n",
    "created_at": "2007-10-20T03:04:59Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "doctest optional doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/936",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

Do 

   sage -t --optional SAGE_ROOT/devel/sage

and fix the numerous problems.  This requires a Sage install with all optional packages installed,
and maple,mathematica,matlab,reduce,etc., all installed.  (I.e., sage.math.)

Issue created by migration from https://trac.sagemath.org/ticket/936





---

archive/issue_comments_005698.json:
```json
{
    "body": "See the file\n\n```\n   /home/was/d/sage/optional.txt\n```\non sage.math",
    "created_at": "2007-10-20T03:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5698",
    "user": "https://github.com/williamstein"
}
```

See the file

```
   /home/was/d/sage/optional.txt
```
on sage.math



---

archive/issue_comments_005699.json:
```json
{
    "body": "fixed issued in permgroup.py",
    "created_at": "2007-10-20T04:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5699",
    "user": "https://github.com/mwhansen"
}
```

fixed issued in permgroup.py



---

archive/issue_comments_005700.json:
```json
{
    "body": "Attachment [permgroup.patch](tarball://root/attachments/some-uuid/ticket936/permgroup.patch) by @mwhansen created at 2007-10-20 04:56:21\n\nThe errors in lie.py come from the new coercion model:\n\n```\nsage: a = lie('2')\nsage: 2*a\nException exceptions.RuntimeError: RuntimeError('An error occured running a LiE command:\\nIdentifier sage5 is not defined. \\n(in <)',) in 'parent._unregister_pair' ignored\nException exceptions.RuntimeError: RuntimeError('An error occured running a LiE command:\\nIdentifier sage5 is not defined. \\n(in <)',) in 'parent._unregister_pair' ignored\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/mhansen/sage/devel/sage-main/sage/geometry/<ipython console> in <module>()\n\n/home/mhansen/sage/devel/sage-main/sage/geometry/element.pyx in element.RingElement.__mul__()\n\n/home/mhansen/sage/devel/sage-main/sage/geometry/coerce.pyx in coerce.CoercionModel_cache_maps.bin_op_c()\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Integer Ring' and 'LiE Interpreter'\nsage: b = lie('2')\nsage: a*b\n4\n```",
    "created_at": "2007-10-20T04:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5700",
    "user": "https://github.com/mwhansen"
}
```

Attachment [permgroup.patch](tarball://root/attachments/some-uuid/ticket936/permgroup.patch) by @mwhansen created at 2007-10-20 04:56:21

The errors in lie.py come from the new coercion model:

```
sage: a = lie('2')
sage: 2*a
Exception exceptions.RuntimeError: RuntimeError('An error occured running a LiE command:\nIdentifier sage5 is not defined. \n(in <)',) in 'parent._unregister_pair' ignored
Exception exceptions.RuntimeError: RuntimeError('An error occured running a LiE command:\nIdentifier sage5 is not defined. \n(in <)',) in 'parent._unregister_pair' ignored
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/mhansen/sage/devel/sage-main/sage/geometry/<ipython console> in <module>()

/home/mhansen/sage/devel/sage-main/sage/geometry/element.pyx in element.RingElement.__mul__()

/home/mhansen/sage/devel/sage-main/sage/geometry/coerce.pyx in coerce.CoercionModel_cache_maps.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Integer Ring' and 'LiE Interpreter'
sage: b = lie('2')
sage: a*b
4
```



---

archive/issue_comments_005701.json:
```json
{
    "body": "All tests pass for me on polytope.py after running 'polymake --reconfigure'",
    "created_at": "2007-10-20T04:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5701",
    "user": "https://github.com/mwhansen"
}
```

All tests pass for me on polytope.py after running 'polymake --reconfigure'



---

archive/issue_comments_005702.json:
```json
{
    "body": "I attached a patch to fix one of the issues with matlab.  The other one is due to the new coercion model:\n\n```\nFile \"matlab.py\", line 38:\n    sage: avg = (a+b+c)/3                    # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mhansen/sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[8]>\", line 1, in <module>\n        avg = (a+b+c)/Integer(3)                    # optional###line 38:\n    sage: avg = (a+b+c)/3                    # optional\n      File \"element.pyx\", line 1486, in element.RingElement.__div__\n      File \"coerce.pyx\", line 271, in coerce.CoercionModel_cache_maps.bin_op_c\n    TypeError: unsupported operand parent(s) for '/': 'Matlab' and 'Integer Ring'\n\n```",
    "created_at": "2007-10-20T05:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5702",
    "user": "https://github.com/mwhansen"
}
```

I attached a patch to fix one of the issues with matlab.  The other one is due to the new coercion model:

```
File "matlab.py", line 38:
    sage: avg = (a+b+c)/3                    # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mhansen/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[8]>", line 1, in <module>
        avg = (a+b+c)/Integer(3)                    # optional###line 38:
    sage: avg = (a+b+c)/3                    # optional
      File "element.pyx", line 1486, in element.RingElement.__div__
      File "coerce.pyx", line 271, in coerce.CoercionModel_cache_maps.bin_op_c
    TypeError: unsupported operand parent(s) for '/': 'Matlab' and 'Integer Ring'

```



---

archive/issue_comments_005703.json:
```json
{
    "body": "Attachment [matlab.patch](tarball://root/attachments/some-uuid/ticket936/matlab.patch) by @mwhansen created at 2007-10-20 05:05:17",
    "created_at": "2007-10-20T05:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5703",
    "user": "https://github.com/mwhansen"
}
```

Attachment [matlab.patch](tarball://root/attachments/some-uuid/ticket936/matlab.patch) by @mwhansen created at 2007-10-20 05:05:17



---

archive/issue_comments_005704.json:
```json
{
    "body": "Patch added for errors in kash.py",
    "created_at": "2007-10-20T05:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5704",
    "user": "https://github.com/mwhansen"
}
```

Patch added for errors in kash.py



---

archive/issue_comments_005705.json:
```json
{
    "body": "Attachment [kash.patch](tarball://root/attachments/some-uuid/ticket936/kash.patch) by @mwhansen created at 2007-10-20 05:30:36\n\nAdded patch for error in remote_file.py .  It's an error in the URL.  The file in question should be moved to a more permanent spot.",
    "created_at": "2007-10-20T05:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5705",
    "user": "https://github.com/mwhansen"
}
```

Attachment [kash.patch](tarball://root/attachments/some-uuid/ticket936/kash.patch) by @mwhansen created at 2007-10-20 05:30:36

Added patch for error in remote_file.py .  It's an error in the URL.  The file in question should be moved to a more permanent spot.



---

archive/issue_comments_005706.json:
```json
{
    "body": "Attachment [remote_file.patch](tarball://root/attachments/some-uuid/ticket936/remote_file.patch) by @mwhansen created at 2007-10-20 05:43:14\n\nAttached patch for number_field.py",
    "created_at": "2007-10-20T05:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5706",
    "user": "https://github.com/mwhansen"
}
```

Attachment [remote_file.patch](tarball://root/attachments/some-uuid/ticket936/remote_file.patch) by @mwhansen created at 2007-10-20 05:43:14

Attached patch for number_field.py



---

archive/issue_comments_005707.json:
```json
{
    "body": "Attachment [number_field.patch](tarball://root/attachments/some-uuid/ticket936/number_field.patch) by @mwhansen created at 2007-10-20 05:43:34",
    "created_at": "2007-10-20T05:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5707",
    "user": "https://github.com/mwhansen"
}
```

Attachment [number_field.patch](tarball://root/attachments/some-uuid/ticket936/number_field.patch) by @mwhansen created at 2007-10-20 05:43:34



---

archive/issue_comments_005708.json:
```json
{
    "body": "Regarding lseries_ell.py,\n\nIt requires that the following commands are run first:\n\n```\nsage: sympow('-new_data 2')\nsage: sympow('-new_data 1d0')\nsage: sympow('-new_data 1d1')\nsage: sympow('-new_data 1d2')\n```\n\nAfter that, these are the following errors:\n\n```\n**********************************************************************\nFile \"lseries_ell.py\", line 158:\n    sage: RR(a)                      # optional\nExpected:\n    2.4922620442736498\nGot:\n    2.49226204427365\n**********************************************************************\nFile \"lseries_ell.py\", line 184:\n    sage: E.Lseries().sympow_derivs(1,16,2)      # optional -- requires precomputing \"sympow('-new_data 2')\"\nExpected:\n    1n0: 3.837774351482055E-01\n    1w0: 3.777214305638848E-01\n    1n1: 3.059997738340522E-01\n    1w1: 3.059997738340524E-01\n    1n2: 1.519054910249753E-01\n    1w2: 1.545605024269432E-01\nGot:\n    'sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details\\nMinimal model of curve  is [0,0,1,-1,0]\\nAt 37: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\\nConductor is 37\\nsp 1: Conductor at 37 is 1+0, root number is 1\\nsp 1: Euler factor at 37 is 1+1*x\\n1st sym power conductor is 37, global root number is -1\\nNT 1d0: 35\\nNT 1d1: 32\\nNT 1d2: 28\\nMaximal number of terms is 35\\nDone with small primes 1049\\nComputed:  1d0  1d1  1d2 \\nChecked out:  1d1 \\n 1n0: 3.837774351482055E-01\\n 1w0: 3.777214305638848E-01\\n 1n1: 3.059997738340522E-01\\n 1w1: 3.059997738340524E-01\\n 1n2: 1.519054910249753E-01\\n 1w2: 1.545605024269432E-01'\n```",
    "created_at": "2007-10-20T06:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5708",
    "user": "https://github.com/mwhansen"
}
```

Regarding lseries_ell.py,

It requires that the following commands are run first:

```
sage: sympow('-new_data 2')
sage: sympow('-new_data 1d0')
sage: sympow('-new_data 1d1')
sage: sympow('-new_data 1d2')
```

After that, these are the following errors:

```
**********************************************************************
File "lseries_ell.py", line 158:
    sage: RR(a)                      # optional
Expected:
    2.4922620442736498
Got:
    2.49226204427365
**********************************************************************
File "lseries_ell.py", line 184:
    sage: E.Lseries().sympow_derivs(1,16,2)      # optional -- requires precomputing "sympow('-new_data 2')"
Expected:
    1n0: 3.837774351482055E-01
    1w0: 3.777214305638848E-01
    1n1: 3.059997738340522E-01
    1w1: 3.059997738340524E-01
    1n2: 1.519054910249753E-01
    1w2: 1.545605024269432E-01
Got:
    'sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details\nMinimal model of curve  is [0,0,1,-1,0]\nAt 37: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nConductor is 37\nsp 1: Conductor at 37 is 1+0, root number is 1\nsp 1: Euler factor at 37 is 1+1*x\n1st sym power conductor is 37, global root number is -1\nNT 1d0: 35\nNT 1d1: 32\nNT 1d2: 28\nMaximal number of terms is 35\nDone with small primes 1049\nComputed:  1d0  1d1  1d2 \nChecked out:  1d1 \n 1n0: 3.837774351482055E-01\n 1w0: 3.777214305638848E-01\n 1n1: 3.059997738340522E-01\n 1w1: 3.059997738340524E-01\n 1n2: 1.519054910249753E-01\n 1w2: 1.545605024269432E-01'
```



---

archive/issue_comments_005709.json:
```json
{
    "body": "Problems with the lie interface fixed -- patch attached.",
    "created_at": "2007-10-20T19:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5709",
    "user": "https://github.com/mwhansen"
}
```

Problems with the lie interface fixed -- patch attached.



---

archive/issue_comments_005710.json:
```json
{
    "body": "Attachment [lie.patch](tarball://root/attachments/some-uuid/ticket936/lie.patch) by @mwhansen created at 2007-10-20 19:36:13",
    "created_at": "2007-10-20T19:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5710",
    "user": "https://github.com/mwhansen"
}
```

Attachment [lie.patch](tarball://root/attachments/some-uuid/ticket936/lie.patch) by @mwhansen created at 2007-10-20 19:36:13



---

archive/issue_comments_005711.json:
```json
{
    "body": "Recap of errors from /home/was/d/sage/optional.txt\n\n* **functions/functions.py**: passes once Octave is installed\n\n* **functions/constants.py**: one error related to precision once Octave is installed\n\n```\n**********************************************************************\nFile \"constants.py\", line 870:\n    sage: m.N(200)                                 # optional\nExpected:\n    2.6854520010653064453097148354817956938203822939944629530511523455572188595371520028011411749318476979951534659052880900828976777164109630517925334832596683818523154213321194996260393285220448194096181                \nGot:\n    2.685452001065306445309714835481795693820382293994462953051152345557218859537152002801141174931847697995153465905288090082897677716410963051792533483259668381852315421332119499626039328522044819409618068664166428930847788062036073705\n```\n\n* **geometry/polytope.py**: passes once 'polymake --reconfigure' is run\n\n* **groups/perm_gps/permgroup.py**: passes once above patch is applied\n\n* **interfaces/lie.py**: passes once above patch is applied\n\n* **interfaces/axiom.py**: cannot install the new axiom spkg to test\n\n* **interfaces/kash.py**: passes once the above patch is applied\n\n* **misc/remote_file.py**: passes once the above patch is applied\n\n* **rings/polynomial/multi_polynomial_ideal.py**: I just get a timeout error. I tried running some of the failed tests manually, and they all looked good.\n\n* **rings/polynomial/multi_polynomial_libsingular.pyx**: should work once 'polymake --reconfigure' is run\n\n* **rings/number_field/number_field.py**: passes once the above patch is applied\n\n* **schemes/elliptic_curves/ec_database.py**: passes once the new elliptic curve database package is installed\n\n* **schemes/elliptic_curves/lseries_ell.py**: see above comment for current status",
    "created_at": "2007-10-20T19:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5711",
    "user": "https://github.com/mwhansen"
}
```

Recap of errors from /home/was/d/sage/optional.txt

* **functions/functions.py**: passes once Octave is installed

* **functions/constants.py**: one error related to precision once Octave is installed

```
**********************************************************************
File "constants.py", line 870:
    sage: m.N(200)                                 # optional
Expected:
    2.6854520010653064453097148354817956938203822939944629530511523455572188595371520028011411749318476979951534659052880900828976777164109630517925334832596683818523154213321194996260393285220448194096181                
Got:
    2.685452001065306445309714835481795693820382293994462953051152345557218859537152002801141174931847697995153465905288090082897677716410963051792533483259668381852315421332119499626039328522044819409618068664166428930847788062036073705
```

* **geometry/polytope.py**: passes once 'polymake --reconfigure' is run

* **groups/perm_gps/permgroup.py**: passes once above patch is applied

* **interfaces/lie.py**: passes once above patch is applied

* **interfaces/axiom.py**: cannot install the new axiom spkg to test

* **interfaces/kash.py**: passes once the above patch is applied

* **misc/remote_file.py**: passes once the above patch is applied

* **rings/polynomial/multi_polynomial_ideal.py**: I just get a timeout error. I tried running some of the failed tests manually, and they all looked good.

* **rings/polynomial/multi_polynomial_libsingular.pyx**: should work once 'polymake --reconfigure' is run

* **rings/number_field/number_field.py**: passes once the above patch is applied

* **schemes/elliptic_curves/ec_database.py**: passes once the new elliptic curve database package is installed

* **schemes/elliptic_curves/lseries_ell.py**: see above comment for current status



---

archive/issue_comments_005712.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T23:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/936#issuecomment-5712",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002576.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T23:38:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/936",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/936#event-2576"
}
```
