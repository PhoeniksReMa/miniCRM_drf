from rest_framework import serializers, request

from .models import Contact,Deal, Stage, Funnel


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = "__all__"

class DealSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = Deal
        fields = ["id", "name", "description", "user", "stage", "contacts"]

    def get_contacts(self, obj):
        contacts = obj.contact.all()
        return ContactSerializer(contacts, many=True).data

class StageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    deals = serializers.SerializerMethodField()

    class Meta:
        model = Stage
        fields = ["id", "name", "funnel", "user", "deals"]

    def get_deals(self, obj):
        deals = obj.deal.all()
        return DealSerializer(deals, many=True).data

class FunnelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    stages = serializers.SerializerMethodField()

    class Meta:
        model = Funnel
        fields = ["id", "name", "user", "stages"]

    def get_stages(self, obj):
        stages = obj.stage.all()
        return StageSerializer(stages, many=True).data