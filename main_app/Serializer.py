from models import TodoModel
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['userId','id',  'completed','title']