class ATM:
    def __init__(self,card_Number,pin_Number ) :
        self.card_Number = card_Number
        self.pin_Number = pin_Number
    
    def cashWithDrawl(self):
        print("Cash withDrawed")
    
    def BalanceEnquiry(self):
        print("Enquired")

ata = ATM(1222,300)

print(ata.pin_Number)

ata.cashWithDrawl()
ata.BalanceEnquiry()