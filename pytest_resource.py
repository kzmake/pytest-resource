# encoding:utf-8

import pytest


@pytest.fixture
def resource(request):
    """
    指定されたpathからファイルを読み込む

    @pytest.mark.resource(PATH)
    def test_hoge(resource):
        pass
    """
    print(request.keywords)
    if 'resource' not in request.keywords:
        raise ValueError("Resource not found")

    path = request.keywords.get('resource').args[0]
    with open(path, 'r') as f:
        data = f.read()

    return data
