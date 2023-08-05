class Solution:    
    def optimizescan(self, battcap):
        # Input type: Integer
        # return type: float

        #TODO: Write code below to return a float with the solution to the prompt.
        print(battcap)
        p = battcap/250
        area = (p/2)*(p/2)#(p*p)/2
        area = area-(2*(((p)/4)*((p)/4)))
        return area

        pass 

def main():
    battcap = int(input())

    tc1 = Solution()
    ans = tc1.optimizescan(battcap)
    print("%.2f" % ans)

if __name__ and "__main__":
    main()
