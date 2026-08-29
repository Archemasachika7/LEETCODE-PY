class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        p = len(s.split())
        pl = s.split()
        d = {}
        m = {}
        if n == p:
            d = {}
        m = {}
        si = False
        ti = False
        if n == p:
            for i in range(n):

                if pattern[i] not in d.keys():
                    d[pattern[i]] = pl[i]
                    si = True
                elif pattern[i] in d.keys():

                    if d[pattern[i]] == pl[i]:
                        si = True

                    else:
                        si = False
                        break
                if pl[i] not in m.keys():
                    m[pl[i]] = pattern[i]
                    ti = True
                elif pl[i] in m.keys():
                    if m[pl[i]] == pattern[i]:
                        ti = True
                    else:
                        ti = False
                        break

            if (si == True) and (ti == True):
                return True
            return False
        return False
