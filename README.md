# beat
2d stack based esolang inspired by befunge/asciidots/length. the pointer starts at one of the symbols below

@ - sets direction to right

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
## commands
note that these commands represent the _order_ of 1's and 0's and the way theyre placed depends on the direction of the pointer. commands with [arg] require a binary number after them which is separated by a newline aka <>v^. commands with [func] require another function after them

**1 [arg]** - pushes [arg] converted to decimal onto the stack

**10** - pop top value

**11** - get input from the user as a decimal number and push

**100** - get input as a character, get its \<read below> value and push

**101** - output top value (decimal) and pop

**110** - output top value as \<read below> and pop

**111 [func]** - while top value isnt 0, execute the function (it can have [arg]) (might not work properly)

**1000** - convert top value to binary and execute as a function (if its 1 then value below the top value is the arg)

**1001 [func]** - if top value is 0, skips [func]

**1010** - duplicates top value of the stack

**1011** - reverses the order of the stack

**1100** - if top two value on the stack are equal pushes 1, otherwise pushes 0

**1101** - same as **101** but doesnt pop

**1110** - same as **110** but doesnt pop

**1111** - ends the program

## epic ascii ripoff
this is basically like ascii but with different characters and values. used in **100** and **110**

1  -       1 - \n

2  -	     10 - space

3  -      11 - A

4  -     100 - B

5  -     101 - C

6  -     110 - D

7  -     111 - E

8  -    1000 - F

9  -    1001 - G

10 -    1010 - H

11 -    1011 - I

12 -    1100 - J

13 -    1101 - K

14 -    1110 - L

15 -    1111 - M

16 -   10000 - N

17 -   10001 - O

18 -   10010 - P

19 -   10011 - Q

20 -   10100 - R

21 -   10101 - S

22 -   10110 - T

23 -   10111 - U

24 -   11000 - V

25 -   11001 - W

26 -   11010 - X

27 -   11011 - Y

28 -   11100 - Z

29 -   11101 - a

30 -   11110 - b

31 -   11111 - c

32 -  100000 - d

33 -  100001 - e

34 -  100010 - f

35 -  100011 - g

36 -  100100 - h

37 -  100101 - i

38 -  100110 - j

39 -  100111 - k

40 -  101000 - l

41 -  101001 - m

42 -  101010 - n

43 -  101011 - o

44 -  101100 - p

45 -  101101 - q

46 -  101110 - r

47 -  101111 - s

48 -  110000 - t

49 -  110001 - u

50 -  110010 - v

51 -  110011 - w

52 -  110100 - x

53 -  110101 - y

54 -  110110 - z

55 -  110111 - 0

56 -  111000 - 1

57 -  111001 - 2

58 -  111010 - 3

59 -  111011 - 4

60 -  111100 - 5

61 -  111101 - 6

62 -  111110 - 7

63 -  111111 - 8

64 - 1000000 - 9

65 - 1000001 - .

66 - 1000010 - ,

67 - 1000011 - !

68 - 1000100 - ?

69 - 1000101 - :

70 - 1000110 - ;

71 - 1000111 - '

72 - 1001000 - "

73 - 1001001 - (

74 - 1001010 - )

75 - 1001011 - \[

76 - 1001100 - ]

77 - 1001101 - {

78 - 1001110 - }

79 - 1001111 - \<

80 - 1010000 - >

81 - 1010001 - _

82 - 1010010 - @

83 - 1010011 - #

84 - 1010100 - $

85 - 1010101 - &

86 - 1010110 - %

87 - 1010111 - ^

88 - 1011000 - /

89 - 1011001 - \\

90 - 1011010 - +

91 - 1011011 - -

92 - 1011100 - *

93 - 1011101 - =

94 - 1011110 - |

95 - 1011111 - ~

96 - 1100000 - \`

97 - 1100001 - °

98 - 1100010 - tab
