# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, Form
import logging
import datetime

#logger = logging.getLogger(__name__)

#REQUESTED_SLOT = "requested_slot"


LANGUAGES = {
    "telugu":
        {
            "name": "telugu",
            "resource": "tl"
        },
    "english":
        {
            "name": "english",
            "resource": "en"
        },
    "hindi":
        {
            "name": "hindi",
            "resource": "hn"
        }
}
        
MOVIES = [{
            "language":"telugu",
            "name": "Bahubali",
            "resource": "movie_id1",
            "theater_names": [{"theater_name":"Asian Cinemas"},
                              {"theater_name":"PVR Icon"},
                              {"theater_name":"GVK"},
                              {"theater_name":"Forum mall"},
                              {"theater_name":"Manjeera Mall"}]
        },
        {
            "language":"telugu",
            "name": "Ala Vaikuntapuramlo",
            "resource": "movie_id2",
            "theater_names": [{"theater_name":"Prasad's Mlutiplex"},
                              {"theater_name":"PVR Cinemas"},
                              {"theater_name":"Gokul Theater"},
                              {"theater_name":"INOX"},
                              {"theater_name":"Carnival Cinemas"}]
        },
        {
            "language":"hindi",
            "name": "Villan",
            "resource": "movie_id3",
            "theater_names": [{"theater_name":"Platinum Movie Time"},
                              {"theater_name":"Asian Shiv Ganga"},
                              {"theater_name":"Sensation theater"}]
        },
        {
            "language":"english",
            "name": "Joker",
            "resource": "movie_id4",
            "theater_names": [{"theater_name":"Sensation Ismonia"},
                              {"theater_name":"Vijetha Theater"},
                              {"theater_name":"Bhujanga Theater"}]
        },
        {
            "language":"hindi",
            "name": "Murder",
            "resource": "movie_id5",
            "theater_names": [{"theater_name":"Carnival Movie Time"},
                              {"theater_name":"Asia Multiplex"},
                              {"theater_name":"PVR"}]
        },
        {
            "language":"english",
            "name": "Noescape",
            "resource": "movie_id6",
            "theater_names": [{"theater_name":"Platinum Movie Time"},
                              {"theater_name":"Asian Shiv Ganga"},
                              {"theater_name":"Sensation theater"}]
        }]

def _resolve_name(languages, resource) ->Text:
    for key, value in languages.items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""
class FindLanguageTypes(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_language_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        
        buttons = []
        for t in LANGUAGES:
            language = LANGUAGES[t]
            payload = "/inform{\"language\": \"" + language.get(
                "name") + "\"}"

            buttons.append(
                {"title": "{}".format(language.get("name").title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_greet", buttons, tracker)
        return []

class FindMovieNames(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_movie_names"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        selected_language = tracker.get_slot("language")
        movies = [m for m in MOVIES if m.get("language") == selected_language]
        for m in movies:
            #language = LANGUAGES[t]
            payload = "/inform{\"movie_name\": \"" + m.get(
                "name") + "\"}"

            buttons.append(
                {"title": "{}".format(m.get("name").title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_select_movie_name", buttons, tracker)
        return []


class FindAvailableDates(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_available_dates"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        availabledates = []
        today = datetime.date.today()
        for i in range(7):
            availabledates.append({"date": str(today + datetime.timedelta(days = i))})

        for date in availabledates:
            #language = LANGUAGES[t]
            payload = "/inform{\"planned_date\": \"" + date.get("date") + "\"}"

            buttons.append(
                {"title": "{}".format(date.get("date")),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_select_planned_date", buttons, tracker)
        return []

class FindTheaterNames(Action):
    """This action class allows to display buttons for theaters to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_theater_names"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        selected_language = tracker.get_slot("language")
        selected_movie_name = tracker.get_slot("movie_name")
        
        theater_names = [m for m in MOVIES if m.get("language") == selected_language and m.get("name") == selected_movie_name]
        theater_names = theater_names[0].get("theater_names")
        for tname in theater_names:
            #language = LANGUAGES[t]
            payload = "/inform{\"theater_name\": \"" + tname.get(
                "theater_name") + "\"}"

            buttons.append(
                {"title": "{}".format(tname.get("theater_name").title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_select_theater_name", buttons, tracker)
        return []

class FindShowTimings(Action):
    """This action class allows to display buttons for Show timings to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_show_timings"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        
        timings = [{"time": "10:00 AM"},
                   {"time": "11:00 AM"},
                   {"time": "12:00 PM"},
                   {"time": "12:30 PM"},
                   {"time": "01:00 PM"},
                   {"time": "02:00 AM"},
                   {"time": "04:00 AM"},
                   {"time": "05:00 PM"},
                   {"time": "07:30 PM"},
                   {"time": "09:00 PM"}]
        
        for time in timings:
            #language = LANGUAGES[t]
            payload = "/inform{\"planned_time\": \"" + time.get(
                "time") + "\"}"

            buttons.append(
                {"title": "{}".format(time.get("time")),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_select_planned_time", buttons, tracker)
        return []


class FindNoOfTickets(Action):
    """This action class allows to display buttons for Show timings to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_no_of_tickets"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        tickets = []
        for i in range(1, 11):
            tickets.append({"ticket": str(i)})
        
        for ticket in tickets:
            payload = "/inform{\"no_of_tickets\": \"" + ticket.get(
                "ticket") + "\"}"

            buttons.append(
                {"title": "{}".format(ticket.get("ticket")),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_select_no_of_tickets", buttons, tracker)
        return []



class TicketBookingForm(FormAction):
    """Collects rewuired details for Movie ticket booking"""

    def name(self):
        return "ticket_booking_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "language", "movie_name", "planned_date", "theater_name", "planned_time", "no_of_tickets"
            ]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_template("utter_booking_status", tracker )
        return []
    
    '''# noinspection PyUnusedLocal
    def request_next_slot(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type: Dict[Text, Any]
    ):
        # type: (...) -> Optional[List[Dict]]
        """Request the next slot and utter template if needed,
            else return None"""

        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                logger.debug("Request next slot '{}'".format(slot))
                if slot == "planned_time":
                    dispatcher.utter_message("customixed slot but you can enter planned time.")
                    return [SlotSet(REQUESTED_SLOT, slot)]
                else:
                    dispatcher.utter_template(
                        "utter_ask_{}".format(slot),
                        tracker,
                        silent_fail=False,
                        **tracker.slots
                    )
                    return [SlotSet(REQUESTED_SLOT, slot)]

        # no more required slots to fill
        return None'''