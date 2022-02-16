from rest_framework import serializers
from .models import Poll, Choice, Comment

from users.serializers import ProfileSerializer


class ChoiceSerializer(serializers.ModelSerializer):

    # ensures that the id is included
    # there may be issues here in the sense that the id is NOT read-only though it should be
    id = serializers.IntegerField(required=True)
    profiles = ProfileSerializer(many=True)
    class Meta:
        model = Choice
        fields = ('choice_text', 'id', 'choice_image', 'profiles', 'votes')


class CommentSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('comment_text', 'profile', 'created_at')


class PollSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True)
    profile = ProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Poll
        fields = ('id', 'profile', 'updated', 'question_text', 'choices', 'comments')


    # the following method handles creation of new choices
    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        poll = Poll.objects.create(**validated_data) # I think this should update an existing poll if found, not sure tho...
        for choice_data in choices_data:
            Choice.objects.create(poll=poll, **choice_data)
        return poll

    # handles updating of existing choice (e.g. vote registered)
    def update(self, instance, validated_data):
        instance.choice_text = validated_data.get('choice_text', instance.choice_text)
        instance.votes = validated_data.get('votes', instance.votes)
        instance.save()

        return instance

