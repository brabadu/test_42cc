import settings


def settings_processor(request):
    setts_list = [i for i in dir(settings) if not i.startswith('__')]
    setts_dict = dict(zip(setts_list,
                          [getattr(settings, i) for i in setts_list]))

    return {'settings': setts_dict}
