#Your SSH client configuration must be configured to use the
# private key ~/.ssh/school
#Your SSH client configuration must be configured
#to refuse to authenticate using a password
$public_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC4yljFImN7aPWgBSeXvTyF0Q9uDVYCiY+//BXPdG6E3+cv01lIGaYuWOAHBwodByXxuS2jIbr1kE2Lbe62hhGE2VchhSuxyExZ2bXUZ/mj35AebuIaeVueV9pwQnzDLpKxcVF2QrFaAV75kBVytAaZn4nMV91Na8J35W/yXnOrtj/4g9sMeO2lWkz1acTfri+Zz9z4aFsEV3ulqmbuDkHkZt0S9BjKsQ2ezdnKvAzULpPUun5OjayDhCxuNhjexsAXe0bmWltpu05SWdazmTlwBdR6a0r8I2vSnlSINUOLaykuhtSWJfk34hVmGW4uCHmgB9g9YQNw0JKM36v1aG/KtG95SAtO8kxVbDmcbzQHLVuzr6xkV8w87XGJPL6WeFhHa3BbpepY24OEUR6oMOczeyDt0E/y/jEKHLGowfiUhyb15bxOHKj4o6xEMXAwd8T72ovBpr2nunrZWQkPGAvqbz5+qQXo3LM9op4iNtbdIFvc+2wsML97VeJsApM54xE= vagrant@ubuntu-focal'

class ssh_config {
	ssh_authorized_key {'ubuntu@54.237.110.211':
		ensure => present,
		user => '60552-web-01',
		options => {
			'PasswordAuthentication' => 'no'},
		type => 'ssh-rsa',
		path => '~/.ssh/school',
		key => $public_key,
}
} 
