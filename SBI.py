from RBI import RBI
class SBI(RBI):
    def giveLoans(self):
        print("SBI Provide loans")
    def depositAmount(self):
        return super().depositAmount()
    def checkBalanace(self):
        return super().checkBalanace()
    def withdrawAmount(self):
        return super().withdrawAmount()

sbi=SBI()
sbi.giveLoans()
sbi.checkBalanace()