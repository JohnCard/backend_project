#first comment
class TemplateTitleMixin(object):
    title = None
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title'] = self.get_title()
        return context
    def get_title(self):
        return self.title

class TemplateCancel(object):
    link_cancel = None
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['link_cancel'] = self.get_link_cancel()
        return context
    
    def get_link_cancel(self):
        return self.link_cancel
    
class LinkStyle(object):
    linkstyle = None
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['linkstyle'] = self.get_linkstyle()
        return context
    
    def get_linkstyle(self):
        return self.linkstyle
    