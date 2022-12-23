# Issue 4746: Bug in srange

Issue created by migration from https://trac.sagemath.org/ticket/4746

Original creator: vgermrk

Original creation time: 2008-12-09 09:42:20

Assignee: cwitty

One can produce almost every (wrong) behavior concerning the endpoint
of the returned list. Here are some examples:



```
sage: srange(0.5,1.1,0.1,include_endpoint=False)
[0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000,
 1.00000000000000,
 1.10000000000000]

sage: srange(0.5,1,0.1,include_endpoint=False)
[0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000]

sage: srange(0.5,0.9,0.1,include_endpoint=False)
[0.500000000000000, 0.600000000000000, 0.700000000000000,
0.800000000000000]

sage: srange(0,1.1,0.1,include_endpoint=True)
[0.000000000000000,
 0.100000000000000,
 0.200000000000000,
 0.300000000000000,
 0.400000000000000,
 0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000,
 1.00000000000000,
 1.10000000000000,
 1.20000000000000]

sage: srange(0,0.2,0.1,include_endpoint=True)
[0.000000000000000, 0.100000000000000, 0.200000000000000]

sage: srange(0,0.3,0.1,include_endpoint=True)
[0.000000000000000, 0.100000000000000, 0.200000000000000]
```


-MRK- 


---

Comment by jason created at 2008-12-09 09:46:43

what if we added a tolerance option, which it would use in comparing the endpoint?  If you were within tolerance of the endpoint, you would compare as equal to the endpoint.


---

Comment by was created at 2008-12-10 00:41:15


```
On Tue, Dec 9, 2008 at 4:25 PM, Robert Bradshaw <robertwb@math.washington.edu> wrote:
>
> On Dec 9, 2008, at 2:00 AM, Jason Grout wrote:
>
>> John Cremona wrote:
>>> I would not expect this to work perfectly with floating point numbers
>>> which are not representable exactly in binary.
>>
>>
>> But we could add some sort of tolerance argument that would allow some
>> sort of user-settable fuzz factor.  Basically, the tolerance setting
>> could be used when comparing with the ending value.
>
> Where would this be set? Whatever default it set, it would seem kind
> of arbitrary.
>
> Perhaps this is a case where it could distinguish between RealLiteral
> and RealNumber.
>

This is not the answer.  Look at this example:

sage: srange(0,1.1,0.1,include_endpoint=True)
[0.000000000000000,
 0.100000000000000,
 0.200000000000000,
 0.300000000000000,
 0.400000000000000,
 0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000,
 1.00000000000000,
 1.10000000000000,
 1.20000000000000]

That's not right no matter what.  The documentation says:
"        Return list of numbers a, a+step, ..., a+k*step,
        where a+k*step < b and a+(k+1)*step > b."
where a,b are the first two inputs.

Thus the implementation of srange is simply buggy because the person (me!) who implemented didn't take proper care of how floating point numbers behave. 

William
```



---

Comment by jhpalmieri created at 2008-12-10 05:22:56

To whoever works on this problem: I would also request that the options 'universe' and 'check' be documented (or removed).  The documentation for 'include_endpoint' should say something like "whether or not to include the right-hand endpoint" or "whether to include 'end' " or something.  (I mean, it's more or less clear that you will include `start` and the issue is whether `end` is included, but this could be phrased better, I think.)

Along these lines, what does 'include_endpoint=True' mean if `start+k*step` is never equal to `end`?  For example, is

```
srange(start=1, end=3.5, step=1, include_endpoint=True)
```

supposed to behave differently from

```
srange(start=1, end=3.5, step=1, include_endpoint=False)
```

My guess is no, but this could be clarified in the documentation.  ("whether to include 'end' if end == start+k*step for some k"?)

Finally, if you want to set a tolerance, would a default value of `step * epsilon` be good, for some choice of epsilon (e.g. 10^-5)?


---

Comment by ronanpaixao created at 2008-12-12 21:42:16

Maybe one could use Numpy's arange() to do the heavy lifting.

The only problem is that coercing it back could impact performance.


---

Comment by robertwb created at 2009-01-23 05:05:45

Numpy's arange suffers from the same difficulties. 


```
sage: numpy.arange(0.5r, 1.1r, .1r)
array([ 0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  1.1])
```



---

Attachment

Better documentation, and hopefully a bit easier to follow.


---

Attachment


---

Attachment

I had to rebase the patch (the added/removed lines are unchanged).  Also, three doctests failed in interact.py; William said in IRC to change the expected results:

```
 Should I just change the expected result?
<wstein> The Got definitely looks more sensible.
 So yes, do change the expected result.
```


Code looks good, all doctests pass.  Positive review.  Apply 4746-srange-rebased.patch and 4746-referee.patch.


---

Comment by mabshoff created at 2009-02-20 07:37:32

Merged 4746-srange-rebased.patch and 4746-referee.patch in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:37:32

Resolution: fixed
