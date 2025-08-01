"""
@author: cunyue
@file: test_apple.py
@time: 2024/12/10 20:33
@description: 测试苹果芯片信息采集
"""

import pytest

from swanlab.data.run.metadata.hardware.soc.apple import AppleChipCollector
from swanlab.toolkit import is_macos


@pytest.mark.skipif(not is_macos(), reason="Apple chip info only available on macOS")
def test_apple_collector():
    apple = AppleChipCollector()
    apple()
    assert apple.collect_num == 1
