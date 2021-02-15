class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        p = 0
        max_len = 0
        while p < len(s):
            st = set()
            for c in s[p:]:
                if c in st:
                    break
                st.add(c)
            if len(st) > max_len:
                max_len = len(st)
            # sub_str = list(st)
            # sub_str.sort(key=s.index)
            # print(p, "".join(sub_str))
            p += 1
        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(' '))
