
_history = []

def add_message(role, content):
    _history.append({"role": role,
                     "content" : content})


def get_history():
    return _history