from modules.company.models import Relationship

def get_company_id(user_id):
    relationship = Relationship.objects.filter(user_id=user_id).first()
    return relationship.company_data_id