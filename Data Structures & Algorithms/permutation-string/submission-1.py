class Solution:
    def getsubstrings(self, subs):
        mlist=[]
        for i in range(0, len(subs)):
            for j in range(i+1, len(subs)+1):
                mlist.append(subs[i:j])
        return mlist

    def getdict(self, mstr):
        mdict= dict()
        for i in mstr:
            if i in mdict.keys():
                mdict[i]+=1
            else:
                mdict[i]=1
        return mdict

    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicts1= self.getdict(s1)
        mlist= self.getsubstrings(s2)
        print(mlist)
        for i in range(len(mlist)):
            if dicts1== self.getdict(mlist[i]):
                print(mlist[i], s1)
                return True
        return False

