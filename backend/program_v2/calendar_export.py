from typing import TextIO

from django.db import models
from django.http import HttpResponse
from ics import Calendar
from ics import Event as CalendarEvent

from graphql_api.language import DEFAULT_LANGUAGE

from .models.program import Program


def export_programs(
    programs: models.QuerySet[Program],
    output_stream: TextIO | HttpResponse,
    language=DEFAULT_LANGUAGE,
):
    calendar = Calendar()
    for program in programs:
        for schedule_item in program.schedule_items.all():
            event = CalendarEvent()
            event.name = schedule_item.title
            event.begin = schedule_item.start_time
            event.end = schedule_item.end_time
            event.description = program.description
            event.location = program.get_location(language)
            calendar.events.add(event)

    output_stream.writelines(calendar.serialize_iter())


def export_program_response(
    programs: models.QuerySet[Program],
    language=DEFAULT_LANGUAGE,
):
    response = HttpResponse(content_type="text/calendar")
    response["Content-Disposition"] = "attachment; filename=program.ics"
    export_programs(programs, response, language=language)
    return response