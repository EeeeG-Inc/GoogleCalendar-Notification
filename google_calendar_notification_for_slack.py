from my_google_calendar import MyGoogleCalendar


class GoogleCalendarNotificationForSlack:

    def run(self):
        google_calendar = MyGoogleCalendar()

        for name, calendar_id in google_calendar.config.calendar_ids.items():
            text = google_calendar.get_str_next_schedule(calendar_id, name)

            if text is not None:
                google_calendar.slack_post(text, 'Next Calendar TODO', ':calendar:', None)
                print('Slack Post About GoogleCalendar Done!')


google_calendar_notification_for_slack = GoogleCalendarNotificationForSlack()
google_calendar_notification_for_slack.run()
