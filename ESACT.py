# Demo 1
# Author : Ahmed Adel Elemam 
# Email : ahmedelemamn@gmail.com
# license : GNU GENERAL PUBLIC LICENSE

print   "          ###############################################################"
print   "          # Network Team Edge Switch Script by Ahmed ElEmam, ISFP Egypt #"
print   "          ###############################################################"
print   "          #      Supported Switches HP A3100 , HP A3600 , HP A5120      #"
print   "          ###############################################################"
print   "   "

switch_type = int(raw_input('Enter switch type: '))
import time
def switch_5120():
	import sys
	
	class Logger(object):
		def __init__(self, filename="Default.log"):
			self.terminal = sys.stdout
			self.log = open(filename, "a")

		def write(self, message):
			self.terminal.write(message)
			self.log.write(message)

	sys.stdout = Logger("5120.txt")
	
	print   "          ###############################################################"
	print   "          #                          HP A5120                           #"
	print   "          ###############################################################"
	print   "   "

	defult_vlan = int(raw_input('Enter your defult Vlan: '))
	defult_vlan_name = raw_input('Enter your defult Vlan name: ')
	switch_num = int(raw_input('Enter Switch Num: '))  # The Switch number
	ND = int(raw_input ('Enter ND Number: '))          #network distribution switch from 1 to 6 
	Super_pass = raw_input('Enter Super password: ')
	manager_pass = raw_input('Enter manager password: ')
	monitor_pass = raw_input('Enter monitor password:')
	voice = ND + 40
	video = ND + 30
	manag = ND + 240
	manag_ip = switch_num + 10

	print "####################### A5120 #########################"
	print   "   "


	''' Hostname '''
	
	if ND == 1 :
		subs = switch_num + 100
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 2 :
		subs = switch_num + 200
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 3 :
		subs = switch_num + 300
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 4 :
		subs = switch_num + 400
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 5 :
		subs = switch_num + 500
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 6 :
		subs = switch_num + 600
		print 'sysname ND%s-E%s'%(ND, subs)
	else:
		print ' wrong ND number '
		
	print '#'

	'''main entries for the switch '''

	print "telnet server enable "
	print "ssh server enable"
	print 'ip https enable '
	print 'ip http enable '
	print '#'
	print 'stp enable'
	print '#'
	print 'info-center loghost 10.0.10.6'
	print '#'
	print 'user-interface vty 0 15'
	print '  authentication-mode scheme'
	print '#'

	''' vlans configuration '''

	print 'vlan %s' %(video)
	print ' name video_vlan' 
	print '#'
	print 'vlan %s' %(voice)
	print ' name Voice_vlan' 
	print '#'
	print 'vlan %s' %(manag)
	print ' name Management-Vlan'
	print '#'
	print 'vlan %s' %(defult_vlan)
	print ' name %s' %(defult_vlan_name)
	print '#'

	""" this section will configure the bridge aggregation link """

	print "interface Bridge-Aggregation1"
	print ' description Connection-to-ND%s' %(ND)
	print ' port link-type trunk'
	print ' port trunk permit vlan all'
	print ' port trunk pvid vlan %s' %(manag)
	print ' link-aggregation mode dynamic'
	print '#'
	''' this section will configure the interface vlan '''
	print 'interface Vlan-interface%s' %(manag)
	print ' ip address 10.0.%s.%s 255.255.255.0' %(manag, manag_ip)
	print '#'
	''' user profiles for your edge switch '''
	print 'local-user manager'
	print ' password cipher %s' %(manager_pass)
	print ' authorization-attribute level 3'
	print ' service-type ssh telnet'
	print '  service-type web'
	print 'local-user monitor'
	print ' password cipher %s' %(monitor_pass)
	print ' authorization-attribute level 1'
	print ' service-type telnet'
	print '  service-type web'
	print '#'
	''' your access interfaces '''
	for i in range(1, 24):
		print "interface GigabitEthernet 1/0/%d" %(i)
		print "port link-type hybrid"
		print 'undo port hybrid vlan 1'
		print 'port hybrid vlan %s untagged' %(defult_vlan)
		print 'port hybrid pvid vlan %s' %(defult_vlan)
		print 'voice vlan %s enable' %(voice)
		print 'poe enable'
		print 'stp edged-port enable'
		print '#'
	''' your management interface '''
	print 'interface GigabitEthernet 1/0/24'
	print ' description Switch-Management-Port'
	print ' port access vlan %s' %(manag)
	print ' stp edged-port enable'
	print '#'

	''' your UTP trunk interfaces '''

	for g in range(25, 27):
		print 'interface GigabitEthernet 1/0/%d' %(g)
		print ' port link-type trunk'
		print ' port trunk permit vlan all'
		print ' port trunk pvid vlan %s' %(manag)
		print '#'
	
	''' your fiber uplink '''

	for g in range(27, 29):
		print 'interface GigabitEthernet 1/0/%d' %(g)
		print ' port link-type trunk'
		print ' port trunk permit vlan all'
		print ' port trunk pvid vlan %s' %(manag)
		print ' port link-aggregation group 1'
		print '#'

	''' now defult route to your ND '''
	print 'ip route-static 0.0.0.0 0.0.0.0 10.0.%s.1' %(manag)
	print "#"
	
def switch_3100():
	import sys
	
	class Logger(object):
		def __init__(self, filename="Default.log"):
			self.terminal = sys.stdout
			self.log = open(filename, "a")

		def write(self, message):
			self.terminal.write(message)
			self.log.write(message)

	sys.stdout = Logger("3100.txt")
	print   "          ###############################################################"
	print   "          #                          HP A3100                           #"
	print   "          ###############################################################"
	print   "   "

	defult_vlan = int(raw_input('Enter your defult Vlan: '))
	defult_vlan_name = raw_input('Enter your defult Vlan name: ')
	switch_num = int(raw_input('Enter Switch Num: '))  # The Switch number
	ND = int(raw_input ('Enter ND Number: '))          #network distribution switch from 1 to 6 
	Super_pass = raw_input('Enter Super password: ')
	manager_pass = raw_input('Enter manager password: ')
	monitor_pass = raw_input('Enter monitor password:')
	voice = ND + 40
	video = ND + 30
	manag = ND + 240
	manag_ip = switch_num + 10

	print "####################### A3100 #########################"
	print   "   "


	''' Hostname '''


	if ND == 1 :
		subs = switch_num + 100
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 2 :
		subs = switch_num + 200
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 3 :
		subs = switch_num + 300
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 4 :
		subs = switch_num + 400
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 5 :
		subs = switch_num + 500
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 6 :
		subs = switch_num + 600
		print 'sysname ND%s-E%s'%(ND, subs)
	else:
		print ' wrong ND number '
	print '#'

	'''main entries for the switch '''

	print "telnet server enable "
	print "ssh server enable"
	print 'ip https enable '
	print 'ip http enable '
	print '#'
	print 'stp enable'
	print '#'
	print 'info-center loghost 10.0.10.6'
	print '#'
	print 'user-interface vty 0 15'
	print '  authentication-mode scheme'
	print '#'

	''' vlans configuration '''

	print 'vlan %s' %(video)
	print ' name video_vlan' 
	print '#'
	print 'vlan %s' %(voice)
	print ' name Voice_vlan' 
	print '#'
	print 'vlan %s' %(manag)
	print ' name Management-Vlan'
	print '#'
	print 'vlan %s' %(defult_vlan)
	print ' name %s' %(defult_vlan_name)
	print '#'

	""" this section will configure the bridge aggregation link """

	print "interface Bridge-Aggregation1"
	print ' description Connection-to-ND%s' %(ND)
	print ' port link-type trunk'
	print ' port trunk permit vlan all'
	print ' port trunk pvid vlan %s' %(manag)
	print ' link-aggregation mode dynamic'
	print '#'
	''' this section will configure the interface vlan '''
	print 'interface Vlan-interface%s' %(manag)
	print ' ip address 10.0.%s.%s 255.255.255.0' %(manag, manag_ip)
	print '#'
	''' user profiles for your edge switch '''
	print 'local-user manager'
	print ' password cipher %s' %(manager_pass)
	print ' authorization-attribute level 3'
	print ' service-type ssh telnet'
	print '  service-type web'
	print 'local-user monitor'
	print ' password cipher %s' %(monitor_pass)
	print ' authorization-attribute level 1'
	print ' service-type telnet'
	print '  service-type web'
	print '#'
	''' your access interfaces '''
	for i in range(1, 24):
		print "interface Ethernet 1/0/%d" %(i)
		print "port link-type hybrid"
		print 'undo port hybrid vlan 1'
		print 'port hybrid vlan %s untagged' %(defult_vlan)
		print 'port hybrid pvid vlan %s' %(defult_vlan)
		print 'voice vlan %s enable' %(voice)
		print 'poe enable'
		print 'stp edged-port enable'
		print '#'
	''' your management interface '''
	print 'interface Ethernet 1/0/24'
	print ' description Switch-Management-Port'
	print ' port access vlan %s' %(manag)
	print ' stp edged-port enable'
	print '#'

	''' your fiber uplink '''

	for g in range(25, 27):
		print 'interface GigabitEthernet 1/0/%d' %(g)
		print ' port link-type trunk'
		print ' port trunk permit vlan all'
		print ' port trunk pvid vlan %s' %(manag)
		print ' combo fiber enable'
		print ' port link-aggregation group 1'
		print '#'

	''' now defult route to your ND '''
	print 'ip route-static 0.0.0.0 0.0.0.0 10.0.%s.1' %(manag)
	print "#"
	
def switch_3600():
	import sys
	
	class Logger(object):
		def __init__(self, filename="Default.log"):
			self.terminal = sys.stdout
			self.log = open(filename, "a")

		def write(self, message):
			self.terminal.write(message)
			self.log.write(message)

	sys.stdout = Logger("3600.txt")

	print   "          ###############################################################"
	print   "          #                          HP A3600                           #"
	print   "          ###############################################################"
	print   "   "

	defult_vlan = int(raw_input('Enter your defult Vlan: '))
	defult_vlan_name = raw_input('Enter your defult Vlan name: ')
	switch_num = int(raw_input('Enter Switch Num: '))  # The Switch number
	ND = int(raw_input ('Enter ND Number: '))          #network distribution switch from 1 to 6 
	Super_pass = raw_input('Enter Super password: ')
	manager_pass = raw_input('Enter manager password: ')
	monitor_pass = raw_input('Enter monitor password:')
	voice = ND + 40
	video = ND + 30
	manag = ND + 240
	manag_ip = switch_num + 10

	print "####################### A3600 #########################"
	print   "   "
  

	''' Hostname '''
	if ND == 1 :
		subs = switch_num + 100
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 2 :
		subs = switch_num + 200
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 3 :
		subs = switch_num + 300
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 4 :
		subs = switch_num + 400
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 5 :
		subs = switch_num + 500
		print 'sysname ND%s-E%s'%(ND, subs)
	elif ND == 6 :
		subs = switch_num + 600
		print 'sysname ND%s-E%s'%(ND, subs)
	else:
		print ' wrong ND number '
	print '#'

	'''main entries for the switch '''

	print "telnet server enable "
	print "ssh server enable"
	print 'ip https enable '
	print 'ip http enable '
	print '#'
	print 'stp enable'
	print '#'
	print 'info-center loghost 10.0.10.6'
	print '#'
	print 'user-interface vty 0 15'
	print '  authentication-mode scheme'
	print '#'

	''' vlans configuration '''

	print 'vlan %s' %(video)
	print ' name video_vlan' 
	print '#'
	print 'vlan %s' %(voice)
	print ' name Voice_vlan' 
	print '#'
	print 'vlan %s' %(manag)
	print ' name Management-Vlan'
	print '#'
	print 'vlan %s' %(defult_vlan)
	print ' name %s' %(defult_vlan_name)
	print '#'

	""" this section will configure the bridge aggregation link """

	print "interface Bridge-Aggregation1"
	print ' description Connection-to-ND%s' %(ND)
	print ' port link-type trunk'
	print ' port trunk permit vlan all'
	print ' port trunk pvid vlan %s' %(manag)
	print ' link-aggregation mode dynamic'
	print '#'
	''' this section will configure the interface vlan '''
	print 'interface Vlan-interface%s' %(manag)
	print ' ip address 10.0.%s.%s 255.255.255.0' %(manag, manag_ip)
	print '#'
	''' user profiles for your edge switch '''
	print 'local-user manager'
	print ' password cipher %s' %(manager_pass)
	print ' authorization-attribute level 3'
	print ' service-type ssh telnet'
	print '  service-type web'
	print 'local-user monitor'
	print ' password cipher %s' %(monitor_pass)
	print ' authorization-attribute level 1'
	print ' service-type telnet'
	print '  service-type web'
	print '#'
	''' your access interfaces '''
	for i in range(1, 48):
		print "interface Ethernet 1/0/%d" %(i)
		print "port link-type hybrid"
		print 'undo port hybrid vlan 1'
		print 'port hybrid vlan %s untagged' %(defult_vlan)
		print 'port hybrid pvid vlan %s' %(defult_vlan)
		print 'voice vlan %s enable' %(voice)
		print 'poe enable'
		print 'stp edged-port enable'
		print '#'
	''' your management interface '''
	print 'interface Ethernet 1/0/48'
	print ' description Switch-Management-Port'
	print ' port access vlan %s' %(manag)
	print ' stp edged-port enable'
	print '#'

	''' your fiber uplink '''

	for g in range(51,53):
		print 'interface GigabitEthernet 1/0/%d' %(g)
		print ' port link-type trunk'
		print ' port trunk permit vlan all'
		print ' port trunk pvid vlan %s' %(manag)
		print ' combo fiber enable'
		print ' port link-aggregation group 1'
		print '#'

	''' now defult route to your ND '''
	print 'ip route-static 0.0.0.0 0.0.0.0 10.0.%s.1' %(manag)
	print "#"
if switch_type == 5120:
	print switch_5120()
elif switch_type == 3100:
	print switch_3100()
elif switch_type == 3600:
	print switch_3600()
else:
	print '	only supported switches are 3100, 3600, 5120'
	
time.sleep(50) 

