
from travallo.models import Product
from travallo.utils.success import Success
class Product_service:
        def create_reportmaster(self,request_obj,emp_id):

            if not request_obj.get_id() is None:

                reportmaster_update = Product.objects.filter(id=request_obj.get_id()).update(
                    name=request_obj.get_name(),
                    updated_by=emp_id)
                reportmaster_update = Product.objects.get(id=request_obj.get_id())
                error_obj = Success()
                error_obj.set_code = 'SUCCESS'
                error_obj.set_description = 'SUCCESS FULLY UPDATED'
                return error_obj

            else:
                reportmaster_update = Product.objects.create(
                    name=request_obj.get_name(),
                    created_by=emp_id)
                reportmaster_update.code ="RM"+str(reportmaster_update.id)
                reportmaster_update.save()

                error_obj = Success()
                error_obj.set_code = 'SUCCESS'
                error_obj.set_description = 'SUCCESS FULLY CREATED'
                return error_obj