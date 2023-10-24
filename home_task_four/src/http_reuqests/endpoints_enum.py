class Endpoints:
    AUTH = '/auth/login'
    POSTS = '/posts'
    POSTS_SEARCH = '/posts/search'
    POSTS_USERS = '/user'
    POSTS_COMMENTS = lambda posts_id: f'/post/{posts_id}/comments'
    POSTS_ADD = '/posts/add'
