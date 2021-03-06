from datetime import datetime

from unittest import mock

import pytest
from django.urls import reverse
from django.utils import timezone

from pythonpro.django_assertions import dj_assert_contains


@pytest.fixture
def client(client, cohort):
    return client


def test_should_return_200_when_load_invite_page(client):
    resp = client.get(reverse('pages:tpp_webiorico_landing_page'))
    assert resp.status_code == 200


@pytest.fixture
def create_or_update_with_no_role(mocker):
    return mocker.patch('pythonpro.email_marketing.facade.create_or_update_with_no_role.delay')


# TODO: move this phone tests do generic context
def test_should_call_update_when_with_correct_parameters(create_or_update_with_no_role, client):
    client.post(
        reverse('pages:tpp_webiorico_landing_page'),
        {'name': 'Moacir', 'email': 'moacir@python.pro.br'},
        secure=True
    )

    create_or_update_with_no_role.assert_called_with('Moacir', 'moacir@python.pro.br', mock.ANY)


# TODO: move this phone tests do generic context
def test_should_call_update_when_logged_with_correct_parameters(create_or_update_with_no_role, client_with_user):
    client_with_user.post(
        reverse('pages:tpp_webiorico_landing_page'),
        {'name': 'Moacir', 'email': 'moacir@python.pro.br'},
        secure=True
    )

    create_or_update_with_no_role.assert_called_with('Moacir', 'moacir@python.pro.br', mock.ANY)


def test_should_run_form_ok(create_or_update_with_no_role, client, cohort):
    resp = client.post(
        reverse('pages:tpp_webiorico_landing_page'),
        {'name': 'Moacir', 'email': 'moacir@python.pro.br'},
        secure=True
    )

    assert resp.status_code == 302


def test_should_inform_form_error(create_or_update_with_no_role, client, cohort):
    resp = client.post(
        reverse('pages:tpp_webiorico_landing_page'),
        {'name': 'Moacir', 'email': 'moacirpython.pro.br'},
        secure=True
    )

    assert resp.status_code == 200
    dj_assert_contains(resp, 'is-invalid')


def test_should_get_next_wed(mocker, client):
    fake_today = timezone.make_aware(datetime(2020, 10, 8))
    mocker.patch('pythonpro.pages.views.timezone.now', return_value=fake_today)

    resp = client.get(reverse('pages:tpp_webiorico_landing_page'))

    assert resp.status_code == 200
    dj_assert_contains(resp, '14/10')


def test_should_set_date_by_url(client):
    resp = client.get(reverse('pages:tpp_webiorico_landing_page_date_var', args=['13-10']))

    assert resp.status_code == 200
    dj_assert_contains(resp, '13/10')


def test_should_return_200_when_load_thank_you_page(client):
    resp = client.get(reverse('pages:tpp_webiorico_thank_you_page'))
    assert resp.status_code == 200
