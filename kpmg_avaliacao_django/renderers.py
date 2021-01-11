from rest_framework import renderers

import etl


class JSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if not isinstance(data, etl.Engine):
            return super().render(data, accepted_media_type, renderer_context)
        
        return data.to_json().encode()


class CSVRenderer(renderers.BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if not isinstance(data, etl.Engine):
            return renderers.JSONRenderer().render(data, accepted_media_type, renderer_context)
        
        return data.to_csv().encode()
