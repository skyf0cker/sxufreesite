#!/usr/bin/expect
set timeout 30
spawn sudo openconnect --juniper --script /etc/vpnc/vpnc-script https://sslvpn.sxu.edu.cn --servercert sha256:9293411775d8808b551ee2dadc9de27cc114372af0fbd5f84b451fdcfbe3afed
expect "*的密码："
send "自己root的密码\r"
expect "*username"
send "自己的学号\r"
expect "*password"
send "自己的密码\r"
interact
