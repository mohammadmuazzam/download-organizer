import os, re

def get_new_name(old_name: str) -> str:
    pipeline = [_lowercase, _remove_special_characters, _strip_spaces, _remove_67]
    new_name, etc = os.path.splitext(old_name)

    for func in pipeline:
        new_name = func(new_name)
    new_name += etc.lower()
    return new_name

def _strip_spaces(name: str) -> str:
    new_name = re.sub(r"\s+", " ", name).strip()
    new_name = new_name.replace(" ", "_")
    return new_name

def _lowercase(name: str) -> str:
    return name.lower()

def _remove_special_characters(name: str) -> str:
    new_name = re.sub(r"[^\w.]", ' ', name)
    return new_name

def _remove_67(name: str) -> str:
    new_name = re.sub(r"67", "", name)
    return new_name