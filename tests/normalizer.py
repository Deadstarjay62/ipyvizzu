"""A module for postprocessing mocked test outputs."""

import re
from unittest.mock import MagicMock


class Normalizer:
    """A class for normalizing mocked test outputs."""

    def __init__(self):
        self.id1_pattern = re.compile(r"'[a-f0-9]{7}'", flags=re.MULTILINE)
        self.id2_pattern = re.compile(r"\"[a-f0-9]{7}\"", flags=re.MULTILINE)

    def normalize_id(self, output: str) -> str:
        """A method for replacing uuids with the "id" strings."""

        normalized_output = output
        normalized_output = self.id1_pattern.sub("id", normalized_output)
        normalized_output = self.id2_pattern.sub("id", normalized_output)
        return normalized_output

    def normalize_output(self, output: MagicMock, start_index: int = 0) -> str:
        """A method for merging and normalizing mocked test outputs."""

        output_items = [block.args[0] for block in output.call_args_list[start_index:]]
        return self.normalize_id("\n".join(output_items)).strip()
