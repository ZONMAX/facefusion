import os
from datetime import datetime
from typing import Optional, Sequence

from facefusion.filesystem import get_file_extension, get_file_name


def get_step_output_path(job_id : str, step_index : int, output_path : str, target_path : Optional[str] = None, source_paths : Optional[Sequence[str] | str] = None, date_time : Optional[datetime] = None) -> Optional[str]:
        if output_path:
                output_directory_path, _ = os.path.split(output_path)
                output_file_extension = get_file_extension(_)

                target_file_name = get_file_name(target_path) if target_path else get_file_name(_)

                source_path : Optional[str] = None
                if isinstance(source_paths, Sequence):
                        if source_paths:
                                source_path = source_paths[0]
                elif isinstance(source_paths, str):
                        source_path = source_paths
                source_file_name = get_file_name(source_path) if source_path else 'source'

                time_stamp = (date_time or datetime.now()).strftime('%Y%m%d-%H%M%S')
                output_file_name = f"{target_file_name}_{source_file_name}_{time_stamp}"
                return os.path.join(output_directory_path, output_file_name + output_file_extension)
        return None


def suggest_job_id(job_prefix : str = 'job') -> str:
	return job_prefix + '-' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
