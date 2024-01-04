from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)     #This is just the class which specifically stores only data(reason->decorator used(frozen=True makes it immutable)) 
class DataIngestionConfig:
    root_dir: Path
    source_URL:str
    local_data_file: Path
    unzip_dir: Path