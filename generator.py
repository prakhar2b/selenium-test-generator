#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author : Prakhar Pratyush <prakharlabs@gmail.com>
#
#----------------------------------------------------------

import yaml
import pytest

from cookiecutter.main import cookiecutter

file_name = "test.yml"

class Feature(object):
	def __init__(self, d):
		for a, b in d.items():
			if isinstance(b, (list, tuple)):
			   setattr(self, a, [Feature(x) if isinstance(x, dict) else x for x in b])
			else:
			   setattr(self, a, Feature(b) if isinstance(b, dict) else b)


def get_feature(file_name):
	with open(file_name, 'r') as test_f:
		try:
			tf = yaml.safe_load(test_f)  # test_feature 
		except yaml.YAMLError as exc:
			print(exc)

	tf_ = Feature(tf)

	test_name = tf_.test.name
	
	test_config = {
		'base_url': tf_.test.base_url,
		'global_step_wait': tf_.test.step_wait,
		'steps': tf['test']['steps']
	}

	return test_name, test_config

def create_cookiecutter_template(config):
	# You can specify an extra_context dictionary that will override values from cookiecutter.json
	cookiecutter('https://github.com/prakhar2b/selenium-test-generator.git',
		no_input=True,
        extra_context=config)


def main():
	test_name, test_config = get_feature(file_name)
	#test_config_ = "{}".format(test_config)

	dict = {
	"test_name": test_name.lower().replace(' ', '_'),
	"test_config": test_config
	}

	create_cookiecutter_template(dict)


if __name__ == '__main__':
    main()

