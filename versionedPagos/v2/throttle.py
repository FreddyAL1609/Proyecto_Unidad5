from rest_framework.throttling import UserRateThrottle

class v2RateThrottle(UserRateThrottle):
    scope = 'apiv2_pagos'