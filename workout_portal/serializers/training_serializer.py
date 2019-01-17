from rest_framework import serializers

from workout_portal.serializers.exercise_serializer import ExerciseSerializer
from workout_portal.serializers.user_serializer import UserSerializer
from workout_portal.models import Training


class TrainingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Training
        fields = ('name', 'date', 'user', 'exercises')

    # def to_representation(self, value):
    #     duration = time.strftime('%M:%S', time.gmtime(value.duration))
    #     return 'Track %d: %s (%s)' % (value.order, value.name, duration)
