import os
from datetime import datetime

from facefusion.jobs.job_helper import get_step_output_path


def test_get_step_output_path() -> None:
        dt = datetime(2024, 1, 1, 12, 0, 0)
        expected = 'target_source_20240101-120000.mp4'
        assert get_step_output_path('test-job', 0, 'test.mp4', 'target.mp4', ['source.mp4'], dt) == expected
        assert get_step_output_path('test-job', 0, 'test/test.mp4', 'target.mp4', ['source.mp4'], dt) == os.path.join('test', expected)
