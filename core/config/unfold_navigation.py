from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def user_has_group_or_permission(user, permission):
    if user.is_superuser:
        return True

    group_names = user.groups.values_list("name", flat=True)
    if not group_names:
        return True

    return user.groups.filter(permissions__codename=permission).exists()


PAGES = [
    {
        "seperator": True,
        "items": [
            {
                "title": _("Bosh sahifa"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Foydalanuvchilar"),
        "items": [
            {
                "title": _("Guruhlar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_group_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_group"
                ),
            },
            {
                "title": _("Foydalanuvchilar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_user_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
            {
                "title": _("Site"),
                "icon": "language",
                "link": reverse_lazy("admin:sites_site_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_sites"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Models"),
        "items": [
            {
                "title": _("Dynamic Schema"),
                "icon": "schema",
                "link": reverse_lazy("admin:backend_dynamicschema_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_dynamicschema"
                ),
            },
            {
                "title": _("Types"),
                "icon": "checklist",
                "link": reverse_lazy("admin:backend_type_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_type"
                ),
            },
            {
                "title": _("Gallery"),
                "icon": "perm_media",
                "link": reverse_lazy("admin:backend_gallery_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_gallery"
                ),
            },
        ],
    },
]

TABS = [
    {
        "models": [
            "auth.user",
            "auth.group",
        ],
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "link": reverse_lazy("admin:auth_user_changelist"),
            },
            {
                "title": _("Guruhlar"),
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
]
