class AuthSchema:
    @staticmethod
    def get_auth_schema():
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "username": {"type": "string"},
                "email": {"type": "string", "format": "email"},
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "gender": {"type": "string"},
                "image": {"type": "string", "format": "uri"},
                "token": {"type": "string"}
            },
            "required": ["id", "username", "email", "firstName", "lastName", "gender", "image", "token"]
        }
