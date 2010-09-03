import settings

def settings_processor(request):
    settings_list = [i for i in dir(settings) if not i.startswith('__')]
    settings_dictionary = dict(zip(settings_list, [getattr(settings, i) for i in settings_list]))

    return {'settings' : settings_dictionary}

