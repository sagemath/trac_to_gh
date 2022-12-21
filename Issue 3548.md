# Issue 3548: bug in Permutation creation from a string

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-04 00:25:45

Assignee: joyner

This sucks:

```
sage: Permutation( '(4,5)' )
IndexError: list assignment index out of range
```


See below for more details. 


```
On Thu, Jul 3, 2008 at 10:50 AM, John Cremona <> wrote:
>
> I would still say that this is a bug, since the following does work:
> sage: Permutation('(1)(2)(3)(4,5)')
> [1, 2, 3, 5, 4]
> and the docstring says the Permutation can be given a string in cycle
> notation, and 1-cycles are usually omitted.  Looking at the code
> (Permutation??) the error is in the call to from_cycles where the
> first parameter n is computed as the sum of the lengths of the cycles
> input instead of the maximum integer input.
>
> John Cremona
>
> 2008/7/3 Pierre <>:
>>
>> hi all,
>>
>> I'm confused with the cycle notation for permutations (bug ?)
>> While the following works:
>>
>> sage: Permutation( '(1,2)' )
>>
>> the following yields an error:
>>
>> sage: Permutation( '(4,5)' )
>> IndexError: list assignment index out of range
>>
>> What's confusing is that if you go:
>>
>> sage: x= Permutation( (4,5) )
>> sage: s= x.cycle_string(); s
>> '(4,5)'
>>
>> I'm trying to build a dictionnary whose keys are permutations; since
>> the keys have to be hashable, i'm relying on the cycle_string()
>> strings. But the above issue prevents me from recovering a permutation
>> from its string !
>>
>> Is there a way around this ?
>>
>> thanks
>> pierre


```



---

Attachment


---

Comment by cremona created at 2008-07-04 22:09:44

The attached patch (based on 3.0.4.alpha0) fixes this and adds some relevant doctests.


```
sage: p = Permutation( '(4,5)' ); p
[1, 2, 3, 5, 4]
sage: p2 = Permutation( '(4,5)(10)' ); p2
[1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
```



---

Comment by rlm created at 2008-07-05 19:42:05

+1


---

Comment by mabshoff created at 2008-07-05 22:44:00

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-05 22:44:00

Resolution: fixed
