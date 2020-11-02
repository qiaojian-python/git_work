# 自定义频率组件
from rest_framework.throttling import SimpleRateThrottle


class SendMessageRate(SimpleRateThrottle):
    scope = "send"

    # 只对包含手机号的请求做验证  获得唯一标识， 存在缓存中  或者返回时间
    def get_cache_key(self, request, view):
        phone = request.query_params.get('phone')
        if not phone:
            return None
        return phone





