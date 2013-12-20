VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  #CentOS 6.0
  config.vm.define "centos6" do |centos6_config|
    centos6_config.vm.box = "centos_6_x64"
    centos6_config.vm.box_url = "file:///Users/jolly_rojer/Projects/Cometera/vagrant-boxes/centos_6_x64.box"
    centos6_config.vm.hostname = "centos6.qubell.int"
    centos6_config.vm.network "public_network", :bridge => 'en0: Wi-Fi (AirPort)'
    centos6_config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "1024"]
      vb.customize ["modifyvm", :id, "--cpus", "1"]
    end
    centos6_config.vm.provision "chef_solo" do |chef| 
      chef.log_level = "debug"
      chef.cookbooks_path = "cookbooks"
      chef.add_recipe "zookeeper-component"
    end
  end
end
