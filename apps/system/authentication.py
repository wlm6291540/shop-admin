from rest_framework.authentication import SessionAuthentication


class CsrfExcludeAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return
