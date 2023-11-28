class Bank:
    def __init__(self):
        self.banknev = []
        self.bankirodak = []

    def add_new_bank(self, bank_nev, location):
        self.banknev.append([bank_nev, location])

    def check_bank_name(self, bank_nev):
        for bank in self.banknev:
            if bank[0] == bank_nev:
                return True
        return False

    def add_bankoffices(self, bank_nev, fiok_nev):
        if self.check_bank_name(bank_nev):
            self.bankirodak.append([bank_nev, fiok_nev])
        else:
            print("A bank nem található. Hozzá akja adni?")
            answer = input("Írjon 'igen'-t vagy 'nem'-et: ")
            if answer == "igen":
                self.add_new_bank(bank_nev, "")
                self.bankirodak.append([bank_nev, fiok_nev])
                print("Sikeresen hozzá adta a bankfiókot.")
            else:
                print("A bankfiók hozzáadása sikertelen volt.")

    def del_bankoffices(self, fiok_nev):
        for bankfiok in self.bankirodak:
            if bankfiok[1] == fiok_nev:
                self.bankirodak.remove(bankfiok)

    def list_bankoffices(self, bank_nev):
        print(bank_nev,"bankfiókjai: ")
        for fiok in self.bankirodak:
            if fiok[0] == bank_nev:
                print(fiok[1])

class Customer:
    def __init__(self):
        self.customer = []

    def last_cust_id(self):
        if len(self.customer) == 0:
            return 0
        else:
            return self.customer[-1][0]

    def add_customer(self, nev, address, bank_nev, fiok_nev):
        self.customer.append([self.last_cust_id() + 1, nev, address, bank_nev, fiok_nev])
    
    def list_customer(self):
        for cust in self.customer:
            print(cust[0], cust[1], cust[2], cust[3], cust[4])

def main():
    bank = Bank()
    customer = Customer()
    
    choice = None

    while choice != str(8):
        print("\nBank Szoftver")
        print("1. Új bank")
        print("2. Új bankfiók")
        print("3. Bankfiókok listája")
        print("4. Bankfiók törlése")
        print("5. Új ügyfél felvétele")
        print("6. Ügyfelek listája")
        print("7. Ügyfél törlése")
        print("8. Kilépés")

        choice = input("Adja meg választott menüpont számát: ")

        if choice == "1":
            bank_nev = input("Adja meg a bank nevét: ")
            location = input("Adja meg a bank helyét: ")
            bank.add_new_bank(bank_nev, location)
            print("Az új bank sikeresen fel lett véve a rendszerbe.")

        elif choice == "2":
            bank_nev = input("Adja meg a bank nevét: ")
            bankfiok_nev = input("Adja meg a bankfiók nevét: ")
            bank.add_bankoffices(bank_nev, bankfiok_nev)
            

        elif choice == "3":
            bank_nev = input("Adja meg a bank nevét: ")
            bank.list_bankoffices(bank_nev)

        elif choice == "4":
            bankfiok_nev = input("Adja meg a bankfiók nevét: ")
            bank.del_bankoffices(bankfiok_nev)
            print("Sikresen kitörölte a bankfiókot.")

        elif choice == "5":
            nev = input("Adja meg az ügyfél nevét: ")
            address = input("Adja meg az ügyfél címét: ")
            bank_nev = input("Adja meg a bank nevét: ")
            bankfiok_nev = input("Adja meg a bankfiók nevét: ")
            customer.add_customer(nev, address, bank_nev, bankfiok_nev)
            print("Sikeresen felvette az új ügyfelet a rendszerhez.")

        elif choice == "6":
            customer.list_customer()

        elif choice == "7":
            cust_id = input("Adja meg az ügyfél azonosítóját: ")
            for cust in customer.customer:
                if cust[0] == int(cust_id):
                    customer.customer.remove(cust)
                    print("Sikeresen eltávolította az ügyfelet.")
                    
            else:
                print("Ügyfél nem található.")

        elif choice == "8":
            print("Kilépés...")

        else:
            print("Érvénytelen válasz. Probáld újra.")

menu= main()
    