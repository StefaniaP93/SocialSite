from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """Questa views ci consente di reindirizzare l'unico template html post-login. 
    Infatti LoginRequiredMixin ci permettera di vedere il contenuto della view
    solo dopo aver effettuato l'accesso"""
    template_name = "index.html" #per poter accedere a questo template è necessario essere loggati