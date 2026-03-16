# Approach 1 (Best for Beginners — Horizontal Checking)

# Idea:

# 1️⃣ Take first string as prefix
# 2️⃣ Compare with next string
# 3️⃣ Reduce prefix until it matches
# 4️⃣ Continue for all strings

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

# Example usage:
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"
