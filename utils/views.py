from werkzeug.exceptions import abort


def json_abort(status, detail, *args, **kws):
    return abort(status, {'detail': detail}, *args, **kws)
