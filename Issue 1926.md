# Issue 1926: [with patch, needs review] fixes for the maple interface

archive/issues_001926.json:
```json
{
    "body": "Assignee: @burcin\n\nAttached patch includes the following fixes:\n\n* Maple uses = as the equality test operator\n* Use . as multiplication operator\n* Print using printf(\"%q\",var)\n* Add code to convert Sage matrices to Maple\n* Add code to convert Sage vectors to Maple\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1926\n\n",
    "created_at": "2008-01-25T13:53:08Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, needs review] fixes for the maple interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1926",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Attached patch includes the following fixes:

* Maple uses = as the equality test operator
* Use . as multiplication operator
* Print using printf("%q",var)
* Add code to convert Sage matrices to Maple
* Add code to convert Sage vectors to Maple


Issue created by migration from https://trac.sagemath.org/ticket/1926





---

archive/issue_comments_012186.json:
```json
{
    "body": "fixes to the maple interface",
    "created_at": "2008-01-25T13:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12186",
    "user": "https://github.com/burcin"
}
```

fixes to the maple interface



---

archive/issue_comments_012187.json:
```json
{
    "body": "Attachment [sage-maple_interface_fixes.patch](tarball://root/attachments/some-uuid/ticket1926/sage-maple_interface_fixes.patch) by @williamstein created at 2008-01-25 13:58:32\n\nThis patch is very good except I don't like:\n\n```\n \t581\t        # everything is supposed to be comparable in Python, so we define \n \t582\t        # the comparison thus when no comparable in interfaced system. \n \t583\t        return -1   \n```\n\nIt would be better to compare something deterministic instead of always return -1, since you want that if a < b then it isn't the case that b < a; however your code will return that a < b *and* b < a, when the two aren't comparable.  Better would be to compare a hash of the string reps of the objects (can maple do that?!) or _something_ deterministic and easy.",
    "created_at": "2008-01-25T13:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12187",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-maple_interface_fixes.patch](tarball://root/attachments/some-uuid/ticket1926/sage-maple_interface_fixes.patch) by @williamstein created at 2008-01-25 13:58:32

This patch is very good except I don't like:

```
 	581	        # everything is supposed to be comparable in Python, so we define 
 	582	        # the comparison thus when no comparable in interfaced system. 
 	583	        return -1   
```

It would be better to compare something deterministic instead of always return -1, since you want that if a < b then it isn't the case that b < a; however your code will return that a < b *and* b < a, when the two aren't comparable.  Better would be to compare a hash of the string reps of the objects (can maple do that?!) or _something_ deterministic and easy.



---

archive/issue_comments_012188.json:
```json
{
    "body": "fixes to the maple interface (new version, fixing __cmp__ problem)",
    "created_at": "2008-01-25T16:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12188",
    "user": "https://github.com/burcin"
}
```

fixes to the maple interface (new version, fixing __cmp__ problem)



---

archive/issue_comments_012189.json:
```json
{
    "body": "Attachment [sage-maple_interface_fixes.2.patch](tarball://root/attachments/some-uuid/ticket1926/sage-maple_interface_fixes.2.patch) by @burcin created at 2008-01-25 16:27:26\n\nReplying to [comment:1 was]:\n> This patch is very good except I don't like:\n\n {{{\n  \t581\t        # everything is supposed to be comparable in Python, so we define \n  \t582\t        # the comparison thus when no comparable in interfaced system. \n \t583\t        return -1   \n }}}\n\nI copied the body of the `__cmp__` function from `sage/interfaces/expect.py`, and this comment came with it. \n\n> It would be better to compare something deterministic instead of always return -1, since you want that if a < b then it isn't the case that b < a; however your code will return that a < b *and* b < a, when the two aren't comparable.  Better would be to compare a hash of the string reps of the objects (can maple do that?!) or _something_ deterministic and easy.   \n\n\nYou're right. This was also a problem with `expect.py`. attachment:sage-maple_interface_fixes.2.patch  changes the offending lines with\n\n``` \nif hash(str(self)) < hash(str(other):\n    return -1\nelse:\n    return 1\n```\n\nHopefully making `__cmp__` behave more like an order relation.",
    "created_at": "2008-01-25T16:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12189",
    "user": "https://github.com/burcin"
}
```

Attachment [sage-maple_interface_fixes.2.patch](tarball://root/attachments/some-uuid/ticket1926/sage-maple_interface_fixes.2.patch) by @burcin created at 2008-01-25 16:27:26

Replying to [comment:1 was]:
> This patch is very good except I don't like:

 {{{
  	581	        # everything is supposed to be comparable in Python, so we define 
  	582	        # the comparison thus when no comparable in interfaced system. 
 	583	        return -1   
 }}}

I copied the body of the `__cmp__` function from `sage/interfaces/expect.py`, and this comment came with it. 

> It would be better to compare something deterministic instead of always return -1, since you want that if a < b then it isn't the case that b < a; however your code will return that a < b *and* b < a, when the two aren't comparable.  Better would be to compare a hash of the string reps of the objects (can maple do that?!) or _something_ deterministic and easy.   


You're right. This was also a problem with `expect.py`. attachment:sage-maple_interface_fixes.2.patch  changes the offending lines with

``` 
if hash(str(self)) < hash(str(other):
    return -1
else:
    return 1
```

Hopefully making `__cmp__` behave more like an order relation.



---

archive/issue_comments_012190.json:
```json
{
    "body": "> I copied the body of the __cmp__ function from sage/interfaces/expect.py, \n> and this comment came with it.\n\n\nI've certainly made the mistake of defining cmp to return -1 always, which \nis very stupid.  If __cmp__ currently does that in expect.py, please open\na ticket about it!\n\n> if hash(str(self)) < hash(str(other):\n>     return -1\n> else:\n>    return 1\n\n\n> Hopefully making __cmp__ behave more like an order relation. \n\n\nI do not like the above cmp (even though I used to write code\nlike that).  Imagine that self or orther is a 1000x1000 matrix,\nsay, which is completely reasonable.  Then the above would\nliterally take a very long time, since it would have to pull that matrix\nback to Sage, etc.   Much better would be to do a comparison\nthat involves a Maple hash function. \n\nWilliam",
    "created_at": "2008-01-25T17:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12190",
    "user": "https://github.com/williamstein"
}
```

> I copied the body of the __cmp__ function from sage/interfaces/expect.py, 
> and this comment came with it.


I've certainly made the mistake of defining cmp to return -1 always, which 
is very stupid.  If __cmp__ currently does that in expect.py, please open
a ticket about it!

> if hash(str(self)) < hash(str(other):
>     return -1
> else:
>    return 1


> Hopefully making __cmp__ behave more like an order relation. 


I do not like the above cmp (even though I used to write code
like that).  Imagine that self or orther is a 1000x1000 matrix,
say, which is completely reasonable.  Then the above would
literally take a very long time, since it would have to pull that matrix
back to Sage, etc.   Much better would be to do a comparison
that involves a Maple hash function. 

William



---

archive/issue_comments_012191.json:
```json
{
    "body": "I've added a patch which changes the hashing of expect elements and adds a special hash method for MapleElements.",
    "created_at": "2008-01-28T01:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12191",
    "user": "https://github.com/mwhansen"
}
```

I've added a patch which changes the hashing of expect elements and adds a special hash method for MapleElements.



---

archive/issue_comments_012192.json:
```json
{
    "body": "Attachment [1926.patch](tarball://root/attachments/some-uuid/ticket1926/1926.patch) by @mwhansen created at 2008-01-28 01:17:15",
    "created_at": "2008-01-28T01:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12192",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1926.patch](tarball://root/attachments/some-uuid/ticket1926/1926.patch) by @mwhansen created at 2008-01-28 01:17:15



---

archive/issue_comments_012193.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-28T02:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12193",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004639.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-28T02:45:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1926#event-4639"
}
```



---

archive/issue_comments_012194.json:
```json
{
    "body": "Merged sage-maple_interface_fixes.2.patch and 1926.patch in Sage 2.10.1.rc2",
    "created_at": "2008-01-28T02:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12194",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-maple_interface_fixes.2.patch and 1926.patch in Sage 2.10.1.rc2



---

archive/issue_comments_012195.json:
```json
{
    "body": "make the doctests optional in sage/interfaces/maple.py",
    "created_at": "2008-01-29T09:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12195",
    "user": "https://github.com/burcin"
}
```

make the doctests optional in sage/interfaces/maple.py



---

archive/issue_comments_012196.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-01-29T09:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12196",
    "user": "https://github.com/burcin"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_012197.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-01-29T09:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12197",
    "user": "https://github.com/burcin"
}
```

Changing status from closed to reopened.



---

archive/issue_events_004640.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2008-01-29T09:16:41Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1926#event-4640"
}
```



---

archive/issue_comments_012198.json:
```json
{
    "body": "Attachment [1926-make_doctests_optional.patch](tarball://root/attachments/some-uuid/ticket1926/1926-make_doctests_optional.patch) by @burcin created at 2008-01-29 09:16:41\n\nattachment:1926-make_doctests_optional.patch needs to be applied to make the new doctests in the maple interface optional.",
    "created_at": "2008-01-29T09:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12198",
    "user": "https://github.com/burcin"
}
```

Attachment [1926-make_doctests_optional.patch](tarball://root/attachments/some-uuid/ticket1926/1926-make_doctests_optional.patch) by @burcin created at 2008-01-29 09:16:41

attachment:1926-make_doctests_optional.patch needs to be applied to make the new doctests in the maple interface optional.



---

archive/issue_comments_012199.json:
```json
{
    "body": "New patch looks good to me.",
    "created_at": "2008-02-01T03:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12199",
    "user": "https://github.com/mwhansen"
}
```

New patch looks good to me.



---

archive/issue_events_004641.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-01T03:48:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1926#event-4641"
}
```



---

archive/issue_comments_012200.json:
```json
{
    "body": "Merged 1926-make_doctests_optional.patch in Sahe 2.10.1.rc4",
    "created_at": "2008-02-01T03:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 1926-make_doctests_optional.patch in Sahe 2.10.1.rc4



---

archive/issue_comments_012201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T03:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1926#issuecomment-12201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
