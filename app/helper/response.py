from app.models import Log, Admin


class SerializerHelper:
    @staticmethod
    def create_log(who, activity, status, message):
        Log.objects.create(case={"by": who, "activity": activity, "status": status, "message": message})

    @staticmethod
    def get_admin(admin_id):
        a = Admin.objects.get(id=admin_id)
        return a

