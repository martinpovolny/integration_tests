# -*- coding: utf-8 -*-
import pytest

from cfme.base.login import BaseLoggedInPage
from cfme.containers.provider import ContainersProvider
from cfme.utils.appliance.implementations.ui import navigate_to
from cfme.utils.version import current_version


pytestmark = [pytest.mark.provider([ContainersProvider], scope='function')]


def is_menu_visible(appliance, link_text):
    navigate_to(ContainersProvider, 'All')
    logged_in_page = appliance.browser.create_view(BaseLoggedInPage)
    return link_text in logged_in_page.navigation.nav_links()


@pytest.fixture(scope='function')
def is_datawarehouse_menu_visible(appliance):
    return is_menu_visible(appliance, 'Datawarehouse')


@pytest.fixture(scope='function')
def is_monitoring_menu_visible(appliance):
    return is_menu_visible(appliance, 'Monitor')


def test_datawarehouse_invisible(is_datawarehouse_menu_visible):
    """
    Polarion:
        assignee: juwatts
        caseimportance: medium
        casecomponent: Containers
        initialEstimate: 1/4h
    """
    # This should be the default state
    # Verifies BZ#1421175
    assert not is_datawarehouse_menu_visible
