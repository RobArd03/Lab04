import flet as ft
import model as md
import time
import view as View


class SpellChecker:

    def __init__(self, view: View):
        self._view = view
        self._multiDic = md.MultiDictionary()
        self._paroleErrate = "Nessuna parola errata"  # Corretto qui
        self._tempo = 0

    def check(self, e):
        # Salvo il testo inserito dall'utente
        self._txtTrad = self._view._txtIn.value

        # Resetto la casella, la imposto bianca
        self._view._txtIn.value = ""

        # Libero la casella del testo
        self._view._lv.controls.clear()

        # Controllo che il testo inserito non sia vuoto
        if self._txtTrad == "":
            self._view._lv.controls.append(ft.Text("Inserisci una frase da tradurre!!", color="red"))
            self._view.update()
            return

        # Controllo il testo e calcolo degli errori e del tempo di esecuzione
        prov = self.handleSentence(
            self._txtTrad,
            self._view._language.value,
            self._view._modIn.value.lower()
        )

        if prov:  # Fix logico: verifica che 'prov' non sia 'None'
            (self._paroleErrate, self._tempo) = prov  # Corretto qui

        # Metto i valori sotto
        self._view._lv.controls.append(ft.Text(f"Frase Inserita: {self._txtTrad}"  # Corretto qui
                                               f"\nParole Errate: {self._paroleErrate}"  # Corretto qui
                                               f"\nTempo richiesto dalla ricerca: {self._tempo}", color="blue"))
        # Aggiorno la schermata delle stringhe
        self._view.update()

    def handleSentence(self, txtIn, language, modality):
        print(txtIn)
        txtIn = SpellChecker.replaceChars(txtIn.lower())
        words = txtIn.split()
        paroleErrate = " - "
        print(f"{txtIn} {language} {modality}")

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    @staticmethod
    def replaceChars(text=""):
        chars = "`*_{}[]()>#+-.!$?%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text
