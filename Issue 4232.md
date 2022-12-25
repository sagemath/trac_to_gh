# Issue 4232: #249 causes bug in importing large lists

archive/issues_004232.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb alexghitza\n\nTry the following in a sage that contains the patch at #249\n\n\n```\na=[(i,randint(0,100)) for i in range(3000)]                  \nf=open(\"mytest.sage\",'w')                  \nf.write(\"a=[\\n\")                           \nf.writelines([\"%s,\\n\"%str(i) for i in a])  \nf.write(\"(0,0)]\")                          \nf.close()\nload mytest.sage            \n```\n\n\nWithout the patch at #249, the load completes in about a second.  With the patch, I get recursion errors, ending in:\n\n\n```\n/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)\n    811 \n    812 \n--> 813 \n    814 \n    815 \n\n/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)\n    811 \n    812 \n--> 813 \n    814 \n    815 \n\n/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)\n    811 \n    812 \n--> 813 \n    814 \n    815 \n\n/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)\n    678 \n    679 \n--> 680 \n    681 \n    682 \n\n/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in strip_string_literals(code)\n    267 \n    268 \n--> 269 \n    270 \n    271 \n\nRuntimeError: maximum recursion depth exceeded in cmp\n```\n\n\nOne solution is to revert the patch at #249.  Of course, the better is to find the bug and fix it :).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4232\n\n",
    "created_at": "2008-10-01T20:02:22Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "#249 causes bug in importing large lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4232",
    "user": "https://github.com/jasongrout"
}
```
Assignee: somebody

CC:  @robertwb alexghitza

Try the following in a sage that contains the patch at #249


```
a=[(i,randint(0,100)) for i in range(3000)]                  
f=open("mytest.sage",'w')                  
f.write("a=[\n")                           
f.writelines(["%s,\n"%str(i) for i in a])  
f.write("(0,0)]")                          
f.close()
load mytest.sage            
```


Without the patch at #249, the load completes in about a second.  With the patch, I get recursion errors, ending in:


```
/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    811 
    812 
--> 813 
    814 
    815 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    811 
    812 
--> 813 
    814 
    815 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    811 
    812 
--> 813 
    814 
    815 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in preparse(line, reset, do_time, ignore_prompts)
    678 
    679 
--> 680 
    681 
    682 

/home/jason/download/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/misc/preparser.py in strip_string_literals(code)
    267 
    268 
--> 269 
    270 
    271 

RuntimeError: maximum recursion depth exceeded in cmp
```


One solution is to revert the patch at #249.  Of course, the better is to find the bug and fix it :).


Issue created by migration from https://trac.sagemath.org/ticket/4232





---

archive/issue_comments_030696.json:
```json
{
    "body": "This affects sage 3.1.3alpha1 and later.",
    "created_at": "2008-10-01T20:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4232#issuecomment-30696",
    "user": "https://github.com/jasongrout"
}
```

This affects sage 3.1.3alpha1 and later.



---

archive/issue_comments_030697.json:
```json
{
    "body": "Attachment [4232-preparse-long-list.patch](tarball://root/attachments/some-uuid/ticket4232/4232-preparse-long-list.patch) by @robertwb created at 2008-10-01 21:10:32",
    "created_at": "2008-10-01T21:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4232#issuecomment-30697",
    "user": "https://github.com/robertwb"
}
```

Attachment [4232-preparse-long-list.patch](tarball://root/attachments/some-uuid/ticket4232/4232-preparse-long-list.patch) by @robertwb created at 2008-10-01 21:10:32



---

archive/issue_comments_030698.json:
```json
{
    "body": "This patch fixes the bug for me.",
    "created_at": "2008-10-01T23:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4232#issuecomment-30698",
    "user": "https://github.com/jasongrout"
}
```

This patch fixes the bug for me.



---

archive/issue_comments_030699.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-02T01:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4232#issuecomment-30699",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030700.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-02T01:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4232#issuecomment-30700",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha3



---

archive/issue_events_009577.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-02T01:42:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4232",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4232#event-9577"
}
```
