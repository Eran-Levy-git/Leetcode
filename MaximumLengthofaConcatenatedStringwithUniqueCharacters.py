class Solution:
    def maxLength(self, arr) -> int:
        """
        Finds the maximum length of a string formed by concatenating a subsequence of
        strings from the given array `arr`, ensuring the resulting string has unique
        characters.

        Args:
            arr (List[str]): The array of strings.

        Returns:
            int: The maximum possible length of the concatenated string with unique characters.
        """

        def backtrack(current_string, current_characters, current_length):
            """
            Recursively explores combinations of strings, starting from the current index,
            keeping track of the current characters and the maximum length encountered.

            Args:
                current_index (int): The index of the current string in the array.
                current_characters (set): A set of characters in the current combination.
                current_length (int): The length of the current combination.

            Returns:
                int: The maximum length found through recursive explorations.
            """

            # Base case: Reached the end of the array
            if current_string == len(arr):
                return current_length

            # Explore two options:

            # Option 1: Skip the current string
            max_length_excluding_current_string = backtrack(
                current_string + 1, current_characters, current_length
            )

            # Option 2: Include the current string (only if its characters are unique)
            new_characters = set(current_characters)
            include_current_string = True
            for char in arr[current_string]:
                if char in new_characters:
                    include_current_string = (
                        False  # Duplicate character found, skip this string
                    )
                    break
                else:
                    new_characters.add(char)

            if include_current_string:
                max_length_including_current_string = backtrack(
                    current_string + 1,
                    new_characters,
                    current_length + len(arr[current_string]),
                )
            else:
                max_length_including_current_string = (
                    0  # Skip this string since it has duplicates
                )

            # Return the maximum length considering both options
            return max(
                max_length_excluding_current_string, max_length_including_current_string
            )

        # Start the backtracking from the beginning with an empty string
        return backtrack(0, set(), 0)


sol = Solution()
print(sol.maxLength(["un", "iq", "ue"]))
"""
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
"""
