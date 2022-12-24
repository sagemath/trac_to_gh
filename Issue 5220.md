# Issue 5220: Weird or non-appearance of default in input_box in interact

archive/issues_005220.json:
```json
{
    "body": "Assignee: boothby\n\nFrom sage-support:\n\n\n```\nOn sagenb.org, try making an interact with an input box explicitly \ndefined, e.g. \n@interact \ndef plotfunction(f=input_box(x^2)): \n    P=plot(f,0,1) \n    show(P) \nIt works fine in the sense that whatever you type in does what it \nshould.  But what's up with how the input box appears?  It's even \nworse on my box (PPC OSX.4) - the initial input does not show up *at \nall* in the box, though again the plot is fine and once you type \nsomething in it behaves normally. \n```\n\n\n\n\n```\nI'm able to reproduce this on sagenb.org on a Mac with FF3. \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5220\n\n",
    "created_at": "2009-02-09T15:35:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Weird or non-appearance of default in input_box in interact",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5220",
    "user": "kcrisman"
}
```
Assignee: boothby

From sage-support:


```
On sagenb.org, try making an interact with an input box explicitly 
defined, e.g. 
@interact 
def plotfunction(f=input_box(x^2)): 
    P=plot(f,0,1) 
    show(P) 
It works fine in the sense that whatever you type in does what it 
should.  But what's up with how the input box appears?  It's even 
worse on my box (PPC OSX.4) - the initial input does not show up *at 
all* in the box, though again the plot is fine and once you type 
something in it behaves normally. 
```




```
I'm able to reproduce this on sagenb.org on a Mac with FF3. 
```



Issue created by migration from https://trac.sagemath.org/ticket/5220





---

archive/issue_comments_040005.json:
```json
{
    "body": "Behavior seems to be unrelated to #4524, though that is a possibility.  \n\nUsing default=x^2 still creates graph, doesn't put anything in input box.  Using default=\"x^2\" or default='x^2' puts something in input box, but then yields an \"invalid literal for float(): x^2\" error when actually plotting.",
    "created_at": "2009-02-09T16:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40005",
    "user": "kcrisman"
}
```

Behavior seems to be unrelated to #4524, though that is a possibility.  

Using default=x^2 still creates graph, doesn't put anything in input box.  Using default="x^2" or default='x^2' puts something in input box, but then yields an "invalid literal for float(): x^2" error when actually plotting.



---

archive/issue_comments_040006.json:
```json
{
    "body": "Replying to [comment:1 kcrisman]:\n> Behavior seems to be unrelated to #4524, though that is a possibility.  \n> \n> \nUsing \n\n```\ndefault=x^2 \n```\n\nstill creates graph, doesn't put anything in input box.  Using \n\n```\ndefault=\"x^2\"\n```\n\nor\n\n```\ndefault='x^2'\n```\n \nputs something in input box, but then yields an \n\n```\n\"invalid literal for float(): x^2\"\n```\n \nerror when actually plotting.",
    "created_at": "2009-02-09T16:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40006",
    "user": "kcrisman"
}
```

Replying to [comment:1 kcrisman]:
> Behavior seems to be unrelated to #4524, though that is a possibility.  
> 
> 
Using 

```
default=x^2 
```

still creates graph, doesn't put anything in input box.  Using 

```
default="x^2"
```

or

```
default='x^2'
```
 
puts something in input box, but then yields an 

```
"invalid literal for float(): x^2"
```
 
error when actually plotting.



---

archive/issue_comments_040007.json:
```json
{
    "body": "The problem is a str versus repr call in the interact code.  I've attached a patch which fixes the issue, but it changes how interact is needs to be used.  Personally, I think the behavior with the patch should be the correct behavior.",
    "created_at": "2009-02-09T20:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40007",
    "user": "jason"
}
```

The problem is a str versus repr call in the interact code.  I've attached a patch which fixes the issue, but it changes how interact is needs to be used.  Personally, I think the behavior with the patch should be the correct behavior.



---

archive/issue_comments_040008.json:
```json
{
    "body": "Attachment [interact-quote.patch](tarball://root/attachments/some-uuid/ticket5220/interact-quote.patch) by jason created at 2009-02-09 20:22:39\n\nNote that the attached patch changes two other doctests in the affected function.  This should be discussed, as this changes how interacts work, I believe.",
    "created_at": "2009-02-09T20:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40008",
    "user": "jason"
}
```

Attachment [interact-quote.patch](tarball://root/attachments/some-uuid/ticket5220/interact-quote.patch) by jason created at 2009-02-09 20:22:39

Note that the attached patch changes two other doctests in the affected function.  This should be discussed, as this changes how interacts work, I believe.



---

archive/issue_comments_040009.json:
```json
{
    "body": "See the mailing list discussion at http://groups.google.com/group/sage-support/browse_thread/thread/c01b61836bc53339/00cebbec4da5304c for how interact changes after this patch.  Basically, doing:\n\n\n```\n@interact\ndef plotfunction(f=input_box('x^2')):\n     print f \n```\n\n\nused to make an input box with x^2 in it.  Now it literally puts the string 'x^2' (with quote marks) in the input box.  In order to make an input box with x^2 in it after the patch, you need to do:\n\n\n```\n@interact\ndef plotfunction(f=input_box(x^2)):\n     print f \n```\n\n\nor even\n\n\n```\n@interact\ndef plotfunction(f=x^2):\n     print f \n```\n",
    "created_at": "2009-03-05T02:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40009",
    "user": "jason"
}
```

See the mailing list discussion at http://groups.google.com/group/sage-support/browse_thread/thread/c01b61836bc53339/00cebbec4da5304c for how interact changes after this patch.  Basically, doing:


```
@interact
def plotfunction(f=input_box('x^2')):
     print f 
```


used to make an input box with x^2 in it.  Now it literally puts the string 'x^2' (with quote marks) in the input box.  In order to make an input box with x^2 in it after the patch, you need to do:


```
@interact
def plotfunction(f=input_box(x^2)):
     print f 
```


or even


```
@interact
def plotfunction(f=x^2):
     print f 
```




---

archive/issue_comments_040010.json:
```json
{
    "body": "P.S. I can see why having\n\n\n```\n@interact\ndef plotfunction(f=input_box('x^2')):\n     print f \n```\n\n\nproduce x^2 in the input box would be good too, though.  There are lots of types in Sage for which repr does not give you back a string that can be used to reconstruct the object.  For example, I believe that after the patch, \n\n```\n@interact\ndef plotfunction(f=input_box(RIF(3.2,3.4))):\n     print f \n```\n\n\nwill produce an input box that has \"3.3?\" in it (without quotation marks).  Of course, this is nonsense.  For that reason, I can see changing how default values are handled to allow:\n\n\n```\n@interact\ndef plotfunction(f=input_box('RIF(3.2,3.4)')):\n     print f \n```\n\n\nto produce an input box with \"RIF(3.2,3.4)\" (without quotation marks) in it.  This means that to make an input box containing a string (with quotation marks), you'll have to do something like:\n\n\n```\n@interact\ndef plotfunction(f=input_box(\"'my string'\")):\n     print f \n```\n\n(i.e., double-quote your string).",
    "created_at": "2009-03-05T02:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40010",
    "user": "jason"
}
```

P.S. I can see why having


```
@interact
def plotfunction(f=input_box('x^2')):
     print f 
```


produce x^2 in the input box would be good too, though.  There are lots of types in Sage for which repr does not give you back a string that can be used to reconstruct the object.  For example, I believe that after the patch, 

```
@interact
def plotfunction(f=input_box(RIF(3.2,3.4))):
     print f 
```


will produce an input box that has "3.3?" in it (without quotation marks).  Of course, this is nonsense.  For that reason, I can see changing how default values are handled to allow:


```
@interact
def plotfunction(f=input_box('RIF(3.2,3.4)')):
     print f 
```


to produce an input box with "RIF(3.2,3.4)" (without quotation marks) in it.  This means that to make an input box containing a string (with quotation marks), you'll have to do something like:


```
@interact
def plotfunction(f=input_box("'my string'")):
     print f 
```

(i.e., double-quote your string).



---

archive/issue_comments_040011.json:
```json
{
    "body": "Attachment [trac_5220-referee.patch](tarball://root/attachments/some-uuid/ticket5220/trac_5220-referee.patch) by was created at 2009-03-05 05:18:39",
    "created_at": "2009-03-05T05:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40011",
    "user": "was"
}
```

Attachment [trac_5220-referee.patch](tarball://root/attachments/some-uuid/ticket5220/trac_5220-referee.patch) by was created at 2009-03-05 05:18:39



---

archive/issue_comments_040012.json:
```json
{
    "body": "I reviewed the patch, noticed it broke a doctest from #4524, fixed that, and in so doing I think I implemented exactly what Jason suggests above in the comment 3 hours ago.",
    "created_at": "2009-03-05T05:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40012",
    "user": "was"
}
```

I reviewed the patch, noticed it broke a doctest from #4524, fixed that, and in so doing I think I implemented exactly what Jason suggests above in the comment 3 hours ago.



---

archive/issue_comments_040013.json:
```json
{
    "body": "The changes was made look good.  I haven't applied it or tested it, but it's exactly what I was thinking of in my comments above.\n\n\nGee, William, I wish you had a nick that didn't make my grammar look so bad!",
    "created_at": "2009-03-05T05:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40013",
    "user": "jason"
}
```

The changes was made look good.  I haven't applied it or tested it, but it's exactly what I was thinking of in my comments above.


Gee, William, I wish you had a nick that didn't make my grammar look so bad!



---

archive/issue_comments_040014.json:
```json
{
    "body": "Merged both patches in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T06:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40014",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_040015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-08T06:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5220#issuecomment-40015",
    "user": "mabshoff"
}
```

Resolution: fixed
