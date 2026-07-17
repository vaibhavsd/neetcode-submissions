class Solution:
    def simplifyPath(self, path: str) -> str:
        out= path.split('/')
        print(out)
        sol= []
        for i in out:
            if i=='' or i=='.':
                continue
            elif i== '..' and sol:
                sol.pop()
            elif i=='..':
                continue
            else:
                sol.append(i)
        joined= '/'.join(sol)
        print(joined)
        return '/'+ joined