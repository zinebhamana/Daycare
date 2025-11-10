from interfaces.payable import Payable

class Abonnement(Payable):
    def __init__(self, montant):
        self.montant = montant
        self.etatPaiement = "Non payée"

    def process_payment(self):
        self.etatPaiement = "Payée"

class Donation(Payable):
    def __init__(self, montant, donateur=None):
        self.montant = montant
        self.donateur = donateur
        self.etatPaiement = "Non payée"

    def process_payment(self):
        self.etatPaiement = "Payée"
