from django import template

register = template.Library()

class AssignNode(template.Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def render(self, context):
        context[self.name] = self.value.resolve(context, True)
        return ''

def do_assign(parser, token):
    """
    Assign an expression to a variable in the current context.

    Syntax::
        {% assign [name] [value] %}
    Example::
        {% assign list entry.get_related %}

    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("'%s' tag takes two arguments" % bits[0])
    value = parser.compile_filter(bits[2])
    return AssignNode(bits[1], value)

register.tag('assign', do_assign)


from time import strftime

@register.filter
def date_to_space(value, prev_date):
    delta = prev_date - value
    return -delta.days*1.5


class GetTransNode(template.Node):
    def __init__(self, objet, property, lang):
        self.objet = template.Variable(objet)
        self.property = property
        self.lang = template.Variable(lang)
    def render(self, context):
        objet = self.objet.resolve(context)
        lang = self.lang.resolve(context)
        if lang == "nl":
            prop = "%s" % self.property
            return objet.__getattribute__(prop)
        else:
            prop = "%s_%s" % (self.property, lang)
            return objet.__getattribute__(prop)

def do_get_trans(parser, token):
    # {% get_trans description %}
    try:
        tag_name, objet, prop, lang = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments" % token.contents.split()[0])
    return GetTransNode(objet, prop, lang)

register.tag('get_trans', do_get_trans)
