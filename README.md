# beat
2d stack based esolang inspired by befunge/asciidots/length. the pointer starts at

@ - and sets direction to right

\# - sets direction to down

? - sets direction to left

% - sets direction to up

the raw code is similar to length but functions are determined by binary numbers 1~1111 instead of line length. the numbers are represented by +'s and amount of perpendicular +'s. new lines are <>v^ which also change the direction the pointer is moving in. read below for how other characters work

for example
```
 +
@+++v
    ++
    ++
```
will become this raw code
```
100
11
```
and this
```
 +
@+++v
 + ++
   ++
```
will be
```
101
11
```
so the same "neighbor +" can be shared by multiple +'s, and 2 neighbors is still 1 in raw code

also
```
@+++>++
  ++ +
```
is
```
1110
```
not
```
011
10
```
because if the pointer is on a turn that is the same as the direction its moving in, its not considered a turn; also 0's at the beginning of a number are removed
#### other characters
if the pointer encounters a character other than +<>v^@#%?, it will simply continue moving forward
```
@++dfkjelkfj+
 +
```
is the same as
```
@+++
 +
```
### commands
note that these commands represent the _order_ of 1's and 0's and the way theyre placed depends on the direction of the pointer. commands with [arg] require a binary number after them which is separated by a newline aka <>v^

**1 [arg]** - pushes [arg] converted to decimal onto the stack

**10** - pop top value

**11** - get input from the user as a decimal number and push

**100** - get input as a character, get its \<read below> value and push

**101** - output top value (decimal) and pop

**110** - output top value as \<read below> and pop
