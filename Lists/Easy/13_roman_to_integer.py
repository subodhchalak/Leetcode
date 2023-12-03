"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
 which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is
written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 

Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].


"""



class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtype = 0

        mydict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        mylist = list(s)
        numlist = []
        for item in mylist:
            if item in mydict:
                numlist.append(mydict[item])
            else:
                return rtype

        for num in numlist:
            num_index = numlist.index(num)
            next_num = 0
            if (num_index + 1) < len(numlist):
                next_num = numlist[num_index+1]
                
            if num == 1:
                if next_num == 5:
                    rtype += 4
                    numlist.remove(next_num)
                elif next_num == 10:
                    rtype += 9
                    numlist.remove(next_num)
                else:
                    rtype += num

            elif num == 10:
                if next_num == 50:
                    rtype += 40
                    numlist.remove(next_num)
                elif next_num == 100:
                    rtype += 90
                    numlist.remove(next_num)
                else:
                    rtype += num

            elif num == 100:
                if next_num == 500:
                    rtype += 400
                    numlist.remove(next_num)
                elif next_num == 1000:
                    rtype += 900
                    numlist.remove(next_num)
                else:
                    rtype += num
                    
            else:
                rtype += num

        return rtype



s = "LVIII"
obj = Solution()
print(obj.romanToInt(s))