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
    return -delta.days*2


@register.filter
def get_trans(objet, propert, lang):
    # {% get_trans description %}
    if lang == 'nl':
        return objet.__getattribute__(propert)
    try:
        return objet.__getattribute__("%s_en" % propert)
    except:
        pass

register.tag('get_trans', get_trans)
