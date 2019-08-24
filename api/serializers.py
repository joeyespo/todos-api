def todo(obj):
    return {
        'id': obj.id,
        'text': obj.text,
        'completed': obj.completed,
    }


def todos(objs):
    return {'todos': [todo(obj) for obj in objs]}
