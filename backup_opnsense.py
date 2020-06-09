#!/usr/bin/env python3

import OpnsenseIP
import time
import os

import config

if __name__ == '__main__':
    if not os.path.exists('backups'):
        os.makedirs('backups')
    router_conn = OpnsenseIP.OpnSense(
        config.router_hostname, config.router_apikey, config.router_apisecret)
    backup_data = router_conn.Get('backup/backup/download', json_output=False)
    backup_filename = 'backups/opnsense.backup.%s.xml' % int(time.time())
    f = open(backup_filename, 'w')
    f.write(backup_data)
    f.close()
