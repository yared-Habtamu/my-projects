class Solution(object):
    def sortSentence(self, s):
        x=s.split()
        num=[]
        for i in range(len(x)):
            num.append(int(x[i][-1]))

        n_sorted=sorted(num)
        ans=""
        for n in range(len(n_sorted)):
            for i in range(len(x)):
                if n_sorted[n]==int(x[i][-1]):
                    ans+=" "+x[i][:-1]
                    break

        return ans.strip()
