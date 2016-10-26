---
layout: post
title: 花了兩個小時幫 bottle.py 修了一個 bug
date: 2016-02-06 10:30
comments: true
categories: 
---
真的很賭爛因為別人的 code 有 bug 讓自己花了超久的時間 debug

最近在寫一個 CTF 訓練平台，架構上採用 peewee + bottle.py 進行開發，因為不想花太多時間去學 Django 這種太龐大的架構（加上有些用法自己不見得喜歡），所以打算自幹整個架構

遇到了一個問題是我需要自訂 view 的路徑，翻了一下 code 之後發現我有 `template_lookup` 這個 keyword argument 可以用，但是不管怎麼嘗試，就是沒辦法讓 bottle.py 去我指定的 path 找 template file，不知道是不是我對 decorator 有誤解，改了老半天，後來又 trace 了一下 bottle.py 的 code，才發現根本不是我的問題.....

## TL;DR

``` python
def template(*args, **kwargs):
    """
    Get a rendered template as a string iterator.
    You can use a name, a filename or a template string as first parameter.
    Template rendering arguments can be passed as dictionaries
    or directly (as keyword arguments).
    """
    tpl = args[0] if args else None
    # should mixin args into kwargs here
    adapter = kwargs.pop('template_adapter', SimpleTemplate)
    lookup = kwargs.pop('template_lookup', TEMPLATE_PATH)  # <-- template_lookup reads from here
    tplid = (id(lookup), tpl)
    if tplid not in TEMPLATES or DEBUG:
        settings = kwargs.pop('template_settings', {})
        if isinstance(tpl, adapter):
            TEMPLATES[tplid] = tpl
            if settings: TEMPLATES[tplid].prepare(**settings)
        elif "\n" in tpl or "{" in tpl or "%" in tpl or '$' in tpl:
            TEMPLATES[tplid] = adapter(source=tpl, lookup=lookup, **settings)
        else:
            TEMPLATES[tplid] = adapter(name=tpl, lookup=lookup, **settings)
    if not TEMPLATES[tplid]:
        abort(500, 'Template (%s) not found' % tpl)
    for dictarg in args[1:]:
        kwargs.update(dictarg)  # <-- my template_lookup appears here
    return TEMPLATES[tplid].render(kwargs)


mako_template = functools.partial(template, template_adapter=MakoTemplate)
cheetah_template = functools.partial(template,
                                     template_adapter=CheetahTemplate)
jinja2_template = functools.partial(template, template_adapter=Jinja2Template)


def view(tpl_name, **defaults):
    """ Decorator: renders a template for a handler.
        The handler can control its behavior like that:

          - return a dict of template vars to fill out the template
          - return something other than a dict and the view decorator will not
            process the template, but return the handler result as is.
            This includes returning a HTTPResponse(dict) to get,
            for instance, JSON with autojson or other castfilters.
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (dict, DictMixin)):
                tplvars = defaults.copy()
                tplvars.update(result)
                return template(tpl_name, **tplvars)
            elif result is None:
                return template(tpl_name, defaults)  # <-- if goes here
            return result

        return wrapper

    return decorator
```

[Patch at here](https://github.com/Inndy/bottle/commit/ba5b4da8afdb09e1d9490e43dbec95002fb4f7fb) and [PR at here](https://github.com/bottlepy/bottle/pull/830)
