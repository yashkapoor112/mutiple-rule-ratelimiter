import json
import logging
from datetime import timedelta

from rest_framework.decorators import api_view, authentication_classes

from kills.accessors.dragon_accessor import DragonAccessor
from kills.accessors.kills_accessor import KillsAccessor
from kills.accessors.rules_accessor import RulesAccessor
from kills.builders.result_builder import ResultBuilder
from kills.helpers import get_or_none, get_datetime_object_from_string, get_difference_between_two_dates
from kills.models import Dragon, Rule
from kills.entity.setters import Setters

logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_dragon(request):
    result_builder = ResultBuilder()
    post_data = request.POST
    dragon_name = post_data.get('dragon_name', None)
    print(post_data)
    print("\n\n")
    if not dragon_name:
        return result_builder.set_fail().set_message("Name of the dragon not provided").get_json_response()

    if get_or_none(Dragon, name=dragon_name):
        return result_builder.set_fail().set_message("A dragon by this name already exists").get_json_response()

    dragon_created = Setters().set_dragon(dragon_name=dragon_name)
    if dragon_created:
        result = { }
        result['id'] = dragon_created.id
        return result_builder.set_success(). \
            set_message("Dragon Registered"). \
            set_results(result).get_json_response()

    return result_builder.set_fail().set_message("Cannot Register Dragon").get_json_response()


@api_view(['POST'])
def add_rule(request):
    result_builder = ResultBuilder()
    post_data = request.POST

    maximum_hours = post_data.get('maximum_hours', None)
    maximum_kills = post_data.get('maximum_kills', None)

    if not (maximum_kills and maximum_hours):
        return result_builder.set_fail().set_message("Necessary parameters missing").get_json_response()

    if get_or_none(Rule, maximum_kills=maximum_kills, maximum_hours=maximum_hours):
        return result_builder.set_fail().set_message("Same Rule already exists").get_json_response()

    rule_created = Setters().set_rule(maximum_kills=maximum_kills, maximum_hours=maximum_hours)
    if rule_created:
        result = { }
        result['id'] = rule_created.id
        return result_builder.set_success(). \
            set_message("Rule created"). \
            set_results(result).get_json_response()

    return result_builder.set_fail().set_message("Cannot create rule").get_json_response()


@api_view(['POST'])
def delete_rule(request):
    result_builder = ResultBuilder()
    post_data = request.POST
    id = post_data.get('id', None)

    if not id:
        return result_builder.set_fail().set_message("No rule id given").get_json_response()

    deleted_rule = RulesAccessor(id=id).delete_rule_by_id()
    if not deleted_rule:
        return result_builder.set_fail().set_message("Invalid id").get_json_response()
    return result_builder.set_success().set_message("Rule deleted").get_json_response()


@api_view(['POST'])
def kill_animal(request):
    result_builder = ResultBuilder()
    post_data = request.POST

    date_time_str = post_data.get('datetime', None)
    number_of_animals_to_be_killed = int(post_data.get('number_of_animals', None))
    dragon_id = post_data.get('dragon_id', None)
    current_timestamp = get_datetime_object_from_string(date_time_str)

    if not (date_time_str and number_of_animals_to_be_killed and dragon_id):
        return result_builder.set_fail().set_message("Necessary parameters missing").get_json_response()

    dragon = DragonAccessor().get_dragon_by_id(dragon_id)
    if not dragon:
        return result_builder.set_fail().set_message("Invalid Name").get_json_response()

    kill_created, message = KillsAccessor(dragon=dragon).set_kill(current_timestamp, number_of_animals_to_be_killed)

    if not kill_created:
        return result_builder.set_fail().set_message(message).get_json_response()
    return result_builder.set_success().set_message(message).get_json_response()
