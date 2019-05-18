#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author : Prakhar Pratyush <prakharlabs@gmail.com>
#
#----------------------------------------------------------

import pytest
from tests.helpers import do_steps

class Objectify(object):
	def __init__(self, d):
		for a, b in d.items():
			if isinstance(b, (list, tuple)):
			   setattr(self, a, [Objectify(x) if isinstance(x, dict) else x for x in b])
			else:
			   setattr(self, a, Objectify(b) if isinstance(b, dict) else b)
			
test_config = {'base_url': 'https://google.com', 'global_step_wait': '5', 'steps': [{'type': 'input', 'text': 'dbmndbndbndjkbdkbdgbdgbdgbgdkbkgk', 'description': 'Enter text', 'locators': [{'type': 'attribute', 'key': 'name', 'value': 'q'}, {'type': 'attribute', 'key': 'title', 'value': 'Search'}], 'config': {'step_wait': '0'}}, {'type': 'click', 'description': 'Click search button', 'locators': [{'type': 'attribute', 'key': 'value', 'value': 'Google Search'}, {'type': 'css_selector', 'value': 'center > input', 'position': '3'}], 'config': {'step_wait': '0'}}, {'type': 'wait', 'description': 'Wait for 10 seconds', 'value': '30', 'until': 'url_changed', 'config': {'step_wait': '0'}}, {'type': 'assertion', 'assertionType': 'textExists', 'value': 'Your search - dbmndbndbndjkbdkbdgbdgbdgbgdkbkgk - did not match any documents', 'locators': [{'type': 'xpath', 'value': "//div[id='topstuff']/div/div/p"}], 'config': {'step_wait': '5'}}, {'type': 'assertion', 'assertionType': 'elementNotExists', 'locators': [{'type': 'attribute', 'key': 'id', 'value': 'ires'}], 'config': {'step_wait': '0'}}]}
test_config = Objectify(test_config)

def test_no_result_found(driver_):
	base_url = test_config.base_url
	global_step_wait = test_config.global_step_wait
	steps = test_config.steps
	
	global driver 
	driver = driver_
	driver.get(base_url)

	driver.implicitly_wait(global_step_wait)
	
	for step in steps:
		do_steps(step, driver)
	
	driver.quit()
