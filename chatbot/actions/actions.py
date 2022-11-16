# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

import traceback
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import spacy
import pickle
import os

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

pkl_name = 'spacymap.pkl'
with open(pkl_name, 'rb') as f:
    entity_map = pickle.load(f)

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        userMessage = tracker.latest_message['text']
        print(userMessage)
        ent_str = None
        entitytypes = ['PERSON', 'GPE', 'ORG', 'EVENT', 'LOC', 'NORP', 'PRODUCT']
        for etype in entitytypes:
            ent_str = next( tracker.get_latest_entity_values(etype), None)
            if ent_str:
                break
        if ent_str is None:
            dispatcher.utter_message(text="Sorry, I couldn't find an article about that. (Couldn't parse entity.)")
        elif ent_str not in entity_map.keys():
            dispatcher.utter_message(text="Sorry, I couldn't find an article about that.")
            dispatcher.utter_message(text="Looked for: <" + ent_str + ">.")
        else:
            dispatcher.utter_message(text="Here you go: ")
            dispatcher.utter_message(text="Looked for: <" + ent_str + ">.")
            for article in entity_map[ent_str]:
                dispatcher.utter_message(text=article)

class ActionListEnts(Action):
    def name(self) -> Text:
        return "action_list_ents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(entity_map.keys())