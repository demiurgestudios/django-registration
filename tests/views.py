"""
Viw classes to exercise options of the registration view behavior not
covered by the built-in workflows.

"""
from django.core.urlresolvers import reverse
from django.utils.functional import lazy
reverse_lazy = lazy(reverse, str)

from django_registration.backends.activation.views import ActivationView


class ActivateWithComplexRedirect(ActivationView):
    success_url = reverse_lazy('django_registration_activation_complete')
