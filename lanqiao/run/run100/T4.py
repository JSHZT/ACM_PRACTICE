class CompressString(object):

    def compress(self, string):
        if  string is None:
            return None
        elif  string == '':
            return ''
        ans = ''
        ch = string[0]
        cnt = 0
        for c in string:
            if c == ch:
                cnt += 1
            else:
                if cnt > 1:
                    ans += ch + str(cnt)
                else:
                    ans += ch
                ch = c
                cnt = 1
        if cnt > 1:
            ans += ch + str(cnt)
        else:
            ans += ch
        return ans if len(ans) < len(string) else string