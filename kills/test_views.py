import requests
import json
from datetime import date, timedelta
import pytest
from pytest_mock import mocker
from django.test import Client

from kills.accessors.dragon_accessor import DragonAccessor
from kills.accessors.kills_accessor import KillsAccessor
from kills.accessors.rules_accessor import RulesAccessor


def get_register_post_request_data(dragon_name):
    return { 'dragon_name': dragon_name }


def get_add_post_request_data(maximum_hours, maximum_kills):
    return { 'maximum_hours': maximum_hours,
             'maximum_kills': maximum_kills }


def get_delete_post_request_data(id):
    return { 'id': id }


def get_kill_post_request_data(datetime, number_of_animals, dragon_id):
    return { 'datetime': datetime,
             'number_of_animals': number_of_animals,
             'dragon_id': dragon_id }


def get_post_response_from_api(url, data):
    client = Client()
    response = client.post(url, data)
    return json.loads(response.content)


class TestViews:

    @pytest.mark.django_db
    @pytest.mark.parametrize(('name', 'expected_status_response'), [('yash', 1),
                                                                    ('kapoor', 1),
                                                                    ('', 0)])
    def test_register_dragon(self, name, expected_status_response):
        data = get_register_post_request_data(name)
        actual_response = get_post_response_from_api(url='/add/dragon/', data=data)

        assert actual_response['status-code'] == expected_status_response

    @pytest.mark.django_db
    @pytest.mark.parametrize(('maximum_hours', 'maximum_kills', 'expected_status'), [(3, 1, 1),
                                                                                     (4, 2, 1),
                                                                                     (5, 3, 1)])
    def test_add_rule(self, maximum_kills, maximum_hours, expected_status):
        data = get_add_post_request_data(maximum_hours, maximum_kills)

        actual_response = get_post_response_from_api(url='/add/rule/', data=data)

        assert actual_response['status-code'] == expected_status

    @pytest.mark.parametrize(('id', 'expected_status'), [(1, 1),
                                                         (2, 1),
                                                         (3, 1)])
    def test_delete_rule(self, mocker, id, expected_status):
        data = get_delete_post_request_data(id)
        mocker.patch.object(RulesAccessor, 'delete_rule_by_id',
                            return_value=1)
        actual_response = get_post_response_from_api(url='/delete/rule/', data=data)

        assert actual_response['status-code'] == expected_status


    @pytest.mark.parametrize(('datetime', 'number_of_animals', 'dragon_id', 'expected_status'), [('2020-01-01-00:00', 2, 1, 1),
                                                                                                 ('2020-01-01-01:00', 2, 1, 1),
                                                                                                 ('2020-01-01-02:00', 2, 1, 1)])
    def test_kill_animal(self, mocker, datetime, number_of_animals, dragon_id, expected_status):
        data = get_kill_post_request_data(datetime, number_of_animals, dragon_id)
        mocker.patch.object(DragonAccessor, 'get_dragon_by_id',
                            return_value=1)
        mocker.patch.object(KillsAccessor, 'set_kill',
                            return_value=(1, "test"))
        actual_response = get_post_response_from_api(url='/kill/animal/', data=data)

        assert actual_response['status-code'] == expected_status
