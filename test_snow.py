from rest_classes.RestEndpoint import RestEndpoint

snow = RestEndpoint(url='https://dev82732.service-now.com/api/now', username='admin', password='XXX')

snow.set_headers()

ticket = {"id": "1234", "kpi_id": "1236", "level": "2", "producer": "Router1", "state": "down", "uuid": "123456789",
          "msg": "Test Call"}

call = snow.post(p_params=['table', 'x_397387_cw_alerts_alert_table'], payload=ticket)

print(call['status_code'])
print(call['body'])

call2 = snow.get(p_params=['table', 'x_397387_cw_alerts_alert_table', '33ad8342db33330088ad2706ca961900'])

print(call2['status_code'])
