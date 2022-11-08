class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        len_s = len(s)
        longest_palindrome = ""
        for win_start in range(len_s):
            win_end = len_s
            if len(s[win_start:win_end]) <= len(longest_palindrome):
                break
            while win_end > win_start:
                current_window = s[win_start:win_end]
                if len(current_window) > len(longest_palindrome):
                    # check further
                    if current_window == current_window[::-1]:
                        # Palindrome
                        longest_palindrome = current_window
                else:
                    break
                win_end -= 1
        print(longest_palindrome)
        return longest_palindrome

# Solution().longestPalindrome("babad")
st = "cmmrracelnclsbtdmuxtfiyahrvxuwreyorosyqapfpnsntommsujibzwhgugwtvxsdsltiiyymiofbslwbwevmjrsbbssicnxptvwmsmiifypoujftxylpyvirfueagprfyyydxeiftathaygmolkcwoaavmdmjsuwoibtuqoewaexihispsshwnsurjopdwttlzyqdbkypvjsbuidsdnpgklhwfnqdvlffcysnxeywvwvblatmxbflnuykhfhjptenhcxqinomlwalvlezefqybpuepbnymzlruuirpiatqgjgcnfmrlzshauoxuoqopcikogfwpssjdeplytcapmujyvgtfmmolnuadpwblgmcaututcrwsqrlpaaqobjfnhudmsulztbdkxpfejavastxejtpbqfftdtcdhvtpbzfuqcwkxtldtjycreimiujtxudtmokcoebhodbkgkgxjzrgyuqhozqtidltodlkziyofdeszwiobkwesdijxbbagguxvofvtphqxgvidqfkljufgubjmjllxoanbizwtedykwmneaosopynzlzvrlqcmyaahdcagfatlhwtgqxsyxwjhexfiplwtrtydjzrsysrcwszlntwrpgfedhgjzhztffqnjotlfudvczwfkhuwmdzcqgrmfttwaxocohtuscdxwfvhcymjpkqexusdaccw"
Solution().longestPalindrome(st)