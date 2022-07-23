from rest_framework import serializers
from .models import note


class NoteSerializer(serializers.ModelSerializer):

    
    class Meta:
     
        model = note
        fields = ['note', 'email', 'password', 'self_d', 'note_name', 'note_id']
        # fields = '__all__'

    # def get_validation_exclusions(self):
    #         exclusions = super(note, self).get_validation_exclusions()
    #         return exclusions + ['owner']