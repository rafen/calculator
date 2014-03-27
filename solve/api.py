from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from solve.models import Equation


class CalculatorResource(ModelResource):
    """
    Simple resource to manage the Equation model
    """
    class Meta:
        queryset = Equation.objects.all()
        resource_name = 'calculator'
        excludes = ['created', 'id']
        include_resource_uri = False
        always_return_data = True
        # WARNING this make the API public!
        authorization = Authorization()
