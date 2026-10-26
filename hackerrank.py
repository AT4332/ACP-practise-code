# ============================================================
# HACKERRANK - FIRST 20 PYTHON PRACTICE CHALLENGES
# LEETCODE - FIRST 5 PROBLEMS
# Language: Python

# ==================== HACKERRANK ====================

# Challenge 1: Say Hello, World!
# Statement: Print "Hello, World!" to the output.

def hacker_rank_01():
    print("Hello, World!")


# Challenge 2: Python If-Else
# Statement: Given an integer N, determine whether it is Weird
# or Not Weird according to the problem's conditions.

def hacker_rank_02():
    n = int(input())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# Challenge 3: Arithmetic Operators
# Statement: Given two integers, print their sum, difference,
# and product on separate lines.

def hacker_rank_03():
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)


# Challenge 4: Python Division
# Statement: Given two integers, print integer division
# and floating-point division on separate lines.

def hacker_rank_04():
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)


# Challenge 5: Loops
# Statement: Given an integer N, print the square of every
# integer from 0 to N-1, each on a separate line.

def hacker_rank_05():
    n = int(input())

    for i in range(n):
        print(i * i)


# Challenge 6: Write a Function
# Statement: Determine whether a given year is a leap year.

def hacker_rank_06():
    def is_leap(year):
        return (
            year % 400 == 0
            or (year % 4 == 0 and year % 100 != 0)
        )

    year = int(input())
    print(is_leap(year))


# Challenge 7: Print Function
# Statement: Given N, print the integers from 1 to N
# consecutively without spaces.

def hacker_rank_07():
    n = int(input())
    print("".join(str(i) for i in range(1, n + 1)))


# Challenge 8: List Comprehensions
# Statement: Generate all coordinates [i, j, k] within the
# given ranges, excluding those whose sum equals N.

def hacker_rank_08():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    print(result)


# Challenge 9: Find the Runner-Up Score!
# Statement: Find the second-highest distinct score
# from the given list of scores.

def hacker_rank_09():
    n = int(input())
    scores = list(map(int, input().split()))

    unique_scores = sorted(set(scores), reverse=True)
    print(unique_scores[1])


# Challenge 10: Nested Lists
# Statement: Find the students with the second-lowest
# score and print their names in alphabetical order.

def hacker_rank_10():
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest = sorted({
        score for name, score in students
    })[1]

    for name in sorted(
        name for name, score in students
        if score == second_lowest
    ):
        print(name)


# Challenge 11: Finding the Percentage
# Statement: Store each student's scores and print the
# average score of the requested student to 2 decimal places.

def hacker_rank_11():
    n = int(input())
    students = {}

    for _ in range(n):
        data = input().split()
        students[data[0]] = list(map(float, data[1:]))

    name = input()
    average = sum(students[name]) / len(students[name])

    print(f"{average:.2f}")


# Challenge 12: Lists
# Statement: Perform insert, print, remove, append, sort,
# pop, and reverse operations on a list.

def hacker_rank_12():
    n = int(input())
    result = []

    for _ in range(n):
        command, *args = input().split()
        args = list(map(int, args))

        if command == "insert":
            result.insert(args[0], args[1])
        elif command == "print":
            print(result)
        elif command == "remove":
            result.remove(args[0])
        elif command == "append":
            result.append(args[0])
        elif command == "sort":
            result.sort()
        elif command == "pop":
            result.pop()
        elif command == "reverse":
            result.reverse()


# Challenge 13: Tuples
# Statement: Convert the given integers into a tuple
# and print its hash value.

def hacker_rank_13():
    n = int(input())
    values = tuple(map(int, input().split()))
    print(hash(values))


# Challenge 14: sWAP cASE
# Statement: Convert uppercase letters to lowercase and
# lowercase letters to uppercase.

def hacker_rank_14():
    s = input()
    print(s.swapcase())


# Challenge 15: String Split and Join
# Statement: Split a string by whitespace and join its
# words using hyphens.

def hacker_rank_15():
    line = input()
    print("-".join(line.split()))


# Challenge 16: What's Your Name?
# Statement: Given first and last names, print the required
# greeting message.

def hacker_rank_16():
    first_name = input()
    last_name = input()

    print(
        f"Hello {first_name} {last_name}! "
        "You just delved into python."
    )


# Challenge 17: Mutations
# Statement: Replace the character at the specified
# position in a string.

def hacker_rank_17():
    s = input()
    position, character = input().split()
    position = int(position)

    result = (
        s[:position]
        + character
        + s[position + 1:]
    )

    print(result)


# Challenge 18: Find a String
# Statement: Count how many times a substring appears
# in a string, including overlapping occurrences.

def hacker_rank_18():
    string = input().strip()
    sub_string = input().strip()

    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    print(count)


# Challenge 19: String Validators
# Statement: Check whether a string contains any
# alphanumeric, alphabetical, digit, lowercase, or
# uppercase characters. Print five Boolean results.

def hacker_rank_19():
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# Challenge 20: Text Alignment
# Statement: Print the letter H in the specified
# HackerRank text-art pattern for the given thickness.

def hacker_rank_20():
    thickness = int(input())
    c = "H"

    for i in range(thickness):
        print(
            (c * i).rjust(thickness - 1)
            + c
            + (c * i).ljust(thickness - 1)
        )

    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    for i in range(thickness):
        print(
            (
                (c * (thickness - i - 1)).rjust(thickness)
                + c
                + (c * (thickness - i - 1)).ljust(thickness)
            ).rjust(thickness * 6)
        )


# ==================== LEETCODE ====================

# LeetCode Problem 1: Two Sum
# Statement: Given an integer array nums and an integer
# target, return the indices of two numbers that add up
# to target. Exactly one solution exists.

class LeetCode01:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []


# LeetCode Problem 2: Add Two Numbers
# Statement: Two non-empty linked lists represent two
# non-negative integers in reverse order. Add them and
# return the result as a linked list.
# LeetCode provides the ListNode definition automatically.

class LeetCode02:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


# LeetCode Problem 3: Longest Substring Without Repeating
# Characters
# Statement: Find the length of the longest substring
# containing no repeated characters.

class LeetCode03:
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            longest = max(longest, right - left + 1)

        return longest


# LeetCode Problem 4: Median of Two Sorted Arrays
# Statement: Given two sorted arrays, find their median
# with O(log(min(m, n))) time complexity.

class LeetCode04:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2:
                    return float(max(Aleft, Bleft))

                return (
                    max(Aleft, Bleft)
                    + min(Aright, Bright)
                ) / 2

            elif Aleft > Bright:
                right = i - 1

            else:
                left = i + 1

        return 0.0


# LeetCode Problem 5: Longest Palindromic Substring
# Statement: Return the longest substring that reads
# the same forward and backward.

class LeetCode05:
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        end = 0

        def expand(left, right):
            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):
            left1, right1 = expand(i, i)
            left2, right2 = expand(i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end + 1]


# ============================================================
# HOW TO USE THIS FILE IN VS CODE
#
# 1. Save this file as coding_challenges.py
# 2. Select one HackerRank function to test.
# 3. Add a call at the bottom, for example:
#
#    hacker_rank_01()
#
# 4. Run the file in the VS Code terminal:
#
#    python coding_challenges.py
#
# 5. For LeetCode, submit the relevant class's method on
#    LeetCode. Problem 2 uses LeetCode's built-in ListNode.
# 6. Remove or comment out the test call before switching
#    to another HackerRank challenge.
# ============================================================
