# 383
## implement function embolden(s,lst)
-   s : string
-   lst :  list of substrings 
## Wraps all substrings in s with html bold tag (b)
## if two bold tags overlap or contiguous , they should be megred
## Example
- s = 'abcdefg' and lst = ['bc' , 'ef'] return a<b>bc</b>d<b>ef</b>g
-  s = 'abcdefg' and lst = ['bcd' , 'def'] return a<b>bcdef</b>g
