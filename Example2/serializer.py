from rest_framework import routers,serializers,viewsets
from Example2.models import Example2

class Ejemplo2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')