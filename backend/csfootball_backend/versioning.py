from rest_framework.versioning import URLPathVersioning


class MonitoringAPIVersioning(URLPathVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'

    def determine_version(self, request, *args, **kwargs):
        version = super().determine_version(request, *args, **kwargs)
        if version not in self.allowed_versions:
            return self.default_version
        return version
