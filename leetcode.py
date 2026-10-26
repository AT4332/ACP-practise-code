
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
