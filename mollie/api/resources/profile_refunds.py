from .refunds import Refunds


class ProfileRefunds(Refunds):
    profile_id = None

    def get_resource_path(self):
        return f"refunds?profileId={self.profile_id}"

    def with_parent_id(self, profile_id):
        self.profile_id = profile_id
        return self

    def on(self, profile):
        return self.with_parent_id(profile.id)
