import hashlib
import os
from typing import Optional

from facefusion import state_manager
from facefusion.filesystem import get_file_extension, is_image, is_video
from datetime import datetime


def convert_int_none(value : int) -> Optional[int]:
	if value == 'none':
		return None
	return value


def convert_str_none(value : str) -> Optional[str]:
	if value == 'none':
		return None
	return value


def suggest_output_path(output_directory_path : str, target_path : str) -> Optional[str]:
        if is_image(target_path) or is_video(target_path):
                source_paths = state_manager.get_item('source_paths')
                source_path = None
                if isinstance(source_paths, list) and source_paths:
                        source_path = source_paths[0]
                elif isinstance(source_paths, str):
                        source_path = source_paths
                target_file_name = os.path.splitext(os.path.basename(target_path))[0]
                source_file_name = os.path.splitext(os.path.basename(source_path))[0] if source_path else 'source'
                time_stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
                target_file_extension = get_file_extension(target_path)
                output_file_name = f"{target_file_name}_{source_file_name}_{time_stamp}"
                return os.path.join(output_directory_path, output_file_name + target_file_extension)
        return None
