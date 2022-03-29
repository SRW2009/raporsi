from django.utils import timezone

from app.helper.response import SerializerHelper as HLog
from rest_framework import serializers
from app.models import Admin, Divisi
from django.db import transaction
# from django.core import serializers as S


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'name']


class DivisiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=True)

    def create(self, admin_id):
        activity = 'Create Divisi'
        try:
            with transaction.atomic():
                d = Divisi.objects.create(name=self.data['name'], created_by_id=admin_id)
        except Exception as e:
            pass
            HLog.create_log(admin_id, activity, False, str(e))
            return {"error": str(e)}
        HLog.create_log(admin_id, activity, True, "Divisi successfully created")
        return {"message": "Divisi successfully created"}

    def update(self, divisi_id, admin_id):
        activity = 'Update Divisi'
        try:
            d = Divisi.objects.get(id=divisi_id, deleted_at__isnull=True)
            with transaction.atomic():
                d.name = self.data['name']
                d.updated_at = timezone.now()
                d.updated_by_id = admin_id
                d.save()
        except Exception as e:
            pass
            HLog.create_log(admin_id, activity, False, str(e))
            return {"error": str(e)}
        pass
        HLog.create_log(admin_id, activity, True, "Divisi updated successfully")
        return{"message": "Divisi updated successfully"}

    @staticmethod
    def delete(divisi_id, admin_id):
        activity = 'Delete Divisi'
        try:
            d = Divisi.objects.get(id=divisi_id, deleted_at__isnull=True)
            with transaction.atomic():
                d.deleted_at = timezone.now()
                d.deleted_by_id = admin_id
                d.save()
        except Exception as e:
            pass
            HLog.create_log(admin_id, activity, False, str(e))
            return {"error": str(e)}
        pass
        HLog.create_log(admin_id, activity, True, "Divisi deleted successfully")
        return{"message": "Divisi deleted successfully"}

    @staticmethod
    def get(admin_id,id,name):
        activity = 'Get Divisi'
        try:
            if id == "" and name == "":
                d = Divisi.objects.filter(deleted_at__isnull=True)
            elif id != "" and name == "":
                d = Divisi.objects.filter(id=id, deleted_at__isnull=True)
            elif id != "" and name != "":
                d = Divisi.objects.filter(id=id, name=name, deleted_at__isnull=True)
            data = []
            for item in d:
                data.append({
                    "id": item.id,
                    "name": item.name,
                })
            HLog.create_log(admin_id, activity, True, "Divisi successfully fetched")
            return {"message": "Divisi fetch successfully", "data": data}
        except Exception as e:
            HLog.create_log(admin_id, activity, False, str(e))
            return {"error": str(e)}

    # @staticmethod
    # def filter(admin_id, id, name):
    #     activity = 'Get Divisi'
    #     try:
    #         d = Divisi.objects.filter(id=id, name=name, deleted_at__isnull=True)
    #         data = []
    #         for item in d:
    #             data.append({
    #                 "id": item.id,
    #                 "name": item.name,
    #             })
    #         HLog.create_log(admin_id, activity, True, "Divisi successfully fetched")
    #         return {"message": "Divisi fetch successfully", "data": data}
    #     except Exception as e:
    #         HLog.create_log(admin_id, activity, False, str(e))
    #         return {"error": str(e)}




