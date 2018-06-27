# encoding:utf-8

import json

import pytest


@pytest.mark.resource('tests/resources/sample.json')
def test_json_resource(resource):
    """
    指定したjsonファイルを読み込む
    """
    sut = json.loads(resource)

    with open('tests/resources/sample.json', 'r') as f:
        expected = json.load(f)

    assert sut is not None
    assert sut == expected


@pytest.mark.resource('tests/resources/sample.xml')
def test_xml_resource(resource):
    """
    指定したxmlファイルを読み込む
    """
    sut = resource

    with open('tests/resources/sample.xml', 'r') as f:
        expected = f.read()

    assert sut is not None
    assert sut == expected
