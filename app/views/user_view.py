def render_user_list(users):
    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "password_hash": user.password_hash,
            "roles": user.roles,
        }
        for user in users
    ]


def render_user_detail(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password_hash": user.password_hash,
        "roles": user.roles,
    }