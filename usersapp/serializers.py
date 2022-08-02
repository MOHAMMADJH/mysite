from rest_framework import serializers
from .models import note


class NoteSerializer(serializers.ModelSerializer):

    
    class Meta:
     
        model = note
        fields = ['pk','note', 'email', 'password', 'self_d', 'note_name', 'note_id']
        # fields = '__all__'

    # def get_validation_exclusions(self):
    #         exclusions = super(note, self).get_validation_exclusions()
    #         return exclusions + ['owner']

    """
    
    [
    {
        "note": "sadasd",
        "email": "mohjas97_fes@hotmail.com",
        "password": "1233456",
        "self_d": "2022-07-23T17:27:06Z",
        "note_name": "asd",
        "note_id": "9613237a-c503-4e13-b279-84b5c18fe95f"
    },
    
    
    """