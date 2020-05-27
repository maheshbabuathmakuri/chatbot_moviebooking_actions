## happy path
* greet
  - find_language_types
  - slot{"language":"telugu"}
* inform{"language": "telugu"}
  - find_movie_names
  - slot{"movie_name":"Bahubali"}
* inform{"movie_name":"Bahubali"}
  - find_available_dates
  - slot{"planned_date":"13-05-20"}
* inform{"planned_date":"13-05-20"}
  - find_theater_names
  - slot{"theater_name":"Asian Cinemas"}
* inform{"theater_name":"Asian Cinemas"}
  - find_show_timings
  - slot{"planned_time":"10:00 AM"}
* inform{"planned_time":"10:00 AM"}
  - find_no_of_tickets
  - slot{"no_of_tickets":"5"}
* inform{"no_of_tickets":"5"}
  - ticket_booking_form
  - form{"name": "ticket_booking_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path 1
* inform{"language": "telugu", "movie_name":"Bahubali"}
  - find_available_dates
  - slot{"planned_date":"13-05-20"}
* inform{"planned_date":"13-05-20"}
  - find_theater_names
  - slot{"theater_name":"Asian Cinemas"}
* inform{"theater_name":"Asian Cinemas"}
  - find_show_timings
  - slot{"planned_time":"10:00 AM"}
* inform{"planned_time":"10:00 AM"}
  - find_no_of_tickets
  - slot{"no_of_tickets":"5"}
* inform{"no_of_tickets":"5"}
  - ticket_booking_form
  - form{"name": "ticket_booking_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
