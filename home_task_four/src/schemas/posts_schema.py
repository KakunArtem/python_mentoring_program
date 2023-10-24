class PostsSchema:
    @staticmethod
    def get_all_posts_schema():
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "posts": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "string"},
                            "body": {"type": "string"},
                            "userId": {"type": "integer"},
                            "tags": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "reactions": {"type": "integer"}
                        },
                        "required": ["id", "title", "body", "userId", "tags", "reactions"]
                    }
                },
                "total": {"type": "integer"},
                "skip": {"type": "integer"},
                "limit": {"type": "integer"}
            },
            "required": ["posts", "total", "skip", "limit"]
        }

    @staticmethod
    def get_post_schema():
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "body": {"type": "string"},
                "userId": {"type": "integer"},
                "tags": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "reactions": {"type": "integer"}
            },
            "required": ["id", "title", "body", "userId", "tags", "reactions"]
        }
