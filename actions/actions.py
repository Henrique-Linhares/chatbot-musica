from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPedirRecomendacao(Action):
    def name(self) -> Text:
        return "action_pedir_recomendacao"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        genero = tracker.get_slot("genero")

        if not genero:
            dispatcher.utter_message(text="Eu ainda não sei qual gênero você prefere. Pode me dizer um estilo musical?")
            return []

        musicas = self.obter_musicas(genero)

        if musicas:
            dispatcher.utter_message(text=f"Para o gênero {genero.capitalize()}, recomendo: {', '.join(musicas)}")
        else:
            dispatcher.utter_message(template="utter_genero_nao_listado")

        return []

    def obter_musicas(self, genero: Text) -> List[Text]:
        base_musicas = {
            "rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
            "samba": ["Aquarela do Brasil", "Garota de Ipanema", "Mas que nada"],
            "sertanejo": ["Evidências", "Ai Se Eu Te Pego", "Fio de Cabelo"],
            "pop": ["Shape of You", "Uptown Funk", "Blinding Lights"],
            "rap": ["Lose Yourself", "N.Y. State of Mind", "Juicy"],
            "trap": ["Sicko Mode", "Mo Bamba", "The Box"],
            "gospel": ["Amazing Grace", "How Great Is Our God", "10,000 Reasons"],
            "classica": ["Sinfonia No. 5", "Moonlight Sonata", "Für Elise"],
            "eletronica": ["Strobe", "Levels", "One More Time"]
        }

        return base_musicas.get(genero.lower(), [])