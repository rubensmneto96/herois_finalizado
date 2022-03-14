import herois

def initialize(context):
    """Inicializa Herois"""
    context.registerClass(
        herois.Herois,
        constructors = (
            herois.manage_addHeroisSiteForm,
            herois.manage_addHeroisSite,
            herois.nav,
            herois.foot,
            herois.Herois.style,
        ),
        icon = None
    )