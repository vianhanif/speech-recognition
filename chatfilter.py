# -*- coding: utf-8 -*-
from chatterbot.filters import Filter

class ChatFilter(Filter):

    def filter_selection(self, chatterbot, session_id):
        session = chatterbot.conversation_sessions.get(session_id)

        if session.conversation.empty():
            return chatterbot.storage.base_query

        text_of_recent_responses = []

        for statement, response in session.conversation:
            text_of_recent_responses.append(response.text)
            print response.text

        query = chatterbot.storage.base_query.statement_text_not_in(
            text_of_recent_responses
        )
        return query
