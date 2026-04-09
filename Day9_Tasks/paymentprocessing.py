class Payment:
    def process_payment(self):
        print("Processing payment")
class CreditCard(Payment):
    def process_payment(self):
        print("Paid using credit card")
class UPI(Payment):
    def process_payment(self):
        print("Paid using UPI")
class NetBanking(Payment):
    def process_payment(self):
        print("Paid using NetBanking")
payments=[CreditCard(),UPI(),NetBanking()]
for p in payments:
    p.process_payment()
        
       
