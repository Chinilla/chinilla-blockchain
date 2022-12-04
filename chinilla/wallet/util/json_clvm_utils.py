from __future__ import annotations

from typing import Any

from chinilla.types.blockchain_format.program import Program


def json_to_chinillalisp(json_data: Any) -> Any:
    list_for_chinillalisp = []
    if isinstance(json_data, list):
        for value in json_data:
            list_for_chinillalisp.append(json_to_chinillalisp(value))
    else:
        if isinstance(json_data, dict):
            for key, value in json_data:
                list_for_chinillalisp.append((key, json_to_chinillalisp(value)))
        else:
            list_for_chinillalisp = json_data
    return Program.to(list_for_chinillalisp)
