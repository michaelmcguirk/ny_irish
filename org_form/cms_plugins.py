from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Organisation, OrgPluginModel
from django.utils.translation import ugettext as _


class OrgPluginPublisher(CMSPluginBase):
    model = OrgPluginModel  # model where plugin data are saved
    module = _("Organisation")
    name = _("Organistion Search")  # name of the plugin in the interface
    render_template = "org_form/search.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(OrgPluginPublisher)  # register the plugin