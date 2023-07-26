import datetime
import sys
from nltk.stem import SnowballStemmer

stm = SnowballStemmer("french")

class Student:
    all_cins = []

    etude_serie = {
    "Marocain": {
        "SM": {"SMA", "SMB"}, 
        "SE": {"SPC", "SVT", "SA"}, 
        "Economie et gestion": {"Economie", "Gestion"}, 
        "Lettres et SH": {"Lettres", "SH"}, 
        "STE": {"STE"}, "STM": {"STM"},
        "Arts": {"Arts"}
        }, 
    "Français": {
        "Général": {"S", "SE", "L"}, 
        "Technologique": {"STI2D", "STMG"}
        }, 
    "Américain": {"Américain": {"Américain"}},
    "Britannique": {"Britannique": {"Britannique"}}, 
    "Allemand": {"Allemand": {"Allemand"}}, 
    "Espagnol": {"Espagnol": {"Espagnol"}},
    "Canadien": {"Canadien": {"Canadien"}}, 
    "Belge": {"Belge": {"Belge"}}, 
    "Suisse": {"Suisse": {"Suisse"}},
    "Chinois": {"Chinois": {"Chinois"}}, 
    "Japonais": {"Japonais": {"Japonais"}}, 
    "Indien": {"Indien": {"Indien"}}
    }
    # systems = [stm.stem(i) for i in list(etude_serie.keys())]
    # series = [stm.stem(i) for i in list(etude_serie[self.sys_etudes].keys())]
    # options = [stm.stem(i) for i in list(etude_serie[self.sys_etudes][self.serie].keys())]
    



    def __init__(self):
        print("\nBienvenue à l'UIR! ")
        print("Pour nous aider à mieux vous connaitre, veuillez répondre aux questions suivantes: ")
        self.cin = self.get_valid_cin()
        self.nom = self.get_valid_nom()
        self.prenom = self.get_valid_prenom()
        self.birthdate = self.get_valid_birthdate()
        self.sys_etudes = self.get_valid_sys()
        self.serie = self.get_valid_serie()
        self.option = self.get_valid_option()

        Student.all_cins.append(self.cin)

    # etudes_possibles = list(etude_serie.keys())
    # series_possibles = list(etude_serie[self.sys_etudes].keys())
    # options_possibles = list(etude_serie[self.sys_etudes][self.serie])

    def get_valid_cin(self):
        cin = input("N°CIN: ")
        while len(cin) > 8:
            cin = input("Le N°CIN doit contenir au plus 8 caractères. Réessayez: ")
        while not cin[0].isalpha() or not cin[2:].isdigit():
            cin = input("N°CIN invalide. Réessayez: ")
        while cin in Student.all_cins:
            cin = input("Ce numéro est déjà inscrit.")
            sys.exit()
        return cin
    
    def get_valid_birthdate(self):
        while True:
            birthdate = input("Veuillez saisir votre date de naissance: ")

            try:
                birthdate_obj = datetime.datetime.strptime(birthdate, "%d/%m/%Y")
                current_date = datetime.datetime.now()
                age = current_date.year - birthdate_obj.year
                if age < 16:
                    print("Vous devez avoir au moins 16 ans pour candidater.")
                    sys.exit()
                return birthdate
        
            except ValueError:
                print("Date invalide. Veuillez respecter le format format JJ/MM/AAAA.")


    def get_valid_nom(self):
        nom = input("Quel est votre nom? ")
        while not nom.isalpha():
            nom = input("Nom invalide. Veuillez réentrer votre nom: ")
        return nom.upper()
                 
    def get_valid_prenom(self):
        prenom = input("Quel est votre prénom? ")
        while not prenom.isalpha():
            prenom = input("Prénom invalide. Veuillez réentrer votre prénom: ")
        return prenom.capitalize()
    
    def get_valid_sys(self):
        sys = input("Quel est votre système d'études? (Français, marocain, spécifiez si autre): ")
        systems = [stm.stem(i) for i in list(Student.etude_serie.keys())]
        while stm.stem(sys) not in systems:
            sys = input("Ce système est invalide ou n'est pas accepté par l'université, veuillez en saisir un valide (Appuyez sur H pour voir les systèmes acceptés): ")
            if sys.upper() == "H":
                self.get_possibilities()
                self.get_valid_sys()
        return sys.capitalize()
    
    # pour les series, vu qu'on a que fr et marocain de connus, on va utliser encore des lsites pour vérifier les séries, si autre, garder 
    # le même nom que systeme pour l'instant

    def get_valid_serie(self):
        serie = input("Quelle série? (Marocain: sm, se, lettres... Français: géneral, technologique): ")
        series = [stm.stem(i) for i in list(Student.etude_serie[self.sys_etudes].keys())]
        while stm.stem(serie) not in series:
            serie = input("La série que vous avez saisie ne correspond à votre système d'études, veuillez en saisir une autre (Appuyez sur H pour voir les séries acceptées): ")
            if serie.upper() == "H":
                self.get_possibilities(self.sys_etudes)
                self.get_valid_serie()
        return serie
    
    def get_valid_option(self):
        option = input("Quelle option ? (Marocain: SMA, SMB, SP... Français: S, ES, L): ")
        options = [stm.stem(i) for i in list(Student.etude_serie[self.sys_etudes][self.serie])]
        while stm.stem(option) not in options:
            option = input("L'option que vous avez saisie ne correspond pas à votre série, veuillez réessayer (Appuyez sur H pour voir les options acceptées): ")
            if option.upper() == "H":
                self.get_possibilities(self.sys_etudes, self.serie)
                self.get_valid_option()
        return option


# Si le user cherche à voir les systèmes, séries ou options possibles et leur notation
    def get_possibilities(self, syst=None, ser=None):
       
        if syst == None: 
            print("Voici les systèmes d'études acceptés: ", list(Student.etude_serie.keys()))
            syst = input("Vous souhaitez connaître les séries de quel système d'études?(Q pour quitter) : ")
            if syst.upper() == "Q":
                return
            sys_possibles = list(Student.etude_serie[syst.capitalize()].keys())
            print(sys_possibles)
        else:
            sys_possibles = list(Student.etude_serie[self.sys_etudes].keys())
            print(sys_possibles)
        if ser == None:
            ser = input("Vous souhaitez connaître les options de quelle série?(Q pour quitter) : ")
            if ser.upper() == "Q":
                return
            ser_possibles = list(Student.etude_serie[syst.capitalize()][ser])
            print(ser_possibles)
        else:
            ser_possibles = list(Student.etude_serie[syst.capitalize()][ser])
            print(ser_possibles)


    def get_valid_attribute(self, attribute):
        value = input(f"Veuiller saisir votre {attribute}: ")
        while value is None:
            print(f"Il semble que vous avez oublié de préciser votre {attribute}. Veuillez réessayer. ")
            return value
            


# En utilisant lemmatization et stemming de nltk, on peut améliorer l'input du user, le chatbot comprendra par exemple que le user est en sciences
# mathématiques s'il écrit "lettre", "lettres" ou mots similaires, l'input n'a plus besoin d'être correct et on prend en considération l'erreur
# humaine