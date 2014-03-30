from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.resources import ModelResource
from solve.models import Equation, Session


class SessionResource(ModelResource):
    """
    Simple resource to manage the Sessions.
    It only allow to save sessionss
    """
    class Meta:
        queryset = Session.objects.all()
        resource_name = 'session'
        excludes = ['id', 'user']
        list_allowed_methods = ['post']
        include_resource_uri = False
        always_return_data = True
        authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication())
        authorization = DjangoAuthorization()
        filtering = {
            "name": ALL_WITH_RELATIONS,
        }

    def obj_create(self, bundle, **kwargs):
        res = super(SessionResource, self).obj_create(bundle, **kwargs)
        if bundle.request.user.is_authenticated():
            # get all session from this user with no name
            uname_sessions = Session.objects.filter(user=bundle.request.user, name="")
            # set name to all sessions with no name
            uname_sessions.update(name=bundle.data['name'])
        return res


class CalculatorResource(ModelResource):
    """
    Simple resource to manage the Equation model
    """
    session = fields.ForeignKey(SessionResource, 'session')

    class Meta:
        queryset = Equation.objects.all()
        resource_name = 'calculator'
        excludes = ['created', 'id']
        include_resource_uri = False
        always_return_data = True
        filtering = {
            "session": ALL_WITH_RELATIONS,
            "valid": ALL_WITH_RELATIONS,
        }
        # authentication
        authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication())
        authorization = DjangoAuthorization()

    def obj_create(self, bundle, **kwargs):
        res = super(CalculatorResource, self).obj_create(bundle, **kwargs)
        if bundle.request.user.is_authenticated():
            res.obj.session.user = bundle.request.user
            res.obj.session.save()
        return res

