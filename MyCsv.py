"""
MyCsv.py
"""

import os
import csv


"""
-MyCsvFile-
    Classe personale per una gestione semplificata dei File CSV
    Attributi:
        path        - indirizzo directory del file
        name        - nome del file
        fields      - campi di testata del file
        rows        - lista di righe del file
        delimiter   - delimitatore scelto per il Csv
        quotechar   - char di quotatura scelto per il Csv
        error       - classe di errore
"""
class MyCsvFile:
    """
    Inizializzazione di tutte le variabili di classe
    """
    def __init__(self):
        self.path=""
        self.name=""
        self.fields=[]
        self.rows=[]
        self.delimiter=","
        self.quotechar='"'
        self.error=0

    """
    Restituisce in forma di stringa una fotografia della classe in quel momento
    utile in fase di controllo
    """
    def __str__(self):
        string=f"Istance of MyCsvFile:\npath={self.path}\nname={self.name}\nfields={self.fields}\nrows={self.rows}\ndelimiter={self.delimiter}\nquotechar={self.quotechar}\nerror={self.error}"
        return string
    """
    Compara i fields con la prima riga del reader assicurarsi che sia il csv adatto
    """
    def IsMyCsvFile(self,reader,fields):
        try:
            """Leggi la prima riga e compara con fields"""
            first_row=next(reader)
            if first_row==fields:
                return True
            else:
                raise MyCsvError()
        except Exception as this_error:
            self.error=type(this_error).__name__
            return False
    """
    Controlla il file obj se è un Csv corretto
    """
    def IsCsvFile(self,file):
        try:
            sample=file.read(1024)
            """Check di presenza di char non stampabili"""
            #if not all([c in string.printable or c.isprintable() for c in tab]):
            #raise MyCsvError()
            """Check presenza di dialetto"""
            dialect = csv.Sniffer().sniff(sample)
            file.seek(0)
        except csv.Error as this_error:
            """Cattura l'errore csv.Error: torna falso e assegna l'errore alla variabile di classe"""
            self.error=type(this_error).__name__
            file.seek(0)
            return False
        return True
    """
    Carica il file indicato in fullpath che rispetta i fields specificati.
    Se valido e il caricamento è andato bene ritorna True
    """
    def load(self,fullpath,fields=0):
        try:
            with open(fullpath,'r',newline='') as csvfile:
                if not self.IsCsvFile(csvfile):
                    return False
                reader=csv.reader(csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
                if fields!=0:
                    """Fai il check su fields se valorizzato"""
                    if not self.IsMyCsvFile(reader,fields):
                        return False
                """
                Arrivati qui tutti i check sono positivi quindi
                popola le variabili di classe
                """
                self.path,self.name=os.path.split(fullpath)
                csvfile.seek(0)
                self.fields=next(reader)
                for row in reader:
                    self.rows.append(row)
        except Exception as this_error:
            self.error=type(this_error).__name__
            return False
        #self.error=0
        return True

    """
    Salva il file di name e path
    Se specificato con le nuove righe e testata.
    Ritorna True se il salvataggio è andato bene
    """
    def save(self,newfields=0,newrows=0):
        return True#da fare

    """
    Salva il file in fullpath
    Se specificato con le nuove righe e testata.
    Ritorna True se il salvataggio è andato bene
    """
    def saveas(self,fullpath,newfields=0,newrows=0):
        self.path,self.name=os.path.split(fullpath)
        return True#da fare


"""
-MyCsvError-
    Classe personale per una gestione semplificata di Errori in MyCsv
    derivata da Exception per File non supportato
"""
class MyCsvError(Exception):
    def __init__(self,message="File non supportato!"):
        super().__init__(message)

    def __str__(self):
        return super().__str__()

class File:
    def __init__(self):
        self.New()
        self.fields=['"NOME"', '"Val1"', '"Val2"', '"Val3"', '"Val4"', '"Val5"',
                '"Val6"', '"Val7"', '"Val8"', '"Val9"', '"Val10"', '"Val11"',
                '"Val16"', '"Val17"', '"Val18"', '"Val19"', '"Val20"', '"Val21"',
                '"Val22"', '"Val23"', '"Val24"', '"Val25"\n']
    def New(self):
        self.path=""
        self.name="Nuovo"
        self.recipe=[]
        self.recipe.append([0,'Nuovo Programma di taglio', '', '', '', '', '',
                '', '', '', '', '', '',
                '', '', '', '', '', '',
                '', '', '', ''])
    def Load(self):
        #aggiungere controlli validità file
        path=filedialog.askopenfilename(initialdir = "/",title = "Open file")
        file=open(path)
        recipe=[]
        fields=file.readline().split(",")
        #print(fields)
        i=0
        if fields == self.fields:
            for x in file:
                # RIMUOVE \N
                x=x.strip()
                # RIMUOVE "
                x=x.replace('"','')
                # SEPARA PER ,
                x=x.split(",")
                # INSERISCI INDICE NUMERICO
                x.insert(0,i)
                recipe.append(x)
                #print(recipe[i])
                i+=1
            file.close()
            self.path,self.name=os.path.split(path)
            self.recipe=recipe
            return True
        else:
            return False

    def Save(self):
        pass

    def SaveAs(self):
        path=filedialog.asksaveasfilename(initialdir = "/",title = "Save as")
