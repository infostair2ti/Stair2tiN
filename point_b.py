import math
class Complejo:
    def __init__(self,r,i):
        self.r = float(r)
        self.i = float(i)
    
    

class Operation:

    # def law_signs(self,n1,s2):
    #     s1 = "+" if n1 > 0 else  "-"
    #     if s1 == "+" and s2 == "+":
    #         return "+"
    #     elif s1 == "+" and s2 == "-":
    #         return "-"
    #     elif s1 == "-" and s2 == "+":
    #         return "-"
    #     else:
    #         return "+"
    
    def sum(self,A,B):
        return str((A.r + B.r)) + "+" + str((A.i+B.i)) + "i"
    def subtraction(self,A,B):
        im = A.i-B.i
        s = "+" if im > 0 else "-"
        return str((A.r - B.r)) + s+ str(abs(im)) + "i"
        
        
    
    def multiplication(self,A,B):
        t1 = A.r * B.r
        t2 = A.r * B.i
        t3 = A.i * B.r
        t4 = A.i * B.i * -1
        s = "+" if (t2+t3)>0 else "-"
        return str(t1+t4) + s + str(abs(t2+t3)) + "i"

    def division(self,A,B):
        t1 = A.r * B.r
        t2 = A.r * B.i * -1
        t3 = A.i * B.r
        t4 = A.i * B.i * -1 * -1
        t5 = (B.r*B.r) + (B.i*B.i)
        n2 = (t2+t3)/t5
        s = "+" if n2 > 0 else "-"
        return str(round((t1+t4)/t5,2)) + s + str(abs(round(n2,2)))
         

    def mod(self,A):    
        return str(round(math.sqrt(((A.r*A.r)+(A.i*A.i))),2)) + "+0.00i"

if __name__ == "__main__":
    print("Point B")
    A = Complejo(2,1)
    B = Complejo(5,6)
    op = Operation()
    print(op.sum(A,B))
    print(op.subtraction(A,B))
    print(op.multiplication(A,B))
    print(op.division(A,B))
    print(op.mod(A))
    print(op.mod(B))