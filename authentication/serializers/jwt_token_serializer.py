from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.context import get_current_company

class JWTTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        """
            Function to add custom claims to the JWT token
            ----------------------------------------------
            Add any custom claims you want to include in the JWT token here,
            in this case we are adding a custom claim of `company_id` 
            for tenant-based authentication

            Params:
            -------
                user (User): The user instance for whom the token is being generated.

            Returns:
            --------
                token (Token): The JWT token with custom claims added.
        """
        token = super().get_token(user)
        company: int = get_current_company()
        # # set the custom claims for company
        # token['company_id'] = user.profile.company_id
        # token['company_code'] = user.profile.company.code

        return token
