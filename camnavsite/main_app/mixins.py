from django.core.exceptions import PermissionDenied


class ExampleMixin(object):

    def __init__(self):
        # print 'ExampleMixin'
        pass

    def dispatch(self, request):
        # print request.user

        if request.user is None:
            raise PermissionDenied
        return super(ExampleMixin, self).dispatch(request)


class ScoreMixin(object):
    """Mixin to another class to provide access to a User's ``Score``."""
    @property
    def score(self):
        """Get the latest score for the User who saved this Job."""
        if not hasattr(self, "_score"):
            self._score = self.user.score_set.latest()
        return self._score