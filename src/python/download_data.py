import os
import zipfile
from pathlib import Path

import kaggle


def download_data():
    """Utility function to grab the Kaggle 
    data from the API if it's not present in the repo.

    Args: None
    Returns: None

    Raises:
        KaggleAPIException: if the Kaggle API fails
    """

    iskaggle = os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')
    path = Path('us-patent-phrase-to-phrase-matching')

    if not iskaggle and not path.exists():
        try:
            kaggle.api.competition_download_cli(str(path))
            zipfile.ZipFile(f'{path}.zip').extractall(path)
            return
        except kaggle.KaggleAPIException as e:
            print(e)
