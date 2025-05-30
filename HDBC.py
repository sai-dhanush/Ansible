from RBI import RBI

class HDFC(RBI):
    initalBalance=1000
    def giveLoans(self):
        print("HDFC Provide loans")
    def depositAmount(self):
        return super().depositAmount()
    def checkBalanace(self):
        return 'hi'
    def withdrawAmount(self):
        amt=int(input('Enter Amount to withdraw '))
        self.initalBalance -= amt
        if self.initalBalance>0:
            print("Remaining balance",self.initalBalance )
        else:
            print("Amount cannot be withdrawn more than 1000")


hdfc=HDFC()
hdfc.giveLoans()

print(hdfc.withdrawAmount())