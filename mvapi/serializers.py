from rest_framework import serializers
from branch.models import branches

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=branches
        fields='__all__'